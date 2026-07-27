# Run Eval

Execute a regression run of the kit against a frozen fixture, so results are comparable across versions. **Maintainer skill** — for template development, not case authoring.

## Usage

```
/run-eval [fixture-name]
```

Defaults to `jpm-llm-suite`. See `evals/EVALS.md` for the method and `evals/test-log.md` for previous runs.

## Why comparability is the whole point

A regression number only means something against an identical baseline. Change the corpus, the scripted answers, or the scoring method between runs and the comparison is worthless — you will be measuring drift in the test rather than change in the kit. Verify the corpus hashes before every run and stop if they do not match.

## Instructions

### 1. Decide what actually needs testing

Not every change warrants a full run. Match the test to the change:

| What changed | What to run |
|--------------|-------------|
| Documentation, packaging, terminology | Nothing. Say so rather than burning a run |
| A verification or assessment skill | Layer 2: inject the defect classes that skill should catch |
| The authoring skills | Full pipeline + all three layers |
| A coaching skill | The probes in `probe-set.yaml`, scored against recorded ground truth |

State which you are running and why before starting.

### 2. Prepare an isolated run directory

Outside the repository — eval runs are large and must never be committed:

```bash
RUN=../eval-runs/run-$(date +%F)-A
mkdir -p "$RUN"
git archive vX.Y.Z | tar -x -C "$RUN"        # the version under test, not the working tree
rm -rf "$RUN/evals" "$RUN/.github"            # template-only; not part of a case project
cp evals/fixtures/<fixture>/case-config.yaml "$RUN/"
rsync -a --exclude COPY_SOURCES_HERE.md evals/fixtures/<fixture>/sources/ "$RUN/sources/"
```

**Verify the corpus before doing anything else:**

```bash
cd "$RUN" && find sources -type f -exec shasum -a 256 {} \; | sort -k2
```

Compare against `CORPUS_MANIFEST.md`. Any mismatch: stop and investigate. Extract text from PDFs (`pdftotext -layout`) into the run directory only — never into the frozen fixture.

### 3. Use separate agents for separate roles

This is not ceremony. In the baseline run the writing pass produced a spliced quotation while following the rules carefully, and a fresh verification pass caught it. An agent that checks its own work will not find that class of error.

- **Writer** — follows the kit's skill files, answering from the fixture's `setup-answers.md`
- **Verifier** — fresh context, never saw the drafting, adversarial by instruction
- **Judge** — a *different model* from the writer, for Layer 3 rubric scoring

Give the verifier and judge no access to ground truth. A defect-detection score means nothing if the agent was handed the answer key.

### 4. Score all three layers

Per `evals/EVALS.md`: deterministic grounding (`scripts/grounding_check.py` — a lead generator, not a gate), seeded-defect recall from `defect-set.yaml`, and judged quality. For coaching skills use `probe-set.yaml` instead.

Run at least twice when a result will be used to fail a future version. A difference smaller than run-to-run variance is noise.

### 5. Record the run — including failures

Append to `evals/test-log.md` using the template at the top of that file. Never rewrite a previous entry.

Two sections matter most and are the easiest to skip:

- **What changed in execution** — behavioral differences noticed while running: questions the skills asked differently, gates that behaved unexpectedly, places instructions were ambiguous enough to require improvisation. Several kit improvements originated here rather than in the scores.
- **Actions arising** — every miss becomes a new entry in `defect-set.yaml`. Production bugs are test cases wearing disguises.

### 6. Interpret honestly

A stricter version will score *worse* against artifacts blessed under looser standards. That is not a regression; it means the standard became accurate. Say which standard a baseline was blessed under and never retroactively re-bless — record the change instead.

If the kit's own output violates the kit's own rules, that is a finding about the authoring skills, not an embarrassment to hide. It is the most valuable thing a run can produce.
