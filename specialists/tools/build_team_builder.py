"""Builds guide/team-builder.html from specialists/roles.csv (run after any roster change).
Run from the repository root:  python specialists/tools/build_team_builder.py"""
import csv, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / 'specialists/roles.csv')))
names = re.findall(r'[A-Z][a-z]+', (ROOT / 'guide/bot-names.txt').read_text().split('EASY NAMES')[1].split('FAMILIAR')[0])

def proc_files(s):
    return [p.strip() for p in re.split(r'[;,]', s) if re.match(r'^\s*[\w.-]+\.(txt|csv|md)\s*$', p)]

MIKE = {'b-cooling-water', 'b-drying-handling', 'b-scientific-molding', 'b-molding-defects', 'b-mold-buying', 'b-machine-safety', 'b-six-sigma'}
OFFICE = {'b-project-manager', 'b-business-manager', 'b-company-setup', 'b-patent-prep', 'b-trademark', 'b-licensing-funding', 'b-promotion', 'b-prototyping', 'b-quality-planning'}
def basis(r):
    h = r['hands_off_to'].strip()
    tail = (' Hands off to: ' + h.replace(';', ',') + '.') if h and h != '—' else ''
    if r['role'] in MIKE:
        return "Built from Mike Maier's own plant and molding practice." + tail
    if r['tier'] in ('Managed', 'Documented') and tail:
        return 'Organizes the work and prepares the packet; a licensed or hands-on professional decides.' + tail
    if r['role'] in OFFICE:
        return 'Runs on the AN Creation office procedures.' + tail
    return 'Built from the standard references for this area.' + tail

roles = []
for r in rows:
    if r['role'] == 'b-analyst':
        continue
    roles.append({'id': r['role'], 'name': r['promo_name'], 'group': r['group'], 'does': r['does'],
                  'procs': proc_files(r['procedures'])[:4], 'tier': r['tier'], 'handoff': r['hands_off_to'],
                  'basis': basis(r)})

P = 'b-project-manager'
packages = [
    {'id': 'one', 'name': 'Just the basics', 'blurb': 'One bot as your project manager. Add specialists any time.',
     'roles': [P]},
    {'id': 'inventor', 'name': "Inventor's Office", 'blurb': 'Take an idea from first conversation to a product: plan, business, patent prep, design, prototype.',
     'roles': [P, 'b-business-manager', 'b-company-setup', 'b-patent-prep', 'b-trademark', 'b-licensing-funding', 'b-promotion', 'b-design', 'b-dfm', 'b-prototyping', 'b-quality-planning', 'b-product-safety']},
    {'id': 'molding', 'name': 'Molding Plant Office', 'blurb': 'For molders: cooling water, drying and regrind, scientific molding, defects, mold buying, machine safety.',
     'roles': [P, 'b-cooling-water', 'b-drying-handling', 'b-scientific-molding', 'b-molding-defects', 'b-mold-buying', 'b-machine-safety', 'b-plastic-materials']},
    {'id': 'plastic', 'name': 'Plastic Design Office', 'blurb': 'Plastic parts that mold well: part design, tolerance stacks, materials, design for molding.',
     'roles': [P, 'b-plastic-part-design', 'b-tolerance-gdt', 'b-plastic-materials', 'b-dfm', 'b-prototyping', 'b-mold-buying']},
    {'id': 'quality', 'name': 'Quality Office', 'blurb': 'APQP, measurement, Lean Six Sigma and the improvement toolbox.',
     'roles': [P, 'b-quality-planning', 'b-measurement', 'b-six-sigma', 'b-manufacturing']},
    {'id': 'manufacturing', 'name': 'Manufacturing Office', 'blurb': 'Cells and standard work, purchasing, cost, automation and safety.',
     'roles': [P, 'b-manufacturing', 'b-purchasing', 'b-cost-bom', 'b-automation', 'b-machine-safety', 'b-six-sigma']},
    {'id': 'electrical', 'name': 'Electrical Prep Office', 'blurb': 'Get a project ready for your electrical engineer: requirements, controls, batteries, EMI, safety listing.',
     'roles': [P, 'b-electrical', 'b-controls', 'b-battery-power', 'b-emi-fcc', 'b-product-safety']},
    {'id': 'all', 'name': 'Everything', 'blurb': 'Every specialist the office has.', 'roles': [r['id'] for r in roles]},
]
ids = {r['id'] for r in roles}
for p in packages:
    bad = [x for x in p['roles'] if x not in ids]
    assert not bad, (p['id'], bad)

data = json.dumps({'roles': roles, 'packages': packages, 'names': names}, ensure_ascii=False)
tpl = (ROOT / 'specialists/tools/team-builder.template.html').read_text()
(ROOT / 'guide/team-builder.html').write_text(tpl.replace('/*DATA*/null', data))
cat = (ROOT / 'specialists/tools/specialists.template.html').read_text()
(ROOT / 'guide/specialists.html').write_text(cat.replace('/*DATA*/null', data))
print('wrote guide/specialists.html')
print('wrote guide/team-builder.html:', len(roles), 'roles,', len(packages), 'packages,', len(names), 'names')
