"""Drying hopper check (b-drying-handling). Procedure: guide/sop-drying.txt

Run:  python drying.py <input.json>   (format: example-drying-input.json)
Published rule: hopper capacity = drying time x throughput (Conair drying manuals, library: oem-dryer-guides).
Mike: old center-flow hoppers need about 1.5-2x; never less than about an hour of residence.
Drying times and limits come from the resin maker; never from memory. Every result is proposed.
"""
import json, sys

OLD_HOPPER = (1.5, 2.0)   # Mike: old center-flow hoppers, only part of the load cycles
MIN_HOURS = 1.0           # Mike: never less than about an hour in the hopper

def check(j):
    base = j['lb_per_hr'] * max(j['drying_hours'], MIN_HOURS)
    old = j.get('hopper_type') == 'old_center_flow'
    need = base * (OLD_HOPPER[0] if old else 1)
    out = {'job': j.get('job', ''), 'hopper_needed_lb': round(need, 1)}
    if old: out['hopper_needed_lb_range_old'] = [round(base * OLD_HOPPER[0]), round(base * OLD_HOPPER[1])]
    if j.get('bulk_density_lb_ft3'):
        out['hopper_needed_ft3'] = round(need / j['bulk_density_lb_ft3'], 2)
    if j.get('hopper_lb') is not None:
        out['hopper_lb'] = j['hopper_lb']
        out['hopper_ok'] = j['hopper_lb'] >= need
        out['residence_hours_at_rate'] = round(j['hopper_lb'] / j['lb_per_hr'], 2)
        if old: out['note_old_hopper'] = 'center flow: only part of the load cycles; confirm with a moisture sample at the throat'
    flags = []
    if j.get('hopper_lb') is not None and j['hopper_lb'] < need:
        flags.append('hopper too small: resin leaves before its drying time')
    if j.get('measured_dew_point_F') is not None and j.get('target_dew_point_F') is not None and j['measured_dew_point_F'] > j['target_dew_point_F']:
        flags.append('measured dew point above target: check desiccant, filter, fan direction (outlet phase)')
    if j.get('dryer_display_dew_point_F') is not None and j.get('measured_dew_point_F') is not None and j['measured_dew_point_F'] - j['dryer_display_dew_point_F'] > 10:
        flags.append("dryer's own meter reads much drier than the tester: don't trust the meter (Mike)")
    if j.get('moisture_pct') is not None and j.get('moisture_limit_pct') is not None and j['moisture_pct'] > j['moisture_limit_pct']:
        flags.append('resin moisture above the maker\'s limit: do not mold')
    if j.get('outlet_phase_ok') is False:
        flags.append('outlet wired reverse phase or bad ground: fix before any dryer is replaced (Mike)')
    out['flags'] = flags
    return out

if __name__ == '__main__':
    data = json.load(open(sys.argv[1]))
    print(json.dumps({'note': 'Proposed. Drying conditions from the resin maker; practice checks are Mike\'s.',
                      'jobs': [check(j) for j in data['jobs']]}, indent=2))
