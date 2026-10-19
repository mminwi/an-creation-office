AN Creation test scripts for the Bot Tester (https://ancreationoffice.com/tester.txt). Revision 2 — October 18, 2026.
Each script tests one thing a bot's own instructions say it must do. Run them against test copies of the bots, in /workspace/AN-Creation-Test/, never against working bots or /workspace/AN-Creation/. Write your own from https://ancreationoffice.com/template-test-script.txt .

Run in this order (later ones use what earlier ones leave in the test folder):
1. pm-first-run.txt                 the Project Manager Bot's first run: profile, folder, setup check, one question at a time, the AI note, privacy, the first-win read-back, the intake saved
2. pm-hard-rules.txt                pushed for "patentable?", a compliance claim and sending an email: it holds its lines
3. om-join-folder.txt               the Office Manager Bot joins the same test folder, adds its team row and inbox
4. om-first-run-entrepreneur.txt    a fresh test folder: the Office Manager Bot alone for a dog grooming business: the plan, break-even, sales tax and the contractor question left to the sources
5. update-only-when-asked.txt       either bot: no self-update; asks before updating

A worked example for a bot that isn't an AN Creation bot (a made-up bakery order bot): example-bakery-orders.txt . The guide to writing your own: https://ancreationoffice.com/tester-guide.html

To run them all: tell the Bot Tester "Run the AN Creation tests, 1 to 5, against <bot names>." It runs each in its own folder under test-runs/ and sums them up at the end.
