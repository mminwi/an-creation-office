"""Mold cooling water check (b-cooling-water). Procedure: guide/sop-cooling-water.txt

Run:  python cooling_water.py <input.json>
Input: see example-cooling-input.json (one mold) or example-plant-input.json (plant sizing). US units: lb, in, gpm, deg F, BTU.
Every result is proposed; the practice limits are Mike's (his own notes, kept private)
and the physics is standard (water heat balance, Reynolds number).
"""
import json, math, sys

# Mike's practice (2026-10-12). Degrees assumed F until Mike confirms.
GPM_SWEET = (3.0, 4.0)      # "about three, four gallon per minute through a standard water line"
GPM_EROSION = 9.0           # "nine, ten gallons per minute through a standard line ... you'll start eroding"
DT_LOOK = 5.0               # out vs in "more than about five degrees, you need to take a serious look"
DT_WORLD = 2.0              # "within a degree or two ... pretty much world class"
TOWER_X = (1.25, 1.5)       # tower capacity 1.25-1.5 x chiller capacity (Mike)
CHILLER_DT = 10.0           # chillers run best at about a 10 F rise across the chiller
UNITS = 3                   # three chillers and three pump sets, each a third of the worst case
TYPICAL = 2 / 3             # typical load about two thirds: two units run, one backup
HYD_TON_PER_HP = 0.10       # published: Advantage Engineering FYI 073, Conair, Plastics Technology card
def throat_tons(press_tons):  # published: Plastics Technology card (0.5 under 500 t, 1.0 at 500 t and up)
    return 1.0 if press_tons >= 500 else 0.5
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

def heat_per_lb(p):
    """BTU/lb from melt to ejection: an enthalpy number, or specific heat x temperature drop (resin supplier data)."""
    if p.get('delta_h_btu_per_lb') is not None:
        return p['delta_h_btu_per_lb'], 'enthalpy from supplier'
    if p.get('cp_btu_per_lb_F') is not None and p.get('melt_F') is not None and p.get('eject_F') is not None:
        h = p['cp_btu_per_lb_F'] * (p['melt_F'] - p['eject_F']) + (p.get('latent_btu_per_lb') or 0)
        return h, 'specific heat x (melt - eject)' + (' + heat of crystallization' if p.get('latent_btu_per_lb') else '')
    return None, 'not set: need the resin supplier\'s enthalpy, or specific heat with melt and ejection temperatures'

def lb_per_hr(p):
    if p.get('lb_per_hr') is not None: return p['lb_per_hr']
    return p['shot_lb'] * 3600 / p['cycle_s']

def mold(m):
    out = {'mold': m.get('mold', ''), 'note': 'Proposed results. Practice limits are Mike\'s; degrees F.'}
    rows = [circuit(c) for c in m.get('circuits', [])]
    out['circuits'] = rows
    water_q = sum(r['heat_btu_hr'] for r in rows)
    out['water_heat_btu_hr'] = water_q
    p = m.get('plastic')
    load = water_q
    if p:
        h, how = heat_per_lb(p)
        if h is None:
            out['plastic_heat_btu_hr'] = how
        else:
            q = lb_per_hr(p) * h
            load = q
            out['plastic_heat_btu_hr'] = round(q); out['heat_per_lb'] = f'{h:.1f} BTU/lb ({how})'
            out['water_vs_plastic'] = round(water_q / q, 2) if q and rows else None
            t = p.get('target_dt_F', DT_WORLD)
            out['gpm_total_for_target_dt'] = round(q / (500 * t), 1)
    out['tons'] = round(load / 12000, 2)
    return out

def plant(m):
    rows, total, missing = [], 0, []
    for pr in m['presses']:
        h, how = heat_per_lb(pr)
        if h is None:
            missing.append(pr['press']); rows.append({'press': pr['press'], 'worst_job': pr.get('worst_job', ''), 'heat': how}); continue
        lbh = lb_per_hr(pr); q = lbh * h; total += q
        rows.append({'press': pr['press'], 'worst_job': pr.get('worst_job', ''), 'lb_per_hr': round(lbh, 1),
                     'btu_per_lb': round(h, 1), 'heat_btu_hr': round(q)})
    hyd = sum(HYD_TON_PER_HP * pr['hydraulic_hp'] for pr in m['presses'] if pr.get('hydraulic_hp'))
    thr = sum(throat_tons(pr['press_tons']) for pr in m['presses'] if pr.get('press_tons') and pr.get('feed_throat', True))
    tons = total / 12000
    out = {'plant': m.get('plant', ''), 'note': 'Proposed. Mike\'s method: worst job on every press at once, split over three units, two run typically.',
           'presses': rows, 'worst_case_btu_hr': round(total), 'worst_case_tons': round(tons, 1),
           'mold_only_each_of_3_units_tons': round(tons / UNITS, 1),
           'hydraulic_tons_at_0.1_per_hp': round(hyd, 1), 'feed_throat_tons': round(thr, 1),
           'all_loads_tons': round(tons + hyd + thr, 1),
           'all_loads_each_of_3_units_tons': round((tons + hyd + thr) / UNITS, 1),
           'typical_load_tons_2_of_3': round((tons + hyd + thr) * TYPICAL, 1),
           'tower_heat_rejection_btu_hr': [round((tons + hyd + thr) * 12000 * x) for x in TOWER_X],
           'tower_nominal_tons_15000': [round((tons + hyd + thr) * 12000 * x / 15000, 1) for x in TOWER_X],
           'tower_note': 'Mike: 1.25-1.5x chiller capacity in chiller tons = 1.0-1.2 nominal tower tons (15,000 BTU/hr, compressor heat already included); do not add 1.25 again. Towers suit dry climates; near-100% humidity, consider air-cooled chillers. Final size from the chiller condenser rejection at site wet-bulb.',
           'chiller_loop_gpm_at_10F': round((tons + hyd + thr) * 12000 / (500 * CHILLER_DT)),
           'note_loads': 'Mike: hydraulics on chilled water, so size the chillers on all_loads. Hydraulic rule uses nameplate hp unless running hp is given.'}
    if missing: out['missing_heat_data'] = missing; out['worst_case_incomplete'] = 'totals leave out the presses listed in missing_heat_data'
    return out

def main(path):
    m = json.load(open(path))
    print(json.dumps(plant(m) if 'presses' in m else mold(m), indent=2))

if __name__ == '__main__':
    main(sys.argv[1])
