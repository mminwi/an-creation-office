---
name: an-tooling-and-launch
description: "Use in the tooling, qualification and launch stages: tool trials, first articles, test plans, first orders, listings."
---

# an-tooling-and-launch

Sections: The tooling loop; Trial log (T-trial or P-trial); Qualification and production approval; AN CREATION — TEST PLAN TEMPLATE — REV 1; AN CREATION — TEST REPORT TEMPLATE — REV 1; Launch; Moved.

## The tooling loop
(procedure file: sop-tooling-loop.txt)

Procedure: The tooling loop. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Starts from: design freeze at the end of the prototype loop (`an-design-and-prototype` (The prototype loop), sop-stages S2).
Goes with: `an-stages` (Stages of a project) (S3), the compliance matrix, `an-market-and-sources` (Review pages and dated folders)

WHY THIS EXISTS
This is where design for manufacturing meets the real thing. The product goes to the people who will make it, and they tool it up. As they do, they find what isn't manufacturable or isn't recommended the way it's drawn. The design changes again, this time to get the tooling right, so the part coming off the tool matches the CAD. More often than not the CAD is updated to match the part that is actually being made.
It is also where most final specifications get set. The basic tolerance stack-up is done at the end of design. The final specs are usually settled by measuring the first parts off the tool and weighing them against what the process actually holds.

THE LOOP
Every round has the same shape:
1. Tooling review. The toolmaker or factory reviews the frozen design for their process: draft angles, wall thickness, undercuts, gate and parting-line locations, bend radii, tolerances they can hold, cost drivers. For molded parts, often a mold-flow study. Their findings go on a review record.
2. Design changes for tooling. Change what they flagged, or agree a different fix. Keep changes "steel-safe" where possible (cut so that later tweaks remove tool material rather than add it back). Update the CAD, drawings and compliance matrix lines touched.
3. Build or adjust the tool, and run a tool trial (T-trial): check out the tooling and run sample parts. Usually one or two T-trials (T0, T1, T2 as the tool is tuned). A T-trial asks: does the tool make the part? It is not yet about running at rate.
4. Measure the parts. First article inspection: every dimension on the drawing measured on sample parts. Check the fit with mating parts and the function. Rerun any compliance matrix tests the change could affect.
5. Update the CAD to match what the tool makes, where the made part is acceptable. The CAD and drawings describe the real part, not the hoped-for one. Update the BOM and part cost from the factory's real quotes, the tooling cost from the toolmaker's actual figures, and the timeline.
6. Review and decide. Another tool adjustment, a design change, or release. The inventor decides, with the factory's input.
A round is done when the CAD is updated to the decision (D-043). Every round is its own dated folder and review page.

TRIALS, WHATEVER THE PROCESS
Plastics plants call them T-trials (tooling trials: check out the tool) and P-trials (process trials: run it at rate and check quality). Most processes have the same two steps under some name: stamping, casting, machining fixtures, PCB assembly, even a hand-assembly line. T-trials happen in this loop. P-trials happen in qualification (`an-tooling-and-launch` (Qualification and production approval)). Use the factory's names for them, and explain them to the inventor.

SETTING THE FINAL SPECIFICATIONS
At design freeze there is a basic tolerance stack-up: how the tolerances of mating parts add up, and whether the assembly still fits and works at the extremes.
Final specs are usually set after the tool is running:
- Measure several sample parts on each critical dimension. How much does the process actually vary? (Process capability, often written Cp or Cpk.)
- Redo the stack-up with the measured variation.
- Negotiate the specs across the parts. Where a process holds a dimension tightly and cheaply, tighten it; where holding it is expensive, widen it and take the room from a part that can give it, so the stack still works. Tighten where it costs the least.
- Write the agreed specs on the drawings and into the compliance matrix as the pass levels for production.
Critical features carry into the production control plan with their final specs.

WHAT ELSE GETS DONE HERE (APQP's process design step, sized to the project)
- Supplier choice: request for quote (RFQ) package, quote comparison, the decision. Often happens just before or at the start of this loop.
- Process flow: the steps from raw material to boxed product.
- Process FMEA: what can go wrong in making it, and how it is caught or prevented.
- Production control plan: what gets checked during production, how, how often, and what happens when it is off.
- Gauges and fixtures for the critical features, and a check that the measuring is trustworthy (measurement system analysis, MSA, at the project's size).
- Packaging, labeling and the shipping or drop test.
- Lab and certification samples from production-intent parts, if not done in the prototype loop.
- A golden sample: an approved part kept as the physical reference.
(The full first article on production parts, the pilot run, the qualifications and the approval package happen in the next stage, `an-tooling-and-launch` (Qualification and production approval).)

NO TOOLING? (low volume, staying small)
Some products never get a hard tool: 3D printed, machined, laser-cut, hand-assembled in small batches. The loop still runs on the production process: choose the shop, run sample parts, measure them, set specs from what the process holds, update the CAD, write the control plan. Same exit.

WHEN THE LOOP STOPS: READY TO QUALIFY
- The tool (or process) makes parts that match the drawings, or the drawings were updated to the accepted parts.
- Final specs are agreed and on the drawings; the stack-up works with measured variation.
- Sample-part first article inspection is filed; critical features are within spec and have control plan checks.
- Compliance matrix lines affected by tooling changes are re-verified.
- Process FMEA, control plan, gauges, packaging and golden sample are in place.
- Cost per part and timeline still fit, or the inventor accepted the trade.
- The inventor agrees it is ready to qualify.

DONE WHEN
The setup is ready to qualify and the current revision (drawings, specs, control plan) is in its dated folder. Next: qualification and production approval (`an-tooling-and-launch` (Qualification and production approval), sop-stages S4).

WHO DOES WHAT
The factory or shop makes the tool and the parts and measures them; their findings and reports are filed in the record. b-analyst turns tooling feedback into design-change proposals, tracks every changed matrix line, redoes the stack-up with measured data, proposes the spec negotiation, and keeps the PFMEA and control plan. b-project-manager shows each round on a review page and records the inventor's decisions. The office never orders tooling, approves payment, or signs for parts. Specs and acceptance are agreed between the inventor and the factory.

## Trial log (T-trial or P-trial)
(procedure file: template-trial-log.txt)

Trial log (T-trial or P-trial). Template. One per trial. Save as YYMMDD-T1-<tool> or YYMMDD-P1-<process>.
Project:
Trial: (T0, T1... tool trial; P1, P2... process trial)
Revision of part and tool:
Date and place: (factory, machine)
Settings used: (from the factory, as they give them)
What happened, in order: (the narration goes here, written up by the AI; "second shot, the boss on the left is short, bumping pressure")
Parts made: (how many, which kept for measuring)
Measurements: (feature, compliance matrix ID, spec, measured values, in or out)
Problems and what was changed:
For P-trials: rate achieved, quality across the run, process capability on critical features
Decision: (adjust tool / change design / another trial / ready)

## Qualification and production approval
(procedure file: sop-qualification.txt)

Procedure: Qualification and production approval. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Starts from: the end of the tooling loop (`an-tooling-and-launch` (The tooling loop), sop-stages S3): the tool or process makes parts that match the CAD, and final specs are agreed.
Goes with: `an-stages` (Stages of a project) (S4), the compliance matrix, the production control plan

WHY THIS EXISTS
Before real production starts, someone has to say: this maker, with this setup, makes good parts, and keeps making them. That is qualification. How much is done depends on what the product is and who is buying it. At the most basic level, you bless the manufacturer so they can go ahead and produce with what they have. At the heavy end (medical, aerospace, automotive) every piece of the setup is qualified and documented.
This is APQP's product and process validation step. In the auto industry its package is the PPAP (production part approval process). Use the terms and explain them (D-040); size the work to the project.

WHAT GETS DONE
1. First article inspection (FAI). Parts from the real production setup, measured against every dimension and note on the drawing, with the results recorded. Done in the tooling loop on sample parts; here it is done on parts from the actual production setup, if anything changed since.
2. First article testing. The compliance matrix tests that need production parts: function, fit with mating parts, drop and shipping, the tests a certification depends on. Sized to what the product is.
3. Process trials (P-trials, a pilot run). After the T-trials have the tool right, run it at rate with the production people, process and checks. Does it hold quality and the specs run after run, not just on the first few parts? Measure the critical features across the run (process capability). Often one or two P-trials; settings that work are recorded as the production process.
4. Qualify what needs it. Any and all of these can be qualified, depending on the product and the risk:
   - the vendor (their quality system, their capacity, their paperwork);
   - a machine or process (it holds the specs; settings recorded);
   - a set of tooling (the tool makes good parts across the run);
   - a manufacturing fixture (it locates and holds the part the same way every time);
   - a measurement fixture or gauge (it measures right and repeats: gauge R&R, part of MSA).
   At the basic level, this is one line: the vendor is approved to produce with what they have.
5. Cost and timeline. Final part cost and tooling cost from the factory's figures, the released BOM, and the launch dates, compared with the estimates from the first round.
6. Approve. The production approval package, at the project's size: FAI report, test results, pilot-run measurements, the qualifications done, the production control plan, the golden sample, and any certificates. The inventor approves; for a buyer who requires it (a retailer, an auto or aerospace customer), the package goes to them for their approval too.

HOW MUCH, BY PROJECT LEVEL
- Simple: the vendor is blessed after a first article check and a look at the first batch. One page.
- Moderate: FAI report, key tests on production parts, a short pilot run with the critical features measured, gauges checked.
- Heavy (medical, aerospace, automotive, a buyer who requires PPAP): the full package, each element qualified and signed, as the buyer or regulation requires.
A buyer's requirements win over the default size.

WHEN IT IS DONE: PRODUCTION APPROVED
- First article inspection and testing are filed, within spec.
- The pilot run held the critical features within spec.
- Everything the project level calls for is qualified, and the record says what was qualified and how.
- The approval package is assembled at the project's size, and the inventor (and any buyer who requires it) has approved.
- The production control plan is in force and the golden sample is kept.
After approval, a change to the vendor, a machine, a tool, a fixture, a gauge or a critical feature goes through change control and repeats the qualification it touches.

DONE WHEN
Production is approved and the approval package is in its dated folder. Next: launch (sop-stages S5).

WHO DOES WHAT
The manufacturer runs the parts, the measurements and the pilot run, and supplies their reports and qualifications. b-analyst builds the checklist for this project's level, checks every report against the drawings, specs and compliance matrix, flags gaps, and assembles the approval package. b-project-manager shows it on a review page and records the inventor's approval. The office never signs for the inventor or the buyer, and never approves payment.

## AN CREATION — TEST PLAN TEMPLATE — REV 1
(procedure file: test-plan-template.txt)

AN CREATION — TEST PLAN TEMPLATE — REV 1
Guide: https://ancreationoffice.com/test-planning.html
Matrix: test-matrix.csv (`an-office-files`)
Original working template; adapt to product, decision and applicable requirements.
Plan work before the build. Unknown critical fields mean the affected test is not ready.
This plan records intended work, not a completed test or a product approval.

1. CONTROL AND DECISION
Project / product / target market / intended use:
Plan ID / revision / status / date / author:
Responsible technical reviewer / approvals actually obtained / dates:
Decision this evidence must support / exclusions:
Linked concept / CTQ / requirements / FMEA / control-plan revisions:
Model / drawing / BOM / PCB / firmware / package revisions:
Changes from prior plan / affected tests:

2. STRATEGY AND REQUIREMENTS
For each requirement: ID / source / measurable limit / conditions:
Related risk or proposed product claim:
Evidence method: inspection / analysis / demonstration / test:
Purpose: learning / verification / validation / compliance / production acceptance:
Standard or method / edition / clause / applicability rationale:
Authorized procedure location / access confirmed / unresolved interpretation:
Coverage and exclusions across variants / rationale:
Customer/lab agreement needed / owner / action:

3. TEST ARTICLES AND RESOURCES
Sample IDs / count / rationale / allocation to each test:
Construction and manufacturing process / configuration / prior test history:
Prototype differences from production / effect on conclusions:
Conditioning / destructive tests / sequence rationale / spares:
Operator / lab / relevant accreditation or recognition scope / witnesses:
Fixture and setup drawings/photos / support equipment:
Instrument IDs / range / resolution / calibration due date / traceability:
Uncertainty and near-limit decision rule where relevant:
Site / environment / facilities / schedule / budget / dependencies:

4. REPEAT THIS BLOCK FOR EACH TEST
Test ID / requirement IDs / sample IDs:
Objective and decision / exact configuration:
Procedure reference and revision / authorized adaptations:
Prechecks and baseline measurements:
Fixture, orientation, operating modes, loads and support equipment:
Conditions, levels, units and tolerances / source and justification:
Sequence / exposure duration / cycles or repetitions / timing:
Measurements during test / monitoring / recording frequency:
Recovery and postchecks / inspection timing / sample handling:
Pass/fail criteria set BEFORE testing, with measurable limits and sources:
Safety hazards / reviewed controls / operator competence:
Stop conditions / emergency action / restart authority:
Expected raw data, logs, photos and report / save locations:
Unresolved fields / owner / test readiness status:

Electrical / EMC / radio additions where applicable:
Supply/charging states / ports / cables and routing / grounding / accessories:
Hardware, firmware and radio/module/antenna details / variants:
Bands, modes, settings and representative/worst-case selection rationale:
Functions monitored / allowed degradation, recovery, resets or data loss:
Applicable safety, emissions, immunity, radio authorization and exposure routes:
Lab-confirmed setup and methods / outstanding integration questions:

Drop additions where applicable:
Bare product or shipment / actual contents, mass and packaging revision:
Height reference / surface / faces, edges or corners / sequence and count:
Operating state / damage and functional criteria / photos per event:
Values come from the applicable requirement/method; no default height is implied.

Water additions where applicable:
Exposure and claim / liquid / temperature / depth reference or pressure:
Duration / orientation / seals / fasteners / ports, caps and mounting:
Preconditioning / prior drops or wear / operating state and safe isolation:
Ingress and functional/safety acceptance criteria / recovery / inspection:
Do not infer jet resistance from immersion alone or invent an IP pass.

5. READINESS REVIEW — RECORD ACTUAL FINDINGS
Requirements/methods/limits reviewed:
Samples, configuration, fixtures and instrumentation ready:
Safety controls and competent operator confirmed:
Critical unresolved items / affected tests held:
Run authorized by / date / plan revision / witness requirements:

6. REPORT AND CHANGE CONTROL
Report IDs and raw evidence links (blank until work occurs):
Deviations and approval / failed, interrupted or inconclusive tests:
Corrective actions / repeat and regression test decisions:
Changes affecting prior evidence / responsible reviewer:
Claims supported and limits / remaining risks / next project decision:
Handoff to b-project-manager with exact plan/report revisions:

## AN CREATION — TEST REPORT TEMPLATE — REV 1
(procedure file: test-report-template.txt)

AN CREATION — TEST REPORT TEMPLATE — REV 1
Use after execution; keep separate from the plan and preserve original results.
Guide: https://ancreationoffice.com/test-planning.html#results

Report ID / revision / author / date / status:
Project / test ID / requirements / purpose:
Approved plan ID/revision / actual procedure and edition:
Operator / lab / dates / witnesses:
Sample IDs / hardware, firmware, materials and package revisions:
Prototype differences / previous exposures / sample condition:
Actual setup, equipment/calibration and environment:
Actual conditions, settings, sequence and durations:
Baseline / observations during exposure / recovery / postchecks:
Raw measurements with units / uncertainty where relevant:
Photos / logs / raw-data file links and exact revisions:
Acceptance criteria and source from the plan:
Outcome: pass / fail / not run / interrupted / inconclusive (with reason):
Deviations / authorization / impact on validity:
Failures, damage and anomalies (do not omit unsuccessful samples):
What this evidence supports / limitations and exclusions:
Corrective action / owner / root-cause record:
Retest/regression plan and new sample/revision:
Technical review / date / disposition:
b-project-manager handoff / affected CTQ, risk and control-plan items / next decision:
A report does not automatically establish regulatory authorization or certification.

## Launch
(procedure file: sop-launch.txt)

Procedure: Launch. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Starts from: production approved (`an-tooling-and-launch` (Qualification and production approval), sop-stages S4).
Goes with: `an-stages` (Stages of a project) (S5), `an-cost-and-risk` (Revisions and engineering change notices), the compliance matrix, the production control plan

WHY THIS EXISTS
Approval is not the finish line. Launch puts the product in front of buyers honestly, with the paperwork they ask for. It is the last stage of the process.
There is no formal feedback loop after launch (D-061). Most inventors make too few products for one to pay off, and the process itself is likely to be reinvented as AI improves before a feedback analysis would mean much. What stays is the duty below: if something goes wrong that could hurt someone, act.

S5 LAUNCH ("Putting it out there")
Trigger: production approved, and a price, a sale, a show or a store.
What gets done, sized to the project:
- First production order: quantity, price, delivery date, the inventor's yes. The office never places or pays for it.
- Final packaging, labels, instructions and warnings, matching the released revision and every certification's labeling rules.
- The buyer packet: spec sheet, instructions and warnings, test and certificate list, insurance certificate, tax form (filled by hand), vendor registrations, quote.
- Listings and marketing from the marketing plan: only true claims, backed by test results and certifications.
- The disclosure check one last time: anything about the invention still unfiled before it goes public?
- Final cost and timeline against the first estimates, and what was learned (a short lessons note for the library).
Gate: first sale or first showing done, with the first batch inspected per the control plan.

IF SOMETHING GOES WRONG AFTER LAUNCH
A problem that could hurt someone: stop shipping the affected units, say so plainly, and fix it through change control (`an-cost-and-risk` (Revisions and engineering change notices)). Safety first; never delayed for paperwork.
If a problem could seriously hurt someone, say so plainly and point to the reporting duty that may apply (for consumer products, CPSC; for medical devices, FDA). The inventor decides and reports; the office prepares the facts and never files for them. A professional is usually needed here.

WHO DOES WHAT
b-analyst prepares the launch paperwork and checks it against the released revision and the certifications. b-project-manager walks the inventor through it and records the decisions. The office never places orders, contacts customers, issues refunds, or files reports on the inventor's behalf.

## Moved
(procedure file: sop-launch-and-feedback.txt)

Moved. Launch is now `an-tooling-and-launch` (Launch) . The feedback loop was removed on October 8, 2026 (D-061).
