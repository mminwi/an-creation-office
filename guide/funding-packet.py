"""Build the funding packet: the pages an inventor hands a lender, an SBDC advisor or a partner.
Procedure: https://ancreationoffice.com/sop-funding-packet.txt (b-business-manager owns it; b-analyst runs this).

  python3 funding-packet.py AN-Creation/Business/funding/<invention>

The folder holds copies of b-project-manager's sheets (intake-001.csv, cost-sheet.csv, risk-table.csv,
decision-log.csv, actions.csv) and b-business-manager's own (funding.csv, business-risks.csv).
Writes funding-packet.html in the same folder: print it, or save it as PDF.
Every figure is computed from the sheets. A funding.csv value with source "illustrative" prints with a small i mark.
"""

import csv
import html
import sys
from collections import OrderedDict
from datetime import date
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: python3 funding-packet.py <funding folder>")
HERE = Path(sys.argv[1]).resolve()
OUT = HERE / "funding-packet.html"


def read_csv(name):
    with open(HERE / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(text):
    text = (text or "").replace("$", "").replace(",", "").strip()
    return float(text) if text else 0.0


def money(value, cents=True):
    sign = "−" if value < 0 else ""
    value = abs(value)
    return sign + (f"${value:,.2f}" if cents else f"${value:,.0f}")


def esc(text):
    return html.escape(str(text or ""))


def fmt_date(text):
    y, m, d = (int(x) for x in text.split("-"))
    return date(y, m, d).strftime("%b %d, %Y").replace(" 0", " ")


# ---------- load ----------
intake = {r["Field"]: r for r in read_csv("intake-001.csv")}
decisions = [d for d in read_csv("decision-log.csv") if d.get("date") and not d["decision"].startswith("Example")]
cost_rows = [r for r in read_csv("cost-sheet.csv") if r.get("part") and not r["part"].startswith("Example")
             and not r["part"].upper().startswith("TOTAL")]
risk_rows = read_csv("risk-table.csv")
actions = read_csv("actions.csv")
brisks = read_csv("business-risks.csv")

funding, uses, milestones, illustrative = {}, OrderedDict(), [], set()
for r in read_csv("funding.csv"):
    key, value = r["key"], r["value"]
    if r["source"] == "illustrative":
        illustrative.add(key)
    if key.startswith("use:"):
        uses[key[4:]] = (num(value), r["source"] == "illustrative", r["note"])
    elif key.startswith("milestone:"):
        milestones.append((value, key[10:], r["source"]))
    else:
        funding[key] = (value, r["note"])

PRODUCT = funding.get("product", ("This product", ""))[0]
U = funding.get("unit", ("unit", ""))[0]                 # what one is called: trap, clamp, unit
US = funding.get("units", (U + "s", ""))[0]
BUYER = funding.get("buyer", ("the buyer", ""))[0]        # who pays the price: the distributor, the store
CHANNEL = funding.get("channel", ("", ""))[0]            # e.g. "to hardware and farm-supply distributors"
PRICE_NOTE = funding.get("price_note", ("", ""))[0]      # one short line under the price, e.g. "their landed-cost target"
PREPARED = date.fromisoformat(funding["prepared"][0]) if funding.get("prepared", ("", ""))[0] else date.today()

# ---------- the numbers ----------
piece = sum(num(r["material cost"]) + num(r["process cost"]) for r in cost_rows)
tooling = sum(num(r["tooling"]) for r in cost_rows)
annual = num(funding["annual_units"][0])
years = num(funding["years"][0])
plan_units = annual * years
price = num(funding["price"][0])
contribution = price - piece
margin_pct = contribution / price * 100 if price else 0
payback_units = tooling / contribution if contribution > 0 else float("inf")
payback_years = payback_units / annual if annual else float("inf")
price_to_close = piece + tooling / plan_units          # price that pays back the tooling over the plan volume
tooling_ceiling = max(contribution, 0) * plan_units   # tooling the current price can pay back over the plan volume
closes = payback_units <= plan_units

placeholders = sum(1 for r in cost_rows if num(r["tooling"]) and "placeholder" in r["tooling notes"].lower())
quoted = sum(1 for r in cost_rows if num(r["tooling"])) - placeholders
TOOL_NOTE = (f"{placeholders} of {placeholders + quoted} tooling figures are placeholders, not quotes" if placeholders
             else "all tooling figures are quotes" if quoted else "no tooling")

total_uses = sum(v for v, _, _ in uses.values())
owner_funds = num(funding["owner_funds"][0])
ask = max(total_uses - owner_funds, 0)

# design risk: group rows into failures (id row, then action rows), skip the summary rows
failures = []
for r in risk_rows:
    if r["id"].startswith("F"):
        failures.append({"id": r["id"], "failure": r["Failure mode / actions"], "effect": r["effect"],
                         "before": (int(r["S"]), int(r["O"]), int(r["D"])), "actions": [], "after": None,
                         "status": r["status"]})
        if r["RPN"]:
            failures[-1]["after"] = failures[-1]["before"]
    elif failures and r["S"]:
        f = failures[-1]
        f["actions"].append(r["Failure mode / actions"])
        if r["RPN"]:
            f["after"] = (int(r["S"]), int(r["O"]), int(r["D"]))
            f["status"] = r["status"]
for f in failures:
    s, o, d = f["after"] or f["before"]
    f["after"] = (s, o, d)
    f["rpn_before"] = f["before"][0] * f["before"][1] * f["before"][2]
    f["rpn_after"] = s * o * d
    f["high_severity"] = f["before"][0] >= 9 or s >= 8
total_before = sum(f["rpn_before"] for f in failures)
total_after = sum(f["rpn_after"] for f in failures)

open_actions = [a for a in actions if a["Status"] in ("open", "waiting") and not a["Action"].startswith("Example")]
owned = [a for a in open_actions if a["Who"] and a["Due"]]
unowned = [a for a in open_actions if not (a["Who"] and a["Due"])]

for b in brisks:
    b["score"] = int(b["likelihood"]) * int(b["impact"])
    b["level"] = "High" if b["score"] >= 15 else "Medium" if b["score"] >= 8 else "Low"
brisks.sort(key=lambda b: -b["score"])

readiness = ("Ready to request funds" if closes else
             "Not ready to request funds: the numbers do not close yet")

# ---------- page pieces ----------
ILL = '<sup class="ill" title="Illustrative: replace with a real figure">i</sup>'


def page(title, body, kicker):
    return f"""<section class="page">
<header><div class="band"><span>{esc(PRODUCT)}</span><span>Funding packet · {PREPARED:%B %d, %Y}</span></div>
<p class="kicker">{esc(kicker)}</p><h1>{esc(title)}</h1></header>
{body}
</section>"""


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


def stat(label, value, note=""):
    return f'<div class="stat"><div class="v">{value}</div><div class="l">{esc(label)}</div>' + (
        f'<div class="n">{esc(note)}</div>' if note else "") + "</div>"


pages = []

# 1. Executive summary
verdict_cls = "ok" if closes else "warn"
top_brisks = brisks[:3]
pages.append(page("Executive summary", f"""
<div class="verdict {verdict_cls}"><strong>{esc(readiness)}.</strong>
{'' if closes else f'At {money(price)} to {BUYER}, each {U} clears {money(contribution)} over its {money(piece)} piece cost. The {money(tooling, False)} of tooling would take {payback_units:,.0f} {US} to pay back, about {payback_years:,.0f} years at {annual:,.0f} a year. This packet shows what has to change, and the work already under way to change it.'}</div>
<h2>The product</h2>
<p>{esc(intake['invention']['Answer'])} {esc(intake['problem']['Answer'])}</p>
<div class="stats">
{stat(f"Piece cost, one {U}", money(piece))}
{stat(f"Price to {BUYER}", money(price), PRICE_NOTE)}
{stat(f"Clears per {U}", money(contribution), f"{margin_pct:.0f}% of price")}
{stat("One-time tooling", money(tooling, False), TOOL_NOTE)}
</div>
<h2>Where it stands</h2>
<p>{esc(intake['stage']['Answer'])} Target: {annual:,.0f} {US} a year {CHANNEL}. The owner is putting in {money(owner_funds, False)}{ILL if "owner_funds" in illustrative else ""}.</p>
<h2>What it would take to close</h2>
<ul class="levers">
<li><strong>Price:</strong> {money(price_to_close)} a {U} pays back today's tooling over {plan_units:,.0f} {US}, against {money(price)} asked.</li>
<li><strong>Tooling:</strong> at {money(price)}, the plan volume pays back at most {money(tooling_ceiling, False)} of tooling.</li>
<li><strong>Volume:</strong> at {money(price)} and today's tooling, {payback_units:,.0f} {US}.</li>
</ul>
<h2>Top risks</h2>
{table(["Risk", "Level", "What is being done"], [[esc(b['risk']), f'<span class="lvl {b["level"].lower()}">{b["level"]}</span>', esc(b['mitigation'])] for b in top_brisks], "compact")}
<h2>Funding request</h2>
<p>{money(total_uses, False)} in startup costs, less {money(owner_funds, False)}{ILL if "owner_funds" in illustrative else ""} from the owner: <strong>{money(ask, False)}</strong>. {'Requested now.' if closes else 'Not requested until the numbers close; shown so a lender or advisor can see the size of it.'}</p>
""", "Page 1"))

# 2. Product and market
answers = [("The problem it solves", "problem"), ("Who buys and uses it", "customer"), ("Where it is used", "where-used"),
           ("What it competes with", "similar"), ("What buyers have said", "buyers-said"), ("Sales goal", "goal")]
rows = []
for label, key in answers:
    a = intake[key]["Answer"] or "Not known yet."
    rows.append([f"<strong>{esc(label)}</strong>", esc(a)])
screen = [r for k, r in intake.items() if k.startswith("S") and r["Status"] == "answered" and r["Answer"].lower().startswith("yes")]
pages.append(page("Product and market", f"""
{table(["", ""], rows, "kv")}
<h2>Rules and standards it runs into</h2>
<p>From the screening questions, these are the ones that apply:</p>
<ul class="levers">{"".join("<li><strong>" + esc(r['Ask it like this']) + "</strong> " + esc(r['Answer']) + "</li>" for r in screen)}</ul>
<p>No electrical, medical, wireless, food-contact or children's-product rules apply.</p>
<h2>Decisions already made</h2>
{table(["Date", "Decision", "Why"], [['<span class="nw">' + fmt_date(d['date']) + "</span>", esc(d['decision']), esc(d['reason'].split('. ')[0] + '.')] for d in decisions], "compact")}
""", "Page 2"))

# 3. Cost and unit economics
bom = []
for r in cost_rows:
    each = num(r["material cost"]) + num(r["process cost"])
    bom.append([f"<strong>{esc(r['part'])}</strong>", esc(r["what it is"]), money(num(r["material cost"])), money(num(r["process cost"])),
                money(each), money(num(r["tooling"]), False) if num(r["tooling"]) else "–"])
bom.append(["<strong>One unit</strong>", "", money(sum(num(r['material cost']) for r in cost_rows)),
            money(sum(num(r['process cost']) for r in cost_rows)), f"<strong>{money(piece)}</strong>", f"<strong>{money(tooling, False)}</strong>"])
sens = []
for units in (plan_units, plan_units * 2, plan_units * 5, payback_units):
    if units == float("inf"):
        continue
    t = tooling / units
    sens.append([f"{units:,.0f}", money(t), money(piece + t), money(price - piece - t)])
pages.append(page("Cost and unit economics", f"""
<h2>Bill of materials, one unit</h2>
{table(["Part", "What it is", "Material", "Process", "Each", "Tooling (once)"], bom, "num bom")}
<p class="small">Tooling is a one-time cost, kept out of the piece cost so it can be seen. {TOOL_NOTE.capitalize()}.</p>
<h2>What one {U} earns</h2>
<div class="stats">{stat(f"Price to {BUYER}", money(price))}{stat("Piece cost", money(piece))}{stat(f"Clears per {U}", money(contribution), f"{margin_pct:.0f}% gross margin")}{stat("Traps to pay back tooling", f"{payback_units:,.0f}")}</div>
<h2>Tooling spread over different volumes</h2>
{table([f"{US.capitalize()} made", f"Tooling per {U}", f"Full cost per {U}", f"Left per {U} at " + money(price)], sens, "num")}
<p class="small">The last row is the break-even volume. A negative number means each {U} loses money at that volume once the tooling is counted.</p>
""", "Page 3"))

# 4. Funding request and milestones
use_rows = [[esc(k) + (ILL if ill else ""), money(v, False), esc(n)] for k, (v, ill, n) in uses.items()]
use_rows.append(["<strong>Total startup cost</strong>", f"<strong>{money(total_uses, False)}</strong>", ""])
use_rows.append(["Owner's contribution" + (ILL if "owner_funds" in illustrative else ""), "– " + money(owner_funds, False), esc(funding["owner_funds"][1])])
use_rows.append(["<strong>Amount to finance</strong>", f"<strong>{money(ask, False)}</strong>", "Loan, grant or partner"])
ms_rows = [[fmt_date(d), esc(m) + (ILL if src == "illustrative" else ""), esc(src)] for d, m, src in sorted(milestones)]
pages.append(page("Funding request and milestones", f"""
<h2>Use of funds</h2>
{table(["", "Amount", "Basis"], use_rows, "num2")}
<h2>Milestones</h2>
{table(["By", "Milestone", "Source"], ms_rows, "compact")}
<h2>Open actions with an owner and a date</h2>
{table(["Action", "Who", "Due", "Status"], [[esc(a['Action']), esc(a['Who']), fmt_date(a['Due']), esc(a['Status'])] for a in owned], "compact")}
<p class="small">{len(unowned)} design changes from the risk analysis still need an owner and a date (appendix A).</p>
""", "Page 4"))

# 5. Risk register
heat = {}
for b in brisks:
    heat.setdefault((int(b["likelihood"]), int(b["impact"])), []).append(b["id"])
cells = ""
for lk in range(5, 0, -1):
    cells += f'<div class="ax">{lk}</div>'
    for im in range(1, 6):
        lvl = "high" if lk * im >= 15 else "medium" if lk * im >= 8 else "low"
        cells += f'<div class="cell {lvl}">{" ".join(heat.get((lk, im), []))}</div>'
cells += '<div></div>' + "".join(f'<div class="ax">{i}</div>' for i in range(1, 6))
reg = [[b["id"], esc(b["risk"]), esc(b["category"]), f'{b["likelihood"]}×{b["impact"]}', f'<span class="lvl {b["level"].lower()}">{b["level"]}</span>',
        esc(b["mitigation"]), esc(b["owner"]), fmt_date(b["due"])] for b in brisks]
pages.append(page("Risk register", f"""
<div class="riskhead">
<div class="heat"><div class="heattitle">Likelihood ↑ · Impact →</div><div class="grid">{cells}</div></div>
<div class="legend"><p><strong>How to read it.</strong> Each risk is scored 1–5 for likelihood and 1–5 for impact. Their product rates it: 15 and up is High, 8–14 Medium, under 8 Low.</p>
<p>High risks are worked before money is committed. Product safety risks are worked by severity first, whatever their score (appendix A).</p></div>
</div>
{table(["", "Risk", "Type", "L×I", "Level", "Response", "Owner", "By"], reg, "compact reg")}
""", "Page 5"))

# 6. Appendix A: design risk analysis
fm = []
for f in sorted(failures, key=lambda f: -f["rpn_after"]):
    b, a = f["before"], f["after"]
    flag = ' <span class="lvl high">Severity ' + str(b[0]) + "</span>" if f["high_severity"] else ""
    fm.append([f["id"], esc(f["failure"]) + flag, f"{b[0]}·{b[1]}·{b[2]} = {f['rpn_before']}",
               esc("; ".join(f["actions"])) or "None: accepted as designed", f"{a[0]}·{a[1]}·{a[2]} = {f['rpn_after']}", esc(f["status"])])
pages.append(page("Appendix A: design risk analysis", f"""
<p>Every way the {U} could fail, scored before and after the design changes. S = severity, O = occurrence, D = detection, each 1–10; their product is the risk priority number (RPN). Total risk fell from <strong>{total_before}</strong> to <strong>{total_after}</strong>. Severity 9–10 items get action whatever their RPN.</p>
{table(["", "Failure", "Before (S·O·D)", "Design change", "After", "Status"], fm, "compact fmea")}
<p class="foot-note">{'<sup class="ill">i</sup> marks an illustrative figure, to be replaced before this is shown. ' if illustrative else ''}Every other figure comes from the project's own sheets. {TOOL_NOTE.capitalize()}. Prepared with the AN Creation Office.</p>
""", "Page 6"))

doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(PRODUCT)}: funding packet</title>
<style>
@page {{ size: letter; margin: 0.55in 0.65in 0.6in;
  @bottom-left {{ content: "{esc(PRODUCT)} · funding packet · draft for review"; font: 7.5pt Arial, sans-serif; color: #777; }}
  @bottom-right {{ content: "Page " counter(page) " of " counter(pages); font: 7.5pt Arial, sans-serif; color: #777; }} }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 9.6pt/1.42 Arial, "Helvetica Neue", sans-serif; color: #1d2328; }}
.page {{ break-after: page; }} .page:last-child {{ break-after: auto; }}
.band {{ display: flex; justify-content: space-between; background: #1f3b4d; color: #fff; font-size: 8pt; letter-spacing: .05em; text-transform: uppercase; padding: 6pt 9pt; border-radius: 3pt; }}
.kicker {{ margin: 12pt 0 0; font-size: 7.5pt; color: #6b7780; letter-spacing: .08em; text-transform: uppercase; }}
h1 {{ font-size: 19pt; margin: 2pt 0 10pt; color: #1f3b4d; }}
h2 {{ font-size: 10.5pt; color: #1f3b4d; margin: 13pt 0 5pt; padding-bottom: 2pt; border-bottom: 1.2pt solid #c9a35b; break-after: avoid; }}
p {{ margin: 0 0 6pt; }} .small {{ font-size: 8pt; color: #5d6770; }}
table {{ width: 100%; border-collapse: collapse; margin: 2pt 0 6pt; break-inside: auto; }}
th {{ text-align: left; font-size: 7.6pt; text-transform: uppercase; letter-spacing: .04em; color: #4b5761; background: #eef2f4; padding: 4pt 5pt; }}
td {{ padding: 4pt 5pt; border-bottom: .5pt solid #d8dee2; vertical-align: top; }} tr {{ break-inside: avoid; }}
table.bom td:nth-child(2) {{ font-size: 8pt; color: #4b5761; }} table.num td:nth-child(n+3), table.num th:nth-child(n+3) {{ text-align: right; white-space: nowrap; }}
table.num2 td:nth-child(2), table.num2 th:nth-child(2) {{ text-align: right; white-space: nowrap; }}
table.kv td:first-child {{ width: 28%; }} table.kv thead {{ display: none; }}
table.compact td {{ font-size: 8.6pt; }} table.fmea td:nth-child(3), table.fmea td:nth-child(5) {{ white-space: nowrap; }}
table.reg td:nth-child(4), table.reg td:nth-child(8) {{ white-space: nowrap; }}
.verdict {{ padding: 8pt 10pt; border-radius: 3pt; margin-bottom: 4pt; }} .verdict.warn {{ background: #fdf3e1; border-left: 4pt solid #c9862b; }} .verdict.ok {{ background: #e8f4ec; border-left: 4pt solid #3d8a5a; }}
.stats {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6pt; margin: 4pt 1pt 6pt 0; }} .stat {{ border: .7pt solid #d8dee2; border-radius: 3pt; padding: 6pt 7pt; }}
.stat .v {{ font-size: 14pt; font-weight: bold; color: #1f3b4d; }} .stat .l {{ font-size: 7.8pt; color: #4b5761; }} .stat .n {{ font-size: 7pt; color: #7b868f; }}
.levers {{ margin: 0 0 4pt; padding-left: 14pt; }} .levers li {{ margin-bottom: 2pt; }}
.lvl {{ display: inline-block; font-size: 7pt; font-weight: bold; padding: 1pt 4pt; border-radius: 2pt; white-space: nowrap; }}
.lvl.high {{ background: #f6d5d0; color: #8a2a1c; }} .lvl.medium {{ background: #fbe9c6; color: #7a5410; }} .lvl.low {{ background: #dcefe2; color: #2e6b43; }}
sup.ill {{ font-size: 6pt; color: #fff; background: #9aa5ad; border-radius: 6pt; padding: 0 2.5pt; margin-left: 1pt; }}
.riskhead {{ display: flex; gap: 14pt; align-items: flex-start; margin-bottom: 6pt; }}
.heat {{ width: 2.1in; flex: none; }} .heattitle {{ font-size: 7pt; color: #5d6770; margin-bottom: 2pt; }}
.grid {{ display: grid; grid-template-columns: 12pt repeat(5, 1fr); gap: 2pt; }}
.cell {{ height: 22pt; border-radius: 2pt; font-size: 7pt; font-weight: bold; display: flex; align-items: center; justify-content: center; }}
.cell.high {{ background: #f0c2ba; }} .cell.medium {{ background: #f8e2b3; }} .cell.low {{ background: #d3eadb; }}
.ax {{ font-size: 7pt; color: #5d6770; text-align: center; align-self: center; }}
.legend {{ font-size: 8.4pt; }} .nw {{ white-space: nowrap; }}
.foot-note {{ font-size: 7.5pt; color: #6b7780; margin-top: 10pt; }}
</style></head><body>
{''.join(pages)}
</body></html>"""

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(doc, encoding="utf-8")
print(f"wrote {OUT.relative_to(HERE)}: piece {money(piece)}, price {money(price)}, clears {money(contribution)}, "
      f"tooling {money(tooling, False)}, payback {payback_units:,.0f} {US}, ask {money(ask, False)}, closes={closes}")
