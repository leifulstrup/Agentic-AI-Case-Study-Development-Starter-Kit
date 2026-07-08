# Fixture: jpm-llm-suite

Frozen regression fixture based on the JPMorgan Chase LLM Suite case (ITEC-617 Spring 2026 prototype). See `../../EVALS.md` for the method.

## What's committed vs. what you supply

| Item | Committed? | Notes |
|------|-----------|-------|
| `case-config.yaml` | Yes | Frozen configuration — do not edit between runs |
| `setup-answers.md` | Yes | Scripted answers to every question the skills ask |
| `CORPUS_MANIFEST.md` | Yes | File list + SHA-256 hashes; proves runs use identical sources |
| `defect-set.yaml` | Yes | Seeded-defect definitions (v1) for Layer 2 |
| `scripts/grounding_check.py` | Yes | Layer 1 quote/number grounding checker |
| `sources/` | **No** (gitignored) | Copy from the private JPM case repo before a run |
| `golden/` | **No** (gitignored) | Blessed baseline output; created after the first passing run |

## One-time setup

1. Copy the source files from the private `ITEC-617-Spring-2026-JP-Morgan-Chase-and-AI-Case-Study-Prototype` repo's `sources/` into `sources/` here (same subfolder structure: transcripts/, financial/, news/, reports/).
2. Generate the manifest hashes and paste the output into `CORPUS_MANIFEST.md`:
   ```bash
   cd evals/fixtures/jpm-llm-suite
   find sources -type f ! -name .gitkeep -exec shasum -a 256 {} \; | sort -k2
   ```
3. Commit the updated `CORPUS_MANIFEST.md` (hashes only — never the sources).

## Running a baseline or regression pass

1. Create a fresh working copy of the template at the version under test:
   ```bash
   git -C /path/to/kit worktree add /tmp/eval-run-$(date +%Y%m%d) vX.Y.Z
   # or clone at the tag
   ```
2. Copy `sources/` and `case-config.yaml` from this fixture into the working copy.
3. Verify the corpus: re-run the shasum command and diff against `CORPUS_MANIFEST.md`. Any mismatch = stop.
4. In your agentic harness, run the pipeline, answering prompts strictly from `setup-answers.md`:
   `/add-sources` → `/assess-sources` → `/write-document` (×4) → `/verify-all`
5. Record harness + model + date. Run the whole pipeline **at least twice** (separate working copies).
6. Score:
   - **Layer 1**: `python3 scripts/grounding_check.py <run-dir>/case-study sources/` (also do a manual spot-check — the script is a helper, not the referee)
   - **Layer 2**: run a third pass with defects injected per `defect-set.yaml`; count detections in the `/verify-all` report
   - **Layer 3**: pairwise-judge the Main Case against `golden/` per `../../EVALS.md`
7. Append results to `../../test-log.md`. If this is the first-ever run, review carefully by hand and, if it passes, copy the output package into `golden/`.

## Cautions

- **Don't fix the fixture mid-run.** If setup-answers.md is ambiguous, finish the run, then improve the fixture and note it in the log.
- **The corpus is frozen on purpose.** Real-world claims about JPMC will drift (the corpus captures 2025 reporting); the fixture tests the *kit*, not JPMC. Never "refresh" sources without bumping the fixture version and re-blessing golden.
- **Interesting known wrinkle worth testing**: public reporting on JPMC varies on employee count and adoption figures across sources. A good `/assess-sources` + `/verify-consistency` run should surface any such tension rather than silently pick one number — watch for this in Layer 3 review.
