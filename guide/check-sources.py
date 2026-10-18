#!/usr/bin/env python3
"""check-sources.py: the source check for the AN Creation office.

Usage: python3 check-sources.py <folder or csv> [...]

Reads every .csv under the folders given. A sheet is checked when it has a
"Source status" column (any capitalization). Each row is listed when it has
no source, a memory-type source, a status that is not allowed, a status that
still needs work, or is marked critical and not checked. Procedure:
https://ancreationoffice.com/sop-source-check.txt
Exit code 1 when anything blocking is found, 0 otherwise.
"""
import csv
import pathlib
import re
import sys

USABLE = {"checked", "measured", "quote", "inventor said"}
OPEN = {"from source, not checked", "from a summary", "to find"}
MEMORY = re.compile(r"\b(ai|memory|general knowledge|typical(ly)?|standard practice|commonly|chatgpt|grok|claude)\b", re.I)


def col(header, *names):
    low = [h.strip().lower() for h in header]
    for n in names:
        if n in low:
            return low.index(n)
    return None


def check(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    head = rows[0]
    st = col(head, "source status")
    if st is None:
        return None, None
    src = col(head, "source")
    on = col(head, "checked on")
    quote = col(head, "source text")
    crit = col(head, "critical")
    rid = 0
    blocking, open_rows = [], []
    for n, r in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in r):
            continue
        get = lambda i: r[i].strip() if i is not None and i < len(r) else ""
        label = f"{path}:{n} {get(rid)[:40]}"
        status = get(st).lower()
        source = get(src)
        critical = get(crit).lower() == "yes"
        if not source:
            blocking.append(f"{label}: no source")
        elif MEMORY.search(source):
            blocking.append(f"{label}: source is memory or general knowledge ({source[:40]}); status must be 'to find'")
        if status not in USABLE | OPEN:
            blocking.append(f"{label}: status '{get(st)}' is not one of the allowed words")
        elif status == "checked":
            if on is not None and not get(on):
                blocking.append(f"{label}: checked, but no 'Checked on' date")
            if quote is not None and not get(quote):
                blocking.append(f"{label}: checked, but no quoted source text")
        elif status in OPEN:
            if critical:
                blocking.append(f"{label}: critical and still '{status}'")
            else:
                open_rows.append(f"{label}: {status}")
    return blocking, open_rows


def main(args):
    if not args:
        print(__doc__)
        return 2
    files = []
    for a in args:
        p = pathlib.Path(a)
        files += sorted(p.rglob("*.csv")) if p.is_dir() else [p]
    blocking, open_rows, sheets = [], [], 0
    for f in files:
        b, o = check(f)
        if b is None:
            continue
        sheets += 1
        blocking += b
        open_rows += o
    print(f"Source check: {sheets} sheet(s) with a Source status column.")
    if blocking:
        print(f"\nMUST FIX before anything is built, bought, tested or filed on it ({len(blocking)}):")
        print("\n".join("- " + x for x in blocking))
    if open_rows:
        print(f"\nSTILL OPEN, fine for planning ({len(open_rows)}):")
        print("\n".join("- " + x for x in open_rows))
    if not blocking and not open_rows:
        print("Every row is traced and checked.")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
