---
name: an-playbooks
description: "Use when a job matches a whole playbook: design from concept to freeze, or the first tooling quotes."
---

# an-playbooks

Sections: Playbooks: the Project Manager Bot; PLAYBOOK: The design loop, from concept to freeze; PLAYBOOK: The first tooling quote.

## Playbooks: the Project Manager Bot
(procedure file: playbooks.txt)

Playbooks: the Project Manager Bot. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Credit: the structure (a mode, one principle per file, playbooks for whole jobs, skills for single steps) and the methodology are heavily based on Lauren Tan's pstack (https://github.com/cursor/plugins/tree/main/pstack), carried from software to inventing and the business around it. More: https://ancreationoffice.com/credits.html

A playbook strings procedures together into one job that comes up again and again: when it runs, what done looks like, the principles that drive it, the steps with who does each and which procedure each uses, the inventor's decisions, what to do when it goes wrong, and what it leaves in the record. When a job matches a playbook, follow the playbook; open each procedure it names when that step comes up.

THE PLAYBOOKS (in the order a project meets them)
- The design loop, from concept to freeze (`an-playbooks` (PLAYBOOK: The design loop, from concept to freeze)). From an approved charter to a frozen design at one released revision: concepts, the first risk analysis, CAD passes, builds that each answer a question, real-use validation, and the freeze review.
- The first tooling quote (`an-playbooks` (PLAYBOOK: The first tooling quote)). From a design ready to quote to real quotes on the cost sheet and the inventor's decision to order, change, or stop.


How a playbook relates to the rest: principles (`an-principles-pm` (Principles: the Project Manager Bot)) say how to decide; a playbook says what to do, in what order, for a whole job; a procedure (sop-*.txt) says how to do one step; a template and the mousetrap example show the result.

## PLAYBOOK: The design loop, from concept to freeze
(procedure file: playbook-design-to-freeze.txt)

PLAYBOOK: The design loop, from concept to freeze. Revision 2 — October 18, 2026.
Index: `an-playbooks` (Playbooks: the Project Manager Bot)
Runs it: b-project-manager. b-analyst does the models, sheets and review pages; the plant office files (`an-plastic-design` (the Plastic Design Office (role b-plastic-design-office)), `an-molding` (the Molding Plant Office (role b-molding-office)), `an-quality` (the Quality Office (role b-quality-office)), `an-manufacturing` (the Manufacturing Office (role b-manufacturing-office))) supply the manufacturing review.
Example: the mousetrap (https://ancreationoffice.com/example-mousetrap/README.txt): concept decisions 2026-10-12 and 10-13, the risk analysis table, printed revision X2 tested in barns, CAD revision X3, freeze planned for 2026-12-15.

WHEN IT RUNS
Fact-finding is done (stage S0): the charter is approved, and the requirements list (the compliance matrix) has its first lines, each traced to a source. It runs until the design freezes.

DONE WHEN
The design is frozen at one named revision, which needs all five of these (`an-design-and-prototype` (The prototype loop) FREEZE):
- every compliance matrix line is met or put off on purpose, with the reason and who agreed;
- at least one validation with real use is done;
- the remaining risks are accepted by the inventor;
- the cost estimate and timeline still fit the charter, or the inventor accepted the trade;
- the drawings, parts list and material specs are released at one revision.
Then the tooling-quote playbook starts (`an-playbooks` (PLAYBOOK: The first tooling quote)).

PRINCIPLES THAT DRIVE IT
- Build to learn: every build answers a stated question (`an-principles-pm` (Build to learn)).
- Fail forward faster: a failed build is information; fix and build again (`an-principles-core` (Fail forward faster)).
- Find surprises early, and design for manufacture from the first pass (`an-principles-pm` (Find the expensive surprises early), `an-principles-pm` (Design for manufacture from day one)).
- Know what good is: write the pass level before checking (`an-principles-pm` (Know what good is before designing)).
- Severity first: anything that could hurt someone is designed out or guarded, whatever its overall score (`an-principles-pm` (Severity first)).
- One change at a time when a test has to show what a change did (`an-principles-pm` (One change at a time, to the root cause)).
- Which gives: when time, money and how well it works pull apart, the inventor picks (`an-principles-pm` (When something has to give, ask which)).
- Scope gate and re-anchor: new ideas become suggestions, not scope (`an-principles-pm` (Scope gate), `an-principles-pm` (Re-anchor)).
- One controlled copy: one released revision, everything else is history (`an-principles-pm` (One controlled copy)).
- Trace every spec to its source (`an-principles-core` (Trace every spec to its source)).

THE STEPS
1. Check the starting point. (b-project-manager)
   Charter approved; requirements list started, with sources checked (python3 check-sources.py); screening done and the resource map built (`an-market-and-sources` (Map the resources to this project)). If not, finish fact-finding first.
2. Concepts. (b-analyst draws; the inventor picks)
   Two or three concepts: sketches, images, rough mock-ups, shown side by side on a review page (`an-market-and-sources` (Review pages and dated folders)). Review them against the user, the marketing plan and the specifications that drive shape. The inventor picks one; the others are parked with a reason. Decision log.
   Uses: `an-design-and-prototype` (The design stage, a review loop) (industrial design passes).
3. First risk analysis on the chosen concept. (b-analyst; b-project-manager reviews)
   The risk analysis table for this product's own parts and steps, worst consequence first (`an-cost-and-risk` (Risk analysis table)). Every failure that could hurt someone gets a design answer before the first build.
4. CAD passes. (b-analyst; the manufacturing review from the plant office files)
   The model, the drawings to the project's drawing standard, the parts list. Each pass is a new revision in its own dated folder. Fill the compliance matrix from the model; mark each line met, not met or not checked. The manufacturing review starts here and gets specific: process, wall, draft, tolerances, part count, assembly. Put rough costs on the cost sheet, marked estimate, and tooling as placeholders. Every pass ends in a recorded review with the inventor.
   Uses: `an-design-and-prototype` (The design stage, a review loop) (CAD passes), `an-cost-and-risk` (Cost sheet), `an-cost-and-risk` (The source check) (WHEN NO PROCEDURE COVERS IT for drawings).
5. Approve a revision to build. (the inventor decides)
   Name the question this build answers, the level (bench check, works-like, looks-like, works-and-looks-like) and what it will cost. Spending register rows when ordered. Decision log.
   Uses: `an-design-and-prototype` (The prototype loop) (levels).
6. Build, verify and validate. (the inventor builds or orders; b-analyst records)
   Verification: the build against the compliance matrix lines it was meant to check, against pass levels written beforehand. Validation: real users in real conditions; at least one round before freeze. Anyone outside the project who sees it goes in the disclosure history. Rescore the risk analysis table with what the build showed; update cost and timeline.
7. Decide the next round. (the inventor decides)
   Another round with a stated question (back to step 4 or 5), or on to freeze. Check for drift every round: builds with no question, the same failure twice without a design change, rounds added to put off a decision. Update the schedule's forecasts and run schedule.py; a slip on the critical path is said in one line. When cost or time pulls away from the charter, ask which gives; a change to the charter's scope, budget or dates is a change notice (`an-cost-and-risk` (Revisions and engineering change notices)).
8. Freeze review. (the inventor decides)
   Walk the five freeze conditions on a review page. Run check-sources.py: nothing critical still unchecked. The inventor accepts the remaining risks in words, in the decision log. Release the drawings, parts list and specs at one revision.
9. After freeze. (b-project-manager)
   Park the risk analysis table and the compliance matrix with their reopen triggers (`an-project-record` (Living and parked documents)). From now on a design change goes through a change notice (`an-cost-and-risk` (Revisions and engineering change notices)); a safety fix is never held back by it. Start the tooling-quote playbook.

WHEN IT GOES WRONG
- A build fails: say what it showed in one line, change the design, build again. The same failure twice without a design change means stop and rethink the feature.
- The cost estimate climbs past the charter: which gives, the inventor's call, and a change notice if the budget moves.
- A late test fails after freeze: believe reality (`an-principles-core` (Believe reality over the plan)). A change notice, and the tests it touches rerun.
- Ideas keep coming: each one goes on the action log as a suggestion (`an-project-record` (Suggestions and actions)), not into this revision.
- A requirement's source turns out wrong or out of date: fix the line, recheck what used it, and note it in the decision log.

WHAT IT LEAVES IN THE RECORD
Revision folders and review pages for each pass; the compliance matrix; the risk analysis table; the cost sheet with estimates and placeholders; decision log lines for the concept, each build, the accepted risks and the freeze; spending register rows for each build; the disclosure history for anyone outside who saw it; the released revision.

## PLAYBOOK: The first tooling quote
(procedure file: playbook-first-tooling-quote.txt)

PLAYBOOK: The first tooling quote. Revision 2 — October 18, 2026.
Index: `an-playbooks` (Playbooks: the Project Manager Bot)
Runs it: b-project-manager. b-business-manager prepares the supplier meeting and the money side; b-analyst does the sheets.
Example: the mousetrap (https://ancreationoffice.com/example-mousetrap/README.txt): action A-001, the request for quote to Molder A, quote-comparison.csv.

WHEN IT RUNS
- The design is frozen, or close enough to quote: the parts that need tooling have CAD at a named revision and their materials are chosen.
- The cost sheet still carries tooling placeholders, and the numbers can't be trusted until they are real (the funding packet's verdict depends on them).
- Or the inventor says "get the molds quoted".

DONE WHEN
At least two comparable quotes (three is better) are on quote-comparison.csv, the chosen basis has replaced the placeholders on the cost sheet, the numbers have been rerun, and the inventor has made the call: order the tooling, change the design, change the price or volume, start with a prototype tool, or stop. The call is in the decision log with the principle that drove it.

PRINCIPLES THAT DRIVE IT
- Proof over estimate: a quote replaces a placeholder; nothing else does (`an-principles-pm` (Proof over estimate)).
- Two-way doors go fast: asking for quotes is two-way, so do it early and in parallel; ordering tooling is one-way, so it waits for the comparison and the inventor (`an-principles-core` (Two-way doors go fast)).
- Find surprises early: the toolmaker's review is the cheapest place to learn the part can't be molded as drawn (`an-principles-pm` (Find the expensive surprises early), `an-principles-pm` (Design for manufacture from day one)).
- Know the unit economics before tooling (`an-principles-bm` (Know the unit economics before tooling)).
- 90% and go: quote on the planning quantities and say they are planning numbers; don't wait for a perfect forecast (`an-principles-core` (90% and go)).
- Decide on the patent before showing it: an NDA before CAD leaves the project (`an-principles-bm` (Decide on the patent before showing it publicly)).
- Trace every spec to its source: a quote is a source; a remembered price is not (`an-principles-core` (Trace every spec to its source)).

THE STEPS
1. Check it is ready to quote. (b-project-manager)
   For each part that needs tooling: CAD and a drawing at a named revision, the material from the decision log, the critical features from the risk analysis table (severity 8 and up) and the compliance matrix. Run python3 check-sources.py on the project: nothing critical goes out unchecked. Anything missing goes on the action log, and the playbook waits for it.
   Uses: `an-design-and-prototype` (The design stage, a review loop) (freeze), `an-cost-and-risk` (Cost sheet), `an-cost-and-risk` (Risk analysis table), `an-cost-and-risk` (The source check). Drawings a shop can quote from follow the drawing standard named for the project (`an-cost-and-risk` (The source check) WHEN NO PROCEDURE COVERS IT).
2. Decide what to ask for. (b-project-manager proposes, the inventor decides)
   Quantities: the first order and the annual volume from the charter and funding.csv, marked as planning numbers. Options worth pricing at the same time: cavities, a family mold, aluminum or steel, a prototype tool for the first few thousand parts. Who owns the tool: the inventor. Write the call in the decision log.
3. Pick two or three suppliers. (b-business-manager, with b-project-manager)
   From the library's manufacturing shelf, referrals, or suppliers already known. Each goes in contacts.csv. A molder that won't sign an NDA is a reason to pick another, not to send CAD anyway.
4. NDA, then CAD. (b-business-manager)
   A mutual NDA, signed, in the correspondence log. Then the CAD and drawings go out, each in its own dated S folder with the exact files and revision (`an-correspondence`), and a row in the disclosure history.
5. The request for quote. (b-business-manager builds it from b-project-manager's copies)
   python3 meeting-packet.py <the meeting's correspondence folder> manufacturer: the parts, quantities, requirements, critical features and terms. The prep sheet lists what to compare like for like (`an-meetings` (The manufacturer packet (request for quote))).
6. The tooling review. (the inventor attends; b-project-manager takes the findings)
   Ask what they would change to make it cheaper or more reliable to mold. Their findings go in the meeting's notes; each one that changes the design goes on the action log and, after freeze, through a change notice (`an-cost-and-risk` (Revisions and engineering change notices)). A finding that changes a risk goes on the risk analysis table.
7. Log each quote as it arrives. (b-analyst)
   The quote itself in its dated R folder. One row per part per supplier on quote-comparison.csv (template-quote-comparison.csv): tooling cost and type, cavities, tool life, piece price at the first order and at volume, lead times, what is included, payment terms, tool ownership, how long the quote is valid. A quote that leaves something out gets a question back, not a guess. Its expiry goes in deadlines.csv; its tool and parts lead times go into the schedule's days after (`an-project-record` (The schedule and the critical path)), and schedule.py shows whether they move the first shipment.
8. Put the chosen basis on the cost sheet. (b-project-manager)
   Replace each placeholder with the quote's figure; "how the cost was figured" names the quote and its date. Recalculate amortization and the cost to make one. Hand the new cost sheet to b-business-manager.
9. Rerun the numbers. (b-business-manager)
   python3 funding-packet.py on the funding folder: does the tooling pay back within the plan volume now? Say it to the inventor in one line before anything else (for example, with made-up figures: "With the real quotes, each trap clears $0.07 and the molds pay back in 1.5 million traps").
10. The inventor decides. (one-way door)
   - Order the tooling: the supplier's purchase order states tool ownership; the spending register gets a committed row; a change notice if the charter's budget moves; the cost sheet and the quote comparison are parked.
   - Change the design to cut the cost: back to the design loop with the toolmaker's suggestions, then requote the changed parts.
   - Change the price or the volume: b-business-manager reruns the market check and the buyer conversations first.
   - A prototype or aluminum tool first: smaller money, real parts, a real signal.
   - Stop: fail forward faster. Write down what was learned, and what would make it worth reopening.
   The decision log names the principle that drove the call.

WHEN IT GOES WRONG
- The quotes come in far above the placeholder: believe reality over the plan (`an-principles-core` (Believe reality over the plan)). Say it plainly, rerun the numbers, and take it to step 10; don't shop for a quote that agrees with the plan.
- The quotes can't be compared: send each supplier the same questions and ask again on the same basis.
- A supplier wants full drawings before quoting: make them, from the drawing standard, rather than sending CAD alone.
- Nobody will quote: ask why. The answer is usually the volume, the drawings, or the part itself, and each is a finding.
- A quote expires before the decision: ask for it to be extended in writing, or requote.

WHAT IT LEAVES IN THE RECORD
quote-comparison.csv; the quotes in the correspondence log; updated cost-sheet.csv; decision-log.csv lines for steps 2 and 10; action log rows for each finding; deadlines for quote expiry; spending register and a change notice if tooling is ordered.
