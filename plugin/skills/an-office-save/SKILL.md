---
name: an-office-save
description: "Use whenever an AN Creation bot saves, versions, or copies a file to Drive or OneDrive, at the end of each task."
---
# Saving

## On this computer (every save)
1. Write the file in `/workspace/AN-Creation/...` in place (working files: office.txt, plan.md, actions.csv, Status, Plan) or as a new dated file or folder (records and outputs are never edited once saved).
2. Before a major change to a working file, copy it to the same folder's `History/` as `<name>_YYMMDD-HHMM.<ext>`. Names you create have no spaces; quote every path in shell commands (some folder names, like `Your files`, have spaces).
3. Read it back: compare the `sha256sum` of what you meant to write with the file on disk. Not the same: say so in one plain line and don't call it saved.
4. If the save changed plan.md or actions.csv, rewrite "Working on" in your office.txt in the same save.
5. Only after the read-back, set "Last saved" in your office.txt: `<date time>, <file>, read back OK`.

## The Drive copy (what the owner reads, and the backup)
Google Drive tools (the Google Drive connector): `create_folder`, `create_file`, `update_file_content`, `read_file`, `list_folder`, `move_or_rename`, `trash_file`. A text file made with `create_file` or UploadFile keeps its ID when you save it with `update_file_content`, move it with `move_or_rename`, and check it with `read_file`. UploadFile itself always makes a new file. A file that isn't text (a PDF, a photo, a real .xlsx) was not checked this way: upload a new dated copy.
- Folders: make them with `create_folder` and note each folder's ID in your own `drive-ids.csv` in your office folder (path, Drive ID, kind, made or last updated). Each bot writes only its own `drive-ids.csv`; read the others' to find what another bot made. To move or rename, use `move_or_rename`: the ID stays the same, so only the path in `drive-ids.csv` changes.
- Working files (office.txt, Status, Plan, To-do, Action log, the .csv sheets): keep them as text (.md, .csv, .txt). The first time, make the file with `create_file` or UploadFile and note its ID. Every later save is `update_file_content` on that ID with the whole new text (`contentMimeType` `text/csv` for .csv, `text/markdown` for .md, else `text/plain`): the owner's link stays the same. That works on text files this connector made, including ones sent with UploadFile. A file dragged into Drive by hand is off limits. If it refuses a file, make a new one with `create_file`, put the new ID in `drive-ids.csv`, and tell the owner once that the file moved.
- Records, outputs and History copies are new dated files: text ones with `create_file`, anything else (PDF, photo, .xlsx, the backup) with UploadFile. Each is made once and never changed; note its ID.
- A file that isn't text and must stay a single copy: upload the new dated one, then `trash_file` the old one (it can be recovered for about 30 days) and update its row in `drive-ids.csv`.
- OneDrive (if that's the owner's choice): UploadFile with overwrite replaces a file in place.
- Read back what you saved: `read_file` the Drive ID (text), or DownloadFile it into your work folder (anything else), and compare `sha256sum` with your copy. Not the same: say so in one line.
- Never search-and-create: a search that comes back empty is not proof the file is missing; check the `drive-ids.csv` files first.
- Update "Last synced" in your office.txt after the copies read back.

## The backup (daily, by routine, quiet)
Once a day when anything changed: pack `/workspace/AN-Creation/` into `AN-Creation_backup_YYMMDD.tar.gz` and upload it to `Backups/` in the Drive AN-Creation folder, read it back, and record it. Nothing changed: do nothing and say nothing.

## A failed save is never quiet
One plain line to the owner, and don't report the work as saved.
