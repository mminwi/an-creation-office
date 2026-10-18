#!/usr/bin/env python3
"""tax-year.py: the year-end summary of the business record, for the accountant.

Usage: python3 tax-year.py <Business folder> <year> [--mile-rate RATE --rate-source "where the rate came from"]

Reads expenses.csv and trips.csv in the folder (templates on the site) and
writes tax-year-<year>.txt next to them: totals by tax category and by whose
money, business miles, and every row that is missing what the record needs
(receipt, business purpose, category, miles). It does not decide what is
deductible; the accountant does. A mileage rate is only used with its source
(the IRS notice or page for that year), never a remembered number.
Procedure: https://ancreationoffice.com/sop-business-record.txt
"""
import argparse
import csv
import datetime
import pathlib
import sys
from collections import defaultdict


def read(path):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


def money(x):
    try:
        return float(str(x).replace("$", "").replace(",", "").strip() or 0)
    except ValueError:
        return None


def days_late(row):
    try:
        d = datetime.date.fromisoformat(row.get("date", "").strip())
        l = datetime.date.fromisoformat(row.get("logged on", "").strip())
        return (l - d).days
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("year")
    ap.add_argument("--mile-rate", type=float)
    ap.add_argument("--rate-source")
    a = ap.parse_args()
    if a.mile_rate is not None and not a.rate_source:
        sys.exit("A mileage rate needs --rate-source: the IRS notice or page for that year, as read (sop-source-check.txt).")
    folder = pathlib.Path(a.folder)
    exp = [r for r in read(folder / "expenses.csv") if r.get("date", "").startswith(a.year)]
    trips = [r for r in read(folder / "trips.csv") if r.get("date", "").startswith(a.year)]

    by_cat, by_from, gaps = defaultdict(float), defaultdict(float), []
    total = 0.0
    for r in exp:
        label = f"{r.get('date')} {r.get('paid to', '')}: {r.get('what it was', '')[:50]}"
        amt = money(r.get("amount"))
        if amt is None:
            gaps.append(f"{label}: amount is not a number ({r.get('amount')})")
            continue
        total += amt
        cat = (r.get("tax category") or "").strip() or "no category yet"
        by_cat[cat] += amt
        by_from[(r.get("paid from") or "").strip() or "not said"] += amt
        if cat in ("no category yet", "ask accountant"):
            gaps.append(f"{label}: tax category is '{cat}'")
        if not (r.get("receipt file") or "").strip():
            gaps.append(f"{label}: no receipt file")
        if not (r.get("business purpose") or "").strip():
            gaps.append(f"{label}: no business purpose")
        late = days_late(r)
        if late is not None and late > 7:
            gaps.append(f"{label}: logged {late} days after it happened")

    miles, park = 0.0, 0.0
    odometer = [r for r in trips if r.get("trip", "").upper().startswith("ODO")]
    for r in trips:
        if r in odometer:
            continue
        label = f"{r.get('date')} {r.get('trip')}: {r.get('to (place and address)', '')[:40]}"
        m = money(r.get("business miles"))
        if not m:
            gaps.append(f"{label}: no business miles")
        else:
            miles += m
        park += money(r.get("parking and tolls")) or 0
        if not (r.get("business purpose") or "").strip():
            gaps.append(f"{label}: no business purpose")
        late = days_late(r)
        if late is not None and late > 7:
            gaps.append(f"{label}: logged {late} days after the trip")
    if trips and not odometer:
        gaps.append(f"No odometer row for {a.year} in trips.csv")

    out = [f"Business record, tax year {a.year}. Built {datetime.date.today()} by tax-year.py from expenses.csv and trips.csv.",
           "For the accountant: this sorts the record; it does not decide what is deductible.", "",
           f"EXPENSES: {len(exp)} rows, ${total:,.2f}", "By tax category:"]
    out += [f"  {k}: ${v:,.2f}" for k, v in sorted(by_cat.items())]
    out += ["By whose money:"] + [f"  {k}: ${v:,.2f}" for k, v in sorted(by_from.items())]
    out += ["", f"TRIPS: {len(trips) - len(odometer)} trips, {miles:,.1f} business miles, ${park:,.2f} parking and tolls",
            "Odometer rows: " + ("; ".join(f"{r.get('date')} {r.get('start odometer') or r.get('end odometer') or '(no reading)'}" for r in odometer) or "none")]
    if a.mile_rate is not None:
        out.append(f"At {a.mile_rate} per mile ({a.rate_source}): ${miles * a.mile_rate:,.2f}")
    else:
        out.append("No mileage rate applied: look up that year's IRS standard mileage rate and rerun with --mile-rate and --rate-source.")
    out += ["", f"GAPS TO CLOSE BEFORE TAX TIME ({len(gaps)}):"] + ([f"- {g}" for g in gaps] or ["- none"])
    text = "\n".join(out) + "\n"
    (folder / f"tax-year-{a.year}.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
