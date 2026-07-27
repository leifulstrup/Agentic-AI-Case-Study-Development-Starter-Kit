# Example — Teaching Note excerpt

*From the same generated package. The Teaching Note is instructor-only: session plan, discussion questions with expected response threads, board plans, and assessment guidance. Full document ~3,000 words.*

---

## 2. Learning Objectives

By the end of the session, students should be able to:

1. **(Innovation management)** Analyze how a large incumbent can run federated, bottom-up innovation and centralized, top-down transformation simultaneously — and diagnose why the two modes compete for resources, measurement systems, and organizational trust. <!-- VERIFIED 2026-07-08: ambidexterity/exploration-exploitation framework per March, "Exploration and Exploitation in Organizational Learning," Organization Science 2(1), 1991, pp. 71–87, and O'Reilly & Tushman, "The Ambidextrous Organization," Harvard Business Review 82(4), April 2004, pp. 74–81; citations confirmed via web search --> (Framework: March, *Organization Science*, 1991; O'Reilly & Tushman, *Harvard Business Review*, April 2004.)
2. **(Workforce transformation)** Evaluate the managerial and ethical trade-offs of the "makers to checkers" transition — retraining vs. reduction, apprenticeship-model erosion, and sequencing change without destroying a voluntary adoption culture — using the case's evidence (ops staff −10% announcement, Stanford/ADP entry-level data, Dimon's retrain-and-redeploy stance).
3. **(Platform strategy)** Explain why JPMorgan bet on connectivity rather than models as the defensible moat ("AI-connected enterprise"), and contrast platform/building-block strategies with point-solution portfolios and their respective failure modes ("proof-of-concept hell").
4. **(Value measurement)** Distinguish capacity creation from cost takeout ("an hour saved here and three hours there… often just shift bottlenecks" — Waldron, McKinsey, Oct. 2025) and assess what each implies for AI ROI claims, using the case's dueling numbers ($2B/$2B, 30–40% gross benefit growth, $700B industry scenario, MIT's $30B-with-no-returns finding).

Objectives 1 and 2 are the required anchors (innovation management; workforce transformation); 3 and 4 support them.

## 4. 80-Minute Session Plan

| Segment | Time | Activity |
|---|---|---|
| 1. Cold open + poll | 0:00–0:08 (8 min) | Cold call: "It's January 2026. You're Waldron. Dimon asks: where does the next dollar go — flywheel or journeys?" Then a hands-up poll: majority bottom-up / majority top-down / 50-50. Record the split on the board; revisit at close. |
| 2. What did bottom-up actually build? | 0:08–0:23 (15 min) | Board 1: inventory the bottom-up results from the case (0→250K users; ~30,000 assistants; flywheel; power users; "cultural transformation"; AI Made Easy; opt-in FOMO dynamics). Push: which of these are assets, and which are just activity? Introduce Waldron's own caveat: capacity ≠ cost takeout. |
| 3. Why top-down? The bear case for the flywheel | 0:23–0:38 (15 min) | Board 2: the transformation argument. End-to-end processes cross teams; "snips shift bottlenecks"; six priority domains; measurable metrics ("80 percent reduction in response time"); industry race economics (McKinsey $700B central scenario, 4-pt ROTE spread for pioneers, compete-away dynamic; MIT $30B no-returns base rate). Ask: what does the top-down pillar need that the bottom-up pillar never needed? (Answer thread: process redesign authority, cross-functional governance, workforce change.) |
| 4. Makers to checkers — the workforce debate | 0:38–0:56 (18 min) | Structured debate (see role play, Section 6). Evidence on the table: ops staff −10% over five years; July retreat apprenticeship concerns; 6-1→4-1 junior banker proposal (at an unnamed bank); Stanford/ADP 6% decline for ages 22–25 in AI-exposed occupations; Dimon: "more jobs, but… less jobs in certain functions"; Waldron: "AI will make everyone a manager." Key question: can a bank that built adoption on voluntarism execute restructuring through the same platform without breaking trust? |
| 5. Decision and synthesis | 0:56–1:12 (16 min) | Return to the opening poll; re-vote. Draw the synthesis: the pillars are complements in capability but competitors in resources and legitimacy. Surface sequencing options (see Section 5.4). Test each against the case's stated constraints (five-teams rule, entitlement governance, agent IAM gaps, human-in-the-loop complacency). |
| 6. Epilogue + verification coda | 1:12–1:20 (8 min) | Share what the sources say as of Dec. 2025 (Section 8). Close with the source-criticism coda (Section 7): nearly every claim in this case originates from the company's executives — what would you want to verify before betting your own capital? |

Timing notes: Segments 2 and 3 can compress to 12 minutes each if the debate in Segment 4 is running hot; protect Segment 6 — the verification coda differentiates this case pedagogically.

## 9. Discussion Questions with Expected Response Threads

**Q1. Why did JPMorgan's platform go viral when, per the MIT report cited by CNBC, most corporate AI programs produced no tangible returns on $30 billion of investment?**
Expected threads: the three founding principles preceded the hype cycle; distribution-first sequencing built demand before solutions; opt-in scarcity created pull rather than push; training (AI Made Easy) and peer channels lowered the competence barrier; the five-teams rule kept the platform tied to real problems. Sharper students will note the survivorship framing: JPMorgan also had advantages most firms lack — an $18B technology budget, 2,000 AI staff since 2012 (Dimon, Bloomberg, Oct. 7, 2025), and a pre-existing entitlement infrastructure the platform could inherit. The honest answer is "playbook plus endowments," not playbook alone.

## 7. The Verification Coda (recommended, 5–8 minutes)

This case is deliberately built from a source set with a known bias profile: five Tier-1 sources, four of which are organized around JPMorgan executives' own accounts — three executive interviews and the company's own earnings release, with a single journalistic piece (itself built on company-provided access) rounding out the set; the tiering and characterization of each source are recorded in `Source_Registry.md`. Use this at the close:

- **Ask:** which numbers in this case were produced or could be audited by someone other than JPMorgan? (Answer: the Q3 earnings figures; the Stanford/ADP study; the MIT report; McKinsey's industry economics. The AI-specific claims — $2B benefit, 30–40% growth, 30,000 assistants, adoption rates — are all company-asserted.)
- **Show the discrepancies** (Additional Sources, "Data Discrepancies"): daily-use figures differ across three months and three outlets; the workforce base is 317,000 in CNBC but "about 400,000" per the VentureBeat host; Dimon's "150,000 a week" sits oddly beside "one in two daily." None is necessarily wrong — metric, base, and date differ — but students should feel the difference between *quoted* and *verified*.
- **Point:** in an AI-saturated information environment, the discipline of tracing every number to a dated, named source is itself the skill this course is teaching.

---

*[Sections 5, 6, 8, 10, 11, 12 omitted: detailed analysis of what students should discover, the role-play design, epilogue, assessment guidance, common student errors, and three board plans.]*

---

## What to notice in this excerpt

**The session plan sums to the configured length.** 8 + 15 + 15 + 18 + 16 + 8 = 80 minutes, matching `session_length_minutes` in `case-config.yaml`. Timing notes say which segments can compress and which to protect.

**Discussion questions come with expected response threads.** Not just what to ask, but what good answers look like and what the sharper students will notice — the difference between a question list and a teaching note.

**The verification coda is a teaching move, not an apology.** The bias assessment found this corpus is ~80% executive voice. Rather than hiding that, the Teaching Note turns it into the closing segment: *nearly every claim here originates from the company's executives — what would you want to verify before betting your own capital?* Students practice source criticism on a real case rather than hearing about it abstractly.

**Known weaknesses are disclosed to the instructor.** The Note flags where evidence is thin (Section 7) so the professor is never surprised in front of a class.
