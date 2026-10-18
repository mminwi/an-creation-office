---
name: an-correspondence
description: "Use whenever an email, file, meeting or call goes to or comes from anyone outside the company: the correspondence log."
---

Procedure: The correspondence log. Revision 4 — October 18, 2026.
Index: the procedure index in `an-office`
Kept by: both bots, one log for the whole company. b-business-manager keeps the index tidy; b-project-manager files what goes out about an invention (quote packages, CAD, drawings). b-analyst files what arrives.
May write: AN-Creation/<business>/correspondence/ (one folder per correspondence) and AN-Creation/<business>/correspondence.csv (the index).
Template: template-correspondence.csv (`an-office-files`) . Example: https://ancreationoffice.com/example-mousetrap/correspondence.csv and https://ancreationoffice.com/example-mousetrap/correspondence/
Goes with: `an-project-record` (Living and parked documents) , `an-meetings` (Meeting prep)

WHY THIS EXISTS
Months later someone will ask: what did we tell the molder, which revision of the model did they quote from, what did the buyer actually say, what was in the packet the banker got? The correspondence log answers that, exactly, because it keeps what went between the company and anyone outside it, as it was, in the order it happened.

WHAT GOES IN IT
Anything between the company (the inventor, or a bot on their behalf) and someone outside it:
- Emails out and in, with their attachments exactly as sent or received.
- Files transmitted: CAD models, drawings, specifications, quote packages, samples shipped (the packing list), each with its revision in the file name.
- Meetings and calls: the meeting notes (who was there, what was shown, what was conveyed, what they said, what was promised), and anything handed over (the packet, a sell sheet, a sample).
- Letters, signed agreements (NDAs, quotes accepted, purchase orders), filings and their receipts from an agency.
Not in it: the inventor's own conversations with the bots and the analysts' runs. Those are internal and stay in record/ and sessions/.

ONE FOLDER PER CORRESPONDENCE
AN-Creation/<business>/correspondence/YYMMDD-NN-X-slug/
- YYMMDD: the date code, the day it was sent, received or held.
- NN: its place in that day, 01, 02, 03 and on, in the order things happened. Two digits, so a busy day still sorts right.
- X: S for sent (from us to them), R for received (from them to us), M for a meeting or call (both ways; the notes are ours). Letters, not I and O, so they are never mistaken for 1 and 0.
- slug: who and what, in a few words.
Examples: 261017-01-S-molder-a-meeting-request, 261018-01-R-molder-a-nda-signed, 261018-02-S-molder-a-models-rev-x3, 261024-01-M-molder-a-quote-meeting. Folders then sort in the exact order things happened, and the name alone says whether we sent it or got it, and what it was about.
- Inside: the email as sent or received (email.txt, or the saved .eml or PDF, with from, to, date and subject), every attachment as it was, CAD and drawings exactly as transmitted, and for a meeting or call: notes.txt, plus the prep and the packet handed over (`an-meetings` (Meeting prep) builds the packet in this folder).
- A meeting folder is made when the prep starts and is dated the day of the meeting; the notes go in after it.
- Once something has gone out or come in, it is never changed. A correction is a new correspondence, in its own dated folder.

THE INDEX: correspondence.csv (a living document)
One row per folder, written the same day: date, folder, direction (sent, received, meeting or call), with, organization, subject, what was conveyed (one line: what they now know or were told), sent or received (the files, with revisions), promised or next, next date, invention, trip, logged on. Every promise also goes on the action log; every trip on the trip log.

BE INSISTENT
The bot is not in the inventor's inbox, so it asks:
- When it drafts an email or a package and the inventor says it went: "Can you forward me the sent copy, or drop it in Send to the office?" File the copy as sent, not the draft.
- When CAD or drawings go to a supplier: which files and which revision, exactly. A quote is only comparable if you know which revision it was quoted from.
- After every meeting or call: the notes, before anything else (`an-business-record` (The business record) BE INSISTENT).
- When an email from outside is mentioned ("the molder wrote back"): ask for it, and file it.

RULES
- What was conveyed is the point: write it plainly, especially anything about price, dates, patent status, or what the product can do (`an-principles-bm` (No claims you can't back), `an-principles-bm` (Decide on the patent before showing it publicly)).
- Never put passwords, full tax IDs or account numbers in a folder; black them out first.
