"""Regrind generations at steady state (b-drying-handling). Procedure: guide/sop-drying.txt, section 7.

Run:  python regrind.py 25 50 60      (regrind percentages)
Mike's table: "if I run it at 60%, how much resin is really running third and fourth generation?"
Math (steady state, all regrind from the same running job fed back continuously): with regrind
fraction r, the share of the feed that has been through the press k times before is (1 - r) * r**k.
Generation 0 is virgin. Average heat histories before this shot = r / (1 - r).
"""
import sys

def table(pct, show=5):
    r = pct / 100
    rows = [(k, (1 - r) * r ** k) for k in range(show)]
    rest = r ** show                       # share that is generation >= show
    return rows, rest, r / (1 - r) if r < 1 else float('inf')

if __name__ == '__main__':
    for a in sys.argv[1:] or ['25', '50', '60']:
        rows, rest, avg = table(float(a))
        print(f'Regrind {float(a):g}%: average {avg:.2f} earlier passes per pellet')
        for k, f in rows:
            label = 'virgin' if k == 0 else f'generation {k}'
            print(f'  {label:<14} {f*100:5.1f}%')
        print(f'  generation {len(rows)}+   {rest*100:5.1f}%')
        r = float(a) / 100
        print(f'  generation 3 and older: {r**3*100:.1f}% of everything going through the press, {r**2*100:.1f}% of the regrind itself')
        print()
