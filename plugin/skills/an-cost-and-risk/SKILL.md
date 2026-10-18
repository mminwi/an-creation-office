---
name: an-cost-and-risk
description: "Use for the cost to make one, the risk analysis table, design changes (ECNs), and tracing every spec to its source."
---

# an-cost-and-risk

Sections: Cost sheet; Risk analysis table; Revisions and engineering change notices; Engineering change notice (ECN); The source check.

## Cost sheet
(procedure file: sop-cost-sheet.txt)

Procedure: Cost sheet. Revision 7 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention. May write: Office files/cost-sheet.csv.
Template: template-cost-sheet.csv (`an-office-files`)
Goes with the spending register (`an-project-record` (The spending register)), which records what was actually spent. One of the seven required documents (`an-project-record` (The project record)). This sheet is the costed bill of materials, laid out the way it would go into an MRP system: every item, how many, made or bought, and what each costs in material, process and tooling. Its bottom line is the cost to manufacture one unit, with the tooling amortized over the volume.

WHY THIS EXISTS
A part has three kinds of money: the material in it, the process that makes it, and the tooling you pay once. Mixing the tooling into the part price hides it. Leaving it off makes the part look cheaper than it is.

COLUMNS
level, part number, part, qty, unit, make or buy, supplier, what it is, material cost, process cost, how the cost was figured, tooling, tooling notes, annual units, years, amortization, unit cost, running total, share of total.
Level is the item's place in the bill: 1 for what goes straight into the product, 2 for what goes into a level-1 subassembly. The finished product itself is the sheet, not a row, so nothing is counted twice; a subassembly row carries only its own assembly cost, and its parts carry theirs. Part number is the inventor's own (MT-001, MT-002) until a supplier's number exists. Unit is how qty is counted: each, grams, inches, feet. Make or buy says whether it is molded or built for the project, or bought ready-made, and supplier names who makes or sells it (or "to quote"). Qty is how many of that part, in that unit, are in one product. What it is names the part so a person who was not in the room can tell it from the next row: material, rough size, and the job it does. How the cost was figured shows the arithmetic behind material cost and process cost. Tooling notes is where the tooling line splits into mold plus fixtures. Write the amounts there, such as "mold 10000 + fixtures 2000". A tool shared by more than one part is written on one row only, so it is counted once. Say on the other row that the tool is already counted.

ONE ROW PER COMPONENT
Every component gets a row. A product is not costed when the first part has a number and the rest are blank. Pins, latches, labels, and springs are components. A feature molded into another part, such as a spike on a pedal, does not get its own row; name it in that part's description so it is not mistaken for a missing line. Packaging is a different sheet unless the call was to cost the packed unit.

HOW AMORTIZATION WORKS
Amortization is the tooling spread across the units you expect to make.
amortization = tooling / (annual units × years)
The example row: 12000 / (5000 × 3) = 0.80 per unit.
A row with no tooling has amortization of 0. If annual units or years is blank, leave amortization blank. Do not invent a volume.
The unit cost on a row is material cost + process cost + amortization. Write that number in the unit cost column.
The running total is that unit cost added to the running total of the row above. The last row is the cost of one unit of the product.
Share of total is that row's unit cost divided by the last running total. It is the part's share of one unit, not the running total itself. The shares add to 100%. A sheet with one part is 100%.

FOR THE FUNDING PACKET
b-business-manager builds funding packets from a copy of this sheet (`an-business-plan-and-money` (The funding packet)). Keep it ready to copy: every component has a row, every tooling amount says whether it is a quote or a placeholder, and the quote's date and source are in tooling notes. When b-business-manager asks for it, send the current file through the office-handoff skill. Never let anyone retype it.

WHEN TO UPDATE IT
Worked during design and quoting, then parked once the quotes are in (`an-project-record` (Living and parked documents)). The triggers below reopen it.
Update the sheet when the design changes: a part added, removed, or changed in material, process, or tooling. Recalculate that row's amortization, every running total from that row down, and every share of total. A new quote that changes a number is updated the same way. Delete the example row before the first real entry.

## Risk analysis table
(procedure file: sop-risk-table.txt)

Procedure: Risk analysis table. Revision 12 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-project-manager, one per invention; b-analyst fills it. Template: template-risk-table.csv (`an-office-files`) . May write: Office files/risk-table.csv and the matching action rows in Office files/actions.csv.
Goes with the Residual risk principle (`an-principles-pm` (Residual risk: work the 80%)). This note is how a risk table is built. It replaces the one-row-per-failure FMEA. The background on FMEA, control plans and the quality chain is `design-risk.txt` (`an-office-files`) ; where they differ on how to build and score the table, this file wins.

THE TABLE GROWS DOWN
One failure mode can take several rows: the starting condition, one or more mitigation ideas, and a final accepted residual row. Do not add columns for extra mitigations. Add another row.

COLUMNS
id, Failure mode / actions, effect, S, O, D, RPN, status.

FIRST ROW OF A FAILURE
The id (F1, F2, and so on) is the failure mode. Score S, O, and D for what is already proposed, including the equipment and the procedure as specified. An action under it is optional.

NO ACTION
The person can accept that score as it is. The sheet for that failure is one line. Write the RPN on that line and mark it accepted. There is no row under it.
One accepted line can be most of the risk by itself. Then stop. The small items under it do not need to be worked.

NO BOILERPLATE
Many FMEAs are paperwork: a standard sheet for "injection molded part" pasted in so someone can say it was done. This table is the opposite. Every failure comes from this product's own parts, features, materials, assembly steps and use, and each row names the part, feature or process step it belongs to. Walk the product the way it is made and used: each part from the cost sheet, each process step, each way a person sets it up, uses it, misuses it and stores it. A generic failure that could be pasted onto any product does not count as a row until it is tied to a feature of this one. The point is that the bot really thinks the design through, and writes it down so the inventor can check that it did.

WHEN TO WORK IT, AND WHEN TO PARK IT (`an-project-record` (Living and parked documents))
The risk table is done for the design: worked while designing, so you know what you are designing for and the design answers the high-severity rows. It is shared with whoever needs to see it was done. After the design review that freezes the design, park it. Do not re-analyze it every conversation. Reopen it for a design change (ECN), a failed test, a field problem or complaint, a new use or market, or to dust it off before showing it to someone; then rescore only the rows the change touches.

WHEN THE AI FILLS THE SHEET
Be exhaustive, and do the exercise for real. For a design or a process, look for the failures that belong to it, score the proposal, and take actions that actually lower S, O, or D until a lower score is not honestly available.
Stop when the risk is the reason for doing the thing, and the person has already accepted it. Skydiving is the case. The failure is that the parachute does not open. There may still be something to name, because the proposal already uses modern gear and the usual procedure, and that is what you score. Do not keep writing actions whose aim is to make the jump safe. The risk is why they are doing it. Accept the line and move on.

ROWS UNDER THAT ID
Use another line only when an action is taken. Leave the id blank. The action has to lower S, O, or D. Write the new scores on that row. Another action can follow if it lowers the score again. Stop when another action would not get a lower RPN. That last row is the residual. It carries the RPN, and status = accepted when the person signs off.
A mitigation with no owner and no deadline is also a row on the action list, so it is not lost.

STATUS
Blank means still open. Accepted means the person has signed off that residual.
Below threshold means the row is in the last 20% of the risk. It is logged. It is not a sign-off. Do not mark it accepted just because the score is small.
A person is free to keep working a below-threshold row. An obvious fix that does not raise the cost of the product is worth doing. Spending more on one of those, while a higher score is still open, is not. Once 80% of the risk is accepted, the rest are not significant.

SEVERITY FIRST
A failure with severity 9 or 10 (someone can be hurt, or a law or safety rule is broken) gets an action whatever its RPN. It is never marked below threshold. Its residual can be accepted only after an action has lowered S, O, or D, or with the reason it cannot be lowered written on the residual row. Say it to the person in one line before asking them to accept it.

SCORING
RPN = S × O × D, on the residual row. Status says whether that residual was accepted or fell below the threshold.
Add every residual RPN. That sum is the total risk. 80% of that sum is the line to work to.
Rank the residual scores and add them from the top. The row that first carries the running total past 80% is still accepted. Everything after it is the leftover risk. Mark those below threshold, not accepted.
The count of issues on either side of that line is whatever the scores produce. Do not aim for a fifth of the rows. A long list of small issues is easy to write, and the meeting starts to feel pointless. Work the issues that represent 80% of the risk.
Driving a score lower eventually costs more money, or the part takes longer to make. Time is money. Accepting a residual means this is as much as will be spent to lower that issue.
Ask "accept as-is or modify?" only on an open failure. Do not ask it on a row that is already accepted.

FOR THE FUNDING PACKET
b-business-manager's funding packet prints this table as an appendix with the before and after scores (`an-business-plan-and-money` (The funding packet)). Keep the first row of each failure as scored for the proposal, so the before score is never lost.

AT THE BOTTOM
Show the sum of every residual RPN, the accepted portion (the first 80% of that sum), and the leftover.

## Revisions and engineering change notices
(procedure file: sop-change-control.txt)

Procedure: Revisions and engineering change notices. Revision 3 — October 18, 2026.
One of the seven required documents (`an-project-record` (The project record)). May write: Office files/ecn-log.csv, Office files/ecn/, and the readable copy of the log in Your files/Project record/.
Index: the procedure index in `an-office`
Goes with: `an-stages` (Stages of a project), the loops, the compliance matrix, `an-folders` (project folders) (dated folders)

WHY THIS EXISTS
Every loop changes the design, and every change can break something already checked. One rule for naming revisions and one record for changes means anyone can tell which version a part, test or quote belongs to, and what has to be checked again after a change. The AI keeps it; the inventor sees the change and says yes or no.

REVISION NAMES
- Concepts in industrial design passes: C1, C2, C3.
- Working revisions in the design and prototype loops: X1, X2, X3. Each loop round that updates the CAD makes the next X.
- Released revisions, from design freeze on: A, B, C. Freeze releases revision A.
Every drawing, model, BOM, compliance matrix, test result, quote and review record names the revision it belongs to. Each revision lives in its own dated folder (D-029); an old revision is never edited.
At an elevated documentation level, follow the buyer's or program's scheme if it has one.

BEFORE FREEZE (C and X revisions)
Change freely; that's what the loops are for. Each round's review record says what changed and why, and the CAD update makes the next revision. No separate change record needed.

ENGINEERING CHANGE NOTICES (ECNs)
An ECN is the change record. Each one is a numbered file, Office files/ecn/YYMMDD-ECN-<number>-<slug>.txt (template `an-cost-and-risk` (Engineering change notice (ECN))), and one row in Office files/ecn-log.csv (template template-ecn-log.csv (`an-office-files`)): number, date, what changes, why, from and to revision, cost and time, decision, status (open, approved, rejected, done). The log is what the inventor reads; the file has the detail.
An ECN is required for:
- Any change to the project charter's scope, budget, milestones or success criteria, from the day the charter is approved (`an-project-record` (The project charter)). The charter's revision letter goes up when the ECN is approved.
- Any change to a frozen design (below).
Before freeze, design changes inside the loops need no ECN; the review records cover them.

AFTER FREEZE (released revisions)
Every change gets an ECN, in its own dated file:
- Number and date (ECN-001, ECN-002; older projects may have CR- numbers, which stay as they are).
- What changes: the part, drawing, process, supplier, tool, fixture, gauge, or label.
- Why: the reason, the test or report that started it (link to the test, report or complaint).
- What it touches: compliance matrix lines, FMEA lines, critical features, control plan checks, certifications, tooling, stock on hand.
- What has to be re-checked: the tests and inspections those lines need, any qualification it affects (vendor, machine, tool, fixture, gauge), and whether a certification lab must be told.
- Cost and time: what the change costs, and how it moves the timeline.
- Decision: the inventor's yes or no, and any buyer approval the buyer requires.
- Done: the new revision letter, the re-checks passed, and the date it takes effect (which batch or serial number).

WHAT A CHANGE MUST RE-CHECK
- Anything on a compliance matrix line the change touches is re-verified.
- A change to a critical feature re-runs its check and updates the control plan.
- A change to the vendor, a machine, a tool, a fixture or a gauge repeats the qualification it touches (`an-tooling-and-launch` (Qualification and production approval)).
- A change that could affect a certification (FCC, UL, CE, medical, aviation) is checked against the tested configuration before it ships; the lab may need to be told.
- Labels, instructions, the buyer packet and listings are updated when the change shows up there.

SAFETY
A safety fix is never held back by paperwork. Make the fix and contain the risk first; complete the change record right after.

WHO DOES WHAT
b-analyst writes the ECN and its log row, works out what it touches and what must be re-checked, and tracks it to done. b-project-manager shows it to the inventor in plain words and records the decision. The inventor approves; the office never approves for them or tells a supplier or lab without them.

## Engineering change notice (ECN)
(procedure file: template-change-record.txt)

Engineering change notice (ECN). Template. For a change to the charter's scope, budget or dates, or to a frozen design. Save as Office files/ecn/YYMMDD-ECN-<number>-<slug>.txt and add its row to Office files/ecn-log.csv.
ECN no.: ECN-
Date:
What changes: (charter scope, budget or dates; part, drawing, process, supplier, tool, fixture, gauge, label)
From revision: To revision:
Why: (reason, and the test, report or complaint that started it)
What it touches: (compliance matrix IDs, FMEA lines, critical features, control plan checks, certifications, tooling, stock on hand)
What must be re-checked: (tests, inspections, qualifications; tell a lab?)
Cost and time:
Decision: (inventor yes/no; buyer approval if required)
Done: (re-checks passed, date or batch it takes effect)

## The source check
(procedure file: sop-source-check.txt)

Procedure: The source check. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: both bots. b-analyst does the second-pass check and runs check-sources.py.
May write: the source columns of any sheet that carries specs or rules (the compliance matrix, deadlines.csv, resource-map.csv, and any sheet that has the columns), and project procedures in procedures/ of the invention or Business folder.
Principle: `an-principles-core` (Trace every spec to its source)
Checker: check-sources.py (`an-office-files`) . Goes with: `an-market-and-sources` (Map the resources to this project) (which sources apply), screening-questions.csv (`an-office-files`) (the early questions that find them)

WHY THIS EXISTS
An AI can state a test level, a tolerance rule, a tax rule or a fee with total confidence and be wrong, or right for an older edition. A wrong spec is found late and found expensive: at the lab, at the molder, at the auditor. So a spec in this office is never written from memory. It comes from a document someone opened, it says which one, and before anyone relies on it, it is checked against that document a second time.

THE SOURCE COLUMNS (any sheet that holds specs or rules)
- Source: the document. "IEC 60529", "Customer spec ACME-114", "Supplier datasheet, Celanese Celcon M90", "USPTO fee schedule", "Inventor, 261012 conversation".
- Edition or date: the edition, revision or date of the copy read ("2013+A2:2019", "Rev C", "page dated 2026-10-01"). An undated web page gets the date it was read.
- Clause or page: where in it ("section 14.2.7", "table 3", "page 4").
- Source text: the few words the value comes from, quoted. Short: enough to compare, never a copy of a paid standard.
- Source status: one of the words below.
- Checked on: the date of the second-pass check, and who did it.

SOURCE STATUS
- checked: the value was compared with the document a second time and matches. Only this status, or measured, quote or inventor said, may be built, bought, tested or filed on.
- measured: our own test or measurement; the source is the dated report or record file.
- quote: a supplier's written quote; the source is the quote file.
- inventor said: the inventor's own requirement or decision (a design spec, a target price); the source is the conversation or decision log line.
- from source, not checked: entered from the document, waiting for the second pass.
- from a summary: taken from a free overview, a datasheet summary or a lab's explainer, not the standard itself. Fine for planning; anything critical waits for the real document.
- to find: a placeholder. The Source column says where it will come from.
Never a status, never a source: "AI", "memory", "general knowledge", "typical", "standard practice", "commonly". If that is all there is, the status is to find.

THE STEPS
1. Find the source before the value. When a requirement comes up (a rating, a test, a label, a material property, a fee, a filing rule, a tax rule), open the library first (resources.json (`an-office-files`)), then the official body named there. A search result is a lead; follow it to the official page or document.
2. Read the current copy. Record the edition or date, the clause, and quote the line. For a paid standard nobody has bought yet: record its title, edition and where to buy it, and use the publisher's or a test lab's free summary marked "from a summary".
3. Enter the value with all six columns, status "from source, not checked".
4. Second pass, before the value is used: a separate step (b-analyst, or a fresh session) opens the document again, finds the clause, and compares the value and the quoted text. Match: status checked, with the date. Mismatch: correct it, note what was wrong in the decision log if anything had already used it.
5. Run the checker on the folder before any review, packet, quote request, test plan or filing: python3 check-sources.py <folder>. It lists every row without a source, with a memory-type source, still not checked, or marked critical and not checked. Nothing critical goes out until its rows are checked.
6. Re-check when the source changes: a new edition, a new customer spec revision, a new tax year. The row goes back to "from source, not checked".

WHEN NO PROCEDURE COVERS IT
The office's procedures cover the common work. Everything else (good drawings, a test method, a label, a packaging rule, a government form) has an authoritative source already written by the people whose job it is. Use it instead of improvising.
1. Name the subject in plain words ("production drawings a molder can quote from").
2. Look in the library for the authoritative source: the standards body, the agency, the publisher. Example: drawings follow the ASME Y14 series: Y14.100 for drawing practices, Y14.5 for dimensioning and tolerancing, Y14.41 for 3D model-based definitions.
3. Not in the library: search the official bodies (.gov, .mil, the standards body, the test lab) and add it to resource-map.csv as "found, not yet checked" with the date (`an-market-and-sources` (Map the resources to this project) step 4).
4. Write the project's own short procedure from it in procedures/<subject>.txt in the invention's folder (or procedures/ in the business folder): each step names the source, edition and clause it comes from. Mark the procedure "from <source>, <edition>". Steps you could not trace are marked "to find".
5. Tell the inventor in one line, and if the subject will come up for other inventors, send Mike a note so it can join the office's procedures.

RULES
- Never relaxed for speed (`an-principles-core` (Trace every spec to its source), `an-principles-core` (Never invent facts)).
- The library is pointers, not copies; never store a paid standard's text beyond the short quote.
- Tax and legal rules are sources too: the IRS publication or the state's page for that year, quoted, with the year. The bot points to them; the inventor's accountant or the agency is the authority (`an-principles-core` (Rigor scales with whose money is at risk)).
