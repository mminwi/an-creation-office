---
name: an-molding-process
description: "Use for molding process work: scientific molding, cooling water, drying and regrind."
---

# an-molding-process

Sections: Scientific molding: setting a robust process (b-scientific-molding); Mold cooling water (b-cooling-water); Resin drying and handling (b-drying-handling).

## Scientific molding: setting a robust process (b-scientific-molding)
(procedure file: sop-scientific-molding.txt)

Procedure: Scientific molding: setting a robust process (b-scientific-molding). Revision 8 — October 18, 2026. Cavity balance, process sheet, gate seal step-down, speed limits and DOE added from Mike's notes.
Index: the procedure index in `an-office`
Source: Mike's practice (Mike's notes, kept private), with the published methods as background (specialists/research/261012-scientific-molding-search.md). Lines marked "Mike" are his practice; "published" lines cite their source; "office" lines are the office's. Tier: deep.
Read this when a new mold is being sampled or qualified, a process drifts or makes scrap, parts crack or warp, a mold moves to another press, or someone wants to buy process monitoring. Calculations: https://github.com/mminwi/an-creation-office/blob/main/specialists/calcs/scientific_molding.py. Related: `an-molding-process` (Mold cooling water (b-cooling-water)) (cooling, hot spots), `an-molding-process` (Resin drying and handling (b-drying-handling)) (wet resin makes every study wrong).

WHAT IT IS, AND WHAT IT ISN'T (Mike)
- Scientific molding, decoupled molding and the other names are good molding practice with principles behind each setting. It is not difficult, and it does not need new equipment or monitoring on every press.
- Much of what is sold under these names is equipment or consulting. Monitoring can help management see what is going on, and it raises alarms; it is not needed to run a good process. Weigh that before recommending a purchase.
- What is needed: people who are taught the principles, not the loudest person in the plant passing on what he made up. Teach the techs why each setting is what it is, and give them feedback: what is good, what is bad, and how we are getting there.
- None of it is new (Mike). The methods came out of the resin makers in the 1950s and 60s, working out how to process their new resins; the courses and books since teach the same principles in different ways. Devices that rotate the melt where a runner splits have their place, but molders balanced runners by layout before they existed; weigh the cost before adding one to a mold.
- "Non-Newtonian" just means shear thinning: the harder you push the plastic, the thinner it gets and the easier it pushes. Nothing magic.

0. BEFORE ANY STUDY
- Dry resin, tested (`an-molding-process` (Resin drying and handling (b-drying-handling))). Balanced cooling with flow and temperatures checked (`an-molding-process` (Mold cooling water (b-cooling-water))). A study on wet resin or an unbalanced mold measures the wrong thing.

1. THE PRESS: DOES IT DO WHAT IT IS TOLD? (Mike)
- Modern presses are much better than the bad ones of the 1980s and 90s, so this is less of an issue than it was. Old, unmaintained presses still fail it.
- Speed: set 3 in/s, does it run 3 in/s? Watch for maintenance that "fixed" a press by dialing the pots back, so it never reaches the set speed (set 3 runs 2; Mike has seen set 1 run 2). Check: fill time at several set speeds; actual speed = screw travel / fill time (published: RJG, the injection speed linearity test).
- Pressure: set 900 psi pack, does it hold 900 psi?
- Check ring: dirt or gunk keeps it from seating, resin pushes back past it during injection, and shot-to-shot repeatability is gone (published: check ring repeatability, RJG).
- Office: RJG's "load sensitivity" test is a press test: how well the press holds its set speed when the load (melt viscosity) changes. Mike uses the phrase for finding the insensitive middle of the process window (section 6); both are kept, with their names.

2. FILL SPEED AND THE VISCOSITY CURVE (Mike)
- Fill as fast as the press allows, in a controlled way. The faster it goes in, the thinner the melt, the more even the pressure across the part, and the less strain left in the resin. Mike has very rarely seen "too fast"; the real limit is being able to stop (transfer) under control.
- "As fast as the press allows" means about 90% of the press's maximum injection speed (the screw's forward speed), not 100% (Mike). At 100% the valves are wide open and the closed loop has nothing left to control with; speed then varies at the mercy of the plastic. At about 90% the press can open and close its valving to hold the set speed. Running wide open is the old-school way, and wrong on a servo machine. Going up to 95-96% is fine if you know the trade: the press has little left to open, so if the speed sags it can barely react.
- On almost any typical press, as fast as it will run (up to about 90%) is simply fine (Mike).
- Where too fast shows up: high-speed presses with lots of accumulator bottles. Watch for burning and venting problems (the air can't get out fast enough), and color burns where shear heating at one point in the mold burns out a color (Mike's example: an orange that burns out past a certain point). Too fast shows up as heat.
- The other limit: overheating the plastic with shear, especially through a choke point (small gate, restriction). The viscosity curve shows how fast this press can fill to get most of the shear-thinning benefit without that.
- Published method: fill to about 95% with no hold, at a series of speeds from fastest down until fill time passes about 10 s; relative shear rate = 1 / fill time; relative viscosity = hydraulic pressure at transfer x intensification ratio x fill time; pick a speed on the flat part of the curve, where pressure changes less than about 10% (Plastics Technology; Entec Polymers). Hold fill time steady once set, about +/-0.04 s (Bozzelli).
- Office: the intensification ratio is the press's ratio of plastic pressure to hydraulic pressure, from the press maker (electric presses read plastic pressure directly; use ratio 1).

3. PRESSURE DROP ACROSS THE PART (Mike)
- Measure the drop from where the plastic enters the cavity to the last place to fill. Fast fill keeps it small (Mike's example: about 200 psi gate to edge); slow fill can double or triple it.
- Why it matters: a big drop means the part is packed hard at the gate and barely packed at the far edges. The lightly packed areas shrink much more than the gate area, and that difference is built-in stress and warp. Minimize the drop.
- Hot spots in the mold act the same way: a hotter area holds expanded plastic when the gate freezes, then shrinks more than the area around it. Run the whole mold at one temperature (`an-molding-process` (Mold cooling water (b-cooling-water))).
- Published: the peak pressure the process needs should stay under about 80% of the press's maximum, lower for thick parts that need more pack; otherwise the process is pressure-limited and fill becomes inconsistent (Kulkarni, FIMMTECH).

4. CAVITY BALANCE (Mike)
- Molds should be built naturally balanced (H runners, geometrically balanced runner systems). A mold that isn't naturally balanced will have problems.
- The common real cause: a hot runner drop where one heater is off: a cold tip with a hot base, so that gate freezes off early. Raising that drop about 5 F during a run can rebalance the fill. That is a fix for the run, not the cure.
- After the run: maintain the heaters. Swap heaters between drops: if the problem moves with the heater, it is the heater; if it stays with the mold, check that every cavity and gate has the same geometry.
- Be ready to tear down the manifold, measure everything with calipers, micrometers and pin gauges, and be exacting.
- Long runner systems: when gates on one runner system are more than about 3 feet apart (runners over 2-3 feet), the hot runner maker's standard tolerances may be too loose. Specify tighter ones up front.
- What good balance looks like (Mike): almost perfect. On an end-of-fill short shot every cavity is better than 90% complete, with no noticeable gap between them, and all of them a little light at their last place to fill. The system can't build pressure until the whole mold is full, so if one cavity is short they should all be just underpacked at the end of fill. If they are, you're okay.
- Measure it with short-shot weights per cavity against a full part's weight (the calculation flags any cavity under 90%, and a noticeable spread).

5. GATE SEAL AND HOLD (Mike)
- Hold pressure until the gate freezes. If pressure comes off while the gate is open, plastic flows back out, the hot gate area sits at low pressure and shrinks, and the plastic around the gate is stretched. Parts used outdoors crack around the gate after a couple of years of heat and cold cycles.
- Hold pressure does not have to be injection pressure; it is often lower. Adjust it and see what works.
- Gate seal time sets when the pressure can come off, when screw recovery for the next shot can start, and, by most people's count, when cooling time begins.
- Mike's method, and the one to use on hot runners and valve gates (where the weight curve may never level off): establish the whole process first. Keep pack pressure, then step the pack/hold time down (10 s, 9 s, 8 s, ...). The first step where the part comes out lighter means the gate wasn't sealed yet; go back to the previous time. That is the gate seal time, and it sets the pack time.
- Published method: fix hold pressure; step hold time up from about 2 s; weigh 3-5 shots per step; plot weight against hold time; the knee is gate seal; set hold about 10% longer (Bozzelli) or 0.5-1 s longer; keep total cycle constant by taking the change out of cooling time. Hot runners, valve gates and soft resins (polyolefins, TPE, TPU) may never level off. Redo after changes to melt or mold temperature, gate size, back pressure, screw speed or a big change in hold pressure.

6. THE PROCESS WINDOW: RUN IN THE MIDDLE (Mike)
- Find the range that makes good parts and run in the middle of it, where ordinary variation can't push you out. Mike's example: good parts from 600 to 1000 psi pack. At 950 you are one swing from overpacking; at about 800 you are insensitive to both over- and underpacking.
- Published: windows are typically mapped as hold pressure against melt temperature (amorphous resins) or against mold temperature (semi-crystalline), with DOE to catch interactions (PlasticsToday, Robust processing).
- DOE, with caution (Mike): he has run many and rarely uses them for this. They are a tool with a place, but in a molding plant the noise often drowns the answer: resin lot to lot, humidity, seasonal temperature, plants that aren't air conditioned, sun on one side of a silo. A DOE is often too fine a magnifying glass for real-world molding: a 20 psi pack change either way is hard to read through that noise, and it is easy to load in too many factors. DOE suits machining and simpler processes better. Before trusting one: have the process under control and look hard at everything else that could be moving it.
- Seasons move the process (Mike): resin from an outside silo can arrive at the press at about 120 F in summer sun and 32 F in winter, and humidity adds moisture that thins the melt, worse if the dryers aren't good. Expect a summer process and a winter process; a setpoint in the middle of the window is what survives both.

7. COOLING TIME (Mike)
- Keep checking it. Cool the part below the temperature where it takes a set: above it, any warp from ejection stays. Mike's numbers: polypropylene about 180 F, polyethylene about 160 F. Office: confirm each resin's number with its maker (heat deflection data).
- With uniform cooling (lots of water, evenly) parts can come out fairly warm: 120 to 140 F is good for polyolefins. PVC, nylons and some engineered resins often eject that warm or warmer.
- Part cost is set by how fast you can melt the plastic, get the heat out of the mold and the part, and make the next shot. That is where you make money or don't.
- Published: the cooling time study plots key dimensions against cooling time and takes the shortest time before they move.

8. THE PROCESS SHEET: LOCK THE CYCLE THE RESIN SEES (Mike)
- The process sheet (setup sheet) carries the entire setup: every setpoint. More and more presses save it; keep the sheet anyway.
- Lock everything the plastic sees: screw speed and injection speeds, all heats, pack and hold pressures and times, cooling time, valve gate open and close timing. If the resin sat still for this long last time, it sits still this long next time; if it saw this pack pressure, it sees it again.
- Change the cycle for the press if you must, never the cycle for the resin. Clamp moves can be a little faster here and slower there as long as total clamp open and closed time stays the same. Mold slowdown position belongs on the safe setup but rarely matters to the part.
- Monitoring checks actuals, not setpoints: actual cycle time, actual injection (fill) time, actual cooling, against the sheet. Checking a setpoint you typed tells you nothing.
- This works with one good resin. With several approved resins for one grade (Mike: e.g. six approved polyethylenes), or resin fed from silos where batches stack, expect some tweaking: the process sheet loosens, and checks lean more on part quality and part measurements than on the process numbers.

WHAT THE WORK PRODUCES
A process development record per mold and press, in its own dated folder: press checks (speed, pressure, check ring), viscosity curve and the chosen fill time, pressure drop by section, cavity balance with causes and fixes, gate seal curve and the chosen hold, the process window and where the setpoint sits in it, cooling time and ejection temperature, and the process sheet. Every setting carries its reason.

HANDS OFF
Hot runner maker (heaters, tolerances), tool shop (gates, geometry), press maker or service (speed, pressure, check ring), resin maker (temperatures, set temperature).

OPEN FOR MIKE
- Nothing open. (Window width: no fixed number from Mike; the rule is to run in the middle so seasonal and resin variation can't push the process out.)

## Mold cooling water (b-cooling-water)
(procedure file: sop-cooling-water.txt)

Procedure: Mold cooling water (b-cooling-water). Revision 10 — October 18, 2026. Plant sizing, the looped header, and towers and outdoor units added from Mike's notes; hydraulic and feed throat allowances from published chiller-maker guidance.
Index: the procedure index in `an-office`
Source: Mike's practice from years of building and running injection molds (Mike's notes, kept private). Lines marked "Mike" are his practice; lines marked "physics" are standard heat transfer; anything else the office adds is marked "office". Tier: deep.
Read this when a mold is being designed or quoted, a mold runs hot, cycles long, warps, sticks, binds or galls, or a plant is sizing chillers, towers or pumps. Calculation: https://github.com/mminwi/an-creation-office/blob/main/specialists/calcs/cooling_water.py (input format: example-cooling-input.json).

WHY IT MATTERS
Cooling water is usually the biggest factor in molded part cost, and often in part quality (Mike). Most of the cycle is cooling time, and uneven cooling shows up as warp, sink, sticking and dimensional spread. The goal is not "more water"; it is balanced cooling: every area of the mold giving up its heat at the same rate.

WHAT TO ASK FOR (a cooling review needs these; unknowns become questions)
- The part: resin and grade, wall thickness, shot weight, the corners and deep areas.
- The mold: steel type, any inserts (beryllium copper such as MoldMax, aluminum), every water circuit with its line size, how circuits are hooked up (single or looped), bubblers and baffles, slides, lifters, cores.
- The process: cycle time and how much of it is cooling, mold temperature setting.
- The measurements: flow per circuit (gpm) and water temperature in and out of each circuit. If the plant has no flow meters, that is the first finding.
- The resin supplier's heat content from melt to ejection (BTU/lb), for the heat load. Never filled from memory.

1. WHERE THE HEAT GOES (mold design)
- The core side does most of the cooling (Mike). Plastic shrinks onto the core and pulls away from the cavity, so cavity-side cooling is partly cut off. Put the cooling effort, and the conductive materials, on the core.
- Balance by conductivity, not only by water (Mike). Count how many hot plastic faces feed heat into each area of steel:
  - One face: steel with normal water.
  - Two faces meeting (an edge or a corner of a box): a more conductive insert, such as MoldMax (beryllium copper), on the core.
  - Three faces meeting (the bottom corner of a box or pan): three units of heat into one spot. An aluminum core cap there pulls the most heat out. The gate is often at that spot too, and aluminum's poor wear resistance does not matter on a core cap.
- Office: beryllium copper dust from grinding or machining is a health hazard; the tool shop follows its beryllium handling rules. Aluminum wears; keep it off shut-offs and sliding faces.

2. WATER INTO EVERYTHING THAT MOVES
- Get water into every component, especially small cores, slides, lifters and the plates behind them (Mike). If it can't reach the front, water the back end anyway: even a bubbler hitting the back of a lifter, or a line through the back plate, gives the heat a way out.
- Why: heat does not cross a sliding fit (ways, gibs, slides) well, and a little corrosion on those faces stops it entirely. An uncooled moving part heats up, grows, binds and galls; you see grinding in the ways and splay in the parts (Mike).
- Ejector pins are the accepted exception: they usually can't be cooled.

3. CIRCUITS
- Keep circuits short (Mike). Short lines pass water well.
- Loop where it makes sense; don't single-circuit everything (Mike). A straight-through line, especially in aluminum, moves a lot of heat and can share its water with a second circuit. Watering every line on its own wastes flow.
- Find the restrictive circuit and give it its own water (Mike). It is usually the one with a bubbler or baffle, and it is the one people loop. That line may only pass about 2 gpm on its own, and the tool needs all of it.
- Judge each loop by flow through it against heat it must remove (calculation below).

4. FLOW
- A standard line, on a 200 to 300 ton mold, is drilled 7/16 in with 3/8 in pipe fittings; some molds use 1/2 in holes (Mike).
- Target about 3 to 4 gpm through a standard line (Mike). That is about as good as cooling gets; more flow adds turbulence but little cooling.
- Don't swing to the other extreme (Mike). Plants that are starved for water often add big pumps and big hoses; at about 9 to 10 gpm through a standard line the water starts eroding the line, aluminum worst of all.
- Physics: the flow must be turbulent (Reynolds number above about 4,000) to carry heat well; the calculation reports it for every circuit, with the velocity.
- Physics, for a 7/16 in line: 3.5 gpm is about 7.5 ft/s and well turbulent (Reynolds about 22,000 in 60 F water); 9.5 gpm is about 20 ft/s. So 3 to 4 gpm is already well past the turbulence a line needs, which fits Mike's point that more flow buys little cooling.

5. MEASURE
- Buy flow meters, ideally with temperature sensors, on every circuit (Mike). Put the temperature on the water coming out of the mold.
- Water out vs water in, per circuit (Mike; degrees F):
  - More than about 5 degrees: take a serious look at that circuit.
  - Within a degree or two on each line: perfect, and usually reachable.
  - The entire mold running within a degree or two: world class.
- Physics: heat removed by a circuit = 500 x gpm x (out - in) in BTU/hr. A circuit with a big rise is working hard and is short of water; a circuit with almost no rise may have more water than it needs, which could go to a starved one.

6. THE CALCULATION (https://github.com/mminwi/an-creation-office/blob/main/specialists/calcs/cooling_water.py)
Input per mold: shot weight, cycle, the resin's heat content from melt to ejection (from the supplier), and per circuit: line size, gpm, water in and out, insert material.
Output per circuit: velocity, Reynolds number, temperature rise, heat removed, and flags (below 3-4 gpm, 9+ gpm erosion, not turbulent, over 5 degrees, within 2 degrees). Per mold: heat from the plastic (from an enthalpy number, or specific heat with melt and ejection temperatures), heat carried by the water, the total gpm needed for a target rise, and tons (BTU/hr / 12,000). Plant mode: see section 7. Every number is marked proposed.

7. PLANT WATER: SIZING CHILLERS AND PUMPS (Mike)
Mold heat load, by pounds:
- For each press, take its worst job: the heaviest pounds per hour (parts per hour x part weight). A packaging plant with a few materials can do this straight from throughput, for example 500 lb/hr.
- Heat per pound = from melt temperature down to ejection, for example from about 350 F to under 150 F. Office: the heat per pound comes from the resin supplier (specific heat over that range, plus the heat of crystallization for semi-crystalline resins, or one enthalpy number); never from memory.
- Worst-case plant load = every press running its worst job at once. Size for that worst case (Mike).
Three units, two running:
- Split the worst case over three chillers and three pump sets, each about a third (Mike).
- Typical load is about two thirds, so two units run and the third is the backup. Running everything at once is rare (Mike recalls about two weeks near 100% in his career).
- Rotate them: when a pump or chiller cycles off and comes back, the next one in line starts (lead rotation), so all three run regularly and you know each one works (Mike).
- Maintenance: one unit can come off line without shutting the plant down (Mike).
- Chillers run best with about a 10 F rise across the chiller, even while the molds run at 2 to 5 F rise; the return water is a bit warmer and the chiller runs more efficiently. Two chillers at part load run better than units pushed to their limit (Mike).
Header piping: run it in a loop (Mike, highly recommended):
- From the pump tank, take the supply out to the floor, tee it, and run one branch each way around the plant so the two meet on the far side. The split can be right after the pumps or where the header reaches the production floor; the loop around the floor is the part that matters.
- Why: demand is never even. Some areas are shut down, one side pulls more than the other. A dead-end header has to be oversized to get enough water to the far end; a loop feeds every press from both directions, so the pressure stays steady and the last press in the row does not see the drop.
- It also lets you close off one section of the loop to add a press, clean a line or repair it, while the rest of the plant keeps running. Office: that needs isolation valves between sections of the loop; place them so any one section can be closed with both directions still feeding the rest.
Towers and outdoor units (Mike):
- In Mike's plants the cooling tower cooled the chillers (it takes away the chillers' heat). Air-cooled chillers work too, but they also need regular cleaning; they pick up whatever is in the air.
- Get towers and air-cooled chillers off the ground. Below about 8 feet the air carries dust, dirt and, in farm country at planting and harvest, a haze of organics. A tower or an air-cooled coil acts like an air filter: it fills with dirt and organics, and then it is cleaning and water treatment from then on.
- Best: on the roof. If not, on a stand about 10 feet tall. Two or three feet up is not enough.
- Height also keeps people from fiddling with them: at 10 feet it takes a lift to reach them.
- Filter, filter, filter: everything should be filtered as much as possible (Mike). On a tower, add a bag filter system on a separate side set. At certain times of year the bags need cleaning daily, so the filters need something that shows clearly when they are loading up. Office: a pressure gauge on each side of the filter (differential pressure) is the usual way to see that.
- Office: plan safe access for the service people (lift, platform, fall protection), and keep the tower on its water treatment and Legionella program (ASHRAE 188, Guideline 12).
Tower size and climate (Mike):
- Size the tower at about 1.25 to 1.5 times the chiller capacity (Mike).
- Units, so it isn't counted twice (Perplexity answer Mike pasted, consistent with the physics): the tower rejects the chillers' load plus the compressors' heat, about 1.25 times the chiller load. A chiller ton is 12,000 BTU/hr; a nominal cooling-tower ton is 15,000 BTU/hr, which already includes that 1.25. So Mike's 1.25-1.5x in chiller tons equals about 1.0-1.2 nominal tower tons per chiller ton. Never multiply a tower-ton rating by 1.25 again.
- Nominal tower ratings assume set conditions (reported as 95 F water in, 85 F out, 78 F outdoor wet-bulb; via Perplexity, confirm on the tower maker's data). Size from the chiller's stated condenser heat rejection at the site's design wet-bulb, water temperatures and flow.
- Towers are evaporative coolers ("swamp coolers"). They work very well in dry climates (Arizona, the desert West); the hard part there is keeping them clean.
- In places that run near 100% humidity most of the time (Georgia, Florida, the East Coast), a tower struggles: it can't get the water cold without the temperature climbing, and the extra plant life puts more organics in the air and the water. There, an air-cooled chiller system sized for the local warm temperatures is often the better choice. Air-cooled chillers have gotten very good, and Mike leans that way.
- Office: the physics behind it: an evaporative tower can only cool water toward the outdoor wet-bulb temperature, and in humid air the wet-bulb is close to the air temperature. Use the site's design wet-bulb (for a tower) or dry-bulb (for an air-cooled chiller) when sizing.
Hydraulic oil and feed throats (published rules of thumb, found 2026-10-12; Mike confirmed 0.1 ton/hp is the rule he remembered):
- Hydraulic injection molding machines: about 0.1 ton of cooling per hydraulic motor horsepower, 1 ton per 10 hp. Sources: Advantage Engineering's sizing sheet (https://advantageengineering.com/fyi/073/advantageFYI073.php), Conair's chiller sizing guidance, and a Plastics Technology data card (https://www.ptonline.com/cdn/cms/PlasticsCard03152022.pdf). Read through search results and Perplexity; the office did not open the pages itself.
- Feed throat: about 0.5 ton per throat on machines under 500 tons, about 1 ton at 500 tons and up (Plastics Technology card; Advantage lists 0.5 ton per throat).
- General hydraulic systems, as a cross-check: heat is a fraction of pump input power, about 25% for simple circuits up to 60-75% for servo systems (Flodraulic, via Perplexity). Physics: 1 hp = 2,545 BTU/hr = 0.212 ton, so 25-33% heat is 0.053-0.070 ton per hp. Injection molding hydraulics run hotter than a simple circuit, which is why the molding rule is 0.1.
- Use running power and duty cycle where known, not just nameplate; and size the oil cooler from its maker's heat rejection at the real oil flow and temperatures.
- Put the hydraulics on chilled water (Mike). His plants started them on tower water and moved them to the chillers over time: tower water is too dirty for servo-driven hydraulics and the heat exchangers on them, which need cleaner water. Size the chillers for mold + hydraulic + feed throat loads together.
The calculation (plant mode) adds up each press's worst-job pounds and heat per pound, adds the hydraulic (0.1 ton/hp) and feed throat allowances when given, then gives the total load in BTU/hr and tons, the size of each of three units, the typical two-thirds load, and the chiller loop flow at a 10 F rise (gpm = BTU/hr / (500 x 10)).
Library: ASHRAE Handbook (HVAC Systems and Equipment), CTI codes, ASHRAE 188 and Guideline 12 (Legionella; they apply to cooling towers), chiller and controller makers' guides.

HANDS OFF
A mechanical contractor for plant piping, chillers and towers; a water treatment vendor for chemistry and the Legionella program on towers; the tool shop for inserts and circuit changes. The office prepares the review and the numbers; it does not specify plant equipment for purchase.

WHAT THE REVIEW PRODUCES
One cooling review per mold, in its own dated folder: the circuit table (flow, in, out, rise, heat, flags), the heat map by face count (one, two, three faces), the list of moving parts with and without water, recommended changes in order (single-circuit the restrictive line, add water to uncooled moving parts, conductive inserts where three faces meet, re-balance loops), and what to measure next. Recommendations are proposals; Mike or the tool shop confirms.

## Resin drying and handling (b-drying-handling)
(procedure file: sop-drying.txt)

Procedure: Resin drying and handling (b-drying-handling). Revision 6 — October 18, 2026. Hopper sizing, regrind and desiccant added from Mike's notes.
Index: the procedure index in `an-office`
Source: Mike's practice (Mike's notes, kept private). Lines marked "Mike" are his practice; "published" lines cite the library; anything else the office adds is marked "office". Tier: deep.
Read this when a resin must be dried (nylon, PC, PET, PBT, ABS and other engineered resins), a process drifts or the parts show splay, the nozzle spits, a dryer "isn't keeping up", a plant adds dryers, or regrind goes into a process. Calculations: https://github.com/mminwi/an-creation-office/blob/main/specialists/calcs/drying.py (hoppers and dryers), https://github.com/mminwi/an-creation-office/blob/main/specialists/calcs/regrind.py (regrind generations).

WHY IT MATTERS
Wet resin makes the process wander (Mike). Water turns to vapor in the barrel: the melt flows easier than it should, the parts show splay, and the nozzle spits and sputters as the gas escapes. Published: nylon must be molded dry; moisture degrades the polymer and costs surface quality and strength (BASF Ultramid brochure, library: resin-design-guides).

1. TEST THE DRYER; DON'T TRUST ITS METER (Mike)
- The most common problem: plants run dryers nobody has ever tested. A dryer with dead desiccant is only a hot air dryer. Warm air preheats the pellets and helps a lot, but not enough for nylon and many engineered resins.
- Buy a dew point tester and measure the air going into the hopper yourself.
- Don't believe the dryer's own dew point display. If it reads -40 seconds after start-up, it is only telling you the machine is on.
- How a twin-bed desiccant dryer starts: it regenerates (cooks) one bed first, and switches to it after roughly 30 minutes to an hour. Until then it is only heating. Test after the first bed has been regenerated and switched in, not before.
2. TEST THE RESIN (Mike)
- Use a moisture analyzer: it heats a resin sample and reports percent water. There is no substitute if you run resin that needs drying.
- Compare the reading with the resin maker's moisture limit for molding.
3. CHECK THE PLANT'S POWER: REVERSE PHASE KILLS DRYERS (Mike)
- Some three-phase outlets get wired with the phases reversed. A dryer plugged into one runs its fans backwards: the air goes over the desiccant without passing the filter first. Resin dust coats the desiccant, the regeneration heat melts it on, and that desiccant is finished; no amount of regenerating brings it back.
- Dryers get wheeled around and plugged in wherever, and desiccant is often replaced only every five years or so. One or two bad outlets can quietly ruin every dryer in the building. A new dryer plugged into the same outlet goes bad too, so replacing dryers does not fix it.
- Test every outlet with a plug-in phase rotation tester: phase rotation and ground, on 220 V and 440 V three-phase. Check that dryer fans and blowers turn the right way.
- Replace desiccant every year whether it seems to need it or not (Mike's practice with mostly engineered resins). Keep the replacement date on each dryer.
- Office: fixing wiring is a job for a qualified electrician; testing live outlets follows the plant's electrical safety practice (NFPA 70E in the library).
4. GRINDERS AND REGRIND (Mike)
- Reverse phase runs grinders backwards too. A backwards blade pulverizes the regrind into dust; the dust gets conveyed into the dryer and seals the desiccant the same way.
- Be careful with regrind generally: it brings fines and dust.
- Regrind levels and color: section 7.
5. THEN DRY TO THE RESIN MAKER'S NUMBERS (Mike)
- Drying temperature, time and dew point: do exactly what the resin maker says. If it says four hours at a given temperature, that is what it is. With good dryers, good drying hoppers and good hoses, nine times out of ten that is all it takes.
- Dryer and hopper come as a pair: the dryer or hopper maker will size the dryer for you.

6. SIZE THE HOPPER TO THE PRESS (Mike: the more critical part)
- The resin must stay in the hopper at least as long as its drying time. Hopper capacity = drying time x pounds per hour through the press. Four hours at 100 lb/hr needs a 400 lb hopper; a 30 lb hopper on a 100 lb/hr press empties every 20 minutes and never dries anything. Never less than about an hour in any case.
- Old hoppers that feed down the center (funnel flow) need about 1.5 to 2 times that: in a 600 lb old hopper often only 300 to 350 lb actually moves; the rest sits on the walls and never cycles. Mike's example: 4 hours at 100 lb/hr is 400 lb in a good hopper, about 600 lb in an old one.
- Newer hoppers flow down more evenly (all of it moves), so they can be sized at drying time x throughput.
- The proof is the resin: pull a sample at the throat, test it on the moisture analyzer. That is how you find a hopper that only flows down the center.
- Published: the same rule, hopper capacity = drying time x throughput (Conair drying manuals, library: oem-dryer-guides). The calculation does this, with the old-hopper factor.

7. REGRIND (Mike)
Levels:
- Injection molding: about 25% is the normal limit, and the near-universal rule; test the parts at 25%. On engineered resins especially, don't go over 25%. Plants sometimes creep up toward 50% to use regrind up; that is a choice to make knowingly, not the standard.
- Blow molding: 50% regrind is common, because the process makes so much trim and flash.
- White, very light colors and clear: zero regrind. It goes from 25% straight to zero; the visual defects aren't worth it.
- The standard regrind note on most customers' drawings is 25% (Mike). Whatever the drawing or spec says wins.
Generations: what you are really running (Mike: "a great one for AI"):
- At steady state, part of the regrind has been through the press two, three, four times. At high regrind the old generations become a big share. Run the table (regrind.py) for the percentage you plan:
  - 25%: virgin 75%; material 3 or more generations old is about 1.6% of the feed.
  - 50%: virgin 50%; 3 or more generations old is 12.5% of the feed (a quarter of the regrind).
  - 60%: virgin 40%; 3 or more generations old is about 21.6% of the feed (over a third of the regrind).
- Physics of the table: with regrind fraction r fed back continuously, the share that has been through k times before is (1 - r) x r^k; the average pellet has r / (1 - r) earlier heat histories.
First ask what the color is for (Mike):
- Coding color: the color tells people what the part is ("red means this size"), or the part is black for UV resistance or just to be black. Mixing regrind across colors, as below, is fine within limits.
- Matched color: the part has to match something, such as a car's interior red, or it is a critical appearance part. Then don't mix other colors' regrind into it at all, whatever the color, black included.
Where the light-colored regrind goes (coding colors only):
- Don't put white regrind back into white. Run it into gray or another color, but only a little: white lightens other colors fast.
- Black (made for UV resistance or plain black, not matched) is the best place for it: black covers. Black colorant is usually loaded about three times heavier than needed for color, because it is also there to stop UV degradation (block sunlight within the first few thousandths of a wall), so it hides almost any other color mixed in (Mike).

WHAT THE AUDIT PRODUCES
A drying audit in its own dated folder:
- Per hopper: capacity, old (center flow) or new (even flow), throughput through it, drying time, and resin moisture at the throat.
- Per dryer: tag, desiccant age, outlet it uses (phase rotation and ground: pass/fail), fan and blower direction, filter condition, the dryer's displayed dew point, the measured dew point after a full regeneration and switch-over, and the hopper size against throughput and drying time.
- Per resin: the maker's drying temperature, time, dew point and moisture limit; measured moisture at the press.
- Per grinder: rotation direction, fines in the regrind; regrind percentage in use against 25% (and any customer limit).
- Findings in order: wrong-phase outlets (fix first, before any dryer is replaced), dead desiccant or desiccant older than a year, undersized or center-flowing hoppers, resin above its moisture limit, regrind fines. Recommendations are proposals; Mike or the plant confirms.

HANDS OFF
Electrician for outlet wiring; the dryer maker or service company for desiccant replacement; the resin maker for drying conditions.

OPEN FOR MIKE
- How often to re-test dryers with the dew point tester (the office proposes: at start-up of every new dryer, after desiccant replacement, and whenever parts show splay).
