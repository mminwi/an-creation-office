# The specialists: one office, many doors
Draft 2026-10-12 (Claude Code, from Mike's conversation). For Mike to mark up: cut, add, rename, fix tiers.
First drafted in mminwi/an-creation (AN-Creation/Business/specialists.md); this copy on the `specialists` branch is the one to keep working on.

## The idea

- Stop promoting "help for inventors." Promote **specialists**: a project manager, a design-for-manufacturing specialist, a cooling water specialist, a patent specialist, and so on. Each one gets its own page, its own one-line promise and its own listing.
- They are called specialists, never engineers, accountants or lawyers, in names and in promotion. A specialist does the work up to the point where a licensed person must decide, then hands over a clean packet.
- Behind the doors it is one office: one shared base (library of standards, forms, calculations, rules, the customer's project record) and one front desk (b-project-manager).
- A visitor can pick one specialist, pick several, or describe the problem and let the front desk pick the team. Every specialist on a job works from the same project record.
- Build them all together. Most of the work is the same work for every specialist: finding the standards and documents that govern the area, writing short pointers to them, and mapping the forms.

## How a specialist is defined (one card each)

| Field | What it holds |
| --- | --- |
| Name | Plain name for promotion, "... Specialist", and its role name b-<what it does> (guide/sop-team.txt) |
| Promise | One line for the website and listings |
| Who it's for | The person who comes in this door |
| Does | What it produces before anyone is paid |
| Hands off to | The licensed or hands-on person, and the packet they get |
| Tier | Deep (Mike has done it), Managed (Mike has run projects like it), Documented (good public sources, outside Mike's experience) |
| Sources | Library pointers: link, date read, what it asks. Pointers, not copies |
| Forms and calcs | From forms-catalog.csv, plus any calculation it runs in code |
| Works with | The specialists it usually teams with |

The tier sets how the specialist is promoted. Deep: "built from Mike's years in molding." Managed and Documented: "gets you ready for your engineer/attorney, and saves you their hours."

## The roster (37 roles; master list is roles.csv)

Generated from roles.csv, which also lists each role's procedures, library sources, new sources and gaps. Edit roles.csv, not this table. Tiers proposed; Mike confirms.


### Project and business
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Project Manager | b-project-manager | Deep | Stages, gates, plan, queue, action log, status; tracks every job | — |
| Analyst | b-analyst | Deep | Headless worker: files records, runs the looks and the specialist work, writes tickets | — |
| Business Manager | b-business-manager | Managed | Everything around the products: company, name, website, profiles, promotion, business paperwork | attorney; accountant; insurance agent |
| Company Setup Specialist | b-company-setup | Documented | Entity, EIN, bank, insurance, organized before paying anyone | attorney; accountant; insurance agent |
| Patent Prep Specialist | b-patent-prep | Documented | Invention disclosure, prior-art log, provisional package draft | patent attorney or agent |
| Trademark and Naming Specialist | b-trademark | Documented | Name screening and the questions for counsel | trademark attorney |
| Licensing and Funding Specialist | b-licensing-funding | Documented | License packet, licensee list, funding worksheet | attorney |
| Launch and Promotion Specialist | b-promotion | Managed | Site, listings, posts, all drafted for a yes | — |
| Retail Selling Specialist | b-retail | Documented | Getting ready for Amazon, Walmart, Lowe's and other buyers: registration, fees, barcodes, supplier requirements | — |
| Government and Defense Contracting Specialist | b-gov-contracting | Documented | SAM registration, contract specs and military standards, supplier setup for federal and defense buyers | contracting officer (their side); APEX Accelerator |

### Design
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Design Specialist | b-design | Deep | Concepts, structure, loads, mechanisms, ergonomics, fits; metal parts | mechanical engineer (load cases near people) |
| Design for Manufacturing Specialist | b-dfm | Deep | Make the part cheaper and easier to build before tooling | — |
| Plastic Part Design Specialist | b-plastic-part-design | Deep | Walls, draft, ribs, bosses, gates, sink and warp risk, joining and sealing | — |
| Tolerance Stack and GD&T Specialist | b-tolerance-gdt | Deep | Stack studies (worst case, RSS, Monte Carlo) and print reviews | — |
| Plastic Material Selection Specialist | b-plastic-materials | Deep | Resin by load, heat, chemicals and disinfectants, flame, food or medical contact | — |
| Prototyping Specialist | b-prototyping | Deep | The right prototype path: print, machine, soft tool, mock-up | prototype shops |

### Molding and tooling
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Mold Buying and Qualification Specialist | b-mold-buying | Deep | Mold spec, quote package, T1 plan, approval | tool shop; molder |
| Scientific Molding Specialist | b-scientific-molding | Deep | Viscosity curve, gate seal, cavity balance, pressure drop, process window | — |
| Molding Defect Troubleshooting Specialist | b-molding-defects | Deep | Short shot, sink, flash, splay, warp: root cause from the data | — |
| Mold and Machine Cooling Water Specialist | b-cooling-water | Deep | Heat load, circuit flow, chiller and tower sizing, water treatment | mechanical contractor; water treatment vendor |
| Material Drying and Handling Specialist | b-drying-handling | Deep | Dryer sizing, moisture, regrind rules | — |
| Automation and Auxiliaries Specialist | b-automation | Managed | Robots, conveyors, end-of-arm tooling, specified for a quote | integrator |

### Quality
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Quality Planning Specialist | b-quality-planning | Deep | APQP, DFMEA, PFMEA, control plan | — |
| Measurement and Inspection Specialist | b-measurement | Deep | Gauge R&R, inspection plans, first article | lab; CMM shop |
| Lean Six Sigma Specialist | b-six-sigma | Deep | DMAIC projects: scrap, OEE, changeover time, capability | — |
| Medical Device Quality Specialist | b-medical-quality | Documented | Design controls and ISO 13485 readiness | regulatory consultant |

### Electrical and compliance
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Electrical Project Prep Specialist | b-electrical | Managed | Requirements, load list, sequence of operation, code screen, RFQ for your electrical engineer | electrical engineer; panel shop |
| Controls and PLC Prep Specialist | b-controls | Managed | I/O list, sequence, alarms, acceptance test | controls integrator |
| Battery and Power Specialist | b-battery-power | Documented | Battery questions, protection, charging, shipping rules | electrical engineer; battery test lab |
| EMI and FCC Specialist | b-emi-fcc | Documented | Design checklist, pre-scan plan, which FCC and EMC rules apply | EMC test lab |
| Product Safety and Listing Specialist | b-product-safety | Documented | Which UL/NRTL path, hazards, warnings, recalls of similar products | NRTL lab |
| Machine Safety and Guarding Specialist | b-machine-safety | Managed | Risk assessment draft, guarding, lockout, safety circuits | safety engineer |
| Food Equipment Specialist | b-food-equipment | Documented | Cleanable design and the NSF path | NSF lab |

### Supply chain and manufacturing
| Specialist | Role | Tier | Does | Hands off to |
|---|---|---|---|---|
| Purchasing Specialist | b-purchasing | Deep | Quote packages, supplier comparison, terms, delivered cost | suppliers |
| Cost and BOM Specialist | b-cost-bom | Deep | Should-cost, molded part cost from cycle, rate and resin, the BOM | — |
| Manufacturing Specialist | b-manufacturing | Deep | Process flow, PFMEA, work instructions, line balance, layout, launch | — |
| Packaging and Shipping Specialist | b-packaging-shipping | Documented | Package design, drop tests, carrier and lithium rules | test lab |

## First-look roles

Seven broad roles do the first and second looks (guide/sop-team.txt): b-project-manager, b-business-manager, b-design, b-electrical, b-plastics, b-manufacturing, b-quality. Each one pulls in the specialists below for its area. b-plastics covers everything plastic and pulls in plastic part design, plastic materials, mold buying, scientific molding, defects, cooling water and drying; it was added after the tray test (2026-10-12), where plastics knowledge was split across three roles.

## How the front desk teams them up

- One intake. The answers pick the specialists, the same way screening questions already pull in standards (screening-questions.csv). Example: "the mold runs hot and the cycle is long" brings in b-cooling-water, b-scientific-molding and b-molding-defects.
- One project record. Every specialist writes to the same forms with the same status words; one field owns each fact.
- One short list. However many specialists are on a job, the customer sees one list of about three items.

## Build plan (all at once)

1. **Roster** (this note). Mike cuts, adds, renames and sets tiers.
2. **Sources pass.** One research run fills the Sources field for every card. Start from the library the office already has (guide/resources.json, about 240 entries) and add only what it doesn't cover. Many specialists share sources (FMEA, PPAP, NFPA 79), so the result is one deduplicated library with each specialist pointing into it. Each pointer is a link, the date it was read, and a few lines on what it asks. Blocked pages are marked "not read" and never filled from memory.
3. **Forms and calcs.** Map each card to forms-catalog.csv; list the forms and calculations that are missing (cooling heat load, stack-up, molded part cost, viscosity curve, and others).
4. **Front desk.** Intake questions that route to specialists, added to the screening set; the first look (guide/sop-team.txt) is the first draft of this.
5. **Try it.** Mike runs real past problems through it and judges the output; fix what's slow or wrong.
6. **Promotion.** b-business-manager gets one page and one listing line per specialist.

The shared base stays in guide/. The specialist cards and anything new for them grow in specialists/ on this branch until Mike is happy, then merge into main.
