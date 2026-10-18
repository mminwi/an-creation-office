---
name: an-folders
description: "Use when making, finding or explaining the project folder layout, moving an older folder, or going back to an earlier version."
---

# an-folders

Sections: project folders; Move an older project folder to the business layout; backups and version control.

## project folders
(procedure file: project-folders.txt)

AN Creation project folders. Revision 18 — October 18, 2026. Human explanation: https://ancreationoffice.com/project-folders.html

One person talks to the system: a solo inventor or entrepreneur. Partners may be involved, but their input comes through that person. One folder holds everything. Inside it, one folder per business, and inside each business, one folder per invention. Everyone starts with one, the default business (Default-org/); an invention not assigned to another business goes there. Each invention has two sides: Your files (the person's) and Office files (the assistants'). Built like a Unix system: files and folders do the work. A queue is a folder of ticket files.

Layout:
AN-Creation/                    shared by every bot
  sops/                         the procedure library: one file per installed version, library-<version>.txt (about 3 MB each, never written over), library.txt (a copy of the newest) and VERSION. Each bot works from the version its office.txt names and moves only when the owner tells that bot to update (`an-version` UPDATING). Kept once, shared, never copied into an office folder
  team.csv                      every bot: its name, its bot id, its business, and the inventions it runs (`an-team` (The bots))
  handoffs/                     one inbox per bot, for-<bot id>.txt. Sending follows the office-handoff skill (`an-team` (The bots) HAND-OFFS)
  offices/<bot id>/             one small folder per Project Manager Bot: its office.txt (Home, "Office version seen", "Last saved", "Working on") and its notes. offices/b-project-manager/ for the first
  ideas.txt                     parked ideas for every business, one line each with the date; not projects yet
  AGENTS.md, CLAUDE.md          (GitHub add-on only, at the top of the repository) how any AI finds the ticket it was sent to work on, from one line; `an-setup-reference` (AGENTS.md for an inventor's an-creation repository)
  Default-org/                  the default business, made at setup even when there is only a Project Manager Bot. Every invention not assigned to another business goes here. A second business gets its own folder beside it, named for that company. Each business's Office Manager Bot works in its folder (`an-office-manager`). In the procedures, AN-Creation/<business>/ is the folder of the business at hand, Default-org/ unless the invention is in another
    office.txt                  that Office Manager Bot's office file
    business.txt, plan.md, actions.csv, brand/ (the brand kit), funding/<invention>/ (the funding packet, `an-business-plan-and-money` (The funding packet)), patent/<invention>/, company.csv, contacts.csv, market-evidence.csv, promo-log.csv, business-decision-log.csv, trips.csv, expenses.csv, deadlines.csv (`an-business-record` (The business record)), procedures/, record/
    correspondence/             the business's correspondence log: a folder per email, file sent, meeting or call, YYMMDD-NN-X-slug (`an-correspondence`)
    correspondence.csv          its index, a row per folder
    All inventions              one line per invention in this business: where it stands, its next step, and which bot runs it
    Fishing Lure/               one folder per invention, inside its business
      Your files/               yours to open, read and change
        READ ME FIRST
        Status                  one page: where it stands, this week, decisions, money, documents, what's coming
        To-do                   three or four paths with a next step on each; you pick
        Project record/         readable copies of the seven required documents: charter and schedule, decisions, actions, cost sheet, spending, risks, change notices (`an-project-record` (The project record))
        Action log              who owes what: your actions and what you're waiting on from others (also on your review page as Your list)
        Plan                    where it stands, decisions, what's next
        Forms/                  filled forms
        Record/                 readable copies of the conversations with the bots; emails, files sent and meeting notes are in the business's correspondence/
        Product/  CAD/  Business/  Company/
        Send to the office/            drop anything here: emails, quotes, photos, notes
        Review/                   web pages for this invention: index.html lists every page, picture and document ever shown; one dated folder per page, never changed
        History/                  earlier copies of Status and Plan, dated
      Office files/              the assistants' side. Please don't edit; tell b-project-manager instead.
        README.txt  PROJECT.txt  plan.md
        actions.csv               the action log master: one row per action or suggestion, never deleted (`an-project-record` (The action log), `an-project-record` (Suggestions and actions))
        cost-sheet.csv            what one unit should cost, every component, tooling separate (`an-cost-and-risk` (Cost sheet))
        risk-table.csv            how it could fail, scored down to the residual (`an-cost-and-risk` (Risk analysis table))
        decision-log.csv          everyday calls, dated, with the reason (`an-project-record` (Decision log))
        project-charter.txt       scope, success criteria, milestones, budget; changed only by ECN (`an-project-record` (The project charter))
        schedule.csv  schedule.html   the charter's dates, forecasts and slips, and the critical path (`an-project-record` (The schedule and the critical path))
        spending.csv              what the project has spent, and whose money (`an-project-record` (The spending register))
        ecn-log.csv  ecn/         engineering change notices (`an-cost-and-risk` (Revisions and engineering change notices))
        forms/                    master forms: answer, context, status for every field
        queue/QUEUE.txt  open/  active/  done/  revisit/
        record/                   the bots' conversations and items dropped in Send to the office that are not correspondence: YYMMDD-NN-R-slug (received), YYMMDD-NN-S-slug (sent), YYMMDD-NN-M-slug (conversation, full text); anything to or from someone outside the company goes in the business's correspondence/; NN is its number in that day, 01, 02... Folders already named the old way (I, O) stay as they are; never rename a record.
        record/INDEX.csv          one line per record item: date, type, summary, fields touched, status
        forms/INDEX.csv           one line per form: what it covers, status counts, last change
        mirror/                   text pulled once from each record item
        sessions/YYMMDD-HHMM-slug/   one per analyst run: prompt, notes, result, DONE.txt
        (no inventor-copy/: Drive version history, or GitHub history, shows what the inventor changed)
        archive/
        business/                 the Office Manager Bot's notes and work about this invention only; readable copies in Your files/Business/ (`an-team` (The bots) WHERE EACH BOT SAVES)

Only the project lives here, plus the procedures: sops/, one file per installed version, each bot on its own until the owner tells it to update (`an-version` UPDATING). The bots read their procedures from it, not from the website. A template copied in to be filled out (a form, the plan) is a project file from then on: dated, and never overwritten by a newer template.

Source of truth: Office files plan.md, forms/ and record/. Your files are produced from them, so they can be rebuilt at any time. Nothing you change or delete there is lost.

Dated folders. Nothing made for you is written over. Each analyst run works in its own dated folder and leaves it as it was. Each page, picture, render, drawing and timeline goes in its own dated folder; an update is a new folder. Before Status or Plan is regenerated, the old copy goes to History/. It uses more space, and it means you can always go back and look.

Your format. At setup b-project-manager asks whether you want plain pages (Markdown, readable on a phone) or Word and Excel files you download. Your files use that format. Office files use whatever suits the assistants. PDF only for things sent out or kept as issued. You can change your mind; the files are regenerated.

The record, two ways. Office files keep everything as received, including full meeting and conversation transcripts. Your files keep the same dated events in readable form: the email, the document, and a typed-up summary of each meeting or conversation instead of the transcript.

Your edits. You may edit your forms, plan or spreadsheets in your own program. At the next conversation b-project-manager notices the changes and checks them with you in a line or two before the master copies change.

Send to the office. Anything dropped there is filed into the record and then cleared. Identical content to something already filed is a duplicate: note where the first copy is, no new task. Changed content is a new version: keep both and check any changed numbers.

The queue. A ticket is a file. Its folder is its status: open, active, done. revisit/ holds "for now" answers named by the date to ask again (261013-company.txt). On that date the file moves to open/.

Analyst runs. Each run works in its own dated folder, writes DONE.txt when it finishes, and is never renamed. Finished runs older than a month move to archive/.

Several inventions. Each has its own folder, plan and queue, inside its business. One b-project-manager can run them all (inventions are folders, not bots); it names the invention it's on and files each conversation in that invention's record. Starting a parked idea: it goes in the default business (Default-org/) unless the owner names another (and which Project Manager Bot runs it, if there is more than one), set up its folder, PROJECT.txt ("Run by: <bot id>"), intake form and first ticket before saying it has started; add it to that business's All inventions with who runs it; mark the idea started in ideas.txt. Answers never cross between inventions. A fact that applies to two, such as your company, is recorded in each, with its source.

Several bots. More than one Project Manager Bot can share the folder, each with its own inventions (for example one for garden tools, one for marine), and each business has one Office Manager Bot. Who runs what is in team.csv, each PROJECT.txt and All inventions. A bot changes only its own inventions; it can read the others. Adding a bot, moving an invention between bots, and adding a second business: `an-team` (The bots) SEVERAL BOTS.

The older layout. Folders made before October 18, 2026 had the inventions, correspondence/, correspondence.csv, All inventions and the Project Manager Bot's office.txt at the top of AN-Creation/. They move once, with the owner's yes: `an-folders` (Move an older project folder to the business layout) . Until then the bot works with them where they are.

Where it lives. One private folder named AN-Creation, wherever the owner wants it, with this layout inside (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it))). A cloud folder (Google Drive, OneDrive, Dropbox) is recommended: it works from a phone, keeps earlier versions, and survives a lost computer. Google Drive is the default when they have no preference. Each bot keeps a working copy of its library version at /workspace/offices/<bot id>/sops/. office-save proves a write by reading it back. For offices or people who write code, the same AN-Creation/ can live in a private GitHub repository named an-creation instead, with one clone per bot at /workspace/offices/<bot id>/an-creation (`an-setup-reference` (GitHub, the optional add-on for code)). office.txt says which: "Home: Google Drive AN-Creation" or "Home: GitHub <username>/an-creation". Every office.txt carries the same Home line. No Home: line: GitHub if /workspace/offices/<bot id>/an-creation is a git clone, otherwise Google Drive.

Backups. Records and outputs are never edited once saved (a change is a new dated file or folder); working files like plan.md and Status are updated in place. Cloud folders like Google Drive and OneDrive keep earlier versions of each file for a while (a plain folder does not, so History/ and the owner's own backup matter more), and a dated copy goes to History/ before any major change (on GitHub, every commit is kept). Going back to an earlier version is a normal part of working with AI. See `an-folders` (backups and version control)

Template. `an-analyst` (# Project plan) contains a blank plan. Do not replace an existing plan with a blank one.

## Move an older project folder to the business layout
(procedure file: sop-folder-move.txt)

Procedure: Move an older project folder to the business layout. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Read this once, when office-startup finds the older layout: an AN-Creation/office.txt at the top, or invention folders, correspondence/, correspondence.csv or All inventions at the top of AN-Creation/. The layout it moves to: `an-folders` (project folders)
Done by: the Project Manager Bot b-project-manager (an Office Manager Bot that finds it first hands it over through office-handoff and works with the folders where they are meanwhile). May write: the folders and files named below, one line in each moved invention's decision-log.csv, one line in Default-org/business-decision-log.csv.

ASK FIRST
Nothing moves without the owner's yes. Say it once, in a few lines: "Your project folder is in the older layout. The new one puts your inventions inside a business folder, Default-org/ (your Business folder, renamed), next to the company files and your correspondence, so more bots or a second business can share it later. Nothing is lost: the Business folder is renamed Default-org and the rest just moves into it. Want me to do it now?" No: write "Folder move: not yet, <date>" in your office.txt, ask again only when the owner asks for a second bot or a second business, and work with the folders where they are.

THE MOVE (one save, in this order)
1. Rename AN-Creation/Business/ to AN-Creation/Default-org/ (the default business); if there is no Business/, make Default-org/. Make AN-Creation/offices/b-project-manager/.
2. Move AN-Creation/office.txt to AN-Creation/offices/b-project-manager/office.txt. Keep every line.
3. Move each invention folder (a folder with Office files/ or Your files/ inside) into AN-Creation/Default-org/. Move AN-Creation/correspondence/, AN-Creation/correspondence.csv and AN-Creation/All inventions into AN-Creation/Default-org/. ideas.txt, team.csv, handoffs/ and sops/ stay at the top.
4. Write "Run by: b-project-manager" in each invention's PROJECT.txt, and a "run by" on each line of All inventions.
5. team.csv: add the columns bot_id, business and runs (`an-team` (The bots) THE TEAM FILE): bot_id the same as covers, business "Default-org", runs "all" for b-project-manager.
6. Older plant office folders (Quality/, Molding/ and so on) stay at the top as they are.
7. One line in each invention's decision-log.csv and in Default-org/business-decision-log.csv: "<date>: project folder moved to the business layout, Business renamed Default-org, owner's yes (`an-folders` (Move an older project folder to the business layout))."
8. Read back: each moved folder opens in its new place and the old place is empty. Then "Last saved" in the new office.txt, and tell the owner in one line it's done.

HOW TO MOVE
- Google Drive, OneDrive and other cloud folders: rename and move folders in place (change the name or the parent); do not copy and delete, so file IDs, sharing and version history stay with it. If your connector cannot move folders, ask the owner to rename and drag them in their Drive or OneDrive window, one step at a time, and check each one afterwards.
- A folder on a computer: move it.
- GitHub: git mv for each (Business to Default-org first), one commit.

OLD POINTERS
Records are never edited, so older records, meeting files and INDEX.csv lines still say AN-Creation/correspondence/..., AN-Creation/<invention>/... or ../../Business/funding/.... Read them as the same folders under AN-Creation/Default-org/ (AN-Creation/Business/... is AN-Creation/Default-org/...). meeting-packet.py finds the moved folders on its own. Nothing is rewritten to change a path.

The Office Manager Bot, after the move: its folder is now AN-Creation/Default-org/, with its office.txt and everything else inside, unchanged. It reads the new paths at its next conversation; send it a hand-off line saying the folder was renamed.

OLDER NAMES (once, no need to ask)
If an invention still has a "Soren's files" folder, rename it to "Office files", and "Your files/Send to Soren" to "Your files/Send to the office"; if AN-Creation/Business or AN-Creation/Default-org still has any of for-project-manager.txt, for-business-manager.txt, for-soren.txt or for-kasper.txt, move every line into the matching inbox (for-project-manager and for-soren into AN-Creation/handoffs/for-b-project-manager.txt; for-business-manager and for-kasper into AN-Creation/handoffs/for-b-business-manager.txt), ending each moved line with "| open" unless it is already on a plan, then delete the old file (`an-team` (The bots) HAND-OFFS); if AN-Creation/team.csv is missing, write it from template-team.csv (`an-office-files`) with the name you go by now covering every role. One commit, no message to the inventor beyond one line saying the office was tidied.

## backups and version control
(procedure file: version-control.txt)

AN Creation backups and version control. Revision 10 — October 18, 2026. Human page: https://ancreationoffice.com/version-control.html
The project folder lives where the owner chose (Office version 261018.14): a cloud folder like Google Drive or OneDrive is recommended, and Google Drive is the default when they have no preference. GitHub stays a full, supported option for offices or people who write code; offices already on GitHub keep working as written under IF THIS OFFICE USES GITHUB.

WHY
AI is new, and it goofs up: a file gets overwritten, two versions get mixed, a chat gets cleared, a bot gets deleted. In practice, going back to an earlier version is close to a daily event. So the office never depends on one copy of anything, and never on the chat.

HOW IT'S KEPT
- The project is one private folder, AN-Creation, in the home the owner chose (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it))). office.txt says which: "Home: Google Drive AN-Creation", "Home: OneDrive AN-Creation", "Home: Folder <path>". Every home that isn't GitHub saves the same way (SAVING ON DRIVE). If it says "Home: GitHub", follow IF THIS OFFICE USES GITHUB below instead. No Home: line yet (offices set up before 261014.2): GitHub if /workspace/offices/<bot id>/an-creation is a git clone, otherwise Google Drive; write the Home: line at the next save.
- The procedure library is in AN-Creation/sops/: one file per installed version, library-<version>.txt, never written over, plus library.txt (a copy of the newest) and VERSION. Each bot works from the version its office.txt names and moves only when the owner tells it to update (`an-version` UPDATING). Each file is about 3 MB. Its first line is the Office version. Each file follows after a marker line `=== FILE: <path> ===`, including the resource library. Each office reads its version from its working copy in /workspace/offices/<bot id>/sops/, one section at a time: awk '$0=="=== FILE: `an-project-manager` ==="{p=1;next} /^=== FILE: /{p=0} p' library-<version>.txt. An update saves a new library-<version>.txt beside the others (`an-version` UPDATING). The rule is `an-version`
- Two kinds of files (D-029). Working files are updated in place: office.txt, business.txt, plan.md, actions.csv, team.csv, the hand-off inboxes, Status and Plan. Before a major change to one, a dated copy goes to History/ ("<name> YYMMDD-HHMM"). Records and outputs are never edited once saved: documents, drawings, pages, analyst runs, record/ entries, released revisions. A change is a new dated file.
- The record. Every conversation and every analyst run is saved in record/ and sessions/. Anything not yet saved is only in the chat.
Say it to the owner once, in a line: "Your work is saved to your project folder as we go, and I keep a dated copy before any big change."

SAVING (every office and b-analyst)
Follow the office-save skill. This is the office rule it carries out.
- Read a working file fresh just before you change it, then write it in place (same name, same folder).
- Before a major change, keep a dated copy in History/.
- After every write, read the file back and check it matches. A write you did not read back is not confirmed.
- Quiet when it works. A failed save is one plain line to the owner. Never call it saved when the read-back failed.
- If the save changed plan.md or actions.csv, rewrite office.txt "Working on" in one line in that same save.
- "Last saved", only after the read-back matches: <date time CT>, <file name> (<Drive file id>), read back OK. On GitHub the id is the commit. Never write that line when the read-back failed.
- Files over about 50 MB: leave them where they are and record where the original lives.
Setup: `an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it))

IF THIS OFFICE USES GITHUB (code offices, and offices already set up on GitHub)
- Your own clone: /workspace/offices/<your bot id>/an-creation. Never a shared clone, and never /workspace/repo. The GitHub connector is read-only; saving is git and gh in your Shell.
- One commit per turn. pull --rebase before the commit; if the push is rejected, pull --rebase and push again. After the push, read the file back with gh. Unpushed work is not saved.
- Never force-push main. A work branch is named by role (b-project-manager/<topic>) and deleted after it merges.
- The library is in AN-Creation/sops/ in the repository, one file per installed version; an update is one download and one commit.
- "Last saved" uses the commit in place of a Drive file id, and only after the gh read-back matches. Files over about 50 MB stay out of the repository.
Setup: `an-setup-reference` (GitHub, the optional add-on for code)

IF SOMETHING GOES WRONG
- A file got overwritten, mixed up or deleted: look at the earlier dated files and History/ first, then the file's version history in Google Drive or OneDrive (or on GitHub; a plain folder has only History/ and whatever backup the owner keeps), find the last good version, restore it as a new save, and say what was restored.
- A chat got cleared, or a bot was deleted and made again: everything that was saved is still there. The new bot looks for the AN-Creation folder first, reads its office.txt (its "Last saved" line), All inventions in its business folder, PROJECT.txt, plan.md and the latest status, and carries on from the last saved checkpoint. Anything said after the last save was only in the old chat: ask the owner about it.
- They lost their phone: sign in to Google (and GitHub, if used) and their AI app on the new one. The project is in the cloud.

NEVER
- Never share the AN-Creation folder publicly or with "anyone with the link". Never make a GitHub repository public.
- Never put passwords, keys, an SSN, or bank or card numbers in any project file, issue or commit message.
- A saved version is not an approval. History does not replace the revision and change records (`an-cost-and-risk` (Revisions and engineering change notices)) or the record of what was sent to whom.
- Big CAD, video and image files (over about 50 MB): record where they are.

Sources: Google Drive version history https://support.google.com/drive/answer/2409045 ; GitHub repositories https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories ; file history https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file ; large files https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github .
