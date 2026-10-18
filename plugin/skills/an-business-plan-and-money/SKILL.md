---
name: an-business-plan-and-money
description: "Use for the one-page plan and pricing, sales and invoices, the monthly close, the weekly review, funding and licensing."
---

# an-business-plan-and-money

Sections: The one-page business plan, and pricing; Customers and sales: the pipeline, quotes, invoices and getting paid; Money each month: the monthly close, cash and runway; The weekly review; Funding a project (b-funding); The funding packet; Licensing an invention (b-licensing).

## The one-page business plan, and pricing
(procedure file: sop-business-plan.txt)

Procedure: The one-page business plan, and pricing. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. May write: business-plan.csv in the business folder (template-business-plan.csv), its readable copy in Your files/Business record/, funding.csv (price, unit, cost_per_sale, monthly_fixed, owner_funds), and rows on the action log.
Goes with: `an-principles-bm` (Principles: the Office Manager Bot) , `an-business-plan-and-money` (Money each month: the monthly close, cash and runway) , `an-business-plan-and-money` (Customers and sales: the pipeline, quotes, invoices and getting paid)
Example: https://ancreationoffice.com/example-mousetrap/business-plan.csv . A small service business with no invention: https://ancreationoffice.com/example-lawn-service/business-plan.csv
Read this in the first conversation about a business, and whenever the price, the customer or the costs change.

WHY THIS EXISTS
Most small businesses never write a plan, and the ones that do write forty pages nobody reads. One page, kept current, is enough to run on: what you sell, to whom, at what price, how they find you, what it costs to run, and the one number that matters this month. It is also page one of every lender, investor and partner packet.

THE FIRST CONVERSATION ABOUT A BUSINESS
Works with or without an invention. With no Project Manager Bot and no invention, the business is the project, and this is its intake.
Open with: "Tell me about your business." Let them talk; fill every row their words answer, the same turn. Then ask the open rows one at a time, each with a default where one is sensible ("Most people start by charging by the hour. Does that fit?"). "Don't know yet" is a fine answer: the row says "for now" with a date to ask again.
The rows (template-business-plan.csv):
- business: its name, or the working name.
- what you sell: in one sentence a customer would say.
- who buys: the first customers, as specific as they can name (not "everyone").
- the problem it solves for them, in their words.
- price, and the unit it is priced in (an hour, a project, a month, an item, an order).
- cost per sale: what one unit costs to deliver (materials, supplies, fees, the outside labor in it). Not the owner's own time; that is the price's job.
- how they find you: the first two or three ways (word of mouth, a website, a market stall, a store, a platform).
- monthly fixed costs: what the business costs to keep open whether it sells or not (rent, software, insurance, phone, storage, any pay).
- owner's money: what the owner is putting in, and what they could lose without harm.
- the first goal: a number and a date ("10 paying clients by March").
- the one number: the figure that shows this month whether it's working (paying customers, sales, cash on hand).
- the biggest risk, in one line, and what would show early that it's real.
- next step: one.
When it's done, read it back in three or four plain lines and ask "Did I get that right?" That is the first win for an entrepreneur. Save, with its readable copy.

PRICING
- Price from three directions and show all three; the owner picks: what it costs (cost per sale plus a share of the fixed costs at the sales they expect), what customers pay now for the alternative (from market-evidence.csv, with sources), and what the value is to the customer.
- Services: per hour, per project, or a monthly retainer or subscription. Per hour is simplest to start and easiest to explain; per project rewards getting faster; a retainer steadies the cash. For any of them, the owner's hours in a month times the hourly rate they need is a check on whether the business can pay them.
- Products: the price chain from the shelf back (`an-tooling-and-launch` (Launch) and the buyer packet), when there is a store or a distributor in between.
- Break-even: monthly fixed costs divided by what each sale clears (price minus cost per sale). Say it as sales a month: "You cover your costs at 14 clients a month." Show it whenever the price, the cost or the fixed costs change.
- Never invent a competitor's price or a market rate. A price someone found is a row in market-evidence.csv with where it came from; a guess is labeled a guess.

KEEPING IT CURRENT
The plan is a living document (`an-project-record` (Living and parked documents)): when a sale, a price change, a new cost or a lost customer changes a row, update it that turn, with the date. The old version goes to History/. Copy price, unit, cost_per_sale, monthly_fixed and owner_funds into funding.csv when a lender, investor or partner meeting is set; the packets read them from there (meeting-packet.py).

DONE WHEN
Every row has an answer or a dated "for now", the owner has heard it read back, and the one number has a value for this month.

## Customers and sales: the pipeline, quotes, invoices and getting paid
(procedure file: sop-sales.txt)

Procedure: Customers and sales: the pipeline, quotes, invoices and getting paid. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. May write: pipeline.csv and invoices.csv in the business folder (template-pipeline.csv, template-invoices.csv), quote and invoice files in the correspondence log, their readable copies in Your files/Business record/, contacts.csv, and rows on the action log.
Goes with: `an-business-plan-and-money` (The one-page business plan, and pricing) , `an-business-plan-and-money` (Money each month: the monthly close, cash and runway) , `an-correspondence`
Example: https://ancreationoffice.com/example-mousetrap/pipeline.csv . A small service business with no invention: https://ancreationoffice.com/example-lawn-service/invoices.csv
Read this when a possible customer comes up, a quote or an invoice is needed, or a payment is late.

WHY THIS EXISTS
Small businesses rarely fail for lack of interest; they fail because the follow-up slipped, the quote went out late, or the invoice was never sent or never chased. A simple list, kept the same day, fixes most of it.

THE PIPELINE (pipeline.csv)
One row per possible sale: who, what they want, what it's worth, where it stands, and the next step with a date. Stages: lead (heard of them or they heard of you), talking, quoted, won, lost. A lost row keeps its reason; it is never deleted.
- Capture it the turn it comes up ("a lady at the market wants 20 for her shop"): the row, the contact in contacts.csv, and the next step on the action log with a date.
- Every row that isn't won or lost has a next step and a date. At the start of a conversation, ask once about any next step that is due ("Did you call the shop back?").
- Waiting on them for more than a week: offer to draft a short nudge. Never send it; the owner sends it.
- Won: the invoice (below) and, for a product, the order to the Project Manager Bot if there is one.

QUOTES
A quote is a document that goes out: it follows the correspondence log (S, the sent copy, dated folder) and moves the pipeline row to quoted. It says what is included, the price, how long it holds, payment terms, and what is not included. Price from the business plan; a discount is the owner's call, recorded with the reason in the decision log.

INVOICES AND GETTING PAID (invoices.csv)
One row per invoice: number, date, customer, what for, amount, sales tax if any, due date, paid on, paid amount, status (sent, paid, part paid, overdue, written off), the file.
- Invoice numbers run in order and are never reused. The invoice file goes in the correspondence log as sent.
- Payment terms are stated on every invoice (for example due in 15 or 30 days, or on delivery).
- The day after an invoice is due and unpaid, its row is overdue and the owner hears it once: "Acme's invoice for $400 was due yesterday. Want me to draft a friendly reminder?" Then again at 2 weeks and 30 days. After that, the owner decides: keep chasing, a payment plan, or write it off (decision log).
- A payment received is a row update (paid on, amount) the same turn, and the cash shows in the monthly close.
- Sales tax charged is not the business's money; it is kept apart and paid on schedule (`an-business-record` (The compliance calendar: licenses, permits, reports and taxes)). The bot never decides whether something is taxable; that comes from the state's own rules, opened and cited.
- Never store full card or bank numbers. "Paid by check" or "paid by card" is enough.

DONE WHEN
Every possible customer is a row with a next step and a date, every sale has an invoice, and every unpaid invoice is followed up on schedule.

## Money each month: the monthly close, cash and runway
(procedure file: sop-monthly-money.txt)

Procedure: Money each month: the monthly close, cash and runway. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. b-analyst totals the month. May write: monthly.csv in the business folder (template-monthly.csv), its readable copy in Your files/Business record/, and rows on the action log.
Goes with: `an-business-record` (The business record) (the expense ledger), `an-business-plan-and-money` (Customers and sales: the pipeline, quotes, invoices and getting paid) (invoices), `an-business-plan-and-money` (The one-page business plan, and pricing)
Example: https://ancreationoffice.com/example-mousetrap/monthly.csv . A small service business with no invention: https://ancreationoffice.com/example-lawn-service/monthly.csv
Read this in the first conversation of each new month, and whenever cash comes up.

WHY THIS EXISTS
The number that ends small businesses is cash, and most owners only look at it when it's already short. Fifteen minutes once a month, from records already kept, shows what came in, what went out, what's left, and how long it lasts.

THE MONTHLY CLOSE (first conversation of a new month)
1. Close the records first: the business record's month-end check (`an-business-record` (The business record) BE INSISTENT): missing receipts, trips without miles, invoices not yet logged.
2. One row in monthly.csv for last month, from the records, never typed from memory:
   - sales: invoices dated that month (invoices.csv), or money received if the owner keeps cash-basis books; say which, and keep to it.
   - cost of sales: what those sales cost to deliver (cost per sale times units, or the actual costs logged).
   - other spending: everything else in the expense ledger that month.
   - owner in, loans in: money put into the business.
   - cash at month end: from the bank statement, as the owner reads it to you. The bot never logs in to a bank.
   - months of cash: cash at month end divided by the average monthly spending of the last three months (the runway).
   - unpaid invoices: total still owed to the business.
   - sales tax held: collected and not yet paid over.
3. Say it in three lines: "October: $1,200 in sales, $640 out. $3,100 in the bank, about 5 months at this rate. $400 still owed to you." Then the one number from the business plan, and whether it moved.
4. Anything that changed the plan (a price, a cost, a customer) updates business-plan.csv the same turn.

WHEN TO SAY SOMETHING
- Fewer than three months of cash: say it plainly once, with the levers (sell more, collect what's owed, cut a fixed cost, add owner money or a loan), and put a decision on the action log.
- Spending that is running ahead of the plan by a quarter or more: one line, with what drove it.
- Unpaid invoices larger than a month's fixed costs: collecting comes first (`an-business-plan-and-money` (Customers and sales: the pipeline, quotes, invoices and getting paid)).

THE HARD LINES
- Never invent a figure; a missing one is asked for and the row says so.
- The bot reports; it does not do the books for the tax return. The accountant packet carries the year (`an-meetings-advisors` (The accountant packet)); once there is real income, an employee or outside money, an accountant is worth the fee (`an-principles-core` (Rigor scales with whose money is at risk)).
- Never store bank logins, full account numbers or card numbers.

DONE WHEN
Every month since the business started has a row, the owner has heard the three lines, and the runway is known.

## The weekly review
(procedure file: sop-weekly-review.txt)

Procedure: The weekly review. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, for the business. May write: weekly.csv in the business folder (template-weekly.csv), its readable copy in Your files/Business record/, and rows on the action log.
Goes with: `an-business-plan-and-money` (The one-page business plan, and pricing) (the one number), `an-business-plan-and-money` (Customers and sales: the pipeline, quotes, invoices and getting paid) , `an-business-plan-and-money` (Money each month: the monthly close, cash and runway) , `an-business-record` (The compliance calendar: licenses, permits, reports and taxes) , `an-project-record` (The action log)
Example: https://ancreationoffice.com/example-mousetrap/weekly.csv . A small service business with no invention: https://ancreationoffice.com/example-lawn-service/weekly.csv
Read this once a week, on the owner's day.

WHY THIS EXISTS
A small business is run in the week, not the year. Ten minutes once a week to look at the one number, what's moving, what slipped and the three things that matter next keeps the owner steering instead of reacting. It is the business version of the Project Manager Bot's "What's next?".

WHEN
The owner picks a day (Monday morning is common); write it in office.txt as "Weekly review: <day>". If you can schedule a task, create a weekly routine for that day that brings the review. If you can't, bring it at the first conversation on or after that day. Once a week; if the owner says "skip", skip it and note it in the row.

THE REVIEW (from the records; never from memory)
1. The one number from the business plan: this week, last week, the goal.
2. Sales this week: new leads, quotes out, won, lost (pipeline.csv), invoices sent and paid, and anything overdue (invoices.csv).
3. Money, in one line: cash if the owner has it handy, and anything that changed the monthly picture (`an-business-plan-and-money` (Money each month: the monthly close, cash and runway) does the full close once a month).
4. The action log: what got done, what slipped (and why, in a few words), and anything waiting on someone else for more than a week.
5. The calendar: anything due in the next two weeks (deadlines.csv), and remind-on dates that have come.
6. The three things that matter most next week, picked by the owner; each goes on the action log with a date if it isn't there.
Say it in five or six lines, then ask one question: "Which three for next week?" Offer a default from the records if they'd like one.

THE ROW (weekly.csv)
Week (the Monday's date), the one number, new leads, quotes out, won, invoices sent, paid, overdue, cash (if known), done, slipped, next three, notes. One row per week; never rewritten after the week ends.

THE MONTH AND THE YEAR
The first review of a new month comes with the monthly close. Every quarter, read the last thirteen rows together in a few lines: is the one number moving, what keeps slipping, is the plan still right (`an-business-plan-and-money` (The one-page business plan, and pricing) KEEPING IT CURRENT).

DONE WHEN
Each week has a row, the owner has heard it, and next week's three are on the action log.

## Funding a project (b-funding)
(procedure file: sop-funding.txt)

Procedure: Funding a project (b-funding). Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Source: the programs' own pages and published guidance (below, read through search 2026-10-12). Tier: documented; an accountant and an attorney advise before money is taken. The office never applies, files, signs or contacts a funder.
Read this when the project needs money it doesn't have, before a big spend (tooling, certification, first inventory), or when someone offers to invest.

1. HOW MUCH, FOR WHAT, AND WHEN
- List the next spends from the plan and the cost tracker: prototype, patent, certification and testing, tooling, first inventory. Each with an amount (quote or "not set") and the stage it belongs to.
- Smallest next step first: often the market check and a cheap prototype need almost nothing.

2. THE OPTIONS, BY FIT
- Your own money and early sales: keeps control; pre-orders show demand.
- Licensing: the licensee pays to make and sell it (`an-business-plan-and-money` (Licensing an invention (b-licensing))); often the least money needed.
- Grants and SBIR/STTR: federal research money for small for-profit companies developing technology. SBIR rules: a small business (500 employees or fewer including affiliates), mostly owned by US citizens or permanent residents (rules on investor ownership differ by agency), and the principal investigator employed by the company (NASA: at least 50%). Award sizes and topics change with each agency's solicitation; read the current one. Good fit for technical projects with research risk; not for a finished consumer product.
- Loans: SBA programs and local lenders; check sba.gov for current amounts and terms (the office does not quote loan limits from memory).
- Rewards crowdfunding (Kickstarter and similar): pre-sells the product; needs a working prototype, a cost and delivery plan, and the patent decision first (it is a public disclosure).
- Equity crowdfunding (SEC Regulation Crowdfunding): selling small stakes to the public through a registered platform; the SEC's page gives a limit of $5 million in 12 months (checked through search 2026-10-12; confirm the current figure). Disclosure and filing duties apply.
- Angel investors: individuals or groups investing for a share, usually once there is evidence (customers, a prototype, a team). They own part of the company.

2b. GOVERNMENT MONEY AND FREE HELP: THE MAP (check each program's current page; amounts change)
- Grants that fund starting a business are rare. Federal grants mostly fund research (SBIR/STTR), and a few fund specific places or purposes (rural, export, energy). Offers of "free government grants" for a fee are scams (FTC).
- SBIR/STTR by agency: each agency runs its own. NSF (America's Seed Fund: broad topics, starts with a short Project Pitch); Defense (DSIP portal; the Air Force's AFWERX runs open topics); NIH, DOE, NASA, USDA and others. Find topics on sbir.gov. Register in SAM.gov first (free; it takes time).
- State help for SBIR: many states pay part of a consultant to write a first proposal and match awards (in Wisconsin: the Center for Technology Commercialization, with WEDC's SBIR Advance). Ask the state SBDC.
- Loans: SBA microloans (small, through nonprofits, often with coaching), 7(a) through banks, 504 for equipment and buildings; the state's own loan and guarantee programs (funded through the federal SSBCI; in Wisconsin, WEDC); community lenders (CDFIs) and credit unions; Kiva US 0% crowdfunded loans for small amounts.
- Tax credit: product and process development often counts as research. A young company (under $5 million in gross receipts, within its first five years of receipts) can elect to apply up to $500,000 a year of the federal research credit against its payroll taxes (Forms 6765 and 8974), so it helps even before there's a profit. Many states have their own research credit. The accountant decides what qualifies.
- Veterans: SBA's veteran programs (Boots to Business training, Veterans Business Outreach Centers), and VetCert certification as a veteran-owned or service-disabled veteran-owned small business, which opens federal set-aside contracts. Ask once whether the owner is a veteran.
- Other certifications that open government work: 8(a), HUBZone, women-owned (SBA certifications).
- Selling to the government: SAM.gov registration, APEX Accelerators (free help bidding on government contracts), the agency's own supplier pages (for example DLA).
- Exporting: the U.S. Commercial Service (trade.gov) and the state's STEP program (help with trade shows and export costs).
- Rural: USDA Rural Development business programs, where the business is in an eligible area.
- Free help with all of it: SBDC, SCORE, Women's Business Centers, Veterans Business Outreach Centers, the state's manufacturing extension partnership (in Wisconsin, WMEP), the state economic development agency (WEDC), and in Wisconsin the Technology Council's angel network for investors.

3. WHAT EACH ASKS FOR (prepare from the files)
- Grants and SBIR: the topic it answers, technical objectives, the team, the budget, the commercial potential.
- Lenders: the plan, financial projections, collateral, personal guarantee.
- Investors and equity crowdfunding: the problem, the market evidence, the product, the business model, the team, the money needed and what it buys.
- Office: the funding worksheet (forms-catalog.csv) is filled from what the project already knows; unknowns become questions.

4. WATCH-OUTS
- Equity means sharing ownership and decisions; read every term with an attorney.
- Public campaigns are public disclosures: patent decision first.
- Invention promotion companies that charge up front to fund or market an idea: FTC and USPTO warnings (library).

SOURCES (library)
sheet-funding, sbir, sbir-eligibility, grants-search, sba-grants, sba-lender, sec-reg-cf, sec-ready, sec-early-investors, angel-groups, kickstarter-handbook, score-financial-projections, score-startup-budget, ftc-invention-marketing, uspto-scam-prevention, ftc-grant-scams, nsf-seed-fund, dod-sbir, afwerx, sba-microloans, sba-7a, sba-504, treasury-ssbci, cdfi-fund, kiva-us, irs-research-credit-payroll, sba-veterans, sba-vetcert, sba-certifications, sam-registration, apex-help, dla-business, trade-export-help, sba-step, usda-rural-business, wi-ctc, wedc-wisconsin, wi-tech-council.

HANDS OFF
Accountant (tax and structure), attorney (securities, investment terms, loan documents), the funder's own program staff (the inventor contacts them).

## The funding packet
(procedure file: sop-funding-packet.txt)

Procedure: The funding packet. Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, one packet per invention. b-analyst builds it.
Templates: template-funding.csv (`an-office-files`) and template-business-risks.csv (`an-office-files`) . Builder: funding-packet.py (`an-office-files`)
Example: https://ancreationoffice.com/example-mousetrap/funding-packet.html (its sheets are in the same folder).
May write: everything in AN-Creation/<business>/funding/<invention>/, one line on the Business action log, and a hand-off line to b-project-manager.
Goes with: `an-business-plan-and-money` (Funding a project (b-funding)) (which kind of money fits), `an-business-record` (The business risk register) , `an-cost-and-risk` (Cost sheet) , `an-cost-and-risk` (Risk analysis table)

WHAT IT IS
The pages an inventor hands a lender, an SBDC advisor, a grant reviewer or a partner about one invention. A business with no invention uses the lender or investor packet instead (`an-meetings` (Meeting prep)): they work from the business plan and show break-even. Six pages: executive summary, product and market, cost and unit economics, funding request and milestones, business risk register, and the design risk analysis as an appendix. A reviewer reads page 1 and decides whether to read the rest, so page 1 carries the verdict, the four key numbers, what it would take, the top risks and the ask.

WHO OWNS WHAT
b-business-manager owns the packet: the price, the funding request, the use of funds, the business risk register, and the call on when it is ready to show anyone.
b-project-manager owns the product numbers: the cost sheet, the risk table, the decision log, the action log and the milestone dates. b-business-manager never retypes or edits them. It asks for current copies (office-handoff: one line in AN-Creation/handoffs/for-b-project-manager.txt, "copies of cost-sheet, risk-table, decision-log, actions and intake for the funding packet") and uses what comes back.

THE FOLDER: AN-Creation/<business>/funding/<invention>/
  intake-001.csv      copy of the invention's intake form, from b-project-manager
  cost-sheet.csv      copy, from b-project-manager
  risk-table.csv      copy, from b-project-manager
  decision-log.csv    copy, from b-project-manager
  actions.csv         copy, from b-project-manager
  funding.csv         b-business-manager's: product name, price, volumes, owner's money, uses of funds, milestones (template-funding.csv)
  business-risks.csv  b-business-manager's: the business risk register (`an-business-record` (The business risk register))
  funding-packet.html the packet. Print it or save it as PDF. Each build replaces it; a packet that was sent to someone is copied to History/ with the date and who got it.
The copies are dated by the hand-off line that brought them. Before a build, check that none is older than the last change b-project-manager logged; if one is, ask for it again.

BUILDING IT
b-analyst runs: python3 funding-packet.py AN-Creation/<business>/funding/<invention>
Every figure is computed from the sheets: piece cost (material plus process, all rows), tooling (all rows, once), what each unit clears at the price, gross margin, the units it takes to pay back the tooling, the price that pays it back over the plan volume, and the tooling the price can carry. Nothing on the packet is typed in by hand.
In funding.csv, a value with source "illustrative" prints with a small i mark. A real packet has none. Remove the marks by replacing the values, never by changing the source.

After the meeting it was built for, the packet is kept as given and its sheets are parked. For the next investor or lender, dust it off (`an-project-record` (Living and parked documents) DUSTING ONE OFF): bring in what changed since, rebuild, park again.

THE VERDICT ON PAGE 1
The packet says plainly whether it is ready to ask for money. It is ready when the tooling pays back within the plan volume (annual units times years) at the stated price. If it does not, page 1 says so, gives the numbers, and shows the three levers: the price that would close it, the tooling the price can carry, and the volume it would take. A packet that hides a gap does not get funded twice. Say it in one line to the inventor before anything else: "At $0.45 each trap clears $0.05, so the molds take 2.1 million traps to pay back. Here's what would change that."

HONESTY RULES
- Never invent a price, a quote, a buyer, a sales figure or a test result. A number nobody has said is a placeholder: write it as one, with where the real number will come from.
- Mold and tooling figures say quote or placeholder, and the quote's date.
- "What buyers have said" is the inventor's words or "Not known yet."
- No projections past what the sheets support: no five-year revenue curve from a guess.
- The packet is prepared for review. b-business-manager never sends it. The inventor sends it, and the record says who got which version.

WHEN TO REBUILD
When a quote arrives, the price changes, a risk changes level, or a milestone date moves. Rebuild before every meeting where it will be shown.

## Licensing an invention (b-licensing)
(procedure file: sop-licensing.txt)

Procedure: Licensing an invention (b-licensing). Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Source: licensing practice from published inventor and licensing sources (below, read through search 2026-10-12). Tier: documented; an attorney writes and reviews any agreement. The office never contacts a company, sends a submission or signs anything.
Read this when the route is licensing (a company makes and sells it and pays a royalty), when it's time to approach companies, or when an offer arrives.

1. BEFORE APPROACHING ANYONE
- Market check done (`an-market-and-sources` (Market check: does anyone want it? (b-market-check))): who buys it and why.
- Patent status settled: at least a provisional application filed, by the inventor or an attorney, lets the inventor say "patent pending" for its year; an issued patent, a working prototype, and interest from retailers or big customers all strengthen the position (Stephen Key).
- Company in place if money will change hands (b-company-setup).

2. THE SELL SHEET (one page)
- A headline with the product name; a one-line benefit statement: why people want it.
- The problem it solves and who it is for.
- A picture: a drawing, a render, or a photo of the prototype.
- Three to five key features as short bullets.
- Patent status ("patent pending") in small print, only if filed.
- Contact information.
- Look like the licensee's own products: model the layout on how that company presents what it already sells. A graphic designer is worth it.
- Short video showing it working, if there is a prototype.
- Office: the sell sheet shows what it does, not how it is made; check it against the patent decision before it goes out.

3. FINDING LICENSEES
- Companies already selling to the same buyers in the same stores or catalogs (often the makers of the products the market check found).
- For each: what they make, who buys it, how they take outside ideas.
- Many companies only accept ideas under their own idea submission terms: read those terms closely before submitting; they can waive rights, so it is a one-way door (with an attorney if the money allows).
- Office: the list is research from public sources, marked "not contacted". The inventor contacts companies.

4. THE APPROACH
- A short note or email: who you are, why this company, the one-line benefit, the sell sheet attached, and a follow-up date.
- Keep a log: company, contact, date, what was sent, the reply, next step (actions.csv, and the correspondence log).
- For a meeting with a company, build the licensee packet: `an-meetings-advisors` (The licensee packet)

5. THE DEAL (with an attorney)
- Royalty: a percentage of net sales is common; Stephen Key reports about 5% of net sales as the standard he has seen, and rates vary widely by industry and how significant the invention is. Never promise a rate; it is negotiated.
- Terms to understand: exclusive or not, territory, minimum royalties or performance, upfront payment, who pays to patent and defend, sublicensing, audits, term and termination, what happens to improvements.
- WIPO's Successful Technology Licensing (free, library) explains each term. The attorney writes and reviews the agreement.

SOURCES (library)
wipo-licensing, sell-sheet-primer, stephen-key-licensing, uspto-provisional, patent-grace-periods, sheet-launch, sheet-economics, uia-inventors, uspto-scam-prevention, ftc-invention-marketing (avoid invention-promotion companies that charge to "license" an idea).

HANDS OFF
Patent attorney (what may be shown); licensing or business attorney (submission terms, the agreement).
