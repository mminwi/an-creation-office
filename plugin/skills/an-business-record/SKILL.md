---
name: an-business-record
description: "Use for the business's required record, the company, the compliance calendar, contractors and first hires, business risks."
---

# an-business-record

Sections: The business record; b-business-manager; The compliance calendar: licenses, permits, reports and taxes; Contractors and first hires; contractor agreement terms checklist; The business risk register.

## The business record
(procedure file: sop-business-record.txt)

Procedure: The business record. Revision 9 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, one set for the business (all inventions). b-analyst fills and updates them, and runs tax-year.py.
May write: the files named below in AN-Creation/<business>/, their readable copies in Your files/Business record/, and hand-off lines to b-project-manager.
Goes with: `an-principles-bm` (Principles: the Office Manager Bot) , `an-project-record` (The project record) (the Project Manager Bot's seven)
Builder: tax-year.py (`an-office-files`) . Example: https://ancreationoffice.com/example-mousetrap/ (expenses.csv, trips.csv, correspondence.csv and correspondence/, deadlines.csv, business-decision-log.csv)

WHY THIS EXISTS
A business is judged on its records: by the accountant at tax time, by a lender, by an investor, by an auditor, by the inventor a year from now trying to remember who said what. Most inventors keep these in their heads and a shoebox of receipts, and rebuild them in April. The bot is in the conversation when things happen, so it writes them down when they happen. Tax time becomes a sort, not a hunt.

THE SEVEN (the business has all of them from the first conversation; none is optional)
1. Company record: the company, its papers, accounts, insurance and registrations, each with its honest status. business.txt and company.csv (template-company.csv). Never full tax IDs, account numbers or passwords.
2. Decision log: every business call, dated, with the reason. business-decision-log.csv (template-business-decision-log.csv; same rules as `an-project-record` (Decision log)).
3. Action log: who owes what, by when; suggestions until they get an owner or expire. actions.csv (`an-project-record` (The action log)).
4. Contacts and the correspondence log: everyone the business deals with (contacts.csv), and everything that went between the company and them: one folder per email, file transmittal, meeting or call, named YYMMDD-NN-X-slug, with the email, its attachments, the CAD as sent and the meeting notes, and its row in correspondence.csv (template-correspondence.csv; `an-correspondence`). One log for the whole company; b-project-manager files what goes out about an invention.
5. Trip log: every business trip: date, where (place and address), who or what, the business purpose, odometer or miles, parking and tolls; plus an odometer row for each vehicle at the start of each year and when it is first used for the business. trips.csv (template-trips.csv).
6. Expense ledger: every dollar the business spends, whichever bot hears of it: date, who was paid, what, the business purpose, the invention, the tax category, amount, how it was paid, whose money, the receipt file, the trip or meeting it belongs to. expenses.csv (template-expenses.csv).
7. Deadlines: every date that cannot be missed (patent, trademark, company reports, taxes, contract notices, quotes), each traced to its source (`an-principles-bm` (Watch the calendar)). deadlines.csv (template-deadlines.csv).
Working files alongside them: business-plan.csv (`an-business-plan-and-money` (The one-page business plan, and pricing)), pipeline.csv and invoices.csv once the business sells (`an-business-plan-and-money` (Customers and sales: the pipeline, quotes, invoices and getting paid)), monthly.csv (`an-business-plan-and-money` (Money each month: the monthly close, cash and runway)), weekly.csv (`an-business-plan-and-money` (The weekly review)), people.csv (`an-business-record` (Contractors and first hires)), market-evidence.csv, promo-log.csv, funding/, record/ (the bots' own conversations; internal, not correspondence). The deadlines are also the compliance calendar (`an-business-record` (The compliance calendar: licenses, permits, reports and taxes)). With no invention, the business is the project, and these are its record.

BE INSISTENT (the part that makes it work)
The record is only as good as what the bot is told, so the bot asks, every time, without waiting to be asked:
- A trip, a visit, a show, a meeting, a call, a purchase, an order, a fee, a decision mentioned in passing ("I ran out to the molder yesterday", "I bought filament", "the banker said no"): stop and capture it in the same turn. Ask for what is missing, one thing at a time: the date, the miles or odometer, the amount, the receipt (a photo is fine), the business purpose, who was there. Then carry on with what the inventor wanted.
- Start of every conversation, after the version check: "Anything since last time I should log: trips, calls, meetings, emails sent or received, anything you paid for?" One line. Every time.
- After every meeting or call: the notes in its correspondence folder, its correspondence row, the trip row, and any costs, before the meeting is closed.
- Every email or file that goes out or comes in: the sent copy (not the draft) and its attachments in a dated correspondence folder; for CAD and drawings, the exact files and revision (`an-correspondence`).
- A receipt missing after a week, a trip without miles, a cost without a purpose: ask again at the start of the next conversation, briefly, until it is closed or the inventor says it is gone (then the row says so).
- Month end (the first conversation of a new month): a two-line close: what was logged last month, what is still missing.
- Insistent is not nagging: one short question at a time, never a lecture, and the inventor can say "later". Later goes on the action log with a date.
Write it the same day. A log written at the time is worth far more to the accountant than one rebuilt months later; the logged on column shows when each row was written.

MONEY, ONCE
The expense ledger is the business's one tax record. A cost for an invention also goes on that invention's spending register (b-project-manager's, `an-project-record` (The spending register)): whichever bot hears of it writes its own row and sends a hand-off line to the other, with the same amount from the same receipt. The ledger's "on spending register" column says yes. The amount always comes from the receipt or invoice, never from memory.

TAX TIME
- Categories: use the category names in that year's IRS instructions for the inventor's return (for a single owner, usually Schedule C), or the accountant's own list once there is one. Read them from the form's instructions for that year; until they are read, the category is "ask accountant". Never a category from memory (`an-principles-core` (Trace every spec to its source)).
- Mileage: the trip log keeps the miles. The rate is that year's IRS standard mileage rate, read from the IRS notice for that year, or actual costs if the accountant chooses; tax-year.py only applies a rate given with its source.
- What the records need: the IRS publications are the source (Publication 463 for travel and car expenses, Publication 583 for business records, both in the library). The trip log's columns follow what they and the accountant ask for; check them against the current publication each year.
- At year end: python3 tax-year.py AN-Creation/Business <year>. It writes tax-year-<year>.txt: totals by category and by whose money, business miles, and every gap (no receipt, no purpose, no category, logged late). Close the gaps, then the inventor takes the summary, the ledger, the trip log and the receipts folder to their accountant or tax software. For a meeting with an accountant, build the accountant packet (`an-meetings-advisors` (The accountant packet)).
- The bot sorts and checks; it does not decide what is deductible. On the inventor's own money, doing their own return is their call; once there is real income, an employee, outside money or a company, an accountant is worth the fee (`an-principles-core` (Rigor scales with whose money is at risk)).

THE HARD LINES
- Living or parked (`an-project-record` (Living and parked documents)). Living, updated the turn something happens: the decision log, the action log, contacts and the correspondence index, the trip log, the expense ledger, the deadlines. Parked until a trigger: the company record. Packets are built for a meeting, kept as given, and their sources parked again afterwards.
- Never invent an amount, a mile, a date or a purpose. A missing fact stays missing and is asked for.
- Never store full tax IDs, account or card numbers, or passwords. "Owner's personal card" is enough.
- The inventor can see all seven at any time: b-analyst keeps a readable copy in Your files/Business record/ (python3 record-view.py AN-Creation/Business "<Your files>/Business record"; record-view.py (`an-office-files`)).

## b-business-manager
(procedure file: sop-company.txt)

Procedure: b-business-manager. Setting up and keeping the company. Revision 6 — October 18, 2026.
Index: the procedure index in `an-office`
Goes with: `an-office-manager`
Read this when the business name, forming a company, the tax ID, a bank account, insurance, licenses or the yearly paperwork comes up. Then leave it.

WHY
A company keeps the inventor's personal money apart from the business's risks, makes them look real to buyers and suppliers, and keeps taxes clean. It's set up once, whether they have one product or twenty. You prepare, explain and keep track; the inventor decides, signs and files. Forming a single-owner LLC, getting a tax ID and opening a bank account are routinely done by the owner; bring in an accountant or attorney when other people's money, partners, employees or a binding contract are involved (`an-principles-core` (Rigor scales with whose money is at risk)). You are not their lawyer or accountant.

ONE STEP AT A TIME (each is a row in actions.csv until it's done)
1. Timing. Ask once: "Are you selling, signing with a supplier, or taking money from anyone in the next few months?" No: it can wait; record "for now" with a date. Yes, or a product could hurt someone: forming a company comes first. One fact first: "A company (usually an LLC) can keep a claim against the business away from your house and savings."
2. The name. Brainstorm a few with them. For each favorite, search, then say what you found in a line or two:
   - The web: a plain search for the name. Who's out there, what they do, and where they are.
   - LinkedIn: companies with the same or similar names.
   - Their state's business registry (Secretary of State business search): is it taken in their state?
   - USPTO trademark search, https://tmsearch.uspto.gov/ : is it a registered trademark for the same kind of product?
   Set expectations plainly, in Mike's words: it is very common for other companies to have your name, or one close to it. Don't be afraid of something similar. A company with the same name six states away, in a different line of work, usually isn't worth worrying about; the chance of growing big enough to collide with them is rare. The same name in the same state, or a registered trademark for the same kind of product, is a real problem; pick another, or ask an attorney. Everything in between is judged on its own merits.
   Practical tests for a name (share the ones that matter, not a lecture):
   - Say it out loud and over the phone: easy to say and spell, no odd spellings.
   - It hints at what they do, or at least doesn't suggest something they don't.
   - Room to grow: they'll likely have more than one product, so don't tie the company name to one product or one town unless they mean to.
   - Not confusingly close to a direct competitor in their own field.
   - A few opinions, not a committee; it's their call.
   - Selling abroad later? Check it doesn't mean something unfortunate elsewhere.
   After those searches, if they're comfortable, they have a name they can work with. Record the searches and what was found in record/ with the date.
3. The form. Lay out the usual choices in plain words: sole proprietorship (nothing to file, no protection), LLC (the common choice for one person; protection, simple taxes), corporation (for outside investors later). Recommend they confirm with an accountant. Don't decide for them.
4. Forming an LLC. In their state: Articles of Organization filed with the Secretary of State (a fee, usually $50 to $500), a registered agent (they can be their own, or pay a service), and an operating agreement (a short document even for one owner). Show them the state's own filing page; warn that look-alike sites charge extra for the same filing. Some states require a publication notice or a yearly report; check their state.
5. The tax ID (EIN). Free from the IRS in minutes, https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online . They apply themselves; it's needed for the bank account. Never pay a site for an EIN.
6. A business bank account, in the company's name, with the EIN and formation papers. All business money goes through it, never mixed with personal money (mixing can undo the protection). Compare two or three: a local bank or credit union (often helpful later for a loan), and an online bank. Check fees, minimum balances, how deposits and transfers work, and that it is FDIC- or NCUA-insured (FDIC BankFind, NCUA locator; an app is often a front end for a partner bank). A business credit card from the same bank keeps business spending separate and builds the company's credit.
7. Bookkeeping. A simple tool or a spreadsheet from day one; keep every receipt (record/). An accountant can set it up in an hour.
8. Insurance. General liability when they start selling or showing in person; product liability before a product reaches customers (buyers and stores often ask for a certificate). Get two or three quotes. Tie it to the product's risks in Office files. For the meeting with an agent, build the insurance packet (`an-meetings-advisors` (The insurance packet)).
9. Licenses and sales tax. A local business license if their city or county wants one; a sales tax permit in their state if they sell taxable goods directly. Check the state and city sites (SBA licenses and permits page). Many states have one portal that forms the company and registers it for state taxes at once (in Wisconsin, the One Stop Business Portal; the Department of Revenue issues the seller's permit).
10. Trademark (later, when the name is settled and they're selling or about to): the owner can file at the USPTO themselves with what the office prepares (the search and the application), or use an attorney; USPTO filing has its own fees.

TAXES ONCE IT'S RUNNING (an accountant sets this up; you keep the dates)
- A one-owner LLC is taxed through the owner's personal return by default; the owner usually pays self-employment tax and quarterly estimated taxes once there is profit (IRS estimated taxes page; IRS Publication 334 is the plain guide).
- Keep receipts and mileage from day one; product development spending can count toward the federal research credit, which a young company can use against payroll taxes (`an-business-plan-and-money` (Funding a project (b-funding))).
- Sales tax: collect and file on the state's schedule if registered.

THE FIRST EMPLOYEE (when it comes up)
Before anyone is paid wages: register as an employer with the state, set up withholding and payroll (a payroll service is usually worth it), Form I-9 for every hire, state new-hire reporting, unemployment insurance, and workers' compensation insurance. Contractors (a 1099, not wages) are different; the test is how the work is controlled, and an accountant should confirm it (SBA hire and manage employees).

OTHER IDS THAT COME UP
- D-U-N-S number: some retailers and large customers ask for one; it's free from Dun & Bradstreet (paid "expedited" offers are optional).
- SAM.gov registration and Unique Entity ID: needed for federal grants, SBIR and government contracts; free. Never pay a site to register in SAM.

KEEPING IT (put each on the calendar in actions.csv)
Yearly state report and fee, registered agent renewal, the domain renewal, insurance renewal, tax dates their accountant gives them. Remind a month ahead.

RECORD
business.txt: the company in one page: legal name, form, state, date formed, EIN (last four digits only, never the full number), registered agent, bank (name only), accountant, attorney, insurance carrier and renewal date. Never store full ID numbers, account numbers or passwords.

Sources: SBA business guide https://www.sba.gov/business-guide ; choosing a structure https://www.sba.gov/business-guide/launch-your-business/choose-business-structure ; registering https://www.sba.gov/business-guide/launch-your-business/register-your-business ; EIN https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online ; trademark search https://tmsearch.uspto.gov/ ; free mentoring: SCORE https://www.score.org , Small Business Development Centers https://americassbdc.org , Women's Business Centers and Veterans Business Outreach Centers (SBA resource partners); banking: FDIC BankFind https://banks.data.fdic.gov/bankfind-suite/bankfind ; taxes: IRS small business center https://www.irs.gov/businesses/small-businesses-self-employed ; Wisconsin: One Stop Business Portal https://openforbusiness.wi.gov/ . Library ids: sba-bank-account, fdic-bankfind, ncua-locator, sba-licenses-permits, irs-sbse-center, irs-pub-334, irs-estimated-taxes, sba-hire-employees, uscis-i9, duns-number, sam-registration, wi-onestop, wi-dfi, wi-dor-btr.

MEETING AN ATTORNEY
For forming the company with an attorney, or any agreement before it is signed, build the business attorney packet (`an-meetings-advisors` (The business attorney packet)).

## The compliance calendar: licenses, permits, reports and taxes
(procedure file: sop-compliance-calendar.txt)

Procedure: The compliance calendar: licenses, permits, reports and taxes. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. b-analyst finds the sources. May write: rows in deadlines.csv (template-deadlines.csv), company.csv (registrations and their status), and rows on the action log.
Goes with: `an-principles-bm` (Watch the calendar) , `an-principles-core` (Trace every spec to its source) , `an-business-record` (b-business-manager) , `an-business-record` (The business record) (deadlines)
Example: https://ancreationoffice.com/example-mousetrap/deadlines.csv . A small service business with no invention: https://ancreationoffice.com/example-lawn-service/deadlines.csv
Read this once the business, its state and its type of company are known, when it forms or changes form, when it starts selling, and at the start of each year.

WHY THIS EXISTS
A missed annual report can get a company dissolved; a missed sales-tax return brings penalties; a missing local license can close a shop. None of it is hard, but it is scattered across the IRS, the state, the county and the city, and every place is different. The calendar puts every date in one list, each traced to the page that sets it.

WHAT GOES ON IT (only what applies to this business, from where it is and what it does)
- Federal: estimated tax payments if the owner expects to owe (IRS Form 1040-ES and its instructions for that year), the business's own return and its due date, payroll filings once there is an employee, information returns for contractors paid over the threshold in that year's IRS instructions, and any federal filing the company type requires.
- State: the company's annual or biennial report (the secretary of state or the state's business filing office), the state income or franchise tax, the seller's permit or sales-tax registration before the first taxable sale and its filing schedule, unemployment insurance once there is an employee.
- County and city: a general business license, a home-occupation permit, zoning, health or food permits, signs, fire inspection: whatever that place requires for this kind of business.
- The trade: a license for the trade itself (contractors, food, cosmetology, child care, alcohol and others), and its renewals and continuing education.
- Contracts and insurance: renewal dates, notice periods, the lease.
- Patent and trademark dates come from those procedures and sit on the same calendar.

HOW EACH DATE GETS ON IT
1. Find the source: the official page of the agency that sets the rule (IRS, the state's revenue department, the secretary of state, the county or city clerk), opened in this run. Library entries first (`resources.txt` (`an-office-files`)). Never from memory: a date or a rule without a source is a row marked "to find", and it is said that way to the owner.
2. Write the row in deadlines.csv: the due date, what, why it matters, the source, its edition or date, the clause or page, the source text, the source status, the date checked, a remind-on date (two to four weeks ahead, longer for anything that needs an accountant or attorney), who does it, and status.
3. A registration that doesn't exist yet but will be needed (a seller's permit before the first sale) is a row with the event as its trigger and the planned date; it moves when the plan moves.
4. Recurring dates (quarterly, yearly) get the next one as a row; when it's done, the next one is added the same turn.
5. Where the rule depends on a judgment (is this taxable here, is this person a contractor or an employee), the row says so and points to the professional or the agency's own guidance. The bot does not make the call.

KEEPING IT
- The start of every conversation brings anything whose remind-on date has arrived, in one line each.
- At the start of each year, b-analyst re-opens every source and checks the dates, rates and thresholds for the new year; changes go on the row with the new edition.
- Done rows stay, marked done with the date and how (confirmation number's last digits at most, never a full ID).

DONE WHEN
Every federal, state, local and trade requirement that applies to this business is a row with a source, or a row marked "to find" with a date to find it.

## Contractors and first hires
(procedure file: sop-contractors-and-hiring.txt)

Procedure: Contractors and first hires. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. b-analyst finds the sources and drafts. May write: people.csv in the business folder (template-people.csv), its readable copy in Your files/Business record/, a draft agreement in the correspondence log once it goes out, rows in deadlines.csv, company.csv and the action log, and hand-off lines to b-project-manager.
Goes with: `an-principles-core` (Trace every spec to its source) , `an-principles-core` (Rigor scales with whose money is at risk) , `an-business-record` (The compliance calendar: licenses, permits, reports and taxes) , `an-meetings-advisors` (The business attorney packet) , `an-meetings-advisors` (The accountant packet)
Example: A small service business with no invention: https://ancreationoffice.com/example-lawn-service/people.csv
Templates: template-people.csv (`an-office-files`) , `an-business-record` (contractor agreement terms checklist)
Read this when the owner is about to pay someone to do work for the business: a freelancer, a CAD designer, a bookkeeper, a helper, a first employee.

WHY THIS EXISTS
The first person a small business pays is often where the paperwork goes wrong: no signed agreement, no tax form collected, a "contractor" who is really an employee, or, for an inventor, a CAD designer who still owns the drawings. Each is cheap to get right before the work starts and expensive after.

CONTRACTOR OR EMPLOYEE (the bot never decides it)
Whether someone is a contractor or an employee is not the owner's choice or the bot's; it follows from how the work is actually done. The sources are the IRS's guidance on independent contractor or employee (behavioral control, financial control, the type of relationship; library: irs-contractor-or-employee, and Publication 15-A section 2, library: irs-pub-15a), IRS Form SS-8 when it is unclear (library: irs-form-ss-8), the U.S. Department of Labor's guidance under the Fair Labor Standards Act (dol.gov, Wage and Hour Division, misclassification; not yet in the library: its site refused the office's check on 2026-10-18), and the state's own rules, which can be stricter. Open the current page of each before relying on it (`an-cost-and-risk` (The source check)); none of it is quoted from memory.
- Ask the plain facts, one at a time: who decides how and when the work is done, whose tools and place, paid by the job or by the hour, do they work for others too, is it ongoing or one project, is it the core work of the business.
- Lay the facts next to the sources and say what they point to, in plain words, with the source. When they point both ways, say so, and say who can answer: the accountant, the SBDC, an employment attorney, or the IRS through Form SS-8.
- Record the facts, the sources and the owner's decision in the business decision log.

HIRING A CONTRACTOR
1. The agreement first, before work starts. Draft it from the terms checklist (`an-business-record` (contractor agreement terms checklist)): the work and what's delivered, the price and when it's paid, the dates, who owns what's made (for drawings, CAD, code, designs, photos and text: assigned to the business in writing), confidentiality, that they are independent (their tools, their schedule, their taxes), and how it ends. On the owner's own money, a plain agreement both sign is the start; where the work matters to the business (the product's design, its brand, its code) or real money is involved, the draft goes to an attorney (`an-meetings-advisors` (The business attorney packet)) before signing. Say so once, plainly.
2. Their tax form before the first payment: in the U.S., Form W-9 (their name, tax ID and type of business; library: irs-form-w-9), kept in the business folder's private records. Never copy the tax ID into a sheet: people.csv only says "W-9 on file".
3. Pay against invoices, logged in the expense ledger with the person on each row, so the year's total is known.
4. At year end, the information return that applies (Form 1099-NEC for nonemployee pay above that year's threshold, from that year's Instructions for Forms 1099-MISC and 1099-NEC; library: irs-form-1099-nec) goes on the compliance calendar with its due date and source (`an-business-record` (The compliance calendar: licenses, permits, reports and taxes)). The bot totals each person's payments for the accountant; it does not file.
5. For an inventor: anything the contractor makes for the invention (drawings, CAD, prototypes, test results) is assigned to the business in the agreement, and the disclosure history notes what they were shown (`an-meetings-advisors` (The patent attorney packet)). b-project-manager gets a hand-off line so the project record knows who did the work.

THE FIRST EMPLOYEE
An employee brings a set of one-time and recurring obligations; most are where they are because of the state. Start from the SBA's guide to hiring (library: sba-hire-employees) and the state's own pages, and put each on the compliance calendar with its source:
- before the first day: an employer identification number if there isn't one, state employer registration and withholding, workers' compensation insurance as the state requires, unemployment insurance registration.
- on the first days: Form W-4 (library: irs-form-w-4) and the state's withholding form, Form I-9 (library: uscis-i9), state new-hire reporting.
- every pay day and quarter: payroll, withholding and deposits, payroll tax returns (the IRS's employer guides for that year: Publication 15, Circular E, library: irs-pub-15, and Publication 15-A, library: irs-pub-15a).
Payroll is where a payroll service or an accountant earns its fee: say so once, and offer the accountant packet (`an-meetings-advisors` (The accountant packet)). The bot never runs payroll or holds bank access.

THE RECORD (people.csv)
One row per person the business pays for work: name, what they do, contractor or employee (and the date it was decided, with the decision log row), start, agreement (file and date signed, or "not yet"), tax form on file (yes or no; never the number), how they're paid, paid this year (from the expense ledger), year-end form due, status. Contacts.csv has their contact details. Living: updated the turn something changes.

THE HARD LINES
- Never classify a worker on the owner's behalf; lay out the facts and the sources, and the owner decides with their accountant or attorney.
- Never store a tax ID, SSN, bank details or immigration documents in a sheet or a chat. "On file" is enough; the documents stay where the owner keeps them.
- Never send an agreement, a form or an offer; the owner does.
- AI can be wrong, and employment rules differ by state: check the sources before relying on them.

DONE WHEN
Everyone the business pays has a row, an agreement or a dated reason there isn't one, their tax form on file, and their year-end and payroll dates on the calendar with sources.

## contractor agreement terms checklist
(procedure file: template-contractor-terms.txt)

AN Creation template: contractor agreement terms checklist. Revision 1 — October 18, 2026.
Used by: `an-business-record` (Contractors and first hires)
This is a checklist of the terms an agreement with a contractor should settle, so b-business-manager can draft one in plain words. It is not legal text. On the owner's own money, a plain agreement both sign is the start; where the work matters to the business or real money is involved, an attorney reviews the draft before signing (`an-meetings-advisors` (The business attorney packet)). Rules differ by state.

THE PARTIES
- The business (its legal name, or the owner's name if not formed yet) and the contractor (their legal name or business name).

THE WORK
- What they will do, in plain words, and what they will hand over (files, formats, quantities).
- When: start, milestones, the finish date.
- How the work is accepted: who checks it, and what happens if it isn't right (one round of fixes, for example).

THE MONEY
- The price: fixed, by the hour with a cap, or by milestone.
- Invoices: when they send them, and when they're paid (for example 15 or 30 days).
- Expenses: which ones are covered, and only with approval in advance.

WHO OWNS WHAT IS MADE
- Everything made for the business under the agreement (drawings, CAD files, designs, code, photos, text, prototypes, test results) belongs to the business, assigned in writing, including any rights in it.
- What the contractor brought with them stays theirs, with the business allowed to use it as part of the work.
- For an invention: they tell the business about any idea for the product they come up with during the work, and it belongs to the business.

CONFIDENTIALITY
- What they learn about the business and the product stays confidential, during and after the work, with the usual exceptions (already public, already theirs).
- If an NDA was signed earlier, say this agreement keeps it in force.

INDEPENDENT CONTRACTOR
- They decide how and when they do the work, use their own tools and place, may work for others, and pay their own taxes; no benefits.
- These words do not make someone a contractor if the work is really done as an employee would do it (`an-business-record` (Contractors and first hires) CONTRACTOR OR EMPLOYEE).

ENDING IT
- Either side can end it with notice (for example 14 days), with payment for work done and the hand-over of everything made so far.

THE REST
- Which state's law applies.
- How changes are made: in writing, signed by both.
- Signatures and dates.

## The business risk register
(procedure file: sop-business-risks.txt)

Procedure: The business risk register. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, one per invention. Template: template-business-risks.csv (`an-office-files`)
May write: AN-Creation/<business>/funding/<invention>/business-risks.csv and its rows on the Business action log.
Goes with: `an-business-plan-and-money` (The funding packet) (page 5 of the packet). The product's own failure modes are b-project-manager's risk table (`an-cost-and-risk` (Risk analysis table)); this register is the risks to the business.

WHAT GOES IN IT
The risks a lender or partner asks about: Financial (the numbers do not close, the budget does not cover the tooling), Market (no buyer has said yes), Product liability (someone can be hurt), Legal (no company, no insurance, patent position), Supply (one supplier, long lead times), Schedule (a date that everything waits on), and Product (a design risk that also threatens the business; cite the risk-table row, do not copy it).
Fill it from what is already known: the intake's open answers, the cost sheet, the action log, the risk table's severity 9-10 rows. Do not pad it. Eight real risks beat twenty generic ones.

COLUMNS
id (B1, B2...), risk (one plain sentence a lender understands), category, likelihood (1-5), impact (1-5), mitigation (what is being done, specific enough to check), owner, due, status (open, waiting, accepted, closed), source (where the risk came from).

SCORING
Likelihood × impact. 15 and up is High, 8 to 14 Medium, under 8 Low. The packet prints the levels and a 5×5 heat map.
High risks are worked before money is committed. Product safety is worked by severity first, whatever its score (`an-cost-and-risk` (Risk analysis table) SEVERITY FIRST).

KEEPING IT CURRENT
A parked document (`an-project-record` (Living and parked documents)): built for the first packet, then parked. It is reopened by the changes below or dusted off before the next packet, not reworked every conversation.
Every mitigation with an owner and a date is also a row on the action log. Rescore when something changes: a quote arrives, a buyer answers, a company is formed. Closed rows stay; they show a reviewer what has already been dealt with.
