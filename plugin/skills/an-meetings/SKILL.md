---
name: an-meetings
description: "Use whenever the owner will meet a buyer, manufacturer, lender, investor or partner: meeting prep and the packet."
---

# an-meetings

Sections: Meeting prep; The buyer packet; The manufacturer packet (request for quote); The lender packet; The investor packet; The partner packet.

## Meeting prep
(procedure file: sop-meeting-prep.txt)

Procedure: Meeting prep. Revision 14 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager. b-analyst drafts the documents and builds the packet.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug/ (the meeting file, the packet, the notes; `an-correspondence`) and its row in correspondence.csv, rows in the Business action log, decision log, contacts.csv and market-evidence.csv, and hand-off lines to b-project-manager.
Builder: meeting-packet.py (`an-office-files`) . Examples: https://ancreationoffice.com/example-mousetrap/correspondence/261028-01-M-distributor-buyer-meeting/buyer-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261024-01-M-molder-a-quote-meeting/manufacturer-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261104-01-M-community-lender-meeting/lender-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261112-01-M-family-investor-meeting/investor-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261208-01-M-accountant-year-end/accountant-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261023-01-M-patent-agent-consult/patent-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261119-01-M-pest-control-company-licensing/licensee-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261109-01-M-insurance-agent-quote/insurance-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261105-01-M-business-attorney-consult/attorney-packet.html , https://ancreationoffice.com/example-mousetrap/correspondence/261102-01-M-partner-tool-and-die-maker/partner-packet.html (each folder has its meeting.csv)
Goes with: `an-principles-bm` (Principles: the Office Manager Bot) , `an-business-plan-and-money` (The funding packet)

WHY THIS EXISTS
An inventor starting a business has to win over people who have seen many inventors before: a store buyer, a molder, a banker, an investor. Each one has worries, and each worry is answered by a document or an analysis the inventor has never had to make. The bot knows what each one will want to see, has the pieces ready, and sends the inventor in prepared.

THE TRIGGER
Any mention of a meeting, a call, a visit, an email to send, or a person to approach: "I'm seeing the farm-supply buyer Thursday." "The molder wants to talk." "Should I go to the bank?" Ask three things, one at a time if they are not already clear: who, when, and what the inventor wants out of it.

WHO'S ACROSS THE TABLE, AND WHAT THEY WANT TO SEE
- Buyer (distributor, store buyer, business customer). Worries: can you deliver, will it sell, will it cause trouble. Packet: `an-meetings` (The buyer packet)
- Manufacturer, toolmaker or supplier. Worries: is this real, can you pay, is the volume believable, are the drawings clear. Packet: `an-meetings` (The manufacturer packet (request for quote))
- Banker or lender. Worries: can you repay, what if you can't, how much of your own money is in. Packet: `an-meetings` (The lender packet)
- Investor (friends and family, an angel, crowdfunding backers). Worries: is it worth it, will you see it through, what happens to my money. Packet: `an-meetings` (The investor packet)
- Grant reviewer, pitch competition or advisor. Worries: is it new, is the plan credible. Packet: the funding packet (`an-business-plan-and-money` (The funding packet)) plus the program's own form (`an-business-plan-and-money` (Funding a project (b-funding))).
- Licensee. Worries: does it sell, can they own it, what will it cost to make. Packet: `an-meetings-advisors` (The licensee packet)
- Accountant, tax preparer or bookkeeper. Worries: are the records complete, is business money kept apart, what will they have to answer. Packet: `an-meetings-advisors` (The accountant packet)
- Patent attorney or agent, a patent clinic or the USPTO's free help. Worries: what exactly is new, what is out there, who has seen it and when, who owns it. Packet: `an-meetings-advisors` (The patent attorney packet)
- Insurance agent or broker. Worries: how could it hurt someone, what has been done about it, how much will sell and through whom. Packet: `an-meetings-advisors` (The insurance packet)
- Business attorney. Worries: what needs their eyes and by when, who owns what, what has been signed. Packet: `an-meetings-advisors` (The business attorney packet)
- Possible partner (a co-founder, a skilled friend, a shop offering help for a share). Worries: is this real, what would I do and get, who decides. Packet: `an-meetings` (The partner packet)

THE STEPS
1. Who, when, what they want out of it. Name the counterpart type from the list.
2. Open the packet procedure for that type. List what that person will want to see.
3. Dust off what exists (parked documents come out for this meeting and go back after, `an-project-record` (Living and parked documents) DUSTING ONE OFF). Check what exists: the business record (AN-Creation/<business>/) and copies of b-project-manager's project record. Ask b-project-manager for current copies of anything product-side through office-handoff (the cost sheet, specs, drawings list, risk table, charter); never retype them.
4. Draft what is missing, honestly. A pre-revenue company has no sales history, no credit and maybe no insurance yet: the packet says so, says what is being done about it, and puts it on the action log. Never invent a fact to fill a gap (`an-principles-core` (Never invent facts)).
5. Write the meeting file, meeting.csv: who, when, the goal, the ask, the walk-away (`an-principles-bm` (Know your walk-away number)), the questions they will likely ask with the answers, and what to leave behind. Two record rows tell the builder where the sheets are, relative to the meeting folder: ../../funding/<invention> (the funding folder, with company.csv, pricing and the copies of b-project-manager's sheets) and ../../<invention>/Office files.
6. Build the packet: python3 meeting-packet.py AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug <buyer|manufacturer|lender|investor|accountant|patent|licensee|insurance|attorney|partner>. The packet's last page is the prep sheet; it is for the inventor and is not handed over. The builder runs on working copies in your Shell; save the packet back with office-save. Without a Shell, write the same pages by hand from the packet procedure's list, from the same sheets.
7. Before the meeting, tell the inventor in a few lines: what is in the packet, the two or three questions most likely to come up, the ask, and anything still missing.
8. After the meeting, before anything else: the meeting notes in the meeting's folder and its row in correspondence.csv, the trip row with the miles if they drove (trips.csv), and every cost with its receipt (expenses.csv), per `an-business-record` (The business record) . Then add what they said or did to market-evidence.csv when it is a signal; update contacts.csv with the next step and date; put every promise on the action log; write any decision to the decision log.

RULES
- Rigor scales with whose money is at risk (`an-principles-core` (Rigor scales with whose money is at risk)). A lender's or investor's money, or a contract to sign, brings the standing advice: get legal and professional counsel before signing.
- The inventor sends, signs and attends. The bot prepares (`an-principles-bm` (The owner acts; the bot drafts)).
- Decide on the patent before showing how it works (`an-principles-bm` (Decide on the patent before showing it publicly)). A buyer packet shows what it does, not how it is made, until there is a filing or an NDA.
- Every spec, rating, certification, rate or term in a packet traces to its source (`an-principles-core` (Trace every spec to its source)). Run check-sources.py on the folders the packet draws from before building it.
- After the meeting, park the sources again in plan.md with the date; the packet itself is kept as given.
- Packets are copies built for one meeting and kept in that meeting's correspondence folder, never changed afterwards, so the correspondence log shows exactly what each person was given and when.

## The buyer packet
(procedure file: sop-packet-buyer.txt)

Procedure: The buyer packet. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each buyer meeting (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug/, and pricing-terms.csv and company.csv in AN-Creation/<business>/funding/<invention>/.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261028-01-M-distributor-buyer-meeting/buyer-packet.html . Templates: template-pricing-terms.csv (`an-office-files`) , template-company.csv (`an-office-files`) , template-meeting.csv (`an-office-files`)

WHO IT IS FOR
A distributor, a store buyer, a catalog, or a business customer deciding whether to carry or buy the product.

WHAT WORRIES THEM
- Will it sell? Who buys it, at what shelf price, and why this one over what they already stock.
- Can you deliver? Lead time, minimum order, case pack, capacity, a supplier behind you.
- Will it cause trouble? Safety, labeling, returns, insurance, and a vendor they can set up.

WHAT GOES IN IT (meeting-packet.py builds these pages from the sheets)
1. Sell sheet: the product in one line, the problem, three or four benefits in the buyer's terms, who it is for, the shelf price, a picture.
2. Pricing and terms: the price waterfall from the shelf price down to the inventor's price (never the inventor's own cost; that stays on the prep sheet), the buyer's margin, case pack, minimum order, lead time, payment terms, shipping terms, returns and warranty (pricing-terms.csv).
3. Product specifications: materials, size and weight, what is in the pack, and how it is labeled. Facts from the cost sheet and the charter; a measurement nobody has taken says "to measure".
4. Company and compliance: the company, the vendor paperwork they will ask for (W-9, insurance certificate, UPC/GTIN barcodes), certifications that apply, and the honest status of each, with the date it will be ready (company.csv, the action log).
5. Prep sheet, for the inventor only: the goal, the ask, the walk-away, the questions they will likely ask with answers, what to leave behind (meeting.csv).

WHAT BUYERS USUALLY ASK FOR, AND THE HONEST ANSWER WHEN IT IS NOT READY
- A certificate of product liability insurance, often $1 million or more, naming them. "Quoting it now; it will be in place before the first shipment."
- UPC or GTIN barcodes (GS1). "We'll license them before packaging is printed."
- A W-9 and vendor setup forms. The company has to exist for these (`an-business-record` (b-business-manager)).
- Samples. Say how many, when, and whether they are production or prototype.
- Proof you can deliver: the supplier behind the product, the lead time, the first-order quantity you can fill.

RULES
- Show what it does, not how it is made, until the patent decision is made (`an-principles-bm` (Decide on the patent before showing it publicly)).
- Never claim sales, customers, reviews or certifications that do not exist (`an-principles-bm` (No claims you can't back)).
- Price from the waterfall and the cost sheet. A price that does not cover the cost is said plainly before the meeting, not discovered in it (`an-principles-bm` (Price on value, never below cost)).

## The manufacturer packet (request for quote)
(procedure file: sop-packet-manufacturer.txt)

Procedure: The manufacturer packet (request for quote). Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager for the meeting; the technical content is b-project-manager's (cost sheet, drawings list, specifications, risk table), sent as copies through office-handoff. b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug/, and a hand-off line to b-project-manager for the quote when it arrives (it goes on the cost sheet).
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261024-01-M-molder-a-quote-meeting/manufacturer-packet.html . Template: template-meeting.csv (`an-office-files`) (its parts row lists the part numbers this supplier quotes)
Goes with: `an-manufacturing` (Manufacturing role) (purchasing and supplier comparison)

WHO IT IS FOR
A molder, a toolmaker, a contract manufacturer, a wire-form or spring maker, a packaging supplier: anyone being asked to quote or make a part.

WHAT WORRIES THEM
- Is this real? A clear package and a real company make a supplier take the quote seriously; a vague one gets a high number or no answer.
- Can you pay? Who pays for tooling, when, and on what terms.
- Is the volume believable? A first order and an annual forecast, with what they are based on.
- Are the drawings and requirements clear? What is critical, what is cosmetic, what tolerance, what material, what inspection.

WHAT GOES IN IT (meeting-packet.py builds these pages from the sheets)
1. Request for quote letter: who we are, what we want quoted, the quantities (first order and annual), when the quote is needed, and how to reply.
2. Parts to quote: every make item from the cost sheet with part number, description, material, quantity per unit, the drawing or CAD file and its revision, and the tooling question (new tool, family mold, cavities).
3. Requirements: the critical features (from the risk table's high-severity rows and the specifications), material and finish, quality expectations (first articles, inspection), packaging and labeling of parts.
4. Commercial terms: tooling ownership (the inventor owns the tool), payment terms asked, NDA, the timeline.
5. Prep sheet, for the inventor only: the goal, the questions the supplier will ask with answers, what to ask them, the walk-away, and how the quote will be compared like for like.

COMPARING QUOTES
Put every quote on the same basis before comparing, one row per part per supplier on quote-comparison.csv (template-quote-comparison.csv (`an-office-files`); the whole job: `an-playbooks` (PLAYBOOK: The first tooling quote)): piece price at the same quantity, tooling, tooling life and ownership, lead time, terms, what is included (inspection, packaging, freight). Write each into the cost sheet as a quote with its date, replacing the placeholder (`an-cost-and-risk` (Cost sheet)). Ask at least two or three suppliers for anything with tooling.

RULES
- An NDA before sending drawings that show how the invention works, unless the patent filing is in (`an-principles-bm` (Decide on the patent before showing it publicly)).
- Quantities are the charter's and the funding plan's; never inflate them to get a better price.
- The inventor owns the tooling they pay for; say so in the request and get it in writing in the purchase order.
- Accepting a quote or placing a tooling order is a one-way door: it goes to the inventor with the comparison, and the spending register gets a committed row when they say yes.

## The lender packet
(procedure file: sop-packet-lender.txt)

Procedure: The lender packet. Revision 5 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each lender meeting (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug/, and cash-flow.csv and company.csv in AN-Creation/<business>/funding/<invention>/.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261104-01-M-community-lender-meeting/lender-packet.html . Templates: template-cash-flow.csv (`an-office-files`) , template-company.csv (`an-office-files`) , template-meeting.csv (`an-office-files`)
Goes with: `an-business-plan-and-money` (Funding a project (b-funding)) (which kind of money fits), `an-meetings` (The investor packet) (the investor's packet, built from the same sheets)

WHO IT IS FOR
A bank, a credit union, an SBA microlender, a community development lender (CDFI), or a state or local loan fund.

WHAT WORRIES THEM
- Can you repay? Lenders lend against cash flow: the money coming in each month has to cover the payment with room to spare. They often look for at least $1.25 of cash available for each $1 of payment.
- What if you can't? Collateral, a personal guarantee, and the owner's own money already in.
- Are you organized? A clear request, a use of funds, a projection with its assumptions, the company's papers.

WHAT GOES IN IT (meeting-packet.py builds these pages from the sheets)
1. Loan request: the amount, what it pays for (use of funds), the term asked, and how it will be repaid.
2. Owner's investment: what the owner has already put in (the spending register's owner rows) and is putting in now. Lenders want the owner to have money at risk too.
3. Cash-flow projection: 12 to 24 months, month by month, with every assumption stated (cash-flow.csv). Sales start when the product can ship, not before.
4. Repayment check: the estimated monthly payment at the stated rate and term against the projected cash available, month by month, and the coverage ratio.
5. Company and documents: the company, its papers, insurance, and the documents the lender will ask for (company.csv), each with its honest status.
6. Risks and what is being done: the High and Medium rows of the business risk register.
7. Prep sheet, for the inventor only: the goal, the ask, the walk-away, the questions a lender will ask with answers.

THE HONEST VERDICT
The packet's first page says whether the projection repays the loan. A pre-revenue company rarely gets a bank loan; say so plainly, and point to what fits the stage: an SBA microloan through a local intermediary (up to $50,000), a community lender, a state loan fund, or own money and grants first (`an-principles-bm` (Fit the money to the stage)). A packet that shows the gap honestly, with the plan to close it, earns a second meeting; one that hides it does not.

WHAT LENDERS USUALLY ASK FOR
A business plan (the one-page plan and this packet), personal and business tax returns, a personal financial statement, bank statements, the company's formation papers and tax ID, any leases or contracts, and a list of collateral. The inventor fills in personal financial details themselves; the bot never stores account numbers, tax IDs in full or passwords.

RULES
- Borrowed money is other people's money: the standing advice applies, and the loan documents are read with an accountant or attorney before signing (`an-principles-core` (Rigor scales with whose money is at risk)).
- Every projected number traces to an assumption written on the sheet. No hockey stick without a reason a lender would accept.

## The investor packet
(procedure file: sop-packet-investor.txt)

Procedure: The investor packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each investor meeting (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv; funding.csv and company.csv in AN-Creation/<business>/funding/<invention>/.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261112-01-M-family-investor-meeting/investor-packet.html . Template: template-meeting.csv (`an-office-files`) (the rows marked Investor only)
Goes with: `an-business-plan-and-money` (Funding a project (b-funding)) (which kind of money fits), `an-business-plan-and-money` (The funding packet) (the packet for an advisor or a grant reviewer, built from the same sheets), `an-principles-bm` (Fit the money to the stage)

WHO IT IS FOR
Someone who might put money in for a share of the outcome: family and friends, an angel investor or an angel group, or the backers of an equity crowdfunding campaign. A loan from a bank or a lender is the lender packet (`an-meetings` (The lender packet)).

WHAT WORRIES THEM
- Is it worth it? Who buys it, what they have said and done so far, and whether each sale makes money.
- Will you see it through? Who is asking, what they have already done, and how much of their own money is in.
- What happens to my money? What it pays for, what it reaches, what they get, how they could get money back, and what happens if it fails.

WHAT GOES IN IT (meeting-packet.py builds these pages from the sheets and meeting.csv)
1. Investment summary: the verdict, the ask, how it is offered, the owner's money in, what each unit clears; what the money does (the use: rows, adding up to the ask); what it reaches; who is asking.
2. The product and the evidence: who it is for, why it sells, what people use now (alternative rows), what people have said and done (market-evidence.csv), and how big it could be: a market size only with its source, otherwise "Not estimated yet".
3. The numbers: price, cost to make one, what each clears, tooling, plan volume, units to pay back the tooling, and the three levers (price, tooling, volume). Computed from the cost sheet and funding.csv, the same math as the funding packet.
4. The plan and the risks: the milestones in date order, and every open business risk with its level and what is being done.
5. The terms and what to know: what is offered, the term rows, how an investor gets money back (in plain words, including the case where it fails), the standing statements below, and the company's status.
6. Prep sheet, for the inventor only: the goal, the ask, the walk-away, the questions they will likely ask with answers, and what is still open.

THE HONEST VERDICT
Page 1 says whether the numbers close (the tooling pays back within the plan volume at the price). When they don't, the packet says so and the ask is for the step that shows whether they can: quotes, tests, buyer feedback, a prototype tool. Not the production molds. Money for production tooling is asked for once the numbers close (`an-principles-bm` (Fit the money to the stage), `an-principles-bm` (Know the unit economics before tooling)).

THE STANDING STATEMENTS (on page 5 of every investor packet)
- This is an early, high-risk investment in a product that is not made yet. It can fail, and the money can be lost. Invest only money you can afford to lose.
- A share of the company, a note or a SAFE is a security. Under federal and state law, every offer and sale of securities, even to one person, including family and friends, has to be registered or fall under an exemption. The terms are set with an attorney before any money changes hands.
  Source: SEC, "Private Companies and the SEC" and "Ready to raise capital" (library: sec-ready, sec-early-investors; https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/private-companies-sec ). Source status: from a summary (search, 2026-10-18; sec.gov did not open from the office's build machine). Open the pages before relying on any detail; states have their own rules too.
- Nothing here is a promise of a return.

RULES
- Other people's money: the standing advice is not optional here. Before any money changes hands, the terms are written and reviewed by an attorney, whatever the amount and however close the family (`an-principles-core` (Rigor scales with whose money is at risk)). The bot never drafts the investment agreement itself as final; it prepares the questions and the facts for the attorney.
- The bot never chooses the instrument (loan, share, note, SAFE) or the valuation. It lays out the options in plain words and the inventor decides with the attorney.
- Family and friends first: say plainly to the inventor that family money that is lost can cost more than money. Put everything in writing, and keep each investor's monthly update in the correspondence log.
- Never claim sales, customers, a market size or a valuation that does not exist (`an-principles-bm` (No claims you can't back), `an-principles-core` (Trace every spec to its source)).
- Show what it does, not how it is made, until the patent decision is made (`an-principles-bm` (Decide on the patent before showing it publicly)).
- The inventor sends, signs and attends. The bot prepares (`an-principles-bm` (The owner acts; the bot drafts)).

## The partner packet
(procedure file: sop-packet-partner.txt)

Procedure: The partner packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with someone who might join the project or the business (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv; a planned row in disclosure-history.csv when they will see how it is made.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261102-01-M-partner-tool-and-die-maker/partner-packet.html . Template: template-meeting.csv (`an-office-files`) (rows marked Partner only)
Goes with: `an-meetings-advisors` (The business attorney packet) (where any arrangement gets written), `an-team` (The bots)

WHO IT IS FOR
Someone who wants to join: a co-founder, a skilled friend or neighbor, a shop or a company offering help, time or money in exchange for a share, a royalty or a role.

WHAT WORRIES THEM
- Is this real? What it is, where it stands, and whether the numbers work.
- What would I do, and what would I get?
- Who decides, and who owns what?

WHAT WORRIES THE INVENTOR (the prep sheet)
- Promising a share in the room, by word or handshake, that is hard to take back.
- Showing how it is made before an NDA.
- A partner who wants more than they bring, or who leaves halfway.

WHAT GOES IN IT (meeting-packet.py builds it: partner)
1. The project in brief: the headline, who it is for, where it stands, the numbers honestly (the same math as the other packets: what each unit clears, the tooling, whether it pays back), the owner's money in, sales so far, the next milestones.
2. What the project needs: each need with why, from the record; and the work on the action log that has no one on it.
3. How working together could look: what they would bring, the ways it could be set up as topics (paid by the job, a royalty, a share once the company exists), who owns what today, and what stays the same until it is written.
4. Prep sheet, for the inventor only: an NDA before drawings, ask for a reference and call them, the goal, the ask, the walk-away, their likely questions, and the questions to ask them.

RULES
- Topics, not offers. No share, royalty or role is promised in the meeting, by word or handshake; the inventor decides afterward, and any arrangement is written and read by an attorney before anyone relies on it (`an-principles-core` (Rigor scales with whose money is at risk), `an-meetings-advisors` (The business attorney packet)).
- A share of a company needs the company formed first.
- The simplest arrangement that works comes first: paying for the work changes no ownership.
- An NDA before they see drawings or CAD (`an-principles-bm` (Decide on the patent before showing it publicly)); a planned row in the disclosure history.
- Never overstate the project to win someone over (`an-principles-bm` (No claims you can't back)): the numbers on page 1 are the same as in every other packet.
- After the meeting: what they said in the meeting's folder; any decision in the business decision log; if they will work on the project, their row in team.csv only once it is agreed in writing.
