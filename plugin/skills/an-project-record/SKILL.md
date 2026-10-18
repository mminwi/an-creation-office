---
name: an-project-record
description: "Use for an invention's required record: charter, schedule, decisions, actions, suggestions, spending, reminders, living and parked documents."
---

# an-project-record

Sections: The project record; The project charter; Project charter; The schedule and the critical path; Decision log; The action log; Suggestions and actions; The spending register; Reminders and parked ideas; Living and parked documents.

## The project record
(procedure file: sop-project-record.txt)

Procedure: The project record. Revision 6 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one set per invention. b-analyst fills and updates them.
May write: the files named below in Office files/, and their readable copies in Your files/Project record/.
Goes with: `an-principles-pm` (Principles: the Project Manager Bot)

WHY THIS EXISTS
These are the traditional project management tools, and they are required. Engineers often fill them in after the fact, or paste a standard one, so they can say they did it. An AI has no reason to skip them: it can do the analysis for real and write it down in a form a person can check. Filling them in is how the bot shows it has thought the project through, and how the inventor sees that it has.

THE SEVEN (every invention has all of them; none is optional)
1. Project charter and its schedule: what the project is, what is in and out, what done looks like, the budget and the milestones. The baseline everything else is measured against. The schedule keeps the charter's dates, today's forecasts and the slips, with the critical path.
   Office files/project-charter.txt and schedule.csv . Skills: `an-project-record` (The project charter) and `an-project-record` (The schedule and the critical path)
2. Decision log: every call, dated, with the reason.
   Office files/decision-log.csv . Skill: `an-project-record` (Decision log)
3. Action log: who owes what, by when; suggestions sit on it with status suggestion until they get an owner and a date or expire.
   Office files/actions.csv . Skills: `an-project-record` (The action log) and `an-project-record` (Suggestions and actions)
4. Cost sheet: the bill of materials with material, process and tooling for every item, the cost to manufacture, and the tooling amortized over the volume.
   Office files/cost-sheet.csv . Skill: `an-cost-and-risk` (Cost sheet)
5. Spending register: every dollar spent or committed on the project, and whose money it was.
   Office files/spending.csv . Skill: `an-project-record` (The spending register)
6. Risk analysis table: a simplified FMEA, done for real for this product and its processes. To the inventor it is the risk analysis table.
   Office files/risk-table.csv . Skill: `an-cost-and-risk` (Risk analysis table)
7. Engineering change notices: every change to the charter's scope, budget or dates, and every change to a frozen design, as a numbered ECN with its log.
   Office files/ecn-log.csv and Office files/ecn/ . Skill: `an-cost-and-risk` (Revisions and engineering change notices)

WHEN EACH STARTS
- First conversation: decision log, action log, spending register (even if the only line is "nothing spent yet").
- End of fact-finding (S0): project charter, first cost sheet (rough is fine, marked estimate), first risk table.
- From the charter on: ECNs for any change to scope, budget or dates. From design freeze on: ECNs for any design change too.

THE HARD LINES
- Living or parked (`an-project-record` (Living and parked documents)). Living: the decision log, the action log, the spending register and the ECN log are updated the same turn something happens, never "later". Parked: the charter, the cost sheet and the risk table are done properly for their purpose, shared, and parked in plan.md with their reopen triggers; they are dusted off when a trigger happens, not reworked every conversation. The risk table is done for the design, so the design answers the risks, and parked at design freeze.
- Specs trace to their source. A requirement, rating, tolerance, material property or test level on any sheet carries its source, edition, clause, quoted text and source status, and is checked against the document before it is built, bought or tested on (`an-cost-and-risk` (The source check), `an-principles-core` (Trace every spec to its source)). Run check-sources.py before every review and every quote package.
- They are done for real. No pasted standard FMEA, no copied BOM from another product, no round-number cost guesses presented as figures (`an-principles-core` (Never invent facts)).
- The inventor can see all seven at any time: b-analyst keeps a readable copy of each in Your files/Project record/, in the format the inventor chose, and the review page links them. For web pages: python3 record-view.py "<Office files folder>" "<Your files>/Project record" (record-view.py (`an-office-files`); example: https://ancreationoffice.com/example-mousetrap/views/index.html). The inventor is the decision-maker; they review what the bot has thought through.
- A document the inventor has not seen yet is mentioned in one line when it first exists: "Your risk analysis table is up: nine ways it could fail, two worth working now."
- Other working documents (control plan, compliance matrix, test plans, the resource map) are kept as the stages call for them. These seven are the minimum.

FOR b-business-manager
b-business-manager keeps the business's own seven (`an-business-record` (The business record)), including the expense ledger every spending row is copied to.
The funding packet copies the charter's milestones, the cost sheet, the risk table, the decision log and the action log (`an-business-plan-and-money` (The funding packet)). The spending register shows what the owner has already put in.

EXAMPLE
All seven, filled in for one product: https://ancreationoffice.com/example-mousetrap/

## The project charter
(procedure file: sop-project-charter.txt)

Procedure: The project charter. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention. b-analyst drafts it; the inventor approves it.
Template: `an-project-record` (Project charter) . Example: https://ancreationoffice.com/example-mousetrap/project-charter.txt
May write: Office files/project-charter.txt, its readable copy in Your files/Project record/, and a decision-log row when it is approved.
Goes with: `an-project-record` (The project record) , `an-stages` (The project description: what fact-finding delivers) (the long description it summarizes), `an-cost-and-risk` (Revisions and engineering change notices)

WHAT IT IS
A one- or two-page statement of work: what this project will deliver, what it will not, what done looks like, what it may spend, and by when. It is the baseline. Everything after is measured against it, and changing it takes an engineering change notice (ECN). It is not a business plan and not a sales pitch.

WHEN
Drafted at the end of fact-finding (S0), from the project description and the intake. Approved by the inventor: one decision-log row, "Charter rev A approved". Revised only through an ECN, which raises its revision (A, B, C).

SECTIONS (keep each short; a line or a short list)
1. Product: what it is and the problem it solves, in two sentences.
2. Objective: what this project delivers (for example, "a molded, tested trap ready for first orders"), and what it leaves for later.
3. In scope / out of scope: two short lists. Out of scope is as important as in.
4. Success criteria: the few measurable things that mean done (cost per unit, a test passed, a date, a first order).
5. Deliverables by stage: what comes out of each stage the project will run (S0 to S5, `an-stages` (Stages of a project)).
6. Milestones: dated, the same dates as the action log and the funding packet. They are the planned dates on the schedule (schedule.csv, `an-project-record` (The schedule and the critical path)), where the forecasts and the critical path are kept.
7. Budget: what may be spent in total and through the next gate, and whose money it is (the spending register tracks against it).
8. Assumptions and constraints: what is being taken as true (volume, material, channel) and what limits the project (money, time, tools).
9. Top risks: the three that could sink it, from the risk table.
10. Decision-maker and approvals: who decides (usually the inventor alone), and what needs whose yes.
11. Revision: letter, date, and the ECN that made it.

RULES
- Every number is a figure from the files or marked estimate (`an-principles-core` (Never invent facts)).
- Rough is fine at S0 (90% and go). The charter gets sharper through ECNs as the facts come in; it does not wait for certainty.
- Out of scope is written down, so a new idea goes through the scope gate (`an-principles-pm` (Scope gate)) instead of creeping in.

## Project charter
(procedure file: template-project-charter.txt)

Project charter. Template. Office files/project-charter.txt. Replace every line in brackets; delete what does not apply.
Revision: A, [YYYY-MM-DD], approved by [the inventor] (decision log [date])

1. PRODUCT
[What it is and the problem it solves, in two sentences.]

2. OBJECTIVE
This project delivers: [the end state, e.g. a molded, tested product ready for first orders].
Left for later: [what this project does not try to finish].

3. SCOPE
In: [short list]
Out: [short list]

4. SUCCESS CRITERIA (measurable)
- [Cost per unit at or under $__ at __ units a year]
- [Passes __ test]
- [First order or first sale by __]

5. DELIVERABLES BY STAGE
- S0 Fact-finding: [project description, charter, first cost sheet and risk table]
- S1 Design: [...]
- S2 Prototype: [...]
- S3 Tooling: [...]
- S4 Qualification: [...]
- S5 Launch: [...]

6. MILESTONES
- [YYYY-MM-DD] [milestone]

7. BUDGET
Total to launch: $[__] ([estimate or quotes]). Through the next gate: $[__].
Whose money: [the owner's own / a grant / a loan / an investor]. Tracked in the spending register.

8. ASSUMPTIONS AND CONSTRAINTS
- [Volume, material, channel taken as true]
- [Limits: money, time, tools]

9. TOP RISKS (from the risk table)
- [F_] [risk] [what is being done]

10. DECISION-MAKER AND APPROVALS
[Who decides; what needs whose yes.]

11. REVISIONS
A [date] first issue.

## The schedule and the critical path
(procedure file: sop-schedule.txt)

Procedure: The schedule and the critical path. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention. b-analyst runs schedule.py.
May write: Office files/schedule.csv and schedule.html, and the readable copy in Your files/Project record/.
Template: template-schedule.csv (`an-office-files`) . Checker: schedule.py (`an-office-files`) . Example: https://ancreationoffice.com/example-mousetrap/schedule.csv and https://ancreationoffice.com/example-mousetrap/schedule.html
Goes with: `an-project-record` (The project charter) (the milestones), `an-cost-and-risk` (Revisions and engineering change notices) , `an-principles-pm` (When something has to give, ask which)

WHY THIS EXISTS
The charter sets the dates. Things move: a quote is late, a buyer meeting slips, a test fails. Some slips don't matter, because there is spare time after them; some move the end date, because everything after them waits. The schedule keeps the charter's dates, today's forecast and the slip side by side, and the critical path shows which slips move the end.

THE SHEET: schedule.csv (one row per milestone)
- id, milestone: the charter's milestones, plus any step the project waits on that the charter leaves out (a field test, a lab slot).
- depends on: the ids it cannot happen before, space-separated. Leave empty when it waits on nothing in the schedule.
- days after: how long it needs after the last thing it depends on. An estimate, marked as one in the notes until a supplier or a test gives a real number (`an-principles-core` (Trace every spec to its source)).
- planned: the charter's date. It changes only through a change notice.
- forecast: today's best date. A living field: update it the same turn something moves (`an-project-record` (Living and parked documents)).
- actual: the date it happened.
- owner, source, notes: who it waits on, where the date comes from (an action, a quote, the charter), and why the forecast moved.

THE CRITICAL PATH
python3 schedule.py "<Office files>": for each milestone it works out the earliest date its dependencies allow and which dependency drives it; the chain of drivers back from the last milestone is the critical path. It prints the path, every slip (marked CRITICAL when on the path), whether the end has moved, and any forecast that is earlier than its dependencies allow, and writes schedule.html. It changes no dates.

WHAT THE BOT DOES WITH IT
- When something moves (a quote's lead time, a missed due date on the action log, a failed test), update the forecast that turn, run schedule.py, and fix any forecast it says is too early.
- A slip on the critical path: say it in one line with what it moves ("The buyer feedback is two weeks late, and that moves first shipment a week past the charter's date"). Then ask which gives (`an-principles-pm` (When something has to give, ask which)): recover time on the critical path (run things side by side, cut a step, spend to speed up), or accept the new date.
- When the last milestone moves past the charter's date and the inventor accepts it: a change notice for the charter's dates (`an-cost-and-risk` (Revisions and engineering change notices)); planned dates change only then.
- A slip off the critical path: note it in the forecast; no alarm, it uses up spare time.
- Keep it light: the charter's milestones and the few steps between them, not every task. Tasks are the action log's.

WHEN IT STARTS
With the charter, at the end of fact-finding. Living from then on; parked only when the product has shipped.

## Decision log
(procedure file: sop-decision-log.txt)

Procedure: Decision log. Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention (b-business-manager keeps its own in AN-Creation/<business>/). May write: Office files/decision-log.csv.
Template: template-decision-log.csv (`an-office-files`)
Goes with the Decisions section of the project plan. The plan still holds the choice in the inventor's words. This log is the list you look up.

WHY THIS EXISTS
Everyday calls get made in conversation and then disappear: which material, which supplier, which idea to shelve. Write them down the day they are made.

WHEN TO WRITE AN ENTRY
Write one row the same day the call is made. Write a row for a material choice, a supplier pick, shelving an idea, or any other everyday call of that size. One row per call, in the person's words. A mention is not a call. A changed mind is a new row with a new date. Do not delete rows. Delete the example row before the first real entry.

The reason has to stand without the meeting. Say what was chosen, what was set aside, and why. A few words that only repeat the decision are not a reason.

DATE IS THE LOOKUP POINTER
The date column is how you find an entry. There is no separate ID. To look something up, start with the date it was decided, then read the decision and the reason on that row. Write the date as YYYY-MM-DD. Add new rows at the bottom.

COLUMNS
date, decision, reason.

## The action log
(procedure file: sop-action-log.txt)

Procedure: The action log. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Template: template-action-log.csv (`an-office-files`)
Goes with: `an-project-manager`, `an-analyst` (standing context for b-analyst), `an-market-and-sources` (Review pages and dated folders), `an-folders` (project folders)

WHY THIS EXISTS
Inventors rarely keep their own to-do list, and without one they have no record of what they need to do, what they're waiting on, or what got done. So we keep it for them. Every action anyone owes on the project goes in one log: the inventor's tasks, what a supplier or lab owes back, and what b-project-manager or b-analyst promised. It shows on the inventor's review page, always current. Industry calls this an action log, issue log or action item list.

WHERE IT LIVES
This procedure updates Office files/actions.csv.
It may also write Your files/Action log, the previous copy in Your files/History/, and Your files/Review/index.html.
Master: Office files/actions.csv (one row per action; rows are never deleted).
Inventor's copy: Your files/Action log, in their format (usually Excel), regenerated from the master; the previous copy goes to Your files/History/ first.
On the review page: the index (Your files/Review/index.html) shows "Your list" at the top: your open actions, then what you're waiting on from others, then what was done recently. Rebuilt with review.py whenever the log changes.
Git: checkpoint after every change, like everything else.

ONE ROW PER ACTION
ID: A-001, A-002 ... never reused.
Opened: date.
Action: what has to happen, in plain words, specific enough to know when it's done ("Mail the signed NDA to Acme Molding", not "NDA stuff").
Who: You (the inventor), b-project-manager, b-analyst, or a named outside party (the supplier, the lab, the attorney).
Why / from: where it came from: a ticket, a review, a decision, a risk, an email (link the record item).
Due: a date if one was agreed or a deadline exists; blank otherwise. Never invent one.
Status: open, waiting (on someone else), done, or dropped. A suggestion (an idea with no owner or no date yet) is also a row, status suggestion, and becomes an action when both are set (`an-project-record` (Suggestions and actions)).
Done how: in the inventor's words, how it got done ("dropped it at the post office Tuesday", "Acme sent the quote").
Closed: date.
Notes: anything else; follow-ups asked, with dates.

WHEN A ROW IS ADDED
- Anything the inventor agrees to do, in any conversation.
- Anything they're waiting on from someone else: a quote, a sample, a lab result, an attorney's review.
- Anything b-project-manager or b-analyst promised to prepare.
- Each short-list item that needs the inventor to act outside the conversation.
- A "for now" with a small step they took on.
Say it when you add it: "I've put that on your list: mail the NDA to Acme, by Friday."

DONE MEANS DONE
- No checkbox counts as done. A row closes only when the inventor says, in words, that it happened, or the evidence arrives (the quote is in Send to the office, the lab report is filed).
- Ask plainly, without blame: "Did the NDA get mailed?" "Did Acme get back to you?" If not yet: keep it open, note the date asked, offer a new date if they want one.
- On or after a due date, ask once at the start of the next conversation. Waiting items: suggest a nudge after a week ("Want me to draft a short follow-up email to Acme?").
- Dropped is fine: record why. Nothing is deleted.

KEEP IT FOCUSED (D-078)
- One form: the inventor's own actions and everything they're waiting on from other people, together, so they're reminded to chase what's still owed.
- No hard limit on how many rows. But don't get far ahead of them. Their own open actions are usually two to five. Waiting items can be as many as there really are (six suppliers each owing a quote is six rows).
- Only put actions on the log that are in front of them now, roughly the next two weeks. Further-out work stays in b-project-manager's queue and the plan's Later list until it is close. With dozens of open items, one change ripples through three or four of them at once; keep the list on what's in front of them, not what's down the road.
- If their own list starts stacking up, sort it with them: what's really this week, what can wait (back to Later), what can be dropped (`an-focus-and-gateways` (Keep the project focused)).
- The status sheet's "This week" pulls from the log. The work queue (queue/QUEUE.txt) stays b-project-manager's; the log is the inventor's view of who owes what.
- Each invention has its own log. b-project-manager runs every invention, so say which invention an action belongs to.

WHO DOES WHAT
b-project-manager adds and closes rows during conversations and asks the follow-ups. b-analyst adds rows that come out of its runs (a quote to request, a sample to order, a form to sign), checks the log against the record every run, and rebuilds the review page. The inventor does the actions; they never have to maintain the log.

## Suggestions and actions
(procedure file: sop-suggestions.txt)

Procedure: Suggestions and actions. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept in: Office files/actions.csv, the same log as every action (`an-project-record` (The action log)). May write: that file.
Goes with the action log. A suggestion is not an action until it graduates.

STATUS
Suggestion is its own status. It is not a true action. The action statuses stay open, waiting, done, and dropped. Nothing is owed on a suggestion until it graduates.
The action text says what the change actually is, and the notes say what done looks like. A title with no picture of the finished work is not a row.

SOFT-DROP
A suggestion survives the meeting it was raised in, plus one more meeting. If it is not raised again in that next meeting, it expires. The row stays on the log. Expired is the soft-drop.

GRADUATION
Graduation requires an owner and a deadline. Until both are set, it stays a suggestion.
If no deadline is stated, the default is next week.
Once both are set, the row is a true action, status open, with that owner and that deadline.

## The spending register
(procedure file: sop-spending-register.txt)

Procedure: The spending register. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention. b-analyst adds the rows. Template: template-spending-register.csv (`an-office-files`)
May write: Office files/spending.csv and its readable copy in Your files/Project record/.
Goes with: `an-project-record` (The project record) , `an-cost-and-risk` (Cost sheet) (what one unit should cost; this register is what the project has actually spent)

WHY THIS EXISTS
A basic accounting register for the project: how much has gone out, on what, and whose money it was. Inventors lose track of what they have put in, and a lender, an investor or a tax preparer will ask. It is not the company's books (the Office Manager Bot keeps those with the owner's accountant); it is the project's spending, kept as it happens.

COLUMNS
date, stage (S0 to S5), what it was, category (Prototype, Tooling, Testing, Fees, Samples, Services, Travel, Other), vendor or who, amount, committed or paid, paid from, running total, receipt or quote file, notes.
- paid from: Owner (the inventor's own money), or the other party by name: a grant, a loan, an investor, a partner. This is how the register shows out-of-pocket against other people's money.
- committed: an order placed or a quote accepted but not yet paid. It counts toward the budget now.
- running total: the sum of every amount so far, paid and committed.

RULES
- A row the same turn a receipt, invoice, order or accepted quote comes in. A quote not yet accepted is not spending; it goes on the cost sheet.
- Only real amounts. Never estimate a row (`an-principles-core` (Never invent facts)). Hours are optional and go in notes.
- Every row also goes to b-business-manager's expense ledger, the business's one tax record (`an-business-record` (The business record) MONEY, ONCE): send a hand-off line with the date, who was paid, what, the amount and the receipt file. A cost b-business-manager hears of first comes the other way. Same amount, same receipt.
- At each gate, and whenever asked, say in one line: spent so far, how much was the owner's, and what is left in the charter's budget through the next gate.
- When the money stops being only the owner's, say it in one line and follow `an-principles-core` (Rigor scales with whose money is at risk).

## Reminders and parked ideas
(procedure file: sop-reminders.txt)

Procedure: Reminders and parked ideas. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, for each invention it runs. May write: Office files/queue/revisit/, queue/open/ and queue/done/ for reminder files, and AN-Creation/ideas.txt.
Read this when a "for now" answer needs a date, when a reminder comes due, or when a new idea comes up.

Reminders are files. queue/revisit/ holds "for now" answers by date, one file per topic, named YYMMDD-topic.txt with a short plain topic (company, patent, cost-per-lure). Check it at the start of every conversation (office file, START OF EVERY CONVERSATION step 2).
- A reminder that is due today gets asked once today, or they choose a new date. Ticket wording like "don't ask until <date>" no longer applies on that date.
- Before setting a reminder, look for one on the same topic in revisit/ or open/. If there is one, rename it to the new date instead of making another.
- When a due reminder has been asked: if they decided, record the decision and move the file to done/. If it's still "for now", rename it to the new date in revisit/. A reminder never stays in open/ after it's been asked.
- One topic, one file, even when the words differ. A sharper corner and a wet-root try on the same notch are one file. A chewed lid and a morning glance at that lid are one file. Ask a due reminder as the outcome, once ("How did it go?"). Mentioning the day is not the question. Then move it to done/ or rename it in revisit/. It must not stay in open/. A reminder is not a ticket: do not give it a T- number, and do not say it is on their list unless queue/open has a T- ticket for that thing. "I've put that on your list" is only for a row you just added to actions.csv. Do not name a weekday or a date they did not say. Next week stays next week.
- Ideas: check AN-Creation/ideas.txt before adding. One line per idea; if it's already there, leave it.

## Living and parked documents
(procedure file: sop-document-life.txt)

Procedure: Living and parked documents. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: both bots. b-analyst does the dusting off.
May write: the PARKED section of plan.md, and the documents named below when their rule says so.
Goes with: `an-project-record` (The project record) , `an-business-record` (The business record)

WHY THIS EXISTS
Not every document needs watching. An action list changes every time someone follows up; a risk assessment is done for the design, shared, and then left alone until something changes. Treating every document as living wastes the inventor's time and the bot's attention, and a bot that re-analyzes everything every day loses track of what matters today. So every document is one of three kinds, and the bot treats each kind differently.

LIVING: updated every time something happens, the same turn
These are the day-to-day record. Every follow-up, every email, every trip, every cost, every call goes in when it happens. At the start of a conversation the bot looks at these, and only at what is open or due in them.
- Project Manager Bot: action log (actions.csv), decision log (decision-log.csv), spending register (spending.csv), the schedule's forecasts (schedule.csv), the ECN log (a line when a change happens).
- Office Manager Bot: action log, decision log (business-decision-log.csv), contacts, trip log (trips.csv), expense ledger (expenses.csv), deadlines (deadlines.csv), market evidence, the promotion log.
- Both: the correspondence log's index (correspondence.csv), office.txt, plan.md, the hand-off inbox.
Logs are only added to. Read the open rows and the last few lines, not the whole history.

PARKED: done properly for a purpose, then put away until a trigger
These are built when the work calls for them, done for real, shared with whoever needs to see them, and then parked. The bot does not reread or rework a parked document, and does not mention it, until one of its reopen triggers happens.
- Project charter: parked once the inventor agrees it. Reopen: only through an ECN (a change to scope, budget or dates).
- Risk table: worked during design, so the design answers the risks; parked after the design review that freezes the design. Reopen: a design change (ECN), a failed test, a field problem or complaint, a new use or market, or to dust off before showing it to someone.
- Cost sheet: worked during design and quoting; parked once the quotes are in. Reopen: a quote arrives, the design changes, before a price decision or a packet.
- Compliance matrix: worked through design and testing; parked when every line is met or put off. Reopen: a design change, a new market, a new edition of a source it cites.
- Resource map: built at the start. Reopen: the product changes in a way that matters (it gets a battery, it goes to Europe).
- Company record and business risk register: parked after they are set up. Reopen: the company changes (formed, insured, a bank account), money comes in or is borrowed, or before a packet.
- Funding packet, pricing and terms, cash flow, the brand kit: parked after the meeting or launch they were made for. Reopen: the next meeting that needs them.

THE CORRESPONDENCE LOG: never edited (`an-correspondence`)
Everything that went between the company and someone outside it, one folder per correspondence named with its date code and a slug (261017-01-S-molder-a-meeting-request), so they stay in the order they happened: emails with their attachments, CAD and drawings as transmitted, meeting notes, packets handed over, signed agreements. Once filed, never changed; a correction is a new dated folder. Its index, correspondence.csv, is living: a row the same day.
Also never edited once done: an approved ECN, and a tax-year summary given to the accountant.

PARKING A DOCUMENT
When a parked-type document has done its job (the review is held, the meeting is over, the quotes are in):
1. Make sure it is finished: no "to find" rows that the purpose needed, and check-sources.py has nothing under MUST FIX for it.
2. Write one line in the PARKED section of plan.md: the document, the date parked, why ("design freeze X4", "lender meeting 261104"), and its reopen triggers.
3. Tell the inventor in one line, if it matters: "Your risk table is done for this design; I'm parking it until something changes."
At the start of a conversation, the PARKED section is all the bot reads about these documents.

DUSTING ONE OFF
When a trigger happens ("I'm seeing another investor in three weeks", "the molder changed the gate"):
1. Open it, and look at what happened since the date it was parked: the decision log, the action log, the spending register, ECNs and quotes since then. Only that; do not redo the whole analysis.
2. Bring it up to date with those changes. A risk table gets the rows the change touches rescored; a cost sheet gets the new quote; a packet gets this person's ask.
3. Run check-sources.py on it. Anything older than its source's current edition gets checked again.
4. Make what this purpose needs: for a meeting, the new packet copy in that meeting's folder (`an-meetings` (Meeting prep)).
5. One line in the decision log: what changed while dusting it off ("Risk table dusted off for investor B: F2 rescored after the soak test").
6. Park it again with the new date.

RULES
- A living document missing an entry is a gap: chase it (`an-business-record` (The business record) BE INSISTENT). A parked document left alone is not a gap; it is the plan.
- Never re-analyze a parked document just because a conversation started, a week passed, or nothing else is going on.
- When unsure whether something is a trigger, ask the inventor in one line: "The supplier changed the spring wire. Want me to reopen the risk table for that?"
