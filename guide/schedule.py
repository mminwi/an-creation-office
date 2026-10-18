#!/usr/bin/env python3
"""schedule.py: the schedule and its critical path, for the AN Creation office.

Usage: python3 schedule.py <folder with schedule.csv> [<output folder>]

schedule.csv has one row per milestone: id, milestone, depends on (ids,
space-separated), days after (how long it needs after the last thing it
depends on), planned (the charter's date), forecast (today's best date),
actual (when it happened), owner, source, notes.

It works out, for each milestone, the earliest date its dependencies allow,
which dependency drives it, and the critical path: the chain of drivers that
sets the last milestone's date. It flags a forecast earlier than its
dependencies allow, every slip, and every slip on the critical path, and
writes schedule.html (readable) next to the sheet. It changes no dates; the
bot updates the forecasts. Procedure: https://ancreationoffice.com/sop-schedule.txt
"""
import csv
import html
import pathlib
import sys
from datetime import date, timedelta


def d(text):
    try:
        return date.fromisoformat((text or "").strip())
    except ValueError:
        return None


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    src = pathlib.Path(argv[0])
    out = pathlib.Path(argv[1]) if len(argv) > 1 else src
    with open(src / "schedule.csv", newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("id") or "").strip()]
    by = {r["id"].strip(): r for r in rows}
    for r in rows:
        r["_deps"] = [x for x in (r.get("depends on") or "").replace(",", " ").split() if x]
        r["_when"] = d(r.get("actual")) or d(r.get("forecast")) or d(r.get("planned"))
    problems = []
    for r in rows:
        for x in r["_deps"]:
            if x not in by:
                problems.append(f"{r['id']} depends on {x}, which is not on the schedule")
    # earliest each dependency allows, and the driver
    for r in rows:
        lag = int(float(r.get("days after") or 0))
        best, driver = None, None
        for x in r["_deps"]:
            p = by.get(x)
            if p and p["_when"]:
                e = p["_when"] + timedelta(days=lag)
                if best is None or e > best:
                    best, driver = e, x
        r["_earliest"], r["_driver"] = best, driver
    # critical path: from the last milestone back through its drivers
    ends = [r for r in rows if r["_when"] and not any(r["id"] in o["_deps"] for o in rows)]
    last = max(ends, key=lambda r: r["_when"]) if ends else None
    crit, cur = [], last
    while cur is not None:
        crit.append(cur["id"])
        cur = by.get(cur["_driver"]) if cur["_driver"] else None
    crit.reverse()
    lines = []
    for r in rows:
        planned, when = d(r.get("planned")), r["_when"]
        r["_slip"] = (when - planned).days if planned and when else None
        r["_crit"] = r["id"] in crit
        if r["_earliest"] and not d(r.get("actual")) and d(r.get("forecast")) and d(r.get("forecast")) < r["_earliest"]:
            problems.append(f"{r['id']} {r['milestone']}: forecast {r['forecast']} is earlier than {r['_driver']} allows ({r['_earliest']}); move the forecast or the dependency")
        if r["_slip"] and r["_slip"] > 0:
            lines.append(f"{'CRITICAL ' if r['_crit'] else ''}{r['id']} {r['milestone']}: {r['_slip']} days late against the charter ({r.get('planned')} → {when})")
    # report
    print("Critical path: " + " → ".join(f"{i} {by[i]['milestone']}" for i in crit) if crit else "No critical path: no dated milestones")
    if last is not None and last["_slip"] and last["_slip"] > 0:
        print(f"The end moves: {last['milestone']} is forecast {last['_slip']} days after the charter's date. Recover on the critical path, or a change notice for the charter's dates (sop-change-control.txt).")
    print("\n".join(lines) or "Nothing is slipping.")
    if problems:
        print("\nTO FIX:\n" + "\n".join("- " + p for p in problems))
    e = lambda t: html.escape(str(t or ""))
    body = "".join(
        f"<tr class='{'crit' if r['_crit'] else ''}'><td>{e(r['id'])}</td><td>{e(r['milestone'])}</td><td>{e(' '.join(r['_deps']))}</td>"
        f"<td class='n'>{e(r.get('days after'))}</td><td class='d'>{e(r.get('planned'))}</td><td class='d'>{e(r.get('forecast'))}</td><td class='d'>{e(r.get('actual'))}</td>"
        f"<td class='n {'late' if (r['_slip'] or 0) > 0 else ''}'>{'' if r['_slip'] is None else ('+' if r['_slip'] > 0 else '') + str(r['_slip'])}</td>"
        f"<td>{'yes' if r['_crit'] else ''}</td><td>{e(r.get('notes'))}</td></tr>" for r in rows)
    summary = "<p><strong>Critical path:</strong> " + e(" → ".join(by[i]["milestone"] for i in crit)) + ".</p>"
    if last is not None and last["_slip"] and last["_slip"] > 0:
        summary += f"<p class='end'><strong>The end moves:</strong> {e(last['milestone'])} is forecast {last['_slip']} days after the charter's date. Recover time on the critical path, or the inventor accepts the new date through a change notice.</p>"
    if lines:
        summary += "<ul>" + "".join(f"<li>{e(x)}</li>" for x in lines) + "</ul>"
    if problems:
        summary += "<p><strong>To fix:</strong></p><ul>" + "".join(f"<li>{e(x)}</li>" for x in problems) + "</ul>"
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Schedule</title>
<style>@media screen and (max-width:760px){{table{{display:block;overflow-x:auto;max-width:100%}}}}body{{margin:0;background:#e9e6df;font:14px/1.45 Inter,"Segoe UI",Arial,sans-serif;color:#1d2427}}.page{{max-width:1180px;margin:24px auto;background:#fff;border:1px solid #d7d2c6;border-radius:6px;padding:28px 32px 36px}}
.top{{border-bottom:3px solid #315f5c;padding-bottom:10px;margin-bottom:14px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#315f5c;font-weight:700}}h1{{font-size:22px;margin:0 0 8px}}
table{{border-collapse:collapse;width:100%;font-size:12.5px;margin-top:10px}}th{{background:#f1eee6;text-align:left;border:1px solid #d9d4c8;padding:6px 7px}}td{{border:1px solid #e1ddd3;padding:6px 7px;vertical-align:top}}td.n{{text-align:right;white-space:nowrap}}
tr.crit td{{background:#f4f8f6;font-weight:600}}td.late{{color:#9a2b1b;font-weight:700}}.foot{{margin-top:14px;font-size:12px;color:#6b7275}}td.d{{white-space:nowrap}}.end{{background:#fdf3e1;border-left:4px solid #c9862b;padding:8px 10px}}</style></head><body><div class="page">
<div class="top">AN Creation Office · Project record</div><h1>Schedule</h1>{summary}
<table><thead><tr><th>ID</th><th>Milestone</th><th>Depends on</th><th>Days after</th><th>Planned (charter)</th><th>Forecast</th><th>Actual</th><th>Slip, days</th><th>Critical</th><th>Notes</th></tr></thead><tbody>{body}</tbody></table>
<p class="foot">Built by schedule.py from schedule.csv. Shaded rows are the critical path: the chain that sets the last date. A slip there moves the end; a slip elsewhere only uses up spare time.</p></div></body></html>"""
    out.mkdir(parents=True, exist_ok=True)
    (out / "schedule.html").write_text(page, encoding="utf-8")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
