"""Builds the AN Creation offices from specialists/roles.csv (run after any roster or office change).
Run from the repository root:  python specialists/tools/build_offices.py
Writes into guide/:
  welcome.html                      the site's front page: pick an office
  offices.html                      the overview of the six offices
  <office page>.html                one page per office: what's inside, how to start it, the paste message
  office-<id>.txt                   standing instructions for the four specialty offices
                                    (the Inventor's Office reads standing.txt; the Business Manager's Office reads business-manager.txt)
  specialists/tools/sidebar.html    the "Your offices" sidebar block, for pasting into the other site pages
Each office is one bot. The owner names it; the procedures call it by its role name."""
import csv, html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
GUIDE = ROOT / 'guide'
SITE = 'https://ancreationoffice.com/'
GH = 'https://github.com/mminwi/an-creation-office/blob/main/'
rows = {r['role']: r for r in csv.DictReader(open(ROOT / 'specialists/roles.csv', encoding='utf-8'))}
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
    dict(id='plastic', covers=['Plastic part design', 'Tolerances: will the parts fit together', 'Choosing the plastic', 'Designing for molding', 'Prototypes', 'Buying a mold'], page='plastic-design-office.html', jobs=['Review a part for molding: walls, draft, ribs, gates', 'Check whether parts will fit together (a tolerance stack)', 'Choose a plastic for the job'], result='A design-for-molding review tied to your drawing revision, with open questions for the molder.', name='Plastic Design Office', role='b-plastic-design-office',
         standing='office-plastic-design.txt', folder='AN-Creation/Plastic Design', face='morgan',
         icon='<path d="M4 18 12 4l8 14z"/><path d="M8 18h8"/>',
         short='Plastic parts that mold well',
         who='For anyone designing plastic parts.',
         blurb='Plastic parts that mold well: part design, tolerance stacks, material choice, design for molding, prototypes and the mold.',
         members=['b-plastic-part-design', 'b-tolerance-gdt', 'b-plastic-materials', 'b-dfm', 'b-prototyping', 'b-mold-buying'],
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
]
for o in OFFICES:
    bad = [m for m in o['members'] if m not in rows]
    assert not bad, (o['id'], bad)

def procs(role):
    out = []
    for p in re.split(r'[;,]', rows[role]['procedures']):
        p = p.strip().rstrip('.')
        if re.match(r'^[\w.-]+\.(txt|csv)$', p):
            out.append((p, SITE + p))
        elif re.match(r'^specialists/calcs/[\w.-]+\.py$', p):
            out.append((p.split('/')[-1], GH + p))
    return out

def member_name(role):
    n = rows[role]['promo_name']
    return {'b-project-manager': 'Project management', 'b-business-manager': 'Business management'}.get(role, re.sub(r' Specialist$', '', n))

def face(o, size=''):
    return (f'<i class="face face-{o["face"]}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{o["icon"]}</svg></i>')

def sidebar(current=None):
    out = ['<p class="side-label">Your offices</p>']
    for o in OFFICES:
        cur = ' aria-current="page"' if current == o['page'] else ''
        out.append(f'<a href="{o["page"]}"{cur}>{face(o)}<span class="who"><b>{e(o["name"])}</b><span>{e(o["short"])}</span></span></a>')
    cur = ' aria-current="page"' if current == 'offices.html' else ''
    out.append(f'<a href="offices.html"{cur}>All offices</a>')
    return '\n      '.join(out)

def paste(o):
    lines = [f'You are my {o["name"]} for AN Creation.',
             f'In the procedures your role is {o["role"]}: that is how they refer to you.',
             'Read and follow your standing instructions:',
             SITE + o['standing'],
             'If you cannot open a link, ask me to paste the text.']
    if o['first']:
        lines += ['If this is my first office, help me set up first, one step at a time:', SITE + 'sop-office.txt',
                  'If I already have an an-creation repository on GitHub, use it and add yourself to AN-Creation/team.csv.']
    else:
        lines += ['Use my an-creation repository on GitHub and add yourself to AN-Creation/team.csv.',
                  'If I don\'t have one yet, help me set it up first, one step at a time:', SITE + 'github-setup.txt']
    lines += [o['then'], 'One question at a time.']
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

NEED = ('<div class="of-need"><p><strong>What you need:</strong> a Grok subscription (<a href="start.html#need">which one</a>). '
        'The offices are free; Grok’s own charges apply. Your office helps you make a free GitHub account to save your work.</p></div>')


def picker():
    """The six offices as cards: who it's for, and one job to try."""
    return ('<div class="of-list of-pick"><ul class="team-list">' + ''.join(
        f'<li><a href="{x["page"]}">{face(x)}<span><strong>{e(x["name"])}</strong>'
        f'<span class="team-role">{e(x["who"])}</span>'
        f'<span class="team-try">Try: {e(x["jobs"][0])}</span></span>'
        f'<span class="card-arrow" aria-hidden="true">↗</span></a></li>' for x in OFFICES) + '</ul></div>')

HOW = '''<ol class="plain">
    <li><p><strong>Pick the office that fits your work.</strong> You don’t need the others to start.</p></li>
    <li><p><strong>Make a new bot in Grok and paste one message.</strong> The office page has it, with a Copy button.</p></li>
    <li><p><strong>Answer its questions.</strong> One at a time, like texting. It walks you through setup, then asks what you’re working on.</p></li>
    </ol>'''


def page(o):
    others = [x for x in OFFICES if x is not o]
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
    <p>It asks one question at a time. The first time, it helps you set up a private place to save your work and checks each step with you. Then it asks what you’re working on. If it ever goes quiet, ask “What’s next?”</p>
    <p>Already have another office? This one joins the same project folder.</p>
    </section></div>
    {NEED}
    <h2 style="margin-top:40px">Good first jobs</h2>
    <ul class="plain">{''.join(f'<li>{e(j)}</li>' for j in o['jobs'])}</ul>
    <p><strong>What you get back:</strong> {e(o["result"])}</p>
    <h2 id="inside" style="margin-top:40px">What it covers</h2>
    <ul class="plain">{''.join(f'<li>{e(c)}</li>' for c in o['covers'])}</ul>
    <h2 style="margin-top:40px">You stay in charge</h2>
    <p>The office prepares the work; you make the decisions. Its instructions tell it never to send, sign, pay for, file or order anything for you, and to keep what you told it apart from its own estimates and from what is still unknown. Check important results before you use them. Where a licensed or hands-on professional has to decide, it says so and prepares a clean packet for them.</p>
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
    build_page(o['page'], o['name'], o['blurb'], page(o), o['page'])

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
build_page('offices.html', 'The offices', 'Six AN Creation offices, each an AI assistant you set up in Grok. Start with the one that fits your work.', overview, 'offices.html')

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
(ROOT / 'specialists/tools/sidebar.html').write_text(sidebar() + '\n', encoding='utf-8')

# standing instructions for the four specialty offices
for o in OFFICES:
    if o['id'] in ('inventor', 'business'):
        continue
    spec = []
    for m in o['members']:
        r = rows[m]
        links = ' ; '.join(u for _, u in procs(m))
        h = r['hands_off_to'].strip()
        ho = f' Hands off to: {h.replace(";", ",")}.' if h and h != '—' else ''
        spec.append(f'- {member_name(m)} ({m}): {r["does"]}.{ho}' + (f' Procedures: {links}' if links else ''))
    txt = f'''AN Creation: the {o["name"]} (role {o["role"]}). Revision 1 — October 13, 2026.
Human page: {SITE}{o["page"]}
Generated from specialists/roles.csv by specialists/tools/build_offices.py; change the roster there, not here.

WHO YOU ARE
You are the {o["name"]}, one of the AN Creation offices. {o["blurb"]} The owner names you in Grok; go by that name if you know it, and never ask about names. Write your row in AN-Creation/team.csv on your first conversation (the name if you know it, otherwise the office name). In the procedures your role is {o["role"]}: that is how they refer to you, never what you call yourself. You talk like a person texting: one question at a time, short answers, plain words. Your specialists are listed below. Take one at a time and say which one is talking when it helps ("Cooling water: ...").

VERSION CHECK (first, every conversation)
Open https://ancreationoffice.com/version.txt?t=<today's date> and follow it. Keep the version you last saw as "Office version seen" in {o["folder"]}/office.txt. Newer: re-read this file fresh and tell the owner in one line what changed that affects them.

YOUR FILES (the chat is not the record)
The owner's private GitHub repository an-creation, folder {o["folder"]}/. Look there first; a re-made office carries on from its files and never starts over. If there is no repository yet, set it up with them first, one step at a time: https://ancreationoffice.com/github-setup.txt
- office.txt: one page: what this office is working on, the plant or product it serves, key facts, "Office version seen".
- plan.md: what's open, decided, waiting, next.
- actions.csv: who owes what (columns and rules: https://ancreationoffice.com/sop-action-log.txt).
- jobs/YYMMDD-<slug>/: one folder per job (a mold that runs hot, a dryer to size, a capability study): the data you were given, the calculation, the result, what was decided.
- record/: emails, documents and photos that arrive (YYMMDD-I-slug), what goes out (YYMMDD-O-slug), and each conversation (YYMMDD-M-conversation), saved as you go.
Write the same turn things happen, and commit, silently: never announce saving or committing. Nothing is overwritten: an update is a new dated file.

THE TEAM AND THE OTHER OFFICES
- AN-Creation/team.csv lists every office bot the owner runs: name, covers (the role), reports_to, platform, notes. Add or update your own row on the first conversation. How the offices work together: https://ancreationoffice.com/sop-team.txt
- Work for another office goes in AN-Creation/handoffs/for-<its role>.txt (date, what, why); tell the owner in one line which office it's for, by that bot's name if team.csv has one. Read AN-Creation/handoffs/for-{o["role"]}.txt at the start of every conversation and clear each line once it is on your plan.
- A product an inventor is developing is tracked by the Inventor's Office (b-project-manager). You judge your specialists' content; it keeps the project plan.

START OF EVERY CONVERSATION
After the version check: read office.txt, plan.md, actions.csv and your hand-off file. Mention anything due or waiting in one line. Then ask what they want to work on, or offer the next step.

YOUR SPECIALISTS (open the procedure when its subject comes up, use it, then leave it)
{chr(10).join(spec)}

HOW YOU WORK
- Ask for data, not opinions: measurements, settings, readings, drawings, photos. Propose a default when one is sensible, and ask only what the owner alone can answer.
- Show the arithmetic. Where a procedure has a calculation script, run it (Grok Build in your cloud terminal) or work it through in the job folder, and say the inputs you assumed.
- Lines in the procedures are marked "Mike" (his practice), "published" (with the source) or "office". Say which one a recommendation comes from when it matters.
- Heavy work (research, long calculations, documents): write a short brief in the job folder and run it as its own step with Grok Build in your cloud terminal (b-analyst's role), then check what came back. If that isn't working, do it yourself as a separate step.
- When something has to give, ask: "Which do you keep: the date, the money, or how well it works?"

NEVER
- Never file, send, buy, order, sign, post or contact anyone; prepare it and the owner does it.
- Never invent prices, test results, ratings or limits; say what has to be measured or quoted.
- Never tell anyone not to report a hazard. Safety concerns go up the chain of command, every time, and are written down (sop-machine-safety.txt). Outside reporting stays the worker's right.
- You are not a licensed engineer, lawyer or accountant. Where one has to decide, say so and prepare the packet.
'''
    (GUIDE / o['standing']).write_text(txt, encoding='utf-8')

print('wrote', len(OFFICES), 'office pages, offices.html, sidebar.html and',
      sum(1 for o in OFFICES if o['id'] not in ('inventor', 'business')), 'office standing files')
