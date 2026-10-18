"""Build a meeting packet: the pages an inventor takes into a meeting with a buyer, a manufacturer, a lender, an investor or an accountant.
Procedure: https://ancreationoffice.com/sop-meeting-prep.txt (b-business-manager owns it; b-analyst runs this).

  python3 meeting-packet.py AN-Creation/correspondence/YYMMDD-NN-X-slug buyer|manufacturer|lender|investor|accountant

The meeting folder (its folder in the correspondence log, sop-correspondence.txt) holds meeting.csv (key,value,note: who, when, the goal, the ask, the walk-away, the questions
they will ask). Its "record" row names the folder with the sheets (relative to the meeting folder): the copies of
b-project-manager's sheets (cost-sheet.csv, risk-table.csv, actions.csv, spending.csv) and b-business-manager's own
(funding.csv, company.csv, pricing-terms.csv, cash-flow.csv, business-risks.csv, market-evidence.csv).
Writes <type>-packet.html in the meeting folder. The last page is the prep sheet, for the inventor only.
"""

import csv
import html
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) != 3 or sys.argv[2] not in ("buyer", "manufacturer", "lender", "investor", "accountant"):
    sys.exit("usage: python3 meeting-packet.py <meeting folder> buyer|manufacturer|lender|investor|accountant")
MEET = Path(sys.argv[1]).resolve()
KIND = sys.argv[2]


def rows(path):
    if not path.is_file():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


meeting = rows(MEET / "meeting.csv")
M = {}
MULTI = {}
for r in meeting:
    M.setdefault(r["key"], r["value"])
    MULTI.setdefault(r["key"], []).append(r)
REC = (MEET / M.get("record", ".")).resolve()


def sheet(name):
    return rows(MEET / name) or rows(REC / name)


def kv(name):
    out = {}
    for r in sheet(name):
        out.setdefault(r["key"], []).append(r)
    return out


def first(d, key, default=""):
    return d.get(key, [{"value": default}])[0]["value"]


def num(text):
    text = (text or "").replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(text)
    except ValueError:
        return 0.0


def money(v, cents=True):
    sign = "−" if v < 0 else ""
    v = abs(v)
    return sign + (f"${v:,.2f}" if cents else f"${v:,.0f}")


def esc(t):
    return html.escape(str(t or ""))


def fdate(t):
    try:
        y, m, d = (int(x) for x in t.split("-"))
        return date(y, m, d).strftime("%b %d, %Y").replace(" 0", " ")
    except Exception:
        return esc(t)


funding = kv("funding.csv")
company = sheet("company.csv")
pricing = kv("pricing-terms.csv")
cost = [r for r in sheet("cost-sheet.csv") if r.get("part") and not r["part"].startswith("Example")]
risk = sheet("risk-table.csv")
brisks = sheet("business-risks.csv")
actions = sheet("actions.csv")
spending = sheet("spending.csv")
cashflow = sheet("cash-flow.csv")
evidence = sheet("market-evidence.csv")
expenses = sheet("expenses.csv")
trips = sheet("trips.csv")
deadlines = sheet("deadlines.csv")

PRODUCT = first(funding, "product", "This product")
U = first(funding, "unit", "unit")
US = first(funding, "units", U + "s")
piece = sum(num(r["material cost"]) + num(r["process cost"]) for r in cost)
tooling = sum(num(r["tooling"]) for r in cost)
TITLE = {"buyer": "Buyer packet", "manufacturer": "Request for quote", "lender": "Lender packet", "investor": "Investor packet", "accountant": "Accountant packet"}[KIND]


def table(head, body, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in body)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def page(title, body, kicker):
    return (f'<section class="page"><header><div class="band"><span>{esc(PRODUCT)}</span>'
            f'<span>{TITLE} · {fdate(M.get("date", ""))}</span></div><p class="kicker">{esc(kicker)}</p>'
            f'<h1>{esc(title)}</h1></header>{body}</section>')


def stat(label, value, note=""):
    return (f'<div class="stat"><div class="v">{value}</div><div class="l">{esc(label)}</div>'
            + (f'<div class="n">{esc(note)}</div>' if note else "") + "</div>")


def pill(status):
    s = (status or "").lower()
    cls = "low" if s == "ready" else "medium" if s == "in progress" else "high"
    return f'<span class="lvl {cls}">{esc(status)}</span>'


def company_table():
    return table(["", "", "Status"], [[f"<strong>{esc(r['key'])}</strong>", esc(r["value"]), pill(r["status"])] for r in company], "compact")


def prep_sheet(extra="", top=""):
    qa = [[esc(r["value"]), esc(r["note"])] for r in MULTI.get("q", [])]
    asks = "".join(f"<li>{esc(r['value'])}</li>" for r in MULTI.get("ask", []))
    gaps = [r for r in company if r["status"] != "ready"]
    body = f"""<div class="verdict warn"><strong>For the inventor only. Not handed over.</strong> {esc(M.get('who'))}, {fdate(M.get('date'))}.</div>
{top}<h2>The goal</h2><p>{esc(M.get('goal'))}</p>
<h2>What we ask for</h2><ul class="levers">{asks}</ul>
<h2>Walk-away</h2><p>{esc(M.get('walk_away'))}</p>
<h2>What they will likely ask</h2>{table(['Question', 'Answer'], qa, 'compact')}
{extra}
<h2>Still open (say so if asked)</h2>{table(['', 'Today', 'Note'], [[f"<strong>{esc(r['key'])}</strong>", esc(r['value']), esc(r['note'])] for r in gaps], 'compact')}
<h2>Leave behind</h2><p>{esc(M.get('leave_behind', 'This packet, minus this page.'))}</p>
<h2>After the meeting</h2><p class="small">Record what was said in this folder; add any signal to market-evidence.csv; update contacts.csv with the next step and date; put every promise on the action log (sop-meeting-prep.txt step 8).</p>"""
    return page("Prep sheet", body, "Last page")


CSS = """
@page { size: letter; margin: 0.55in 0.65in 0.6in;
  @bottom-left { content: "PRODUCT_NAME · PACKET_NAME"; font: 7.5pt Arial, sans-serif; color: #777; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); font: 7.5pt Arial, sans-serif; color: #777; } }
* { box-sizing: border-box; }
body { margin: 0; font: 9.6pt/1.42 Arial, "Helvetica Neue", sans-serif; color: #1d2328; }
.page { break-after: page; } .page:last-child { break-after: auto; }
.band { display: flex; justify-content: space-between; background: #1f3b4d; color: #fff; font-size: 8pt; letter-spacing: .05em; text-transform: uppercase; padding: 6pt 9pt; border-radius: 3pt; }
.kicker { margin: 12pt 0 0; font-size: 7.5pt; color: #6b7780; letter-spacing: .08em; text-transform: uppercase; }
h1 { font-size: 19pt; margin: 2pt 0 10pt; color: #1f3b4d; }
h2 { font-size: 10.5pt; color: #1f3b4d; margin: 13pt 0 5pt; padding-bottom: 2pt; border-bottom: 1.2pt solid #c9a35b; break-after: avoid; }
p { margin: 0 0 6pt; } .small { font-size: 8pt; color: #5d6770; }
table { width: 100%; border-collapse: collapse; margin: 2pt 0 6pt; break-inside: auto; }
th { text-align: left; font-size: 7.6pt; text-transform: uppercase; letter-spacing: .04em; color: #4b5761; background: #eef2f4; padding: 4pt 5pt; }
td { padding: 4pt 5pt; border-bottom: .5pt solid #d8dee2; vertical-align: top; } tr { break-inside: avoid; }
table.bom td:nth-child(2) { font-size: 8pt; color: #4b5761; } table.num td:nth-child(n+3), table.num th:nth-child(n+3) { text-align: right; white-space: nowrap; }
table.num2 td:nth-child(2), table.num2 th:nth-child(2) { text-align: right; white-space: nowrap; }
table.kv td:first-child { width: 28%; } table.kv thead { display: none; }
table.compact td { font-size: 8.6pt; } table.fmea td:nth-child(3), table.fmea td:nth-child(5) { white-space: nowrap; }
table.reg td:nth-child(4), table.reg td:nth-child(8) { white-space: nowrap; }
.verdict { padding: 8pt 10pt; border-radius: 3pt; margin-bottom: 4pt; } .verdict.warn { background: #fdf3e1; border-left: 4pt solid #c9862b; } .verdict.ok { background: #e8f4ec; border-left: 4pt solid #3d8a5a; }
.stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6pt; margin: 4pt 1pt 6pt 0; } .stat { border: .7pt solid #d8dee2; border-radius: 3pt; padding: 6pt 7pt; }
.stat .v { font-size: 14pt; font-weight: bold; color: #1f3b4d; } .stat .l { font-size: 7.8pt; color: #4b5761; } .stat .n { font-size: 7pt; color: #7b868f; }
.levers { margin: 0 0 4pt; padding-left: 14pt; } .levers li { margin-bottom: 2pt; }
.lvl { display: inline-block; font-size: 7pt; font-weight: bold; padding: 1pt 4pt; border-radius: 2pt; white-space: nowrap; }
.lvl.high { background: #f6d5d0; color: #8a2a1c; } .lvl.medium { background: #fbe9c6; color: #7a5410; } .lvl.low { background: #dcefe2; color: #2e6b43; }
sup.ill { font-size: 6pt; color: #fff; background: #9aa5ad; border-radius: 6pt; padding: 0 2.5pt; margin-left: 1pt; }
.riskhead { display: flex; gap: 14pt; align-items: flex-start; margin-bottom: 6pt; }
.heat { width: 2.1in; flex: none; } .heattitle { font-size: 7pt; color: #5d6770; margin-bottom: 2pt; }
.grid { display: grid; grid-template-columns: 12pt repeat(5, 1fr); gap: 2pt; }
.cell { height: 22pt; border-radius: 2pt; font-size: 7pt; font-weight: bold; display: flex; align-items: center; justify-content: center; }
.cell.high { background: #f0c2ba; } .cell.medium { background: #f8e2b3; } .cell.low { background: #d3eadb; }
.ax { font-size: 7pt; color: #5d6770; text-align: center; align-self: center; }
.legend { font-size: 8.4pt; } .nw { white-space: nowrap; }
.foot-note { font-size: 7.5pt; color: #6b7780; margin-top: 10pt; }
"""

pages = []

# ---------------- buyer ----------------
if KIND == "buyer":
    shelf = num(first(pricing, "shelf_price"))
    rm = num(first(pricing, "retailer_margin_pct")) / 100
    dm = num(first(pricing, "distributor_margin_pct")) / 100
    ours = num(first(pricing, "our_price"))
    retailer_pays = shelf * (1 - rm)
    dist_pays = retailer_pays * (1 - dm)
    benefits = "".join(f"<li>{esc(r['value'])}</li>" for r in pricing.get("benefit", []))
    pages.append(page(PRODUCT, f"""
<p class="lede-big">{esc(first(pricing, 'headline'))}</p>
<h2>Who it's for</h2><p>{esc(first(pricing, 'who_for'))}</p>
<h2>Why it sells</h2><ul class="levers">{benefits}</ul>
<div class="stats">{stat('Suggested shelf price', money(shelf))}{stat('Retailer margin', f'{rm*100:.0f}%')}{stat('Distributor margin', f'{dm*100:.0f}%')}{stat('Case pack', esc(first(pricing, 'case_pack')))}</div>
<h2>Samples</h2><p>{esc(first(pricing, 'samples'))}</p>""", "Sell sheet"))
    closes = abs(dist_pays - ours) < 0.02 or dist_pays >= ours
    wf = [["Shelf price", money(shelf), "What the shopper pays"],
          [f"Retailer pays (keeps {rm*100:.0f}%)", money(retailer_pays), ""],
          [f"Distributor pays (keeps {dm*100:.0f}%)", money(dist_pays), ""],
          [f"Our price per {U}", money(ours), ""]]
    terms = [[esc(k.replace("_", " ").capitalize()), esc(first(pricing, k))] for k in
             ("minimum_order", "lead_time", "payment_terms", "shipping", "returns", "warranty") if k in pricing]
    pages.append(page("Pricing and terms", f"""
<h2>From the shelf price to ours</h2>{table(['', 'Per ' + U, ''], wf, 'num2')}
<h2>Terms</h2>{table(['', ''], terms, 'kv')}""", "Page 2"))
    specs = [[esc(k[5:]), esc(r["value"])] for k, v in pricing.items() if k.startswith("spec:") for r in v]
    parts = [[esc(r["part"]), esc(r["what it is"])] for r in cost]
    pages.append(page("Product specifications", f"""
{table(['', ''], specs, 'kv')}
<h2>What's in it</h2>{table(['Part', 'What it is'], parts, 'compact')}
<p class="small">A value that says "to measure" has not been measured yet and is not guessed.</p>""", "Page 3"))
    pages.append(page("Company and compliance", f"""
<p>Where each item a buyer usually asks for stands today, and when the open ones will be ready.</p>
{company_table()}""", "Page 4"))
    ev = [[fdate(r["date"]), esc(r["who"]), esc(r["what they said"]), esc(r["what they did or would pay"])] for r in evidence]
    check = (f"<h2>Price check (never shown to the buyer)</h2><p>The chain works back from {money(shelf)} on the shelf to {money(dist_pays)} paid by the distributor, against our price of {money(ours)}"
             + ("." if closes else ": they do not match, so fix the price or the terms before the meeting.")
             + f" Our cost to make one {U} is {money(piece)}, so each one leaves {money(ours - piece)} before tooling; the {money(tooling, False)} of tooling takes "
             + (f"{tooling / (ours - piece):,.0f} {US} to pay back." if ours > piece else "forever to pay back at this price.")
             + " Do not agree to a lower price in the room.</p>")
    pages.append(prep_sheet(f"<h2>What others have said so far</h2>{table(['Date', 'Who', 'Said', 'Did or would pay'], ev, 'compact')}" if ev else "", check))

# ---------------- manufacturer ----------------
if KIND == "manufacturer":
    wanted = M.get("parts", "").replace(",", " ").split()
    to_quote = [r for r in cost if r.get("part number") in wanted] if wanted else [r for r in cost if r.get("make or buy") == "make"]
    pages.append(page("Request for quote", f"""
<p>{fdate(M.get('date'))}</p>
<p>To: {esc(M.get('who'))}</p>
<p>We are developing the {esc(PRODUCT.lower())} and are asking a small number of suppliers to quote the parts below. The drawings and CAD files are attached under a mutual NDA.</p>
<div class="stats">{stat('First order', esc(M.get('first_order_qty')))}{stat('Planned volume', esc(M.get('annual_qty')))}{stat('Quote needed by', fdate(M.get('quote_due')))}{stat('Parts to quote', str(len(to_quote)))}</div>
<h2>Please quote</h2><ul class="levers">{''.join(f"<li>{esc(r['value'])}</li>" for r in MULTI.get('ask', []))}</ul>
<p>For each part: piece price at the first-order and annual quantities, tooling cost and type, cavities, tool life, lead time for tooling and for parts, and what is included (inspection, packaging, freight).</p>
<p>Reply to {esc(M.get('reply_to'))}.</p>""", "Page 1"))
    pq = [[esc(r.get("part number")), f"<strong>{esc(r['part'])}</strong>", esc(r["what it is"]), f"{esc(r['qty'])} {esc(r.get('unit', ''))}",
           esc(M.get("drawing:" + r.get("part number", ""), "Description above")), esc(r.get("make or buy"))] for r in to_quote]
    pages.append(page("Parts to quote", table(["Part no.", "Part", "What it is", "Per unit", "Drawing / CAD", "Make or buy"], pq, "compact"), "Page 2"))
    crit = []
    cur = None
    for r in risk:
        if r.get("id", "").startswith("F"):
            cur = r
            if int(r.get("S") or 0) >= 8:
                crit.append([esc(r["id"]), esc(r["Failure mode / actions"]), "Severity " + esc(r["S"])])
        elif cur and r.get("S") and int(cur.get("S") or 0) >= 8:
            crit.append(["", esc(r["Failure mode / actions"]), "design feature to hold"])
    q = "".join(f"<li>{esc(r['value'])}</li>" for r in MULTI.get("quality", []))
    pages.append(page("Requirements", f"""
<h2>Critical features (from the risk analysis)</h2>
<p>These come from the failures that could hurt someone or stop the product working. They are marked on the drawings.</p>
{table(['', 'Failure or feature', 'Why it matters'], crit, 'compact')}
<h2>Quality</h2><ul class="levers">{q}</ul>
<h2>Packaging of parts</h2><p>{esc(M.get('packaging'))}</p>""", "Page 3"))
    ms = [[fdate(r["value"]), esc(r["key"][10:])] for k, v in funding.items() if k.startswith("milestone:") for r in v]
    pages.append(page("Commercial terms and timeline", f"""
{table(['', ''], [['Tooling ownership', esc(M.get('tooling_owner'))], ['Payment terms asked', esc(M.get('payment_terms_asked'))], ['Confidentiality', esc(M.get('nda'))]], 'kv')}
<h2>Timeline</h2>{table(['By', 'Milestone'], sorted(ms), 'compact')}""", "Page 4"))
    compare = [["Piece price at first order and at annual volume", ""], ["Tooling: cost, type (steel or aluminum), cavities, life in shots", ""],
               ["Who owns the tool, and can it move", ""], ["Lead time: tooling, first articles, production", ""],
               ["What's included: inspection, packaging, freight", ""], ["Payment terms", ""]]
    pages.append(prep_sheet(f"<h2>Comparing the quotes like for like</h2>{table(['Line every quote up on', 'Molder A'], compare, 'compact')}<p class='small'>Each quote goes on the cost sheet as a quote with its date, replacing the placeholder (today's placeholder tooling: {money(tooling, False)}).</p>"))

# ---------------- lender ----------------
if KIND == "lender":
    amount = num(M.get("loan_amount"))
    rate = num(M.get("rate_pct")) / 100 / 12
    n = int(num(M.get("term_months")) or 60)
    payment = amount * rate / (1 - (1 + rate) ** -n) if rate else amount / n
    owner_spent = sum(num(r["amount"]) for r in spending if r.get("paid from", "").lower() == "owner")
    owner_funds = num(first(funding, "owner_funds"))
    price = num(first(funding, "price"))
    uses = [[esc(k[4:]), money(num(r["value"]), False), esc(r["note"])] for k, v in funding.items() if k.startswith("use:") for r in v]
    # projection
    cash = owner_funds
    funded = False
    proj, cover, notes = [], [], []
    for r in cashflow:
        units = num(r["units sold"])
        rev = units * price
        cogs = units * piece
        cin = num(r["owner in"]) + num(r["loan in"]) + num(r["other cash in"]) + rev
        funded = funded or num(r["loan in"]) > 0
        pay = payment if funded and not num(r["loan in"]) else 0
        out = cogs + num(r["tooling"]) + num(r["other spending"]) + pay
        cash += cin - out
        operating = rev - cogs - num(r["other spending"])
        proj.append([esc(r["month"]), f"{units:,.0f}", money(rev, False), money(cogs, False), money(num(r["tooling"]) + num(r["other spending"]), False),
                     money(num(r["owner in"]) + num(r["loan in"]), False), money(pay, False), money(cash, False)])
        if r["note"]:
            notes.append(f"<li><strong>{esc(r['month'])}:</strong> {esc(r['note'])}</li>")
        if units:
            cover.append((r["month"], operating, operating / payment if payment else 0))
    avg_cover = sum(c for _, _, c in cover) / len(cover) if cover else 0
    repays = avg_cover >= 1.25
    avg_op = sum(o for _, o, _ in cover) / max(len(cover), 1)
    makes = (f"makes about {money(avg_op, False)} a month before debt" if avg_op >= 0 else f"loses about {money(-avg_op, False)} a month even before debt")
    verdict = ("The projection covers the payment with room to spare." if repays else
               f"The projection does not repay this loan: once sales start, the business {makes}, against an estimated payment of {money(payment, False)}. Coverage is {avg_cover:.2f}; lenders usually look for 1.25 or more.")
    pages.append(page("Loan request", f"""
<div class="verdict {'ok' if repays else 'warn'}"><strong>{'Ready to request.' if repays else 'Not ready to borrow this yet.'}</strong> {verdict}</div>
<div class="stats">{stat('Amount', money(amount, False))}{stat('Term', f'{n} months')}{stat('Estimated payment', money(payment, False), f"at {num(M.get('rate_pct')):.1f}% (illustrative)")}{stat("Owner's money in", money(owner_spent, False), f'plus {money(owner_funds, False)} committed')}</div>
<h2>What it pays for</h2>{table(['Use', 'Amount', 'Basis'], uses, 'num2')}
<h2>Collateral and guarantee</h2>{table(['', ''], [['Collateral', esc(M.get('collateral'))], ['Personal guarantee', esc(M.get('personal_guarantee'))]], 'kv')}
<h2>What fits this stage</h2><p>A pre-revenue company rarely gets a bank loan of this size. What fits now: own money and grants through the quotes and the buyer tests; then an SBA microloan through a local intermediary (up to $50,000) or a community lender, once the mold quotes close the numbers and a distributor has said what it would buy.</p>""", "Page 1"))
    pages.append(page("Cash-flow projection", f"""
<p>Month by month, starting with {money(owner_funds, False)} of the owner's money. Sales are at {money(price)} a {U}; the cost of each {U} sold is {money(piece)} (the cost sheet). Every row's assumption is in its note.</p>
{table(['Month', US.capitalize() + ' sold', 'Sales', 'Cost of goods', 'Tooling and other', 'Owner and loan in', 'Loan payment', 'Cash at month end'], proj, 'compact num')}
<h2>Assumptions</h2><ul class="levers small">{''.join(notes)}</ul>""", "Page 2"))
    cv = [[esc(m), money(o, False), money(payment, False), f"{c:.2f}"] for m, o, c in cover]
    pages.append(page("Repayment check", f"""
<p>Cash the business makes each month before the loan payment, against the estimated payment of {money(payment, False)} ({n} months at {num(M.get('rate_pct')):.1f}%, illustrative). Coverage is the first divided by the second; lenders usually want at least 1.25.</p>
{table(['Month', 'Cash before debt', 'Payment', 'Coverage'], cv, 'num')}
<p><strong>Average coverage: {avg_cover:.2f}.</strong> {'' if repays else 'What would change it: a lower mold cost (the quotes due ' + fdate(first(funding, 'milestone:Base mold quote in hand')) + '), a higher price, more volume, or a smaller loan.'}</p>""", "Page 3"))
    hb = [[esc(b["id"]), esc(b["risk"]), esc(b["mitigation"])] for b in brisks if int(b["likelihood"]) * int(b["impact"]) >= 8]
    docs = [["Business plan", "This packet and the one-page plan"], ["Personal and business tax returns", "The inventor brings them"],
            ["Personal financial statement", "The inventor fills it in on the lender's form"], ["Bank statements", "The inventor brings them"],
            ["Formation papers and tax ID", "After the company is formed"], ["Collateral list", esc(M.get("collateral"))]]
    pages.append(page("Company, documents and risks", f"""
{company_table()}
<h2>Documents a lender will ask for</h2>{table(['Document', 'Status'], docs, 'compact')}
<h2>The risks, and what is being done</h2>{table(['', 'Risk', 'What is being done'], hb, 'compact')}""", "Page 4"))
    pages.append(prep_sheet())

# ---------------- investor ----------------
if KIND == "investor":
    amount = num(M.get("amount"))
    price = num(first(funding, "price"))
    annual = num(first(funding, "annual_units"))
    years = num(first(funding, "years")) or 1
    plan_units = annual * years
    clears = price - piece
    margin_pct = clears / price * 100 if price else 0
    payback_units = tooling / clears if clears > 0 else float("inf")
    price_to_close = piece + (tooling / plan_units if plan_units else 0)
    carry = max(clears, 0) * plan_units
    closes = payback_units <= plan_units
    owner_spent = sum(num(r["amount"]) for r in spending if r.get("paid from", "").lower() == "owner")
    owner_funds = num(first(funding, "owner_funds"))
    uses = [[esc(r["key"][4:]), money(num(r["value"]), False), esc(r["note"])] for r in meeting if r["key"].startswith("use:")]
    use_total = sum(num(r["value"]) for r in meeting if r["key"].startswith("use:"))
    payback = f"{payback_units:,.0f} {US}" if payback_units != float("inf") else "never at this price"
    if closes:
        verdict = (f"<strong>The numbers close.</strong> At {money(price)} a {U}, each one clears {money(clears)} over its {money(piece)} cost to make, "
                   f"and the {money(tooling, False)} of tooling pays back in {payback}, inside the plan of {plan_units:,.0f}.")
    else:
        verdict = (f"<strong>The numbers do not close yet.</strong> At {money(price)} a {U}, each one clears {money(clears)} over its {money(piece)} cost to make; "
                   f"the {money(tooling, False)} of tooling would take {payback} to pay back, against a plan of {plan_units:,.0f}. "
                   f"This round does not pay for production molds. It pays for the step that shows whether the numbers can close: {esc(M.get('reaches'))}")
    pages.append(page("Investment summary", f"""
<div class="verdict {'ok' if closes else 'warn'}">{verdict}</div>
<p class="lede-big">{esc(first(pricing, 'headline') or PRODUCT)}</p>
<div class="stats">{stat('The ask', money(amount, False))}{stat('Offered as', esc(M.get('instrument_short', 'To be set')))}{stat("Owner's money in", money(owner_spent, False), f'plus {money(owner_funds, False)} committed')}{stat(f'Clears per {U}', money(clears), f'{margin_pct:.0f}% of the price')}</div>
<h2>What the money does</h2>{table(['Use', 'Amount', 'Basis'], uses + [['<strong>Total</strong>', '<strong>' + money(use_total, False) + '</strong>', '']], 'num2')}
<h2>What it reaches</h2><p>{esc(M.get('reaches'))}</p>
<h2>Who is asking</h2><p>{esc(M.get('founder'))}</p>""", "Page 1"))
    benefits = "".join(f"<li>{esc(r['value'])}</li>" for r in pricing.get("benefit", []))
    alts = [[esc(r["value"]), esc(r["note"])] for r in MULTI.get("alternative", [])]
    ev = [[fdate(r["date"]), esc(r["who"]), esc(r["what they said"]), esc(r["what they did or would pay"]), esc(r["strength"])] for r in evidence]
    pages.append(page("The product and the evidence", f"""
<h2>Who it's for</h2><p>{esc(first(pricing, 'who_for'))}</p>
<h2>Why it sells</h2><ul class="levers">{benefits}</ul>
<h2>What people use now</h2>{table(['Alternative', 'Where this one is different'], alts, 'compact')}
<h2>What people have said and done so far</h2>{table(['Date', 'Who', 'Said', 'Did or would pay', 'Strength'], ev, 'compact')}
<h2>How big it could be</h2><p>{esc(M.get('market', 'Not estimated yet. A market size goes here only with its source.'))}</p>""", "Page 2"))
    econ = [[f"Price to {first(funding, 'buyer', 'the buyer')}", money(price), esc(first(funding, 'price_note'))],
            [f"Cost to make one {U}", money(piece), "Cost sheet: material plus process, all parts"],
            [f"Clears per {U}", money(clears), f"{margin_pct:.0f}% of the price"],
            ["Tooling (molds)", money(tooling, False), "Cost sheet; placeholders until the quotes arrive"],
            ["Plan volume", f"{plan_units:,.0f} {US}", f"{annual:,.0f} a year for {years:,.0f} years"],
            ["Units to pay back the tooling", payback, ""]]
    pages.append(page("The numbers", f"""
{table(['', '', 'Basis'], econ, 'num2')}
<h2>What would change it</h2><ul class="levers">
<li><strong>Price:</strong> {money(price_to_close)} a {U} pays back today's tooling over the plan volume.</li>
<li><strong>Tooling:</strong> at today's price, the plan volume pays back {money(carry, False)} of tooling.</li>
<li><strong>Volume:</strong> at today's price and tooling, {payback}.</li></ul>
<p class="small">Every figure is computed from the cost sheet and the funding sheet; none is typed in. Values marked illustrative are not quotes.</p>""", "Page 3"))
    ms = [[fdate(r["value"]), esc(r["key"][10:]), esc(r["note"])] for r in sorted((r for k, v in funding.items() if k.startswith("milestone:") for r in v), key=lambda r: r["value"])]
    br = sorted(brisks, key=lambda b: -int(b["likelihood"]) * int(b["impact"]))
    lvl = lambda b: "high" if int(b["likelihood"]) * int(b["impact"]) >= 15 else "medium" if int(b["likelihood"]) * int(b["impact"]) >= 8 else "low"
    rk = [[esc(b["id"]), esc(b["risk"]), f'<span class="lvl {lvl(b)}">{lvl(b)}</span>', esc(b["mitigation"])] for b in br if b["status"] != "closed"]
    pages.append(page("The plan and the risks", f"""
<h2>Milestones</h2>{table(['By', 'Milestone', 'Basis'], ms, 'compact')}
<h2>What could go wrong, and what is being done</h2>{table(['', 'Risk', 'Level', 'What is being done'], rk, 'compact')}""", "Page 4"))
    def investor_company():
        keep = ("legal name", "entity", "owner", "product liability insurance", "rules that apply", "years in business")
        rows_ = [r for r in company if r["key"].lower() in keep] or company
        return table(["", "", "Status"], [[f"<strong>{esc(r['key'])}</strong>", esc(r["value"]), pill(r["status"])] for r in rows_], "compact")
    terms = [[f"<strong>{esc(r['value'])}</strong>", esc(r["note"])] for r in MULTI.get("term", [])]
    pages.append(page("The terms, and what to know", f"""
<h2>What is offered</h2><p>{esc(M.get('instrument'))}</p>
{table(['', ''], terms, 'kv') if terms else ''}
<h2>How an investor gets money back</h2><p>{esc(M.get('exit'))}</p>
<h2>Before anyone invests</h2><ul class="levers">
<li>This is an early, high-risk investment in a product that is not made yet. It can fail, and the money can be lost. Invest only money you can afford to lose.</li>
<li>A share of the company, a note or a SAFE is a security. Under federal and state law, every offer and sale of securities, even to one person, including family and friends, has to be registered or fall under an exemption. The terms are set with an attorney before any money changes hands.</li>
<li>Nothing here is a promise of a return. The numbers are the inventor's plan, built from the sheets named on each page.</li></ul>
<h2>The company</h2>{investor_company()}""", "Page 5"))
    pages.append(prep_sheet(top=f"<p class='small'>Owner's money already in: {money(owner_spent, False)} spent, {money(owner_funds, False)} committed. Investors ask this first.</p>"))

# ---------------- accountant ----------------
if KIND == "accountant":
    year = M.get("tax_year", M.get("date", "")[:4])
    ex = [r for r in expenses if r.get("date", "").startswith(year)]
    tr = [r for r in trips if r.get("date", "").startswith(year)]
    odo = [r for r in tr if r.get("trip", "").upper().startswith("ODO")]
    tr = [r for r in tr if r not in odo]
    total = sum(num(r["amount"]) for r in ex)
    miles = sum(num(r["business miles"]) for r in tr)
    tolls = sum(num(r.get("parking and tolls")) for r in tr)
    by_cat, by_from = {}, {}
    for r in ex:
        c = (r.get("tax category") or "").strip() or "no category yet"
        by_cat[c] = by_cat.get(c, 0) + num(r["amount"])
        w = (r.get("paid from") or "").strip() or "not said"
        by_from[w] = by_from.get(w, 0) + num(r["amount"])
    gaps = []
    for r in ex:
        lab = f"{fdate(r['date'])}, {esc(r['paid to'])}: {esc(r['what it was'])}"
        if not (r.get("receipt file") or "").strip():
            gaps.append(lab + ": no receipt")
        if not (r.get("business purpose") or "").strip():
            gaps.append(lab + ": no business purpose")
        if (r.get("tax category") or "").strip() == "":
            gaps.append(lab + ": no category")
    for r in tr:
        if not num(r.get("business miles")):
            gaps.append(f"{fdate(r['date'])}, trip {esc(r['trip'])}: no miles")
    if tr and not odo:
        gaps.append(f"No odometer reading for {year}")
    ask_acct = [r for r in ex if (r.get("tax category") or "").strip().lower() == "ask accountant"]
    ready = not gaps
    keep = ("legal name", "entity", "tax id (ein)", "business bank account", "years in business", "owner")
    co = [r for r in company if r["key"].lower() in keep] or company
    pages.append(page(f"For the accountant: tax year {year}", f"""
<div class="verdict {'ok' if ready else 'warn'}"><strong>{'The records are complete for this year.' if ready else f'{len(gaps)} gaps to close before the meeting.'}</strong> Everything here comes from the business record, kept as things happened: the expense ledger, the trip log and the company record. It sorts the year; it does not decide what is deductible.</div>
<div class="stats">{stat('Expenses this year', money(total))}{stat('Rows in the ledger', str(len(ex)))}{stat('Business miles', f'{miles:,.0f}', f'{len(tr)} trips')}{stat('Categories to decide', str(len(ask_acct)), money(sum(num(r["amount"]) for r in ask_acct)))}</div>
<h2>The business</h2>{table(['', '', 'Status'], [[f"<strong>{esc(r['key'])}</strong>", esc(r['value']), pill(r['status'])] for r in co], 'compact')}
<h2>What we are asking for</h2><ul class="levers">{''.join(f"<li>{esc(r['value'])}</li>" for r in MULTI.get('ask', []))}</ul>""", "Page 1"))
    cat = [[esc(k), money(v)] for k, v in sorted(by_cat.items())]
    frm = [[esc(k), money(v)] for k, v in sorted(by_from.items())]
    led = [[fdate(r["date"]), esc(r["paid to"]), esc(r["what it was"]), esc(r.get("business purpose")) or "<em>missing</em>",
            esc(r.get("tax category")) or "<em>none</em>", money(num(r["amount"])), "yes" if (r.get("receipt file") or "").strip() else "<em>missing</em>"] for r in ex]
    pages.append(page("Expenses", f"""
<div class="riskhead"><div style="flex:1">{table(['By tax category', 'Total'], cat, 'num2')}</div><div style="flex:1">{table(["By whose money", 'Total'], frm, 'num2')}</div></div>
<p class="small">"ask accountant" means the category waits for your call. Category names follow that year's IRS instructions or your own list once you give it to us.</p>
<h2>The ledger</h2>{table(['Date', 'Paid to', 'What it was', 'Business purpose', 'Category', 'Amount', 'Receipt'], led, 'compact')}""", "Page 2"))
    trows = [[fdate(r["date"]), esc(r["trip"]), esc(r.get("to (place and address)")), esc(r.get("business purpose")), esc(r.get("start odometer")), esc(r.get("end odometer")), f"{num(r['business miles']):,.0f}"] for r in tr]
    orows = [[fdate(r["date"]), esc(r.get("who or what")), esc(r.get("start odometer") or r.get("end odometer"))] for r in odo]
    same_day = sum(1 for r in tr if (r.get("logged on") or "").strip() == r.get("date", "").strip())
    pages.append(page("Trips and mileage", f"""
{table(['Date', 'Trip', 'To', 'Business purpose', 'Odometer start', 'Odometer end', 'Miles'], trows, 'compact')}
<p><strong>{miles:,.0f} business miles</strong>{f', plus {money(tolls)} in parking and tolls' if tolls else ''}. {same_day} of {len(tr)} trips were logged on the day they happened (the logged on column in the trip log).</p>
<h2>Odometer readings</h2>{table(['Date', 'What', 'Odometer'], orows, 'compact')}
<p class="small">No mileage rate is applied here: the rate is that year's IRS standard mileage rate, or actual costs if you choose that method.</p>""", "Page 3"))
    qs = [[f"<strong>{esc(r['value'])}</strong>", esc(r["note"])] for r in MULTI.get("question", [])]
    if ask_acct:
        qs.insert(0, ["<strong>Which category for each \"ask accountant\" row?</strong>", f"{len(ask_acct)} rows, {money(sum(num(r['amount']) for r in ask_acct))}: " + "; ".join(esc(r["what it was"]) for r in ask_acct)])
    dl = [[esc(r["due"]), esc(r["what"]), esc(r["Source"]), esc(r["Source status"])] for r in deadlines if any(w in (r.get("what", "") + r.get("why it matters", "")).lower() for w in ("tax", "irs", "1099", "estimated"))]
    pages.append(page("Questions for you", f"""
{table(['Question', 'What the record shows'], qs, 'compact')}
<h2>Tax deadlines we are tracking</h2>{table(['Due', 'What', 'Source', 'Source status'], dl, 'compact') if dl else '<p>None recorded yet.</p>'}
<p class="small">A deadline marked "to find" has no date yet because nobody has read it from the source. We would like you to confirm each one.</p>""", "Page 4"))
    gl = "".join(f"<li>{g}</li>" for g in gaps) or "<li>None.</li>"
    pages.append(prep_sheet(f"<h2>Gaps to close before the meeting</h2><ul class='levers small'>{gl}</ul><p class='small'>Find the receipt (a photo is fine), write the purpose, or mark the row \"receipt lost\" in its notes. tax-year.py lists the same gaps.</p>"))

css = CSS
doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(PRODUCT)}: {TITLE.lower()}</title>
<style>{css.replace('PRODUCT_NAME', esc(PRODUCT)).replace('PACKET_NAME', TITLE.lower())}
table.num td:first-child {{ white-space: nowrap; }}
.lede-big {{ font-size: 13pt; color: #1f3b4d; font-weight: bold; margin: 2pt 0 8pt; }}</style></head><body>{''.join(pages)}</body></html>"""
out = MEET / f"{KIND}-packet.html"
out.write_text(doc, encoding="utf-8")
print(f"wrote {out.name}: {len(pages)} pages")
