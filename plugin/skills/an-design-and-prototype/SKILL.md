---
name: an-design-and-prototype
description: "Use in the design and prototype stages: concepts, CAD, AI-assisted CAD, design reviews, prototype builds and tests."
---

# an-design-and-prototype

Sections: The design stage, a review loop; AN CREATION — SHORT DESIGN AND FAILURE REVIEW — TEMPLATE REV 1; Getting the most out of Claude and Codex on CAD work; Review record; The prototype loop; Prototype control plan.

## The design stage, a review loop
(procedure file: sop-design-loop.txt)

Procedure: The design stage, a review loop. Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Playbook: the whole job from concept to freeze is `an-playbooks` (PLAYBOOK: The design loop, from concept to freeze)
Starts from: the project description (`an-stages` (The project description: what fact-finding delivers)), the deliverable of fact-finding.
Goes with: `an-stages` (Stages of a project), `an-market-and-sources` (Review pages and dated folders), compliance-matrix-template.csv

WHY THIS EXISTS
Fact-finding decided what this product has to meet: the standards, the specifications, the marketing needs, the risks. Design is where the product is shaped to meet them, and where the proof is collected. Design is not one pass. It is design, design, design, review, and again, until the people who have to be satisfied are satisfied.

THE OFFICE UNDERSTANDS APQP (D-039, as changed by Mike: formal APQP is not run on every project)
The office understands APQP (Advanced Product Quality Planning, the automotive method) and uses its logic to keep track of what exists, what has been touched and what hasn't, and how each specification traces through to a good part and to what gets inspected. Keeping those links is cheap for an AI. How formal the documents get is the inventor's call and what the product and its customer require (`an-stages` (Stages of a project)); offer the formal level, don't impose it. Project level changes what the inventor sees and how big each document is.
The inventor does not have to work in APQP. They see plain words, reviews and decisions. b-analyst keeps the structure underneath.

APQP's five steps (APQP calls them phases) and our stages:
1. Plan and define: fact-finding. Output: the project description.
2. Product design and development: this design stage. Outputs below.
3. Process design and development: ready to make (process flow, process FMEA, production control plan, packaging).
4. Product and process validation: first production parts checked against the frozen design (a production-approval package sized to the project).
5. Feedback and improvement. Not used as a stage here (D-061): too few products per inventor for it to pay off.

The trace chain b-analyst keeps, every project:
requirement (matrix ID) → design FMEA line → design feature on the drawing → verification plan and result → critical feature → process FMEA line → control plan check → inspection record.
Every link carries the compliance matrix ID. A requirement with no verification, a critical feature with no control plan check, or an FMEA action with no owner is a gap, and gaps are listed on every review.

Design-stage outputs b-analyst keeps, at the project's size:
- compliance matrix (requirements, data sheet, check sheet; it doubles as the design verification plan and report, DVP&R)
- design FMEA, updated every pass
- drawings, parts list, material specs at a named revision
- critical feature list
- prototype control plan for each build (what it must prove, what is measured, how)
- design for manufacturing and assembly review
- review records
- what the next stage will need: tooling, fixtures, gauges, supplier questions

USE THE REAL TERMS, AND EXPLAIN THEM (D-040)
The inventor will talk to engineers, suppliers, labs, buyers and investors who use these words. Don't shy away from them. The first time a term matters, say it, explain it in a line or two of plain words, and say what the office does with it. After that, use it.
The usual line: "The AI keeps track of this for you. When you need one, say so and we'll pop it up. We'll already have most of the data."
On request, produce the document on a review page and as a file in their format, filled from what the office already has, with the gaps marked.

Terms to have ready, plain first:
- Compliance matrix: one list of everything the product has to meet (each standard, spec and marketing need), what data each one needs, how it's proven, and whether it's met. Also called a requirements or verification matrix.
- APQP (Advanced Product Quality Planning): the auto industry's step-by-step way of planning a product so it comes out right. The office runs every project this way behind the scenes.
- FMEA (failure mode and effects analysis): a list of what could fail, how bad it would be, how likely, how we'd catch it, and what we're doing about it. Design FMEA for the product, process FMEA for how it's made.
- DVP&R (design verification plan and report): the list of tests and checks, and their results. Our compliance matrix covers it.
- Verification and validation: verification is "did we build it to the spec"; validation is "does it actually do the job for real users".
- Control plan: what gets checked during making, how, how often, and what happens if it's off.
- Critical (special) characteristic: a feature that matters most for safety or function, so it gets checked every time.
- DFM / DFA (design for manufacturing / assembly): making sure it can be made and put together at the target cost.
- Design review: a recorded meeting where the design is checked and a decision is made.
- Design freeze: the point where the design stops changing so tooling and testing can start. Changes after it go through change control.
- Design history file: the full record of how the design got where it is.
- PPAP (production part approval process): the package that proves the first production parts match the design. Sized to the project.

DESIGN FOR MANUFACTURING FROM THE FIRST PASS (D-043)
DFM / DFA is not a step that arrives at some point. From the first sketch, every pass is designed with how it will be made and put together in mind: process (printed, machined, molded, sheet metal, cast), materials, tolerances, part count, assembly, cost at the target quantity. An industrial design concept that can't be made at the target cost is not a finished concept.
Every review includes someone with manufacturing in mind, not only the designer and the inventor: a machinist, molder or sheet-metal shop, a contract manufacturer, a supplier quoting the part, or the office's manufacturing role when no person is available yet. Their comments go on the review record like anyone else's.

THE LOOP
Every pass has the same shape:
1. Design. Make or change the thing this pass is about.
2. Collect. Fill the data the compliance matrix asks for: dimensions, materials, ratings, labels, test numbers, submittal information.
3. Check. Mark each matrix line this pass touched: met, not met, or not checked yet, with the evidence.
4. Review. A recorded review (below). The inventor always takes part.
5. Update. FMEA, the BOM with estimated part costs, estimated tooling cost, and the timeline (another round adds time) against the inventor's budget and dates. Penciled-in estimates; rough is fine, having a number early is the point (D-051). Design changes are where time, cost and quality move; say which corner moved.
6. Decide. Loop again, move on to the next kind of pass, or approve a revision to build. The inventor decides.
A round is done when the CAD (or, in industrial design passes, the concept drawings) is updated to the decision. That updated revision is what the next round starts from.

Each pass is a new revision in its own dated folder (D-029). Nothing from an earlier pass is written over.

KINDS OF PASSES
The loop moves through kinds of passes, usually in this order. A project starts where it needs to: a bracket with no looks to speak of can start at CAD. A later pass can send it back (CAD shows the handle can't be molded the way it was drawn: back to industrial design for that feature).

Industrial design passes (often two or three)
Design: concept sketches, concept images, renders, rough mock-ups. Form, ergonomics, how it is held and used, how it looks on the shelf.
Collect: the user needs and marketing specifications this concept answers; rough size and weight.
Review against: the "yours" items, the user, the marketing plan, the specifications that drive shape. Show the concepts on a review page side by side.
Move on when: the inventor picks one concept. The others are parked with a reason, not deleted.

CAD passes (always, at some point)
Design: 3D model, drawings, parts list, material choices, a rough build plan. FEA paint where it needs to bend or carry load (a labeled guess, not a sign-off).
Collect: everything the compliance matrix asks for from the standards and specifications, filled from the model.
Check: clearances, critical features, and the DFM / DFA review with the manufacturing reviewer (it started in the first pass; here it gets specific: process, tolerances, part count, assembly steps, cost).
Review against: the whole matrix.
Move on when: the inventor approves a revision to build. That starts the prototype loop (`an-design-and-prototype` (The prototype loop), sop-stages S2). Test results come back here when a feature has to change.

THE COMPLIANCE MATRIX (data sheet and check sheet in one)
One list per project, built from the project description. One line per requirement, from every source: each standard that applies, the design specifications, the marketing specifications, and the risks that need a design answer.
Columns (compliance-matrix-template.csv):
- ID: a short number so drawings, tests and changes can point to the line.
- Source: where it came from (a standard, the spec, the marketing plan, an FMEA line, the inventor). Never AI memory.
- Edition or date, Clause or page, Source text (the few words quoted), Source status, Checked on: the trace back to the document, and the second-pass check against it (`an-cost-and-risk` (The source check)). No line is built, tested or quoted on until its source status is checked, measured, quote or inventor said.
- Requirement: what it asks, in plain words.
- Kind: submittal (information a regulator or lab needs), test, or design (something to build in).
- Data to collect: the facts this line needs. This is the data sheet half.
- How proven: test, inspection (measure or look), analysis (calculation, FEA), demonstration (show it working), or lab certification.
- Pass level: what counts as met, written before checking (survives a 1 m drop onto concrete). This is the check sheet half.
- Evidence: the dated file that shows it.
- Status: met, not met, not checked yet, or put off (with the reason and who agreed).
- Critical: yes for the few features that matter most for safety or function. These carry into the production control plan.
Read each pulled standard's current page to build its lines (sop-resource-map step 5). A standard's whole checklist is not copied in; only the lines that apply to this product.

TWO KINDS OF CHECKING
Verification: did we build it right? It meets each line's pass level. Mostly the compliance matrix.
Validation: did we build the right thing? Real users, real conditions: the back-parking-lot test, a user trial, a buyer's hands. A design can pass every line and still fail the user.
In the design loop, checks are by inspection and analysis of the model and drawings. Tests on real parts, and validation, happen in the prototype loop. Every project gets at least one validation before freeze.

THE REVIEW RECORD
Every review is written down, in its own dated file, and shown on a review page:
- Date, who took part: the inventor, someone with manufacturing in mind (always), and the roles that matter for this pass (design, engineering, marketing; a human engineer or lab when a line needs one).
- Which revision was reviewed.
- What was looked at, and against which matrix lines.
- Results: what passed, what did not, what was learned.
- Actions: what changes next pass, who, by when.
- Decision: loop again, next kind of pass, or freeze.

HANDING OFF TO THE PROTOTYPE LOOP
The design loop ends when the inventor approves a revision to build:
- every compliance matrix line that can be checked on paper (inspection, analysis) has a status;
- the lines that need a real part are listed with their test and pass level;
- the drawings, parts list and material specs are at one named revision;
- the prototype control plan says what the build must prove and what gets measured;
- the cost estimate and timeline still fit, or the inventor accepted the trade.
The two loops trade back and forth: a prototype result sends a feature back for a design pass, and the new revision comes back to be built. Freeze is the exit of the prototype loop (`an-design-and-prototype` (The prototype loop)).

DONE WHEN
A revision is approved to build, the compliance matrix shows every line's status or planned test, the review records are filed, and that revision's drawings, parts list and specs are in their dated folder.

WHO DOES WHAT
b-analyst builds the compliance matrix, fills data from the model and documents, proposes the check status, and writes the review record. b-project-manager puts each review on a review page, walks the inventor through it, and records the decision. Human designers, engineers and labs supply what the office can't: CAD by a person when needed, a signed stress check, a lab report. The inventor decides every loop, move-on and freeze.

## AN CREATION — SHORT DESIGN AND FAILURE REVIEW — TEMPLATE REV 1
(procedure file: design-review.txt)

AN CREATION — SHORT DESIGN AND FAILURE REVIEW — TEMPLATE REV 1
Companion: https://ancreationoffice.com/design-risk.html
Use one or two pages for a simple product; expand where needed.
Blank fields are unresolved. This is not product approval or certification.

PART 1 — WHAT MUST WORK, AND WHAT MUST FIT
Product / intended users and use:
Product, model and drawing revisions / date:
Scope, interfaces, exclusions and qualified reviewers:

b-project-manager drafts this review from project records and specialist input.
Customer needs / requirements (repeat for each significant need):
ID / customer wording / source:
Agreed measurable target and use conditions (unknown if not agreed):
Design feature or characteristic that addresses it:
Verification method / acceptance criteria:
Actual evidence and revision / status / owner:
Validation with intended users / result or remaining work:
Conflicting or deferred input / reason / agreed decision:

Fit and manufacture:
Critical interface / functional minimum and maximum clearance:
Dimensions, geometric controls and datums / units:
Worst-case tight and loose stack / assumptions / result:
Allowance for environment, coating, movement and wear:
General tolerance convention and edition / explicit exceptions:
Supplier capability and inspection method / evidence:
Edges, radii, walls, cores, draft, tool access and assembly sequence:
Wrong-way assembly prevention / incorrect attempts to test:

PART 2 — HOW IT COULD FAIL, AND WHAT WE WILL DO
Copy this block for each significant failure mode:
Risk ID / linked CTQ and requirement / design or process scope:
Function / failure mode:
Effect on user and system / severity and rationale:
Possible cause / likelihood and evidence or uncertainty:
Existing prevention / evidence:
Existing detection / escape likelihood and evidence:
Priority and rationale; serious safety effects reviewed explicitly:
If formal ratings are used: defined scale, S / O / D / required method:
Possible routes around or through / person or expertise that could help:
Question to carry into the next relevant conversation:
What can continue now / affected activity only if a limit applies:
Action to prevent or reduce the problem:
Owner / due date / status:
Planned effectiveness test and acceptance criteria:
Actual result / exact tested revision / evidence location:
Remaining risk / revised assessment / reviewer and decision date:

For an observed failure also record:
Symptom / expected behavior / affected units / containment:
Conditions where it happens and does not / recent changes:
Measurement checks / hypotheses / tests / confirmed contributing causes:
Corrective action / repeat and regression tests / recurrence monitoring:

Linked control plan: process step, characteristic/limit and source, prevention,
measurement, sampling/frequency, owner, result record and reaction plan.
Unknown details remain proposed/unresolved; actual evidence is separate.
Templates: critical-quality.csv and control-plan.csv beside this file.

Review summary:
Open safety issues and limits on the next activity:
Roadblock-list links / opportunities to follow up:
Next useful action that moves the project forward:
Actions and dependencies to send to b-project-manager:
Responsible reviewer / next review date and change triggers:
Do not lower a rating or close an action without supporting evidence.

## Getting the most out of Claude and Codex on CAD work
(procedure file: sop-ai-cad.txt)

Procedure: Getting the most out of Claude and Codex on CAD work. Driving SOLIDWORKS (and KiCad) with an AI coding agent: the setup, the brief, and the checks. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Lines are marked "office" or "published" (with the source to check).

WHAT THIS IS (office)
AI coding agents such as Claude Code and Codex can run SOLIDWORKS through its programming interface (the SOLIDWORKS API, a COM interface on Windows). They write and run macros and scripts that build parts from a written specification, change dimensions and equations, fill custom properties, make drawings from a template, and export STEP, PDF and DXF files in batches. Today they are fair at it, not good. They are dependable on repetitive, well-specified, parametric work. They are unreliable on free-form modeling, on picking the right face or edge, and on judging whether a model looks right.
The job of this office is to set the work up so the agent succeeds: you (the Grok office) plan the work and write the brief; the agent on the owner's CAD computer does the CAD; the owner checks the result. You never touch SOLIDWORKS yourself.

WHERE EACH PIECE RUNS (office)
- This office (Grok): the specification, the brief for the agent, the check list, and the record in the project repository.
- The CAD computer: Windows with a licensed SOLIDWORKS; Claude Code or Codex in a terminal; Python with pywin32 (or VBA, or C#/VB.NET) to reach the API; optionally an MCP server that gives the agent SOLIDWORKS tools directly.
- The project repository: the brief, the scripts the agent wrote, exported STEP and PDF files, pictures of the model, and the check results. SOLIDWORKS files are binary; keep the working models in the vault (PDM) or a backed-up folder, and commit the exports and scripts.

THREE WAYS TO DRIVE SOLIDWORKS, MOST RELIABLE FIRST (office)
1. A parametric template plus a script. The owner models the part family once by hand, with named global variables, equations and a design table. The agent only changes values, rebuilds, checks and exports. This is the most reliable use and the one to steer toward for anything done more than twice.
2. The agent writes and runs API scripts from a written specification: sketches on named planes, features named as it goes, then measurement and export. Good for simple prismatic parts, batch jobs, custom properties and drawings. Python (pywin32), VBA macros, and C# or VB.NET (VSTA or the free xCAD.NET framework) all work; use whichever the owner's existing macros use.
3. An MCP server. Several community servers on GitHub expose SOLIDWORKS operations as tools an agent calls directly (from read-only API documentation lookup to modeling and drawings; Claude Code and Codex both connect to MCP servers). Fastest to try; maturity varies a lot. It runs on the CAD computer with the owner's rights, so read its code (or have the agent review it) before installing, try it on test parts first, and keep the version that works.
A fourth route for new, simple parts (brackets, plates, 3D-printed enclosures): code-CAD. The agent models the part in CadQuery or build123d (free Python libraries), exports STEP, and the owner imports it into SOLIDWORKS. Agents write these more reliably than SOLIDWORKS API calls, and the script itself is the design record. The imported STEP is a plain solid: if the part must be edited in SOLIDWORKS later, rebuild its features there, or keep editing the script.

THE BRIEF: WHAT TO GIVE THE AGENT (office)
Write it in the job folder (jobs/YYMMDD-<slug>/brief.md) and have the owner hand it to the agent.
- The goal in one line, and the units.
- A dimensioned sketch or table: every dimension, which ones drive and which are derived, the datums, what sits at the origin, which plane is the front.
- Names: file name, feature and sketch names, variable names. Ask it to name every feature and sketch.
- Material and custom properties (part number, description, revision, material).
- The outputs: where the SLDPRT is saved, STEP (AP214 or AP242), PDF drawing, DXF flat pattern.
- What "done" means: the checks below, with the numbers to hit.
- Rules: the SOLIDWORKS version; use only documented API calls (look each one up in the API help for that version rather than guessing); rebuild with zero errors and warnings; fully define every sketch; work on a copy; ask before deleting or overwriting any file.
- One step at a time: one feature, rebuild, check, then the next. Commit the script after each step that works.

SETTING UP THE AGENT (office)
- Start the agent in the project folder with a short instructions file it reads every session (CLAUDE.md for Claude Code, AGENTS.md for Codex): the SOLIDWORKS version, the API language, where the API help and the working example scripts are, the naming rules, the check list, and "ask before deleting or overwriting files".
- Give it a tiny working script first: connect to SOLIDWORKS, open a part, read one dimension, print it. Build everything from what already works.
- Keep a folder of scripts that worked. Reusing a proven script beats generating a new one.
- Tell it to select geometry by name or by reference planes, axes and points, never by "the face at x, y, z", which breaks as soon as the model changes.

CHECKING (office: never accept "done" on the agent's word)
- Rebuild: zero errors and warnings.
- Numbers: volume, mass, center of mass and bounding box from mass properties, against values worked out from the brief.
- Key dimensions measured by script between named faces or reference geometry, reported as a table: wanted, got, difference.
- Every sketch fully defined; features named as asked; custom properties filled.
- Pictures: the agent saves standard views (isometric, front, top, right) as images in the job folder, and the owner looks at them. An AI checking its own pictures misses things.
- Assemblies: interference detection. Drawings: views and dimensions against the model.
- Export STEP and open it in a viewer to confirm it is the right part at the right size.
Record the check table in the job folder with the script's commit.

WHEN IT GOES ROUND IN CIRCLES (office)
Stop it. Write down what was tried and what failed. Make the step smaller, or have the owner do that one step by hand, and let the agent carry on from there. Two failed tries at the same step is the signal.

GOOD JOBS TO GIVE IT (office)
Custom properties across a folder of parts; batch export of STEP, PDF and DXF; a configurator for a part family from a table; drawings from a template with standard views; renaming, copying and Pack and Go; checking a folder of parts for missing materials or properties; BOM export; simple plates, brackets, spacers and fixture blocks; a 3D-printed enclosure built around a circuit board's STEP model.

CIRCUIT BOARDS (office)
KiCad's files are text, so agents can read them, and its command-line tool (kicad-cli) runs the electrical and design rule checks and every export from a script. Community MCP servers for KiCad exist too. Use the agent to check, export, compare against data sheets and document; keep the schematic's intent and the layout of the power parts under the owner's eye.

NEVER (office)
- Never let an agent overwrite or delete the only copy of a model: work on copies or under version control.
- Never release a part an agent made without the checks above and a person looking at it.

SOURCES (published; ids in your library): SOLIDWORKS API Help for your version (solidworks-api-help); recording and editing macros (solidworks-macros); CodeStack examples (codestack); xCAD.NET (xcad-net); community MCP servers (solidworks-mcp-servers); Model Context Protocol (mcp-protocol); Claude Code docs (claude-code-docs); Codex docs (openai-codex-docs); CadQuery (cadquery); build123d (build123d); KiCad docs (kicad-docs).

## Review record
(procedure file: template-review-record.txt)

Review record. Template. Save as a dated file: YYMMDD-HHMM-review-<stage>-<revision>.
Project:
Stage and round: (S1 industrial design / S1 CAD / S2 prototype / S3 tooling / S4 qualification)
Revision reviewed: (C1, X3, A...)
Date:
Who took part: (the inventor; someone with manufacturing in mind; others and their role)
What was looked at: (files, parts, test results; compliance matrix lines by ID)
Results: (passed / not passed / learned, one line each, with the matrix IDs)
Cost and timeline: (BOM and part cost estimate, tooling estimate, spent so far vs budget, timeline change; which corner moved)
Actions: (what changes next, who, by when)
Decision: (loop again / next kind of pass / approve to build / freeze / ready to qualify / approved; at a stage exit: go, hold or drop)
Reason, in the inventor's words:

## The prototype loop
(procedure file: sop-prototype-loop.txt)

Procedure: The prototype loop. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Playbook: the whole job from concept to freeze is `an-playbooks` (PLAYBOOK: The design loop, from concept to freeze)
Starts from: a revision approved to build in the design loop (`an-design-and-prototype` (The design stage, a review loop), sop-stages S1).
Goes with: `an-stages` (Stages of a project) (S2), the compliance matrix, `an-market-and-sources` (Review pages and dated folders)

WHY THIS EXISTS
Paper and CAD only go so far. The prototype loop builds the design, tests it, learns from it, refines the design, and builds again. It can go around two or three times, or a dozen; that depends on the product and who is building it. Each build answers specific questions before more money is spent, and the builds climb toward something close to production.

THE LOOP
The difference from the design loop is the test: each round builds something, tests it somehow (measure it up, drop it, use it, put it on the bench), and changes the design based on what the test showed. A round is done when the CAD is updated. Then: another prototype round, or on to the tooling loop.
DFM keeps running (`an-design-and-prototype` (The design stage, a review loop), D-043): every build is also a check on how it will be made, and every review includes someone with manufacturing in mind.
Every round has the same shape:
1. Plan the build. Its level (below), what it must prove, what gets measured, and the pass levels from the compliance matrix. That is the prototype control plan. Written before building.
2. Build. In-house, a maker space, a prototype shop, a contract builder. Record what was actually built: revision, materials, process, anything changed on the fly.
3. Test. The tests this build is for: bench checks, measurements, back-parking-lot use, a user trial, a pre-check before a lab. Record results against the compliance matrix lines as evidence.
4. Review. A recorded review (same record as the design loop): what passed, what didn't, what was learned, what changes.
5. Refine and update. Redesign or refine the part from the test results and update the CAD, the BOM with estimated part costs, the estimated tooling cost, and the timeline (another round adds time). That update closes the round. A change big enough to need its own concept or layout rethink goes back to the design loop instead.
6. Decide. Another prototype round (same level or the next), or freeze and on to manufacturing. The inventor decides.
Every build, test and review is its own dated folder and gets a review page. Nothing from an earlier round is written over.

LEVELS OF PROTOTYPE
Builds come at different levels, and a project uses only the ones it needs. A simple product may go straight to a works-and-looks-like build. Use the industry names, and explain them (D-040).
- Bench check (breadboard, proof of concept): one part of it on the bench to prove the idea works. Electronics only on a breadboard, a mechanism in cardboard and screws. Looks don't matter.
- Works-like: the whole thing functions, but doesn't look like the product.
- Looks-like: the right size, shape, color and feel, but doesn't work. For ergonomics, photos, buyer and user reactions.
- Works-and-looks-like (alpha): both together, built with prototype methods (3D printing, machining, hand assembly).
- Engineering prototype (beta, EVT): built close to the real design with near-production materials; full verification against the compliance matrix.
- Pre-production (DVT, PVT): built with production-intent parts and processes, often by the factory that will make it. Used for validation, lab and certification samples, and buyer samples.
The hardware industry's EVT / DVT / PVT (engineering, design and production validation test) are the late levels. Most inventors stop well short of all three; name them when a supplier or buyer uses them.

WHAT EACH ROUND CHECKS
Verification: does the build meet the compliance matrix lines it was meant to check?
Validation: does it do the job for real users in real conditions? At least one round must include real use before freeze, usually a works-and-looks-like build or later.
Lab and certification: a pre-compliance check early (a cheap look at FCC emissions or a drop test) saves a failed lab visit later. Formal lab samples come from a late build that matches the frozen design.
Update the design FMEA every round with what the build actually showed. Update cost and timeline: another round is time and money, so say which corner moves.

HOW MANY ROUNDS
As many as it takes, and no more. Each round needs a reason: a question it answers. Stop building when the remaining questions can be answered on paper or in the factory. Signs of drift: builds with no stated question, the same failure twice without a design change, rounds added to delay a decision. Bring these up at the review.

FREEZE: WHEN THE LOOP STOPS
The design freezes when:
- every compliance matrix line is met or put off on purpose (with the reason and who agreed);
- at least one validation with real use is done;
- the remaining risks are accepted by the inventor;
- the cost estimate and timeline still fit, or the inventor accepted the trade;
- the drawings, parts list and material specs are released at one named revision.
After freeze, a change goes through change control: what changes, why, which lines and tests it touches, the time and money, and the inventor's yes. Safety fixes are never held back by this.

DONE WHEN
The design is frozen, the compliance matrix shows every line's status with evidence from real builds, the build and review records are filed, and the frozen revision is in its dated folder. Next: the tooling loop (`an-tooling-and-launch` (The tooling loop), sop-stages S3).

WHO DOES WHAT
b-analyst writes each prototype control plan, records results against the compliance matrix, updates the FMEA, cost and timeline, and writes the review record. b-project-manager puts each build's results on a review page, walks the inventor through them, and records the decision. The inventor, or the shop they choose, builds; the office never orders or pays for anything. Labs and engineers sign what the office can't.

## Prototype control plan
(procedure file: template-prototype-control-plan.txt)

Prototype control plan. Template. Write before building. Save as YYMMDD-prototype-plan-<revision>.
Project:
Build: (number, revision built, level: bench check / works-like / looks-like / works-and-looks-like / engineering / pre-production)
The question this build answers:
How it is built: (process, materials, who builds it, quantity)
What gets measured or tested: (compliance matrix ID, the feature or test, method, pass level, how many units)
Critical features on this build:
What will be decided from the results:
Estimated cost and time of the build:
Results: (filled after: each line met / not met, the evidence file)
