# The specialists: one office, many doors
Draft 2026-10-12 (Claude Code, from Mike's conversation). For Mike to mark up: cut, add, rename, fix tiers.
First drafted in mminwi/an-creation (AN-Creation/Business/specialists.md); this copy on the `specialists` branch is the one to keep working on.

## The idea

- Stop promoting "help for inventors." Promote **specialists**: a project manager, a design-for-manufacturing specialist, a cooling water specialist, a patent specialist, and so on. Each one gets its own page, its own one-line promise and its own listing.
- They are called specialists, not engineers, accountants or lawyers. A specialist does the work up to the point where a licensed person must decide, then hands over a clean packet.
- Behind the doors it is one office: one shared base (library of standards, forms, calculations, rules, the customer's project record) and one front desk (Soren).
- A visitor can pick one specialist, pick several, or describe the problem and let the front desk pick the team. Every specialist on a job works from the same project record.
- Build them all together. Most of the work is the same work for every specialist: finding the standards and documents that govern the area, writing short pointers to them, and mapping the forms.

## How a specialist is defined (one card each)

| Field | What it holds |
| --- | --- |
| Name | Plain name, "... Specialist" |
| Promise | One line for the website and listings |
| Who it's for | The person who comes in this door |
| Does | What it produces before anyone is paid |
| Hands off to | The licensed or hands-on person, and the packet they get |
| Tier | Deep (Mike has done it), Managed (Mike has run projects like it), Documented (good public sources, outside Mike's experience) |
| Sources | Library pointers: link, date read, what it asks. Pointers, not copies |
| Forms and calcs | From forms-catalog.csv, plus any calculation it runs in code |
| Works with | The specialists it usually teams with |

The tier sets how the specialist is promoted. Deep: "built from Mike's years in molding." Managed and Documented: "gets you ready for your engineer/attorney, and saves you their hours."

## First roster (32, tiers proposed, Mike confirms)

### Project and business
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 1 | New Product Project Manager | Stages, gates, schedule and a short to-do list for a new product | Deep | — | Office stages and gates; PMI basics |
| 2 | Company Setup | Entity, EIN, bank, insurance, organized before you pay anyone | Documented | Attorney, accountant, insurance agent | State SOS, IRS, SBA |
| 3 | Patent Prep | Invention disclosure, prior-art log, provisional package draft | Documented | Patent attorney or agent | USPTO, MPEP, Patent Public Search |
| 4 | Trademark and Naming | Name screening and the questions for counsel | Documented | Trademark attorney | USPTO trademark search, TMEP |
| 5 | Licensing and Funding | License packet, licensee list, funding worksheet | Documented | Attorney | USPTO/SBA guides |
| 6 | Launch and Promotion | Site, listings, posts (Kasper) | Managed | — | Platform rules |

### Product design
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 7 | Design for Manufacturing | Make the part cheaper and easier to build before tooling | Deep | — | Process design guides |
| 8 | Plastic Part Design | Walls, draft, ribs, bosses, gates, sink and warp risk | Deep | — | Resin supplier design guides |
| 9 | Tolerance Stack and GD&T | Stack studies (worst case, RSS, Monte Carlo) and print reviews | Deep | — | ASME Y14.5-2018, Y14.5.1 |
| 10 | Plastic Material Selection | Resin choice by load, heat, chemicals, flame, food/medical | Deep | — | UL 94, FDA 21 CFR 177, supplier data |
| 11 | Prototyping | Right prototype path: print, machine, soft tool | Deep | Prototype shops | Shop capability data |

### Molding and tooling
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 12 | Mold Buying and Qualification | Mold spec, quote package, T1 plan, approval | Deep | Tool shop | PLASTICS (SPI) mold classes, AIAG PPAP |
| 13 | Scientific Molding | Viscosity curve, gate seal, cavity balance, process window | Deep | — | Decoupled/scientific molding literature |
| 14 | Molding Defect Troubleshooting | Short shot, sink, flash, splay, warp: root cause from your data | Deep | — | Resin supplier troubleshooting guides |
| 15 | Mold and Machine Cooling Water | Heat load, circuit flow, chiller and tower sizing, water treatment | Deep | Mechanical contractor | ASHRAE handbooks, CTI, OEM data |
| 16 | Material Drying and Handling | Dryer sizing, moisture, regrind rules | Deep | — | Resin supplier drying data |
| 17 | Automation and Auxiliaries | Robots, conveyors, end-of-arm tooling, specified for a quote | Managed | Integrator | ANSI/RIA R15.06, ISO 10218 |

### Quality
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 18 | Quality Planning | APQP, DFMEA, PFMEA, control plan | Deep | — | AIAG-VDA FMEA, AIAG APQP, ISO 9001 |
| 19 | Measurement and Inspection | Gauge R&R, inspection plans, first article | Deep | Lab, CMM shop | AIAG MSA, AS9102 |
| 20 | Lean Six Sigma | DMAIC projects: scrap, OEE, mold change time | Deep | — | ASQ body of knowledge |
| 21 | Medical Device Quality | Design controls, ISO 13485 readiness | Documented | Regulatory consultant | FDA 21 CFR 820, ISO 13485 |

### Electrical and compliance
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 22 | Electrical Project Prep | Load list, sequence of operation, code screen, RFQ for your EE | Managed | Electrical engineer, panel shop | NFPA 79, NFPA 70 (NEC), UL 508A |
| 23 | Controls and PLC Prep | I/O list, sequence, alarms, acceptance test | Managed | Controls integrator | NFPA 79, IEC 61131 |
| 24 | Battery and Power | Battery choice questions, protection, shipping rules | Documented | Electrical engineer | UL 2054, IEC 62133, UN 38.3 |
| 25 | EMI and FCC | Design checklist, pre-scan plan, which FCC rules apply | Documented | EMC test lab | FCC Part 15/18, CISPR 32 |
| 26 | Product Safety and Listing | Which UL/NRTL path, hazards, warnings | Documented | NRTL lab | OSHA NRTL list, CPSC |
| 27 | Machine Safety and Guarding | Risk assessment draft, guarding, lockout | Managed | Safety engineer | ISO 12100, ANSI B11.0, OSHA 1910.212/147 |
| 28 | Food Equipment | Cleanable design and NSF path | Documented | NSF lab | NSF/ANSI 2, 51; FDA Food Code |

### Supply chain and manufacturing
| # | Specialist | Promise | Tier | Hands off to | Key sources |
|---|---|---|---|---|---|
| 29 | Sourcing and RFQ | Quote packages and side-by-side supplier comparison | Deep | Suppliers | Office RFQ form |
| 30 | Cost and BOM | Should-cost, molded part cost from cycle, rate and resin | Deep | — | Office BOM form |
| 31 | Manufacturing Engineering | Process flow, work instructions, line balance, layout | Deep | — | Office forms |
| 32 | Packaging and Shipping | Package design, drop tests, carrier rules | Documented | Test lab | ISTA, UN 38.3, carrier rules |

## How the front desk teams them up

- One intake. The answers pick the specialists, the same way screening questions already pull in standards (screening-questions.csv). Example: "the mold runs hot and the cycle is long" brings in 15, 13 and 14.
- One project record. Every specialist writes to the same forms with the same status words; one field owns each fact.
- One short list. However many specialists are on a job, the customer sees one list of about three items.

## Build plan (all at once)

1. **Roster** (this note). Mike cuts, adds, renames and sets tiers.
2. **Sources pass.** One research run fills the Sources field for every card. Start from the library the office already has (guide/resources.json, about 240 entries) and add only what it doesn't cover. Many specialists share sources (FMEA, PPAP, NFPA 79), so the result is one deduplicated library with each specialist pointing into it. Each pointer is a link, the date it was read, and a few lines on what it asks. Blocked pages are marked "not read" and never filled from memory.
3. **Forms and calcs.** Map each card to forms-catalog.csv; list the forms and calculations that are missing (cooling heat load, stack-up, molded part cost, viscosity curve, and others).
4. **Front desk.** Intake questions that route to specialists, added to the screening set.
5. **Try it.** Mike runs real past problems through it and judges the output; fix what's slow or wrong.
6. **Promotion.** Kasper gets one page and one listing line per specialist.

The shared base stays in guide/. The specialist cards and anything new for them grow in specialists/ on this branch until Mike is happy, then merge into main.
