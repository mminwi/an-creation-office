# Scientific molding: what the published sources say (office search, 2026-10-12)
Background for the b-scientific-molding procedure, before Mike's practice. Read through search results; the office did not open the pages. Vendor sources (RJG sells the method) are marked.

## The usual study sequence
Viscosity (rheology) study, pressure drop, cavity balance, process window, gate seal, cooling time. Sources: plastemart technical paper (https://www.plastemart.com/plastic-technical-articles/casting/1362); PlasticsToday "Robust processing" parts 1-2 (https://www.plasticstoday.com/plastics-processing/robust-processing-part-1-the-aesthetic-dimensional-and-control-process-windows, https://www.plasticstoday.com/plastics-processing/robust-processing-part-2-scientific-molding-and-design-of-experiments); UMass Lowell robust process development seminar.

## Machine qualification first (RJG, vendor)
- Injection speed linearity: inject at slow, medium, fast; actual fill rate = screw travel / fill time vs setpoint; screw acceleration makes it imprecise.
- Load sensitivity: how the machine holds speed when the load changes (air shot via purge or decompression); percent change of fill time and pressure; run at several speeds.
- Check ring (non-return valve) repeatability: listed by RJG; wear and leakage cause process variation; no procedure found.
Sources: https://rjginc.com/3-critical-tests-for-maintaining-part-quality-how-to-uncover-machine-weaknesses-before-they-cost-you/ ; https://pmplastic.com/?p=2077

## Viscosity curve
- Fill to about 95% with zero hold, at many speeds (one author: at least 12 points, slow speeds matter as much as fast); relative viscosity from fill time and plastic pressure at transfer.
- Pick the speed in the flat part of the curve, so machine speed variation barely changes viscosity; more data helps choose within the flat region.
- Keep fill time steady once set: Bozzelli recommends about +/-0.04 s.
- Vents can cap how fast you can fill.
Sources: https://www.ptonline.com/articles/a-new-look-at-evaluating-fill-times-for-injection-molding ; https://www.ptonline.com/articles/is-faster-always-better-when-it-comes-to-injection-molding-fill-times ; https://www.plasticstoday.com/plastics-processing/robust-repeatable-recommendations-fill-time ; Protolabs scientific molding guide.
Not found: a published intensification-ratio formula (machine data; to come from Mike and the press maker).

## Pressure drop
- Peak injection pressure needed should stay under about 80% of the machine's maximum; lower for thick parts that need more pack (Kulkarni, FIMMTECH, on UL Prospector: https://ulprospector.ul.com/1207/pe-plastic-pressure-drop/). Otherwise the process is pressure-limited and fill becomes inconsistent.
- Fill imbalance raises pressure drop and clamp force (Poznan study).

## Cavity balance
- Short-shot weights per cavity show fill balance. One gate seal source wants about 95% balance or better before the gate study. No single accepted tolerance found.

## Gate seal (gate freeze) study
- Fix hold pressure; step hold time up from about 2 s; weigh 3-5 shots per step; plot weight vs hold time; the knee is gate seal.
- Set hold about 10% longer than seal (Bozzelli), or 0.5-1 s longer.
- Keep total cycle constant: add or subtract the hold change from cooling time.
- Hot runners, valve gates and soft materials (polyolefins, TPE, TPU) may never plateau.
- Redo after melt or mold temperature, gate size, back pressure, screw speed or big hold pressure/cycle changes.
- It doesn't tell you if the gate is too shallow or deep.
Sources: https://www.ptonline.com/columns/injection-molding-gate-seal-testing-done-right- ; https://www.ptonline.com/columns/injection-molding-why-how-to-do-gate-seal-experiments ; https://www.ptonline.com/articles/gate-freeze-study-danger-in-a-name ; https://ptonline.com/articles/how-to-optimize-pack-hold-times-for-hot-runner-valve-gated-molds

## Cooling time
- Shortest cooling time without distortion: plot key dimensions vs cooling time (plastemart).

## Process window
- Find the limits of good parts. Amorphous: hold pressure vs melt temperature. Semi-crystalline: hold pressure vs mold temperature (PlasticsToday part 1). DOE for interactions (part 2). Aesthetic, dimensional and control windows.

## Decoupled molding (RJG terms, vendor)
- Decoupled II: fill on velocity to a transfer position, then pack and hold on pressure.
- Decoupled III: velocity-controlled pack too, with transfer to hold on a cavity pressure setpoint; RJG reports a tighter dimensional range.
Sources: https://rjginc.com/injection-molding-process-methods/ ; https://rjginc.com/wp-content/uploads/2019/05/Tolerances-Shrinkage-and-Process-Strategies.pdf ; https://www.plasticsnet.com/doc/decoupled-moldingsm-0001
