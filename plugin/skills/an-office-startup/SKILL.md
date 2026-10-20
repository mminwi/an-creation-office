---
name: an-office-startup
description: "Use at the start of every conversation with the owner, before anything else: find the folder, check Drive, read what's due."
---
# Start of every conversation

1. The office. Read `an-office` once per conversation. Your office folder: a Project Manager Bot uses `/workspace/AN-Creation/offices/<your bot id>/`; an Office Manager Bot its business folder, `/workspace/AN-Creation/Default-org/` for the default business; the Bot Tester `/workspace/AN-Creation-Test/offices/b-tester/`.
2. Find the project folder: `/workspace/AN-Creation/` on this computer. Missing, or your office.txt missing: this is setup; follow `an-office-setup` and come back. Never make a second project folder.
3. Your version: the "Office version seen" line in your office.txt should match the installed AN Creation Office version: the "Office version:" line of `/workspace/AN-Creation-office-skills/VERSION.txt` (no such file: the plugin's version, or `office-version.txt` in your project folder). Different: say it once in one line ("The office was updated to <version>; I'm now on it.") and write the new number; all the owner's bots share the same skills, so an update reaches every bot at once, and only when the owner installs it (`an-version` UPDATING). Never look for updates on the website unless the owner asks.
4. The Drive copy: if the owner may have changed files there since the last save (Your files), list the Drive AN-Creation folder for files changed after the "Last synced" time in your office.txt, download each with DownloadFile, and treat them as the owner's edits (`an-analyst` step 2). Say nothing unless something changed.
5. Read team.csv, your office.txt, plan.md, actions.csv and your inbox `/workspace/AN-Creation/handoffs/for-<your bot id>.txt`. Messages from other bots (SendToAgent) since last time: ordinary work goes on your plan; anything consequential waits for the owner.
6. Then follow START OF EVERY CONVERSATION in your job skill: what to mention, what to ask first. Ask once; don't repeat a question already asked.
