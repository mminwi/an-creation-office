# AN Creation Office: the procedures

Every procedure, template and data file the **AN Creation Office** runs on, in plain text. The live office is **https://ancreationoffice.com/** (start at the Welcome page). This repository is a copy of the same files, so an AI assistant such as Grok Bot, or a person, can read everything from one place.

AN Creation is two free AI bots for getting a product made. The Project Manager Bot walks an idea from fact-finding through design, prototyping, tooling, qualification and launch, brings in molding, plastic part design, quality and manufacturing when the product needs them, and keeps the paperwork. The Office Manager Bot runs the business around it: the company, patent preparation, a name and trademark, licensing, funding and selling. You make the decisions.

The procedures use role names (b-project-manager for the Project Manager Bot, b-business-manager for the Office Manager Bot). You name your own bots; the names go in `AN-Creation/team.csv`.

## Start with the website

**[https://ancreationoffice.com/](https://ancreationoffice.com/)** explains all of this far better than plain text files can. Read it first:

- [Welcome](https://ancreationoffice.com/): the two bots, and the message that starts each one
- [Start](https://ancreationoffice.com/start.html): set up your first bot in Grok, from your phone
- [How it works](https://ancreationoffice.com/system.html): how it works, and why
- [Terms you'll hear](https://ancreationoffice.com/terms.html): the engineering, manufacturing and business words, in plain language
- [Resources](https://ancreationoffice.com/resources.html): the library of sources the office works from
- [Keeping your project safe](https://ancreationoffice.com/version-control.html): saving and backups

This repository is the plain-text backbone: the same procedures, for AI assistants and for anyone who wants to read every word.

> **This is AI, and AI is changing quickly.** We keep working on it to make it the best it can be. You make the decisions and you use it at your own risk. Your work is saved to a private folder in your own Google Drive, with a dated copy kept before any big change: AI mixes things up often enough that going back to an earlier version is a normal part of working with it ([why](https://ancreationoffice.com/version-control.html)).

## Start here (for Grok Bot or any AI assistant)

Paste this into a new Grok Bot conversation:

```
You are my Project Manager Bot for AN Creation (role: b-project-manager).
First, set up your own profile. Open https://ancreationoffice.com/profile.txt,
find the Project Manager Bot block, and use your profile tool to set your description
to that block exactly as written and your title to "Project Manager Bot".
Read your profile back to me to confirm.
Then read and follow your office file: https://ancreationoffice.com/standing.txt
(same file: https://raw.githubusercontent.com/mminwi/an-creation-office/main/guide/standing.txt)
If you cannot open a link, ask me to paste the text.
If I have no project folder yet, help me set it up in my Google Drive, one step at a time: https://ancreationoffice.com/sop-office.txt
Then run office-setup-check and tell me the results.
Then ask what I want to work on. One question at a time.
```

**Links:** the procedures link to each other at `https://ancreationoffice.com/<file>`. Every one of those files is also in [`guide/`](guide/) here under the same name (raw text: `https://raw.githubusercontent.com/mminwi/an-creation-office/main/guide/<file>`). If a site link won't open, use the copy here.

## Every procedure

In the order of the procedure index ([`sop.txt`](guide/sop.txt)).

| File | What it is | Live |
|---|---|---|
| [`LICENSE.txt`](guide/LICENSE.txt) | License: © 2026 Advance Now LLC, CC BY-NC-SA 4.0 | [live](https://ancreationoffice.com/LICENSE.txt) |
| [`standing.txt`](guide/standing.txt) | The Project Manager Bot (b-project-manager), the chat the inventor talks to | [live](https://ancreationoffice.com/standing.txt) |
| [`business-manager.txt`](guide/business-manager.txt) | The Office Manager Bot (b-business-manager) | [live](https://ancreationoffice.com/business-manager.txt) |
| [`office-molding.txt`](guide/office-molding.txt) | Plant and product work, done by the Project Manager Bot from these files (older projects may still have a bot for one): Molding Plant | [live](https://ancreationoffice.com/office-molding.txt) |
| [`office-plastic-design.txt`](guide/office-plastic-design.txt) | Plant and product work, done by the Project Manager Bot from these files (older projects may still have a bot for one): Plastic Design | [live](https://ancreationoffice.com/office-plastic-design.txt) |
| [`office-quality.txt`](guide/office-quality.txt) | Plant and product work, done by the Project Manager Bot from these files (older projects may still have a bot for one): Quality | [live](https://ancreationoffice.com/office-quality.txt) |
| [`office-manufacturing.txt`](guide/office-manufacturing.txt) | Plant and product work, done by the Project Manager Bot from these files (older projects may still have a bot for one): Manufacturing | [live](https://ancreationoffice.com/office-manufacturing.txt) |
| [`analyst.txt`](guide/analyst.txt) | b-analyst, called by b-project-manager to do the thinking | [live](https://ancreationoffice.com/analyst.txt) |
| [`advance-now.txt`](guide/advance-now.txt) | The reason behind all of it, from Mike | [live](https://ancreationoffice.com/advance-now.txt) |
| [`version.txt`](guide/version.txt) | Version check, first in every conversation | [live](https://ancreationoffice.com/version.txt) |
| [`start-on-your-phone.txt`](guide/start-on-your-phone.txt) | For a first-time user, on a phone: start here | [live](https://ancreationoffice.com/start-on-your-phone.txt) |
| [`sop-team.txt`](guide/sop-team.txt) | Set up the Project Manager Bot and b-analyst. Each one is its own bot | [live](https://ancreationoffice.com/sop-team.txt) |
| [`sop-cooling-water.txt`](guide/sop-cooling-water.txt) | Specialist procedure: mold cooling water, b-cooling-water | [live](https://ancreationoffice.com/sop-cooling-water.txt) |
| [`sop-drying.txt`](guide/sop-drying.txt) | Specialist procedure: resin drying, b-drying-handling | [live](https://ancreationoffice.com/sop-drying.txt) |
| [`sop-scientific-molding.txt`](guide/sop-scientific-molding.txt) | Specialist procedure: scientific molding, b-scientific-molding | [live](https://ancreationoffice.com/sop-scientific-molding.txt) |
| [`sop-molding-defects.txt`](guide/sop-molding-defects.txt) | Specialist procedure: molding defect troubleshooting, b-molding-defects | [live](https://ancreationoffice.com/sop-molding-defects.txt) |
| [`sop-mold-buying.txt`](guide/sop-mold-buying.txt) | Specialist procedure: buying a mold, b-mold-buying (started) | [live](https://ancreationoffice.com/sop-mold-buying.txt) |
| [`sop-machine-safety.txt`](guide/sop-machine-safety.txt) | Specialist procedure: machine safety, b-machine-safety | [live](https://ancreationoffice.com/sop-machine-safety.txt) |
| [`sop-six-sigma.txt`](guide/sop-six-sigma.txt) | Specialist procedure: Lean Six Sigma projects, b-six-sigma | [live](https://ancreationoffice.com/sop-six-sigma.txt) |
| [`toolbox-improvement.txt`](guide/toolbox-improvement.txt) | The improvement toolbox: Lean, 5S, Six Sigma and TPS tools, picked by the problem | [live](https://ancreationoffice.com/toolbox-improvement.txt) |
| [`sop-market-check.txt`](guide/sop-market-check.txt) | Specialist procedure: Market check (b-market-check): who would buy it, asked without disclosing the idea | [live](https://ancreationoffice.com/sop-market-check.txt) |
| [`sop-licensing.txt`](guide/sop-licensing.txt) | Specialist procedure: Licensing (b-licensing): sell sheet, licensees, the approach, the deal with an attorney | [live](https://ancreationoffice.com/sop-licensing.txt) |
| [`sop-funding.txt`](guide/sop-funding.txt) | Specialist procedure: Funding (b-funding): the options by fit, what each asks for, watch-outs | [live](https://ancreationoffice.com/sop-funding.txt) |
| [`sop-plastic-part-design.txt`](guide/sop-plastic-part-design.txt) | Specialist procedure: Plastic part design (b-plastic-part-design): from the resin makers' design guides | [live](https://ancreationoffice.com/sop-plastic-part-design.txt) |
| [`sop-tolerance-stack.txt`](guide/sop-tolerance-stack.txt) | Specialist procedure: Tolerance stacks and print review (b-tolerance-gdt): worst case, RSS, Monte Carlo | [live](https://ancreationoffice.com/sop-tolerance-stack.txt) |
| [`sop-ai-cad.txt`](guide/sop-ai-cad.txt) | Specialist procedure: AI-assisted CAD (b-ai-cad): getting Claude Code and Codex to do SOLIDWORKS and KiCad work, the brief, and the checks | [live](https://ancreationoffice.com/sop-ai-cad.txt) |
| [`sop-material-selection.txt`](guide/sop-material-selection.txt) | Specialist procedure: Plastic material selection (b-plastic-materials): chemical compatibility first | [live](https://ancreationoffice.com/sop-material-selection.txt) |
| [`sop-manufacturing-cell.txt`](guide/sop-manufacturing-cell.txt) | Specialist procedure: Manufacturing cells and work design (b-manufacturing): takt, U-cells, standard work, ergonomics | [live](https://ancreationoffice.com/sop-manufacturing-cell.txt) |
| [`drive-setup.txt`](guide/drive-setup.txt) | The default project home: connecting Google Drive, the AN-Creation folder, saving and read-back, and the analyst (Grok Build) | [live](https://ancreationoffice.com/drive-setup.txt) |
| [`office-startup.txt`](guide/office-startup.txt) | The four shared skills: start a conversation, save, hand work to another office, and check that setup can write and read back | [live](https://ancreationoffice.com/office-startup.txt) |
| [`github-setup.txt`](guide/github-setup.txt) | Optional add-on for people who write code: private GitHub repository, clones, the analyst, and troubleshooting | [live](https://ancreationoffice.com/github-setup.txt) |
| [`sop-company.txt`](guide/sop-company.txt) | K1. b-business-manager: the company. Name checks, forming an LLC, tax ID, bank account, insurance, licenses, yearly upkeep | [live](https://ancreationoffice.com/sop-company.txt) |
| [`sop-website.txt`](guide/sop-website.txt) | K2. b-business-manager: domain, website, business email, Google Search Console and Bing, the weekly search check | [live](https://ancreationoffice.com/sop-website.txt) |
| [`sop-presence.txt`](guide/sop-presence.txt) | K3. b-business-manager: the brand kit and profiles. Logo, descriptions, fact sheet; LinkedIn, X, Facebook, YouTube and more | [live](https://ancreationoffice.com/sop-presence.txt) |
| [`sop-promotion.txt`](guide/sop-promotion.txt) | K4. b-business-manager: promotion and listings. Where to promote, the approval loop, pace and honesty, the patent check, directories | [live](https://ancreationoffice.com/sop-promotion.txt) |
| [`sop-focus.txt`](guide/sop-focus.txt) | Keep the project focused: risks as questions, decisions, "for now" and circling back | [live](https://ancreationoffice.com/sop-focus.txt) |
| [`ticket-template.txt`](guide/ticket-template.txt) | The ticket format b-project-manager runs | [live](https://ancreationoffice.com/ticket-template.txt) |
| [`agents-md.txt`](guide/agents-md.txt) | AGENTS.md for the inventor's repository: how any AI finds its ticket from one line | [live](https://ancreationoffice.com/agents-md.txt) |
| [`intake-001.csv`](guide/intake-001.csv) | The first form, always: the invention and the screening questions | [live](https://ancreationoffice.com/intake-001.csv) |
| [`screening-questions.csv`](guide/screening-questions.csv) | Screening: 25 questions that narrow the standards to the few that matter | [live](https://ancreationoffice.com/screening-questions.csv) |
| [`sop-resource-map.txt`](guide/sop-resource-map.txt) | Map the library to this project: in, later, out, ask | [live](https://ancreationoffice.com/sop-resource-map.txt) |
| [`sop-gateways.txt`](guide/sop-gateways.txt) | Gateways: the one fact before each side road | [live](https://ancreationoffice.com/sop-gateways.txt) |
| [`sop-graph.txt`](guide/sop-graph.txt) | Which form opens next. The flowchart | [live](https://ancreationoffice.com/sop-graph.txt) |
| [`project-description.txt`](guide/project-description.txt) | What fact-finding delivers: the project description, twelve sections, each with "done when" | [live](https://ancreationoffice.com/project-description.txt) |
| [`sop-stages.txt`](guide/sop-stages.txt) | Stages and tracks: S0 fact-finding, S1 design loop, S2 prototype loop, S3 tooling loop, S4 qualification, S5 launch. Quality planning (APQP) sized to the product and its risks; every stage ends with go, hold or drop | [live](https://ancreationoffice.com/sop-stages.txt) |
| [`sop-design-loop.txt`](guide/sop-design-loop.txt) | The design loop: industrial design then CAD, DFM from the first pass, the compliance matrix, recorded reviews | [live](https://ancreationoffice.com/sop-design-loop.txt) |
| [`sop-prototype-loop.txt`](guide/sop-prototype-loop.txt) | The prototype loop: build, test, refine, at whatever prototype levels it needs, to design freeze | [live](https://ancreationoffice.com/sop-prototype-loop.txt) |
| [`sop-tooling-loop.txt`](guide/sop-tooling-loop.txt) | The tooling loop: tool trials, design changes for tooling, final specs from measured parts and the stack-up | [live](https://ancreationoffice.com/sop-tooling-loop.txt) |
| [`sop-qualification.txt`](guide/sop-qualification.txt) | Qualification and production approval: first article, process trials, qualifying what's needed, the approval package | [live](https://ancreationoffice.com/sop-qualification.txt) |
| [`sop-launch.txt`](guide/sop-launch.txt) | Launch: first order, packaging and labels, the buyer packet, honest listings | [live](https://ancreationoffice.com/sop-launch.txt) |
| [`sop-change-control.txt`](guide/sop-change-control.txt) | Revisions and change control: C, X and A/B/C revision names; the change record and what a change must re-check | [live](https://ancreationoffice.com/sop-change-control.txt) |
| [`template-apqp-file.csv`](guide/template-apqp-file.csv) | Templates b-analyst fills: APQP file | [live](https://ancreationoffice.com/template-apqp-file.csv) |
| [`template-review-record.txt`](guide/template-review-record.txt) | Templates b-analyst fills: review record | [live](https://ancreationoffice.com/template-review-record.txt) |
| [`template-prototype-control-plan.txt`](guide/template-prototype-control-plan.txt) | Templates b-analyst fills: prototype control plan | [live](https://ancreationoffice.com/template-prototype-control-plan.txt) |
| [`template-trial-log.txt`](guide/template-trial-log.txt) | Templates b-analyst fills: trial log | [live](https://ancreationoffice.com/template-trial-log.txt) |
| [`template-fai-report.csv`](guide/template-fai-report.csv) | Templates b-analyst fills: first article report | [live](https://ancreationoffice.com/template-fai-report.csv) |
| [`template-change-record.txt`](guide/template-change-record.txt) | Templates b-analyst fills: change record | [live](https://ancreationoffice.com/template-change-record.txt) |
| [`template-cost-tracker.csv`](guide/template-cost-tracker.csv) | Templates b-analyst fills: cost and time tracker | [live](https://ancreationoffice.com/template-cost-tracker.csv) |
| [`sop-quality.txt`](guide/sop-quality.txt) | The quality chain | [live](https://ancreationoffice.com/sop-quality.txt) |
| [`sop-checklists.txt`](guide/sop-checklists.txt) | Fill a form from what is already known | [live](https://ancreationoffice.com/sop-checklists.txt) |
| [`sop-routes.txt`](guide/sop-routes.txt) | Roads in detail: patent, funding, company, standards, power, stores | [live](https://ancreationoffice.com/sop-routes.txt) |
| [`analyst-after-intake.txt`](guide/analyst-after-intake.txt) | Prepared prompts: after intake | [live](https://ancreationoffice.com/analyst-after-intake.txt) |
| [`analyst-refill.txt`](guide/analyst-refill.txt) | Prepared prompts: refill the queue | [live](https://ancreationoffice.com/analyst-refill.txt) |
| [`forms-catalog.csv`](guide/forms-catalog.csv) | Formal forms and documents each road produces | [live](https://ancreationoffice.com/forms-catalog.csv) |
| [`project-folders.txt`](guide/project-folders.txt) | The project folders: Your files and Office files. Dated folders; records are never edited once saved | [live](https://ancreationoffice.com/project-folders.txt) |
| [`sop-review-page.txt`](guide/sop-review-page.txt) | Review pages: a local web page per invention for timelines, risks, pictures, documents and short walkthroughs | [live](https://ancreationoffice.com/sop-review-page.txt) |
| [`terms.txt`](guide/terms.txt) | Terms: the plain-language glossary to explain terms from (about 200, with read-more links) | [live](https://ancreationoffice.com/terms.txt) |
| [`sop-action-log.txt`](guide/sop-action-log.txt) | The action log: who owes what, kept for the inventor and shown as Your list on the review page | [live](https://ancreationoffice.com/sop-action-log.txt) |

## Reference files, templates and data

Used by the procedures above: guides, worksheets, templates, and the resource library as data.

| File | What it is | Live |
|---|---|---|
| [`advance-now-roadblocks.csv`](guide/advance-now-roadblocks.csv) | Worksheet / table (CSV): Issue ID / existing risk ID, Concern / what is known or uncertain, Affected activity, Possible route around or through... | [live](https://ancreationoffice.com/advance-now-roadblocks.csv) |
| [`advance-now.json`](guide/advance-now.json) | Data behind the advance now page (JSON) | [live](https://ancreationoffice.com/advance-now.json) |
| [`blender-template.py`](guide/blender-template.py) | Tool / template script (Python) | [live](https://ancreationoffice.com/blender-template.py) |
| [`bot-names.txt`](guide/bot-names.txt) | Names for your bots. Revision 1 — October 12, 2026. | [live](https://ancreationoffice.com/bot-names.txt) |
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
| [`library.txt`](guide/library.txt) | 261018.2 | [live](https://ancreationoffice.com/library.txt) |
| [`manufacturing.txt`](guide/manufacturing.txt) | Manufacturing role. Reference for b-project-manager when the manufacturing role is the one in front of it. The | [live](https://ancreationoffice.com/manufacturing.txt) |
| [`office-automation-machine.txt`](guide/office-automation-machine.txt) | AN Creation: the Automation Machine Office (role b-automation-machine). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-automation-machine.txt) |
| [`office-charger-board.txt`](guide/office-charger-board.txt) | AN Creation: the Charger Board Office (role b-charger-board). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-charger-board.txt) |
| [`office-handoff.txt`](guide/office-handoff.txt) | AN Creation skill: office-handoff. The office rule is https://ancreationoffice.com/sop-team.txt HAND-OFFS. | [live](https://ancreationoffice.com/office-handoff.txt) |
| [`office-mil-battery.txt`](guide/office-mil-battery.txt) | AN Creation: the MIL Battery Office (role b-mil-battery). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-mil-battery.txt) |
| [`office-pneumatic-fixture.txt`](guide/office-pneumatic-fixture.txt) | AN Creation: the Pneumatic Fixture Office (role b-pneumatic-fixture). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-pneumatic-fixture.txt) |
| [`office-promotion.txt`](guide/office-promotion.txt) | AN Creation: the Promotion Office (role b-promotion-office). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-promotion.txt) |
| [`office-rugged-enclosure.txt`](guide/office-rugged-enclosure.txt) | AN Creation: the Rugged Enclosure Office (role b-rugged-enclosure). Revision 4 — October 17, 2026. | [live](https://ancreationoffice.com/office-rugged-enclosure.txt) |
| [`office-save.txt`](guide/office-save.txt) | AN Creation skill: office-save. The office rule is https://ancreationoffice.com/version-control.txt SAVING and | [live](https://ancreationoffice.com/office-save.txt) |
| [`office-setup-check.txt`](guide/office-setup-check.txt) | AN Creation skill: office-setup-check. Run once after https://ancreationoffice.com/drive-setup.txt, and report | [live](https://ancreationoffice.com/office-setup-check.txt) |
| [`office-spacex.txt`](guide/office-spacex.txt) | AN Creation: the SpaceX Office (role b-spacex-office). Revision 2 — October 14, 2026. | [live](https://ancreationoffice.com/office-spacex.txt) |
| [`office-version-history.txt`](guide/office-version-history.txt) | AN Creation office version history, retired from the startup file on October 14, 2026. | [live](https://ancreationoffice.com/office-version-history.txt) |
| [`plan-template.txt`](guide/plan-template.txt) | Project plan | [live](https://ancreationoffice.com/plan-template.txt) |
| [`planning-resources.json`](guide/planning-resources.json) | Data behind the planning resources page (JSON) | [live](https://ancreationoffice.com/planning-resources.json) |
| [`planning-resources.txt`](guide/planning-resources.txt) | Product, startup and project planning. Checked 2026-09-30. | [live](https://ancreationoffice.com/planning-resources.txt) |
| [`planning-review.csv`](guide/planning-review.csv) | Worksheet / table (CSV): Item ID, Question, Suggested roles, Source IDs... | [live](https://ancreationoffice.com/planning-review.csv) |
| [`product-development.txt`](guide/product-development.txt) | PRODUCT DEVELOPMENT: THE PROCESS BEHIND THE CONVERSATION | [live](https://ancreationoffice.com/product-development.txt) |
| [`profile.txt`](guide/profile.txt) | AN Creation bot profiles (October 18, 2026). b-project-manager profile version 6. b-business-manager profile v | [live](https://ancreationoffice.com/profile.txt) |
| [`project-manager.txt`](guide/project-manager.txt) | b-project-manager: the project manager role for AN Creation. The inventor names the bot that covers it (https: | [live](https://ancreationoffice.com/project-manager.txt) |
| [`resource-crosscheck.json`](guide/resource-crosscheck.json) | Data behind the resource crosscheck page (JSON) | [live](https://ancreationoffice.com/resource-crosscheck.json) |
| [`resource-crosscheck.txt`](guide/resource-crosscheck.txt) | Resource cross-check, September 30, 2026. | [live](https://ancreationoffice.com/resource-crosscheck.txt) |
| [`resources.json`](guide/resources.json) | Data behind the resources page (JSON) | [live](https://ancreationoffice.com/resources.json) |
| [`resources.txt`](guide/resources.txt) | Resource use for b-project-manager. Same entries as the human shelves linked from https://ancreationoffice.com | [live](https://ancreationoffice.com/resources.txt) |
| [`review.py`](guide/review.py) | Tool: builds the inventor's local review pages | [live](https://ancreationoffice.com/review.py) |
| [`revision-log.csv`](guide/revision-log.csv) | Worksheet / table (CSV): item_id, title, revision, previous_revision... | [live](https://ancreationoffice.com/revision-log.csv) |
| [`revisions.txt`](guide/revisions.txt) | AN Creation revision control. Human lesson: https://ancreationoffice.com/revisions.html | [live](https://ancreationoffice.com/revisions.txt) |
| [`robots.txt`](guide/robots.txt) | User-agent: * | [live](https://ancreationoffice.com/robots.txt) |
| [`sop-automation-controls.txt`](guide/sop-automation-controls.txt) | SOP: Controls for an automation machine. PLC, servo motion, the control panel, machine states, networks. Revis | [live](https://ancreationoffice.com/sop-automation-controls.txt) |
| [`sop-automation-handling.txt`](guide/sop-automation-handling.txt) | SOP: Moving and processing small parts on an automation machine. Air (tube) feeding, nests and the index wheel | [live](https://ancreationoffice.com/sop-automation-handling.txt) |
| [`sop-automation-project.txt`](guide/sop-automation-project.txt) | SOP: Running a custom automation machine project, from specification to buy-off. Revision 1 — October 13, 2026 | [live](https://ancreationoffice.com/sop-automation-project.txt) |
| [`sop-automation-vision.txt`](guide/sop-automation-vision.txt) | SOP: Machine vision for inspection and good/bad sorting. Revision 1 — October 13, 2026. | [live](https://ancreationoffice.com/sop-automation-vision.txt) |
| [`sop-board-design.txt`](guide/sop-board-design.txt) | SOP: Designing a small circuit board with free tools. From the idea to a checked design ready for a prototype  | [live](https://ancreationoffice.com/sop-board-design.txt) |
| [`sop-board-emi.txt`](guide/sop-board-emi.txt) | SOP: Clean power and low EMI on a small board with a switching converter. Layout rules, filtering, measuring r | [live](https://ancreationoffice.com/sop-board-emi.txt) |
| [`sop-board-prototype.txt`](guide/sop-board-prototype.txt) | SOP: Getting prototype boards made from a free-tools design. What to send the shop, handing a KiCad design to  | [live](https://ancreationoffice.com/sop-board-prototype.txt) |
| [`sop-charger-circuit.txt`](guide/sop-charger-circuit.txt) | SOP: A charger for power-tool lithium-ion battery packs, with USB-C power. How the circuit is set up, the deci | [live](https://ancreationoffice.com/sop-charger-circuit.txt) |
| [`sop-hats.txt`](guide/sop-hats.txt) | SOP: Form, record, and call a session. Revision 3 — October 1, 2026. | [live](https://ancreationoffice.com/sop-hats.txt) |
| [`sop-intake-survey.txt`](guide/sop-intake-survey.txt) | SOP: The intake survey. Collecting a large project's facts from its documents in one pass, instead of one ques | [live](https://ancreationoffice.com/sop-intake-survey.txt) |
| [`sop-interns.txt`](guide/sop-interns.txt) | SOP: Use an intern. Revision 1 — October 1, 2026. | [live](https://ancreationoffice.com/sop-interns.txt) |
| [`sop-mil-electronics-build.txt`](guide/sop-mil-electronics-build.txt) | SOP: Building military electronics. Workmanship classes, boards, conformal coating, cables and shielding. Revi | [live](https://ancreationoffice.com/sop-mil-electronics-build.txt) |
| [`sop-mil-emi.txt`](guide/sop-mil-emi.txt) | SOP: Military EMI/EMC (MIL-STD-461) for a small soldier-worn power device. Revision 1 — October 13, 2026. | [live](https://ancreationoffice.com/sop-mil-emi.txt) |
| [`sop-mil-enclosure.txt`](guide/sop-mil-enclosure.txt) | SOP: A sealed, shielded aluminum enclosure. Conductive gaskets, compression and stack-up, finishes, galvanic c | [live](https://ancreationoffice.com/sop-mil-enclosure.txt) |
| [`sop-mil-environmental.txt`](guide/sop-mil-environmental.txt) | SOP: Military environmental testing (MIL-STD-810) for soldier-worn electronics. Revision 1 — October 13, 2026. | [live](https://ancreationoffice.com/sop-mil-environmental.txt) |
| [`sop-mil-power.txt`](guide/sop-mil-power.txt) | SOP: Battery-powered electronics for the project manager. Lithium-ion charging, power paths, USB power, and th | [live](https://ancreationoffice.com/sop-mil-power.txt) |
| [`sop-mil-program.txt`](guide/sop-mil-program.txt) | SOP: Running a defense hardware project. Program management, AS9100, configuration, first article, and qualifi | [live](https://ancreationoffice.com/sop-mil-program.txt) |
| [`sop-office.txt`](guide/sop-office.txt) | SOP: Set up b-project-manager and b-analyst. Revision 13 — October 18, 2026. | [live](https://ancreationoffice.com/sop-office.txt) |
| [`sop-pneumatic-fixture.txt`](guide/sop-pneumatic-fixture.txt) | SOP: A pneumatic assembly fixture with air-logic controls. Two-hand start, guard locking, cylinders, the fixtu | [live](https://ancreationoffice.com/sop-pneumatic-fixture.txt) |
| [`sop-promo-audience.txt`](guide/sop-promo-audience.txt) | SOP: Building Mike's audience. Positioning, the topics he's known for, a weekly rhythm, the numbers to watch,  | [live](https://ancreationoffice.com/sop-promo-audience.txt) |
| [`sop-promo-channels.txt`](guide/sop-promo-channels.txt) | SOP: Other ways to get the word out. Reddit, Hacker News, Product Hunt, YouTube, podcasts, press, newsletters, | [live](https://ancreationoffice.com/sop-promo-channels.txt) |
| [`sop-promo-images.txt`](guide/sop-promo-images.txt) | SOP: Pictures for Mike's posts. Writing prompts for Grok Imagine (or another image AI), the house style, sizes | [live](https://ancreationoffice.com/sop-promo-images.txt) |
| [`sop-promo-linkedin.txt`](guide/sop-promo-linkedin.txt) | SOP: LinkedIn for Mike. The profile, the company page, posts that get read, comments, the newsletter, and meas | [live](https://ancreationoffice.com/sop-promo-linkedin.txt) |
| [`sop-promo-voice.txt`](guide/sop-promo-voice.txt) | SOP: Writing as Mike Maier. His voice, the rules about what to say and not say, and how to learn from his edit | [live](https://ancreationoffice.com/sop-promo-voice.txt) |
| [`sop-promo-x.txt`](guide/sop-promo-x.txt) | SOP: X for Mike. How the feed picks posts, replies that build an audience, posts and threads, and using Grok's | [live](https://ancreationoffice.com/sop-promo-x.txt) |
| [`sop-rugged-cots.txt`](guide/sop-rugged-cots.txt) | SOP: Ruggedizing a commercial electronic product for military use. An off-the-shelf enclosure and connectors,  | [live](https://ancreationoffice.com/sop-rugged-cots.txt) |
| [`sop-spacex-practice.txt`](guide/sop-spacex-practice.txt) | SOP: Turning one finding into something Mike can use. Revision 1 — October 13, 2026. | [live](https://ancreationoffice.com/sop-spacex-practice.txt) |
| [`sop-spacex-watch.txt`](guide/sop-spacex-watch.txt) | SOP: What the SpaceX Office watches. X first, then the official page a post points at. Revision 1 — October 13 | [live](https://ancreationoffice.com/sop-spacex-watch.txt) |
| [`sop.txt`](guide/sop.txt) | AN Creation standard operating procedures. Revision 13 — October 18, 2026. | [live](https://ancreationoffice.com/sop.txt) |
| [`sops-manifest.txt`](guide/sops-manifest.txt) | 261018.2 | [live](https://ancreationoffice.com/sops-manifest.txt) |
| [`status-template.txt`](guide/status-template.txt) | STATUS SHEET: one page, answers only. Rewritten by b-analyst every run as "Your files/Status" (inventor's form | [live](https://ancreationoffice.com/status-template.txt) |
| [`survey-automation-machine.csv`](guide/survey-automation-machine.csv) | Worksheet / table (CSV): id, section, question, why... | [live](https://ancreationoffice.com/survey-automation-machine.csv) |
| [`survey-fill-instructions.txt`](guide/survey-fill-instructions.txt) | Instructions for the AI filling an AN Creation intake survey. Give these to the AI along with the survey file  | [live](https://ancreationoffice.com/survey-fill-instructions.txt) |
| [`survey-mil-battery.csv`](guide/survey-mil-battery.csv) | Worksheet / table (CSV): id, section, question, why... | [live](https://ancreationoffice.com/survey-mil-battery.csv) |
| [`survey-pneumatic-fixture.csv`](guide/survey-pneumatic-fixture.csv) | Worksheet / table (CSV): id, section, question, why... | [live](https://ancreationoffice.com/survey-pneumatic-fixture.csv) |
| [`survey-rugged-enclosure.csv`](guide/survey-rugged-enclosure.csv) | Worksheet / table (CSV): id, section, question, why... | [live](https://ancreationoffice.com/survey-rugged-enclosure.csv) |
| [`template-a3.txt`](guide/template-a3.txt) | One-page project summary (A3). Template, from Mike's practice (sop-six-sigma.txt section 6). Copy into the pro | [live](https://ancreationoffice.com/template-a3.txt) |
| [`template-action-log.csv`](guide/template-action-log.csv) | Worksheet / table (CSV): ID, Opened, Action, Who... | [live](https://ancreationoffice.com/template-action-log.csv) |
| [`template-team.csv`](guide/template-team.csv) | Worksheet / table (CSV): name, covers, reports_to, platform... | [live](https://ancreationoffice.com/template-team.csv) |
| [`test-matrix.csv`](guide/test-matrix.csv) | Worksheet / table (CSV): Project, Plan ID / revision, Test ID, Requirement / CTQ / risk IDs... | [live](https://ancreationoffice.com/test-matrix.csv) |
| [`test-plan-template.txt`](guide/test-plan-template.txt) | AN CREATION — TEST PLAN TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-plan-template.txt) |
| [`test-planning.json`](guide/test-planning.json) | Data behind the test planning page (JSON) | [live](https://ancreationoffice.com/test-planning.json) |
| [`test-planning.txt`](guide/test-planning.txt) | Plan the test before the build — REV 1 — 2026-09-30 | [live](https://ancreationoffice.com/test-planning.txt) |
| [`test-report-template.txt`](guide/test-report-template.txt) | AN CREATION — TEST REPORT TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-report-template.txt) |
| [`using-other-ais.txt`](guide/using-other-ais.txt) | AN Creation: using Claude, ChatGPT (Codex), Cursor, or another AI. Revision 2 — October 14, 2026. | [live](https://ancreationoffice.com/using-other-ais.txt) |
| [`version-control.txt`](guide/version-control.txt) | AN Creation backups and version control. Revision 7 — October 14, 2026. Human page: https://ancreationoffice.c | [live](https://ancreationoffice.com/version-control.txt) |

## The specialists

The [`specialists/`](specialists/) folder (kept in this repository, not synced) holds the roster, the role map ([`specialists/roles.csv`](specialists/roles.csv)), the calculations the analyst runs ([`specialists/calcs/`](specialists/calcs/)). [`specialists/tools/build_offices.py`](specialists/tools/build_offices.py) built the six office pages and is retired: the site has two bots now, and its start page is written by hand. The next sync overwrites `guide/` from creation-office `site/create/`, so a file written only into `guide/` does not last.


## License

© 2026 Advance Now LLC. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (full text: [LICENSE](LICENSE); explained in plain words at [https://ancreationoffice.com/license.html](https://ancreationoffice.com/license.html)).

**Using AN Creation for your own inventions is free and always welcome, even if you sell the product. What's not allowed is selling these procedures, or a paid program or service built on them.** Share it and adapt it freely; credit Advance Now LLC with a link to the website, and keep anything you build from it under the same license.

## How this copy is kept

Synced from the live site by a script after each publish. If this copy and https://ancreationoffice.com/ ever differ, the live site is current.

*Last synced October 18, 2026.*
