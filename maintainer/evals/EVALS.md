# Regression Testing the Kit Against Real Source Material

How to confirm a new kit version still works — and works *better* — by running it against a frozen corpus of source materials (e.g., the JPMorgan LLM Suite sources), and how to test outputs that require judgment.

---

## Why this exists

The kit's outputs are prose, not code: a new version can't be "unit tested" in the ordinary sense. But most of what matters *can* be measured, and the part that can't be measured can be compared. The design below separates three layers, from fully objective to human-judged.

## The fixture: a frozen source corpus

Pick a case with rich, already-collected sources — the JPMorgan AI case is ideal (VentureBeat "Beyond the Pilot" interview, McKinsey interview with Derek Waldron, Bloomberg TV Dimon interview, CNBC exclusive, Q3 2025 earnings).

```
maintainer/evals/fixtures/jpm-llm-suite/
  case-config.yaml        ← frozen, fully filled in
  setup-answers.md        ← scripted answers to every question the skills ask
  sources/                ← the frozen corpus (copied in locally; see note below)
  CORPUS_MANIFEST.md      ← file list + SHA-256 hashes + retrieval dates
  golden/                 ← a "blessed" output package from a known-good run
```

> **Note**: `maintainer/evals/fixtures/*/sources/` is gitignored in the public template (copyright — see `templates/SOURCE_ACQUISITION.md`). Keep the corpus in your private JPM case repo and copy it in when running evals. The MANIFEST (hashes only) is committed, so any runner can confirm they're testing against the identical corpus.

## Running a regression pass

For each new kit version:

1. Create a fresh temp project from the template at the version under test.
2. Copy in the frozen corpus and config.
3. Run the standard pipeline with a single agentic harness, answering prompts from `setup-answers.md`: add-sources → assess-sources → write-document (×4) → verify-all.
4. Record the run context: **kit version, harness + version, model + version, date**. Model drift is a real confound — when comparing kit v3.2 to v3.3, use the same model for both runs whenever possible; when the model changed too, say so in the log.
5. Score the output (below) and append results to `maintainer/evals/test-log.md`.

Run the pipeline **twice** (n=2 minimum, n=3 better). LLMs are nondeterministic; a single run can't distinguish a regression from noise. Report ranges.

## Layer 1 — Deterministic checks (objective, scriptable, every run)

| Check | Metric |
|-------|--------|
| All four documents produced, no placeholder text remaining | pass/fail |
| Word counts within configured ranges | pass/fail per doc |
| **Quote grounding rate**: every quoted string in the output found (fuzzy match) in the corpus | % — should be 100 |
| **Number grounding rate**: every figure in output traceable to a corpus document | % |
| Verification debt at end of run | count — should be 0 open |
| Source Registry consistent with files present | pass/fail |
| Bibliography entries match in-text citations | pass/fail |
| Internal arithmetic (percentages vs. underlying numbers) | error count |

These catch the worst failure mode — fabrication — without any judgment at all.

## Layer 2 — Seeded-defect probes (the trick for testing judgment tools)

You can't easily score "is this verification skill *wise*?" — but you can score **"does it catch planted defects?"** Before a run, copy the corpus and deliberately inject known errors:

- Change one revenue figure in a financial source copy referenced by the draft
- Misattribute one quote (right words, wrong speaker)
- Add one plausible fabricated quote to the draft
- Shift one date to create a timeline impossibility
- Add one dead URL

Then run `/verify-all` and measure **detection recall** (how many of the N seeded defects were flagged?) and **precision** (how many flags were real vs. false alarms?). This converts "requires judgment" into a number, and it's the single best regression signal for the verification skills — if v3.3's checks catch 9/10 seeded defects where v3.2 caught 7/10, that's a real improvement; if it drops, that's a regression regardless of how nice the prose looks.

Keep the seeded-defect list in `maintainer/evals/fixtures/jpm-llm-suite/defect-set.yaml` (defect, location, expected detection) and grow it whenever a real-world miss is discovered — every production bug becomes a permanent test.

## Layer 3 — Judged quality (rubric + comparison, per release)

For narrative quality, teachability, and tension — the truly judgment-laden dimensions:

1. **Rubric scoring by an LLM judge.** Score the output against the Case Quality Rubric (see `templates/rubrics/` when added, or the criteria in AGENTS.md Writing Standards). Use a **different model than the one that wrote the case**, run the judge 3×, and report median + spread. Absolute scores drift, so treat them as directional.
2. **Pairwise comparison (more reliable than absolute scores).** Give the judge the new version's Main Case and the golden/previous version's Main Case, positions swapped across two calls, and ask which better serves a specified teaching objective, with reasons. Consistent preference across swaps = signal; split verdicts = tie.
3. **Human anchor, once per release.** A professor reads one document (rotate which) against the rubric and logs 3 observations. Periodically compare human scores to judge scores; if they diverge, recalibrate the judge prompt. Human reads are the expensive scarce resource — spend them per release, not per commit, and on the dimensions the judge is least trustworthy about (teachability, classroom feel).

### Principles for testing judgment-dependent output

- **Convert judgment to detection wherever possible** (Layer 2 — seeded defects).
- **Compare, don't score**: pairwise A/B with position swap beats absolute 1–5 ratings for reliability.
- **Separate writer and judge models**; a model grading its own homework is systematically generous.
- **Measure variance before trusting differences**: n≥2 runs; a difference smaller than run-to-run spread is noise.
- **Anchor to humans sparingly but regularly**, and use disagreement to improve the judge, not just the kit.
- **Track distributions over versions, not single points** — `test-log.md` is the memory.

## What "still working properly" means (release gate)

A version passes when: Layer 1 all green (quote/number grounding 100%, debt 0), Layer 2 detection recall ≥ previous version on the standing defect set, and Layer 3 pairwise verdict is "no worse" than the previous version's golden output. Log every run — including failures — in `maintainer/evals/test-log.md`.
