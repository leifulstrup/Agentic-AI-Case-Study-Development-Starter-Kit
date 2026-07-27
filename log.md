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

---

## 2026-07-08 — Corpus frozen + BASELINE EVAL RUN executed (v3.2.0, jpm-llm-suite)

**Corpus**: Leif copied 6 source files from the private JPM repo; sorted into type subfolders; SHA-256 manifest frozen as corpus v1.

**Run**: full pipeline executed via agent harness in `eval-runs/run-2026-07-08-A/` (kept outside the repo). Writer agent (claude-fable-5) followed the kit's skill files with scripted setup-answers; separate fresh verifier agent ran verify-all; separate opus judge scored the rubric. Defected variant (`-defected/`) carried all 10 seeded defects from defect-set v1.

**Results** (full detail in `evals/test-log.md`): 4/4 documents produced (GREEN gate); agent-traced quote verification ~97% VERIFIED with real flaws caught (spliced quote, altered wording, garbled attribution) → clean-run status "Needs Review" = publication gate correctly blocked; **seeded-defect recall 10/10, zero false alarms**; opus rubric 31/35, "teach with minor edits," weakest = data sufficiency (no quantitative exhibit).

**Output staged**: `evals/fixtures/jpm-llm-suite/golden/baseline-v3.2.0-candidate/` (gitignored) — awaiting Leif's human review before blessing as golden.

**Baseline blessed (same day, per Leif)**: all verify-flagged issues fixed surgically (FIXES-2026-07-08.md), 6 definitional citations web-confirmed and added as T3 references, debt 9/9 verified. `golden/baseline-v3.2.0/` is the release-gate comparator; Leif's original Jan 2026 human-finished package added as `golden/reference-human/` ceiling anchor. Fixes spot-checked independently against transcripts before blessing.

**Actions queued for v3.3** (from run observations): ASR-transcript quoting rule; MODIFIED verdict for spliced/silently-corrected quotes; voice-based (not outlet-based) bias counting; quote counting unit; filename tolerance in verify skills; grounding_check.py v2 (attribution-aware extraction — v1 false-flags rhetorical quotes at ~45%); defect-set v2 adds spliced-quote and silent-correction classes; n=2 variance run.

---

## 2026-07-08 (later) — /coach-case: the coach & advisor cycle (post-v3.2.0, toward v3.3)

**Direction from Leif**: the kit should coach the case developer — find holes in source types and foundational confidence, offer to research additional material (including bios of the protagonist and other named people/orgs), iterate with version control, logging, and QA/QC of whether additions help or hurt.

**Built**: `.claude/skills/coach-case.md` — six-phase loop: Diagnose (5-lens Gap Map: source types, voice-based perspectives, load-bearing-claim confidence, people/org biographical grounding, rubric-facing weaknesses) → Coach (max 3 gaps at a time, each with a pedagogical why + research offer) → Research (with permission; primary-source-first; bios saved as sources/reports/BIO_[Name].md) → QA/QC gate (provenance/independence/corroboration/tier/risk; rejections logged; conflicts kept as teachable discrepancies) → Measure (re-run assessment, record deltas + HELPED/NEUTRAL/HURT) → log iteration to coaching/coaching-log.md + git checkpoint. Plus `templates/COACHING_LOG.md`; wired into AGENTS.md (behavior rule + workflow table), README, WORKFLOW.md, CLAUDE.md, copilot equivalents; CHANGELOG [Unreleased]. Design rationale in upgrade-plan/07-coach-and-advisor.md, including eval hooks (gap-detection recall + QA/QC discrimination probes for a future defect-set).

**Design notes**: lenses 2 and 4 come straight from baseline-run findings (outlet-vs-voice bias miscount; Buehler misattribution traced to missing bio grounding). Impact measurement is deliberately allowed to say a new source HURT.

---

## 2026-07-09/10 — Pipeline bookends: /scout-case + learning-context.yaml (toward v3.3)

**Direction from Leif**: explore a pre-case sourcing coach and post-case mass-customization front-ends tailored to student/classroom context. Also: whether to fork a new private "2.0" repo.

**Repo strategy decided**: no fork. Two remotes on one clone — private dev repo as `origin` (default push target, can hold copyrighted eval corpus), public template as `public` (curated releases only). Documented in `RELEASING.md` with a pre-publish checklist; `.gitignore-private` variant provided for the private repo where corpus/golden ARE tracked. Version lineage stays continuous (3.x) — marketing "2.0" is a separate label for a future public relaunch.

**Built**:
1. `.claude/skills/scout-case.md` (18th skill) — pre-commitment scouting of 1–4 candidates across five evidence areas (protagonist voice and decision moment fatal-if-absent), scored on the same four dimensions as `/assess-sources` plus tension quality and effort estimate; verdicts PURSUE / VIABLE WITH WORK / REDIRECT / AVOID; outputs comparison table, per-candidate detail, recommendation, and a starter source list feeding `/add-sources`. Verdict recorded in PROJECT_CONTEXT so later coaching distinguishes known-from-the-start gaps from new ones.
2. `learning-context.yaml` — classroom config (audience/session/teaching/front_ends/guardrails) that front-end generators will read for tailoring. Guardrails from design doc 03 are now machine-readable (`verified_body_only`, `provenance_header`, `reveal_outcome`).
3. Wiring: AGENTS.md (behavior rule, process model now shows SCOUT + COACH loop, workflow table, file structure), README (skills table, contents, 18-skills count), WORKFLOW.md (new Phase 0: Scouting), CLAUDE.md, copilot equivalents, CHANGELOG [Unreleased].
4. Local backup `eval-assets-backup-2026-07-27.tar.gz` (2.2 MB) of the gitignored corpus + golden baselines — they existed on one laptop only.

**Design rationale**: upgrade-plan/08-scout-and-learning-context.md, including three eval hooks — scouting calibration against the baseline's actual assessment scores (systematic optimism is measurable), scouting discrimination (strong vs. unworkable candidate), and context sensitivity (same front-end under two contexts must actually differ).

**Not done**: `/setup-context` conversational writer for learning-context.yaml (currently hand-edited, which violates the kit's no-manual-YAML principle — fix when generators land); public-policy scouting variants.

---

## 2026-07-27 — Coaching-skill probes against the JPM fixture

**Rationale**: the authoring pipeline is unchanged since the v3.2.0 baseline, so re-running it would measure model variance, not kit improvement. Probed the two genuinely new skills against ground truth the baseline already established.

**Probe A — /coach-case gap detection** (offline, `eval-runs/probe-2026-07-27-coach/`): **6/6 recall** on known gaps, plus **8 verified novel findings** the baseline's verification pass and rubric judge both missed — including that the VentureBeat episode is vendor-sponsored (Outshift by Cisco), that the McKinsey source says on its face it was "edited for clarity and length" while being quoted as verbatim, a third unreconciled headcount figure (Dimon's "600,000"), and that the case's title number (30,000 assistants) is confirmation-by-assent from the host rather than a Waldron statement. All four spot-checked against the corpus and confirmed true. Zero false positives in the sample. The probe also challenged the baseline's own assessment scores with reasons (Reliability 5 → 3-4, Breadth 3 → 2).

**Probe B — /scout-case calibration + discrimination** (web-enabled, no sources in hand): predicted 5/4/4/4 vs. actual 5/3/5/4 — **MAE 0.5, signed error 0**, i.e. no systematic optimism, which is the specific defect this probe exists to catch. Correctly separated PURSUE (JPMorgan) from REDIRECT (Bloomberg L.P. — private partnership, completeness gap uncloseable by effort) and offered a reframe (BloombergGPT frozen at March 2023) rather than a bare rejection, as the skill specifies.

**Cross-probe finding**: both independently flagged the frozen corpus as stale (nothing after Dec 2025; the scout found an Apr 2026 Dimon letter and a 2026 shift from voluntary adoption to tracked usage). Decision recorded: keep corpus v1 frozen for regression comparability; build a corpus v2 separately if teaching realism is wanted. Different jobs, different corpora.

**Added**: `evals/fixtures/jpm-llm-suite/probe-set.yaml` — makes both probes repeatable with recorded pass criteria and baseline results, the coaching analogue of defect-set.yaml.

**New actions queued**: fix the inaccurate "All quotations verbatim" assertion; add a source independence/interests column to the Source Registry (both the Cisco sponsorship and McKinsey's commercial interest fell through that hole); `/assess-sources` should check for ASR/editor-processing disclaimers before allowing T1; defect-set v2 gains sponsored-source and third-headcount classes.

---

## 2026-07-27 — v3.3.0 "Source Integrity" released

**Theme**: everything the probes and baseline run found. Tier measured access; nothing measured interest or quotability; documents asserted rigor they couldn't support.

**Built**: Independence column + Processing Status in the registry; capture at registration in `add-sources`; integrity step in `assess-sources` ahead of the gates (with Reliability downgrade when quoted sources are EDITED/ASR); MODIFIED verdict in `verify-quotes` covering five look-verbatim-but-aren't classes plus an integrity-claim check; voice-based counting in `assess-bias`; integrity-claim audit in `add-disclaimers`; canonical Quoting Rules in AGENTS.md; defect-set v2 (16); grounding_check v2.

**grounding_check v2 finding worth remembering**: the ~45% false-flag rate was NOT rhetorical quoting as first assumed. It was a quote-parity bug — a single character class for open and close marks meant one unpaired quote flipped pairing and the checker compared *narrative prose between quotations* against the corpus. Documents using straight quotes only (306 in the test corpus) are especially exposed since straight marks are open/close ambiguous. Fixed by matching curly and straight separately plus rejecting captured prose by content. 54.8% → 78.7% on identical input; residual gap is PDF line-break artifacts and borderline compound phrases. Still a lead-generator, not a gate.

**Regression** (`evals/test-log.md`): 5/5 on the new defect classes (D12–D16), pre-existing defects re-caught, plus novel finds (two more silent ASR corrections, a Supplement splice, ~40 unmarked smoothings). Headline: same documents, v3.2.0 reported ~225 VERIFIED; v3.3.0 reports ~33 of ~195 because three of five sources can't support verbatim quotation. The standard became accurate.

**Open items**: golden baseline is a v3.2.0-standard artifact — do not re-bless retroactively; create a v3.3-standard golden at the next full authoring run. Carry the AGENTS.md quoting rules into `write-document.md` so the writer follows them at drafting time rather than having verification catch ~40 smoothings after the fact. n=2 variance run still deferred.

---

## 2026-07-27 (post-release) — CI green for the first time

Published to both remotes; the public repo showed a failing check. Reproduced markdownlint locally against tracked files only (CI checks out the repo, so gitignored `golden/` case documents never reach it — 68 of the 78 local violations were phantom).

**Ten real violations, six of them pre-existing since at least v3.1.0** — CI has been red since before this work began, which is worth knowing: a red check that has always been red stops being read.

- `setup-case.md` (6, pre-existing): MD029 ordered-list numbering. Renumbering would have made procedural steps read 1,1,1,1 — worse for the human reader than for the linter. Disabled MD029 in `.markdownlint.json` instead; step numbers in instruction files are semantic.
- `CHANGELOG.md` (1, mine): duplicate `### Added` under [3.3.0], created when the release section was inserted above the existing unreleased block. Merged into one Added list and moved the regression summary to the end of the section — a genuine structure fix, not a lint workaround.
- `log.md` (3, mine): a `---` placed directly after a paragraph turned that paragraph into a setext heading (MD003 + MD026 trailing punctuation), plus a double blank line. Fixed by blank-line separation.

**Lesson**: lint the tracked file set, not the working directory — gitignored artifacts produce phantom failures that hide the real ones.

---

## 2026-07-27 (later) — examples/ folder: making the output visible

**Rationale**: the kit had 3 stars and 1 fork. A professor landing on the repo saw a README about verification debt and source tiering, and had to *imagine* the output. The blessed golden baseline — a complete, verified, four-document package — was sitting gitignored on one laptop. Publishing excerpts converts the abstract pitch into evidence at near-zero cost.

**Built**: `examples/` with a README (what went in, what came out, what verification found, what an independent judge scored, and honest caveats) plus five annotated excerpts — main case opening, teaching note objectives + session plan + discussion questions + verification coda, source registry showing tier/independence/processing as three separate questions, the `/verify-all` report including the two defects that blocked publication, and the verification-debt ledger showing an item tracked and resolved. Every excerpt ends with "what to notice" so a reader knows what they're looking at. Linked from the README package table and the file listings in README/AGENTS.

**Deliberate choices**: (1) the main case excerpt shows the **v3.3-standard** integrity note, not the v3.2-era one that shipped in the golden — publishing the old wording would have shipped the exact error the current release catches; (2) the verification report excerpt leads with the defects found rather than the clean numbers, because a quality report that only shows passes isn't credible; (3) the caveats section states plainly that this package has a thin, executive-heavy source base — the kit measured it, so hiding it would undercut the whole premise.

**Self-check caught an error**: the README claimed a ~32,000-word corpus. That came from a `wc` glob that matched extracted PDFs twice. True figure is ~22,000. Fixed before commit — a reminder that the kit's own standard applies to its marketing copy.
