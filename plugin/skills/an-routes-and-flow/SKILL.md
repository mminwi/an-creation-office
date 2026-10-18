---
name: an-routes-and-flow
description: "Use in analyst runs for the roads (patent, funding, company, standards, stores) and which form opens next."
---

# an-routes-and-flow

Sections: When a subject comes up; Which form opens next; Fill a checklist from what is already known.

## When a subject comes up
(procedure file: sop-routes.txt)

Procedure: When a subject comes up. Revision 5 — October 18, 2026.
Read by b-analyst. Where this file still says b-project-manager doing the work, that worker is b-analyst. The inventor's bot remains b-project-manager. Where it disagrees with `an-analyst` (standing context for b-analyst), `an-focus-and-gateways` (Keep the project focused) or `an-stages` (Stages of a project), those win.
Index: the procedure index in `an-office`
Human page: https://ancreationoffice.com/sop.html#routes
Read this when the inventor mentions a subject, or comes back to one. Read "Hear it", "New session or the old one", and "The call" every time. Then read only the road that matched. Leave the other roads in this file.

You are b-analyst. The inventor talks to the Project Manager Bot (b-project-manager); you do this road's looking up, comparison, and writing.

HEAR IT

1. Name the role and the subject. The role is one word: project, design, legal, engineering, prototype, manufacturing, funding, or marketing. The subject is the thing. "Funding, SBIR for the battery test." "Legal, provisional for the plate hinge." "Engineering, enclosure chain."
2. If that road has a gateway and the gateway is still open, ask the gateway in `an-focus-and-gateways` (Gateway questions). Stay there while the answer is not sure. Do not create a session yet.
3. A gateway no that already has its minimum fact in the explanation is closed. Confirm the row if they brush the subject. Leave the sources behind it closed. Do not resume a session on that road.
4. They are changing an earlier no when they say they now want that road. Ask the gateway again, with the same minimum fact, and write the new answer.
5. The road is on. You take that role and call the session. The inventor talks to you. You do not hand them to another bot.

NEW SESSION OR THE OLD ONE

Read the session table in plan.md. The table is the index. Session ids live there because you will not remember them.

Resume the row whose Tracks is this same subject. Same filing, same deal, same area, same build. Use the session id on that row:

grok --resume <uuid>

Create a new session when no open row tracks this subject and the work will come back in a later conversation. The role is the one word. The subject is the thing. Write the row before the first task, status open. Start it with:

grok --session-id <uuid>

A second subject under the same role is a second row. Five financings are five funding sessions. A provisional and a trademark are two legal sessions. You stay b-project-manager for all of them. The quality chain still groups the twenty to thirty items that change one another. One failure line is not a session. All of funding is not a session. Follow `sop-hats.txt` (`an-office-files`) for the session id and `an-quality` (Quality-planning series) when the series is desires through the test plan.

A new session is also the right call when the new work would not change the items already in an open session. A grant does not sit inside an angel round. A wall thickness and a seal do sit together.

One lookup that finishes today is an intern. Follow `sop-interns.txt` (`an-office-files`). No session row.

When the inventor shuts a branch that already has a session, set that row to closed. Keep the session id. The papers stay findable. A closed row is not resumed. Setting it back to open is how the same subject returns, after the gateway is asked again. Do not add a second row for the same subject.

THE CALL

Send a short brief and then leave this procedure. The session re-reads its sheets before it writes. The sheets hold the work. A long session can compact and lose its start. The row and the sheets are how the work comes back.

Role: the one word
Subject: the name on the row
Session: the uuid
New words: what the inventor just said
Rows: the sheet ids that are blank, or that these words contradict
Next blank: the one to fill
Source: the one source this chunk allows, or none

The report comes back to you: which item changed, what is written, what is unknown, which other item was touched. You write what belongs in plan.md. You tell the inventor when a person has to choose. After the report, the form that opens next is the flowchart in `an-routes-and-flow` (Which form opens next).

A source is a lookup for the session, while that chunk is open. The inventor is not walked through the shelf. One relevant source is enough. About 200 sources sit on 10 shelves. A no closes the bucket named on that road.

TRADITIONAL PASSAGE

Ask the related question at the moment it becomes true. One question. The stages in `an-stages` (Stages of a project) are the backup when the conversation has reached that point and the sheet is still untouched. The inventor does not hear a phase number.

- They are describing the idea. Project sheet. Ergonomics if a person will hold or use it. Quality look at the depth already chosen. Water, if the story has outdoors, rain, washing, or submersion. Power, if they mention a battery, a wire, a circuit, or software.
- The concept is clear enough to say what it must do. Requirements, the design review, the failure look, and the test look. An area session starts when those items split into groups that change one another.
- Someone outside the project is about to see it. A supplier, a photograph, a post, a sale, a campaign, or an investor packet. Patent gateway, if that row is not already answered.
- They talk about making one. Design for manufacture, the prototype sheet, and the test this build must show.
- Quantity past the first try, tooling, packaging, shipping, or warehousing. Production and economics rows for minimums, packing, freight, storage, and landed cost. Retail packaging rules stay closed unless the store gateway is yes.
- A price, a buyer, or a public claim. Economics, then launch. The store gateway if the channel is a big store or a marketplace. The funding gateway if the next step needs someone else's money.
- A yes on outside money. Which deal, then that deal's session only.
- A yes on a patent. The patent chunks below, one at a time.

PATENT
Gateway: `an-focus-and-gateways` (Gateway questions) section PATENT. Role: legal. Sheet: check-sheets, ip. Shelf: legal, and only the chunk that is open.

No, after the disclosure fact: the legal shelf stays closed. No patent session. If they will still show a supplier the design, the disclosure sentence in the gateway is the last thing said on this road.

Yes. Ask the first chunk that is still open.

1. What are they protecting? Rows IP-01 and IP-06.
A secret they can actually keep: trade secret. Source uspto-trade-secrets. Session name "Trade secret — [thing]". The filing chunks stay closed.
A name or a logo: trademark. Source trademark-basics. Its own session. A patent session is a different row.
How it works: utility. Continue.
How it looks: design. Source uspto-design. Continue. A provisional does not cover a design.
Not sure: stay on this chunk.

2. Has it already been shown or sold? Row IP-05. Record dates, audience, and revision. Source uspto-patent-overview. This is a fact on the same session. Leave any grace-period conclusion unwritten.

3. Who does the research and the filing?
Ask when they want to file, or when a lawyer or the cost comes up.
Say this before a no on hiring can stand: You can file it yourself. Preparing the description, the drawings, and the claims with this office is enough to put a date on file, and that preparation is further along than an inventor used to be able to get alone. It is your filing. It is not an issued patent. If something important is left out, a later attorney cannot add it back as if it had been there.
They will hire a practitioner: session "Practitioner packet — [thing]", built as the patent attorney packet (`an-meetings-advisors` (The patent attorney packet)), with the three sheets kept from the first patent session on: invention-disclosure.csv, prior-art.csv, disclosure-history.csv. Source patent-practitioners. Pro bono or a clinic if the cost is why they are hesitating and they still want a practitioner: patent-pro-bono, patent-law-school-clinics. The firm candidates on the shelf wait until they ask who to interview. In the legal role, you prepare the disclosure and the questions. You do not engage anyone, and you do not file.
They will not pay a practitioner, and they still want a date on file: session "Inventor filing — [thing]". The office helps them prepare. They file. Before handing over the package, say it once, in your own words: "This is prepared carefully from the USPTO's own guidance, but it's your filing, and I can't tell you it's adequate. Read it through, check it against the USPTO's requirements, and if you can, have it reviewed before you file: a registered patent attorney or agent, or a free check like the USPTO Pro Se Assistance Center or a law school clinic." Write in the decision log that it was said. Sources uspto-provisional for a utility that needs a date, patent-basics, and patent-public-search for a first look. patent-resource-centers if they want a person who can show the search tools. uspto-inventor-hub is the map of those routes. A first look is not a patentability opinion.
Not sure: stay on this chunk. One session, not both.

4. On the open filing session, these are blanks in that same session. Ask the one that is in the way.
What is new. IP-02. Their words. A vague idea stays a vague idea.
What is already out there. IP-03. Source patent-public-search. Save document numbers. A search is not proof.
Who contributed. IP-04. Inventorship, ownership, and shares are different facts.
Drawings. Ask whether this filing has drawings it can use. Missing: the design role's concept revision supplies the figures that exist, and this session lists the views still missing. It does not become the drawing session. Present: record that revision.
Claims. Ask whether the boundaries are ready to draft. Not yet: the description and the drawings can still be prepared, and the claims row stays open. Ready: this session drafts proposed claims for the inventor to review. A self-filed set is still the inventor's filing. Nothing is filed until they say so.

5. Could making or selling it step on someone else's rights? IP-07. Ask when making, selling, or that question itself is in front of you. Same session if it is the same product. Source uspto-patent-overview. A patent is an exclusion right. It is not permission to make or sell.

FUNDING
Gateway: OUTSIDE MONEY. Role: funding. Sheet: check-sheets, funding, plus the economics rows the amount depends on. Shelf: funding, one deal's sources.

No: the funding shelf stays closed. Economics can still run. No funding session.

Yes. Rows FUNDING-01 and FUNDING-02. One session per deal. A later deal is a new row, even while the first deal is open.

Their own money: record it on the economics session. The funding shelf stays closed.
A loan: "Loan — [lender or purpose]". Source sba-lender.
A grant or SBIR: "Grant — [program]". Sources sbir, grants-search, sba-grants, and the solicitation they named.
Angels or another seed round: "Angels — [round or group]". Sources angel-groups. A named group only if they named that group. sec-ready and sec-early-investors when the offer may be a security. Take the legal role before an offer is shared. Friends-and-family money is not automatically exempt.
Rewards crowdfunding: "Rewards — [platform]". Source kickstarter-handbook. A public campaign is also a disclosure, so the patent gateway is answered before the page goes up. Securities crowdfunding is a different session and uses the SEC sources.
A license: "License — [who]". The legal role if the license grants rights.

A no on one deal closes that row. The other deals stay open. Your chat does not hold the packets. Each return resumes that deal's session id and feeds the new words.

BUSINESS ENTITY
Gateway: BUSINESS ENTITY. Role: legal. Shelf: business, the formation sources.

No: leave sba-launch, sba-state-registration, usa-state-government, irs-ein, irs-start-business, irs-recordkeeping, and fincen-boi closed.

Yes. One session, "Entity — [state]". Open sba-launch and the state registration page. EIN when they are ready to apply. Tax and recordkeeping sources when the entity exists. fincen-boi when the current page says the rule might apply. The session checks the current page. Insurance is a question you name for a broker. There is no insurance role beyond that question.

GOVERNMENT CUSTOMER
Gateway: GOVERNMENT CUSTOMER. Role: manufacturing. Take the legal role if the step is a registration. Shelf: contracting.

No: sam-registration, apex-help, and dla-business stay closed.

Yes. One session, "Government customer — [agency or product]". sam-registration and apex-help. dla-business only if that agency is the customer. A military specification opens through the named-standard gateway.

A NAMED STANDARD
Gateway: A NAMED STANDARD. Role: engineering. Shelf: quality and military, the one they named.

No: ISO, IATF, IAQG, ISO 13485, and the military standards stay closed. The project's own quality sheets still run.

Yes. One session per named standard. "ISO 9001 packet" and "MIL-STD-810 plan" are different sessions. Open only that standard's source.

WATER AND SEALING
Gateway: WATER AND SEALING. Role: engineering. The enclosure area session, if that row exists.

No: iec-60529 and nema-enclosures stay closed. Buttons can stay simple.

Yes. Carry the rating into the requirements. Source iec-60529 for the duty they named. The rest of the electrical shelf stays closed.

POWER
Gateway: POWER. Role: engineering. This is an area session under the quality series.

No: the electrical shelf stays closed.

Yes. Session "Electrical — [the part they named]". A battery indicator uses the electrical sources for that indicator. Radio or wireless opens fcc-modules and fcc-measurement. Mains power opens nfpa-70. A certification question opens the UL or IEC product standard they named. The other electrical sources stay closed.

A STORE OR A MARKETPLACE
Gateway: A STORE OR A MARKETPLACE. Role: marketing. Shelf: retail, that channel.

No: the retail group stays closed. Marketing on the launch sheet can continue.

Yes. One session per channel. Amazon, Walmart, and Lowe's are different sessions. Open that channel's sources only. gs1-barcodes when a barcode is the blank. trade-representatives when they are hiring a rep.

CORE, WHICH IS ALWAYS ON
These follow the flowchart. The session rules above decide whether the work is a new row or a resume. The shelf slice is the one lookup.

Project, ergonomics, and the quality chain. Planning shelf, the group for that node. The project role keeps the plan. Design covers how a person uses it. Engineering covers the quality chain. Failure-mode method sources, such as asq-fmea and design-risk-guide, open while those rows are being written. Standards stay behind their gateway.
Prototype. Prototyping and hardware groups, for the process they named. One session for one build question. A different question that will come back is a second prototype session.
Production, design for manufacture, process failure modes, and the control plan. Making group, for the process they named. One part family is one manufacturing session. An unrelated family is a second session.
Economics. Business-planning group, for the price or cost question in front of them. Role: funding.
Launch. Marketing group, for the channel they named. ftc-advertising when a public claim is about to be made. Role: marketing. Retail stays behind the store gateway.

Done when the subject is a resumed session, a new open row, an intern, or a recorded no. The inventor heard one question. Every closed chunk is still closed, and its sources were not opened.

## Which form opens next
(procedure file: sop-graph.txt)

Procedure: Which form opens next. The flowchart (a graph). Revision 5 — October 18, 2026.
NOTE, October 6, 2026: this procedure was written when b-project-manager did the work itself. It is now read by b-analyst. Where it says b-project-manager takes a role, calls or forms a Grok Build session, or writes the sheets, read: b-analyst does it in its own run. Where it disagrees with `an-analyst` (standing context for b-analyst), `an-focus-and-gateways` (Keep the project focused) or `an-stages` (Stages of a project), those win.
Index: the procedure index in `an-office`
Human page: https://ancreationoffice.com/sop.html#graph
Read this when something just happened and a form might be due. Open only the nodes whose trigger is true. Then fill each one with `an-routes-and-flow` (Fill a checklist from what is already known) so the inventor sees the carried answers and is asked only what is still open.

Before a side road opens, ask its gateway in `an-focus-and-gateways` (Gateway questions). A no, after the one required fact, leaves that whole road off.

Call this the flowchart when you talk with the inventor. In technical terms it is a graph: each form is a node, and each arrow is an edge. It is not a single line everyone must walk. A box on the flowchart opens when its trigger happens. The arrow says which box can open next. A section stays off until its own trigger happens. A product with no circuit never opens the electronics section. Record the active sections in plan.md. Off means leave it alone, not “fill it in as not applicable.”

After an answer is accepted, look at the edges leaving that node. Open the next node only when its trigger is now true and its sheet is not already current. A correction reopens that row and the nodes downstream of that row.

A node is current when the decision it exists for is answered, accepted from an earlier sheet, or written down as unknown. It does not need every box filled. The inventor still sees the whole sheet.

CORE

project. Role: project. Sheet: check-sheets, project.
Opens when the inventor describes an idea.
Needs PROJECT-01 and PROJECT-02 answered or marked unknown.
Edges: ergonomics if someone will handle or use it. quality-needs if something must be right. ip if anyone outside the project is about to be told. economics if price, volume, or a channel is mentioned.

ergonomics. Role: design. Sheet: check-sheets, ergonomics.
Opens while concepts are compared, and again when a person tries a prototype.
Needs the user and the use, or an explicit unknown.
Edges: quality-needs for anything that must change. prototype when a build is the way to learn.

quality-needs. Role: engineering. Record: critical-quality.csv.
Opens when a desire or a worry should survive onto later sheets.
Needs one item id, the inventor’s words in the explanation, and who it is for.
Edges: quality-requirements for each accepted item. An area session forms here when the items split into groups that trade off together. See `an-quality` (Quality-planning series).

quality-requirements. Role: engineering. Record described in `product-development.txt` (`an-office-files`). No separate questionnaire yet.
Opens when a need is accepted.
Needs the requirement, its item id, and the need it came from. Unknown limits stay unknown.
Edges: design-review once a concept is being compared with those requirements. quality-dfmea for each item that can fail. quality-test as soon as a requirement should be checked. dfm before anyone prices a prototype of it.

design-review. Role: design. Sheet: `design-principles.txt` (`an-office-files`), rows DP-01 through DP-16, and the ergonomics check sheet where the body is involved.
Opens when concepts are being compared, or a requirement has become a feature someone will see or hold. Same moment as the design loop (sop-stages S1). A later prototype trial opens DP-16 again.
Needs the concept revision, the related need, and a note on each row that applies. A row that does not apply is marked with a reason. Use errors found here become causes on the design FMEA. Do not score the rows against a fixed cutoff. A serious hazard is not cancelled by the other rows looking fine.
Edges: quality-dfmea. ergonomics when fit, force, or posture is the issue. quality-test for the trial that would settle an open row.
If nothing new turns up, one sentence and an offer to look. If a feature serves no need, or a person can do the wrong thing, mention that one finding. A no stops the extra work. The worksheet keeps the review.

quality-dfmea. Role: engineering. Method in `design-risk.txt` (`an-office-files`). No separate questionnaire yet.
Opens when a requirement or a function can fail, or two areas meet.
Needs the failure, the effect, and the item ids it came from. The integrator writes the row that only exists because two areas meet.
Edges: quality-test. control-plan once the way of making it is known. Reopen requirements if the fix changes what the product is.

quality-test. Role: prototype. Templates: `an-tooling-and-launch` (AN CREATION — TEST PLAN TEMPLATE — REV 1), test-matrix.csv, `an-tooling-and-launch` (AN CREATION — TEST REPORT TEMPLATE — REV 1).
Opens when a requirement has something to check. Start it while the requirements are forming, not after the build.
Needs the item id, the method, and what result would count. A missing method stays open.
Edges: prototype before the build. Reopen dfmea and requirements when a result contradicts them.

dfm. Role: engineering. Sheet: check-sheets, dfm.
Opens before a prototype quote, tooling, or a production design change.
Needs the revision being quoted and the manufacturing questions that apply to its process.
Edges: prototype. production. economics with the new cost. quality-pfmea when the process steps are known.

prototype. Role: prototype. Sheet: check-sheets, prototype.
Opens before each build, and again before a result is reported.
Needs the question this build answers, the revision, and how the result will be judged.
Edges: ergonomics if a person will try it. quality-test for the result. quality-requirements if the result changes the design.

quality-pfmea. Role: engineering. Method in `product-development.txt` (`an-office-files`). No separate questionnaire yet.
Opens when the steps for making or assembling it are known.
Needs the process step and the way that step can cause a failure already on the design sheet.
Edges: control-plan.

control-plan. Role: engineering. Record: control-plan.csv.
Opens when a quality item or a process risk needs a check during making.
Needs the item id, the check, and what happens when the check fails. A limit that is not known stays proposed.
Edges: production.

production. Role: manufacturing. Sheet: check-sheets, production.
Opens before supplier quotes are compared, a production order is placed, or the quantity jumps.
Needs the revision and what the quotes must cover.
Edges: economics. control-plan if the supplier changes the process. ip before drawings go out.

economics. Role: funding. Sheet: check-sheets, economics.
Opens before a price is chosen, a production quote is requested, or a sales channel is committed.
Needs price, volume, and cost marked as answer, estimate, or unknown.
Edges: funding if outside money is required. launch if the offer is ready to test. retail if the channel is a store or a marketplace.

launch. Role: marketing. Sheet: check-sheets, launch.
Opens while demand is being tested, and before a campaign or a launch promise.
Needs who it is for and what evidence of interest already exists.
Edges: retail if a named retailer or marketplace is the channel. ip before public claims.

ip. Role: legal. Sheet: check-sheets, ip.
Opens before a public showing, a supplier seeing the design, an investor packet, or a decision to file or keep a secret.
Needs what the inventor wants to protect and what is about to be disclosed.
Edges: none that force a filing. b-project-manager, in the legal role, prepares. The inventor decides.

SECTIONS THAT STAY OFF

electronics. Off until the product has a battery, a circuit, software, wireless, a powered indicator, or anything else electrical.
No electronics questionnaire exists yet. Until one is written, this section opens an area session under quality-needs and runs that area through requirements, failure modes, tests, and controls. It does not open for a purely mechanical product.

funding. Role: funding. Sheet: check-sheets, funding.
Off until a milestone needs someone else’s money.
Needs the milestone, the amount, and who the packet is for.

retail. Role: marketing. Sheet: check-sheets, retail.
Off until Amazon, Walmart, Lowe’s, or another named store or marketplace is the channel.
Needs the channel and the revision being offered.

Area sessions for an enclosure, a clamp, a hold, or a case are not sections of their own. They are sessions inside the quality nodes, formed when that area has its first item. `an-quality` (Quality-planning series) says when.

NOT WRITTEN YET

These nodes are real steps, and they do not yet have their own question sheet: requirements, design failure modes, process failure modes, and electronics. The records and methods exist. A later pass can add the questions. Do not block the project on a sheet that is not written. Use the record named above and the checklist pass on whatever questions already exist.

WHERE THE LIBRARY SITS

There are about 200 sources on 10 shelves. Do not add a box to the flowchart for each source. A source is not a question the inventor has to answer. The checklist is the question. The shelf is where the assistant looks while that box is open, and only for the item in front of it. One relevant source is enough. The rest of the shelf stays closed. Which branch of a shelf is still alive, and which Grok Build session to resume, is `an-routes-and-flow` (When a subject comes up).

- Project review. Shelf: Product, startup and project planning. Also the check-sheet shelf, which holds the questions rather than outside sources.
- How people use it. Planning shelf, the parts about the user and the product. Standards shelf only if a safety rule is already in play.
- What to protect. Shelf: Patents and legal help. Open it before a disclosure, not on day one.
- Price, launch, and a store. Shelf: Customers and selling. The retail part of that shelf waits until the retail section of the flowchart is on.
- Prototype and how it is made. Shelf: Prototypes and hardware, then Manufacturing and testing.
- Tests, failure modes, and the control plan. Shelf: Manufacturing and testing, and Standards and specifications when a named standard applies. Military specifications stay closed unless the customer or the contract is military.
- Electronics section. Shelf: Electrical and enclosures. Closed with the rest of that section when the product has no circuit, battery, or software.
- Funding section. Shelf: Funding. Closed until outside money is the task.
- Company or government section. Shelf: Company and government. Off until the inventor is forming a company or selling to the government. This section is not on the main flowchart yet.

Done when plan.md names the active sections, every box whose trigger is true has been opened or listed as the next one, and every section whose trigger is false is still off.

## Fill a checklist from what is already known
(procedure file: sop-checklists.txt)

Procedure: Fill a checklist from what is already known. Revision 2 — October 18, 2026.
NOTE, October 6, 2026: this procedure was written when b-project-manager did the work itself. It is now read by b-analyst. Where it says b-project-manager takes a role, calls or forms a Grok Build session, or writes the sheets, read: b-analyst does it in its own run. Where it disagrees with `an-analyst` (standing context for b-analyst), `an-focus-and-gateways` (Keep the project focused) or `an-stages` (Stages of a project), those win.
Index: the procedure index in `an-office`
Read this when a checklist, questionnaire, or the next sheet in a series is about to be opened. An intern does the pass. The named assistant asks only what is still open.

The inventor should say a thing once. Later paperwork picks it up. Opening a fresh sheet as thirty blank questions is the failure this procedure exists to prevent.

The question library is `check-sheets.txt` (`an-office-files`) and the worksheet check-sheets.csv (`an-office-files`) . Use the sheet that matches the decision. Save the filled copy in that sheet’s subject folder. Do not write answers back onto the public blank.

Send an intern across the project, not across one previous page. It reads plan.md, the concept note, earlier sheets, hat reports, and the explanation field on every answered row. Then it tries every question on the new sheet.

Two fields on every row.

Answer. The words that belong on the form. Short enough to read in the box. This is the field the inventor sees.

Explanation. How that answer was reached. Quote the inventor’s words that matter. Name the earlier item id it came from. Say what was inferred. Say what must not be added. This field is kept and is not read back to the inventor unless they ask to see the reasoning. The next intern reads it first. Intent travels in this field. A short answer alone drops it.

Status is one of these.

- Carried. The project already answered it. Copy the answer forward and rewrite the explanation so it applies to this sheet.
- Needs a look. It carried forward, but this sheet asks something the old wording does not quite cover. Show the carried answer and the one point to confirm.
- Open. Nothing in the project answers it. This is a question for the inventor.
- Conflict. Two records disagree. Show both, with their item ids. Do not pick one.

The intern does not invent a customer, a price, a test result, or a limit. A guess stays open.

If a quality sheet is already answered by the other forms and nothing turned up, say so in one sentence and offer to go over it. If the inventor says no, stop. The file remains the record. This is the usual result of a light quality pass.

If the pass finds one practical problem, mention that problem in one sentence and ask what they want to do. A minimum buy, a lead time, or a part that does not match the quantity are that kind of finding. If they drop it, write that it was brought up and that they do not want planning around it. Then stop. If they want it looked at, take the next step they asked for. The sheets are what cause these findings to be looked for.

Show the sheet when something on it still needs them. The filled boxes stay visible with the open ones. They should be able to read the carried answers and say that those are what they said. Accepting a row is enough. Do not ask that row again. Bring up a quality sheet only for the item that alerted.

Report to the owner with the sheet, and no further.

- Where the filled copy was saved.
- How many rows were carried, how many need a look, and how many are open.
- The open questions, the rows that need a look, and any conflict. A conflict shows both versions.
- One line the assistant can say: “Twenty-four match what you already told us. Six still need an answer.”

The named assistant asks one or two of those remaining questions at a time. A carried row the inventor accepts is finished. A carried row they correct is written down, and only the later sheets that use that row are updated. When an answer arrives, write the short answer and the explanation before the next question. The explanation includes the inventor’s words. Then the intern, or the owning hat, may apply that new answer to the rest of the open rows. A later sentence often closes another question. Do not ask it again.

Moving down the series uses the same pass. The desire “the operator can tell the battery is adequate,” with an explanation that they want a glance and did not ask for a percentage, becomes the specification answer “a visible battery indicator.” The explanation on that row still says “adequate” was their word, so nobody turns it into a fuel gauge. The failure-mode sheet, the test sheet, and the control sheet start from that explanation. Each sheet should open with a handful of new questions, not the whole list.

If the same sheet will be revised for weeks, the owning hat keeps it. The intern is the first pass and any later pass that only reads and proposes. Accepted rows belong to the hat. Follow `sop-interns.txt` (`an-office-files`) for the intern brief, and `an-quality` (Quality-planning series) when the sheet is in the quality series.

Done when the filled copy exists, both fields are written on every carried or answered row, and the inventor has been asked only what the project could not answer.
