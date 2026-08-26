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
