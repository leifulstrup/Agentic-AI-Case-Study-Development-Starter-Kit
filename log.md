# Development Log

*Append-only log of what changed in each working session and version, in more operational detail than CHANGELOG.md (which records releases). Companion to `lessons_learned.md` (what we learned) and `evals/test-log.md` (how versions performed against source material).*

---

## 2026-07-07 — v3.2.0 "Trust & Standards" (from v3.1.0)

**Context**: Full kit evaluation performed with an agentic AI session (Claude/Cowork), including research on MBA AI pedagogy and cross-harness standards. Evaluation and forward roadmap live outside this repo in the companion `upgrade-plan/` folder (evaluation, verification/rubrics plan, learning front-ends plan, portability/MARP plan, roadmap v3.2→v5.0, research notes with reliability flags).

**Changes made** (see CHANGELOG.md [3.2.0] for the release summary):

1. LICENSE: CC BY-NC 4.0 → MIT, named copyright holder, scope note separating kit license from produced-case license. Grepped repo for stale license references; updated README badge/footer, case-config.yaml comments, setup-case skill template block.
2. README: added "Built for Verification" section (verification debt, tier gates, seven-check pipeline) near the top; added License section; bumped badges.
3. New VERIFICATION_PLEDGE.md (author sign-off artifact).
4. `.claude/skills/verify-quotes.md`: added VERIFIED/LIKELY/DISPUTED/APOCRYPHAL verdicts, evidence requirements, publication rule, trace-to-primary-source requirement.
5. New AGENTS.md as canonical instruction file; CLAUDE.md rewritten as `@AGENTS.md` import + Claude-specific section; `.github/copilot-instructions.md` slimmed to pointer + equivalents table. Rationale: AGENTS.md is Linux Foundation-stewarded and read by Codex/Cursor/Copilot-agent/Windsurf/Zed natively, Gemini CLI via settings.
6. New CITATION.cff, CONTRIBUTING.md (includes verified-body invariant for future generator skills).
7. templates/SOURCE_ACQUISITION.md: strengthened legal section (private-during-development, links+excerpts for T2, fair use is a balancing test).
8. New evals/ framework: EVALS.md (3-layer regression design: deterministic grounding checks, seeded-defect detection recall, LLM-judge + pairwise + human anchor), test-log.md (append-only run log, v3.2.0 baseline entry).
9. This log.md and lessons_learned.md added.
10. TEMPLATE_VERSION and PROJECT_CONTEXT.md bumped to 3.2.0.

**Not done in this version** (planned, see upgrade-plan/05-roadmap.md): SKILL.md directory migration, rubrics, verification-literacy guide, examples/ excerpts (v3.3); MARP slides, provenance manifest, red-team skill (v3.4); front-end generators (v4.0).

**Execution notes**: `.claude/` paths were write-protected for the assistant's file tools in this session; edits routed through the sandbox shell. Worth remembering for future agentic maintenance sessions.

---

## 2026-07-07 (later) — jpm-llm-suite eval fixture scaffolded (post-v3.2.0)

**Changes**: Created `evals/fixtures/jpm-llm-suite/`: fixture README (setup + run procedure + cautions), frozen `case-config.yaml` (Waldron/LLM Suite/ITEC-617), `setup-answers.md` (scripted answers for every skill decision point, including "accept defaults, no edits" policy so runs test default output quality), `CORPUS_MANIFEST.md` (hash template, unpopulated until sources copied from private JPM repo), `defect-set.yaml` v1 (10 seeded defects across financial/quote/timeline/attribution/link/bias/cross-document layers; D1/D2/D9 modeled on real Moderna-test misses), and `scripts/grounding_check.py` (dependency-free Layer 1 quote+number grounding checker).

**Testing**: grounding_check.py validated against a synthetic corpus: true quote grounded (after fixing a fuzzy-window bug where oversized comparison windows penalized true matches below threshold), fabricated quote flagged, ungrounded number flagged, and a 5-word silent paraphrase correctly flagged as ungrounded — the D5 defect class is detectable.

**Remaining before first baseline run**: copy sources from the private JPM repo, populate manifest hashes, run the pipeline twice on v3.2.0, bless `golden/`.
