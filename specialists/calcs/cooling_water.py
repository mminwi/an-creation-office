"""Mold cooling water check (b-cooling-water). Procedure: guide/sop-cooling-water.txt

Run:  python cooling_water.py <input.json>
Input: see example-cooling-input.json. US units: lb, in, gpm, deg F, BTU.
Every result is proposed; the practice limits are Mike's (record/261012-M-cooling-water-mike.md)
and the physics is standard (water heat balance, Reynolds number).
"""
import json, math, sys

# Mike's practice (2026-10-12). Degrees assumed F until Mike confirms.
GPM_SWEET = (3.0, 4.0)      # "about three, four gallon per minute through a standard water line"
GPM_EROSION = 9.0           # "nine, ten gallons per minute through a standard line ... you'll start eroding"
DT_LOOK = 5.0               # out vs in "more than about five degrees, you need to take a serious look"
DT_WORLD = 2.0              # "within a degree or two ... pretty much world class"
RE_TURBULENT = 4000         # physics: fully turbulent pipe flow above about Re 4000

# Water kinematic viscosity, ft^2/s, from standard property tables (deg F -> value)
NU = [(40, 1.664e-5), (50, 1.410e-5), (60, 1.217e-5), (70, 1.059e-5), (80, 0.930e-5),
      (100, 0.739e-5), (120, 0.609e-5), (140, 0.514e-5), (160, 0.442e-5), (180, 0.385e-5)]

def nu_water(t):
    if t <= NU[0][0]: return NU[0][1]
    for (t1, v1), (t2, v2) in zip(NU, NU[1:]):
        if t <= t2: return v1 + (v2 - v1) * (t - t1) / (t2 - t1)
    return NU[-1][1]

def circuit(c):
    d_ft = c['line_dia_in'] / 12
    area = math.pi * d_ft ** 2 / 4
    vel = c['gpm'] * 0.002228 / area                     # gpm -> ft^3/s
    t_avg = (c['t_in_F'] + c['t_out_F']) / 2
    re = vel * d_ft / nu_water(t_avg)
    dt = c['t_out_F'] - c['t_in_F']
    q = 500 * c['gpm'] * dt                               # BTU/hr; 500 = 8.33 lb/gal x 60 min x 1 BTU/lb-F
    flags = []
    if c['gpm'] < GPM_SWEET[0]: flags.append('below 3-4 gpm: find the restriction; single-circuit this line')
    if c['gpm'] >= GPM_EROSION: flags.append('9+ gpm: erosion risk' + (' (aluminum: high)' if c.get('material') == 'aluminum' else ''))
    if re < RE_TURBULENT: flags.append(f'Re {re:,.0f}: not turbulent')
    if dt > DT_LOOK: flags.append(f'out-in {dt:.1f} F: take a serious look')
    elif dt <= DT_WORLD: flags.append('within 2 F: world class')
    return dict(name=c['name'], gpm=c['gpm'], velocity_ft_s=round(vel, 2), reynolds=round(re), dt_F=round(dt, 1),
                heat_btu_hr=round(q), flags=flags)

def main(path):
    m = json.load(open(path))
    out = {'mold': m.get('mold', ''), 'note': 'Proposed results. Practice limits are Mike\'s; degrees F assumed.'}
    rows = [circuit(c) for c in m.get('circuits', [])]
    out['circuits'] = rows
    water_q = sum(r['heat_btu_hr'] for r in rows)
    out['water_heat_btu_hr'] = water_q
    p = m.get('plastic')
    if p and p.get('delta_h_btu_per_lb') is not None:
        shots_hr = 3600 / p['cycle_s']
        plastic_q = p['shot_lb'] * shots_hr * p['delta_h_btu_per_lb']
        out['plastic_heat_btu_hr'] = round(plastic_q)
        out['water_vs_plastic'] = round(water_q / plastic_q, 2) if plastic_q else None
        t = p.get('target_dt_F', DT_WORLD)
        out['gpm_total_for_target_dt'] = round(plastic_q / (500 * t), 1)
    elif p:
        out['plastic_heat_btu_hr'] = 'not set: need delta_h_btu_per_lb from the resin supplier (melt to ejection)'
    load = out.get('plastic_heat_btu_hr') if isinstance(out.get('plastic_heat_btu_hr'), (int, float)) else water_q
    out['chiller_tons_before_margin'] = round(load / 12000, 2)
    out['margin'] = 'not set: chiller and tower sizing margin is Mike\'s call (sop-cooling-water.txt, open questions)'
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main(sys.argv[1])
