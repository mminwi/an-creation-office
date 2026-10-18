---
name: an-version
description: "Use when the owner asks what version the office is on, or asks about or for an update."
---
# Versions and updates

The office version is the installed AN Creation Office plugin's version (or the version written in `/workspace/AN-Creation/office-version.txt` when the skills were installed one by one). All the owner's bots share the same skills, so they are always on the same version.

"What version are you on?": that version, in one line.

UPDATING (only when the owner asks; never on your own)
1. Look for a newer version: the plugin's newest version in the marketplace, or `an-version` (reference only: read its CHANGES).
2. Nothing newer: say so in one line and stop.
3. Newer: tell the owner in a few lines what's new, from the CHANGES entries after your version. If they asked to update, that's the yes; if they only asked whether there is one, ask "Want me to update?" and wait.
4. The update itself: the owner installs the newer plugin version (InstallPlugin), or reinstalls the skills one by one the way `an-office-files` INSTALL says. Then write the new version in `/workspace/AN-Creation/office-version.txt` and your office.txt, re-read your job skill, and say it's done in one line.
A bot you know is better than a new bot you don't: the owner decides when.
