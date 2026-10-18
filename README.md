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
| [`sop-folder-move.txt`](guide/sop-folder-move.txt) | Moving an older project folder to the business layout, once, with the owner's yes | [live](https://ancreationoffice.com/sop-folder-move.txt) |
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
| [`drive-setup.txt`](guide/drive-setup.txt) | The project home: ask where the owner wants the project folder (a cloud folder like Google Drive or OneDrive is best; anywhere the bot can write to works), the AN-Creation folder, saving and read-back, and the analyst (Grok Build) | [live](https://ancreationoffice.com/drive-setup.txt) |
| [`office-startup.txt`](guide/office-startup.txt) | The four shared skills: start a conversation, save, hand work to another office, and check that setup can write and read back | [live](https://ancreationoffice.com/office-startup.txt) |
| [`github-setup.txt`](guide/github-setup.txt) | Optional add-on for people who write code: private GitHub repository, clones, the analyst, and troubleshooting | [live](https://ancreationoffice.com/github-setup.txt) |
| [`sop-company.txt`](guide/sop-company.txt) | K1. b-business-manager: the company. Name checks, forming an LLC, tax ID, bank account, insurance, licenses, yearly upkeep | [live](https://ancreationoffice.com/sop-company.txt) |
| [`sop-website.txt`](guide/sop-website.txt) | K2. b-business-manager: domain, website, business email, Google Search Console and Bing, the weekly search check | [live](https://ancreationoffice.com/sop-website.txt) |
| [`sop-presence.txt`](guide/sop-presence.txt) | K3. b-business-manager: the brand kit and profiles. Logo, descriptions, fact sheet; LinkedIn, X, Facebook, YouTube and more | [live](https://ancreationoffice.com/sop-presence.txt) |
| [`sop-promotion.txt`](guide/sop-promotion.txt) | K4. b-business-manager: promotion and listings. Where to promote, the approval loop, pace and honesty, the patent check, directories | [live](https://ancreationoffice.com/sop-promotion.txt) |
| [`sop-funding-packet.txt`](guide/sop-funding-packet.txt) | K5. b-business-manager: the funding packet a lender or advisor reads: executive summary, unit economics, use of funds, milestones, risk register | [live](https://ancreationoffice.com/sop-funding-packet.txt) |
| [`sop-business-risks.txt`](guide/sop-business-risks.txt) | K6. b-business-manager: the business risk register | [live](https://ancreationoffice.com/sop-business-risks.txt) |
| [`sop-meeting-prep.txt`](guide/sop-meeting-prep.txt) | K7. b-business-manager: meeting prep. Who is across the table, what they will want to see, the packet and a prep sheet | [live](https://ancreationoffice.com/sop-meeting-prep.txt) |
| [`sop-packet-buyer.txt`](guide/sop-packet-buyer.txt) | K7. b-business-manager: packets: buyer | [live](https://ancreationoffice.com/sop-packet-buyer.txt) |
| [`meeting-packet.py`](guide/meeting-packet.py) | K7. b-business-manager: builder | [live](https://ancreationoffice.com/meeting-packet.py) |
| [`sop-business-record.txt`](guide/sop-business-record.txt) | K8. b-business-manager: the business record, required: company record, decision log, action log, contacts and the correspondence log, trip log, expense ledger (the tax record), deadlines. Insist on hearing about every trip, meeting and cost when it happens. Year end: tax-year.py | [live](https://ancreationoffice.com/sop-business-record.txt) |
| [`sop-project-record.txt`](guide/sop-project-record.txt) | The project record, required for every invention | [live](https://ancreationoffice.com/sop-project-record.txt) |
| [`sop-decision-log.txt`](guide/sop-decision-log.txt) | decision log | [live](https://ancreationoffice.com/sop-decision-log.txt) |
| [`sop-action-log.txt`](guide/sop-action-log.txt) | action log with suggestions | [live](https://ancreationoffice.com/sop-action-log.txt) |
| [`sop-cost-sheet.txt`](guide/sop-cost-sheet.txt) | cost sheet | [live](https://ancreationoffice.com/sop-cost-sheet.txt) |
| [`sop-spending-register.txt`](guide/sop-spending-register.txt) | spending register | [live](https://ancreationoffice.com/sop-spending-register.txt) |
| [`sop-risk-table.txt`](guide/sop-risk-table.txt) | risk table | [live](https://ancreationoffice.com/sop-risk-table.txt) |
| [`sop-change-control.txt`](guide/sop-change-control.txt) | engineering change notices | [live](https://ancreationoffice.com/sop-change-control.txt) |
| [`principles-pm.txt`](guide/principles-pm.txt) | Principles, read first every conversation | [live](https://ancreationoffice.com/principles-pm.txt) |
| [`sop-source-check.txt`](guide/sop-source-check.txt) | The source check, both bots: every spec traces to an actual document, never AI memory, and is checked against it when it goes into a sheet; when no procedure covers something, write the project's procedure from the authoritative source in the library | [live](https://ancreationoffice.com/sop-source-check.txt) |
| [`check-sources.py`](guide/check-sources.py) | The source check, both bots: checker | [live](https://ancreationoffice.com/check-sources.py) |
| [`sop-document-life.txt`](guide/sop-document-life.txt) | Living and parked documents, both bots: which documents are updated every time something happens (action logs, decision logs, spending, trips, expenses, the correspondence index, deadlines) and which are done for a purpose and parked until a trigger (charter, cost sheet, risk table, compliance matrix, packets, company record), and how to dust one off | [live](https://ancreationoffice.com/sop-document-life.txt) |
| [`sop-correspondence.txt`](guide/sop-correspondence.txt) | The correspondence log, both bots, one for the company: a folder per email, file sent (CAD, drawings), meeting or call, named YYMMDD-NN-X-slug (date code, its number in the day, S sent, R received or M meeting or call, a slug) so they stay in order, never changed once filed, with its index correspondence.csv | [live](https://ancreationoffice.com/sop-correspondence.txt) |
| [`playbooks.txt`](guide/playbooks.txt) | Playbooks, b-project-manager: whole jobs strung from the procedures, with the inventor's decisions marked | [live](https://ancreationoffice.com/playbooks.txt) |
| [`playbook-design-to-freeze.txt`](guide/playbook-design-to-freeze.txt) | Playbooks, b-project-manager: the design loop from concept to freeze | [live](https://ancreationoffice.com/playbook-design-to-freeze.txt) |
| [`playbook-first-tooling-quote.txt`](guide/playbook-first-tooling-quote.txt) | Playbooks, b-project-manager: the first tooling quote | [live](https://ancreationoffice.com/playbook-first-tooling-quote.txt) |
| [`sop-schedule.txt`](guide/sop-schedule.txt) | The schedule and the critical path, b-project-manager: the charter's dates, forecasts and slips, and which slips move the end | [live](https://ancreationoffice.com/sop-schedule.txt) |
| [`schedule.py`](guide/schedule.py) | The schedule and the critical path, b-project-manager: checker | [live](https://ancreationoffice.com/schedule.py) |
| [`sop-focus.txt`](guide/sop-focus.txt) | Keep the project focused: risks as questions, decisions, "for now" and circling back | [live](https://ancreationoffice.com/sop-focus.txt) |
| [`ticket-template.txt`](guide/ticket-template.txt) | The ticket format b-project-manager runs | [live](https://ancreationoffice.com/ticket-template.txt) |
| [`agents-md.txt`](guide/agents-md.txt) | AGENTS.md for the inventor's repository: how any AI finds its ticket from one line | [live](https://ancreationoffice.com/agents-md.txt) |
| [`intake-001.csv`](guide/intake-001.csv) | The first form, always: the invention and the screening questions | [live](https://ancreationoffice.com/intake-001.csv) |
| [`screening-questions.csv`](guide/screening-questions.csv) | Screening: 26 questions that narrow the standards to the few that matter | [live](https://ancreationoffice.com/screening-questions.csv) |
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
| [`template-apqp-file.csv`](guide/template-apqp-file.csv) | Templates b-analyst fills: APQP file | [live](https://ancreationoffice.com/template-apqp-file.csv) |
| [`template-review-record.txt`](guide/template-review-record.txt) | Templates b-analyst fills: review record | [live](https://ancreationoffice.com/template-review-record.txt) |
| [`template-prototype-control-plan.txt`](guide/template-prototype-control-plan.txt) | Templates b-analyst fills: prototype control plan | [live](https://ancreationoffice.com/template-prototype-control-plan.txt) |
| [`template-trial-log.txt`](guide/template-trial-log.txt) | Templates b-analyst fills: trial log | [live](https://ancreationoffice.com/template-trial-log.txt) |
| [`template-fai-report.csv`](guide/template-fai-report.csv) | Templates b-analyst fills: first article report | [live](https://ancreationoffice.com/template-fai-report.csv) |
| [`template-change-record.txt`](guide/template-change-record.txt) | Templates b-analyst fills: change record | [live](https://ancreationoffice.com/template-change-record.txt) |
| [`sop-quality.txt`](guide/sop-quality.txt) | The quality chain | [live](https://ancreationoffice.com/sop-quality.txt) |
| [`sop-checklists.txt`](guide/sop-checklists.txt) | Fill a form from what is already known | [live](https://ancreationoffice.com/sop-checklists.txt) |
| [`sop-routes.txt`](guide/sop-routes.txt) | Roads in detail: patent, funding, company, standards, power, stores | [live](https://ancreationoffice.com/sop-routes.txt) |
| [`analyst-after-intake.txt`](guide/analyst-after-intake.txt) | Prepared prompts: after intake | [live](https://ancreationoffice.com/analyst-after-intake.txt) |
| [`analyst-refill.txt`](guide/analyst-refill.txt) | Prepared prompts: refill the queue | [live](https://ancreationoffice.com/analyst-refill.txt) |
| [`forms-catalog.csv`](guide/forms-catalog.csv) | Formal forms and documents each road produces | [live](https://ancreationoffice.com/forms-catalog.csv) |
| [`project-folders.txt`](guide/project-folders.txt) | The project folders: Your files and Office files. Dated folders; records are never edited once saved | [live](https://ancreationoffice.com/project-folders.txt) |
| [`sop-review-page.txt`](guide/sop-review-page.txt) | Review pages: a local web page per invention for timelines, risks, pictures, documents and short walkthroughs | [live](https://ancreationoffice.com/sop-review-page.txt) |
| [`terms.txt`](guide/terms.txt) | Terms: the plain-language glossary to explain terms from (about 200, with read-more links) | [live](https://ancreationoffice.com/terms.txt) |

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
| [`compliance-matrix-template.csv`](guide/compliance-matrix-template.csv) | Worksheet / table (CSV): ID, Source, Edition or date, Clause or page... | [live](https://ancreationoffice.com/compliance-matrix-template.csv) |
| [`control-plan.csv`](guide/control-plan.csv) | Worksheet / table (CSV): Control ID, Plan phase (prototype/prelaunch/production), Product and drawing revision, Process flow revision and step... | [live](https://ancreationoffice.com/control-plan.csv) |
| [`critical-quality.csv`](guide/critical-quality.csv) | Worksheet / table (CSV): CTQ ID, Original concern or customer need, Raised by and source, Source revision or date... | [live](https://ancreationoffice.com/critical-quality.csv) |
| [`design-principles-review.csv`](guide/design-principles-review.csv) | Worksheet / table (CSV): Project, Concept / exact revision, Area ID, Review area... | [live](https://ancreationoffice.com/design-principles-review.csv) |
| [`design-principles.json`](guide/design-principles.json) | Data behind the design principles page (JSON) | [live](https://ancreationoffice.com/design-principles.json) |
| [`design-principles.txt`](guide/design-principles.txt) | DESIGN PRINCIPLES: PEOPLE, FORM AND USE | [live](https://ancreationoffice.com/design-principles.txt) |
| [`design-review.txt`](guide/design-review.txt) | AN CREATION — SHORT DESIGN AND FAILURE REVIEW — TEMPLATE REV 1 | [live](https://ancreationoffice.com/design-review.txt) |
| [`design-risk.txt`](guide/design-risk.txt) | AN Creation — Design risk and troubleshooting. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/design-risk.txt) |
| [`funding-packet.py`](guide/funding-packet.py) | Tool / template script (Python) | [live](https://ancreationoffice.com/funding-packet.py) |
| [`handoff-log.csv`](guide/handoff-log.csv) | Worksheet / table (CSV): handoff_id, sent_date, sender, recipient... | [live](https://ancreationoffice.com/handoff-log.csv) |
| [`ip-ratings.txt`](guide/ip-ratings.txt) | IP enclosure ratings. Basic orientation only; use IEC 60529 and the actual test evidence for requirements and  | [live](https://ancreationoffice.com/ip-ratings.txt) |
| [`library.txt`](guide/library.txt) | 261018.35 | [live](https://ancreationoffice.com/library.txt) |
| [`manufacturing.txt`](guide/manufacturing.txt) | Manufacturing role. Reference for b-project-manager when the manufacturing role is the one in front of it. The | [live](https://ancreationoffice.com/manufacturing.txt) |
| [`office-handoff.txt`](guide/office-handoff.txt) | AN Creation skill: office-handoff. The office rule is https://ancreationoffice.com/sop-team.txt HAND-OFFS. | [live](https://ancreationoffice.com/office-handoff.txt) |
| [`office-save.txt`](guide/office-save.txt) | AN Creation skill: office-save. The office rule is https://ancreationoffice.com/version-control.txt SAVING and | [live](https://ancreationoffice.com/office-save.txt) |
| [`office-setup-check.txt`](guide/office-setup-check.txt) | AN Creation skill: office-setup-check. Run once after setup (https://ancreationoffice.com/drive-setup.txt), an | [live](https://ancreationoffice.com/office-setup-check.txt) |
| [`office-version-history.txt`](guide/office-version-history.txt) | AN Creation office version history, retired from the startup file on October 14, 2026. | [live](https://ancreationoffice.com/office-version-history.txt) |
| [`plan-template.txt`](guide/plan-template.txt) | Project plan | [live](https://ancreationoffice.com/plan-template.txt) |
| [`planning-resources.json`](guide/planning-resources.json) | Data behind the planning resources page (JSON) | [live](https://ancreationoffice.com/planning-resources.json) |
| [`planning-resources.txt`](guide/planning-resources.txt) | Product, startup and project planning. Checked 2026-09-30. | [live](https://ancreationoffice.com/planning-resources.txt) |
| [`planning-review.csv`](guide/planning-review.csv) | Worksheet / table (CSV): Item ID, Question, Suggested roles, Source IDs... | [live](https://ancreationoffice.com/planning-review.csv) |
| [`principle-always-a-next-step.txt`](guide/principle-always-a-next-step.txt) | Principle: Always a next step. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-always-a-next-step.txt) |
| [`principle-audience-before-launch.txt`](guide/principle-audience-before-launch.txt) | Principle: Build the audience before launch. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-audience-before-launch.txt) |
| [`principle-believe-reality.txt`](guide/principle-believe-reality.txt) | Principle: Believe reality over the plan. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-believe-reality.txt) |
| [`principle-build-to-learn.txt`](guide/principle-build-to-learn.txt) | Principle: Build to learn. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-build-to-learn.txt) |
| [`principle-cash-is-oxygen.txt`](guide/principle-cash-is-oxygen.txt) | Principle: Cash is oxygen. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-cash-is-oxygen.txt) |
| [`principle-cheapest-real-signal.txt`](guide/principle-cheapest-real-signal.txt) | Principle: Get the cheapest real signal. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-cheapest-real-signal.txt) |
| [`principle-context-window.txt`](guide/principle-context-window.txt) | Principle: Guard the context window. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/principle-context-window.txt) |
| [`principle-design-for-manufacture.txt`](guide/principle-design-for-manufacture.txt) | Principle: Design for manufacture from day one. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-design-for-manufacture.txt) |
| [`principle-fail-forward-faster.txt`](guide/principle-fail-forward-faster.txt) | Principle: Fail forward faster. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-fail-forward-faster.txt) |
| [`principle-find-surprises-early.txt`](guide/principle-find-surprises-early.txt) | Principle: Find the expensive surprises early. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-find-surprises-early.txt) |
| [`principle-know-what-good-is.txt`](guide/principle-know-what-good-is.txt) | Principle: Know what good is before designing. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-know-what-good-is.txt) |
| [`principle-money-fits-the-stage.txt`](guide/principle-money-fits-the-stage.txt) | Principle: Fit the money to the stage. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-money-fits-the-stage.txt) |
| [`principle-never-invent-facts.txt`](guide/principle-never-invent-facts.txt) | Principle: Never invent facts. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-never-invent-facts.txt) |
| [`principle-ninety-percent-and-go.txt`](guide/principle-ninety-percent-and-go.txt) | Principle: 90% and go. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-ninety-percent-and-go.txt) |
| [`principle-no-claims-you-cant-back.txt`](guide/principle-no-claims-you-cant-back.txt) | Principle: No claims you can't back. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-no-claims-you-cant-back.txt) |
| [`principle-one-change-at-a-time.txt`](guide/principle-one-change-at-a-time.txt) | Principle: One change at a time, to the root cause. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-one-change-at-a-time.txt) |
| [`principle-one-controlled-copy.txt`](guide/principle-one-controlled-copy.txt) | Principle: One controlled copy. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-one-controlled-copy.txt) |
| [`principle-one-customer-one-channel.txt`](guide/principle-one-customer-one-channel.txt) | Principle: One customer, one channel first. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-one-customer-one-channel.txt) |
| [`principle-owner-acts-bot-drafts.txt`](guide/principle-owner-acts-bot-drafts.txt) | Principle: The owner acts; the bot drafts. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-owner-acts-bot-drafts.txt) |
| [`principle-patent-before-public.txt`](guide/principle-patent-before-public.txt) | Principle: Decide on the patent before showing it publicly. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-patent-before-public.txt) |
| [`principle-price-on-value.txt`](guide/principle-price-on-value.txt) | Principle: Price on value, never below cost. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-price-on-value.txt) |
| [`principle-proof-over-estimate.txt`](guide/principle-proof-over-estimate.txt) | Principle: Proof over estimate. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-proof-over-estimate.txt) |
| [`principle-propose-a-default.txt`](guide/principle-propose-a-default.txt) | Principle: Propose a default. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-propose-a-default.txt) |
| [`principle-re-anchor.txt`](guide/principle-re-anchor.txt) | Principle: Re-anchor. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/principle-re-anchor.txt) |
| [`principle-residual-risk.txt`](guide/principle-residual-risk.txt) | Principle: Residual risk: work the 80%. Revision 9 — October 18, 2026. | [live](https://ancreationoffice.com/principle-residual-risk.txt) |
| [`principle-rigor-scales-with-money.txt`](guide/principle-rigor-scales-with-money.txt) | Principle: Rigor scales with whose money is at risk. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/principle-rigor-scales-with-money.txt) |
| [`principle-scope-gate.txt`](guide/principle-scope-gate.txt) | Principle: Scope gate. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/principle-scope-gate.txt) |
| [`principle-severity-first.txt`](guide/principle-severity-first.txt) | Principle: Severity first. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-severity-first.txt) |
| [`principle-start-with-what-you-have.txt`](guide/principle-start-with-what-you-have.txt) | Principle: Start with what you have. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-start-with-what-you-have.txt) |
| [`principle-trace-to-source.txt`](guide/principle-trace-to-source.txt) | Principle: Trace every spec to its source. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-trace-to-source.txt) |
| [`principle-two-way-doors.txt`](guide/principle-two-way-doors.txt) | Principle: Two-way doors go fast. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-two-way-doors.txt) |
| [`principle-unit-economics-first.txt`](guide/principle-unit-economics-first.txt) | Principle: Know the unit economics before tooling. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-unit-economics-first.txt) |
| [`principle-walk-away-number.txt`](guide/principle-walk-away-number.txt) | Principle: Know your walk-away number. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-walk-away-number.txt) |
| [`principle-watch-the-calendar.txt`](guide/principle-watch-the-calendar.txt) | Principle: Watch the calendar. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-watch-the-calendar.txt) |
| [`principle-which-gives.txt`](guide/principle-which-gives.txt) | Principle: When something has to give, ask which. Revision 1 — October 18, 2026. | [live](https://ancreationoffice.com/principle-which-gives.txt) |
| [`principles-bm.txt`](guide/principles-bm.txt) | Principles: the Office Manager Bot. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/principles-bm.txt) |
| [`product-development.txt`](guide/product-development.txt) | PRODUCT DEVELOPMENT: THE PROCESS BEHIND THE CONVERSATION | [live](https://ancreationoffice.com/product-development.txt) |
| [`profile.txt`](guide/profile.txt) | AN Creation bot profiles (October 18, 2026). b-project-manager profile version 6. b-business-manager profile v | [live](https://ancreationoffice.com/profile.txt) |
| [`project-manager.txt`](guide/project-manager.txt) | b-project-manager: the project manager role for AN Creation. The inventor names the bot that covers it (https: | [live](https://ancreationoffice.com/project-manager.txt) |
| [`record-view.py`](guide/record-view.py) | Tool / template script (Python) | [live](https://ancreationoffice.com/record-view.py) |
| [`resource-crosscheck.json`](guide/resource-crosscheck.json) | Data behind the resource crosscheck page (JSON) | [live](https://ancreationoffice.com/resource-crosscheck.json) |
| [`resource-crosscheck.txt`](guide/resource-crosscheck.txt) | Resource cross-check, September 30, 2026. | [live](https://ancreationoffice.com/resource-crosscheck.txt) |
| [`resources.json`](guide/resources.json) | Data behind the resources page (JSON) | [live](https://ancreationoffice.com/resources.json) |
| [`resources.txt`](guide/resources.txt) | Resource use for b-project-manager. Same entries as the human shelves linked from https://ancreationoffice.com | [live](https://ancreationoffice.com/resources.txt) |
| [`review.py`](guide/review.py) | Tool: builds the inventor's local review pages | [live](https://ancreationoffice.com/review.py) |
| [`revision-log.csv`](guide/revision-log.csv) | Worksheet / table (CSV): item_id, title, revision, previous_revision... | [live](https://ancreationoffice.com/revision-log.csv) |
| [`revisions.txt`](guide/revisions.txt) | AN Creation revision control. Human lesson: https://ancreationoffice.com/revisions.html | [live](https://ancreationoffice.com/revisions.txt) |
| [`robots.txt`](guide/robots.txt) | User-agent: * | [live](https://ancreationoffice.com/robots.txt) |
| [`sop-hats.txt`](guide/sop-hats.txt) | SOP: Form, record, and call a session. Revision 3 — October 1, 2026. | [live](https://ancreationoffice.com/sop-hats.txt) |
| [`sop-interns.txt`](guide/sop-interns.txt) | SOP: Use an intern. Revision 1 — October 1, 2026. | [live](https://ancreationoffice.com/sop-interns.txt) |
| [`sop-office.txt`](guide/sop-office.txt) | SOP: Set up b-project-manager and b-analyst. Revision 16 — October 18, 2026. | [live](https://ancreationoffice.com/sop-office.txt) |
| [`sop-packet-accountant.txt`](guide/sop-packet-accountant.txt) | SOP: The accountant packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-accountant.txt) |
| [`sop-packet-attorney.txt`](guide/sop-packet-attorney.txt) | SOP: The business attorney packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-attorney.txt) |
| [`sop-packet-insurance.txt`](guide/sop-packet-insurance.txt) | SOP: The insurance packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-insurance.txt) |
| [`sop-packet-investor.txt`](guide/sop-packet-investor.txt) | SOP: The investor packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-investor.txt) |
| [`sop-packet-lender.txt`](guide/sop-packet-lender.txt) | SOP: The lender packet. Revision 4 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-lender.txt) |
| [`sop-packet-licensee.txt`](guide/sop-packet-licensee.txt) | SOP: The licensee packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-licensee.txt) |
| [`sop-packet-manufacturer.txt`](guide/sop-packet-manufacturer.txt) | SOP: The manufacturer packet (request for quote). Revision 4 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-manufacturer.txt) |
| [`sop-packet-partner.txt`](guide/sop-packet-partner.txt) | SOP: The partner packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-partner.txt) |
| [`sop-packet-patent.txt`](guide/sop-packet-patent.txt) | SOP: The patent attorney packet. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-packet-patent.txt) |
| [`sop-project-charter.txt`](guide/sop-project-charter.txt) | SOP: The project charter. Revision 2 — October 18, 2026. | [live](https://ancreationoffice.com/sop-project-charter.txt) |
| [`sop-suggestions.txt`](guide/sop-suggestions.txt) | SOP: Suggestions and actions. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/sop-suggestions.txt) |
| [`sop.txt`](guide/sop.txt) | AN Creation standard operating procedures. Revision 28 — October 18, 2026. | [live](https://ancreationoffice.com/sop.txt) |
| [`sops-manifest.txt`](guide/sops-manifest.txt) | 261018.35 | [live](https://ancreationoffice.com/sops-manifest.txt) |
| [`status-template.txt`](guide/status-template.txt) | STATUS SHEET: one page, answers only. Rewritten by b-analyst every run as "Your files/Status" (inventor's form | [live](https://ancreationoffice.com/status-template.txt) |
| [`tax-year.py`](guide/tax-year.py) | Tool / template script (Python) | [live](https://ancreationoffice.com/tax-year.py) |
| [`template-a3.txt`](guide/template-a3.txt) | One-page project summary (A3). Template, from Mike's practice (sop-six-sigma.txt section 6). Copy into the pro | [live](https://ancreationoffice.com/template-a3.txt) |
| [`template-action-log.csv`](guide/template-action-log.csv) | Worksheet / table (CSV): ID, Opened, Action, Who... | [live](https://ancreationoffice.com/template-action-log.csv) |
| [`template-business-decision-log.csv`](guide/template-business-decision-log.csv) | Worksheet / table (CSV): date, decision, reason, status... | [live](https://ancreationoffice.com/template-business-decision-log.csv) |
| [`template-business-risks.csv`](guide/template-business-risks.csv) | Worksheet / table (CSV): id, risk, category, likelihood... | [live](https://ancreationoffice.com/template-business-risks.csv) |
| [`template-cash-flow.csv`](guide/template-cash-flow.csv) | Worksheet / table (CSV): month, owner in, loan in, units sold... | [live](https://ancreationoffice.com/template-cash-flow.csv) |
| [`template-company.csv`](guide/template-company.csv) | Worksheet / table (CSV): key, value, status, note... | [live](https://ancreationoffice.com/template-company.csv) |
| [`template-contacts.csv`](guide/template-contacts.csv) | Worksheet / table (CSV): name, organization, type, status... | [live](https://ancreationoffice.com/template-contacts.csv) |
| [`template-correspondence.csv`](guide/template-correspondence.csv) | Worksheet / table (CSV): date, folder, direction, with... | [live](https://ancreationoffice.com/template-correspondence.csv) |
| [`template-cost-sheet.csv`](guide/template-cost-sheet.csv) | Worksheet / table (CSV): level, part number, part, qty... | [live](https://ancreationoffice.com/template-cost-sheet.csv) |
| [`template-deadlines.csv`](guide/template-deadlines.csv) | Worksheet / table (CSV): due, what, why it matters, Source... | [live](https://ancreationoffice.com/template-deadlines.csv) |
| [`template-decision-log.csv`](guide/template-decision-log.csv) | Worksheet / table (CSV): date, decision, reason... | [live](https://ancreationoffice.com/template-decision-log.csv) |
| [`template-disclosure-history.csv`](guide/template-disclosure-history.csv) | Worksheet / table (CSV): date, to whom, what was shown, revision... | [live](https://ancreationoffice.com/template-disclosure-history.csv) |
| [`template-ecn-log.csv`](guide/template-ecn-log.csv) | Worksheet / table (CSV): number, date, what changes, why... | [live](https://ancreationoffice.com/template-ecn-log.csv) |
| [`template-expenses.csv`](guide/template-expenses.csv) | Worksheet / table (CSV): date, paid to, what it was, business purpose... | [live](https://ancreationoffice.com/template-expenses.csv) |
| [`template-funding.csv`](guide/template-funding.csv) | Worksheet / table (CSV): key, value, source, note... | [live](https://ancreationoffice.com/template-funding.csv) |
| [`template-invention-disclosure.csv`](guide/template-invention-disclosure.csv) | Worksheet / table (CSV): key, value, note... | [live](https://ancreationoffice.com/template-invention-disclosure.csv) |
| [`template-market-evidence.csv`](guide/template-market-evidence.csv) | Worksheet / table (CSV): date, who, what they saw, what they said... | [live](https://ancreationoffice.com/template-market-evidence.csv) |
| [`template-meeting.csv`](guide/template-meeting.csv) | Worksheet / table (CSV): key, value, note... | [live](https://ancreationoffice.com/template-meeting.csv) |
| [`template-pricing-terms.csv`](guide/template-pricing-terms.csv) | Worksheet / table (CSV): key, value, source, note... | [live](https://ancreationoffice.com/template-pricing-terms.csv) |
| [`template-prior-art.csv`](guide/template-prior-art.csv) | Worksheet / table (CSV): ref, title, date, owner or assignee... | [live](https://ancreationoffice.com/template-prior-art.csv) |
| [`template-project-charter.txt`](guide/template-project-charter.txt) | Project charter. Template. Office files/project-charter.txt. Replace every line in brackets; delete what does  | [live](https://ancreationoffice.com/template-project-charter.txt) |
| [`template-quote-comparison.csv`](guide/template-quote-comparison.csv) | Worksheet / table (CSV): supplier, quote ref, quote date, valid until... | [live](https://ancreationoffice.com/template-quote-comparison.csv) |
| [`template-risk-table.csv`](guide/template-risk-table.csv) | Worksheet / table (CSV): id, Failure mode / actions, effect, S... | [live](https://ancreationoffice.com/template-risk-table.csv) |
| [`template-schedule.csv`](guide/template-schedule.csv) | Worksheet / table (CSV): id, milestone, depends on, days after... | [live](https://ancreationoffice.com/template-schedule.csv) |
| [`template-spending-register.csv`](guide/template-spending-register.csv) | Worksheet / table (CSV): date, stage, what it was, category... | [live](https://ancreationoffice.com/template-spending-register.csv) |
| [`template-team.csv`](guide/template-team.csv) | Worksheet / table (CSV): name, covers, bot_id, business... | [live](https://ancreationoffice.com/template-team.csv) |
| [`template-trips.csv`](guide/template-trips.csv) | Worksheet / table (CSV): trip, date, from, to (place and address)... | [live](https://ancreationoffice.com/template-trips.csv) |
| [`test-matrix.csv`](guide/test-matrix.csv) | Worksheet / table (CSV): Project, Plan ID / revision, Test ID, Requirement / CTQ / risk IDs... | [live](https://ancreationoffice.com/test-matrix.csv) |
| [`test-plan-template.txt`](guide/test-plan-template.txt) | AN CREATION — TEST PLAN TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-plan-template.txt) |
| [`test-planning.json`](guide/test-planning.json) | Data behind the test planning page (JSON) | [live](https://ancreationoffice.com/test-planning.json) |
| [`test-planning.txt`](guide/test-planning.txt) | Plan the test before the build — REV 1 — 2026-09-30 | [live](https://ancreationoffice.com/test-planning.txt) |
| [`test-report-template.txt`](guide/test-report-template.txt) | AN CREATION — TEST REPORT TEMPLATE — REV 1 | [live](https://ancreationoffice.com/test-report-template.txt) |
| [`using-other-ais.txt`](guide/using-other-ais.txt) | AN Creation: using Claude, ChatGPT (Codex), Cursor, or another AI. Revision 3 — October 18, 2026. | [live](https://ancreationoffice.com/using-other-ais.txt) |
| [`version-control.txt`](guide/version-control.txt) | AN Creation backups and version control. Revision 10 — October 18, 2026. Human page: https://ancreationoffice. | [live](https://ancreationoffice.com/version-control.txt) |

## The specialists

The [`specialists/`](specialists/) folder (kept in this repository, not synced) holds the roster, the role map ([`specialists/roles.csv`](specialists/roles.csv)), the calculations the analyst runs ([`specialists/calcs/`](specialists/calcs/)). [`specialists/tools/build_offices.py`](specialists/tools/build_offices.py) built the six office pages and is retired: the site has two bots now, and its start page is written by hand. The next sync overwrites `guide/` from creation-office `site/create/`, so a file written only into `guide/` does not last.


## License

© 2026 Advance Now LLC. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (full text: [LICENSE](LICENSE); explained in plain words at [https://ancreationoffice.com/license.html](https://ancreationoffice.com/license.html)).

**Using AN Creation for your own inventions is free and always welcome, even if you sell the product. What's not allowed is selling these procedures, or a paid program or service built on them.** Share it and adapt it freely; credit Advance Now LLC with a link to the website, and keep anything you build from it under the same license.

## How this copy is kept

Synced from the live site by a script after each publish. If this copy and https://ancreationoffice.com/ ever differ, the live site is current.

*Last synced October 18, 2026.*
