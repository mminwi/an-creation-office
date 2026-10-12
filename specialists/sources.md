# Sources pass, part 1 (2026-10-12)

## What was done
- roles.csv: every role (37) with its specialist name, tier, first-look role, what it does, the procedures it uses (guide/ files), the library sources it uses (ids in guide/resources.json), new sources it needs, who it works with and who it hands off to.
- All 220 entries in the existing library are mapped to at least one role. Two roles were added because the library already had sources nobody owned: b-retail (Amazon, Walmart, Lowe's) and b-gov-contracting (SAM, military standards, DLA).
- Renamed, per Mike: no "engineer" anywhere in names. Sourcing is now b-purchasing (Purchasing Specialist); Manufacturing Engineering is b-manufacturing (Manufacturing Specialist); the first-look role b-mechanical is now b-design (Product Design Specialist).
- sources-new.csv: 73 sources the roles need that the library doesn't have (standards, regulations, handbooks), each with publisher, where to find it, and which roles use it.

## What was not done, and why
None of the 73 new sources has been read. The cloud container this ran in blocks the publishers' sites (nfpa.org and ecfr.gov were refused on 2026-10-12), so every row says "not read". Their link, edition and "what it asks" columns are blank on purpose: the office never fills them from memory.
To finish: run part 2 from a tool that can open the publishers' sites (Cursor's cloud agent, or this environment with those sites allowed), one row at a time: open the official page, record the link, the current edition, the date, and a few lines of what it asks. A page that blocks automated readers is marked "not read: the site blocks automated access" with the date (analyst.txt).
When a row is read, it moves into guide/resources.json with the same fields as the existing entries, and roles.csv points to it.

## Gaps the map shows
Roles with no procedure yet (they have sources, but no written way of working):
- b-cooling-water: heat load, flow per circuit (turbulent check), temperature rise across the mold, chiller and tower sizing, water treatment. All calculation; a strong first procedure because it is Mike's deep area and the results can be checked.
- b-drying-handling: dryer sizing, residence time, moisture, regrind.
- b-six-sigma: a DMAIC procedure with tollgates and the forms (charter, SIPOC, data collection plan, MSA, capability, control plan).
- b-machine-safety: risk assessment and guarding procedure.
Roles with nothing in the existing library (only new sources, all unread): b-scientific-molding, b-cooling-water, b-drying-handling.
Calculations no role has yet, to be written as code with results marked proposed: tolerance stack (worst case, RSS, Monte Carlo); mold cooling heat load and flow; molded part cost (cycle, press rate, resin, scrap); battery energy from a power budget; process capability (Cp, Cpk).

## Suggested order
1. Part 2 of the sources pass (read the 73), from a tool that can reach the sites.
2. The b-cooling-water procedure and its calculation, Mike reviews it against his experience.
3. b-six-sigma (DMAIC), then b-scientific-molding.
