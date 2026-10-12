# Going live: from the specialists work to the websites
Written 2026-10-12. Main of mminwi/an-creation-office now holds the specialists work (merged 2026-10-12). Nothing below is live until it is done on the server.

## Where the live sites come from (found 2026-10-12)
- **ancreationoffice.com** is served from `site/create/` in the `creation` project on Mike's Beelink (`/home/mike/projects/creation`, GitHub copy: mminwi/creation-office). nginx: `site/nginx-an-creation-office.conf`.
- **advancenowllc.com** is served from `site/` in the same project. nginx: `site/nginx-advance-now.conf`.
- **mminwi/an-creation-office** is a copy synced *from* the website (every earlier commit is "Sync procedures from ancreationoffice.com"). Going live means changing `site/create/` on the Beelink; changing this repo alone does nothing to the site.

## 1. Stop the sync from overwriting the work
- [ ] Pause the website-to-GitHub sync, or reverse it (main becomes the source and is copied to `site/create/`). Otherwise the next sync writes Soren, Kasper and the old file names back into main. The specialists branch keeps a copy either way.

## 2. Reconcile the two sides (both have changes the other lacks)
- [ ] Files on the live site that main doesn't have: `agents-md.txt` (an AGENTS.md text already written for Soren; merge it with `guide/template-agents.md` and keep one), `sop-launch-and-feedback.txt`, `sop-phases.txt`, `blender-template.py`, `guide.css`, `guide.js`, `office.png`, `press-kit/`, `sitemap.xml`, and the HTML pages. Bring the text files into main (renamed to role names) before copying back.
- [ ] Files only on main: the new procedures (cooling water, drying, scientific molding, molding defects, mold buying, machine safety, Six Sigma, part design, tolerance stack, material selection, manufacturing cell), `sop-team.txt`, `template-team.csv`, `template-a3.txt`, `toolbox-improvement.txt`, `start-on-your-phone.txt`, `using-other-ais.txt`, `template-agents.md`, `bot-names.txt`, the renamed files, and the larger `resources.json`/`resources.txt` (309 sources).
- [ ] Diff every text file that exists on both sides; keep the newer content of each.

## 3. Copy main to the site
- [ ] Copy `guide/` into `site/create/` on the Beelink (the `specialists/` folder too, or link to it on GitHub: roster, role map, calculations, records).
- [ ] The calculations (`specialists/calcs/*.py`) are scripts the analyst runs; publish them as text files or link to GitHub.

## 4. Old links must keep working (bots already set up read them)
Add nginx redirects in `nginx-an-creation-office.conf`:
- [ ] `soren.txt` → `project-manager.txt`, `kasper.txt` → `business-manager.txt`
- [ ] `sop-kasper-company.txt` → `sop-company.txt`, `sop-kasper-website.txt` → `sop-website.txt`, `sop-kasper-presence.txt` → `sop-presence.txt`, `sop-kasper-promotion.txt` → `sop-promotion.txt`
- [ ] `soren.html` → the new project manager page; `setup.html#making-kasper` → the business manager setup section

## 5. The HTML pages
- [ ] All 34 pages in `site/create/` mention Soren or Kasper. Change them to "your bot" / the role names, with the bot's own name chosen by the user (bot-names.txt).
- [ ] `start.html`: make the one-Grok-account path the start (from `start-on-your-phone.txt`); other AIs only as the one link (`using-other-ais.txt`).
- [ ] New pages: the specialists (one page per specialist or per group; see 9), the team builder (see 8), cooling water, drying, scientific molding and the other procedures, the improvement toolbox.
- [ ] `sitemap.xml` and the navigation updated.

## 6. Version and profiles
- [ ] New entry in `version.txt` saying what changed for existing users (names gone from procedures, team file, Grok-only default, new specialists), and a new profile version in `profile.txt` so existing bots re-paste their profile.
- [ ] `resources.json`, `planning-resources.json` and `resource-crosscheck.json` still key roles by old personal names (andy, casey, larry, ellis, peter, morgan, frankie, maya); switch to role names with the pages that read them. `advance-now.json` has a `soren` key.

## 7. Existing projects (Mike's own first)
- [ ] mminwi/an-creation: rename `Soren's files` → `Office files` in tray; `Business/for-soren.txt` → `for-project-manager.txt`, `for-kasper.txt` → `for-business-manager.txt`; add `AN-Creation/team.csv` (Soren and Kasper as the names, if Mike keeps them); update `AGENTS.md` from the template. One commit, done by the analyst.
- [ ] The web app at office.advancenowllc.com uses eight named assistants (Andy, Casey ...). Decide whether it follows the role-name and team-file model or stays separate.

## 8. Mike's additions (2026-10-12)
- [ ] **Names list** for people naming their bots: done, `guide/bot-names.txt` (24 easy names, the early office names, and job-style names). Link it from setup and from `sop-team.txt`.
- [ ] **Many products, not one big one.** Present the office as a set of specialist teams people can pick from and combine, each with its own name and focus. Proposed packages to start (each is a preset team file):
  - Inventor's Office: project manager, business, patent prep, design, prototyping (today's office).
  - Molding Plant Office: cooling water, drying and regrind, scientific molding, molding defects, mold buying, machine safety.
  - Quality Office: quality planning (APQP), measurement, Lean Six Sigma, the improvement toolbox.
  - Plastic Design Office: plastic part design, tolerance stacks, material selection, DFM for molding.
  - Manufacturing Office: manufacturing cells, purchasing, cost and BOM, automation, machine safety.
  - Electrical Prep Office: electrical prep, controls, battery and power, EMI and FCC, product safety.
- [ ] **Team builder.** A form where the user lists the specialists they want and writes a bot name next to each. Same name on several lines = one bot covering all of them; different names = separate bots. From it the office writes `team.csv` and a short custom instruction block for each bot (its name, the roles it covers, the procedures it reads). Default: one bot, all roles.
- [ ] **Positioning (Mike):** the design package is presented and marketed as plastics design (the Plastic Design Office), not as a general product design service. Mike works for a product design company and must not appear to compete with it directly. The package contents stay as they are; only how it is named and promoted changes. Apply the same care to every page, listing and post.
- [ ] **Market to different groups.** One page and one listing per package, aimed at its audience (molders and plastics groups, plant and manufacturing engineers, quality and Six Sigma people, inventors). This is b-business-manager's work (sop-promotion.txt): plan the groups and channels per package.
- [ ] **Thicken the main website (advancenowllc.com) for credibility.** More pages on product development and the specialist areas, written from Mike's experience.
  - Sources: Mike's career stories in the mminwi/about-me repository (confirmed by Mike), and the conversation records in `specialists/record/` (cooling water, drying, scientific molding, molding defects, mold buying, machine safety, Six Sigma).
  - Mike approves every story and quote before it goes public; the records include opinions about named people and companies that stay private unless he says otherwise.
- [ ] **Thicken the office site (ancreationoffice.com).** The specialist pages and packages above, with plain descriptions of what each does and where it hands off to a licensed person.

## 9. Test before announcing
- [ ] Mike's father sets up from `start-on-your-phone.txt` alone, on his phone, with one Grok account and a new GitHub account. Write down every place he gets stuck; fix the page or the bot's steps; repeat until he gets through without help.
- [ ] Confirm on a real phone: the Grok bot has a cloud terminal with Grok Build on that plan, how it signs in to GitHub, and the exact Grok Build command; put the real steps into github-setup.txt PART 2.
- [ ] Run one ticket end to end on the tray with Grok Build as the analyst.
- [ ] Run the second look on the tray with the seven roles (sop-team.txt).
