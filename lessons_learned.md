# Lessons Learned

*Append-only. One section per version. What we learned building, testing, and using each version — distinct from `log.md` (what changed) and `evals/test-log.md` (how it scored). The goal: no lesson gets learned twice.*

---

## v3.2.0 — 2026-07-07

**1. The differentiator was buried.** The verification machinery (debt tracking, tier gates, seven checks) was the kit's strongest and most novel feature — external research found no comparable published framework — yet it appeared only as rows in a skills table. A capable evaluator nearly missed it. Fixed by leading the README with it. Lesson: periodically re-read the repo as a stranger; the pitch drifts from the substance.

**2. License information lives in more places than LICENSE.** Badge, footer, config default, skill template block, and owner intent were five separately-drifting copies. Relicensing required a repo-wide grep. Lesson: minimize the places metadata is restated, and grep before declaring done.

**3. Instruction-file duplication was already drifting.** CLAUDE.md and copilot-instructions.md were hand-maintained near-copies with small divergences. The AGENTS.md-canonical + thin-adapters structure removes the failure mode instead of patching it. Lesson: one source of truth, adapters point at it.

**4. Verify capability claims against first-party docs — even our own.** During the evaluation, a secondary source claimed Claude Code natively reads AGENTS.md; official docs said otherwise (import/symlink required). And an early plan draft said Gemini CLI reads AGENTS.md "natively" when it needs a settings entry. Both caught by checking primary sources before shipping. Lesson: the kit's trace-to-primary rule applies to docs about the kit.

**5. Judgment-dependent output is testable if you convert judgment to detection.** The breakthrough framing for regression-testing the kit: don't ask "is the case good?" (hard), ask "does verification catch the ten defects we planted?" (measurable recall). Pairwise comparison with position-swap handles the rest better than absolute scoring. Encoded in evals/EVALS.md.

**6. Every real-world miss should become a permanent test.** The seeded-defect set should grow from actual failures (the Moderna test exposed financial errors and late-discovered bias — those belong in defect-set v1). Lesson: bugs are test cases wearing disguises.

**7. (Baseline run, 2026-07-08) The seeded-defect method works better than hoped.** 10/10 planted defects caught with zero false alarms on the first try — including the offline URL defect (caught by cross-checking the bibliography against the source file's own footer, a detection path we didn't anticipate). Judgment-to-detection conversion is validated as the kit's regression backbone.

**8. (Baseline run) The writer makes exactly the errors the verifier exists to catch.** The clean authoring run — following the kit's rules carefully — still produced a spliced composite quote, one altered quote, and a garbled attribution. The verification pass caught all of them and correctly blocked publication. Two implications: never skip verification even on "careful" runs, and the verdict scale needs a MODIFIED category (verbatim words, altered assembly) — the two real failure classes found are exactly the ones the current VERIFIED/LIKELY/DISPUTED/APOCRYPHAL scale can't name.

**9. (Baseline run) Naive deterministic checkers over-flag prose.** grounding_check.py v1 reported 54.8% quote grounding while full agent tracing showed ~97% — the regex counts rhetorical/hypothetical quoted text (Teaching Note cold-call prompts, scare quotes) as attributed quotes. Deterministic tools for prose need linguistic awareness (attribution patterns) or they become noise generators; until v2, the script is a lead-generator, not a gate.

**10. (Baseline run) The bias check measures the wrong denominator.** Outlet-origin counting scored the corpus 20% "company-generated," but ~80% of substantive claims are JPMorgan executives speaking through independent outlets. Bias assessment should count by claim-maker voice, not publication masthead. Queued for v3.3.

**11. (Baseline run) The judge's critique converged with the human plan.** The opus judge's top improvements (forcing event, quantitative exhibit, dissenting voice) independently match what the case-method literature says separates drafts from published cases — evidence the rubric dimensions are pointing at real quality, and a concrete authoring-skill improvement: `/write-document` should ask "what quantitative exhibit will students compute with?" during Main Case setup.

**12. Agentic maintenance sessions have their own friction.** `.claude/` was write-protected for file tools in this environment; shell was the workaround. Documenting environment quirks in log.md saves the next session the rediscovery.

**13. (Bookends, 2026-07-09) The pipeline's ends were where the leverage was.** Two conversations added a pre-stage and a post-stage input without touching the verified middle — evidence that the "verified body as hinge" architecture is sound: upstream work makes the body trustworthy, downstream work renders it, and neither perturbs the other.

**14. Scouting predictions are an eval signal, not just a convenience.** Because `/scout-case` scores on the same four dimensions `/assess-sources` uses later, predicted-vs-actual becomes measurable. A scout that systematically over-promises is a defect we can catch, not a vibe.

**15. Mass customization needed an input, not more generators.** The front-end plan was complete except for anything describing the classroom. `learning-context.yaml` is small, but without it "many front-ends" means "the same artifact generated repeatedly." The failure mode to watch: a generator that reads the context file and ignores it — hence the context-sensitivity eval probe.

**16. Two remotes beat a fork.** The instinct to protect a working repo was right; the fork was the wrong mechanism. One history with a private default remote and a public release remote gives the same safety without the eventual manual porting between drifting codebases.

**17. (Probes, 2026-07-27) The coach outperformed two prior expert passes on the same material.** A verification agent and an opus rubric judge had both gone over this case; the coach found everything they found and eight material issues they missed — vendor sponsorship of a "primary" source, an editor-processed transcript quoted as verbatim, a third contradictory headcount figure, and the discovery that the case's own title number was asserted by an interviewer and merely assented to. The lesson isn't that one agent is better; it's that **different diagnostic lenses catch different failures**. Verification asks "is this claim supported?"; coaching asks "what's missing and how confident is the foundation?" Both are needed.

**18. Source independence is a hole no existing check covers.** The Cisco sponsorship and McKinsey's undisclosed commercial interest in the material it was summarizing both passed every gate the kit has, because tiering measures *access* (do we have the full text?) and bias assessment measures *outlet*. Neither asks "who paid for this, and what do they sell?" The Source Registry needs an interests column.

**19. Scouting predicts well enough to be trusted.** MAE 0.5 with zero signed bias against a post-sourcing assessment, from web reconnaissance alone. More interesting: where scout and baseline disagreed on Reliability, the coach's independent analysis sided with the scout — the blind prediction may have been more accurate than the informed assessment it was scored against.

**20. A regression fixture and a teaching corpus are different artifacts.** Both probes flagged the JPM corpus as stale. That's a virtue for regression testing (a moving corpus makes version comparison meaningless) and a defect for classroom use. Don't let one requirement corrupt the other — freeze v1 forever as the fixture, build v2 if the case is to be taught.
