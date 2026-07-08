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
