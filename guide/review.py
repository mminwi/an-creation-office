"""AN Creation review pages: dated web pages per invention, never overwritten.

Each new page goes in its own dated folder under Your files/Review/, with a copy of its
source and every picture and document it shows. Old pages are never changed. The index
(Review/index.html) shows Your list (the action log) first, then every page in the order made,
with "today" on top, and a history of every picture and document ever shown.

  python review.py new   "AN-Creation/Fishing Lure" path/to/page.json [--slug timeline] [--today]
  python review.py today "AN-Creation/Fishing Lure" 261007-1430-timeline
  python review.py index "AN-Creation/Fishing Lure"
  python review.py serve "AN-Creation/Fishing Lure" [--port 8765]

In a GitHub repository (the cloud office), pages are also written as Markdown
(README.md in each page folder, and Review/README.md as the index) because GitHub shows
Markdown but not HTML, and documents are linked instead of copied: Git keeps every version.

Standard library only.
"""
import argparse
import csv
import datetime as dt
import html
import http.server
import json
import os
import re
import shutil
import socketserver
from pathlib import Path
from urllib.parse import quote

PICTURES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
DOCUMENTS = {".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md", ".csv", ".step", ".stp", ".stl"}
MAX_COPY_MB = 100  # bigger files are linked, not copied
FOLDER_RE = re.compile(r"^\d{6}-\d{4}-[a-z0-9-]+$")


def esc(text):
    return html.escape(str(text or ""))


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")[:40] or "page"


CSS = """
:root{--bg:#f7f5f0;--fg:#1d1d1b;--muted:#6b6862;--line:#d9d4c9;--accent:#1f5f8b;--risk:#a33a1f;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#171716;--fg:#ecebe6;--muted:#a19d94;--line:#3a3833;--accent:#7fb6dc;--risk:#e58a6f;--card:#212120}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
header{padding:20px 16px;border-bottom:1px solid var(--line)}header h1{margin:0;font-size:1.5rem}
header p{margin:4px 0 0;color:var(--muted)}nav{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px}
nav a,a{color:var(--accent)}nav a{text-decoration:none}main{max-width:960px;margin:0 auto;padding:0 16px 48px}
section{margin-top:32px}h2{font-size:1.2rem;border-bottom:1px solid var(--line);padding-bottom:4px}
table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600}
.timeline{list-style:none;padding:0;border-left:3px solid var(--line);margin-left:8px}
.timeline li{position:relative;padding:6px 0 10px 18px}.timeline li::before{content:"";position:absolute;left:-8px;top:12px;width:13px;height:13px;border-radius:50%;background:var(--accent)}
.timeline li.inventor-date::before{background:var(--fg)}.timeline li.lead-time::before{background:var(--muted)}
.date{font-weight:600;margin-right:10px}.kind,.muted{color:var(--muted);font-size:.85rem}.kind{margin-left:8px}.risk{color:var(--risk);font-size:.9rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px;margin:16px 0}
.weight{font-size:.75rem;font-weight:600;color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:1px 6px;vertical-align:middle}
.slide{display:none}.slide.on{display:block}.slide img{max-width:100%;border-radius:6px}
.deck-nav{display:flex;gap:12px;align-items:center;margin-top:8px}.deck-nav button{padding:6px 14px;border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:6px;cursor:pointer}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}
.gallery img{width:100%;height:130px;object-fit:cover;border-radius:6px}figcaption{font-size:.85rem;color:var(--muted)}
.pages li{margin:6px 0}.today{border-left:4px solid var(--accent)}
"""

JS = """
document.querySelectorAll('.topic').forEach(t=>{const s=[...t.querySelectorAll('.slide')];let i=0;
const c=t.querySelector('.count');const show=()=>{s.forEach((x,k)=>x.classList.toggle('on',k===i));if(c)c.textContent=s.length?(i+1)+' of '+s.length:''};
t.querySelectorAll('.deck-nav button').forEach(b=>b.onclick=()=>{i=Math.max(0,Math.min(s.length-1,i+ +b.dataset.step));show()});show()});
"""


def shell(title, subtitle, nav, body, script=True):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{CSS}</style></head><body>'
            f'<header><h1>{esc(title)}</h1><p>{subtitle}</p><nav>{nav}</nav></header>'
            f'<main>{body}</main>{"<script>" + JS + "</script>" if script else ""}</body></html>')


# ---------- copying files into the dated folder ----------

def in_git(path):
    """True when the folder is inside a Git repository (the cloud office on GitHub)."""
    here = Path(path).resolve()
    return any((p / ".git").exists() for p in [here, *here.parents])


class Copier:
    """Copies each source file once into <page>/files/ and returns the link to use.
    In a Git repository it links to the file where it is instead (Git keeps every version)."""

    def __init__(self, page_dir, your_files, link_only=False):
        self.page_dir = page_dir
        self.files_dir = page_dir / "files"
        self.your_files = your_files
        self.link_only = link_only
        self.done = {}

    def link(self, src):
        src = Path(src)
        if src in self.done:
            return self.done[src]
        if not src.exists():
            self.done[src] = ""
        elif self.link_only:
            self.done[src] = quote(os.path.relpath(src, self.page_dir).replace(os.sep, "/"))
        elif src.stat().st_size > MAX_COPY_MB * 1024 * 1024:
            self.done[src] = "../../" + quote(str(src.relative_to(self.your_files)).replace("\\", "/"))
        else:
            self.files_dir.mkdir(exist_ok=True)
            dest = self.files_dir / src.name
            n = 2
            while dest.exists():
                dest = self.files_dir / f"{src.stem}-{n}{src.suffix}"
                n += 1
            shutil.copy2(src, dest)
            self.done[src] = "files/" + quote(dest.name)
        return self.done[src]


# ---------- page sections ----------

def section_status(page):
    rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in page.get("status", {}).items())
    return f'<section id="status"><h2>Where it stands</h2><table>{rows}</table></section>' if rows else ""


def section_timeline(page):
    items = sorted(page.get("timeline", []), key=lambda i: i.get("date", ""))
    if not items:
        return ""
    lis = "".join(
        f'<li class="{esc(i.get("kind", "step"))}"><span class="date">{esc(i.get("date"))}</span>'
        f'{esc(i.get("what"))}<span class="kind">{esc(i.get("kind", "step")).replace("-", " ")}</span>'
        + (f'<div class="risk">Risk: {esc(i["risk"])}</div>' if i.get("risk") else "") + "</li>"
        for i in items)
    return f'<section id="timeline"><h2>Timeline</h2><ol class="timeline">{lis}</ol></section>'


def section_risks(page):
    rows = "".join(f"<tr><td>{esc(r.get('risk'))}</td><td>{esc(r.get('cost'))}</td>"
                   f"<td>{esc(r.get('when'))}</td><td>{esc(r.get('time_left'))}</td></tr>"
                   for r in page.get("risks", []))
    return ('<section id="risks"><h2>Risks so far</h2><table><tr><th>What could go wrong</th><th>Cost</th>'
            f'<th>When it bites</th><th>Time left</th></tr>{rows}</table></section>') if rows else ""


def section_topics(page, copier):
    nav, blocks = [], []
    for t in page.get("topics", []):
        tid = esc(t.get("id") or slugify(t.get("title")))
        nav.append(f'<a href="#topic-{tid}">{esc(t.get("title"))}</a>')
        slides = []
        for n, sl in enumerate(t.get("slides", []), 1):
            src = copier.link(copier.your_files / sl["image"]) if sl.get("image") else ""
            img = f'<img src="{src}" alt="">' if src else ""
            bullets = "".join(f"<li>{esc(b)}</li>" for b in sl.get("bullets", []))
            links = "".join(f'<li><a href="{esc(l["url"])}" target="_blank">{esc(l["label"])}</a></li>'
                            for l in sl.get("links", []))
            slides.append(f'<div class="slide"><h3>{esc(sl.get("title"))}</h3>{img}<ul>{bullets}</ul>'
                          + (f"<ul>{links}</ul>" if links else "") + "</div>")
        weight = f' <span class="weight">{esc(t["weight"])}</span>' if t.get("weight") else ""
        blocks.append(f'<article class="card topic" id="topic-{tid}"><h2>{esc(t.get("title"))}{weight}</h2>'
                      f'<p>{esc(t.get("summary"))}</p>{"".join(slides)}'
                      '<div class="deck-nav"><button data-step="-1">Back</button><span class="count"></span>'
                      '<button data-step="1">Next</button></div></article>')
    body = f'<section id="topics"><h2>To talk over</h2>{"".join(blocks)}</section>' if blocks else ""
    return " ".join(nav), body


def section_files(page, copier):
    """Pictures and documents: the ones page.json names, or everything in Your files if it says "all"."""
    wanted = page.get("files", "all")
    if wanted == "all":
        paths = [p for p in sorted(copier.your_files.rglob("*")) if p.is_file()
                 and "Review" not in p.relative_to(copier.your_files).parts]
    else:
        paths = [copier.your_files / f for f in wanted]
    pics, docs = [], []
    for p in paths:
        ext = p.suffix.lower()
        if ext in PICTURES or ext in DOCUMENTS:
            href = copier.link(p)
            if href:
                (pics if ext in PICTURES else docs).append((p.name, href))
    out = ""
    if pics:
        out += ('<section id="pictures"><h2>Pictures</h2><div class="gallery">' + "".join(
            f'<figure><a href="{h}" target="_blank"><img src="{h}" alt=""></a><figcaption>{esc(n)}</figcaption></figure>'
            for n, h in pics) + "</div></section>")
    if docs:
        out += ('<section id="documents"><h2>Documents</h2><ul>' + "".join(
            f'<li><a href="{h}" target="_blank">{esc(n)}</a></li>' for n, h in docs) + "</ul></section>")
    return out


# ---------- Markdown (for GitHub) ----------

def md_cell(text):
    return str(text or "").replace("|", "/").replace("\n", " ")


def md_page(page, copier, made, shown):
    out = [f"# {page.get('title') or 'Review'}", "", f"_Made {made}. This page is never changed. [All pages](../README.md)_", ""]
    if page.get("summary"):
        out += [page["summary"], ""]
    if page.get("status"):
        out += ["## Where it stands", "", "| | |", "|---|---|"]
        out += [f"| **{md_cell(k)}** | {md_cell(v)} |" for k, v in page["status"].items()] + [""]
    items = sorted(page.get("timeline", []), key=lambda i: i.get("date", ""))
    if items:
        out += ["## Timeline", ""]
        for i in items:
            line = f"- **{i.get('date', '')}** {i.get('what', '')} _({str(i.get('kind', 'step')).replace('-', ' ')})_"
            out.append(line + (f" Risk: {i['risk']}" if i.get("risk") else ""))
        out.append("")
    if page.get("risks"):
        out += ["## Risks so far", "", "| What could go wrong | Cost | When it bites | Time left |", "|---|---|---|---|"]
        out += [f"| {md_cell(r.get('risk'))} | {md_cell(r.get('cost'))} | {md_cell(r.get('when'))} | {md_cell(r.get('time_left'))} |"
                for r in page["risks"]] + [""]
    for tp in page.get("topics", []):
        out += [f"## {tp.get('title', '')}" + (f" ({tp['weight']})" if tp.get("weight") else ""), ""]
        if tp.get("summary"):
            out += [tp["summary"], ""]
        for sl in tp.get("slides", []):
            if sl.get("title"):
                out += [f"### {sl['title']}", ""]
            if sl.get("image"):
                href = copier.link(copier.your_files / sl["image"])
                if href:
                    out += [f"![{sl.get('title', '')}]({href})", ""]
            out += [f"- {b}" for b in sl.get("bullets", [])]
            out += [f"- [{lk['label']}]({lk['url']})" for lk in sl.get("links", [])]
            out.append("")
    wanted = page.get("files", "all")
    if wanted == "all":
        paths = [p for p in sorted(copier.your_files.rglob("*")) if p.is_file()
                 and "Review" not in p.relative_to(copier.your_files).parts]
    else:
        paths = [copier.your_files / f for f in wanted]
    pics, docs = [], []
    for p in paths:
        ext = p.suffix.lower()
        if ext in PICTURES or ext in DOCUMENTS:
            href = copier.link(p)
            if href:
                (pics if ext in PICTURES else docs).append((p.name, href))
    if pics:
        out += ["## Pictures", ""] + [f"![{n}]({h})" for n, h in pics] + [""]
    if docs:
        out += ["## Documents", ""] + [f"- [{n}]({h})" for n, h in docs] + [""]
    shown.extend(pics + docs)
    return "\n".join(out)


def md_index(invention, root, pages, metas, today):
    out = [f"# {invention.name}: review pages", "", "_Everything we've put up for you. Old pages are kept as they were._", ""]
    path = invention / "Soren's files" / "actions.csv"
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as fh:
            rows = [r for r in csv.DictReader(fh) if (r.get("ID") or "").strip()]
        mine = [r for r in rows if (r.get("Status") or "").strip().lower() == "open"
                and (r.get("Who") or "").strip().lower() in ("you", "inventor", "the inventor")]
        out += ["## Your list", ""]
        out += [f"- **{r['ID']}** {r.get('Action', '')}" + (f" (due {r['Due']})" if r.get("Due") else "") for r in mine] or ["Nothing on your list right now."]
        out.append("")
    if today:
        m = metas[today]
        out += ["## What we're talking about today", "", f"**[{m.get('title')}]({quote(today)}/README.md)**", "", m.get("summary", ""), ""]
    if pages:
        out += ["## Every page, in the order made", ""]
        out += [f"1. [{metas[p.name].get('title')}]({quote(p.name)}/README.md) _{metas[p.name].get('made', p.name)}_" for p in pages] + [""]
    shown = []
    for p in reversed(pages):
        for n, h in metas[p.name].get("shown", []):
            shown.append(f"- [{n}]({quote(p.name)}/{h}) _{metas[p.name].get('made', p.name)}_")
    if shown:
        out += ["## Every picture and document shown", ""] + shown + [""]
    (root / "README.md").write_text("\n".join(out), encoding="utf-8")


# ---------- commands ----------

def review_root(invention):
    return Path(invention).resolve() / "Your files" / "Review"


def new_page(invention, page_json, slug=None, today=False):
    invention = Path(invention).resolve()
    your_files = invention / "Your files"
    page = json.loads(Path(page_json).read_text(encoding="utf-8"))
    stamp = dt.datetime.now().strftime("%y%m%d-%H%M")
    name = f"{stamp}-{slugify(slug or page.get('title') or 'page')}"
    page_dir = review_root(invention) / name
    n = 2
    while page_dir.exists():  # never write into an existing page
        page_dir = review_root(invention) / f"{name}-{n}"
        n += 1
    page_dir.mkdir(parents=True)
    shutil.copy2(page_json, page_dir / "page.json")
    git = in_git(invention)
    copier = Copier(page_dir, your_files, link_only=git)
    topic_nav, topics = section_topics(page, copier)
    body = (section_status(page) + section_timeline(page) + section_risks(page)
            + topics + section_files(page, copier))
    nav = '<a href="../index.html">All pages</a> ' + " ".join(
        f'<a href="#{i}">{n}</a>' for i, n in [("status", "Status"), ("timeline", "Timeline"),
                                               ("risks", "Risks"), ("pictures", "Pictures"),
                                               ("documents", "Documents")] if f'id="{i}"' in body) + " " + topic_nav
    made = dt.datetime.now().strftime("%d %b %Y, %H:%M")
    (page_dir / "index.html").write_text(
        shell(page.get("title") or invention.name, f"Made {made}. This page is never changed.", nav,
              body or "<p>Nothing to show yet.</p>"), encoding="utf-8")
    meta = {"title": page.get("title") or name, "summary": page.get("summary", ""), "made": made}
    if git:
        shown = []
        (page_dir / "README.md").write_text(md_page(page, copier, made, shown), encoding="utf-8")
        meta["shown"] = shown
    (page_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    if today:
        set_today(invention, page_dir.name)
    else:
        build_index(invention)
    return page_dir


def set_today(invention, folder_name):
    root = review_root(invention)
    if not (root / folder_name / "index.html").exists():
        raise SystemExit(f"No page {folder_name}")
    (root / "today.txt").write_text(folder_name, encoding="utf-8")
    build_index(invention)


def actions_section(invention):
    """Your list: the inventor's open actions, what they're waiting on, and what was done recently (sop-action-log.txt)."""
    path = Path(invention) / "Soren's files" / "actions.csv"
    if not path.exists():
        return ""
    with path.open(encoding="utf-8-sig", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if (r.get("ID") or "").strip()]
    today = dt.date.today().isoformat()
    st = lambda r: (r.get("Status") or "").strip().lower()
    you = lambda r: (r.get("Who") or "").strip().lower() in ("you", "inventor", "the inventor")
    mine = [r for r in rows if st(r) == "open" and you(r)]
    waiting = [r for r in rows if st(r) == "waiting" or (st(r) == "open" and not you(r))]
    done = sorted((r for r in rows if st(r) == "done"), key=lambda r: r.get("Closed") or "", reverse=True)[:5]

    def due(r):
        d = (r.get("Due") or "").strip()
        if not d:
            return ""
        return f'<span class="risk">{esc(d)} overdue</span>' if d < today else esc(d)

    out = '<section class="card today" id="your-list"><h2>Your list</h2>'
    if mine:
        out += ("<table><tr><th>ID</th><th>What to do</th><th>Due</th><th>From</th></tr>" + "".join(
            f"<tr><td>{esc(r['ID'])}</td><td>{esc(r.get('Action'))}</td><td>{due(r)}</td><td>{esc(r.get('Why / from'))}</td></tr>" for r in mine) + "</table>")
    else:
        out += "<p>Nothing on your list right now.</p>"
    if waiting:
        out += ("<h3>Waiting on others</h3><table><tr><th>ID</th><th>What</th><th>Who</th><th>Due</th></tr>" + "".join(
            f"<tr><td>{esc(r['ID'])}</td><td>{esc(r.get('Action'))}</td><td>{esc(r.get('Who'))}</td><td>{due(r)}</td></tr>" for r in waiting) + "</table>")
    if done:
        out += ("<h3>Done recently</h3><table><tr><th>ID</th><th>What</th><th>How</th><th>Closed</th></tr>" + "".join(
            f"<tr><td>{esc(r['ID'])}</td><td>{esc(r.get('Action'))}</td><td>{esc(r.get('Done how'))}</td><td>{esc(r.get('Closed'))}</td></tr>" for r in done) + "</table>")
    out += f'<p class="muted">The full log, including dropped items, is in Your files/Action log. {len(rows)} actions so far.</p></section>'
    return out


def build_index(invention):
    """The index only lists pages. It is the one file that is rebuilt."""
    invention = Path(invention).resolve()
    root = review_root(invention)
    root.mkdir(parents=True, exist_ok=True)
    pages = sorted(p for p in root.iterdir() if p.is_dir() and FOLDER_RE.match(p.name))
    metas = {}
    for p in pages:
        try:
            metas[p.name] = json.loads((p / "meta.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            metas[p.name] = {"title": p.name}
    today = (root / "today.txt").read_text(encoding="utf-8").strip() if (root / "today.txt").exists() else ""
    if today not in metas:
        today = pages[-1].name if pages else ""

    body = actions_section(invention)
    if today:
        m = metas[today]
        body += (f'<section class="card today"><h2>What we\'re talking about today</h2>'
                 f'<p><a href="{quote(today)}/index.html"><strong>{esc(m.get("title"))}</strong></a></p>'
                 f'<p>{esc(m.get("summary"))}</p><p class="muted">{esc(m.get("made"))}</p></section>')
    body += ('<section id="pages"><h2>Every page, in the order made</h2><ol class="pages">' + "".join(
        f'<li><a href="{quote(p.name)}/index.html">{esc(metas[p.name].get("title"))}</a> '
        f'<span class="muted">{esc(metas[p.name].get("made", p.name))}</span></li>' for p in pages)
        + "</ol></section>") if pages else "<p>No pages yet.</p>"

    pics, docs = [], []
    for p in reversed(pages):  # newest first
        files = p / "files"
        if files.is_dir():
            for f in sorted(files.iterdir()):
                href = f"{quote(p.name)}/files/{quote(f.name)}"
                label = metas[p.name].get("made", p.name)
                if f.suffix.lower() in PICTURES:
                    pics.append((f.name, href, label))
                elif f.suffix.lower() in DOCUMENTS:
                    docs.append((f.name, href, label))
    if pics:
        body += ('<section id="pictures"><h2>Every picture shown</h2><div class="gallery">' + "".join(
            f'<figure><a href="{h}" target="_blank"><img src="{h}" alt=""></a>'
            f'<figcaption>{esc(n)}<br>{esc(l)}</figcaption></figure>' for n, h, l in pics) + "</div></section>")
    if docs:
        body += ('<section id="documents"><h2>Every document shown</h2><ul>' + "".join(
            f'<li><a href="{h}" target="_blank">{esc(n)}</a> <span class="muted">{esc(l)}</span></li>'
            for n, h, l in docs) + "</ul></section>")

    if in_git(invention):
        md_index(invention, root, pages, metas, today)
    nav = '<a href="#your-list">Your list</a> <a href="#pages">Pages</a> <a href="#pictures">Pictures</a> <a href="#documents">Documents</a>'
    (root / "index.html").write_text(
        shell(invention.name, "Everything we've put up for you. Old pages are kept as they were.", nav, body,
              script=False), encoding="utf-8")
    return root / "index.html"


def serve(invention, port):
    build_index(invention)
    root = Path(invention).resolve() / "Your files"
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(root), **k)
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Review pages: http://127.0.0.1:{port}/Review/index.html", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a_new = sub.add_parser("new"); a_new.add_argument("invention"); a_new.add_argument("page_json")
    a_new.add_argument("--slug"); a_new.add_argument("--today", action="store_true")
    a_today = sub.add_parser("today"); a_today.add_argument("invention"); a_today.add_argument("folder")
    a_index = sub.add_parser("index"); a_index.add_argument("invention")
    a_serve = sub.add_parser("serve"); a_serve.add_argument("invention"); a_serve.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()
    if a.cmd == "new":
        print(new_page(a.invention, a.page_json, a.slug, a.today) / "index.html")
    elif a.cmd == "today":
        set_today(a.invention, a.folder)
    elif a.cmd == "index":
        print(build_index(a.invention))
    else:
        serve(a.invention, a.port)
