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

---

## 2026-07-27 (later) — v3.4.0 "Adoption" released

Version bumped for the `examples/` addition (additive and user-facing = semver minor), the HBR→business-school terminology change, and the markdownlint CI fix.

**Release mechanics note worth remembering**: the `v3.3.0` tag pointed at `f950ebf`, but three commits had landed since. Cutting a GitHub Release from that tag would have produced a tarball *without* `examples/` — the very artifact built to make the kit evaluable. Rather than force-move a published tag, bumped to 3.4.0 so the release points at current main. `release.yml` fires on `TEMPLATE_VERSION` changes and auto-creates the GitHub Release from the matching CHANGELOG section, so the bump does the publishing.

**Version now lives in seven places** — TEMPLATE_VERSION, README badge + footer, case-config.yaml, setup-case.md's config template block, CITATION.cff, PROJECT_CONTEXT.md, VERIFICATION_PLEDGE.md. All updated; grep confirms no stale 3.3.0 outside historical records (CHANGELOG, logs, examples' note about which standard the golden reflects). This restating-in-seven-places is itself a small design smell; worth collapsing if it grows.

---

## 2026-07-27 (later) — v3.5.0: maintainer tooling + Perplexity guidance

**Rationale**: three consecutive releases were done by hand and each manual step failed at least once — version drift needing a follow-up grep every time, local lint disagreeing with CI, and a release nearly cut from a tag that predated its headline feature. None were hard problems; they were memory problems. A kit premised on "important work needs checklists and gates" was releasing itself on recall.

**Built and tested** (`scripts/`): `bump-version.sh` (7-file propagation + `--check` audit — tested against non-semver input, same-version, empty arg, single-file sabotage, and a full 3.4.0→9.9.9→revert round trip), `lint.sh` (tracked-files-only, matching CI — tested clean, violation detection, and `--fix`), `release-preflight.sh` (nine checks — **tested the two that matter by sabotage**: staged a fake copyrighted corpus file and confirmed it fails with DO-NOT-PUSH; created a commit after the tag and confirmed it detects "tag N commits behind HEAD," the exact v3.3.0 mistake), `release-notes.sh` (CHANGELOG section extraction — tested default arg, unknown version, older versions, and no next-heading bleed).

Preflight caught one false positive during its own testing: README's generic "`/slash-commands`" was being read as a skill name. Fixed by excluding that literal.

**Skills**: `/release-kit` (judgment layer — semver decision, changelog prose, then delegate to scripts; explicitly states which decisions are the human's and which are the script's) and `/run-eval` (fixture orchestration, role separation between writer/verifier/judge, and honest interpretation — including that a stricter version scoring worse against an older baseline is success, not regression).

**Perplexity guidance in README** — researched because AU faculty commonly have campus licenses. The finding that changes the advice: Perplexity's agentic surfaces mostly *cannot* touch a local repository. Comet's agent is blocked from `file://`; Computer's filesystem is an isolated cloud sandbox; only the Mac-only Personal Computer connects to a local folder, and git/shell are absent from its documented capabilities. Windows and Linux faculty have no local-file agent at all. So the honest framing is two tools, two jobs: Perplexity for scouting and sourcing (which is genuinely well suited to `/scout-case` and `/coach-case` work), an agentic tool for authoring and verification. Also flagged that inline citations make sources easy to find but do not confirm a source supports the claim attached to it — exactly the gap `/verify-quotes` closes. Two corrections worth noting: "Spaces" are now "Projects," and Comet is not Perplexity's most capable agentic surface.

**Note for the next release**: this one was cut *using* `/release-kit` and the scripts. First dogfooding.

---

## 2026-07-27 (later) — v3.5.1: Perplexity guidance sharpened against the product page

Leif surfaced Perplexity's Computer product page. Three refinements to the README section written in v3.5.0:

1. **A capability I had undersold.** Computer runs background and recurring tasks over long horizons with connectors and subagents. For a case taught across multiple semesters, standing monitors for new filings or coverage are a genuine fit — that belongs in the "what Perplexity is good at" list, not the limitations.
2. **The name is a trap, and saying so is the teaching moment.** Perplexity markets Computer as an assistant that "uses your computer." Its own help documentation says each task runs in an isolated container with a dedicated filesystem, separate from the user's machine. A reasonable reading of the product name yields the wrong operational answer. The README now names this explicitly as a live demonstration of the kit's own rule: check claims against primary sources rather than inferring from how something is described.
3. **Plan availability is not what I assumed.** The product page lists Pro and Max; Enterprise inclusion is not stated there. Since the guidance is aimed at faculty with campus licenses, the README now says to confirm coverage with whoever administers the license rather than assuming.

**Correction, same day**: Leif's read of the first draft — "not right, too wordy, and very negative." Accurate. 704 words for a tool note, framed around what Perplexity cannot do, with a moralizing aside about the product name being a "trap." Rewritten to ~260 words leading with genuine strengths (topic scouting, source hunting, Computer's recurring tasks for keeping a corpus current, Projects for student sharing) and stating the handoff to an agentic tool once, plainly, instead of as accumulated warnings. Lesson: a limitation worth one sentence does not become more useful at five, and framing a capable tool by its boundaries misrepresents it to the reader who needs to decide whether to use it.

**Process note**: this was cut with `/release-kit` and the scripts — `bump-version.sh 3.5.1`, `lint.sh`, `release-preflight.sh`. Second dogfooding, and the first patch release. The preflight's tag check correctly flagged that v3.5.1 did not yet exist before tagging.

---

## 2026-07-27 (later) — v3.5.2: placeholder hygiene + maintainer-file note

Two small corrections, both from Leif reviewing the published repo.

**Placeholders should not name real companies.** The README's repo-naming example and `/setup-case`'s company-naming example both used a real pharmaceutical firm — a leftover from early testing. A professor skimming the quick start could reasonably read that as a suggested subject. Now `CompanyXYZ`. Deliberately *not* changed: the same company's name in PROJECT_CONTEXT testing history, the `assess-bias` provenance note, and `defect-set.yaml` — those are factual records of real test runs, and scrubbing them would erase the evidence trail the kit exists to preserve. Placeholders are examples; provenance is fact.

**Maintainer files travel with the template.** Reviewing the published tree surfaced that "Use this template" hands every case author the kit's own release machinery — `scripts/`, `evals/`, `RELEASING.md`, `.gitignore-private`, and two maintainer skills. Harmless but confusing: release tooling for a kit they are not maintaining, sitting beside the files they need. Added a one-line README note that it can all be deleted. Considered and rejected: `.gitattributes export-ignore` (affects `git archive`, not template instantiation) and removing the files (a forker who wants to maintain their own variant needs them).

**Placeholder names swept (per Leif).** The flagged `case-config.yaml` example — "Teresa Carlson Waldron," with the equally invented title "Chief Availability Officer" — turned out to be one of ten. A grep across template contexts found real companies and real executives used as illustrations throughout: a real Tesla VP in the config header block, "JPMorgan Chase & Co." in inline comments, "Waldron noted that…" as the indirect-speech example in AGENTS.md, verify-quotes, and QA_WORKFLOW, and "McKinsey_Waldron_Interview.pdf" as a filename example in SOURCE_ACQUISITION. All now use unmistakable placeholders (CompanyXYZ, Jane Doe, Doe).

The distinction applied throughout: **placeholders must be obviously fictional; provenance must stay factual.** Real names in the testing history, `assess-bias` motivation note, `defect-set.yaml`, `evals/`, and `examples/` were left untouched — those record real runs against real sources, and genericizing them would destroy the evidence trail. A kit that teaches attribution discipline cannot put a fabricated composite of two real executives in front of users as an example, and equally cannot scrub the record of what it actually tested.

---

## 2026-07-27 (later) — v3.5.3: placeholder sweep completed, and a divergence caught by preflight

**The fix**: v3.5.2 genericized the two company-name examples Leif flagged. A grep across template contexts found eight more instances using real executives or names alluding to them — a real Tesla VP in the `case-config.yaml` header block, "Waldron noted that…" as the indirect-speech example in three files, "McKinsey_Waldron_Interview.pdf" as a filename example, and the composite "Teresa Carlson Waldron" with the invented title "Chief Availability Officer." All now `CompanyXYZ` / `Jane Doe` / `Doe`.

The rule applied throughout: **placeholders must be obviously fictional; provenance must stay factual.** Real names in testing history, `assess-bias` motivation, `defect-set.yaml`, `evals/`, and `examples/` were left alone — those record real runs against real sources.

**The process failure worth recording.** I amended the v3.5.2 commit to fold in the extra sweep — but Leif had already pushed v3.5.2 to both remotes. The amend produced a divergent commit carrying the same version number as one already published. `release-preflight.sh` caught it: *"public/main has 1 commit(s) you don't — fetch and merge first."* Check 8 exists precisely for this and did its job on a mistake I made, not a hypothetical one.

Resolution: reset to the published commit, restore the `v3.5.2` tag to it, and ship the extra work as **v3.5.3** on top. No published history rewritten. **Rule for the future, now in `/release-kit`'s spirit: never amend a commit that has been pushed — cut a patch release instead.** Amending is cheap right up until it isn't, and "has this been pushed?" is a question worth asking before every `--amend`.

---

## 2026-07-27 (later) — preflight check 10: published tags are immutable

**Trigger**: the v3.5.3 push was rejected on the `v3.5.2` tag ref — after the dev push had already landed the commits. Cause: when undoing the earlier amend I recreated the local `v3.5.2` tag, producing a new tag *object* (annotated tags carry their own identity) even though it pointed at the same commit. Git will not silently replace a remote tag, so it rejected that one ref and, because the two pushes were chained with `&&`, the public push never ran.

**Fix applied**: adopted the published tag (`git tag -d v3.5.2 && git fetch public --tags`). No force-push; nothing rewritten on a remote.

**Encoded so it cannot recur**:
1. `scripts/release-preflight.sh` **check 10** — compares every local tag against both remotes' tag objects and fails with the exact remedy. Tested by sabotage: recreated a published tag, confirmed the check fires and names the drift, confirmed it clears on restore.
2. `/release-kit` gains a non-negotiable rule section at the top: never amend a pushed commit, never recreate a pushed tag, ask "has this been pushed?" before either — and push targets with `;` rather than `&&`.
3. `RELEASING.md` documents the same, including the deliberate path if a tag genuinely must move (`git push --delete`, so the change is visible rather than silently overwritten).

**Observation worth keeping**: check 8, written the previous day for a hypothetical divergence, caught a real one within a day. The value of a preflight is not that it validates the happy path — it is that it fires on the mistake you were about to make while confident you weren't making one.

---

## 2026-07-27 — Project reflection at v3.5.4

Stocktake rather than a change entry. Eight releases and 21 commits since v3.1.0: MIT relicense, AGENTS.md cross-harness structure, source-integrity release, coaching and scouting skills, examples folder, maintainer tooling, and four patch releases of hygiene.

**Where the kit genuinely stands**: 20 skills, 4 tested scripts, a 10-check release preflight, a frozen JPM fixture with 16 seeded defects and recorded probe baselines, a blessed golden package, and 38 recorded lessons. Quality is now measured rather than asserted — the strongest claim available is that the kit's own verification blocked publication of its own output, twice, on defects a careful human review had missed.

**Where it does not stand**: no external adopter. Three stars, one fork, zero professors outside this project have authored a case with it. Every metric collected is internal. The v4.0 front-end generators — personas, concept maps, decision games, the "one case, many front-ends" thesis that motivated the whole effort — remain unbuilt. The `learning-context.yaml` written to drive them has never been read by anything.

**Honest note on this session's back half**: four patch releases in a day, all correct, none advancing adoption. Release hygiene is legible and satisfying in a way that outreach is not, and that asymmetry pulled effort away from the stated Fall-semester goal. Recording it here because the pattern will recur.

**Deferred and still deferred**: n=2 variance run; corpus v2 for teaching realism (v1 stays frozen as the fixture); SKILL.md directory migration; the three grading rubrics; verification-literacy guide; carrying the quoting rules into `write-document` so the author follows them at drafting time rather than verification catching them after.

---

## 2026-07-27 — v3.6.0: the workflow map

**Why**: adoption work, not polish. A professor deciding whether to invest a weekend was being asked to assemble the mental model from six scrolling README sections. The map answers "what will I actually be doing?" in one screen.

**Built as Mermaid, deliberately.** GitHub renders it natively, so no image pipeline; it stays diffable and versionable like everything else in the kit; and any AI tool can read and update it when a skill is renamed. An SVG would look marginally better and rot silently the first time the workflow changed. The SVG version exists too, at `docs/workflow-map.svg`, for slides and handouts — with a note in `docs/README.md` that the Mermaid is authoritative and this one needs syncing.

**Placed near the top**, immediately after the examples link and before "Built for Verification" — per Leif, so a reader knows a map exists before they start scrolling. Reading order is now: what it produces → what you'll be doing → why you can trust it → how to start.

**Three things the diagram makes visible that the prose buried**: the two gates carry the whole design (assess blocks writing, verify blocks publishing); the three loops are expected behavior rather than failure, which matters enormously for a first-time user hitting a YELLOW gate; and the destination is a verified body, not four files.

---

## 2026-07-28 — v3.7.0: the chat path had silently fallen four releases behind

**Found by**: Leif asking where `STARTER_PROMPT.md` fits in the new workflow map. It didn't — and checking why surfaced the larger problem.

**The finding**: `STARTER_PROMPT.md` had zero occurrences of scouting, coaching, source independence, processing status, verification debt, quote verdicts, or the go/no-go gate. Its last substantive edit predates v3.2. Every methodology improvement from the last four releases — the ones that came out of real failures on real material — reached the agentic paths and never reached the chat path.

**Why that matters more than it first appears**: the chat path serves users who can't run slash commands, don't have Claude Code, and are least equipped to notice a missing guardrail. The kit's protections were weakest exactly where users depend on them most. Skills are visible artifacts that get updated when the workflow changes; a prose prompt is invisible infrastructure that silently rots.

**Fixed**: `STARTER_PROMPT.md` now carries the current methodology conversationally — Step 0 scouting with the fatal-if-absent criteria, three separate source questions (tier/independence/processing) with the reminder that they're independent of each other, a Step 2b coaching loop including the honest helped/neutral/hurt judgment, voice-based perspective counting, verification-debt tracking during drafting, the full quoting rules, the five-verdict scale, and a pre-share checklist. Grew from ~1,000 to ~1,830 words.

**Also**: the workflow map was silently agentic-only — eight slash commands an Option C user cannot run. Added a note under it pointing to the starter prompt, and a header in the starter prompt pointing back at the map.

**Standing risk worth a future check**: nothing enforces parity between the skills and the starter prompt. A preflight check comparing key methodology terms across both would catch the next drift. Not built — noting it rather than reflexively adding an eleventh check.

---

## 2026-07-28 — v3.8.0: fixing release automation that had been silently absent

**Found by**: Leif noticing the GitHub Releases sidebar still showed v3.5.0 while tags ran to v3.7.0.

**Root cause**: `release.yml` triggered on `TEMPLATE_VERSION` changes, then checked whether `v{version}` already existed and skipped if so. That design assumes you push `main` alone and let the action create the tag. We push `main --tags` together, so the tag always arrived with the commit, the check always found it, and the workflow always stood down. Six releases, no output, no signal — a skipped workflow and a workflow with nothing to do look identical.

**My first recommendation was wrong, and worth recording why.** I proposed removing the automation and making release creation manual, reasoning "explicit beats clever." Leif pushed back and asked whether that was really best. It wasn't. The failure mode here was *a forgotten step* — six releases went uncreated because nobody remembered. Responding to a forgotten-step failure by adding a manual step repeats the error, and contradicts the lesson behind the version-bumper and the preflight: memory is the unreliable component. I generalized from "clever automation no-opped" to "less automation," when the actual lesson was "*this* automation had the wrong trigger."

**Fix**: trigger on `push: tags: ['v*']`. Pushing the tag *is* publishing the release. The tag-exists check is deleted — the tag's presence is now the precondition rather than a conflict. The workflow never creates tags, so tags stay locally authored: one authority, and preflight check 10 keeps working. Rejected alternative: pushing `main` first and letting the action create the tag would split tag authority between local git and CI, which is exactly what produced today's earlier tag-object mismatch.

**Deliberate choice**: the workflow **fails** on a missing CHANGELOG section rather than emitting boilerplate. An empty release passes visual inspection and communicates nothing; a red Actions run is visible and fixable. Preflight check 4 already blocks this before tagging, so this is defense in depth.

**Testing**: YAML validated after a real bug — a `---` inside a heredoc was parsed as a YAML document separator, splitting the file; replaced with `printf` lines. Then replayed the workflow's shell steps locally against v3.7.0, v3.6.0, and v3.2.0 (correct extraction, no next-heading bleed) and against a non-existent version (exits 1 as designed).

**Live test**: pushing the v3.8.0 tag is itself the first real run of the new workflow. If the rewrite is wrong we get a red X rather than silence — which is the whole improvement.

**Still manual, once**: the six already-pushed tags (v3.5.1 through v3.7.0) need releases created by hand. Re-pushing those tags to force a trigger would violate the published-refs-are-immutable rule.

---

## 2026-07-31 — v3.8.1: privacy guard + field-test intake

**Context**: v3.8.0 shipped to both remotes. Leif is now testing the kit against
independent case examples in a working area outside this repository, with the
intent of using what that testing shows to design and prioritize the next version.

**Changes**:

1. `scripts/release-preflight.sh` — new check 11 scans tracked files for
   machine-specific paths (`/Users/...`, `/home/...`, `C:\Users\`, application-support
   and session directories) and fails the release if any are found. The script
   excludes itself, since it necessarily contains the patterns it hunts. A full scan
   of the current tree came back clean; a planted path was correctly caught and the
   check returned to green once removed.
2. Check 10 (published refs immutable) now warns when a remote cannot be listed
   rather than skipping it silently. Found by accident: in an unauthenticated shell
   the private remote was unreadable, the loop `continue`d over it, and the check
   reported green having compared nothing. Same shape as the release.yml bug fixed
   one version earlier — a guard that cannot see should say so, not pass.
3. `RELEASING.md` — preflight is now described as 11 checks.
4. `PROJECT_CONTEXT.md` — status updated to reflect the field-testing phase.

**Why check 11 now**: the kit's whole posture is that it is safe to hand to other
professors and to students. A public template carrying a maintainer's home directory
structure is a small leak with an outsized signal — it says the repo was published
without being read. Check 5 already blocks the unrecoverable mistake (copyrighted
corpus). Check 11 blocks the merely embarrassing one, and costs nothing per release.

**Field-test intake method** (design note kept outside this repo): inventory before
interpreting; classify every observation as DEFECT / GAP / FRICTION / MISFIT / USER;
weight by frequency x severity with blast radius as tiebreak; convert defects into
permanent seeded tests before fixing them; size the release honestly, including the
option of no release. The method was written **before** the test material was read,
so it cannot be bent to fit a conclusion.

**Not done**: the testing material had not been made available to the session when
this was written, so no findings are recorded here yet.

---

## 2026-08-26 — v3.9.0: making the gates compute

**Context**: the first field test of the kit by someone other than the author is in.
Two complete four-document packages were built against v3.8.0 on the Claude Code
path, one from a single promotional seed and one from a subject who self-publishes
prolifically. Both finished; both were graded honestly by their operator. The intake
method was fixed in advance so the findings could not be bent toward the existing
roadmap — and they were not. None of the nine standing backlog items names what the
test found.

**What the test found**, in behavior terms:

1. **The verification pipeline reports verdicts it has not earned.** `/verify-all`
   returned PASS on quotes for a document set in which a later span-by-span file trace
   found five substantive quote defects. The quote check had reasoned at the level of
   source categories — "essay quotations are quotable as written", "ASR quotations use
   the bracket convention" — and never enumerated individual quoted spans. Notably,
   `/verify-quotes` already *specifies* span-level tracing: it requires a source file
   and line number for a VERIFIED verdict, and it carries a five-way MODIFIED taxonomy
   that names four of the five defects found. The skill was not deficient. It was
   reported as passed without being performed at the granularity it specifies, and
   nothing in the output could distinguish the two.

2. **The assessment gate cannot tell a thin base from a one-sided one.** A base of one
   promotional source scored RED and blocked, correctly. A base of 33 sources that was
   ~82% the subject's own material scored YELLOW and proceeded — because the overall
   gate averages four dimensions, two of which reward volume, and because independence
   enters the gate only as a floor of one source rather than as a proportion. The
   report named the imbalance accurately in prose and then let it through.

3. **Delegated research breaks the chain of custody for quotations.** Sources read
   live in a browser or gathered by subagents arrive as summarizing dossiers. The
   verbatim wording never reaches a file, so quotations drawn from it trace to
   nothing. `/add-sources` does not prompt for the raw capture.

4. **`*.log` is gitignored, so gate logs are discarded by default.** The assessment
   and verification logs are the evidence that the gates ran. One field case kept them
   only because its operator forced the add; the other kept none.

**Why these are one finding as much as four**: items 1, 2 and 4 are all cases of a
check that reports a verdict it did not earn — the same shape as the release workflow
that silently no-opped for six versions and the preflight check that passed because it
could not reach a remote. Both of those were found and fixed in the release tooling.
The same class was never swept for in the verification pipeline, which is the part
users actually depend on. A fifth instance was found in passing while running the
release script on a different machine: `scripts/lint.sh` uses a bash 4+ builtin, so
under macOS's bash 3.2 it aborts, and preflight reports "lint violations" — a
substantive finding it never made. The markdown was clean.

**Order of work**, per the standing rule that bugs are test cases wearing disguises:
the three defects were written into the seeded defect set as D17–D19 (version 3)
**before** any fix was drafted. This is the first defect set drawn from cases the
author did not choose, against sources the author did not curate, which makes it the
most externally valid one in the project.

**Sizing**: v3.9.0. Every fix makes the existing architecture do what it already
says — enumerate the spans, compute the ratio, keep the logs. No new stage, no new
document, no change to the workflow map. The counter-argument is recorded rather than
buried: if the two gates *are* the architecture, then "they narrate rather than gate"
is a structural finding and v4.0 would be defensible. The v4.0 front-end generators
remain parked; by the intake method's own instruction they lose to anything that puts
a wrong quote in a classroom.

**Not covered by this test, and worth saying plainly**: both runs used Claude Code, so
the Copilot and chat paths still have no field evidence at all — and the chat path
serves the users least equipped to notice a missing guardrail. Neither case reached a
classroom, so teaching readiness remains unmeasured. Two cases, one operator, one
week: still n=1 in every dimension that matters for variance.

## 2026-08-26 — v3.9.1: withdrawing a claim v3.9.0 could not support

**Context**: v3.9.0 shipped two quote-related fixes under one diagnosis — a rewrite of
`/verify-quotes` and a unit-count requirement in `/verify-all` — and the changelog
credited both. Neither had been tested for compliance; the release's own validation had
executed the procedure as a script, which measures whether the procedure works, not
whether an agent following the prose performs it.

**What was run**: four blind agent runs across two probes. Each pair received identical
corrupted documents and an identical source corpus, with the skill files the only
difference between arms. Five defects were planted, one of them deliberately of a class
named by neither version's text, so that a clean sweep could not be the skill listing
being read back.

**Probe 1 — `/verify-quotes` standalone.** Both arms 5/5, both enumerated spans, both
returned FAIL, both caught the unprimed defect. On the one unplanted defect either arm
found — an assent converted to assertion — the **older** text did better. The prose
rewrite has no measured effect.

**Probe 2 — `/verify-all`, the condition the field failure occurred in.** The arms
separate. The v3.8.0 pipeline adjudicated 96 "distinct quotations" and missed the
planted framing-inside-the-marks defect; the v3.9.0 pipeline enumerated 355 spans,
verdicted all 355, and caught it. Offline, the v3.8.0 pipeline logged the link check as
six warnings and did not block; the v3.9.0 pipeline reported `0 of 4 URLs requested`,
declared it NOT RUN, and blocked. 4/5 versus 5/5.

**Conclusion**: the orchestration change carries the release. The skill rewrite does
not, and v3.9.1 withdraws that claim while keeping the text, which documents the
failure classes better than what it replaced.

**What is still wrong**: a prediction recorded before probe 2 — that the v3.8.0
pipeline would report quotes PASS, reproducing the field failure — was **falsified**.
It reported a quote failure and blocked distribution. Three hypotheses tested, none
reproduces the original incident. The remaining untested candidates are a long
preceding authoring session, a verifier checking documents it had itself authored, and
a real case with no planted defects to find. **The kit is better and the incident is
unexplained**, and this entry exists so the second half does not get quietly dropped.

## 2026-08-26 — v3.10.0: three gaps in the instructions, not the logic

**Context**: v3.9.x fixed what the field test found and then tested those fixes,
correcting one claim that did not survive. What remained were three gaps that no skill
logic could close because they were absent from the guidance itself.

**1. Nobody was told who should verify.** `AGENTS.md` had no rule about it. Both field
cases and the run that produced the unexplained pass authored and verified in one
session. Meanwhile the project's one independent verification run had recorded *"fresh
eyes; did not author the documents"* in its own log and had found a spliced quote the
authoring session missed. A condition that was met, noted, and never required. The new
*Who Verifies* section states the preference, requires disclosure when author and
verifier are the same, and demotes a clean self-review to a draft check. `/verify-all`
now carries a `Verifier:` field that must say `SAME SESSION AS AUTHOR` when that is
true.

**2. The most recurrent bug in the project had never been written down.** Six instances
of a check reporting a verdict it had not earned, six local fixes, zero statements of
the principle in the file the next author reads. Now a section of its own, with all six
instances as evidence and the question that would have caught every one of them.

**3. The quoting rules were in the wrong file.** Canonical, good, and invisible to the
writer, whose only guidance was to attach a speaker and a date. The writer therefore
produced what the verifier was built to catch — unmarked smoothing counted in the dozens
on three separate occasions over four months. `write-document.md` gains a drafting gate
that references the canonical rules rather than copying them, and adds the drafting-time
practices: paste and trim rather than retype, never quote from a dossier, keep your
framing outside the marks.

**Propagated to all three tool paths**, since the kit's premise is that they read one
canonical file: the Copilot pointer's summary was stale, and the chat path — least
technical users, least able to spot a missing guardrail — got the independence rule in
plain language with a concrete instruction to start a new chat for verification.

**Still open, and stated so it is not lost**: the incident that prompted v3.9.0 is not
explained. The independence rule is the leading hypothesis and shipping it is not the
same as confirming it.

## 2026-08-26 — v4.0.0: adopting a colleague's onboarding, and lightening the ask

**Context**: a teaching colleague forked v3.1.2, rebuilt the onboarding around Claude
Cowork for non-technical students, segmented the instructions into a single "happy
path", and shortened the writing load for MBA students holding full-time jobs. He
reported that he changed no skill logic — only packaging. His fork was not available, so
this release was designed from his stated principles rather than from a diff.

**What changed**: Cowork becomes the recommended path with a full inline quickstart and
the other three tools demoted to documented alternates; the slash-command fallback is
restated as the normal case rather than a degradation; and `documents.required` in
`case-config.yaml` now drives which documents `/write-document`, `/verify-all` and
`/verify-cross-document` expect, with word-count defaults sized for a working
professional.

**On the Teaching Note**: it stays. Removing it from `documents.required` is how a
course says "the instructor writes this", and the skill that produces it is untouched.
Dropping the artifact would have orphaned `/verify-cross-document`, whose main job is
checking Teaching Note against Main Case.

**Two errors caught in the third-hand summary of the colleague's analysis**, both
checked against this repository before designing anything: verification debt is gated at
"zero *or acknowledged*", not blocked at zero; and the v3.2.0 MIT relicensing left
produced cases defaulting to CC BY-NC, so the educational-content protection he was
worried about losing was never lost. Neither changed the design. Both would have been
carried forward as fact if the summary had been trusted.

**The uncomfortable part, recorded rather than smoothed over**: the Cowork path has
never been run end-to-end. This kit's own field evidence says the least technical path
serves the users least equipped to notice a missing guardrail, and this release puts an
untested path in front of exactly those people. The README carries an explicit
"not yet field-tested" callout asking for issues. **That is honest labelling, not
evidence.** One full run through Cowork on the fixture is the first thing the next
release should do — before anything else on the backlog.

## 2026-08-27 — v4.1.0: correcting the kit's claims about itself

**Context**: the README's verification section promised more than any workflow can
deliver — "you can defend every sentence in your case", "you always know exactly what is
sourced and what is not", "traces every quote to a dated source". The third is
contradicted by this project's own `evals/test-log.md`, which records `/verify-all`
reporting quotes as passing on a package that a later line-by-line trace showed carried
five genuine quote defects.

**What changed**: the section is now "Built for Verification — and for Your Judgment".
It says the kit surfaces issues for the author to weigh rather than certifying output,
describes each mechanism with its actual limits, and cites the kit's own verification
failure by name. The organizing metaphor is stated: the author is a manager delegating
to a capable assistant who is occasionally, confidently wrong, and remains accountable
for everything published under their name.

**Where it was embedded**: `AGENTS.md` gains "Who Is Responsible" — never imply work is
verified because a check passed, hand judgment calls back rather than settling them in
whichever direction lets work proceed, volunteer doubts at the time, expect to be
overruled by someone who knows their field. `VERIFICATION_PLEDGE.md` now claims work
done rather than outcomes achieved, and closes by naming what it does not claim.
`STARTER_PROMPT.md` and the Copilot pointer carry the same framing, so no tool path
receives a weaker version of it.

**Teaching purpose stated as a purpose**: the kit exists partly so authors and students
see directly where current AI helps and where it fails. Agents are now told to name
their own failures as material worth recording rather than smoothing over.

**No logic changed.** Every check does what it did in v4.0.0. What changed is what the
kit claims those checks mean — which had drifted from what the evidence supports, in a
repository whose entire subject is that kind of drift.

## 2026-08-27 — v4.2.0: half the length, and a recommendation instead of an assumption

**Context**: a teaching colleague's central observation about the kit was that its
documents are too long for the people who actually have to write and review them. His
targets run about half of what the kit specified.

**What changed**: the Main Case target drops to 2,000-3,000 words — roughly 8-12 pages at
250 words per page — with the other three documents scaled to match, putting a complete
package near 7,500 words rather than 15,000. `/setup-case` now states that recommendation
in plain language and asks only whether the author wants it longer or shorter. It does
not present a menu or ask for a number: on a first interaction, asking someone to specify
a length is asking them to have an opinion they have no basis for yet.

**A defect found while doing it**: v4.0.0 lightened the word counts in `case-config.yaml`
and left the same numbers heavy in three other places — the README's package table, two
files under `templates/`, and most damagingly the config template inside
`setup-case.md`, which meant every newly generated project silently got the old heavy
values back. The documented default and the generated default were different numbers and
the generator won. Fixed by removing the duplicates rather than syncing them: the
templates now reference `documents.target_word_counts` instead of restating it.

## 2026-08-27 — v4.2.1: what a no-slash-command run found

**Context**: v4.0.0 made Cowork the recommended path without testing it. Actual Cowork
is not reachable from this environment, so the nearest available test was run instead: an
agent given the project folder, `AGENTS.md`, and no slash-command surface, handed the
README's own opening phrase by a notional non-technical professor.

**The v4.0.0 premise holds.** The agent read `AGENTS.md`, located every procedure through
the skills table, ran eight of them, and produced a complete four-document package with
no slash-commands. It quoted the rule that the skill file is the specification and the
command only a shortcut. That was the thing most at risk and it works.

**Three defects, none subtle, all read past repeatedly by people with a terminal open:**
`documents.required` was mandated in bold with no handling for the many projects that
predate it; the Cowork path promised no terminal while the README's own Step 2 opens with
`git clone`; and word-count targets were stated but never checked, with the agent
overshooting every one of them by 23-55%.

**The length finding matters most**, arriving one release after the targets were halved.
Cutting a number in a config file does nothing if drafts land 41% over it. `write-document`
now budgets the target across sections before writing, measures when finished, and cuts
before showing the author rather than apologising afterwards.

**An observation worth recording separately**: the agent, following v3.10.0's
independence rule, commissioned a verifier that had not written the documents. That
verifier found 20 quote defects. The agent fixed them and reported all fixed — a second
independent pass found **eight were still wrong and the correction round had introduced
eleven new ones**. A self-check reported success it had not achieved, which is the shape
of the still-unexplained field incident. Not a controlled test of that question, but the
first direct sighting of the mechanism.

## 2026-08-27 — v4.3.0: freeze the tree, re-verify the fixes

**Context**: the no-slash-command run that produced v4.2.1 did something unplanned — the
authoring agent, following v3.10.0's independence rule, commissioned a verifier that had
not written the documents, fixed its 25 findings, and then commissioned a second pass to
check the corrections. That second pass is where this release comes from.

**What it found**: the correction round introduced **11 new defects** while fixing 25. The
author's own summary said *"Fixed. All 15 converted"* when **eight were still live**. And
the first verification log made four statements that were false about the files on disk —
not when written, but by the time anyone read them, because the documents were edited
fourteen minutes after the log froze its state. Timeline confirmed independently: log at
10:51, documents last modified 11:05, second pass at 11:10.

**Two structural gaps, now closed.** `/verify-all` gains a freeze step: record every
document's word count before checking, tell the author not to edit, do not repair while
verifying, re-read the counts at the end, and declare the report void if anything moved.
And the workflow no longer ends at "fix the findings" — corrections get their own pass,
run by someone who did not make them, checking both that each fix landed and that the
round introduced nothing new.

**The sharpest line the second verifier wrote**, now the honest status the kit teaches:
*no state of this package has yet been read end to end by anyone who did not also change
it.* That was true, it went unnoticed, and nothing in the workflow would have surfaced it.

**Relevance to the still-unexplained field incident**: this is the second sighting of a
self-report claiming completion it had not achieved, and the first inside a correction
round rather than an initial check. Still not a controlled test of that question. But the
mechanism is no longer hypothetical — it has now been observed twice, in runs that were
not looking for it.

## 2026-08-27 — v4.3.1: what happened when we ran what we shipped

**Context**: four of the last five releases shipped instructions whose effect on
behaviour had never been observed. One full authoring pass against the fixture tested
four claims at once, with the agent told nothing about what was being measured.

**Three claims confirmed.** The freeze protocol recorded a frozen-tree table, re-read it
at the end, and correctly flagged four checks stale against a package that had grown from
7,859 to 9,503 words during corrections — the exact failure that produced v4.3.0. The
post-correction pass ran, by an agent that had neither written the documents nor made the
fixes, and found that the correction round had rewritten three integrity claims *wrongly*
and that the first independent trace had mis-filed a span. The independence rule is in
live use: seven checks labelled SAME SESSION AS AUTHOR, two independent passes
commissioned unprompted.

**One partial.** Word budgeting cut package overshoot from +41% to +27%, and the Main Case
landed at +9% — inside tolerance for the first time. Three of four documents still miss.

**The most useful finding is that the worst miss was correct behaviour.** The agent hit
the Additional Sources target exactly as instructed and broke traceability for four
quotations the Main Case later used. It refused to do it again. The rule said "cut the
weakest material", which is right for prose and wrong for an evidence file, where the
weakest material is still evidence. The instruction was defective and obedience exposed it.

**Five defects fixed**, four of which maintainers had read past repeatedly: an
unconditional verification claim sitting in boilerplate the kit hands authors to paste —
one release after the README was rewritten to remove exactly that sentence; a hardcoded
"v3.0" fourteen releases stale in the same pasted text; `examples/` advertising a length
the kit no longer targets; a zero-debt publication bar unreachable without a network; and
the evidence-file rule above.

**The pattern worth keeping**: reading your own instructions does not find these, because
you read what you meant. Running them does, because an agent has only what you wrote.

**Kept**: the case package at `eval-runs/authoring-2026-08-27/`, outside any repository —
four documents, four exports, nine logs, a full defect history, and an honest status of
not fit to publish.
