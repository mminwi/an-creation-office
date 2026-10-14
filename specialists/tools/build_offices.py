"""Builds the AN Creation offices from specialists/roles.csv (run after any roster or office change).
Run from this repository's root, pointing at a creation-office checkout:
  python specialists/tools/build_offices.py --site ../creation-office/site/create
Writes into that site/create/ folder (the source of truth). sync-public-repo.py then copies it into guide/ here;
anything written only into guide/ is overwritten by the next sync. --site defaults to $CREATION_SITE, then
../creation-office/site/create. Review the diff in creation-office before committing: the generated office pages
and office-*.txt replace hand edits made there since the last build.
Writes:
  welcome.html                      the site's front page: pick an office
  sop.html                          every procedure, by office (counts generated)
  offices.html                      the overview of the six offices
  <office page>.html                one page per office: what's inside, how to start it, the paste message
  office-<id>.txt                   standing instructions for the four specialty offices
                                    (the Inventor's Office reads standing.txt; the Business Manager's Office reads business-manager.txt)
  specialists/tools/sidebar.html    the "Your offices" sidebar block, for pasting into the other site pages
Each office is one bot. The owner names it; the procedures call it by its role name."""
import argparse, csv, html, json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
_ap = argparse.ArgumentParser(description='Build the AN Creation office pages into creation-office site/create/.')
_ap.add_argument('--site', default=os.environ.get('CREATION_SITE') or str(ROOT.parent / 'creation-office' / 'site' / 'create'),
                 help='path to creation-office site/create (default: $CREATION_SITE or ../creation-office/site/create)')
GUIDE = pathlib.Path(_ap.parse_args().site).resolve()   # output folder (name kept for the code below)
if not (GUIDE / 'version.txt').is_file():
    sys.exit(f'{GUIDE} is not a creation-office site/create folder (no version.txt). Pass --site.')
SITE = 'https://ancreationoffice.com/'
GH = 'https://github.com/mminwi/an-creation-office/blob/main/'
rows = {r['role']: r for r in csv.DictReader(open(ROOT / 'specialists/roles.csv', encoding='utf-8'))}
LIB = {r['id']: r for r in json.load(open(GUIDE / 'resources.json', encoding='utf-8'))['resources']}
shell = (ROOT / 'specialists/tools/office-shell.template.html').read_text(encoding='utf-8')
e = lambda s: html.escape(s, quote=False)

OFFICES = [
    dict(id='inventor', covers=['Planning the project and keeping it on track', "Whether people want it, and what they'd pay", 'Design', 'Prototypes', 'Making it easier and cheaper to build', 'Product safety and listings'], page='inventors-office.html', jobs=['Tell it your idea in a few sentences and see what it asks', 'Find out what your product will have to meet: safety rules, standards, a patent search', 'Plan your first prototype'], result="A short summary of your idea: what's known, what isn't yet, and the next useful question or experiment.", name="Inventor's Office", role='b-project-manager',
         standing='standing.txt', folder='(one folder per invention)', face='andy',
         icon='<circle cx="12" cy="12" r="9"/><path d="M14.8 8.2 13.2 13.2 8.2 14.8 9.8 9.8z" fill="currentColor" stroke="none"/>',
         short='Your idea, from first talk to prototype',
         who='For anyone with an idea for a product.',
         blurb="Your project manager for every invention. It takes an idea from the first conversation through design, prototypes, tooling, testing and launch, keeps the paperwork, and tells you what's next.",
         members=['b-project-manager', 'b-market-check', 'b-design', 'b-prototyping', 'b-dfm', 'b-product-safety'],
         first=True, then='Then ask me to tell you about my invention.'),
    dict(id='business', covers=['The company', 'Patent preparation', 'A name and trademark', 'Licensing', 'Funding', 'Your website and promotion', 'Getting into stores'], page='business-office.html', jobs=['Decide whether, and when, to form a company', 'Get ready for a first talk with a patent attorney', 'Plan the money for your next step'], result='A short list of the business decisions in front of you, and a draft packet for the first one.', name="Business Manager's Office", role='b-business-manager',
         standing='business-manager.txt', folder='AN-Creation/Business', face='larry',
         icon='<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
         short='Company, patent, money, selling',
         who='For the business side of having a product.',
         blurb='The business around your products: the company, patent preparation, a name and trademark, licensing, funding, your website, promotion, and getting into stores.',
         members=['b-business-manager', 'b-company-setup', 'b-patent-prep', 'b-trademark', 'b-licensing', 'b-funding', 'b-promotion', 'b-retail'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='molding', covers=['Setting up a solid molding process', 'Molding defects', 'Mold and machine cooling water', 'Drying and regrind', 'Buying a mold', 'Plastic materials', 'Machine safety'], page='molding-office.html', jobs=['Work through a molding defect: short shots, sink, flash, splay', 'Check a cooling water or drying problem', 'Get ready to buy a mold'], result='An investigation record: the readings you gave it, the likely causes, and the next checks to run at the press.', name='Molding Plant Office', role='b-molding-office',
         standing='office-molding.txt', folder='AN-Creation/Molding Plant', face='peter',
         icon='<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9h10M7 13h6"/>',
         short='Molding, cooling, drying, molds',
         who='For molders and anyone running injection molding.',
         blurb="Built from Mike Maier's years running molding plants: cooling water, drying and regrind, scientific molding, molding defects, buying molds, materials and machine safety.",
         members=['b-scientific-molding', 'b-molding-defects', 'b-cooling-water', 'b-drying-handling', 'b-mold-buying', 'b-plastic-materials', 'b-machine-safety'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='plastic', covers=['Plastic part design', 'Tolerances: will the parts fit together', 'Choosing the plastic', 'Designing for molding', 'Prototypes', 'Buying a mold', 'Getting AI agents to do the CAD work'], page='plastic-design-office.html', jobs=['Review a part for molding: walls, draft, ribs, gates', 'Check whether parts will fit together (a tolerance stack)', 'Choose a plastic for the job'], result='A design-for-molding review tied to your drawing revision, with open questions for the molder.', name='Plastic Design Office', role='b-plastic-design-office',
         standing='office-plastic-design.txt', folder='AN-Creation/Plastic Design', face='morgan',
         icon='<path d="M4 18 12 4l8 14z"/><path d="M8 18h8"/>',
         short='Plastic parts that mold well',
         who='For anyone designing plastic parts.',
         blurb='Plastic parts that mold well: part design, tolerance stacks, material choice, design for molding, prototypes and the mold.',
         members=['b-plastic-part-design', 'b-tolerance-gdt', 'b-plastic-materials', 'b-dfm', 'b-prototyping', 'b-mold-buying', 'b-ai-cad'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='quality', covers=['Quality planning', 'Measurement and inspection', 'Lean Six Sigma and improvement'], page='quality-office.html', jobs=['Draft a control plan from your requirements', 'Make sense of measurement or scrap data', 'Outline a corrective action'], result='A draft quality record, linked to the evidence you gave it, for your team to review.', name='Quality Office', role='b-quality-office',
         standing='office-quality.txt', folder='AN-Creation/Quality', face='maya',
         icon='<path d="M5 12l4 4 10-10"/>',
         short='APQP, measurement, Six Sigma',
         who='For quality planning and improvement work.',
         blurb='Quality planning (APQP, FMEA, control plans), measurement and inspection, and Lean Six Sigma with the improvement toolbox.',
         members=['b-quality-planning', 'b-measurement', 'b-six-sigma'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='manufacturing', covers=['Manufacturing cells and standard work', 'Purchasing', 'Cost and the parts list', 'Automation', 'Machine safety', 'Lean Six Sigma and improvement'], page='manufacturing-office.html', jobs=['Compare supplier quotes like for like', 'Draft standard work for a cell', 'Plan a bottleneck investigation'], result='A side-by-side quote comparison, a standard-work draft or an investigation plan.', name='Manufacturing Office', role='b-manufacturing-office',
         standing='office-manufacturing.txt', folder='AN-Creation/Manufacturing', face='frankie',
         icon='<path d="M3 20V10l6 4V10l6 4V6l6 4v10z"/>',
         short='Cells, purchasing, cost, automation',
         who='For setting up and running production.',
         blurb='Manufacturing cells and standard work, purchasing, cost and the bill of materials, automation, machine safety and Lean Six Sigma.',
         members=['b-manufacturing', 'b-purchasing', 'b-cost-bom', 'b-automation', 'b-machine-safety', 'b-six-sigma'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='mil-battery', listed=False, own_project=True,
         repo='private GitHub repository for this project (ask the owner its name the first time; it is not an-creation)',
         covers=['Program management under AS9100', 'Export control: what may and may not be kept here', 'Military environmental testing (MIL-STD-810)', 'EMI/EMC (MIL-STD-461)', 'Sealed, shielded enclosure: gaskets, stack-up, finishes', 'Lithium-ion charging and battery-powered electronics', 'Soldier power and radio interfaces', 'Military electronics build quality'],
         page='mil-battery-office.html', jobs=['Lay out the qualification test plan and sequence', 'Walk the power design through the charging question list', 'Check the gasket compression stack-up'],
         result='A program plan, test matrix and question list the team can work from, with controlled data kept where it belongs.',
         name='MIL Battery Office', role='b-mil-battery',
         standing='office-mil-battery.txt', folder='AN-Creation/MIL Battery', face='peter',
         icon='<rect x="3" y="7" width="16" height="10" rx="2"/><path d="M21 10v4M7 10v4M11 10v4"/>',
         short='Soldier-worn power, MIL testing',
         who='For a soldier-worn battery power device on a defense program.',
         blurb='Project manager for a soldier-worn battery power device: AS9100 program management, MIL-STD-810 and MIL-STD-461 testing, sealed and shielded enclosures, and lithium-ion charging, with export-controlled data kept out.',
         members=['b-mil-program', 'b-mil-power', 'b-mil-emi', 'b-mil-environmental', 'b-mil-enclosure', 'b-tolerance-gdt', 'b-mil-electronics-build', 'b-quality-planning', 'b-measurement', 'b-purchasing', 'b-cost-bom', 'b-prototyping'],
         extra='''EXPORT CONTROL (first, always)
This project's technical data is ITAR-controlled. Project information generally is not. You run the project here: schedule, actions, decisions in plain words, test planning, suppliers, quality records, and the questions to ask. Never store or repeat controlled technical data (schematics, layouts, drawings, models, interface control documents, controlled test data, firmware); record only that it exists, its number and revision, and where it lives in the company's controlled system. Design analysis happens in the company's controlled environment, not here. If something pasted looks controlled, say so in one line and don't save it. Full rule: https://ancreationoffice.com/sop-mil-program.txt (EXPORT CONTROL FIRST).

YOUR JOB ON THIS PROJECT
You are the project manager. You keep the plan and you are the one asking "have we considered this? have we looked at that?" across power, EMI, environmental testing, the enclosure and the build, using your specialists' question lists. Answers come from the engineers, the labs and the contract; you track them to closure. The contract's editions of standards govern over the newest ones. Never use the customer's or the end program's name in the repository; use the project's own code name.''',
         first=False, then='Then ask what I want to work on.'),
    dict(id='automation-machine', listed=False, own_project=True,
         repo='private GitHub repository for this project (ask the owner its name the first time; it is not an-creation)',
         covers=['Machine project management: specification to buy-off', 'Proof of concept, build, first power-up, debug and run-off', 'PLC state machines, servo indexing and the control panel', 'Machine vision inspection and good/bad sorting', 'Air feeding, nests and the index wheel', 'Adhesive dispensing and cure', 'Machine safety', 'FAT, SAT, and validation when the product is regulated'],
         page='automation-machine-office.html', jobs=['Turn the requirements into a specification and acceptance criteria', 'Plan the proof-of-concept tests for feeding, vision and dispensing', 'Lay out the FAT and endurance run'],
         result='A specification, risk list, build and test plan the team can work from, with every open question owned.',
         name='Automation Machine Office', role='b-automation-machine',
         standing='office-automation-machine.txt', folder='AN-Creation/Automation Machine', face='frankie',
         icon='<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2"/><path d="M12 4v4M12 16v4M4 12h4M16 12h4"/>',
         short='Plant-floor automation machine',
         who='For building a custom automation machine for the plant floor.',
         blurb='Project manager for a custom plant-floor automation machine: part feeding, an indexing wheel, vision inspection, dispensing, PLC and servo controls, safety, and the build, prove-out and buy-off.',
         members=['b-automation-project', 'b-automation-controls', 'b-machine-vision', 'b-automation-handling', 'b-machine-safety', 'b-automation', 'b-measurement', 'b-six-sigma', 'b-purchasing', 'b-cost-bom', 'b-prototyping', 'b-ai-cad'],
         extra='''CONFIDENTIALITY (first, always)
This is the owner's work project. In the repository use the project's code name; never the customer's name, the product's brand, prices, or the customer's drawings and specifications. Keep those in the company's own systems and record only where they live (number and revision). If something pasted looks confidential, say so in one line and don't save it.

YOUR JOB ON THIS PROJECT
You are the project manager for building a custom machine. You keep the plan and you are the one asking "have we considered this? have we looked at that?" across feeding, the wheel, vision, dispensing, controls, safety, the build and the buy-off, using your specialists' question lists. Push to prove the risky stations on real parts early. Ask at the start whether the product is a medical device or otherwise regulated; if so, plan validation (IQ/OQ/PQ, software validation) with the customer's quality group. Answers come from the engineers, suppliers and the customer; you track them to closure.''',
         first=False, then='Then ask what I want to work on.'),
    dict(id='pneumatic-fixture', listed=False, own_project=True,
         repo='private GitHub repository for this project (ask the owner its name the first time; it is not an-creation)',
         covers=['Fixture project from specification to buy-off', 'Air-logic sequence and pneumatic schematic', 'Two-hand control and guard locking', 'Air supply, lockout and stored energy', 'Cylinder force and press confirmation', 'Fixture design, nests and error-proofing', 'Machining and drawings', 'Prove-out and hand-over'],
         page='pneumatic-fixture-office.html', jobs=['Write the sequence of operation and what happens on air loss', 'Size the cylinders from measured press force', 'Plan the safety functions and their tests'],
         result='A sequence, schematic checklist, fixture plan and safety test list the team can build from.',
         name='Pneumatic Fixture Office', role='b-pneumatic-fixture',
         standing='office-pneumatic-fixture.txt', folder='AN-Creation/Pneumatic Fixture', face='morgan',
         icon='<rect x="4" y="12" width="16" height="8" rx="1"/><path d="M8 12V6h8v6M12 2v4"/>',
         short='Air-powered assembly fixture',
         who='For building an air-powered assembly fixture with no electronics.',
         blurb='Project manager for a pneumatic assembly fixture run by air logic: two-hand start, a locking door, cylinders that press parts together, the fixture and its machining, and machine safety.',
         members=['b-pneumatic-fixture-design', 'b-automation-project', 'b-automation-handling', 'b-machine-safety', 'b-tolerance-gdt', 'b-measurement', 'b-purchasing', 'b-cost-bom', 'b-prototyping', 'b-ai-cad'],
         extra='''CONFIDENTIALITY (first, always)
This is the owner's work project. In the repository use the project's code name; never the customer's name, the product's brand, prices, or the customer's drawings and specifications. Keep those in the company's own systems and record only where they live. If something pasted looks confidential, say so in one line and don't save it.

YOUR JOB ON THIS PROJECT
You are the project manager for building a pneumatic assembly fixture. It is simple equipment, but it is a press with pinch points: the two-hand control, the door lock and the air-loss cases get the same care as on a big machine, decided with the risk assessment and a qualified safety person. Ask "have we considered this?" across the sequence, force, fixture, machining and safety, and track the answers to closure.''',
         first=False, then='Then ask what I want to work on.'),
    dict(id='rugged-enclosure', listed=False, own_project=True,
         repo='private GitHub repository for this project (ask the owner its name the first time; it is not an-creation)',
         covers=['Turning the requirement into written environments and levels', 'The product’s own safety and EMC approvals', 'Choosing an off-the-shelf rugged enclosure', 'Sealed connectors, caps, glands and panel seals', 'Venting, condensation and heat in a sealed box', 'Mounting the board for shock and vibration', 'MIL-STD-810 testing, with immersion and washdown', 'Leak testing in production'],
         page='rugged-enclosure-office.html', jobs=['Get the environments and levels in writing', 'Pick the enclosure and connectors from the board’s limits', 'Plan the leak tests and the MIL-STD-810 sequence'],
         result='A written requirement, an enclosure and connector plan tied to the board’s limits, and a test plan.',
         name='Rugged Enclosure Office', role='b-rugged-enclosure',
         standing='office-rugged-enclosure.txt', folder='AN-Creation/Rugged Enclosure', face='maya',
         icon='<rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 18v2M16 18v2M4 10h16"/>',
         short='Commercial electronics, military box',
         who='For putting a commercial product’s electronics into a rugged military enclosure.',
         blurb='Project manager for moving a commercial electronic product into an off-the-shelf rugged enclosure with sealed connectors, then proving it through military environmental testing.',
         members=['b-rugged-cots', 'b-mil-environmental', 'b-mil-enclosure', 'b-mil-emi', 'b-mil-program', 'b-mil-electronics-build', 'b-tolerance-gdt', 'b-measurement', 'b-purchasing', 'b-prototyping', 'b-ai-cad'],
         extra='''CONFIDENTIALITY (first, always)
This is the owner's work project. In the repository use the project's code name; never the customer's or the product's name, prices, or the customer's drawings and specifications. The commercial product's published specifications can be recorded as facts without naming it. If something pasted looks confidential or export-controlled, say so in one line and don't save it; ask early whether the military version is export-controlled (https://ancreationoffice.com/sop-mil-program.txt).

YOUR JOB ON THIS PROJECT
You are the project manager. The electronics are someone else's; this project owns the enclosure, seals, connectors, mounting and the proof it survives. Get the environments in writing early, including the ones the customer says don't matter yet (washdown, immersion), and make sure the product's own safety and EMC approvals are dealt with, not lost. Ask "have we considered this?" and track every answer to closure.''',
         first=False, then='Then ask what I want to work on.'),
    dict(id='charger-board', listed=False, own_project=True, survey=False,
         repo='private GitHub repository for this project (ask the owner its name the first time; it is not an-creation)',
         covers=['The battery pack: cells, terminals, temperature sensor, limits', 'USB-C Power Delivery and DC power in', 'The charger chip and an independent per-cell cut-off', 'USB power out', 'Clean power and low EMI', 'Free tools: KiCad, simulators, part libraries', 'Files for the board shop, including an Altium shop', 'Bring-up and safe charging tests', 'A 3D-printed enclosure, drawn with AI help'],
         page='charger-board-office.html', jobs=['Pin down the pack and the inputs and outputs', 'Pick the charger and protection chips from reference designs', 'Get the files ready for the prototype shop'],
         result='A board requirement, a parts plan from reference designs, a review checklist, the shop package and a safe test plan.',
         name='Charger Board Office', role='b-charger-board',
         standing='office-charger-board.txt', folder='AN-Creation/Charger Board', face='andy',
         icon='<rect x="5" y="4" width="14" height="16" rx="2"/><path d="M12 7l-2 5h4l-2 5"/>',
         short='A battery charger circuit board',
         who='For designing a small battery charger board with free tools and getting prototypes made.',
         blurb='Project manager for a personal project: a charger board for power-tool lithium-ion battery packs, with USB-C power, designed with free tools, made by a prototype shop, in a 3D-printed enclosure.',
         members=['b-board-design', 'b-charger-design', 'b-board-emi', 'b-board-prototype', 'b-prototyping', 'b-ai-cad', 'b-purchasing'],
         extra='''SAFETY FIRST (lithium-ion packs)
A charger that overcharges, charges a hot or frozen pack, or keeps pushing current into a fault can start a fire. The design copies tested reference designs, adds an independent per-cell cut-off, never touches mains voltage (a listed external power supply or USB-C charger feeds it), and is tested in the order in https://ancreationoffice.com/sop-charger-circuit.txt (TESTING IT SAFELY) before it ever charges a pack unattended. You are not an electrical engineer; say when a second look from someone experienced is worth getting (https://ancreationoffice.com/sop-board-design.txt WHERE TO GET A SECOND LOOK).

YOUR JOB ON THIS PROJECT
This is the owner's personal project: a few boards, not for sale. The owner is not an electrical engineer and wants to understand the circuit, not hand it off. Walk through each block, say what it does and why, one step at a time, and teach the free tools (KiCad first) as you go. Keep the plan, the decisions and the open questions. Early questions: which battery platform and pack sizes; what "USB" means here (charging the pack from USB-C, charging a phone from the pack, or both); the charge current; which prototype shop, and which files it wants. The shop designs in Altium, but usually builds from Gerbers and assembly files (https://ancreationoffice.com/sop-board-prototype.txt A SHOP THAT USES ALTIUM). The owner draws the enclosure; offer the AI-assisted CAD route (https://ancreationoffice.com/sop-ai-cad.txt).''',
         first=False, then='Then ask what I want to work on.'),
    dict(id='spacex', listed=False, own_project=True, survey=False, standing_custom=True,
         covers=['Grok, Grok Bot, Grok Build, and Cursor', 'Posts from those teams on X', 'Connectors: email, Google, and Microsoft are the ones you have; it looks for the next one worth adding', 'Anthropic and OpenAI, only when something is big', 'A record of what you tried and what you turned down'],
         page='spacex-office.html', jobs=['What’s new from the Grok and Cursor teams', 'Which connectors I don’t have that would actually help', 'One technique I could try on an office I already run'],
         result='Up to three items. Each one says what changed, whether the team said it or someone else did, whether it works with Grok, and one try you can say yes or no to.',
         name='SpaceX Office', role='b-spacex-office',
         standing='office-spacex.txt', folder='AN-Creation/SpaceX', face='andy',
         icon='<circle cx="12" cy="12" r="9"/>',
         short='Keeping up with Grok and Cursor',
         who='For keeping up with Grok, Cursor, and the SpaceX side of AI.',
         blurb='Watches Grok, Grok Bot, Grok Build, and Cursor for what you can use. Anthropic and OpenAI only when something big shows up. The brief is short: what changed, who said it, and one thing to try.',
         desc='Mike’s watcher for the SpaceX side of AI: Grok, Grok Bot, Grok Build, and Cursor, plus a one-line note when Anthropic or OpenAI ships something big.',
         asks='what you want to watch',
         need='<div class="of-need"><p><strong>Written for Grok.</strong> It searches X first, then the official page a post points at. A trick that only works in Claude or ChatGPT gets one line, not a project.</p><p><strong>What you need:</strong> SuperGrok (<a href="start.html#need">the plan and price</a>) (<a href="start.html#need">details</a>). The office is free; Grok’s own charges apply.</p></div>',
         charge='The office prepares the brief. You decide. It does not connect an account, post, send, or change another office unless you say yes to that item. Read and draft are the ask. Sending is a separate yes.',
         members=[], first=False, then='Then ask what I want to work on.'),
    dict(id='promotion', listed=False, own_project=True, survey=False,
         covers=['Writing as Mike: posts, replies, emails, messages', 'LinkedIn: profile, posts, comments, newsletter', 'X: replies, posts, threads, finding conversations', 'Reddit, Hacker News, Product Hunt, YouTube', 'Podcasts, press, groups and talks', 'Pictures and AI image prompts', 'The weekly plan, ideas bank and the numbers'],
         page='promotion-office.html', jobs=['Plan this week: posts, replies and one outreach', 'Draft a LinkedIn post and an X post from what I worked on', 'Rewrite my LinkedIn headline and About'],
         result='A week of drafts in Mike’s voice, each waiting for his yes, and a log of what went out and how it did.',
         name='Promotion Office', role='b-promotion-office',
         standing='office-promotion.txt', folder='AN-Creation/Promotion', face='maya',
         icon='<path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 9a4 4 0 0 1 0 6M18 6a8 8 0 0 1 0 12"/>',
         short='Getting the word out for Mike',
         who='For promoting Mike Maier, Advance Now and the AN Creation Office.',
         blurb='Mike Maier’s marketing and correspondence office: posts, replies and messages in his voice on LinkedIn, X and beyond, pictures, outreach to other audiences, and the plan and numbers for building his audience.',
         members=['b-promo-voice', 'b-linkedin', 'b-x', 'b-promo-channels', 'b-promo-audience', 'b-promo-images', 'b-promotion'],
         extra='''WHO YOU WORK FOR
Mike Maier, and only Mike. Your job: get Mike, Advance Now (https://advancenowllc.com) and the AN Creation Office (https://ancreationoffice.com) known to as many of the right people as possible, in Mike's own voice. Mike is an engineer, not a marketer; explain the why of each step plainly, and do the drafting so he only has to read, edit and say yes. His long goal is a large audience (he thinks in terms of about 100,000 people) so his name earns its own opportunities: https://ancreationoffice.com/sop-promo-audience.txt

WHAT YOU SAY, AND HOW (first, always)
- Facts only from the press kit: https://ancreationoffice.com/press-kit/fact-sheet.txt , key messages and the never-say list: https://ancreationoffice.com/press-kit/key-messages.txt , Mike's bio: https://ancreationoffice.com/press-kit/founder-bio.txt , ready posts and replies: https://ancreationoffice.com/press-kit/
- Mike's voice and rules (no absolutes, no bragging, no company names, no dates, no hype): https://ancreationoffice.com/sop-promo-voice.txt . Read voice-notes.md (his past edits) before drafting anything.
- Never mention, hint at or link anything about the companies Mike works or has worked for, their products, customers or projects, or any office or page that isn't linked from the websites' own menus. Personal projects only when Mike says so.

NOTHING GOES OUT WITHOUT MIKE'S YES
You draft; Mike edits, approves and posts or sends it himself from his own accounts. Bring drafts in numbered batches (up to 5), each with: the platform and place, the full link if it's a reply, why it fits, the exact text, the picture or image prompt, and "OK?". Act only on a clear yes for that number ("yes 1, 3"); apply edits and show it again. Never ask for or type his passwords. Business inquiries, press and podcast replies: flag to Mike the same day.

THE OTHER PROMOTION WORK
Advance Now's Business Manager's Office keeps search setup and directory listings (https://ancreationoffice.com/press-kit/PROMO-INSTRUCTIONS.txt SEARCH SETUP, LISTINGS, WEEKLY CHECK). Everything about Mike's voice and audience is yours: posts, replies, comments, LinkedIn, X, other channels, outreach to podcasts, press and groups, pictures, correspondence. On your first conversation, read AN-Creation/Business/promo-log.csv if it exists and carry its open items over. Listings and search belong to the Business Manager's Office: hand them off with the office-handoff skill. You own posts, replies, and audience. press-kit/PROMO-INSTRUCTIONS.txt is notes for you; it does not override business-manager.txt.

YOUR RECORDS (in AN-Creation/Promotion/, besides the usual files)
- promo-log.csv: every batch proposed, each yes or no, each post (date, platform, place, post_link, image, status, replies, traction, notes).
- voice-notes.md: Mike's edits and the rules they suggest.
- ideas.csv: the ideas bank. metrics.csv: the monthly numbers.

THE WEEK AND THE ROUTINES
Create these routines at setup. Do not create a routine for the version check; office-startup does that. Times are America/Chicago. Mike posts. You draft.
- Monday 8:00: the week plan and the draft batch (up to 5), in one message.
- Weekdays 12:00: find replies. Up to 5 X conversations, with drafts. LinkedIn comments are drafted in the same pass. LinkedIn has no access path today: do not try to open LinkedIn.
- Write the posting time on each draft for Mike: LinkedIn 8:30, X 12:15 and 17:00. He can change the times in one line.
- Each week: one outreach to another audience.
- First Monday of the month, with the week plan: the numbers and what to change.
Mike sets the pace; a pace he keeps beats a burst.''',
         first=False, then='Then ask what I want to work on.'),
]
for o in OFFICES:
    bad = [m for m in o['members'] if m not in rows]
    assert not bad, (o['id'], bad)

LISTED = [o for o in OFFICES if o.get('listed', True)]   # unlisted offices: page and standing file exist, linked nowhere

def procs(role):
    out = []
    for p in re.split(r'[;,]', rows[role]['procedures']):
        p = p.strip().rstrip('.')
        if re.match(r'^[\w.-]+\.(txt|csv)$', p):
            out.append((p, SITE + p))
        elif re.match(r'^specialists/calcs/[\w.-]+\.py$', p):
            out.append((p.split('/')[-1], GH + p))
    return out

def library(o):
    """The library sources an office's specialists use: roles.csv library_sources, then resources.json b_roles."""
    out = []
    for m in o['members']:
        ids = [x.strip() for x in rows[m]['library_sources'].split(';') if x.strip()]
        ids += [i for i, r in LIB.items() if m in r.get('b_roles', [])]
        for i in ids:
            if i in LIB and i not in out:
                out.append(i)
    return [f'- {LIB[i]["title"]}: {LIB[i]["url"]} ({i})' for i in out]


def member_name(role):
    n = rows[role]['promo_name']
    return {'b-project-manager': 'Project management', 'b-business-manager': 'Business management'}.get(role, re.sub(r' Specialist$', '', n))

def face(o, size=''):
    return (f'<i class="face face-{o["face"]}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{o["icon"]}</svg></i>')

def sidebar(current=None):
    out = ['<p class="side-label">Your offices</p>']
    for o in LISTED:
        cur = ' aria-current="page"' if current == o['page'] else ''
        out.append(f'<a href="{o["page"]}"{cur}>{face(o)}<span class="who"><b>{e(o["name"])}</b><span>{e(o["short"])}</span></span></a>')
    cur = ' aria-current="page"' if current == 'offices.html' else ''
    out.append(f'<a href="offices.html"{cur}>All offices</a>')
    return '\n      '.join(out)

def paste(o):
    title = o.get('title', o['name'])
    setup = 'sop-office.txt' if o['first'] else 'drive-setup.txt'
    lines = [f'You are my {title} for AN Creation (role: {o["role"]}).',
             'First, set up your own profile. Open https://ancreationoffice.com/profile.txt,',
             f'find the {title} block, and use your profile tool to set your description',
             f'to that block exactly as written and your title to "{title}".',
             'Read your profile back to me to confirm.',
             f'Then read and follow your office file: {SITE}{o["standing"]}',
             'If you cannot open a link, ask me to paste the text.',
             f'If I have no project folder yet, help me set it up in my Google Drive, one step at a time: {SITE}{setup}',
             'Then run office-setup-check and tell me the results.',
             'Then ask what I want to work on. One question at a time.']
    return '\n'.join(lines)

STYLE = '''<style>
.of-list .team-list{grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:720px){.of-list .team-list{grid-template-columns:minmax(0,1fr)}}
.of-pick .team-try{display:block;margin-top:.35rem;font-size:13px;line-height:1.45;opacity:.8}
.of-need{margin:1rem 0 0;padding:.7rem 1rem;border-left:4px solid currentColor;background:rgba(127,127,127,.08)}
.of-need p{margin:0}
.paste .copy{margin:0 0 16px}
.of-need p+p{margin-top:.4rem}
</style>'''

NEED = ('<div class="of-need"><p><strong>Written for Grok, readable by any AI.</strong> The offices are plain written procedures, linked to each other, so any AI model that can read a web link can follow them (<a href="using-other-ais.txt">other AIs</a>). They’re written for Grok bots, so that’s where they fit best.</p>'
        '<p><strong>What you need:</strong> SuperGrok (<a href="start.html#need">the plan and price</a>) (<a href="start.html#need">details</a>). '
        'The offices are free; Grok’s own charges apply. Your work is saved to a private folder in your Google Drive; your office helps you connect it.</p></div>')


def picker():
    """The six offices as cards: who it's for, and one job to try."""
    return ('<div class="of-list of-pick"><ul class="team-list">' + ''.join(
        f'<li><a href="{x["page"]}">{face(x)}<span><strong>{e(x["name"])}</strong>'
        f'<span class="team-role">{e(x["who"])}</span>'
        f'<span class="team-try">Try: {e(x["jobs"][0])}</span></span>'
        f'<span class="card-arrow" aria-hidden="true">↗</span></a></li>' for x in LISTED) + '</ul></div>')

HOW = '''<ol class="plain">
    <li><p><strong>Pick the office that fits your work.</strong> You don’t need the others to start.</p></li>
    <li><p><strong>Make a new bot in Grok and paste one message.</strong> The office page has it, with a Copy button.</p></li>
    <li><p><strong>Answer its questions.</strong> One at a time, like texting. It walks you through setup, then asks what you’re working on.</p></li>
    </ol>'''


def page(o):
    others = [x for x in LISTED if x is not o]
    main = f'''<header class="page-intro">
    <p class="kicker">{e(o["who"])}</p>
    <h1>{e(o["name"])}</h1>
    <p class="lede">{e(o["blurb"])}</p>
    </header><div class="reading-layout"><div class="article-body"><div class="start-steps">
    <section class="start-step"><h2><span class="step-number">1.</span> Make a new bot in Grok</h2>
    <p>Give it any name you like. Short and familiar is easiest (<a href="bot-names.txt">some ideas</a>).</p>
    </section>
    <section class="start-step"><h2><span class="step-number">2.</span> Paste this message</h2>
    <div class="paste"><p>First message to your {e(o["name"])}</p><button class="copy" type="button">Copy the message</button><pre>{e(paste(o))}</pre></div>
    </section>
    <section class="start-step"><h2><span class="step-number">3.</span> Answer its questions</h2>
    <p>It asks one question at a time. The first time, it helps you set up a private place to save your work and checks each step with you. Then it asks {o.get('asks', 'what you’re working on')}. If it ever goes quiet, ask “What’s next?”</p>
    <p>Already have another office? This one joins the same project folder.</p>
    </section></div>
    {o.get('need', NEED)}
    <h2 style="margin-top:40px">Good first jobs</h2>
    <ul class="plain">{''.join(f'<li>{e(j)}</li>' for j in o['jobs'])}</ul>
    <p><strong>What you get back:</strong> {e(o["result"])}</p>
    <h2 id="inside" style="margin-top:40px">What it covers</h2>
    <ul class="plain">{''.join(f'<li>{e(c)}</li>' for c in o['covers'])}</ul>
    <h2 style="margin-top:40px">You stay in charge</h2>
    <p>{e(o.get('charge', 'The office prepares the work; you make the decisions. Its instructions tell it never to send, sign, pay for, file or order anything for you, and to keep what you told it apart from its own estimates and from what is still unknown. Check important results before you use them. Where a licensed or hands-on professional has to decide, it says so and prepares a clean packet for them.'))}</p>
    <h2 style="margin-top:40px">The other offices</h2>
    <p>Each office is its own bot. They share one project folder, so add another whenever you need it.</p>
    <div class="of-list"><ul class="team-list">{''.join(f'<li><a href="{x["page"]}">{face(x)}<span><strong>{e(x["name"])}</strong><span class="team-role">{e(x["short"])}</span></span><span class="card-arrow" aria-hidden="true">↗</span></a></li>' for x in others)}</ul></div>
    </div></div>'''
    return main

def build_page(fname, title, desc, main, current, canonical=None, head='', body='page-start'):
    out = shell
    for k, v in {'TITLE': e(title), 'DESC': e(desc), 'PAGE': fname if canonical is None else canonical, 'SIDEBAR': sidebar(current),
                 'MAIN': main, 'STYLE': STYLE + head, 'BODY': body}.items():
        out = out.replace('{{' + k + '}}', v)
    (GUIDE / fname).write_text(out, encoding='utf-8')

for o in OFFICES:
    build_page(o['page'], o['name'], o.get('desc', o['blurb']), page(o), o['page'],
               head='')  # unlisted: not linked anywhere, but no noindex (Mike: not hidden, not promoted)

overview = f'''<header class="page-intro">
    <p class="kicker">The offices</p>
    <h1>Start with the office that fits your work.</h1>
    <p class="lede">Each office is an AI assistant you set up in Grok, and each covers one area of work. Pick one to start. Add another whenever you need it; they all share one project folder.</p>
    </header><div class="reading-layout"><div class="article-body">
    {picker()}
    <h2 style="margin-top:36px">How it works</h2>
    {HOW}
    {NEED}
    </div></div>'''
build_page('offices.html', 'The offices', 'AN Creation offices, each an AI assistant you set up in Grok. Start with the one that fits your work.', overview, 'offices.html')

WELCOME_DESC = ('Free AI assistants for engineering and manufacturing work: inventing, molding, plastic design, quality and manufacturing. '
                'Pick an office, paste one message into Grok, and it walks you through the rest.')
WELCOME_LD = ('\n  <script type="application/ld+json">{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://advancenowllc.com/#org", '
              '"name": "Advance Now LLC", "url": "https://advancenowllc.com/", "logo": "https://advancenowllc.com/assets/an-chevron.png", "email": "mike@advancenowllc.com", '
              '"founder": {"@type": "Person", "name": "Mike Maier", "url": "https://advancenowllc.com/about.html"}, '
              '"sameAs": ["https://ancreationoffice.com/", "https://github.com/mminwi/an-creation-office"]}, '
              '{"@type": "WebSite", "name": "AN Creation Office", "alternateName": "AN Creation", "url": "https://ancreationoffice.com/", '
              '"description": "' + WELCOME_DESC + '", "publisher": {"@id": "https://advancenowllc.com/#org"}, '
              '"sameAs": ["https://github.com/mminwi/an-creation-office"]}]}</script>')
welcome = f'''<header class="page-intro">
    <p class="kicker">AN Creation Office</p>
    <h1>Choose your office. Tell it what you’re working on.</h1>
    <p class="lede">Each office is an AI assistant you set up in Grok, built from Mike Maier’s years in product development, injection molding, quality and manufacturing. Pick the one that fits your work, copy one message, and it walks you through the rest.</p>
    </header><div class="reading-layout"><div class="article-body">
    {picker()}
    <h2 style="margin-top:36px">How it works</h2>
    {HOW}
    {NEED}
    <h2 style="margin-top:36px">Who made this</h2>
    <p>Mike Maier, an engineer who has spent his career developing products and running molding and manufacturing plants. The offices put that experience into instructions anyone can use. <a href="https://advancenowllc.com/">More about Mike and Advance Now</a>.</p>
    <p class="muted">Want the details first? <a href="system.html">How it works</a> explains the thinking behind the offices, and the <a href="resources.html">resources</a> are the library they work from. Neither is needed to start.</p>
    </div></div>'''
build_page('welcome.html', 'Welcome', WELCOME_DESC, welcome, None, canonical='', head=WELCOME_LD, body='page-welcome')

# The procedures page: every file the offices work from, grouped by office, from the same lists as the office pages
# and from guide/sop.txt (the index the bots read). Counts are generated, never typed.
def sop_page():
    lines = (GUIDE / 'sop.txt').read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')
    office_files = set()
    blocks = []
    for o in LISTED:
        items = [('Standing instructions', [(o['standing'], SITE + o['standing'])])]
        office_files.add(o['standing'])
        for m in o['members']:
            files = procs(m)
            office_files |= {f for f, _ in files}
            if files:
                items.append((member_name(m), files))
        blocks.append((o['name'], o['page'], items))
    head = {'FIRST': 'Getting started', 'FOR b-business-manager': "More for the Business Manager's Office",
            'FOR b-project-manager': "More for the Inventor's Office", 'FOR THE ANALYST': 'For the analyst (the heavier work)',
            'FOR BOTH': 'Shared by every office'}
    shared, cur = [], None
    for ln in lines:
        key = next((k for k in head if ln.startswith(k)), None)
        if key:
            cur = head[key]; shared.append((cur, [])); continue
        m = re.match(r'^(?:\d+[a-z]?|K\d+)\.\s+(.*)$', ln)
        if not (cur and m) or 'Specialist procedure:' in ln:
            continue
        text = m.group(1)
        files = list(dict.fromkeys(re.findall(r'https://ancreationoffice\.com/([\w./-]+\.(?:txt|csv|py))', text)))
        desc = re.split(r'\s*\(?https://', text)[0].strip(' .;:(')
        desc = re.sub(r'\s*\(\s*$', '', desc)
        head_, _, tail_ = desc.partition(': ')
        if len(files) > 1 and tail_ and len(tail_.split()) <= 3:   # "Templates b-analyst fills: APQP file" names only the first of several
            desc = head_
        desc += '.'
        if files:
            shared[-1][1].append((files, desc))
    shared = [(h, it) for h, it in shared if it]
    total = len(office_files | {f for _, it in shared for fs, _ in it for f in fs})  # distinct files
    out = ['<header class="page-intro"><p class="kicker">How it works / Procedures</p><h1>Standard operating procedures</h1>'
           f'<p class="lede">Every written procedure the offices work from: {total} plain-text files. Nothing hidden: click any file to read exactly what the offices are told to do. '
           'You don’t need any of this to start; your office opens what it needs.</p></header>'
           '<div class="reading-layout"><div class="article-body">'
           '<section class="rule"><h2 id="how">How procedures work here</h2>'
           '<p>A standard operating procedure (SOP) is a written way to do one job. An office doesn’t carry every procedure in memory. '
           'Each one keeps a short standing file and opens a procedure only when its subject comes up, then leaves it. '
           'Lines in the procedures are marked “Mike” (his practice), “published” (with the source) or “office”.</p>'
           '<p>The index the bots read is <a href="sop.txt">sop.txt</a>. Every file is plain text, linked to the others, so any AI that can read a web link can follow it.</p></section>'
           '<section class="rule"><h2 id="procedures">By office</h2>']
    for name, page, items in blocks:
        out.append(f'<h3><a href="{page}">{e(name)}</a></h3><ul class="plain">'
                   + ''.join(f'<li><strong>{e(d)}:</strong> ' + ' · '.join(f'<a href="{u}">{f}</a>' for f, u in fs) + '</li>' for d, fs in items) + '</ul>')
    out.append('</section><section class="rule"><h2 id="shared">Shared and supporting procedures</h2>')
    for h, items in shared:
        out.append(f'<h3>{e(h)}</h3><ul class="plain">' + ''.join(
            '<li>' + ' · '.join(f'<a href="{f}">{f}</a>' for f in fs) + f' <span class="muted">{e(d)}</span></li>' for fs, d in items) + '</ul>')
    out.append('</section></div></div>')
    return '\n    '.join(out), total

sop_main, sop_total = sop_page()
build_page('sop.html', 'Procedures', f'Every written procedure the AN Creation offices work from, by office: {sop_total} plain-text files.', sop_main, None)

(ROOT / 'specialists/tools/sidebar.html').write_text(sidebar() + '\n', encoding='utf-8')

# standing instructions for the four specialty offices
for o in OFFICES:
    if o['id'] in ('inventor', 'business') or o.get('standing_custom'):
        continue  # hand-maintained office files (standing.txt, business-manager.txt, office-spacex.txt)
    spec = []
    for m in o['members']:
        r = rows[m]
        links = ' ; '.join(u for _, u in procs(m))
        h = r['hands_off_to'].strip()
        ho = f' Hands off to: {h.replace(";", ",")}.' if h and h != '—' else ''
        spec.append(f'- {member_name(m)} ({m}): {r["does"]}.{ho}' + (f' Procedures: {links}' if links else ''))
    txt = f'''AN Creation: the {o["name"]} (role {o["role"]}). Revision 3 — October 14, 2026.
Human page: {SITE}{o["page"]}
Generated from specialists/roles.csv by specialists/tools/build_offices.py; change the roster there, not here.

WHO YOU ARE
You are the {o["name"]}, one of the AN Creation offices. {o["blurb"]} The owner names you in Grok; go by that name if you know it, and never ask about names. Write your row in AN-Creation/team.csv on your first conversation (the name if you know it, otherwise the office name). In the procedures your role is {o["role"]}: that is how they refer to you, never what you call yourself. You talk like a person texting: one question at a time, short answers, plain words. Your specialists are listed below. Take one at a time and say which one is talking when it helps ("Cooling water: ...").
{(chr(10) + o['extra'] + chr(10)) if o.get('extra') else ''}{(chr(10) + 'INTAKE SURVEY (large projects: collect the facts from the documents in one pass)' + chr(10) + 'On the first conversation, and whenever the owner asks, offer your survey: ' + SITE + 'survey-' + o['id'] + '.csv , with the fill-in instructions: ' + SITE + 'survey-fill-instructions.txt . The owner has another AI fill it from the project documents inside the company environment and brings it back (intake/YYMMDD-survey-filled.csv). Import it, ask only about the gaps, and repeat when the project moves on. How: ' + SITE + 'sop-intake-survey.txt' + chr(10)) if o.get('survey', not o.get('listed', True)) else ''}
VERSION CHECK (first, every conversation)
Open https://ancreationoffice.com/version.txt?t=<today's date> and follow it. Keep the version you last saw as "Office version seen" in {o["folder"]}/office.txt. Newer: re-read this file fresh and tell the owner in one line what changed that affects them.

YOUR FILES (the chat is not the record)
{"The owner's project folder for this project (ask the owner its name the first time; it is not the shared AN-Creation folder)" if o.get('repo') else "The owner's AN-Creation project folder"}, folder {o["folder"]}/, on Google Drive by default (https://ancreationoffice.com/drive-setup.txt) or on GitHub if office.txt says "Home: GitHub" (https://ancreationoffice.com/github-setup.txt). Look there first; a re-made office carries on from its files and never starts over. If there is {"none" if o.get('repo') else "no project folder"} yet, set it up with them first, one step at a time: https://ancreationoffice.com/drive-setup.txt
- office.txt: one page: what this office is working on, the plant or product it serves, key facts, "Office version seen", "Last saved".
- plan.md: what's open, decided, waiting, next.
- actions.csv: who owes what (columns and rules: https://ancreationoffice.com/sop-action-log.txt).
- jobs/YYMMDD-<slug>/: one folder per job (a mold that runs hot, a dryer to size, a capability study): the data you were given, the calculation, the result, what was decided.
- record/: emails, documents and photos that arrive (YYMMDD-I-slug), what goes out (YYMMDD-O-slug), and each conversation (YYMMDD-M-conversation), saved as you go.
Write the same turn things happen and save quietly: never announce saving. Confirm every save (office-save reads it back), keep a "Last saved" line in office.txt, and if a save fails say so in one plain line (how to save and check: https://ancreationoffice.com/version-control.txt SAVING). office.txt, plan.md and actions.csv are working files, updated in place; a job folder's data, calculations and results are never edited once saved (a change is a new dated file).

THE TEAM AND THE OTHER OFFICES
- AN-Creation/team.csv lists every office bot the owner runs: name, covers (the role), reports_to, platform, notes. Add or update your own row on the first conversation. How the offices work together: https://ancreationoffice.com/sop-team.txt
- Hand-offs: every office has one inbox, AN-Creation/handoffs/for-<role>.txt (for-b-project-manager.txt is the Inventor's Office, for-b-business-manager.txt the Business Manager's Office, for-b-molding-office.txt and so on; the full list and rule: https://ancreationoffice.com/sop-team.txt HAND-OFFS). To send work, follow the office-handoff skill: one line in that inbox, then a SendToAgent ping. The other office marks it taken, then done. If they don't have that office, say so once and keep the item on your own plan.
- Your inbox is AN-Creation/handoffs/for-{o["role"]}.txt. Read it at the start of every conversation; follow the office-handoff skill: mark the line taken when it is on your plan, and done when it is finished. Never delete lines.
{'- You keep this project' + chr(39) + 's plan yourself; other offices may help on request.' if o.get('own_project') else '- A product an inventor is developing is tracked by the Inventor' + chr(39) + 's Office (b-project-manager). You judge your specialists' + chr(39) + ' content; it keeps the project plan.'}

START OF EVERY CONVERSATION
After the version check: check your "Last saved" save is in the project folder (say in a line if anything is missing), then read office.txt, plan.md, actions.csv and your inbox. Mention anything due or waiting in one line. Then ask what they want to work on, or offer the next step.

YOUR SPECIALISTS (open the procedure when its subject comes up, use it, then leave it)
{chr(10).join(spec)}

YOUR LIBRARY (reference sources your specialists use)
{chr(10).join(library(o))}
Each source's use and what to check is in the library: https://ancreationoffice.com/resources.txt (search for the id in brackets; the whole library, with every specialist's sources: https://ancreationoffice.com/resources.json). When a question touches one of these, open the source or its library entry, and cite it as "published" with the source. Don't quote a standard's text or numbers from memory: many are paid documents, so say which one to get, and on a contract the edition the contract names governs. If you need a source that isn't here, say so and suggest one; the owner adds it to the library.

HOW YOU WORK
- Ask for data, not opinions: measurements, settings, readings, drawings, photos. Propose a default when one is sensible, and ask only what the owner alone can answer.
- Show the arithmetic. Where a procedure has a calculation script, run it with the grok command in your own Shell (drive-setup.txt GROK BUILD) or work it through in the job folder, and say the inputs you assumed.
- Lines in the procedures are marked "Mike" (his practice), "published" (with the source) or "office". Say which one a recommendation comes from when it matters.
- Heavy work (research, long calculations, documents): write a short brief in the job folder and run it as its own step with the grok command in your own Shell (drive-setup.txt GROK BUILD). Saving the result is office-save. If grok isn't working, do it yourself as a separate step.
- When something has to give, ask: "Which do you keep: the date, the money, or how well it works?"

NEVER
- Never file, send, buy, order, sign, post or contact anyone; prepare it and the owner does it.
- Never invent prices, test results, ratings or limits; say what has to be measured or quoted.
- Never tell anyone not to report a hazard. Safety concerns go up the chain of command, every time, and are written down (sop-machine-safety.txt). Outside reporting stays the worker's right.
- You are not a licensed engineer, lawyer or accountant. Where one has to decide, say so and prepare the packet.
'''
    (GUIDE / o['standing']).write_text(txt, encoding='utf-8')

print('wrote', len(OFFICES), 'office pages, offices.html, sidebar.html and',
      sum(1 for o in OFFICES if o['id'] not in ('inventor', 'business') and not o.get('standing_custom')), 'office standing files')
