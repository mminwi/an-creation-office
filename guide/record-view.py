#!/usr/bin/env python3
"""record-view.py: readable, printable copies of the project and business record.

Usage: python3 record-view.py <folder> [<output folder>]

Reads the record sheets it knows in <folder> (cost sheet, risk table, action log,
decision log, charter, compliance matrix, spending register, expense ledger,
trip log, correspondence index) and writes one HTML page per sheet, plus
index.html, into <output folder> (default: <folder>/views). The inventor reads
these; the CSV files stay the record. Procedures:
https://ancreationoffice.com/sop-project-record.txt and
https://ancreationoffice.com/sop-business-record.txt
"""
import csv
import html
import pathlib
import re
import sys

# file: (title, which record, columns to show (None = all), right-aligned columns)
SHEETS = {
    "project-charter.txt": ("Project charter", "Project record", None, ()),
    "cost-sheet.csv": ("Cost sheet: the costed bill of materials", "Project record",
                       ["part number", "part", "qty", "make or buy", "what it is", "material cost", "process cost",
                        "tooling", "amortization", "unit cost", "running total", "share of total"],
                       ("qty", "material cost", "process cost", "tooling", "amortization", "unit cost", "running total", "share of total")),
    "risk-table.csv": ("Risk table: simplified FMEA, severity first", "Project record", None, ("S", "O", "D", "RPN")),
    "actions.csv": ("Action log", "Project record", ["ID", "Opened", "Action", "Who", "Due", "Status"], ()),
    "decision-log.csv": ("Decision log", "Project record", None, ()),
    "spending.csv": ("Spending register", "Project record", ["date", "stage", "what it was", "vendor or who", "amount", "committed or paid", "paid from", "running total"], ("amount", "running total")),
    "compliance-matrix.csv": ("Requirements, traced to their sources", "Project record",
                              ["ID", "Requirement", "Source", "Source status", "Pass level", "Status", "Critical"], ()),
    "expenses.csv": ("Expense ledger", "Business record", ["date", "paid to", "what it was", "business purpose", "tax category", "amount", "paid from", "receipt file"], ("amount",)),
    "trips.csv": ("Trip and mileage log", "Business record", ["trip", "date", "to (place and address)", "who or what", "business purpose", "start odometer", "end odometer", "business miles"], ("start odometer", "end odometer", "business miles")),
    "correspondence.csv": ("Correspondence log", "Business record", ["date", "folder", "direction", "with", "organization", "what was conveyed", "sent or received"], ()),
}

CSS = """
:root { color-scheme: light; }
body { margin: 0; background: #e9e6df; font: 14px/1.45 "Inter", "Segoe UI", Arial, sans-serif; color: #1d2427; }
.page { max-width: 1180px; margin: 24px auto; background: #fff; border: 1px solid #d7d2c6; border-radius: 6px; padding: 28px 32px 36px; }
.top { display: flex; justify-content: space-between; gap: 16px; border-bottom: 3px solid #315f5c; padding-bottom: 10px; margin-bottom: 14px; }
.top b { font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: #315f5c; }
.top span { font-size: 12px; color: #6b7275; text-align: right; }
h1 { font-size: 22px; margin: 0 0 4px; }
.sub { color: #5b6467; margin: 0 0 16px; }
table { border-collapse: collapse; width: 100%; font-size: 12.5px; }
th { background: #f1eee6; text-align: left; font-weight: 650; border: 1px solid #d9d4c8; padding: 6px 7px; vertical-align: bottom; }
td { border: 1px solid #e1ddd3; padding: 6px 7px; vertical-align: top; }
tr:nth-child(even) td { background: #fbfaf7; }
td.n { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
td.nw { white-space: nowrap; }
tr.action td:first-child { border-top-color: transparent; }
tr.action td:nth-child(2) { padding-left: 22px; color: #3e4a4d; }
td.hi { background: #f6dcd3 !important; font-weight: 700; }
.foot { margin-top: 14px; font-size: 12px; color: #6b7275; }
.charter h2 { font-size: 15px; margin: 18px 0 4px; color: #315f5c; }
.charter p { margin: 0 0 6px; }
ul.idx li { margin: 4px 0; }
@media print { body { background: #fff; } .page { border: 0; margin: 0; max-width: none; } }
"""


def page(title, kind, project, body, note):
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body><div class='page'>"
            f"<div class='top'><b>AN Creation Office · {html.escape(kind)}</b><span>{html.escape(project)}</span></div>"
            f"<h1>{html.escape(title)}</h1>{body}<p class='foot'>{note}</p></div></body></html>")


def table(rows, cols, right, risk=False):
    head = rows[0]
    idx = [head.index(c) for c in (cols or head) if c in head]
    out = ["<table><thead><tr>" + "".join(f"<th>{html.escape(head[i])}</th>" for i in idx) + "</tr></thead><tbody>"]
    for r in rows[1:]:
        if not any(x.strip() for x in r):
            continue
        cls = " class='action'" if risk and not r[0].strip() else ""
        cells = []
        for i in idx:
            v = r[i] if i < len(r) else ""
            c = []
            if head[i] in right:
                c.append("n")
            elif re.fullmatch(r"\d{4}-\d\d-\d\d|[A-Z]+-\d+|T-\d+|ODO-\d+", v.strip()):
                c.append("nw")
            if risk and head[i] == "S" and v.strip().isdigit() and int(v) >= 8:
                c.append("hi")
            cells.append(f"<td{' class=' + repr(' '.join(c)) if c else ''}>{html.escape(v)}</td>")
        out.append(f"<tr{cls}>" + "".join(cells) + "</tr>")
    return "".join(out) + "</tbody></table>"


def charter(text):
    lines = text.strip().splitlines()
    out = [f"<p class='sub'>{html.escape(lines[1]) if len(lines) > 1 else ''}</p><div class='charter'>"]
    for line in lines[2:]:
        if not line.strip():
            continue
        if re.match(r"^\d+\. [A-Z][A-Z ,&/-]+$", line.strip()):
            out.append(f"<h2>{html.escape(line.strip())}</h2>")
        else:
            out.append(f"<p>{html.escape(line)}</p>")
    return "".join(out) + "</div>"


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    src = pathlib.Path(argv[0])
    dst = pathlib.Path(argv[1]) if len(argv) > 1 else src / "views"
    dst.mkdir(parents=True, exist_ok=True)
    project = src.resolve().name
    charter_file = src / "project-charter.txt"
    if charter_file.exists():
        first = charter_file.read_text(encoding="utf-8").splitlines()[0]
        project = first.replace("Project charter.", "").strip() or project
    note = "Readable copy built by record-view.py from the sheet of the same name. The sheet is the record."
    made = []
    for name, (title, kind, cols, right) in SHEETS.items():
        f = src / name
        if not f.exists():
            continue
        if name.endswith(".txt"):
            body = charter(f.read_text(encoding="utf-8"))
        else:
            with open(f, newline="", encoding="utf-8-sig") as fh:
                rows = list(csv.reader(fh))
            body = table(rows, cols, right, risk=name == "risk-table.csv")
            if name == "risk-table.csv":
                body = "<p class='sub'>Each failure mode with its first scores; indented lines are the actions taken and the new scores. Severity 8 and up is shaded.</p>" + body
        out = dst / (pathlib.Path(name).stem + ".html")
        out.write_text(page(title, kind, project, body, note), encoding="utf-8")
        made.append((out.name, title, kind))
    links = "".join(f"<li><a href='{n}'>{html.escape(t)}</a> ({html.escape(k)})</li>" for n, t, k in made)
    (dst / "index.html").write_text(page("The record, readable", "Record", project, f"<ul class='idx'>{links}</ul>", note), encoding="utf-8")
    print(f"wrote {len(made)} pages and index.html to {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
