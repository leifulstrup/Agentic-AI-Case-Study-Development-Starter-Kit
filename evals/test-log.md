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

## v3.2.0 — 2026-07-07 — (no corpus run yet)

- Status: **Framework established with this release; no regression run executed.**
- v3.2.0's changes are documentation, licensing, and instruction-file structure — no changes to write-document or assess-sources logic. The one behavioral change is `/verify-quotes` (confidence verdicts + trace-to-primary rule), which should *increase* Layer 2 quote-defect detection.
- **Next action**: build the `jpm-llm-suite` fixture (copy sources from the private JPM case repo, write CORPUS_MANIFEST.md and setup-answers.md, seed defect-set v1), run the first baseline pass against v3.2.0, and designate that output as `golden/`. All future versions compare against this baseline.
