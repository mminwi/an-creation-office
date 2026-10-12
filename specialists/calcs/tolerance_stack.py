"""Linear tolerance stack: worst case, RSS and Monte Carlo (b-tolerance-gdt). Procedure: guide/sop-tolerance-stack.txt

Run:  python tolerance_stack.py <input.json>   (format: example-stack-input.json)
Each dimension in the loop: nominal, +tol, -tol, direction (+1 or -1 around the loop).
Worst case: every part at its worst limit at once; guarantees assembly.
RSS: root-sum-square of the tolerances; assumes independent, roughly normal, centered parts.
Monte Carlo: random parts (normal, tolerance = 3 sigma by default, or uniform); reports the share outside the gap limits.
Standard methods (ASME Y14.5 sets the drawing language; the stack math is general). Results are proposed.
"""
import json, math, random, statistics, sys

def stack(d, n=100000, seed=1):
    dims = d['dims']
    nom = sum(x['dir'] * x['nominal'] for x in dims)
    # convert unequal tolerances to mean shift + symmetric half-tolerance
    mids = [x['dir'] * (x['plus'] - x['minus']) / 2 for x in dims]
    halves = [(x['plus'] + x['minus']) / 2 for x in dims]
    center = nom + sum(mids)
    wc = sum(halves)
    rss = math.sqrt(sum(h * h for h in halves))
    rnd = random.Random(seed)
    dist = d.get('distribution', 'normal'); k = d.get('sigma_per_tol', 3)
    samples = []
    for _ in range(n):
        g = 0.0
        for x, m, h in zip(dims, mids, halves):
            dev = rnd.gauss(0, h / k) if dist == 'normal' else rnd.uniform(-h, h)
            g += x['dir'] * x['nominal'] + m + dev
        samples.append(g)
    out = {'nominal_gap': round(nom, 4), 'mean_gap': round(center, 4),
           'worst_case': [round(center - wc, 4), round(center + wc, 4)],
           'rss': [round(center - rss, 4), round(center + rss, 4)],
           'monte_carlo': {'n': n, 'distribution': dist, 'min': round(min(samples), 4), 'max': round(max(samples), 4),
                           'sd': round(statistics.pstdev(samples), 5)}}
    lo, hi = d.get('gap_min'), d.get('gap_max')
    if lo is not None or hi is not None:
        bad = sum(1 for s in samples if (lo is not None and s < lo) or (hi is not None and s > hi))
        out['monte_carlo']['pct_outside_limits'] = round(bad / n * 100, 3)
        out['worst_case_ok'] = (lo is None or center - wc >= lo) and (hi is None or center + wc <= hi)
        out['rss_ok'] = (lo is None or center - rss >= lo) and (hi is None or center + rss <= hi)
    out['contributors'] = sorted(({'name': x['name'], 'share_of_variance_pct': round(h * h / (rss * rss) * 100, 1)} for x, h in zip(dims, halves)), key=lambda c: -c['share_of_variance_pct'])
    out['assumptions'] = ['1D loop; all dimensions along one axis', 'parts independent', f'Monte Carlo: {dist}, tolerance = {k} sigma' if dist == 'normal' else 'Monte Carlo: uniform within tolerance', 'plastic parts: include shrink and warp variation in the tolerances']
    return out

if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    print(json.dumps({'note': 'Proposed. ' + d.get('stack', '')} | stack(d), indent=2))
