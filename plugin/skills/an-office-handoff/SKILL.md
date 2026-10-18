---
name: an-office-handoff
description: "Use whenever work belongs to another of the owner's bots: an inbox line and a SendToAgent message."
---

AN Creation skill: office-handoff. The office rule is `an-team` (The bots) HAND-OFFS.

1. Add one line to AN-Creation/handoffs/for-<their bot id>.txt:
   <date time CT> | from <your bot id> | <one line of the work> | open
   Their bot id is in team.csv: for an invention, the Project Manager Bot that runs it; for business work, the Office Manager Bot of that invention's business. With one bot of each kind, the id is the role (b-project-manager, b-business-manager).
2. Send a SendToAgent ping to that bot. If you cannot ping it, tell the owner the line and the bot's name. If they don't have that bot, say so once and keep the item on your own plan.
3. When a line is on your plan, change its last word from open to taken. When the work is finished, change it to done.
4. Never delete a line.
