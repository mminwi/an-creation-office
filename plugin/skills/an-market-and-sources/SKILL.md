---
name: an-market-and-sources
description: "Use for the market check, review pages for the inventor, and mapping the resource library to a project."
---

# an-market-and-sources

Sections: Market check: does anyone want it? (b-market-check); Review pages and dated folders; Map the resources to this project.

## Market check: does anyone want it? (b-market-check)
(procedure file: sop-market-check.txt)

Procedure: Market check: does anyone want it? (b-market-check). Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Source: standard customer discovery practice and patent disclosure law (sources below, read through search 2026-10-12); written at Mike's request so inventors check the market before spending on patents and prototypes. Tier: documented; the patent decision comes before any showing (`an-principles-bm` (Decide on the patent before showing it publicly)).
Read this when an idea is new, before money goes into a patent, a prototype or tooling, and whenever the inventor isn't sure who would buy it.

WHY
A common inventor story: years in secrecy, an overbuilt prototype, a full patent, and then no market. Check first that people have the problem, how they solve it now, and what they would pay. It costs little and can save the most.

1. PROTECT THE IDEA WHILE YOU ASK (do this first)
- Talking about how the invention works before a patent application is filed can be a public disclosure.
- United States: the inventor's own disclosure is not prior art if the application is filed within one year after it (35 U.S.C. 102(b)(1)(A); MPEP 2153.01). That is a narrow safe harbor, not an extension, and a sale or offer to sell can start other clocks.
- Most other countries (Europe included) require absolute novelty: a disclosure before filing can end patent rights there, even the inventor's own.
- So: ask about the problem, not the solution. Talk about what people do today, what bothers them, what they've tried and paid. Don't show or describe how your invention works.
- If you need to show the idea: settle the patent decision first (b-patent-prep, the patent conversation ticket): a provisional filed by the inventor or an attorney, only what it does shown, or knowingly no patent. The office records every outside conversation with its date and what was shown (record/).

2. WHO TO ASK
- The people who would use it, and separately the people who would buy it (in a hospital the user and the buyer are different people). Write each group down.
- Not friends and family: they are kind, not informative.

3. HOW TO ASK (past behavior, not opinions)
- Ask about the last time it happened: "Tell me about the last time you dealt with this." "What did you do?" "What did it cost you?" "What have you tried?"
- Don't ask "Would you buy this?" or "Would you use a tool that does X?": people overestimate what they will do.
- Listen far more than you talk. Look for evidence the idea is wrong, not for agreement.
- Price: what they pay now for the current way, and what the problem costs them.
- How many: about 10 to 20 conversations per group usually shows the pattern (five is a bare minimum); programs like NSF I-Corps run far more across many groups.

4. DESK CHECKS (no disclosure)
- Competitors and substitutes: what people use today; search the stores and catalogs they buy from.
- Demand signals: search trends, industry size (Census Business Builder), recall and complaint records for similar products (CPSC, SaferProducts).
- Price ladder: the retail price of similar products; what a retailer or distributor takes; what that leaves for the product cost (b-cost-bom).

5. WRITE IT UP
- One page: the problem in the customers' words, who has it, what they do now, what it costs them, what they would pay, the competitors, and the go/hold/drop signal. Mark each point with how many people said it.
- It feeds the project description (section 7, marketing) and the patent and licensing decisions.

SOURCES (library)
nsf-icorps, strategyzer-vpc, strategyzer-test-card, census-business-builder, google-trends, cpsc-recalls, saferproducts, sheet-launch, sheet-economics, patent-grace-periods, patentability-vs-fto, mpep (MPEP 2153.01, grace period), customer-discovery-method, absolute-novelty.

HANDS OFF
The patent decision (a self-filed provisional, an attorney, or knowingly none): before any conversation that shows how the invention works.

## Review pages and dated folders
(procedure file: sop-review-page.txt)

Procedure: Review pages and dated folders. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Tool: review.py (Python standard library only)

THE DATED-FOLDER RULE (all work, not only pages)
Be overly robust with the record. Nothing made for the inventor is ever written over.
- Every analyst call works in its own dated folder (Office files/sessions/YYMMDD-HHMM-slug/). When it finishes, whatever is there stays there.
- Every web page, graphic, render, drawing or slideshow goes in its own dated folder.
- An update is a new folder, not an edit. The timeline made at kickoff and the timeline made a month later are two pages in two places. The new one may start from the old one; the old one is never changed.
- Folders are never renamed or emptied. Old ones may move to archive/, never deleted.
- It costs disk space. That is the price of letting the inventor go back and look, and they often need to.

WHY REVIEW PAGES EXIST
Talking is easier with something on the screen. Each invention gets web pages on the inventor's computer: where it stands, the timeline, the risks, pictures, documents, and short slideshows on anything worth talking over. b-project-manager sends a link and says "take a look at this" instead of describing it.

WHEN
Make the first page right after intake, the same day the folder is made. Do not wait for content. Status and three dates are enough.
Make a new page whenever the status, timeline, risks or a topic changes, and before any discussion where the inventor should see something.

WHERE
Your files/Review/
  index.html                    the history page: Your list (the action log) first, then today's page, every page in the order made, every picture and document ever shown
  today.txt                     which page is "what we're talking about today"
  YYMMDD-HHMM-slug/             one folder per page, never changed after it is made
    index.html                  the page
    page.json                   copy of what it was made from
    meta.json                   title, summary, when made
    files/                      copies of every picture and document the page shows (files over 100 MB are linked instead)
The index is the only file that is rebuilt, and it only lists. Served on this computer only (127.0.0.1). Nothing goes on the internet.

ON GITHUB (the cloud office)
GitHub shows Markdown, not HTML, so review.py also writes each page as README.md and the list as Your files/Review/README.md (it notices it is in a Git repository). Documents and pictures are linked where they are, not copied into files/: Git keeps every version. Send the inventor the GitHub link to Your files/Review/ (the folder opens to the list) or to a page's folder. There is no "serve" step on GitHub. Never copy the same document into several folders; link to the one dated copy.

WHO WRITES WHAT
b-analyst writes page.json inside its own session folder, then runs "new". b-project-manager runs "serve" and "today" and sends links.

COMMANDS
New page:   python review.py new "AN-Creation/<business>/<invention>" "<session folder>/page.json" --slug timeline [--today]
Set today:  python review.py today "AN-Creation/<business>/<invention>" 261107-1430-timeline
Rebuild index: python review.py index "AN-Creation/<business>/<invention>"
Show:       python review.py serve "AN-Creation/<business>/<invention>"   (prints the link; default port 8765)
Link to one topic: .../Review/<page folder>/index.html#topic-<id>

WHAT GOES IN page.json
title, summary (one line for the index)
status: a few lines (stage, project level, business route, next step)
timeline: date, what, kind (inventor-date, lead-time, milestone), optional risk
risks: risk, cost, when it bites, time left
topics: id, title, weight (Follow, Recommend, Mention), summary, slides (title, bullets, optional image path inside Your files, optional links)
files: "all" (default: every picture and document in Your files) or a list of paths inside Your files
Every section is optional. A page can be just a timeline, or one topic.

HOW b-project-manager USES IT
- After intake: "I've set up a page for your invention. Here's the link."
- Offering a discussion: "There's this: [one line]. I put a short walkthrough up if you'd like to go over it."
- Fuller explanation asked for: b-analyst researches, makes a new page with the topic, b-project-manager sends the link.
- "Where's that picture from last month?": send the history page. Every picture and document ever shown is there, newest first.

RULES
- Plain words. Short slides: a title and three or four bullets.
- Only real artifacts. A rough sketch is labeled as one. No made-up numbers or quotes.
- No passwords, account numbers or SSN on any page.
- Local only. Putting pages online is a separate decision.

## Map the resources to this project
(procedure file: sop-resource-map.txt)

Procedure: Map the resources to this project. Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Library: resources.json (`an-office-files`) (about 470 sources in 18 groups; specialist sources carry b_roles naming the specialist roles that use them)
Goes with: `an-focus-and-gateways` (Gateway questions) (the questions), `an-focus-and-gateways` (Keep the project focused) (what goes on the list)
Read this once the inventor has described the product, and again when the product changes in a way that matters (it gets a battery, it will be sold in Europe, a hospital wants it). Then leave it.

WHY THIS EXISTS
Most of what a project needs to know is already written somewhere: which tests, which certifications, which records, which risks. The library points at the real sources. This procedure decides, in bulk and early, which of them this project touches, which it does not, and what is missing. Then the work reads the current version of the ones that apply.
Most projects touch a good handful. None touches all of them.
The point is risk. Every one of these programs (ISO, AS9100, the medical rules, FCC, UL, CE, military testing, patents, a company) exists to check and lower the risk of a product in its intended use, or the business risk around it. A patent is business risk: someone else making and selling the idea. We use the same standards everyone else judges products by, early, so the inventor sees the risks while there is time to react, before they become a crisis.
Time is part of every risk. A risk with six months to fix is not the same as one due in three weeks, so each "in" source gets a lead time against the inventor's dates.
The library is a first, cursory look, not the whole list. It gets to the right questions fast. Answering them will often still need a search.

SINGLE-SOURCE FROM THE LIBRARY (D-062)
The library is a chosen set that represents each area well, picked so the AI can go to one good source and stay in line with how products should be developed. Start from it. Do not go looking for a dozen equivalent standards or guides on a topic the library already covers; use the library's source for that area and read its current page. Search outside the library only for what it doesn't cover: the industry search, a standard a buyer or contract names, or a missing official source (step 4). The inventor does not explain the resources to you; you read and search them yourself and bring back what applies.

1. WRITE THE PRODUCT PROFILE
From what the inventor already said, fill this short profile. Answer what you can from their words. Mark the rest "unsure". Do not quiz them on every line.
- What it is, who uses it, where.
- Medical: does it diagnose, treat, monitor, or go in or on the body for a health reason?
- Aircraft or space: does it fly, or go on something that does?
- Vehicle: is it part of, or attached to, a car, truck or other vehicle?
- Military or government buyer?
- Power: battery, plug, circuit, software, radio or wireless?
- Children: made for, or likely used by, kids under 12?
- Food or skin: touches food, drink, mouth, or skin for long periods?
- Water and weather: used outdoors, washed, or wet?
- Machine or tool: moving parts, blades, heat, pressure, or industrial use?
- Where it will be sold: friends, online, big stores, marketplaces, outside the U.S.?
- Industry and setting: is it sold into a particular industry (railroad, mining, marine, oil and gas, food plant, hospital) or used somewhere unusual (washdown, hazardous area)?
- Materials: electronics, or sold in Europe or California (restricted substances)? Lithium battery?
- Drawings: will a shop make parts from drawings or CAD files?
- Business roads: company, patent, outside money (these are the gateways in `an-focus-and-gateways` (Gateway questions)).
Show the inventor the filled profile. Ask them to fix what is wrong and answer only the "unsure" lines that change which shelves open, one at a time.

2. THE PROFILE PICKS THE SYSTEM
Every product gets our own quality sheets. ISO 9001 is the general background most things can fall under. A yes below adds a stricter system with more testing and records. Name it; do not claim certification.
- Medical: FDA rules for devices, ISO 13485, IEC 62366 usability. Usually a professional's road early.
- Aircraft or space: AS9100 (IAQG), plus the aviation authority's rules.
- Vehicle: IATF 16949 and the AIAG core tools.
- Military or government: MIL-STD for the environment, EMI, packaging and marking; ASSIST; SAM.gov registration.
- Power: UL or another recognized test lab (OSHA NRTL list), FCC for anything that radiates, IEC/CENELEC if sold abroad, NEC for wiring.
- Water: IP or NEMA ratings for the case and controls.
- Children, food or skin, machines: the consumer safety (CPSC) and matching shelves.
- Stores and marketplaces: the retailer's supplier requirements.

3. SCREEN THE WHOLE LIBRARY IN ONE PASS
This is a job for one intern, not a conversation. Give it the profile and resources.json. It writes resource-map.csv, one row per source:
- in: this project needs it now.
- later: needed when a trigger happens ("before the first sale", "if it goes to Europe").
- out: the profile says no. Mark whole groups out at once: no military means the military group is out; no medical means the medical sources are out.
- ask: depends on an "unsure" line. That line becomes one gateway question.
Each row gets a one-line reason pointing at the profile line. Most rows will be out. That is the point.
The inventor does not see two hundred rows. They see the profile, the short "in" list, and one question at a time for "ask".

4. LOOK FOR WHAT THE LIBRARY IS MISSING
Always run the industry search, every project, once the inventor has said who buys it, where it is used and in what conditions. The library holds the common programs; many industries have their own specs that it does not. Railroad is the known gap: rail buyers have their own rules for electronics, remote controls, enclosures and washdown. Search:
"Does the [industry] have specifications or requirements that affect [product type]: the electronics, the enclosure, the environment (washdown, vibration, temperature, outdoors), or how buyers approve suppliers?"
Search the buyer's industry and the setting, not only the product name. A hit becomes a row (found, not yet checked) and a question. No hit: record the search and the date in resource-map.csv, and reopen it if a new buyer or setting turns up.
Also search recalls and incident reports on similar products (cpsc-recalls, saferproducts). What went wrong for others is the cheapest start on the FMEA.
For each yes in the profile, ask: is there a source this project needs that we do not have? Search for it. Start from the official body: the government agency (.gov, .mil), the standards body, or the test lab. Add it to resource-map.csv as "found, not yet checked" with the date. Send a note to the library so it can be added for the next person.
Watch for lookalikes. Many .com sites sell company formation, registrations or "official" forms that the government provides directly. A state business filing starts on that state's .gov site. Read the actual web address, not the logo. The library's government-site guidance has the details.

4b. WEIGH EACH "IN" SOURCE AND OFFER TO DISCUSS IT
Give every "in" row a weight in resource-map.csv:
- follow: a rule or official process this product has to meet. It goes on the plan with a risk line and a lead time.
- recommend: a good program or method, worth using, not required. Tell the inventor what it is in two lines and why it fits.
- mention: background, or worth a look later. Look at the site briefly and tell the inventor what it is.
The weight depends on the product: a recall search is recommend for a toolbox and close to follow for a children's product.
Offer to discuss every one, whatever its weight. The default, through b-project-manager: "There's this: [one line]. Would you like to go over what it's about?" Yes: talk it through, or research it and come back with a fuller explanation, or make a short slideshow on a review page (`an-market-and-sources` (Review pages and dated folders)). Not now: note it and move on; offer again if it comes up. A follow item stays on the plan whether or not they discuss it. Any time they ask for a fuller explanation, give one.

5. READ THE CURRENT COPY OF EACH "IN" SOURCE
The library is pointers, not copies. Do not download or store the source. For each "in" row, the session for that subject opens the current page when the work needs it, not a memory of it, and saves a few lines in plan.md or the subject folder:
- the link, the date read, and the edition or revision;
- what it asks of this product: tests, certifications, records, labels;
- the risks or questions it raises.
Next time, open the link again. The page may have changed.
Those questions go through `an-focus-and-gateways` (Keep the project focused): asked as a question, decided, on Now or Later, or dropped. A source does not dump its whole checklist into the project.
Any value taken from a source into a sheet carries the source columns and gets the second-pass check against the document before it is used (`an-cost-and-risk` (The source check)). Never a value from memory.
For a paid standard, record the title, edition and where to get it. Do not copy it. Use the free summary or the official overview until the inventor decides to buy it.

Every "found, not yet checked" source gets its official address, the open question of whether it applies, and a dated check before it is used for design, testing or showing anyone. A search result is a lead, not a source.

6. KEEP IT CURRENT
When the profile changes, re-screen only the groups that line touches. When a gateway answer or a revisit date changes, update its form, framework, plan and the affected resource-map rows in the same run, and point at the decision rather than copying dates. A changed row is a one-line check with the inventor, as in `an-focus-and-gateways` (Keep the project focused): "Because it now has a battery, the electrical shelf opens: UL and FCC. Is that right?"

DONE WHEN
The profile is confirmed, every library row has in, later, out or ask with a reason, every "in" row has a weight and was offered for discussion, the industry and recall searches are recorded with dates, each "ask" was asked once, missing sources were searched from official sites, and each "in" source has a dated note of what it asks of this product.
