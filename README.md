# AN Creation Office: the procedures

Every procedure, template and data file the **AN Creation Office** runs on, in plain text. The live office is **https://ancreationoffice.com/** (start at the Welcome page). This repository is a copy of the same files, so an AI assistant such as Grok Bot, or a person, can read everything from one place.

AN Creation is a free, AI-run product development office for inventors: Soren, your project manager, walks an idea from fact-finding through design, prototyping, tooling, qualification and launch, at an automotive level of quality, and keeps the paperwork. You make the decisions.

## Start with the website

**[https://ancreationoffice.com/](https://ancreationoffice.com/)** explains all of this far better than plain text files can. Read it first:

- [Welcome](https://ancreationoffice.com/): what the office is, the stages, and what you get at each one
- [Start](https://ancreationoffice.com/start.html): set up Soren in Grok Bot in a few minutes
- [Info](https://ancreationoffice.com/system.html): how it works, and why
- [Soren](https://ancreationoffice.com/soren.html): your project manager, and every procedure he follows
- [Terms you'll hear](https://ancreationoffice.com/terms.html): the engineering, manufacturing and business words, in plain language
- [Resources](https://ancreationoffice.com/resources.html): the library of sources the office works from
- [Keeping your project safe](https://ancreationoffice.com/version-control.html): Git and backups

This repository is the plain-text backbone: the same procedures, for AI assistants and for anyone who wants to read every word.

> **This is AI, and AI is changing quickly.** We keep working on it to make it the best it can be. You make the decisions and you use it at your own risk. **Please use Git** for your project folder: AI mixes things up often enough that going back in the history is close to a daily event ([why](https://ancreationoffice.com/version-control.html)).

## Start here (for Grok Bot or any AI assistant)

Paste this into a new Grok Bot conversation:

```
You are Soren, my project manager for AN Creation.
Read and follow your standing instructions:
https://ancreationoffice.com/standing.txt
(same file: https://raw.githubusercontent.com/mminwi/an-creation-office/main/guide/standing.txt)
If you cannot open a link, ask me to paste the text.
Help me set up first, one step at a time:
https://ancreationoffice.com/sop-office.txt
(my project folder, the analyst, and Git for backups).
Then ask me to tell you about my invention.
One question at a time. Take one role at a time; do not create other named bots.
```

**Links:** the procedures link to each other at `https://ancreationoffice.com/<file>`. Every one of those files is also in [`guide/`](guide/) here under the same name (raw text: `https://raw.githubusercontent.com/mminwi/an-creation-office/main/guide/<file>`). If a site link won't open, use the copy here.

## Every procedure

In the order of the procedure index ([`sop.txt`](guide/sop.txt)).

| File | What it is | Live |
|---|---|---|
| [`standing.txt`](guide/standing.txt) | Soren, the chat the inventor talks to | [live](https://ancreationoffice.com/standing.txt) |
| [`analyst.txt`](guide/analyst.txt) | The analyst, called by Soren to do the thinking | [live](https://ancreationoffice.com/analyst.txt) |
| [`advance-now.txt`](guide/advance-now.txt) | The reason behind all of it, from Mike | [live](https://ancreationoffice.com/advance-now.txt) |
| [`sop-office.txt`](guide/sop-office.txt) | Set up Soren and the analyst: one Soren for all inventions or one per invention, the inventor's choice | [live](https://ancreationoffice.com/sop-office.txt) |
| [`sop-focus.txt`](guide/sop-focus.txt) | Keep the project focused: risks as questions, decisions, "for now" and circling back | [live](https://ancreationoffice.com/sop-focus.txt) |
| [`ticket-template.txt`](guide/ticket-template.txt) | The ticket format Soren runs | [live](https://ancreationoffice.com/ticket-template.txt) |
| [`intake-001.csv`](guide/intake-001.csv) | The first form, always: the invention and the screening questions | [live](https://ancreationoffice.com/intake-001.csv) |
| [`screening-questions.csv`](guide/screening-questions.csv) | Screening: 25 questions that narrow the standards to the few that matter | [live](https://ancreationoffice.com/screening-questions.csv) |
| [`sop-resource-map.txt`](guide/sop-resource-map.txt) | Map the library to this project: in, later, out, ask | [live](https://ancreationoffice.com/sop-resource-map.txt) |
| [`sop-gateways.txt`](guide/sop-gateways.txt) | Gateways: the one fact before each side road | [live](https://ancreationoffice.com/sop-gateways.txt) |
| [`sop-graph.txt`](guide/sop-graph.txt) | Which form opens next. The flowchart | [live](https://ancreationoffice.com/sop-graph.txt) |
| [`project-description.txt`](guide/project-description.txt) | What fact-finding delivers: the project description, twelve sections, each with "done when" | [live](https://ancreationoffice.com/project-description.txt) |
| [`sop-stages.txt`](guide/sop-stages.txt) | Stages and tracks: S0 fact-finding, S1 design loop, S2 prototype loop, S3 tooling loop, S4 qualification, S5 launch. A formal APQP on every project; every stage ends with go, hold or drop | [live](https://ancreationoffice.com/sop-stages.txt) |
| [`sop-design-loop.txt`](guide/sop-design-loop.txt) | The design loop: industrial design then CAD, DFM from the first pass, the compliance matrix, recorded reviews | [live](https://ancreationoffice.com/sop-design-loop.txt) |
| [`sop-prototype-loop.txt`](guide/sop-prototype-loop.txt) | The prototype loop: build, test, refine, at whatever prototype levels it needs, to design freeze | [live](https://ancreationoffice.com/sop-prototype-loop.txt) |
| [`sop-tooling-loop.txt`](guide/sop-tooling-loop.txt) | The tooling loop: tool trials, design changes for tooling, final specs from measured parts and the stack-up | [live](https://ancreationoffice.com/sop-tooling-loop.txt) |
| [`sop-qualification.txt`](guide/sop-qualification.txt) | Qualification and production approval: first article, process trials, qualifying what's needed, the approval package | [live](https://ancreationoffice.com/sop-qualification.txt) |
| [`sop-launch.txt`](guide/sop-launch.txt) | Launch: first order, packaging and labels, the buyer packet, honest listings | [live](https://ancreationoffice.com/sop-launch.txt) |
| [`sop-change-control.txt`](guide/sop-change-control.txt) | Revisions and change control: C, X and A/B/C revision names; the change record and what a change must re-check | [live](https://ancreationoffice.com/sop-change-control.txt) |
| [`template-apqp-file.csv`](guide/template-apqp-file.csv) | Templates the analyst fills: APQP file | [live](https://ancreationoffice.com/template-apqp-file.csv) |
| [`template-review-record.txt`](guide/template-review-record.txt) | Templates the analyst fills: review record | [live](https://ancreationoffice.com/template-review-record.txt) |
| [`template-prototype-control-plan.txt`](guide/template-prototype-control-plan.txt) | Templates the analyst fills: prototype control plan | [live](https://ancreationoffice.com/template-prototype-control-plan.txt) |
| [`template-trial-log.txt`](guide/template-trial-log.txt) | Templates the analyst fills: trial log | [live](https://ancreationoffice.com/template-trial-log.txt) |
| [`template-fai-report.csv`](guide/template-fai-report.csv) | Templates the analyst fills: first article report | [live](https://ancreationoffice.com/template-fai-report.csv) |
| [`template-change-record.txt`](guide/template-change-record.txt) | Templates the analyst fills: change record | [live](https://ancreationoffice.com/template-change-record.txt) |
| [`template-cost-tracker.csv`](guide/template-cost-tracker.csv) | Templates the analyst fills: cost and time tracker | [live](https://ancreationoffice.com/template-cost-tracker.csv) |
| [`sop-quality.txt`](guide/sop-quality.txt) | The quality chain | [live](https://ancreationoffice.com/sop-quality.txt) |
| [`sop-checklists.txt`](guide/sop-checklists.txt) | Fill a form from what is already known | [live](https://ancreationoffice.com/sop-checklists.txt) |
| [`sop-routes.txt`](guide/sop-routes.txt) | Roads in detail: patent, funding, company, standards, power, stores | [live](https://ancreationoffice.com/sop-routes.txt) |
| [`analyst-after-intake.txt`](guide/analyst-after-intake.txt) | Prepared prompts: after intake | [live](https://ancreationoffice.com/analyst-after-intake.txt) |
| [`analyst-refill.txt`](guide/analyst-refill.txt) | Prepared prompts: refill the queue | [live](https://ancreationoffice.com/analyst-refill.txt) |
| [`forms-catalog.csv`](guide/forms-catalog.csv) | Formal forms and documents each road produces | [live](https://ancreationoffice.com/forms-catalog.csv) |
| [`project-folders.txt`](guide/project-folders.txt) | The project folders: Your files and Soren's files. Dated folders; nothing is overwritten | [live](https://ancreationoffice.com/project-folders.txt) |
| [`sop-review-page.txt`](guide/sop-review-page.txt) | Review pages: a local web page per invention for timelines, risks, pictures, documents and short walkthroughs | [live](https://ancreationoffice.com/sop-review-page.txt) |
| [`terms.txt`](guide/terms.txt) | Terms: the plain-language glossary to explain terms from (about 200, with read-more links) | [live](https://ancreationoffice.com/terms.txt) |
| [`sop-action-log.txt`](guide/sop-action-log.txt) | The action log: who owes what, kept for the inventor and shown as Your list on the review page | [live](https://ancreationoffice.com/sop-action-log.txt) |

## Reference files, templates and data

Used by the procedures above: guides, worksheets, templates, and the resource library as data.

| File | What it is | Live |
|---|---|---|
| [`advance-now-roadblocks.csv`](guide/advance-now-roadblocks.csv) | Worksheet / table (CSV): Issue ID / existing risk ID, Concern / what is known or uncertain, Affected activity, Possible route around or through... | [live](https://ancreationoffice.com/advance-now-roadblocks.csv) |
| [`advance-now.json`](guide/advance-now.json) | Data behind the advance now page (JSON) | [live](https://ancreationoffice.com/advance-now.json) |
| [`check-sheets.csv`](guide/check-sheets.csv) | Worksheet / table (CSV): Project, Product revision, Sheet revision, Prepared by... | [live](https://ancreationoffice.com/check-sheets.csv) |
| [`check-sheets.json`](guide/check-sheets.json) | Data behind the check sheets page (JSON) | [live](https://ancreationoffice.com/check-sheets.json) |
| [`check-sheets.txt`](guide/check-sheets.txt) | Product development check sheets — Revision 1 — 2026-09-30 | [live](https://ancreationoffice.com/check-sheets.txt) |
| [`compliance-matrix-template.csv`](guide/compliance-matrix-template.csv) | Worksheet / table (CSV): ID, Source, Requirement, Kind... | [live](https://ancreationoffice.com/compliance-matrix-template.csv) |
| [`control-plan.csv`](guide/control-plan.csv) | Worksheet / table (CSV): Control ID, Plan phase (prototype/prelaunch/production), Product and drawing revision, Process flow revision and step... | [live](https://ancreationoffice.com/control-plan.csv) |
| [`critical-quality.csv`](guide/critical-quality.csv) | Worksheet / table (CSV): CTQ ID, Original concern or customer need, Raised by and source, Source revision or date... | [live](https://ancreationoffice.com/critical-quality.csv) |
| [`design-principles-review.csv`](guide/design-principles-review.csv) | Worksheet / table (CSV): Project, Concept / exact revision, Area ID, Review area... | [live](https://ancreationoffice.com/design-principles-review.csv) |
| [`design-principles.json`](guide/design-principles.json) | Data behind the design principles page (JSON) | [live](https://ancreationoffice.com/design-principles.json) |
| [`design-principles.txt`](guide/design-principles.txt) | DESIGN PRINCIPLES: PEOPLE, FORM AND USE | [live](https://ancreationoffice.com/design-principles.txt) |
| [`design-review.txt`](guide/design-review.txt) | AN CREATION — SHORT DESIGN AND FAILURE REVIEW — TEMPLATE REV 1 | [live](https://ancreationoffice.com/design-review.txt) |
| [`design-risk.txt`](guide/design-risk.txt) | AN Creation — Design risk and troubleshooting. Revision 1, September 30, 2026. | [live](https://ancreationoffice.com/design-risk.txt) |
| [`handoff-log.csv`](guide/handoff-log.csv) | Worksheet / table (CSV): handoff_id, sent_date, sender, recipient... | [live](https://ancreationoffice.com/handoff-log.csv) |
| [`ip-ratings.txt`](guide/ip-ratings.txt) | IP enclosure ratings. Basic orientation only; use IEC 60529 and the actual test evidence for requirements and  | [live](https://ancreationoffice.com/ip-ratings.txt) |
| [`manufacturing.txt`](guide/manufacturing.txt) | Manufacturing role. Reference for Soren when the manufacturing role is the one in front of him. This is not a  | [live](https://ancreationoffice.com/manufacturing.txt) |
| [`plan-template.txt`](guide/plan-template.txt) | Project plan | [live](https://ancreationoffice.com/plan-template.txt) |
| [`planning-resources.json`](guide/planning-resources.json) | Data behind the planning resources page (JSON) | [live](https://ancreationoffice.com/planning-resources.json) |
| [`planning-resources.txt`](guide/planning-resources.txt) | Product, startup and project planning. Checked 2026-09-30. | [live](https://ancreationoffice.com/planning-resources.txt) |
| [`planning-review.csv`](guide/planning-review.csv) | Worksheet / table (CSV): Item ID, Question, Suggested roles, Source IDs... | [live](https://ancreationoffice.com/planning-review.csv) |
| [`product-development.txt`](guide/product-development.txt) | PRODUCT DEVELOPMENT: THE PROCESS BEHIND THE CONVERSATION | [live](https://ancreationoffice.com/product-development.txt) |
| [`resource-crosscheck.json`](guide/resource-crosscheck.json) | Data behind the resource crosscheck page (JSON) | [live](https://ancreationoffice.com/resource-crosscheck.json) |
| [`resource-crosscheck.txt`](guide/resource-crosscheck.txt) | Resource cross-check, September 30, 2026. | [live](https://ancreationoffice.com/resource-crosscheck.txt) |
| [`resources.json`](guide/resources.json) | Data behind the resources page (JSON) | [live](https://ancreationoffice.com/resources.json) |
| [`resources.txt`](guide/resources.txt) | Resource use for Soren. Same entries as the human shelves linked from https://ancreationoffice.com/resources.h | [live](https://ancreationoffice.com/resources.txt) |
| [`review.py`](guide/review.py) | Tool: builds the inventor's local review pages | [live](https://ancreationoffice.com/review.py) |
| [`revision-log.csv`](guide/revision-log.csv) | Worksheet / table (CSV): item_id, title, revision, previous_revision... | [live](https://ancreationoffice.com/revision-log.csv) |
| [`revisions.txt`](guide/revisions.txt) | AN Creation revision control. Human lesson: https://ancreationoffice.com/revisions.html | [live](https://ancreationoffice.com/revisions.txt) |
| [`sop-hats.txt`](guide/sop-hats.txt) | SOP: Form, record, and call a session. Revision 3 — October 1, 2026. | [live](https://ancreationoffice.com/sop-hats.txt) |
| [`sop-interns.txt`](guide/sop-interns.txt) | SOP: Use an intern. Revision 1 — October 1, 2026. | [live](https://ancreationoffice.com/sop-interns.txt) |
| [`sop.txt`](guide/sop.txt) | AN Creation standard operating procedures. Revision 11 — October 8, 2026. | [live](https://ancreationoffice.com/sop.txt) |
| [`soren.txt`](guide/soren.txt) | Soren. Project manager for AN Creation. | [live](https://ancreationoffice.com/soren.txt) |
| [`status-template.txt`](guide/status-template.txt) | STATUS SHEET: one page, answers only. Rewritten by the analyst every run as "Your files/Status" (inventor's fo | [live](https://ancreationoffice.com/status-template.txt) |
| [`template-action-log.csv`](guide/template-action-log.csv) | Worksheet / table (CSV): ID, Opened, Action, Who... | [live](https://ancreationoffice.com/template-action-log.csv) |
| [`test-matrix.csv`](guide/test-matrix.csv) | Worksheet / table (CSV): Project, Plan ID / revision, Test ID, Requirement / CTQ / risk IDs... | [live](https://ancreationoffice.com/test-matrix.csv) |
| [`test-plan-template.txt`](guide/test-plan-template.txt) | AN CREATION — TEST PLAN TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-plan-template.txt) |
| [`test-planning.json`](guide/test-planning.json) | Data behind the test planning page (JSON) | [live](https://ancreationoffice.com/test-planning.json) |
| [`test-planning.txt`](guide/test-planning.txt) | Plan the test before the build — REV 1 — 2026-09-30 | [live](https://ancreationoffice.com/test-planning.txt) |
| [`test-report-template.txt`](guide/test-report-template.txt) | AN CREATION — TEST REPORT TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-report-template.txt) |
| [`version-control.txt`](guide/version-control.txt) | AN Creation backups and version control. Revision 2 — October 8, 2026. Human page: https://ancreationoffice.co | [live](https://ancreationoffice.com/version-control.txt) |

## How this copy is kept

Synced from the live site by a script after each publish. If this copy and https://ancreationoffice.com/ ever differ, the live site is current.

*Last synced October 10, 2026.*
