---
name: an-version
description: "Use when the owner asks what version the office is on, or asks about or for an update."
---
# Versions and updates

The office version is the installed AN Creation Office plugin's version (or the version written in `/workspace/AN-Creation/office-version.txt` when the skills were installed one by one). All the owner's bots share the same skills, so they are always on the same version.

"What version are you on?": that version, in one line.

"Is there a newer version?" (from the owner, or a bot the owner set up to test you): look, and answer in one line with both numbers: "I'm on 261018.47; the newest is 261018.50." Looking needs no OK: it reads one page and changes nothing. Updating is the step that needs the owner's yes.

UPDATING (only when the owner asks; never on your own)
1. Look for a newer version: read `an-version` (its "Office version:" line and its CHANGES) with a plain web read, or the plugin's newest version in the marketplace. Don't download the office zip to look.
2. Nothing newer: say so in one line and stop.
3. Newer: tell the owner in a few lines what's new, from the CHANGES entries after your version. If they asked to update, that's the yes; if they only asked whether there is one, ask "Want me to update?" and wait.
4. The update itself: the owner installs the newer plugin version (InstallPlugin), or the bot reinstalls them the way a template's getting-started script does: a fresh download of the office zip, its `an-creation-office/skills/` copied over `/workspace/AN-Creation-office-skills/`, and each short skill in `install/skills/` saved with UpdateSkill. Then write the new version in `/workspace/AN-Creation/office-version.txt` and your office.txt, re-read your job skill, and say it's done in one line.
A bot you know is better than a new bot you don't: the owner decides when.
