---
name: an-meetings-advisors
description: "Use for meetings with an accountant, business attorney, insurance agent, patent attorney or a licensee: the packet."
---

# an-meetings-advisors

Sections: The accountant packet; The business attorney packet; The insurance packet; The patent attorney packet; The licensee packet.

## The accountant packet
(procedure file: sop-packet-accountant.txt)

Procedure: The accountant packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with an accountant, a tax preparer or a bookkeeper (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv; nothing in the ledger, the trip log or the company record (the packet reads them; the gaps are closed in the record itself).
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261208-01-M-accountant-year-end/accountant-packet.html . Template: template-meeting.csv (`an-office-files`) (the rows marked Accountant only)
Goes with: `an-business-record` (The business record) (the ledger, trip log, deadlines and TAX TIME), tax-year.py (`an-office-files`)

WHO IT IS FOR
A CPA, an enrolled agent, a tax preparer or a bookkeeper: the first meeting, to set up how records are kept before the first sale, and the year-end meeting.

WHAT WORRIES THEM
- Are the records complete? Every cost with its receipt and purpose, every trip with its miles, logged when it happened.
- Is business money kept apart from personal money?
- What is the business, legally, and when did it start? The entity, the tax ID, the first sale.
- What questions will they have to answer, and how much work is it?

WHAT GOES IN IT (meeting-packet.py builds these pages from the business record and meeting.csv)
1. For the accountant: the tax year, the gaps still open, the totals (expenses, rows, business miles, categories waiting for their call), the business in brief from the company record, and what we ask of them.
2. Expenses: totals by tax category and by whose money, and the whole year's ledger with each row's purpose, category and whether its receipt is on file.
3. Trips and mileage: every trip with its odometer readings and miles, how many were logged the day they happened, and the year's odometer readings. No mileage rate is applied: that is the accountant's call (standard rate or actual costs).
4. Questions for you: the questions the inventor wants answered (question rows), with what the record shows for each; the "ask accountant" categories listed first; and the tax deadlines from deadlines.csv with their source status.
5. Prep sheet, for the inventor only: the goal, the ask, the walk-away, what they will likely ask, the gaps to close before the meeting, and what is still open in the company record.

BEFORE THE MEETING
- Run python3 tax-year.py AN-Creation/Business <year> and close what it lists: find the receipt (a photo is fine), write the purpose, or mark the row "receipt lost" in its notes. The packet shows the same gaps.
- The ledger, the trip log and the receipts folder go with the packet as files if the accountant wants them.

RULES
- The bot sorts and asks; it does not decide what is deductible, which category a cost belongs in, or how the business should be taxed. Those are the accountant's calls, written into the decision log when made.
- Questions are asked as questions. The packet never states a tax rule, a rate, a threshold or a deadline as fact unless it was read from the source for that year (`an-principles-core` (Trace every spec to its source)).
- Never put full tax IDs, account or card numbers, or passwords in the packet or its folder.
- Don't sign an engagement letter in the room: take the scope and the fee home and compare (`an-principles-bm` (Know your walk-away number)).
- After the meeting: the accountant's answers go in the decision log; the categories they choose go into the ledger; any deadline they give goes in deadlines.csv with them as its source.

## The business attorney packet
(procedure file: sop-packet-attorney.txt)

Procedure: The business attorney packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with a business attorney (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261105-01-M-business-attorney-consult/attorney-packet.html . Template: template-meeting.csv (`an-office-files`) (rows marked Attorney only; this meeting.csv has three more columns: from, by, status)
Goes with: `an-business-record` (b-business-manager) (forming and keeping the company), `an-principles-core` (Rigor scales with whose money is at risk)

WHO IT IS FOR
A business attorney: forming the company and writing its operating agreement, and reading agreements before the inventor signs them (an investor's terms, a buyer's vendor agreement, a license, a company's idea submission form, a supplier's contract). A patent question goes to the patent attorney packet (`an-meetings-advisors` (The patent attorney packet)).

WHAT WORRIES THEM
- What exactly needs their eyes, and by when?
- Who owns what: the company, the invention, any share promised to someone?
- What has already been signed, and what is about to be?
- What is the budget, and is it a flat fee or hourly?

WHAT GOES IN IT (meeting-packet.py builds it: attorney)
1. For the business attorney: whether the company is formed, how many documents need looking at and how many are already signed, the owners of the invention, the first date that matters; what we ask; the business; the legal risks on the business risk register.
2. Documents: every agreement or form, earliest first, with who it is from, what it is and what worries us, the date it matters, and its status (signed, to draft, expected, to prepare). The documents themselves are in the correspondence log.
3. Ownership: who invented it, who owns the invention today, patent filings, and any outside money being discussed.
4. Questions for them, with what the record shows, and the budget.
5. Prep sheet for the inventor.

WHEN TO BUILD IT
Before the first of these comes up: outside money (a loan in writing, a share, a note), forming the company, a company's idea submission form, a license, a buyer's or supplier's agreement. One meeting can cover several documents; list them all, earliest first.

RULES
- The standing advice: on the inventor's own money, forming a simple LLC themselves is their call; other people's money, a license, or an agreement that binds them goes to an attorney before signing (`an-principles-core` (Rigor scales with whose money is at risk)). When money is short, the middle path is a short review of what the bot prepared (SBDC, a law school clinic).
- The bot gathers facts and questions; it never drafts an agreement for signing and never tells the inventor a document is safe to sign.
- Never put full tax IDs, account numbers or passwords in the packet or its folder.
- Don't sign anything in the room; get the fee and the scope in writing before work starts (`an-principles-bm` (Know your walk-away number)).
- After the meeting: their advice goes in the business decision log; each document's status changes in the next packet; each deadline they give goes in deadlines.csv with them as the source; the fee goes on the expense ledger when paid.

## The insurance packet
(procedure file: sop-packet-insurance.txt)

Procedure: The insurance packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with an insurance agent or broker (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv; company.csv (the insurance line) after the meeting.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261109-01-M-insurance-agent-quote/insurance-packet.html . Template: template-meeting.csv (`an-office-files`) (rows marked Insurance only)
Goes with: `an-business-record` (b-business-manager) (8. Insurance), `an-cost-and-risk` (Risk analysis table) , `an-meetings` (The buyer packet) (what buyers ask for)

WHO IT IS FOR
An independent insurance agent or broker quoting product liability and general liability for a small product business. Usually needed before the first shipment, because buyers ask for a certificate.

WHAT WORRIES THEM
- What is the product, who uses it, and how could it hurt someone?
- What has been done about those risks, and what standards and labels apply?
- How much will sell, where, and through whom? Who makes it?
- What is the business, and is there any claims history?

WHAT GOES IN IT (meeting-packet.py builds it: insurance)
1. For the insurance agent: new business, no sales, no claims; the first shipment date, planned first-year sales (plan volume times price, from funding.csv), where it will be sold, how many failure modes could hurt someone; what we ask; what buyers require and where that comes from; the business.
2. The product and how it is used: what it is, who uses it and where, how it is sold, the parts and who makes each (cost sheet), instructions and warnings.
3. Risks, and what has been done: from b-project-manager's risk analysis table, every failure that could hurt someone (severity 8 and up, or an effect that says someone can be hurt), what was done, and the severity before and after; the requirements and standards with their source status (compliance matrix); recalls and incidents on similar products; claims history.
4. Questions for the agent, each with what the record shows.
5. Prep sheet for the inventor.
The product sheets (cost sheet, risk table, compliance matrix) are b-project-manager's: ask for current copies through office-handoff; never retype them.

RULES
- Questions, not assumptions: the packet never states what a policy covers, a limit, a price or a legal requirement for coverage. What a policy covers is in its wording: ask for the wording, not only the quote.
- A buyer's requirement (a limit, being named as additional insured) comes from that buyer's own vendor terms, with the source in the note.
- Every risk the agent sees is the real analysis, including the ones not yet closed (`an-principles-core` (Never invent facts)). Hiding a known risk from an insurer is never an option.
- Run the recall and incident search on similar products before the meeting (library: cpsc-recalls, saferproducts) and record what it found, or that it found nothing, with the date.
- Get two or three quotes and the policy wording before buying; don't buy in the room (`an-principles-bm` (Know your walk-away number)).
- After the meeting: the quote goes in the meeting's folder; the company record's insurance line gets its status; the cost goes on the spending register and the expense ledger when it is paid; the renewal date goes in deadlines.csv.

## The patent attorney packet
(procedure file: sop-packet-patent.txt)

Procedure: The patent attorney packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with a patent attorney or agent, a law school clinic or the USPTO's free help (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: AN-Creation/<business>/patent/<invention>/ (invention-disclosure.csv, prior-art.csv, disclosure-history.csv), the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv.
Templates: template-invention-disclosure.csv (`an-office-files`) , template-prior-art.csv (`an-office-files`) , template-disclosure-history.csv (`an-office-files`) , template-meeting.csv (`an-office-files`) (rows marked Patent only)
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261023-01-M-patent-agent-consult/patent-packet.html
Goes with: `an-routes-and-flow` (When a subject comes up) (the patent road: what is new IP-02, what is already out there IP-03, who contributed IP-04, has it been shown IP-05), `an-principles-bm` (Decide on the patent before showing it publicly)

WHO IT IS FOR
A registered patent attorney or agent, a law school patent clinic, the USPTO Pro Se Assistance Center, or a Patent and Trademark Resource Center: anyone the inventor asks about filing, before or after preparing a filing themselves.

WHAT WORRIES THEM
- What exactly is the invention, and what does the inventor believe is new?
- What is already out there?
- Who has seen it, when, and under what terms? Dates matter more than anything else here.
- Who invented it, and who owns it?
- What does the inventor want from them, and what is the budget?

THE THREE SHEETS (kept during patent preparation, before any packet is needed)
1. invention-disclosure.csv: the title, the problem, how it works, what the inventor believes is new (one row each, never written as a claim), other ways it could be made or used, the drawings and CAD with revisions, when it was conceived and the evidence, the inventors and what each contributed, the owner, and anything filed.
2. prior-art.csv: every document found, with what it shows, how ours may differ (the inventor's belief), how it was found and when, and its source status. A document whose claims have not been read is "from a summary"; dates and owners not read from the document say "to read". Never a document number that was not found in a real search.
3. disclosure-history.csv: every showing or description outside the project, done and planned: date, to whom, what was shown, which revision, NDA or not, the setting, the correspondence folder. Write a row the same day, like the correspondence log; add a planned row as soon as a meeting is set.

WHAT GOES IN THE PACKET (meeting-packet.py builds it: patent)
1. For the attorney or agent: what is filed (usually nothing yet), the first showing without an NDA, the next planned showing without an NDA, and that what any of it means is their call; the invention in brief, what we ask of them, inventors and owner.
2. Invention disclosure: the problem, how it works, what we believe is new, other ways to make or use it, the drawings and CAD, when it was conceived.
3. Prior art found so far, and the searches run.
4. Who has seen it: the disclosure history, done and planned.
5. Questions for them, the budget and scope, and the company.
6. Prep sheet for the inventor: the goal, the ask, the walk-away, what they will likely ask.

RULES
- Never say the invention is new, patentable or protected, and never say a showing did or did not start a clock. Record the facts; the practitioner says what they mean (`an-principles-core` (Trace every spec to its source)).
- A search is a first look, not a patentability opinion and not a freedom-to-operate review.
- Check the practitioner's registration in the USPTO practitioner search before the meeting (library: patent-practitioners), and watch for invention-promotion pitches (library: uspto-scam-prevention).
- Drawings and CAD go to them only after they agree to keep them confidential; most practitioners do by default, so ask.
- On the inventor's own money, preparing the filing themselves and having it reviewed is a sound path; once there is outside money, a practitioner files or reviews (`an-principles-core` (Rigor scales with whose money is at risk)). If the inventor files their own, the patent road's note is said before the package is handed over (`an-routes-and-flow` (When a subject comes up)).
- After the meeting: what they advised goes in the decision log; any deadline they give goes in deadlines.csv with them as its source; any filing goes in invention-disclosure.csv (filed) with its number and date only once it exists.

## The licensee packet
(procedure file: sop-packet-licensee.txt)

Procedure: The licensee packet. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: b-business-manager, built for each meeting with a company that might license the invention (`an-meetings` (Meeting prep)). b-analyst builds it.
May write: the meeting's correspondence folder AN-Creation/<business>/correspondence/YYMMDD-NN-M-slug/ and its row in correspondence.csv; a planned row in disclosure-history.csv as soon as the meeting is set.
Example: https://ancreationoffice.com/example-mousetrap/correspondence/261119-01-M-pest-control-company-licensing/licensee-packet.html . Template: template-meeting.csv (`an-office-files`) (rows marked Licensee only)
Goes with: `an-business-plan-and-money` (Licensing an invention (b-licensing)) (the licensing route: before approaching anyone, the sell sheet, finding licensees, the approach, the deal), `an-meetings-advisors` (The patent attorney packet) (the patent sheets this packet reads)

WHO IT IS FOR
A company that already makes and sells to the same buyers, deciding whether to make and sell the invention and pay the inventor a royalty.

WHAT WORRIES THEM
- Will it sell, and does it fit what we already sell?
- Can we own it? Is there a patent filed, and is anything already out there?
- What will it cost us to make, and is it ready?
- Is this inventor reasonable to deal with?

WHAT GOES IN IT (meeting-packet.py builds it: licensee)
1. Sell sheet: the headline, the problem, who it is for, why people want it, the suggested shelf price, the case pack, how far along it is, the patent status, a picture of the prototype, the contact. It shows what it does, not how it is made (`an-business-plan-and-money` (Licensing an invention (b-licensing)) 2).
2. Why it sells: what people use now, what buyers and users have said, and the cost to make as estimated so far (placeholders say so).
3. Where it stands, and what we'd like to discuss: development, patent status, and the terms to talk about (exclusive or not, royalty, minimums, advance, patent costs, improvements, term) as topics, not offers.
4. Prep sheet, for the inventor only: a warning when nothing is filed, the goal, the ask, the walk-away, their likely questions, an illustrative royalty calculation, and what is still open.

THE ROYALTY CALCULATION
An illustration for the inventor, never shown to the company: a rate, a net price and a volume, each marked illustrative, and the yearly royalty they make. Its purpose is to set expectations before the meeting: licensing usually pays a small share of each sale. The rate comes from a cited source (`an-business-plan-and-money` (Licensing an invention (b-licensing)) 5), never from memory, and is never quoted or agreed in the room.

RULES
- Patent first: "Patent pending" appears only when an application is filed (invention-disclosure.csv). When nothing is filed, the packet says "Not filed" and the prep sheet warns, per `an-business-plan-and-money` (Licensing an invention (b-licensing)) 1.
- Read the company's idea submission terms before sending anything; they can waive rights. Signing them is a one-way door, with an attorney if the money allows.
- Nothing in the packet is an offer. Any agreement is written and reviewed by an attorney before the inventor signs (`an-principles-core` (Rigor scales with whose money is at risk)).
- Never claim sales, a patent or a market that does not exist (`an-principles-bm` (No claims you can't back)).
- Avoid invention-promotion companies that charge to "license" an idea (library: uspto-scam-prevention, ftc-invention-marketing).
- The inventor sends, signs and attends. The bot prepares.
- After the meeting: the notes in the meeting's folder, what they said in market-evidence.csv, the showing marked done in disclosure-history.csv, the next step on the action log.
