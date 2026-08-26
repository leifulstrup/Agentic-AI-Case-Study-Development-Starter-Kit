# Test Log — Regression Runs Against Frozen Source Corpora

*One entry per run. See `EVALS.md` for the method. Append-only; never rewrite history.*

## Entry template

```
## [kit version] — [date] — [corpus fixture]

- Harness/model: [e.g., Claude Code 2.x / claude-sonnet-5] | Runs: n=[2]
- Corpus manifest hash confirmed: [yes/no]

### Layer 1 — Deterministic
| Check | Run 1 | Run 2 |
|-------|-------|-------|
| Quote grounding rate | % | % |
| Number grounding rate | % | % |
| Open verification debt | # | # |
| Docs complete / word counts | pass/fail | pass/fail |
| Arithmetic errors | # | # |

### Layer 2 — Seeded defects (set version: [defect-set vX])
- Detection recall: [x/N] | False alarms: [#]
- Missed: [which defects, verbatim]

### Layer 3 — Judged
- Rubric (judge model, n=3 median): [scores by dimension]
- Pairwise vs [previous version/golden]: [prefer new / prefer old / split], reasons: [1 line]
- Human anchor (if this release): [reader, doc read, 3 observations]

### What changed in execution vs. previous version
[Behavioral differences noticed while running: different questions asked, different gate behavior, new failure modes, speed/friction changes]

### Verdict
[PASS / PASS WITH NOTES / REGRESSION] — [1-line reason]
```

---

## v3.2.0 — 2026-07-07 — (framework established)

- Status: framework established with this release. Baseline run executed 2026-07-08 (next entry).

---

## v3.2.0 — 2026-07-08 — jpm-llm-suite (BASELINE RUN)

- Harness/model: Claude (Cowork/Agent SDK), writer + verifier agents = claude-fable-5; Layer 3 judge = claude-opus (different model per method) | Runs: **n=1** (variance run deferred — see Notes)
- Corpus manifest hash confirmed: **yes** (all 6 files matched before run)
- Run artifacts: `eval-runs/run-2026-07-08-A/` (clean) and `run-2026-07-08-A-defected/` (Layer 2), kept outside the repo

### Layer 1 — Deterministic
| Check | Run 1 |
|-------|-------|
| Quote grounding (script v1) | 54.8% (219/400) — **script artifact, see Notes** |
| Quote grounding (agent full trace) | ~97% (≈225 VERIFIED, 5 LIKELY, 0 DISPUTED, 0 APOCRYPHAL of ~230) |
| Number grounding (script) | 89.7% (113/126); agent recomputation: 0 arithmetic errors, segment sums foot |
| Open verification debt at end | 6 logged by writer (honest general-knowledge flags) + 3 added by verifier |
| Docs complete / word counts | 4/4 docs; 4,821 / 5,788 / 2,957 / 2,959 words (Main Case +15% over target) |

### Layer 2 — Seeded defects (defect-set v1, 10 defects)
- **Detection recall: 10/10** | False alarms: 0 (all 8 additional flags were genuine pre-existing issues, cross-confirmed by the clean-run verification)
- Missed: none. Every defect class caught: financial figure, internal % inconsistency, misattribution, fabricated quote, silent paraphrase, shifted date, vague-attribution stat, wrong URL slug (caught offline via source-footer cross-check), gutted registry, phantom exhibit.

### Layer 3 — Judged (claude-opus, dual-pass, no dimension moved >1)
- Rubric: Decision focus 5 · Protagonist 4 · Evidence discipline 5 · **Data sufficiency 3 (weakest)** · Narrative craft 4 · Teachability 5 · Balance 5 → **31/35**
- Pairwise: n/a (first baseline — this run becomes the comparator)
- Verdict on teachability: "would teach with minor edits." Biggest editor flag: decision is *constructed from public statements, not confronted in-scene*; top fixes: forcing event with stakes, a quantitative exhibit, one dissenting/non-executive voice.

### What changed in execution vs. previous version
First run — baseline. Writer-agent observations for future versions: (1) no rule for quoting noisy ASR transcripts (improvised bracket-correction policy); (2) bias heuristic counts outlet origin, not claim-maker voice — scored 20% "company-generated" for a corpus that is ~80% executive voice; (3) minor spec gaps: tiering of extracted-PDF companions, "Overall" score aggregation, filename convention, whether citations count toward word targets. Verifier-agent observations: (4) verdict scale needs a **MODIFIED** category for spliced/silently-corrected quotes (had to shoehorn into LIKELY); (5) skills don't define the counting unit for "one quote," so pass/warn/fail counts are partly verifier-defined.

### Clean-run publication status (kit's own gate)
"Needs Review" — verification correctly caught real authoring flaws: 1 spliced composite quote, 1 altered quote ("can…use" vs "can be used"), companion-title mismatch, 1 garbled attribution, silent transcript corrections. **This is the system working**: the writer erred, the verifier caught it, publication blocked.

### Verdict
**PASS (baseline established and BLESSED)** — grounding effectively clean on full trace, seeded-defect recall 10/10 with zero false alarms, judged 31/35 and teachable with minor edits.

### Blessing (2026-07-08, per Leif's direction)
All issues flagged by the run's own verify-all pass were fixed surgically before blessing (see `golden/baseline-v3.2.0/FIXES-2026-07-08.md`): spliced two-pillar quote restored verbatim (six-domain list moved outside quotation marks), "can be used" restored, bracket convention applied to 3 transcript corrections, "proof-of-concept hell" reattributed to Kevin Buehler, companion title corrected, Teaching Note no longer cites an absent artifact, adoption base made precise, and all 6 definitional debt items resolved with web-confirmed canonical citations (Vaswani 2017; Lewis 2020; Anthropic MCP 2024; Evident AI Index; March 1991 + O'Reilly & Tushman 2004; Rogers 2003) added as T3 referenced works. Fixes independently spot-checked against source transcripts. **Verification debt: 9/9 verified, 0 open.** Golden = `golden/baseline-v3.2.0/`. Additionally, Leif's original human-finished Jan 2026 case package is preserved at `golden/reference-human/` as the aspirational ceiling anchor for Layer 3 (never the release gate).

### Notes / actions arising
1. **grounding_check.py v2 needed**: v1's regex counts rhetorical/hypothetical quoted text (esp. Teaching Note prompts like "It's January 2026. You're Waldron…") as attributed quotes → 45% false-flag rate. Fix: only check quoted spans with nearby attribution patterns; skip Teaching Note hypotheticals. Until then, the script is a lead-generator, not a gate.
2. **n=2 variance run deferred** (cost/time). Do a second clean run before using this baseline to fail a future version on a small margin.
3. Add to defect-set v2: composite/spliced quote and silent transcript correction (the two real-world classes this run discovered).
4. Skill-spec fixes queued for v3.3 (ASR quoting rule, MODIFIED verdict, voice-based bias counting, counting units, filename tolerance).

---

## Unreleased (post-v3.2.0) — 2026-07-27 — jpm-llm-suite — COACHING-SKILL PROBES

Testing the two skills added since the baseline (`/coach-case`, `/scout-case`). The authoring pipeline is unchanged since v3.2.0, so a full re-run would measure model variance rather than kit improvement; these probes test what's actually new, against ground truth the baseline run already established.

- Harness/model: Claude agent harness, claude-fable-5 for both probes | Runs: n=1 each
- Probe A (coach): offline, `eval-runs/probe-2026-07-27-coach/` — kit skills + baseline run's sources/drafts/registry/debt
- Probe B (scout): web-enabled, no source materials in hand, two candidates — `eval-runs/scouting-report-2026-07-27.md`

### Probe A — `/coach-case` gap-detection recall

Ground truth = the six weaknesses independently established by the baseline run's verification pass and opus rubric judge.

| # | Known gap | Detected? | Where |
|---|-----------|-----------|-------|
| 1 | No employee/customer/regulator/critic voice | YES | Lens 2, P1–P8 |
| 2 | No protagonist biographical grounding | YES | Lens 4, O1 "protagonist minimum NOT met" |
| 3 | Load-bearing claims resting on single sources | YES | Lens 3, F1–F10 ranked by thinness |
| 4 | Unreconciled headcount/adoption discrepancies | YES | Lens 3, F6/F7 |
| 5 | No computable quantitative exhibit | YES | Lens 5, R1/R2/R8 |
| 6 | No forcing event; no dissenting voice | YES | Lens 5, R3/R4/R5 |

**Detection recall: 6/6.**

**Novel findings beyond ground truth (spot-checked against the corpus — all TRUE):**
1. The VentureBeat episode is **sponsored by Outshift by Cisco**, an AI vendor — an independence problem recorded nowhere. *Verified: sponsor read present in transcript.*
2. The McKinsey interview states on its face it "has been **edited for clarity and length**" yet is quoted as verbatim throughout. *Verified.* This makes the "All quotations verbatim" assertion in all four documents inaccurate.
3. Dimon says **"600,000 employees"** on Bloomberg — a third headcount figure alongside 317,000 and 400,000, unreconciled anywhere. *Verified.*
4. The headline **30,000 assistants** figure is confirmation-by-assent: the *host* asserts it, Waldron replies "it it's correct." *Verified.* It is the case's title number.
5. The **$18B** figure traces to an MSN aggregator repost, and the Main Case converts a *technology* budget into an *AI* program — a 9× contradiction with Dimon's $2B.
6. Buehler carries all industry economics with **no disclosure** of McKinsey's commercial interest or his 18-year tie to Waldron.
7. Two of five "T1" sources are unattributed ASR transcripts with visible corruption and no audio/timecode to adjudicate ~20 quotations.
8. Challenged the baseline's own assessment scores with reasons: Reliability 5 → honestly 3–4; Breadth 3 → honestly 2.

Total gap inventory produced: 23 source-type, 15 perspective, 26 confidence, 24 people/org, 16 rubric-facing. No false positives found in the spot-checked sample.

**Verdict: PASS — exceeds design intent.** The skill found everything two prior expert passes found, plus eight material issues they missed, and correctly prioritized three coaching offers with executable search strategies.

### Probe B — `/scout-case` calibration and discrimination

**Calibration** (predicted blind, with no sources in hand, vs. the baseline's actual post-sourcing assessment):

| Dimension | Scout predicted | Baseline actual | Error |
|-----------|-----------------|-----------------|-------|
| Depth | 5 | 5 | 0 |
| Breadth | 4 | 3 | +1 |
| Reliability | 4 | 5 | −1 |
| Completeness | 4 | 4 | 0 |

**Mean absolute error 0.5; signed error 0 — no systematic optimism**, the defect this probe exists to catch. Note: Probe A independently argues actual Reliability is 3–4, which would make the scout's prediction *more* accurate than the baseline assessment it was scored against.

**Discrimination**: correctly separated a workable candidate (JPMorgan → PURSUE) from an unworkable framing (Bloomberg L.P. internal AI tooling → REDIRECT), with the right reasoning — a private partnership has no filings, so the completeness gap cannot be closed by effort. It then did what the skill asks and offered a *reframe rather than a rejection*: "BloombergGPT: build the model or rent the frontier?" frozen at ~March 2023, with the arXiv paper as a quantitative spine.

**Verdict: PASS.** Correctly calibrated, correctly discriminating, and the REDIRECT-not-AVOID behavior worked as designed.

### Cross-probe finding: the frozen corpus is stale
Both probes independently flagged it. The scout, working from the open web, found materially newer primary sources (Dimon's Apr 2026 shareholder letter, a named counter-voice for the top-down pillar, a 2026 mandate shift from voluntary adoption to tracked usage) and proposed a June 2026 freeze date; the coach flagged the corpus as seven months stale with nothing after Dec 17, 2025. **Action: consider a corpus v2 for pedagogical realism — but keep corpus v1 frozen as the regression fixture.** Regression comparability requires a stable corpus; teaching realism requires a current one. These are different jobs and need different corpora.

### Actions arising
1. Fix the "All quotations verbatim" assertion — it is inaccurate wherever ASR or editor-processed sources are quoted. Ties to the queued ASR-quoting rule and MODIFIED verdict.
2. Add a **source independence/interests column** to the Source Registry (sponsorship, commercial interest, personal ties) — the Cisco and McKinsey findings both fell through this hole.
3. Add "third headcount figure (600,000)" and "sponsored-source independence" to defect-set v2.
4. `/assess-sources` should check for editor/ASR processing disclaimers before allowing T1 classification.

---

## v3.3.0 — 2026-07-27 — jpm-llm-suite — REGRESSION (source-integrity release)

- Harness/model: Claude agent harness, claude-fable-5 verifier | Runs: n=1
- Target: the five defect classes v3.3 was built to catch (defect-set v2: D12–D16), injected into a copy of the baseline authoring output
- Artifacts: `eval-runs/regression-v3.3-defected/verify-v3.3-2026-07-27.log`

### Layer 2 — New defect classes (defect-set v2)

| Defect | Injected | Caught? | Evidence |
|--------|----------|---------|----------|
| D12 silent ASR correction | Removed the `[squandering]` bracket marker | **YES** | Flagged, with transcript's "squanding" quoted back |
| D13 stripped independence annotation | Removed Independence column from registry | **YES** | Flagged, *and* noticed `assess-bias` now references a column that no longer exists |
| D14 edited source quoted as verbatim + false integrity claim | Added "All quotations verbatim… independently verified" | **YES** | "False on both counts… the worst line in the package" |
| D15 third unreconciled figure | Inserted "600,000 employees" | **YES** | Blocking; traced the only corpus instance of 600,000 to a garbled ASR fragment about H-1B visas, not headcount |
| D16 assent converted to assertion | Attributed the 30,000 figure to Waldron as a quotation | **YES** | Identified as fabricated quotation + assent-as-assertion; noted the package's own exhibit records the provenance correctly |

**New-class detection recall: 5/5.** Pre-existing unfixed defects from the baseline copy (splice, altered "can be used", companion-title mismatch) were also re-caught.

### Novel findings beyond the injected set
Two additional silent ASR corrections ("nascence" for "nence", "countless" for "ideiation"), a splice in the Supplement's RAG definition, **~40+ instances of unmarked smoothing** (disfluencies removed without ellipsis), and the observation that the bracket convention is used but never declared.

### The headline change vs. v3.2.0
On substantially the same documents, v3.2.0's verification reported **~225 VERIFIED** quotes and a status of "Needs Review." v3.3.0's verification reports **only ~33 of ~195 can be VERIFIED**, because three of five sources cannot support verbatim quotation at all — two are uncorrected ASR, one states it was edited for clarity and length.

This is not a regression in the case; it is the standard becoming accurate. v3.2.0 was counting quotes as verified that no honest reviewer would accept. The source-integrity work moved the kit from *"does this string appear in the corpus?"* to *"can this source support a quotation at all, and is the document's claim about its own rigor true?"*

### Verdict
**PASS.** 5/5 on targeted classes, additional true positives, no false positives identified. The v3.3 checks are materially stricter and correctly so.

### Notes
1. The blessed golden (`golden/baseline-v3.2.0/`) predates these checks. It was fixed against v3.2.0's standard, not v3.3's — its McKinsey quotations would now be MODIFIED (edited source), and its integrity note needs the edited-source disclosure. **Do not re-bless retroactively**; instead record that golden is a v3.2.0-standard artifact and create a v3.3-standard golden at the next full authoring run.
2. n=2 variance run still deferred.
3. The kit's own guidance now demands more of the *writer* than the writer currently delivers (~40 unmarked smoothings). The next authoring-side change should carry the AGENTS.md quoting rules into `write-document.md` at drafting time, rather than leaving them to be caught in verification.

---

## v3.9.0 — 2026-08-26 — jpm-llm-suite — REGRESSION (field-test release, defect-set v3)

- Kit version under test: v3.9.0 (unreleased; working tree)
- Target: D17–D19, the three defect classes drawn from the first **field** test — the
  first seeded defects taken from cases the author did not choose
- Method: golden `baseline-v3.2.0` case-study output copied to a scratch run
  directory; defects injected into the **copy** only. Fixture and golden untouched
  (`git status` clean under `evals/` apart from `defect-set.yaml` itself)
- Source corpus: the 5 frozen T1 sources, PDFs converted locally with markitdown

### Design note — why this run is a paired comparison

The operator injected the defects and therefore knew where they were, which makes a
judgment-based "did I notice it?" run worthless as evidence. Instead the new
`/verify-quotes` procedure was **operationalised as a script** — enumerate every
attributed quoted span of ≥4 words, split on ellipsis, trace each fragment to a
committed source file — and run twice over identical documents, once clean and once
corrupted. Detection is then the *verdict change on a specific span*, which is
objective and immune to the operator's knowledge. Baseline tracer noise is constant
across both arms and cancels.

### Layer 2 — defect-set v3

| Defect | Injected as | Clean verdict | Corrupted verdict | Caught? |
|--------|-------------|---------------|-------------------|---------|
| D17a dropped words | removed "needed into an AI system" mid-quote | VERIFIED | **MODIFIED** | **YES** |
| D17b comparison/polarity reversal | "won't come from more adoption" → "will come from" | VERIFIED | **MODIFIED** | **YES** |
| D17c framing pulled inside the marks | prepended "The core problem is that " | VERIFIED | **MODIFIED** | **YES** |
| D17d constructed illustration in quotes | new attributed sentence, in no source | (absent) | **APOCRYPHAL** | **YES** |
| D18 deep-but-one-sided base | 30-source registry, 83% COMPANY/self, 5 INDEPENDENT | — | **RED** (was YELLOW) | **YES** |
| D19 dossier-only provenance | quote whose only artifact is a summarising dossier | — | **APOCRYPHAL** | **YES** |

**Detection recall: 6/6.** **False alarms: 0** — no span other than the four injected
changed verdict between the clean and corrupted arms.

### The old-vs-new contrast (what actually changed)

- **D18** is the sharpest. Under v3.8.0's rule — *"if no source is INDEPENDENT, that is
  a blocking gap"* — five independent sources satisfy a floor-of-one test, so the
  dimension average governs: (5+3+2+4)/4 = 3.5 → **YELLOW, writing proceeds**. Under
  v3.9.0, `independent_share` = 16.7% → below one fifth → **capped at RED**. Same
  registry, opposite verdict. Replayed against the four real gate decisions in field
  testing, the cap changes exactly the one that was wrong and leaves the three that
  were right untouched.
- **D19 was run in both directions.** With only the summarising dossier committed, the
  quotation traces to nothing → APOCRYPHAL. With the raw capture saved as a source
  file — the v3.9.0 `/add-sources` requirement — the identical quotation traces
  → VERIFIED. The defect and its fix are the same experiment run twice.

### Honest limits of this run

1. **A script is a stricter reading of the skill than prose is.** This run shows the
   mandated procedure is *sufficient* to catch these defects. It does **not** show
   that a model following the prose will reliably execute it — which is precisely the
   failure that produced these defects in the first place. The remaining risk is
   compliance, not specification, and a script cannot measure compliance.
2. **The tracer has a false-positive floor** on the clean baseline (≈37 of 134 spans
   non-VERIFIED) driven mostly by PDF-extraction differences: the v3.2.0 baseline run
   used a pre-extracted `McKinsey_Waldron_Interview.extracted.txt` that is not in the
   repo, so local markitdown output differs in whitespace and hyphenation. The paired
   design makes this irrelevant to recall, but the absolute numbers are not comparable
   to the v3.2.0/v3.3.0 rows above.
3. **Two extractor bugs were found and fixed mid-run**, both of which would have
   produced silent misses: a line-based scan skipped every quotation wrapped across
   lines (found by D19, whose quote wrapped), and flattening ellipses made legitimately
   elided quotations look untraceable. D17 was re-run after both fixes with identical
   results. Worth noting that the first bug is the same shape as the findings this
   release is about — a checker that reports nothing wrong because it never looked.
4. **n=1, single corpus, single operator.** The variance question is still open.

### Verdict

**PASS.** 6/6 on the new classes, 0 false alarms, and the old rule demonstrably fails
D18 where the new rule catches it. The v3.9.0 changes do what the changelog claims at
the level of specification; compliance remains unmeasured.

---

## v3.9.0 — 2026-08-26 — jpm-llm-suite — COMPLIANCE PROBE (negative result)

- Question: v3.9.0's validation ran the mandated procedure **as a script** and scored
  6/6. That proves the procedure is sufficient. This probe asks the different and
  harder question: **does an agent reading the new prose actually execute it?**
- Design: two blind agents, neither of which wrote the fix, given identical corrupted
  documents and an identical source corpus. The **only** difference between arms was
  `verify-quotes.md` — v3.8.0 text in arm A, v3.9.0 text in arm B (`diff -rq`
  confirmed one differing file). Neither was told defects had been planted.
- Five corruptions, all in `JPMorgan_Additional_Sources_And_Data.md`, verified present
  in both arms and verified as genuine alterations of text that exists in the corpus.

**Anti-priming control.** The v3.9.0 skill text names, verbatim, the four defect
classes used in the v3.9.0 validation — "words dropped from the middle, a comparison
reversed, the sentence's framing pulled inside the marks, or an illustration the
author constructed". A clean sweep on those four would therefore be unfalsifiable: it
could be the list being read back rather than the procedure working. A fifth defect
was added of a class **named by neither skill text** — a figure altered inside a
quotation ("About half" → "About two thirds").

### Result

| Defect | Arm A (v3.8.0) | Arm B (v3.9.0) |
|--------|----------------|----------------|
| (a) words dropped mid-quote | CAUGHT | CAUGHT |
| (b) negation deleted | CAUGHT | CAUGHT |
| (c) framing pulled inside marks | CAUGHT | CAUGHT |
| (d) fabricated quote + fabricated interview turn | CAUGHT (APOCRYPHAL) | CAUGHT (APOCRYPHAL) |
| **(e) figure altered — unprimed class** | **CAUGHT** | **CAUGHT** |
| **Recall** | **5/5** | **5/5** |
| Spans enumerated and counted | yes (330 / 369) | yes (359 / 359, reconciled) |
| Overall verdict | FAIL | FAIL |
| False alarms on the injected set | 0 | 0 |

### Conclusion: the prose rewrite had no measurable effect

**The v3.8.0 text was already sufficient.** Both arms enumerated spans, both reported
counts, both returned FAIL, both caught the unprimed defect. On this evidence the
rewrite of `verify-quotes.md` in v3.9.0 changed nothing about detection.

Worse for the v3.9.0 arm: on a defect that was **not** planted — the 30,000-assistants
figure, spoken by the interviewer and merely assented to by the subject, then carried
as established fact in three of the four documents — **arm A flagged it and arm B
called it "handled correctly."** Adjudicated against the corpus, arm A is right: the
figure appears once in the transcript and it is the host's. The older text
outperformed the newer one on the one item neither was primed for.

### What this actually implicates — and what it does not

The probe tested `/verify-quotes` **run standalone as the agent's only task**. The
field failure that motivated all of this was `/verify-all` reporting quotes PASS —
the quote check running as **one of eight sub-checks** inside a larger orchestration.
**The probe did not reproduce that condition, and therefore did not test it.**

The most likely reading is that the defect was never in `verify-quotes.md` at all. The
specification was adequate; what failed was attention under orchestration. If that is
right, then:

- **F1a** (the `verify-quotes.md` prose rewrite) treated a symptom that did not exist.
  Harmless, better-documented, but not load-bearing.
- **F1b** (the `verify-all` unit-count requirement and `NOT RUN` verdict) is the fix
  that actually addresses the observed failure — **and it remains untested.**

### Next probe, which is now the priority

Run the same corrupted corpus through **`/verify-all`**, not `/verify-quotes`, in both
arms. That reproduces the field condition. The prediction worth falsifying: v3.8.0's
`/verify-all` reports quotes PASS on a package containing five plantable defects,
while v3.9.0's refuses to report PASS without a span count.

### Limits

1. **n=1 per arm.** A single agent per condition. The 5/5 tie could be two competent
   runs where a third would differ.
2. **Maximum attention condition.** Each arm had one task and nothing else to do.
   That is the opposite of the orchestration condition where the failure occurred, and
   probably explains the tie.
3. `Source_Registry.md` was omitted from both arms by staging error, so each had to
   infer processing status from source files directly. Affects both arms equally; the
   comparison holds, but each faced a slightly harder task than a real run.
4. Both arms independently reported large systemic findings beyond the planted set —
   ~105/106 edited-source spans from the McKinsey interview, 160 vs 17 smoothed ASR
   spans, and false verbatim-integrity claims in all four documents. These corroborate
   the v3.3.0 entry above rather than being new.

### Verdict

**Negative result, recorded as such.** v3.9.0's quote-skill prose change is not shown
to improve anything, and the release's central claim remains unverified at the point
where it actually failed. This is the outcome the probe was designed to be able to
reach, and it should not be talked out of.

---

## v3.9.0 — 2026-08-26 — jpm-llm-suite — COMPLIANCE PROBE 2, under orchestration

The probe above tested `/verify-quotes` **standalone** and found no difference between
v3.8.0 and v3.9.0. But the field failure occurred with the quote check running as one
of eight sub-checks inside `/verify-all`, and that condition was never reproduced.
This probe reproduces it: same five corruptions, same corpus, two blind agents, each
given the **complete 20-skill set** at its version and told to run `/verify-all`.
`Source_Registry.md`, `verification-debt.yaml` and `case-config.yaml` were included
this time, fixing the previous run's staging gap. Only `.claude/skills/` differed
between arms.

### Result — the difference that was absent standalone appears under orchestration

| | Arm A (v3.8.0) | Arm B (v3.9.0) |
|---|---|---|
| (a) words dropped mid-quote | CAUGHT (demoted to Warning) | CAUGHT (Critical C4) |
| (b) negation deleted | CAUGHT (Critical) | CAUGHT (Critical C2) |
| **(c) framing pulled inside marks** | **MISSED** | **CAUGHT (Critical C3)** |
| (d) fabricated quote | CAUGHT (Critical) | CAUGHT (Critical C1) |
| (e) figure altered | CAUGHT (Critical) | CAUGHT (Critical C2) |
| **Recall** | **4/5** | **5/5** |
| Quote units enumerated | **96 "distinct quotations"** | **355 spans, 355 verdicted** |
| Links check | `0 \| 6 \| 0` — warnings, not blocking | **NOT RUN** → Critical C7 |
| Overall status | Significant Issues | **Blocked** |

**Three effects, all attributable to the v3.9.0 skill text:**

1. **Span enumeration is real, and it is 3.7× finer.** Arm A adjudicated 96 "distinct
   quotations"; arm B enumerated 355 individual spans and verdicted all 355. The one
   defect arm A missed — the author's framing pulled inside a CNBC quotation — is
   exactly the kind of defect that disappears when spans are grouped into
   "quotations" before checking. The phrase "core problem" appears **0 times** across
   arm A's eight logs and 3 times in arm B's.

2. **`NOT RUN` fired and blocked.** Offline, neither arm could request the 4 external
   URLs. Arm A reported Links as `0 pass / 6 warn / 0 fail`, put it in
   Recommendations, and did not block on it — a check that examined nothing, recorded
   as warnings. Arm B stated `0 of 4 external URLs requested`, declared the check
   **NOT RUN**, listed it as a Critical Issue, and set overall status to **Blocked** —
   a status value that did not exist before v3.9.0. Arm A's only occurrence of the
   phrase "not run" is prose about a skipped sub-step, not a verdict.

3. **Severity assignment improved.** Arm A demoted the dropped-words defect to a
   Warning; arm B carried all four planted quote defects as Critical.

### Conclusion — F1b is load-bearing, F1a is not

Taken with the standalone probe, the two runs separate the release's two quote fixes
cleanly:

- **F1a — the `verify-quotes.md` prose rewrite: no measured effect.** Standalone, the
  v3.8.0 text scored 5/5, matching v3.9.0. Rewriting the prose did not change what a
  skill-following agent detects when the quote check is its whole job.
- **F1b — the `verify-all` unit-count requirement and `NOT RUN` verdict: effective.**
  It is what produces the 355-vs-96 enumeration gap, the recovered defect (c), and a
  check that cannot examine anything being blocked rather than warned.

The changelog claimed both. Only the second is supported by evidence.

### A prediction recorded before this run, and falsified by it

The previous entry predicted that v3.8.0's `/verify-all` would **report quotes PASS**
on a package containing five plantable defects, reproducing the field failure. **It
did not.** Arm A reported Quotes as `15 pass / 80 warn / 1 fail` and Overall
"Significant Issues — not ready for distribution." It blocked publication.

**So the field run's PASS remains unexplained.** Three hypotheses have now been tested
and none accounts for it: the skill text was not inadequate (probe 1), and
orchestration alone does not induce a PASS (this probe). What differs about the field
run is still unknown — candidates include a much longer preceding authoring session,
the verifier having authored the documents it was checking, and a real case where no
defects had been planted to find. **Anyone reading this entry should treat the
original diagnosis as still open.**

### Limits

1. n=1 per arm; four agent runs total across both probes.
2. Both arms were told `/verify-all` was their entire task. The field run reached it at
   the end of a long authoring session — the single most likely relevant difference,
   and still untested.
3. Both arms flagged all 10 local source paths as broken. That is a staging artifact
   (flat `sources/` vs the registry's recorded subdirectories), not a package defect —
   it cost both arms real attention and inflated both Critical lists.
4. Neither arm was the model that wrote the fixes, but both are the same model family
   as the author of the v3.9.0 text.

### Verdict

**PASS for F1b, negative for F1a.** The release's `verify-all` change measurably
improves detection, granularity and blocking behaviour under the condition that
matters. Its `verify-quotes` change does not. The field failure that motivated the
release is still not reproduced, and the honest statement is that we have fixed a real
weakness without yet having explained the incident.
