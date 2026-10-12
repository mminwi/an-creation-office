"""Basic Six Sigma statistics with the assumptions shown (b-six-sigma). Procedure: guide/sop-six-sigma.txt

Run:  python six_sigma.py <input.json>   (format: example-six-sigma-input.json)
Formulas are the standard ones (NIST/SEMATECH e-Handbook, library: nist-sematech):
  individuals chart: center = mean, limits = mean +/- 2.66 x average moving range (n=2)
  p-chart: limits = pbar +/- 3 sqrt(pbar (1 - pbar) / n) for each subgroup size n
  capability: sigma (within) = average moving range / 1.128; Cp = (USL - LSL) / 6 sigma;
              Cpk = min(USL - mean, mean - LSL) / 3 sigma
Every result lists the assumptions it rests on and what was checked. Results are proposed.
"""
import json, statistics, sys

def runs_check(x, center):
    # Rule: 8 points in a row on one side of the center suggests a shift (a common run rule)
    run, side, worst = 0, 0, 0
    for v in x:
        s = 1 if v > center else -1 if v < center else 0
        run = run + 1 if s == side and s != 0 else (1 if s != 0 else 0); side = s
        worst = max(worst, run)
    return worst

def individuals(x):
    mr = [abs(b - a) for a, b in zip(x, x[1:])]
    mrbar = statistics.mean(mr); c = statistics.mean(x)
    ucl, lcl = c + 2.66 * mrbar, c - 2.66 * mrbar
    out_pts = [i for i, v in enumerate(x) if v > ucl or v < lcl]
    run = runs_check(x, c)
    return {'n': len(x), 'center': round(c, 4), 'ucl': round(ucl, 4), 'lcl': round(lcl, 4),
            'points_outside': out_pts, 'longest_run_one_side': run,
            'in_control': not out_pts and run < 8,
            'assumptions': ['data in time order', 'one value per time period', 'independent from point to point'],
            'checked': f"{len(out_pts)} points outside limits; longest run on one side {run} (8 or more suggests a shift)"}

def p_chart(subgroups):
    d = sum(s['defective'] for s in subgroups); n = sum(s['n'] for s in subgroups); pbar = d / n
    rows = []
    for i, s in enumerate(subgroups):
        p = s['defective'] / s['n']; sd = (pbar * (1 - pbar) / s['n']) ** 0.5
        ucl, lcl = pbar + 3 * sd, max(0.0, pbar - 3 * sd)
        rows.append({'i': i, 'p': round(p, 4), 'lcl': round(lcl, 4), 'ucl': round(ucl, 4), 'out': p > ucl or p < lcl})
    small = [s['n'] for s in subgroups if s['n'] * pbar < 5]
    return {'pbar': round(pbar, 4), 'subgroups': rows, 'out_of_control': [r['i'] for r in rows if r['out']],
            'assumptions': ['each unit is good or bad', 'units independent', 'same chance of defect within a subgroup'],
            'checked': ('n x pbar under 5 in some subgroups: limits are rough, use bigger subgroups' if small else 'n x pbar at least 5 in every subgroup')}

def capability(x, lsl=None, usl=None):
    ind = individuals(x)
    sigma = statistics.mean([abs(b - a) for a, b in zip(x, x[1:])]) / 1.128
    m = statistics.mean(x); out = {'mean': round(m, 4), 'sigma_within': round(sigma, 4)}
    if lsl is not None and usl is not None: out['Cp'] = round((usl - lsl) / (6 * sigma), 2)
    sides = [v for v in [(usl - m) / (3 * sigma) if usl is not None else None, (m - lsl) / (3 * sigma) if lsl is not None else None] if v is not None]
    if sides: out['Cpk'] = round(min(sides), 2)
    out['assumptions'] = ['process in control (checked with the individuals chart)', 'roughly normal data', 'measurement system adequate (MSA)']
    out['checked'] = 'in control' if ind['in_control'] else 'NOT in control: capability numbers are not meaningful until the process is stable'
    try:
        q = statistics.quantiles(x, n=4); iqr = q[2] - q[0]
        out['normality_hint'] = f'IQR/sigma = {iqr / statistics.stdev(x):.2f} (about 1.35 for normal data); check a histogram'
    except statistics.StatisticsError:
        pass
    return out

if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    res = {'note': 'Proposed. ' + d.get('study', '')}
    if 'individuals' in d: res['individuals'] = individuals(d['individuals'])
    if 'p_chart' in d: res['p_chart'] = p_chart(d['p_chart'])
    if 'capability' in d:
        c = d['capability']; res['capability'] = capability(c['data'], c.get('lsl'), c.get('usl'))
    print(json.dumps(res, indent=2))
