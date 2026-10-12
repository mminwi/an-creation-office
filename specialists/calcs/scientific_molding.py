"""Scientific molding studies (b-scientific-molding). Procedure: guide/sop-scientific-molding.txt

Run:  python scientific_molding.py <input.json>   (format: example-scientific-molding-input.json)
Each section is optional. Every result is proposed; the reasons are in the procedure.
Published formulas: relative shear rate = 1 / fill time; relative viscosity = hydraulic pressure x
intensification ratio x fill time (Plastics Technology); flat region where the change is under about 10%
(Entec Polymers); hold about 10% past gate seal (Bozzelli); peak pressure under about 80% of press max (Kulkarni).
"""
import json, sys

def viscosity(v):
    ir = v.get('intensification_ratio', 1)
    pts = sorted(({'speed': p['speed'], 'fill_s': p['fill_s'], 'shear': 1 / p['fill_s'],
                   'visc': p['hyd_pressure'] * ir * p['fill_s']} for p in v['points']), key=lambda p: p['shear'])
    for a, b in zip(pts, pts[1:]):
        b['change_pct_from_slower'] = round((a['visc'] - b['visc']) / a['visc'] * 100, 1)
    flat = [p for p in pts[1:] if abs(p['change_pct_from_slower']) < 10]
    out = {'points': [{k: (round(x, 3) if isinstance(x, float) else x) for k, x in p.items()} for p in pts]}
    if flat:
        out['flat_from_speed'] = flat[0]['speed']
        out['note'] = 'Flat (under 10% change) from this speed up. Mike: fill as fast as the press allows under control; watch for shear overheating at choke points.'
    return out

def gate_seal(g):
    pts = sorted(g['points'], key=lambda p: p['hold_s'])
    tol = g.get('plateau_pct', 0.1)
    seal = None
    for a, b in zip(pts, pts[1:]):
        if (b['weight'] - a['weight']) / a['weight'] * 100 < tol:
            seal = a['hold_s']; break
    if seal is None:
        return {'gate_seal_s': None, 'note': 'never leveled off: common on hot runners, valve gates and soft resins (procedure section 5)'}
    return {'gate_seal_s': seal, 'hold_set_s': round(seal * 1.1, 2), 'note': f'seal where weight gain fell under {tol}% per step; hold set 10% past it; keep total cycle constant'}

def balance(c):
    w = c['cavity_weights']; hi = max(w.values())
    return {k: round(x / hi * 100, 1) for k, x in w.items()} | {'lowest_pct': round(min(w.values()) / hi * 100, 1)}

def pressure(p):
    pct = p['peak_plastic_psi'] / p['press_max_psi'] * 100
    out = {'peak_pct_of_press_max': round(pct, 1)}
    if pct > 80: out['flag'] = 'over 80% of press max: pressure-limited risk'
    if 'gate_psi' in p and 'end_of_fill_psi' in p:
        out['drop_across_part_psi'] = p['gate_psi'] - p['end_of_fill_psi']
    return out

def window(w):
    lo, hi, run = w['low_good'], w['high_good'], w['running']
    mid = (lo + hi) / 2
    pos = (run - lo) / (hi - lo) * 100
    out = {'middle': mid, 'running_at_pct_of_window': round(pos, 1)}
    if pos < 25 or pos > 75: out['flag'] = f'running near the edge; Mike: run near the middle ({mid:g})'
    return out

def speed(s):
    rows = []
    for r in s['points']:
        actual = s['stroke_in'] / r['fill_s']
        rows.append({'set': r['set'], 'actual': round(actual, 2), 'error_pct': round((actual - r['set']) / r['set'] * 100, 1)})
    return rows

if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    fns = {'viscosity': viscosity, 'gate_seal': gate_seal, 'cavity_balance': balance, 'pressure': pressure, 'window': window, 'speed_check': speed}
    print(json.dumps({'note': 'Proposed. ' + d.get('mold', '')} | {k: fns[k](d[k]) for k in fns if k in d}, indent=2))
