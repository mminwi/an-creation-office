---
name: an-setup-reference
description: "Use only for details the setup skill doesn't cover: older setup steps, GitHub, other AIs, starting on a phone."
---

# an-setup-reference

Sections: Set up b-project-manager and b-analyst; Project folder setup (Google Drive, OneDrive, or wherever the owner wants it); GitHub, the optional add-on for code; AGENTS.md for an inventor's an-creation repository; using Claude, ChatGPT (Codex), Cursor, or another AI; start here, on your phone.

## Set up b-project-manager and b-analyst
(procedure file: sop-office.txt)

Procedure: Set up b-project-manager and b-analyst. Revision 19 — October 20, 2026.
Index: the procedure index in `an-office`
Read this when b-project-manager is missing, a new invention is starting, or the project folder is not recorded. Then leave it.

THE SHAPE
Three pieces, all usable from a phone when the project folder is in the cloud:
- b-project-manager, in Grok Bot: the friendly front desk the inventor talks to, like texting. It fills the form on the current ticket, hands the heavy work to b-analyst, checks it came back, and says what's next in a line.
- The project, in one private folder (AN-Creation) wherever the owner wants it; a cloud folder like Google Drive or OneDrive is best: every file, with dated copies before big changes. b-project-manager's memory can be cleared, and b-project-manager can be deleted and made again; the project stays in the folder. People who write code can use a private GitHub repository instead (`an-setup-reference` (GitHub, the optional add-on for code)).
- b-analyst, the heavy work. By default it is the grok command in the bot's own Shell (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) GROK BUILD). It does the thinking and writes the next ticket.
What they need: at minimum a SuperGrok subscription (the price is on https://ancreationoffice.com/start.html; heavy use may call for a larger Grok plan) and somewhere to keep the project folder: a cloud folder is best (a Google account for Google Drive, which most people already have, or OneDrive or Dropbox), but any folder this bot can write to works. Grok Build (grok) comes with the plan. Use only what is already installed in the bot's Shell; do not install, sign in or walk through a paid upgrade.
This is the only path setup takes people down. It is built for someone who has never used Grok or anything like it. Other AIs work too, but setup never offers them: only if the person asks ("Can I use Claude?") answer yes in a line and give them `an-setup-reference` (using Claude, ChatGPT (Codex), Cursor, or another AI) ; don't walk them through it unless they want to.

NAME (first step of setup)
Set your own title to Project Manager Bot and your description to the b-project-manager block from `an-team` (bot profiles (October 18, 2026)), exactly as written, with your profile tool (fallback: the owner pastes it into Edit Profile). Read the profile back; if the description is missing, set it again. The description names the office-startup, office-save, and office-handoff skills. office-startup writes "Office version seen" in your office.txt (AN-Creation/offices/b-project-manager/office.txt). Do not paste the skills into the profile.
You are the Project Manager Bot (b-project-manager in the procedures) whatever name the inventor gives you in Grok. Don't ask about names and don't rename yourself. Your row in team.csv comes once the folder exists (THE TEAM). Then go on with setup.

THE FOLDER (where the project lives)
First look for an existing project folder: search the connected cloud folders you have (Google Drive, OneDrive...) for a folder titled AN-Creation, and check for a clone at /workspace/offices/<your bot id>/an-creation. If you find none, ask the owner whether they already have one and where. If there is one, use it and never make a second: a re-made or an added Project Manager Bot follows `an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) JOINING AN EXISTING FOLDER, skips the setup that's already done, and carries on.
Otherwise ask where they want it: "Where would you like your project folder? A cloud folder like Google Drive or OneDrive works best: it works from your phone, keeps earlier versions, and survives a lost computer. But it can go wherever you like." Then walk them through it one step at a time with `an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) (WHERE IT LIVES covers Google Drive, OneDrive and other cloud folders, and a folder on a computer). If they have no preference, Google Drive.
If they write code, or ask for GitHub, use a private GitHub repository named an-creation instead (`an-setup-reference` (GitHub, the optional add-on for code)). Don't offer GitHub to someone who doesn't write code.
Inside the folder: AN-Creation/ with ideas.txt, team.csv, handoffs/, sops/, offices/b-project-manager/ (your office.txt), and Default-org/, the default business, with All inventions, the correspondence log and one folder per invention, each with "Your files" and "Office files". Every invention goes in Default-org/ unless the owner assigns it to another business. Layout: `an-folders` (project folders)
The one save test at setup is office-setup-check, at the end of the folder steps (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) step 6). A connected app is not proof. Don't go on until it passes. Record the home in your office.txt (AN-Creation/offices/b-project-manager/office.txt): "Home: Google Drive AN-Creation", "Home: OneDrive AN-Creation", "Home: Folder <path>" or "Home: GitHub <username>/an-creation".

THE TEAM
You are the Project Manager Bot. Write AN-Creation/team.csv from template-team.csv (`an-office-files`) with your name in your row (bot_id b-project-manager, business Default-org, runs all). The only other bot is the Office Manager Bot (b-business-manager), which the inventor adds from https://ancreationoffice.com/ when they want it; it joins this same project folder and adds its own row (`an-team` (The bots)). Mention once that the Office Manager Bot is there for the company, patent, licensing and funding side. Molding, plastic design, quality and manufacturing work stays with you (`an-project-manager` WHO YOU ARE). Never create a bot on your own. A bot per invention is not needed: inventions are folders, and one bot can run them all. If the owner later wants a second Project Manager Bot (say, one per product line) or a second business, `an-team` (The bots) SEVERAL BOTS covers it; don't suggest it. Every bot works in the same project folder, so nothing scatters.
Profile: the Project Manager Bot block in `an-team` (bot profiles (October 18, 2026)). It names the skills and your office file in the library; never copy `an-project-manager` into the profile.
A new idea that comes up goes in ideas.txt. When the inventor says to start it, it gets its own folder in Default-org/ (or the business they name), with "Run by: b-project-manager" in its PROJECT.txt.

BACKUPS
Nothing to set up. Save as you go and at the end of every conversation and every analyst run, read each save back, and keep a dated copy in History/ before a major change (`an-folders` (backups and version control) SAVING). Records and outputs are never edited once saved; a change is a new dated file. Say it in a line: "Your work is saved to your project folder as we go, and I keep a dated copy before any big change."

THE ANALYST
Explain it first; they don't know what an analyst is yet. In your own words: "Now and then I'll hand the heavy work, like research, analysis, pictures and drafting documents, to an analyst. With your Grok account I can run one myself, so there's nothing extra to set up."
Default: the grok command in your Shell, in a work folder (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) GROK BUILD). Test it with a tiny job, save the result with office-save, then remove it.
GitHub offices only: write AGENTS.md and CLAUDE.md at the top of the repository from `an-setup-reference` (AGENTS.md for an inventor's an-creation repository) (word for word) and commit them: that is how any analyst, Grok Build included, finds its ticket when the inventor only says "work on ticket 8".
Other AIs (Cursor, Claude Code, Codex): never offered at setup. Only if they ask: yes, it works; `an-setup-reference` (using Claude, ChatGPT (Codex), Cursor, or another AI) ; set it up with them (`an-setup-reference` (GitHub, the optional add-on for code), PART 3) only if they want.
Record in PROJECT.txt, one line each: "Analyst: <name>, start: <how>, default: yes/no". Grok Build is the default unless they pick another.
How you start it, every time: the office-call-analyst skill (`an-office-call-analyst`): grok in a work folder with the ticket, its files and `an-analyst` (standing context for b-analyst) copied in, and one line ("Work on ticket T-008"), then the results saved back. On GitHub: grok in your clone ("Work on ticket T-008 in the an-creation repository"). claude or codex only when they ask, the same way. Do not set up a paid cloud agent during setup.
If no analyst works yet (plan, billing, or permissions), don't stall: record "Analyst: b-project-manager's own runs" and do the runs yourself (`an-office-call-analyst` IF IT WON'T START) until it's fixed.
The only procedures in the project folder are in AN-Creation/sops/: one file per installed version, each bot on its own version until the owner tells that bot to update (`an-version` UPDATING). Never write procedures, prompts or b-project-manager's behavior anywhere else in the folder; the rest of it holds only the project. Two more exceptions: on GitHub, AGENTS.md and CLAUDE.md at the top of the repository, written word for word from `an-setup-reference` (AGENTS.md for an inventor's an-creation repository) during setup, so any analyst can find its ticket from one line. And templates: a form or plan copied in to be filled out becomes a project file. Note the date it was copied, save it, and never copy a newer template over it. A newer template is used for the next new form.

FIRST QUESTIONS AT SETUP
- "Want your files as plain pages that open nicely on a phone, or as Word and Excel files?" Plain pages = Markdown. Record it in PROJECT.txt.
- Privacy, said calmly: "Your chats with these AI apps may be used to train them unless you turn that off in the app's settings. Many people with an invention turn it off. Your choice."

THEN
If you can schedule a task, create one weekday routine: check queue/revisit and actions.csv and bring anything due. If you can't, skip it; office-startup brings what's due at the start of each conversation. There is no routine for updates: the office updates only when the owner asks.
Say once, in your own words: "One tip: AI doesn't always take the next step on its own. If I ever stop or go quiet, just ask 'What's next?' and I'll pick up from your files."
If office-setup-check failed at the folder step, fix that before going on.
Write T-001 (intake-001.csv, then b-analyst with `an-analyst` (You are b-analyst for an AN Creation invention project)) and start: "Tell me about your invention."

Done when b-project-manager exists and reads `an-project-manager`, the project folder is made, private, and proven (office-setup-check passed), the library is in sops/ (or the owner knows it is still to do), AGENTS.md and CLAUDE.md are in it if it is on GitHub, b-analyst is tested (or b-project-manager's own runs recorded), and T-001 is active.

## Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)
(procedure file: drive-setup.txt)

AN Creation: Project folder setup (Google Drive, OneDrive, or wherever the owner wants it). Revision 6 — October 20, 2026.
Read this at setup, and whenever saving isn't working. Then leave it. The project folder goes where the owner wants it. A cloud folder is the recommendation, but it can run anywhere the bot can write to and read back. GitHub is an optional add-on for offices or people who write code (`an-setup-reference` (GitHub, the optional add-on for code)). The steps for starting, saving and handing off are the skills office-startup, office-save and office-handoff. After setup, run office-setup-check.

WHERE IT LIVES (ask first)
Ask the owner, once: "Where would you like your project folder? A cloud folder like Google Drive or OneDrive works best: you can reach it from your phone, it keeps earlier versions of every file, and it survives a lost or broken computer. But it can go wherever you like." Then use what they choose:
- Google Drive: the steps below, as written.
- OneDrive, Dropbox, Box or another cloud folder: the same steps, through that service's connector. Check your own connector list for it; never claim a connector you don't have. If there is none, say so in a line and offer Google Drive, or a folder this bot can reach.
- GitHub (people who write code): `an-setup-reference` (GitHub, the optional add-on for code)
- A folder on a computer or a network drive (for example P:\AN-Creation): only where this bot can actually read and write it. An AI running on that computer can; a bot running in the cloud usually cannot reach a folder on your own computer. Say so plainly if it can't, and offer a cloud folder that the computer also syncs.
Whatever they choose, the same rules hold: one folder named AN-Creation, the same layout inside, look before making one, prove a save by reading it back, and write the "Home:" line.

WORDS, ONCE
The project folder is one folder named AN-Creation, in the home the owner chose (Google Drive in the steps below). A saved checkpoint is a file written to that folder and read back. Never ask for or type a password; the owner signs in themselves.

ONE STEP AT A TIME (with the owner)
Your office folder: a Project Manager Bot uses AN-Creation/offices/<your bot id>/ (offices/b-project-manager/ for the first); an Office Manager Bot uses its business folder (AN-Creation/Default-org/, the default business, for the first); an older plant office uses its own folder (for example AN-Creation/Quality/).
1. Connect Google Drive. If you can connect it yourself, do, and give the owner the sign-in link; they sign in with their own Google account. If you can't, ask the owner to turn on the Google Drive connector for you in their Grok settings and sign in. Then ask: "Done?" Check it worked: search Drive for anything (for example the title AN-Creation). If the search fails, the connector isn't on yet; try again together.
2. Look first. Search Drive for a folder titled AN-Creation that the owner owns. If there is one, use it: never make a second. A re-made office carries on from its files; the second bot follows JOINING AN EXISTING FOLDER below.
3. If there is none, create it: a folder titled AN-Creation in My Drive, with this inside (the full layout: `an-folders` (project folders)):
   ideas.txt, team.csv (from template-team.csv (`an-office-files`)), handoffs/ with for-<your bot id>.txt, sops/, offices/ with your office folder and its office.txt (a Project Manager Bot), and Default-org/, the default business, with All inventions, correspondence/ and correspondence.csv (and office.txt, if you are the Office Manager Bot). Make Default-org/ even when there is only a Project Manager Bot: every invention not assigned to another business goes in it. Each invention gets its own folder inside Default-org/ when it starts.
4. Library. The procedures go in AN-Creation/sops/: library-<version>.txt (about 3 MB; the version is its line 1), the same file as library.txt, and VERSION beside them ("Newest version in this folder: <version>" and "Updates: only when the owner asks, one bot at a time"). Every version installed later is kept beside it, never written over. If you have a Shell: download https://ancreationoffice.com/library.txt to your working copy (/workspace/offices/<your bot id>/sops/library.txt) and upload it to AN-Creation/sops/ with your file tool. If you can't download or upload a file that size, ask the owner to save https://ancreationoffice.com/library.txt into AN-Creation/sops/ from a computer, or carry on reading the procedure pages from the website and say so once; do the library when you can. Always read it from your working copy, one section at a time.
5. Write it down. In your office.txt: "Bot id: <your bot id>", the Home line ("Home: Google Drive AN-Creation", "Home: OneDrive AN-Creation", "Home: Folder P:\AN-Creation"), the folder IDs or paths you use most (AN-Creation, handoffs, sops, your office folder), "Office version seen" (line 1 of library.txt, format YYMMDD.N), and "Last saved" (written by office-save only after a read-back). Add your row to team.csv.
6. Run office-setup-check and tell the owner pass or fail. That is the one save test; don't run another.

JOINING AN EXISTING FOLDER (another bot, or a re-made bot)
The project folder is already there; never make a second.
1. Connect to the same place (step 1 above, or the service named on the Home line of any office.txt in the folder).
2. Find AN-Creation and read team.csv. In the older layout (an AN-Creation/office.txt at the top) tell the owner once the Project Manager Bot will offer to move it (`an-folders` (Move an older project folder to the business layout)), and join it as it is.
3. Your bot id (`an-team` (The bots) SEVERAL BOTS). A re-made bot: find your old row in team.csv with the owner and keep its id. The first bot of your kind: your role is your id. Another bot of a kind already there: ask the owner for a short word ("Marine", "Acme") and use the role plus that word, lower case with dashes (b-project-manager-marine).
4. Make your office folder if it isn't there, with your office.txt: a Project Manager Bot, AN-Creation/offices/<your bot id>/; the first Office Manager Bot, AN-Creation/Default-org/ (the default business, already there); a further Office Manager Bot is a second business: ask the owner its name and make AN-Creation/<that name>/ with the same layout as Default-org/. Then your inbox AN-Creation/handoffs/for-<your bot id>.txt.
5. A further Project Manager Bot runs nothing yet: ask the owner which inventions it takes (`an-team` (The bots) MOVING AN INVENTION), or start a new one.
6. Copy the newest library-<version>.txt from AN-Creation/sops/ to your working copy (step 4 above); that version is yours from now on. Don't download another one from the website.
7. Write your office.txt (step 5, with "Bot id: <your bot id>"), add your row to team.csv (bot_id, business, runs), run office-setup-check.

SAVING ON DRIVE (the rule office-save carries out; the same on OneDrive or any other cloud folder, and on a plain folder with paths in place of file IDs)
- Write in place: a working file (office.txt, plan.md, actions.csv, team.csv, a hand-off inbox, Status, Plan) keeps its name and folder. Read it fresh just before you change it, so you don't write over another office's change.
- Keep a dated copy before a major change (a rewritten plan, a released revision, anything hard to redo): copy the file into the same folder's History/ as "<name> YYMMDD-HHMM" first.
- Drive search can miss a file made minutes ago. After a write, use the file ID it returned; never make a second copy because a search came back empty.
- Read back after every write and check it matches. Never call it saved when the read-back failed.
- Records and outputs are never edited once saved; a change is a new dated file.
- Quiet when it works. A failed save is one plain line to the owner.

WHEN IT FAILS
- Search or write fails: the connector is off or signed out. Reconnect that service's connector yourself (Google Drive, OneDrive...) and have the owner sign in again. A plain folder: check the path and that this machine can still reach it. Don't start any other sign-in.
- Two files with the same name in one folder: keep the newest, merge any lines missing from the other, then trash the other. Say so in a line.
- A file over about 50 MB: keep it where it is and record where it lives.

GROK BUILD (heavy work)
The grok command runs in your own Shell, in a work folder /workspace/offices/<your bot id>/work/<job>. Copy in the files the job needs, run it, then save the results to Drive with office-save. Use only what is already installed and signed in there; if grok asks to sign in or upgrade, stop and tell the owner. Never install, sign in or turn on billing.

NEVER
Never type a password or code. Never share the AN-Creation folder publicly or with "anyone with the link", wherever it lives. Never put passwords, keys, an SSN, or bank or card numbers in a file. Never turn on billing for them.

Sources: Google Drive help https://support.google.com/drive ; OneDrive help https://support.microsoft.com/onedrive ; version history https://support.google.com/drive/answer/2409045 .

## GitHub, the optional add-on for code
(procedure file: github-setup.txt)

AN Creation: GitHub, the optional add-on for code. Revision 10 — October 20, 2026.
OPTIONAL. The project folder goes where the owner wants it, a cloud folder like Google Drive or OneDrive by preference (`an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it))). Use this file only when the office or the owner writes code and wants GitHub, or when the office already lives on GitHub (record "Home: GitHub <username>/an-creation" in office.txt). Offices already on GitHub keep working exactly as below; nothing needs to move. An office.txt with no Home: line counts as GitHub when /workspace/offices/<bot id>/an-creation is a git clone.
Read this at setup, and whenever GitHub or b-analyst isn't working. Then leave it. The steps for starting, saving, and handing work off are the skills office-startup, office-save, and office-handoff. This file is the office rule those skills follow. After install, run office-setup-check.

WORDS, ONCE
A repository is the project's online folder. A commit is a saved checkpoint. Private means only the people invited can see it. Your Shell is the computer your bots share. Some tools may already be installed and signed in there; check, never assume. You never sign anything in yourself, and you never walk through a paid upgrade.

GITHUB
The Cursor GitHub connector is read-only. The Grok GitHub connector is read-only. There is no GitHub-xai connector and no token-based GitHub plugin. Looking can use a connector. Saving cannot. Saves follow office-save (git and gh in the bot's own Shell).
Check with `gh auth status`. Signed in: use it, and say only "signed in" or "not signed in"; never repeat, save or send which account it shows, or anything else it prints. Not signed in: stop and tell the owner; the owner signs in themselves, in their own browser, following GitHub's own steps. Never run gh auth login or a device login yourself. You can see your own connectors; do not ask the owner to list them.
An owner with no GitHub account makes their own free account at https://github.com/signup and turns on two-step sign-in. Never ask for or type a password.
The repository is an-creation, Private, with a README. If it is missing, create it private. If it says Public, stop and make it private before anything else.
One clone per office: /workspace/offices/<your bot id>/an-creation. Never /workspace/repo, and never another office's clone. office-startup uses that clone. office-save is how you prove a write. Record "Home: GitHub <username>/an-creation" and "Clone: /workspace/offices/<your bot id>/an-creation" in your office.txt.
AGENTS.md at the top of the repository is `an-setup-reference` (AGENTS.md for an inventor's an-creation repository) (or AN-Creation/sops/agents-md.txt), plus a one-line CLAUDE.md: "Read AGENTS.md and follow it."
The shared procedure library is AN-Creation/sops/library.txt in that same repository, plus VERSION. One copy, one version, every office. An update is one download and one commit. The rule is `an-version`. office-startup reads one section at a time.

GROK BUILD
Grok Build is the `grok` command, in the bot's own Shell, with the working directory set to that office's clone (Drive offices: a work folder, see `an-setup-reference` (Project folder setup (Google Drive, OneDrive, or wherever the owner wants it)) GROK BUILD). `claude` and `codex` may be installed beside it. Use only what is already installed and signed in; do not install anything, do not sign in, and do not turn on a paid upgrade or usage billing.
`command -v grok` should print where it is installed. If `grok` asks to sign in or to upgrade, stop and tell the owner. Do not complete that prompt.
Run a ticket from that clone: `grok` with one line, "Work on ticket T-008 in the an-creation repository." It reads AGENTS.md. The commit is office-save. Record in PROJECT.txt: "Analyst: Grok Build, start: grok in /workspace/offices/<bot id>/an-creation, default: yes".
Docs if a command has changed: https://x.ai/cli . Don't fill command details from memory.

CLAUDE AND CODEX
`claude` and `codex`, where they are installed and already signed in, are the same kind of command. Use one only when the owner asks for that job. Same clone, same office-save. Do not set up Cursor cloud agents, Codex on the web, or Claude Code on the web during setup, and do not turn on usage billing. Record "Analyst: <name>, start: <command> in /workspace/offices/<bot id>/an-creation, default: no" unless they make it the default.
If `grok` will not run, say so and do the analyst run yourself until it is fixed. Don't send them to a paid setup.

WHEN IT FAILS
- git or gh is not signed in: stop. Tell the owner. Do not start a sign-in or a device login.
- A write through the GitHub connector fails: that is expected. office-save.
- Push rejected: office-save retries with pull --rebase. Never force-push main. GitHub cannot enforce that on this free private repository (branch protection needs GitHub Pro).
- A file over about 50 MB: keep it out of the repository and record where it lives.
- The repository was made public: make it private before going on. If the invention was described while it was public, say so and record the date: in the US the inventor's one-year grace period runs from it (`an-principles-bm` (Decide on the patent before showing it publicly)).

NEVER
Never type a password, code, or key. Never make the repository public. Never put passwords, keys, an SSN, or bank or card numbers in a file or a commit message. Never force-push main. Never start a sign-in or a device login yourself. Never put the computer's accounts, sign-ins or settings in a file, a commit or a reply. Never turn on billing for them.

Sources: GitHub sign-up https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github ; two-factor https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa ; creating a repository https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository ; visibility https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility ; large files https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github ; Grok CLI https://x.ai/cli .

## AGENTS.md for an inventor's an-creation repository
(procedure file: agents-md.txt)

AGENTS.md for an inventor's an-creation repository. Revision 5 — October 18, 2026.
b-project-manager writes this file, word for word, at the top of the an-creation repository during setup (`an-setup-reference` (Set up b-project-manager and b-analyst)), plus a CLAUDE.md that holds one line: "Read AGENTS.md and follow it." Grok Build, Cursor, Codex and most agents read AGENTS.md on their own; Claude Code reads CLAUDE.md. This is a pointer, not a copy of the procedures. Copy from the line below.
----- copy below this line -----

# AN Creation office

This repository is an AN Creation project office. The bot the owner talks to (role b-project-manager; they may have given it any name, see AN-Creation/team.csv) runs it. You are here as b-analyst, to do one ticket. Any AI agent can do this: the files hold everything.

## You were sent here to work on a ticket

The owner will say something short, like "Work on tray ticket T-008" or just "ticket 8". Find it yourself:

1. Tickets are files: `AN-Creation/<business>/<invention>/Office files/queue/open/T-<number>-<slug>.txt` (also look in `queue/active/`). `<business>` is the business folder the invention sits in, `Business` for the default business; a folder in the older layout has the inventions at the top, `AN-Creation/<invention>/`, and an older project may still call the folder `Soren's files`. "Ticket 8", "T-8" and "T-008" are the same ticket.
2. If they named the invention, use that one. If they didn't and the number exists in more than one invention, ask which one in a single line. If you can't find it, say so and list the open tickets you do see.
3. The ticket has everything: what to do (CALL), what to produce (EXPECT) and how it will be checked (CHECK). Do not ask the owner to paste anything else.
4. Read the procedure the ticket names, starting with `an-analyst` (standing context for b-analyst). Take that one section from AN-Creation/sops/library.txt (the marker line is `=== FILE: <file> ===`; the one-line extract is in `an-folders` (backups and version control)). The file is about 3 MB, so read the section. If you need the live page, https://ancreationoffice.com/<file>. If that site won't open, use the library.txt section, then the public copy at https://raw.githubusercontent.com/mminwi/an-creation-office/main/guide/<file>. That public repository is public on purpose, so a raw link works. Any office may file a ticket. A ticket lives under the invention it belongs to, or under that office's folder when the work is not one invention.

## While you work

- Move the ticket to `queue/active/` and set its Status line to active.
- Work in that invention's folder. Save your run in a new `sessions/YYMMDD-HHMM-<slug>/` folder with `DONE.txt` written last, naming which AI you are.
- Never file, send, buy, register, post or contact anyone. Never invent customers, prices or test results.

## When you finish

- Move the ticket to `queue/done/` with Status "done <date>", update `queue/QUEUE.txt`, and write the next ticket if the ticket asks for one.
- Save with the office-save skill (`an-office-save`). This repository is the GitHub variant: your own clone, pull --rebase, one commit, push, and a gh read-back. Never force-push main. If the push fails, say so plainly; never report work as saved when it isn't.
- End with one or two plain lines for the owner: what you did and what's next.

## using Claude, ChatGPT (Codex), Cursor, or another AI
(procedure file: using-other-ais.txt)

AN Creation: using Claude, ChatGPT (Codex), Cursor, or another AI. Revision 4 — October 20, 2026.
The office is built for Grok bots. Heavy work runs as `grok` (Grok Build) in the bot's own Shell. `claude` and `codex` may be installed beside it. Read `an-setup-reference` (GitHub, the optional add-on for code) before you add anything.

WHY IT WORKS
The project is plain files in the private repository an-creation, with AGENTS.md at the top. Any agent that can open that clone can read the same ticket and write the same files. The bot the owner talks to stays the office. The other tool does the job they named and pushes the result.

HOW
1. Set the office up the normal way first (`an-setup-reference` (GitHub, the optional add-on for code)), so the clone exists at /workspace/offices/<bot id>/an-creation and AGENTS.md is in it.
2. Check what is already on the bot's computer (`command -v claude`, `command -v codex`). Use a tool only if it is installed and already signed in; never say or save which account it is signed in to. Do not install anything, do not sign in, and do not walk through a paid upgrade or usage billing. If a tool isn't there, the owner sets it up themselves, from that tool's own instructions.
3. The Cursor GitHub connector is read-only. It is not how a save is made. Saves from any of these tools go through git and gh in that office's clone (`an-folders` (backups and version control) SAVING).
4. Give it one line: "Work on ticket T-008 in the an-creation repository." It works in the clone, commits once, pushes, and the office reads the result back.
5. To make one of them the default analyst instead of `grok`, the owner says so. Record it in PROJECT.txt. Until they ask, `grok` stays the default.

Do not offer Cursor cloud agents, Codex on the web, or Claude Code on the web as a setup step. If the owner already uses one and asks, point them at `an-setup-reference` (GitHub, the optional add-on for code) PART 3 and let them decide. Setup itself never starts those.

## start here, on your phone
(procedure file: start-on-your-phone.txt)

AN Creation: start here, on your phone. Revision 4 — October 18, 2026.
For someone who has never done this. You need a phone, about an hour, and two accounts. Everything runs in the cloud; nothing goes on a computer.

WHAT YOU NEED
1. At minimum, a SuperGrok subscription (the plan and price: https://ancreationoffice.com/start.html). Depending on how much you use the bots, you may need a larger Grok plan. It includes Grok bots and Grok Build. This one account runs both bots.
2. Somewhere for your project folder. A cloud folder is best: Google Drive (a Google account, which most people have) or OneDrive. Your bot asks where you want it.

THE STEPS
1. Install the Grok app on your phone and sign in.
2. Make a new Grok bot and name it anything you like (short and familiar is easiest). Then paste this, exactly:

   You are my Project Manager Bot for AN Creation (role: b-project-manager).
   First, set up your own profile. Open `an-team` (bot profiles (October 18, 2026)),
   find the Project Manager Bot block, and use your profile tool to set your description
   to that block exactly as written and your title to "Project Manager Bot".
   Read your profile back to me to confirm. If you can't set it yourself, tell me and I'll paste it into Edit Profile.
   Then read and follow your office file: `an-project-manager`
   If you cannot open a link, ask me to paste the text.
   If I have no project folder yet, ask me where I want it (a cloud folder like Google Drive or OneDrive is best) and help me set it up there, one step at a time: `an-setup-reference` (Set up b-project-manager and b-analyst)
   Then run the setup check and tell me the results: `an-office-setup-check`
   Then ask what I want to work on. One question at a time.

3. From there, the bot walks you through it one step at a time: asking where you want your project folder, connecting it, making your private project folder, and testing that it can save your work. It never asks for your passwords; you type those yourself.
4. When it's set up, just talk to it like texting: tell it about your idea, answer its questions, and say "What's next?" whenever you come back.

IF YOU GET STUCK
- Tell the bot exactly what you see on the screen; it has a troubleshooting list.
- Nothing is lost: your bot keeps a dated copy before any big change, and cloud folders like Google Drive keep earlier versions.

Already use Claude, ChatGPT or Cursor and want to use them instead? That works too: `an-setup-reference` (using Claude, ChatGPT (Codex), Cursor, or another AI) . You don't need them.
