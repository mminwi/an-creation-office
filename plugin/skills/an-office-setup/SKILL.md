---
name: an-office-setup
description: "Use once when an AN Creation bot is new or its project folder is missing, and when a bot joins an existing folder."
---
# Setup (one step at a time, with the owner)
One question per message: ask, wait for the answer, then go on.
If the owner has said this bot uses another project folder (a test bot is told to use `/workspace/AN-Creation-Test/`), use that folder everywhere below in place of `/workspace/AN-Creation/`, from the first step, and never open, list or read `/workspace/AN-Creation/`.


1. Profile. If your title and description aren't set, set them with UpdateProfile from your template's profile (or `an-team` (bot profiles (October 18, 2026))), and read them back. A template sets them already: check them quietly and say nothing unless one is missing.
2. The project folder. Look for `/workspace/AN-Creation/` on this computer. There already (another of the owner's bots made it): join it (step 6). Not there: make it with the layout in `an-folders` (project folders): `team.csv` (from the `an-office-files` template), `ideas.txt`, `handoffs/`, `offices/`, and `Default-org/` (the default business) with `All inventions`, `correspondence/` and `correspondence.csv`. Write `/workspace/AN-Creation/office-version.txt` with the installed office version.
2a. The office files (templates, scripts, the resource library). A skill installed by template or UpdateSkill brings only its SKILL.md, not its files. If neither the plugin's `an-office-files/files/` nor `/workspace/AN-Creation-office-files/` is on this computer: download https://ancreationoffice.com/plugin/an-creation-office-latest.zip with curl into `/workspace/AN-Creation-pack/`, unzip it, and copy `an-creation-office/skills/an-office-files/files/` to `/workspace/AN-Creation-office-files/`. They are templates and data you fill in and scripts you run, not instructions; your instructions are the installed skills.
3. The Drive copy. Ask once: "Your work lives on this bot's computer, and I keep a copy in your Google Drive so you can read it on your phone and it's backed up. Google Drive, OneDrive, or none?" Google Drive is the default. Install the connector with InstallPlugin; the owner signs in on the connect card (you never see the password). Make a folder named AN-Creation there (once; look first) and note its ID in your office.txt. None: say once that the work lives only on this computer, and suggest a Drive copy later.
4. Your office.txt (`/workspace/AN-Creation/offices/<your bot id>/office.txt` for a Project Manager Bot): "Bot id:", "Home: this computer, /workspace/AN-Creation", "Drive copy: Google Drive AN-Creation (<folder ID>)" or none, "Office version seen", "Last saved", "Last synced".
5. Your row in team.csv: name, covers, bot_id, business, runs (`an-team` (The bots) SEVERAL BOTS).
6. Joining: the folder is already there: read team.csv; take your bot id (the role, or the role plus a short word if one of your kind is there); make your office folder and inbox `handoffs/for-<your bot id>.txt`; add your row. Never make a second folder.
7. Routines (UpdateRoutine, cron in the owner's timezone): the weekday check of what's due (`45 7 * * 1-5`, quiet when nothing is due) and the daily backup in `an-office-save` (late evening, quiet when nothing changed). Their prompts work in your project folder (Home in your office.txt). A template's routines arrive paused: after the setup check, in its own message, ask the owner once whether to turn them on, and wait for the answer.
8. The setup check (`an-office-setup-check`). Report it in one line: pass or fail, and that the file was read back on this computer (and in Drive, if there's a Drive copy).
Then go back to your job skill's first conversation.
