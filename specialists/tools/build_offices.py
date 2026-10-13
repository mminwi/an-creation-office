"""Builds the AN Creation offices from specialists/roles.csv (run after any roster or office change).
Run from the repository root:  python specialists/tools/build_offices.py
Writes into guide/:
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
    dict(id='inventor', covers=['Planning the project and keeping it on track', "Whether people want it, and what they'd pay", 'Design', 'Prototypes', 'Making it easier and cheaper to build', 'Product safety and listings'], page='inventors-office.html', name="Inventor's Office", role='b-project-manager',
         standing='standing.txt', folder='(one folder per invention)', face='andy',
         icon='<circle cx="12" cy="12" r="9"/><path d="M14.8 8.2 13.2 13.2 8.2 14.8 9.8 9.8z" fill="currentColor" stroke="none"/>',
         short='Your idea, from first talk to prototype',
         who='For anyone with an idea. Start here.',
         blurb="Your project manager for every invention. It takes an idea from the first conversation through design, prototypes, tooling, testing and launch, keeps the paperwork, and tells you what's next.",
         members=['b-project-manager', 'b-market-check', 'b-design', 'b-prototyping', 'b-dfm', 'b-product-safety'],
         first=True, then='Then ask me to tell you about my invention.'),
    dict(id='business', covers=['The company', 'Patent preparation', 'A name and trademark', 'Licensing', 'Funding', 'Your website and promotion', 'Getting into stores'], page='business-office.html', name="Business Manager's Office", role='b-business-manager',
         standing='business-manager.txt', folder='AN-Creation/Business', face='larry',
         icon='<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
         short='Company, patent, money, selling',
         who='For the business side of having a product.',
         blurb='The business around your products: the company, patent preparation, a name and trademark, licensing, funding, your website, promotion, and getting into stores.',
         members=['b-business-manager', 'b-company-setup', 'b-patent-prep', 'b-trademark', 'b-licensing', 'b-funding', 'b-promotion', 'b-retail'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='molding', covers=['Setting up a solid molding process', 'Molding defects', 'Mold and machine cooling water', 'Drying and regrind', 'Buying a mold', 'Plastic materials', 'Machine safety'], page='molding-office.html', name='Molding Plant Office', role='b-molding-office',
         standing='office-molding.txt', folder='AN-Creation/Molding Plant', face='peter',
         icon='<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9h10M7 13h6"/>',
         short='Molding, cooling, drying, molds',
         who='For molders and anyone running injection molding.',
         blurb="Built from Mike Maier's years running molding plants: cooling water, drying and regrind, scientific molding, molding defects, buying molds, materials and machine safety.",
         members=['b-scientific-molding', 'b-molding-defects', 'b-cooling-water', 'b-drying-handling', 'b-mold-buying', 'b-plastic-materials', 'b-machine-safety'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='plastic', covers=['Plastic part design', 'Tolerances: will the parts fit together', 'Choosing the plastic', 'Designing for molding', 'Prototypes', 'Buying a mold'], page='plastic-design-office.html', name='Plastic Design Office', role='b-plastic-design-office',
         standing='office-plastic-design.txt', folder='AN-Creation/Plastic Design', face='morgan',
         icon='<path d="M4 18 12 4l8 14z"/><path d="M8 18h8"/>',
         short='Plastic parts that mold well',
         who='For anyone designing plastic parts.',
         blurb='Plastic parts that mold well: part design, tolerance stacks, material choice, design for molding, prototypes and the mold.',
         members=['b-plastic-part-design', 'b-tolerance-gdt', 'b-plastic-materials', 'b-dfm', 'b-prototyping', 'b-mold-buying'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='quality', covers=['Quality planning', 'Measurement and inspection', 'Lean Six Sigma and improvement'], page='quality-office.html', name='Quality Office', role='b-quality-office',
         standing='office-quality.txt', folder='AN-Creation/Quality', face='maya',
         icon='<path d="M5 12l4 4 10-10"/>',
         short='APQP, measurement, Six Sigma',
         who='For quality planning and improvement work.',
         blurb='Quality planning (APQP, FMEA, control plans), measurement and inspection, and Lean Six Sigma with the improvement toolbox.',
         members=['b-quality-planning', 'b-measurement', 'b-six-sigma'],
         first=False, then='Then ask what I want to work on.'),
    dict(id='manufacturing', covers=['Manufacturing cells and standard work', 'Purchasing', 'Cost and the parts list', 'Automation', 'Machine safety', 'Lean Six Sigma and improvement'], page='manufacturing-office.html', name='Manufacturing Office', role='b-manufacturing-office',
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
    lines = [f'You are my {o["name"]} for AN Creation. Your name is NAME.',
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
.name-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:6px 0 0}
.name-row input{font:inherit;font-size:15px;padding:9px 12px;border:1px solid var(--line);border-radius:6px;min-width:0;width:16rem;max-width:100%}
.of-list .team-list{grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:720px){.of-list .team-list{grid-template-columns:minmax(0,1fr)}}
</style>'''

NAMEJS = '''<script>
(function(){var i=document.getElementById('botName'),p=document.getElementById('pasteText');if(!i||!p)return;var t=p.textContent;
function up(){var n=(i.value||'').trim();p.textContent=t.replace('NAME',n||'NAME');try{localStorage.setItem('anc-name-'+location.pathname,n)}catch(x){}}
try{var s=localStorage.getItem('anc-name-'+location.pathname);if(s){i.value=s}}catch(x){}
i.addEventListener('input',up);up();})();
</script>'''

def page(o):
    others = [x for x in OFFICES if x is not o]
    first_note = ('<p>This is the office to start with. If it\'s your first one, it also sets up your accounts and project folder with you.</p>'
                  if o['first'] else
                  '<p>Already have the Inventor\'s Office? This one joins the same project folder. Starting with this office alone? It sets up the folder with you first.</p>')
    main = f'''<header class="page-intro">
    <p class="kicker">{e(o["who"])}</p>
    <h1>{e(o["name"])}</h1>
    <p class="lede">{e(o["blurb"])}</p>
    </header><div class="reading-layout"><div class="article-body"><div class="start-steps">
    <section class="start-step"><h2><span class="step-number">1.</span> Have your two accounts</h2>
    <p>A Grok account that includes Grok Build, and a free GitHub account. Details on the <a href="start.html">Start page</a>.</p>
    {first_note}
    </section>
    <section class="start-step"><h2><span class="step-number">2.</span> Make a new bot and name it</h2>
    <p>In Grok, start a new chat for this office (or a new bot or project, if your app has them). One office per chat. Give it a name: anything you like. <a href="bot-names.txt">Some ideas</a>.</p>
    <div class="name-row"><label for="botName"><strong>Its name:</strong></label><input id="botName" type="text" placeholder="for example, Ada" autocomplete="off"></div>
    </section>
    <section class="start-step"><h2><span class="step-number">3.</span> Paste this message</h2>
    <div class="paste"><p>First message to your {e(o["name"])}</p><pre id="pasteText">{e(paste(o))}</pre><button class="copy" type="button">Copy</button></div>
    <p>It asks one question at a time from there. If it ever stops or goes quiet, ask “What’s next?”</p>
    </section></div>
    <h2 id="inside" style="margin-top:40px">What it covers</h2>
    <ul class="plain">{''.join(f'<li>{e(c)}</li>' for c in o['covers'])}</ul>
    <h2 style="margin-top:40px">What it won’t do</h2>
    <p>It never sends, pays for, files, signs, publishes or orders anything without you. It never invents customers, prices, test results or limits. Where a licensed or hands-on professional has to decide, it says so and prepares a clean packet for them.</p>
    <h2 style="margin-top:40px">The other offices</h2>
    <p>Each office is its own bot. They share one project folder and pass work to each other, so add another office whenever you need it.</p>
    <div class="of-list"><ul class="team-list">{''.join(f'<li><a href="{x["page"]}">{face(x)}<span><strong>{e(x["name"])}</strong><span class="team-role">{e(x["short"])}</span></span><span class="card-arrow" aria-hidden="true">↗</span></a></li>' for x in others)}</ul></div>
    </div></div>
    {NAMEJS}'''
    return main

def build_page(fname, title, desc, main, current):
    out = shell
    for k, v in {'TITLE': e(title), 'DESC': e(desc), 'PAGE': fname, 'SIDEBAR': sidebar(current), 'MAIN': main, 'STYLE': STYLE}.items():
        out = out.replace('{{' + k + '}}', v)
    (GUIDE / fname).write_text(out, encoding='utf-8')

for o in OFFICES:
    build_page(o['page'], o['name'], o['blurb'], page(o), o['page'])

overview = f'''<header class="page-intro">
    <p class="kicker">The offices</p>
    <h1>Pick the offices you need.</h1>
    <p class="lede">AN Creation is a set of offices. Each one is a bot you name, and each covers one area of work. Start with the Inventor’s Office, then add another office whenever your project needs it. They all share one project folder.</p>
    </header><div class="reading-layout"><div class="article-body">
    <div class="of-list"><ul class="team-list">{''.join(f'<li><a href="{x["page"]}">{face(x)}<span><strong>{e(x["name"])}</strong><span class="team-role">{e(x["blurb"])}</span></span><span class="card-arrow" aria-hidden="true">↗</span></a></li>' for x in OFFICES)}</ul></div>
    <h2 style="margin-top:36px">How it works</h2>
    <ul class="plain"><li><strong>One bot per office.</strong> Each office page has the message to paste into a new bot. You give each bot its own name.</li>
    <li><strong>Each office covers one area.</strong> Pick the ones you need; nothing else to set up.</li>
    <li><strong>One project folder.</strong> Every office works in the same private GitHub repository and passes work to the others.</li>
    <li><strong>Start small.</strong> Most people start with the Inventor’s Office and add the Business Manager’s Office when business questions come up.</li></ul>
    </div></div>'''
build_page('offices.html', 'The offices', 'Six AN Creation offices, each a bot you name, each covering one area of work. Start with the Inventor’s Office.', overview, 'offices.html')
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
You are the {o["name"]}, one of the AN Creation offices. {o["blurb"]} The owner named you in their first message; talk under that name, and write it in your row of AN-Creation/team.csv. In the procedures your role is {o["role"]}: that is how they refer to you, never what you call yourself. You talk like a person texting: one question at a time, short answers, plain words. Your specialists are listed below. Take one at a time and say which one is talking when it helps ("Cooling water: ...").

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
