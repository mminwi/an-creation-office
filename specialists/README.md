# Specialists (branch)

A wider-scoped branch of the AN Creation Office. Instead of one office "for inventors," the office is promoted as a roster of specialists: a project manager, a design-for-manufacturing specialist, a cooling water specialist, a patent prep specialist, and so on. Each one gets its own page and listing. Behind them is one office: the same procedures, library, forms and front desk (b-project-manager) in guide/.

- roles.csv: the master list of roles: procedures, library sources, new sources, links between roles. sources-new.csv: sources still to read. sources.md: what the sources pass did and the gaps.
- roster.md: the idea, the specialist card format, the first roster of 32, how the front desk teams them up, and the build plan.
- Next: the sources pass (every card gets its standards and documents, reusing guide/resources.json), then forms and calculations, then routing questions for the front desk.

main stays the live inventor office (ancreationoffice.com). Nothing on this branch is live until it is merged.

Open item for Mike: guide/ is licensed CC BY-NC-SA 4.0 ("not to sell or to build a paid program on"). If specialists are ever sold, decide the license for this branch before then.

## Role names (2026-10-12)

Procedures no longer use bot names. Every role is a small b, a dash and what it does: b-project-manager (was Soren), b-business-manager (was Kasper), b-analyst, b-electrical, b-mechanical, b-six-sigma. The inventor names their own bots in AN-Creation/team.csv and decides whether one bot covers everything or the roles are split. Rules: guide/sop-team.txt.

Renamed on this branch:
- soren.txt → project-manager.txt, kasper.txt → business-manager.txt
- sop-kasper-company/website/presence/promotion.txt → sop-company.txt, sop-website.txt, sop-presence.txt, sop-promotion.txt
- Project folder "Soren's files" → "Office files" (guide/review.py reads the new name)
- Hand-off files for-soren.txt / for-kasper.txt → for-project-manager.txt / for-business-manager.txt
- version.txt left as written: it is the history.

Before merging to main (the live site):
- Existing projects (mminwi/an-creation: tray, Business) still use "Soren's files" and the old hand-off file names; they need a one-time rename.
- The website's HTML pages (soren.html, setup.html#making-kasper, the start page) still use the names; they live outside this repo.
- The old .txt URLs (soren.txt, kasper.txt, sop-kasper-*.txt) should redirect to the new ones, so bots already set up keep working.
- guide/resources.json, planning-resources.json and resource-crosscheck.json still key roles by personal names (andy, casey, larry, ellis, peter, morgan, frankie, maya); switch them to b-names with the website.
- guide/advance-now.json still has a "soren" key; the website may read it, so it was left alone.
- Version and profile version bump in version.txt.

## Setup: one Grok account (2026-10-12)

Mike wants the default to be the simplest possible: one Grok account (with Grok Build) and a free GitHub account, all from a phone, all in the cloud. The bot runs Grok Build in its own cloud terminal as b-analyst, so there is no second AI service to connect. The simple path is the only one setup takes people down; other AIs are never offered at setup, only answered if asked (guide/using-other-ais.txt, linked once at the bottom of the start page). Cursor, Claude Code and Codex setup details live in github-setup.txt PART 3; any agent can work a ticket because AGENTS.md (guide/template-agents.md) sits at the top of every project repository.
Changed: guide/sop-office.txt (the shape, the analyst), guide/github-setup.txt (PART 2 default, PART 3 optional), guide/standing.txt (how the analyst is started), new guide/start-on-your-phone.txt and guide/template-agents.md.
To test before merging: Mike's father sets it up from his phone with start-on-your-phone.txt alone. Confirm on a real phone: that the Grok app's bot has a cloud terminal with Grok Build on that plan, how it signs in to GitHub, and the exact Grok Build command. Fix the steps from what happens.
