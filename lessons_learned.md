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

## v3.3.0 — 2026-07-27

**21. The bug was never where I assumed.** grounding_check's false-flag rate looked like a rhetorical-quoting problem; measuring it revealed a quote-parity bug that made the checker compare narrative prose against the corpus. I shipped an "attribution-aware" v2 that barely moved the number before measuring again and finding the real cause. Lesson: when a fix doesn't move the metric, the diagnosis is wrong — don't ship the second guess either, measure again.

**22. Straight quotes are structurally ambiguous and prose tooling must respect that.** You cannot tell an opening `"` from a closing one. Any tool pairing them positionally breaks on the first unpaired mark and fails silently for the rest of the document. Curly quotes are self-describing; straight quotes need content-based validation.

**23. The kit now demands more of the writer than the writer delivers.** v3.3's verification found ~40 unmarked smoothings in text the same system authored under the old rules. That's not hypocrisy, it's sequencing — but the fix belongs at drafting time, not verification time. A rule that only exists in the checker teaches the author nothing.

**24. A stricter standard makes old results look worse, and that's success.** Same documents: ~225 verified under v3.2.0, ~33 under v3.3.0. The temptation is to read that as a regression. It's the opposite — v3.2.0 was counting quotes as verified that no honest reviewer would accept, because it asked "does this string appear in the corpus?" instead of "can this source support a quotation at all?" Corollary: golden baselines are versioned artifacts. Don't retroactively re-bless; record which standard a baseline was blessed under.

## v3.5.0 — 2026-07-27

**25. The kit was preaching a discipline it did not practice.** Verification gates, provenance logs, and checklists for case writing; memory and goodwill for its own releases. Every manual release step failed at least once across three releases. Automating them was not efficiency work — it was consistency between what the project claims and how it operates.

**26. Test the failure path, not the happy path.** `release-preflight.sh` passing on a clean repo proves almost nothing. Staging a fake copyrighted file and confirming it refuses to proceed, and creating a commit after the tag to confirm it detects the drift — those tests are the reason to trust it. Both sabotage tests targeted errors that had actually occurred or nearly occurred.

**27. A script's own testing found a bug in the script.** The preflight's skill-existence check read README's generic "`/slash-commands`" as a skill name. Automation introduces its own defects; the answer is to test it like anything else, not to trust it because it is code.

**28. Research changed the guidance rather than confirming it.** The plausible assumption about Perplexity — agentic browser, therefore agentic workflow — is wrong in the way that matters. Comet cannot read local files at all, and the one surface that can is Mac-only with no documented git or shell. Faculty told "use your Perplexity license for this" would have hit a wall. Checking first-party documentation rather than reasoning from the product category is what the kit tells its users to do.

## v3.5.3 — 2026-07-27

**29. Published refs are immutable — and that includes tags.** Two mistakes in one release, both mine. I amended a commit that had already been pushed, producing a divergent commit carrying a published version number. Then, cleaning that up, I recreated the `v3.5.2` tag locally — which makes a *new tag object* even pointing at the same commit, so the next push was rejected part-way through, after other refs had landed. The intuition that "a tag is just a pointer" is wrong for annotated tags: they are objects with their own identity.

**30. The backstop caught it, which is the argument for backstops.** Preflight check 8 flagged the divergent commit before it could reach a remote. That check was written the day before for a hypothetical; it fired on a real error within twenty-four hours. Check 10 (local tags must match published tags) has now been added for the second half, and tested by sabotage — because a rule that lives only in a document is a rule that gets skipped when you're moving fast.

**31. Chain independent operations with `;`, not `&&`.** `git push origin … && git push public …` meant one rejected tag ref silently skipped the public push entirely. The two remotes are independent; failure on one says nothing about the other. Small syntax choice, real consequence.

**32. Ask "has this been pushed?" before every `--amend` and `git tag -f`.** Both errors trace to the same skipped question. Amending is cheap right up until the moment it isn't, and the moment is invisible unless you check.

---

## Project reflection — 2026-07-27

*Written at v3.5.4, after eight releases and twenty-one commits from v3.1.0. A stocktake rather than a version note.*

**33. The kit is now defensible in a way it was not three weeks ago — and that is the real change.** Before, its quality rested on the author's care. Now it rests on measurement: a frozen corpus, sixteen seeded defects, recorded probe results, a blessed baseline, and an append-only test log. When the coach found eight material issues in material that had already passed two expert review passes, that was not a lucky catch — it was a designed one. The kit can now answer "how do you know?" with something other than "I checked carefully."

**34. Nearly every improvement came from running the thing, not from thinking about it.** The independence column, the MODIFIED verdict, voice-based bias counting, the ASR quoting rule, the grounding-script parity bug, four preflight checks — all of them originated in a real run producing a real failure. The planning documents were useful for direction; almost none of the substance came from them. Build the smallest thing that can fail visibly, then run it.

**35. The scoreboard that matters has not moved.** Three stars. One fork. Zero external professors have authored a case with this. Every measurement above is internal, and the pilot evidence (~95% engagement) predates all of it. The kit got substantially better at a job nobody outside this project has yet asked it to do.

**36. Late in this session, effort drifted from the goal.** Four patch releases in one day — placeholder hygiene, a Perplexity rewrite, tag-immutability checks. Each was correct in isolation, and correctness is seductive: a failing lint check or a badly-worded paragraph presents itself as urgent in a way that "email three colleagues" never does. But the stated priority was adoption before Fall, and none of those four releases moves a professor closer to using the kit. The tell was the ratio: hours on release mechanics versus zero on getting it in front of a human.

**37. Rigor has a cost, and it should be spent where the risk is.** The maintainer tooling was worth building — the release process was genuinely failing, repeatedly. But a starter kit with a ten-check release preflight and no users has its investment inverted. The verification machinery earns its keep the moment a student publishes a case with a fabricated quote; the release preflight earns its keep at a scale this project may never reach.

**38. What would actually settle the open question.** One professor outside this project, taking the kit through `/scout-case` to a finished package, in their own subject area, with their own sources. That single run would test more than the entire eval suite does: whether the instructions are followable by someone who did not write them, whether the go/no-go gate feels helpful or obstructive, whether the output survives contact with a syllabus. Everything measured so far assumes a user who thinks like the author. Nothing has tested a user who does not.

**39. (v3.7.0) The least capable path rotted the fastest, and nobody was looking.** `STARTER_PROMPT.md` sat four releases behind: no scouting, no coaching, no source independence, no quote verdicts. Every improvement that came out of a real failure reached the agentic paths and stopped there. The asymmetry is structural — skills are visible files that get edited when the workflow changes; a prose prompt is invisible infrastructure. And it lands on exactly the wrong users: the ones who can't run slash commands are also the ones least able to notice a guardrail is missing.

**40. Cross-path parity needs a check, not good intentions.** Nothing today would catch this drift happening again. The fix is mechanical — compare methodology terms across the skills and the starter prompt — but worth resisting the reflex to add it immediately. The kit already has ten preflight checks and no external users; another check is cheaper to write than to justify.

**41. The best bug reports came from a reader, not a test.** The eval suite, ten preflight checks, and sixteen seeded defects all passed while the chat path silently degraded. Leif noticing that a file wasn't referenced in a diagram found something none of the automation could, because automation checks what you thought to check. Someone reading with fresh eyes remains the highest-yield defect finder available.

**42. (v3.8.0) A workflow that skips is indistinguishable from a workflow with nothing to do.** `release.yml` no-opped for six consecutive releases and produced no signal — green check, no output. Silent success is the worst failure mode in automation, worse than a crash, because nothing prompts investigation. Anything that can decide to do nothing should say so, or be structured so it cannot make that decision.

**43. Match the fix to the failure mode, not to a general principle.** My first proposal was to delete the automation and make release creation manual, on the reasoning that explicit beats clever. Leif asked whether that was really best, and it wasn't: the failure was *a forgotten step*, and the response to a forgotten step is never "add a manual step." I had generalized from "this clever thing broke" to "less cleverness," when the actual lesson was narrower — this automation had the wrong trigger. Reaching for a maxim is a substitute for diagnosing.

**44. Make the trigger the thing you cannot skip.** The fix works because pushing a tag and publishing a release became the same action. You can forget a step that sits beside the work; you cannot forget one that *is* the work. Prefer designs where the desired outcome is a side effect of something you were going to do anyway.

**45. Fail loudly over degrading gracefully — when the degraded output looks fine.** The old workflow's fallback was "see CHANGELOG for details," which would have produced releases that pass visual inspection and tell a reader nothing. The rewrite errors instead. Graceful degradation is right when partial output helps; it is wrong when the partial output is indistinguishable from real output to everyone except a careful reader.

**46. "Are you sure?" is worth answering seriously.** Both of today's course corrections — the over-negative Perplexity section and this one — came from Leif questioning an answer rather than accepting it. Neither would have been caught by any check in the repo. The reviewer who asks why remains more valuable than the checks, and the right response to being asked is to re-derive the answer rather than restate it.

## v3.8.1 — 2026-07-31

**47. Every evaluation of this kit so far has been self-administered.** I wrote the
skills, then the evals, then ran and graded them. The seeded-defect method exists
specifically to escape that circularity and it works — but it only tests what I
thought to plant. Field testing by someone using the kit to do the actual job, on
cases I did not choose and sources I did not curate, is a different and better class
of evidence. The corresponding risk is reading it as confirmation of the roadmap I
already wrote; if the field test happens to endorse every existing priority, the
right response is suspicion of my reading rather than satisfaction.

**48. The kit was fitted to one case, and that boundary is invisible from inside.**
Everything here was built and tuned against a large public company with a named
executive protagonist, abundant press coverage, and a technology-adoption arc. Cases
that are smaller, private, non-US, public-policy, or shaped around a different kind
of decision will strain the kit in places that look like bugs and are actually the
edge of what it was fitted to. Distinguishing "defect" from "misfit" is the most
valuable classification in a field-test review and the one I am least equipped to
make unaided.

**49. Fix the method before you see the data.** The intake procedure for the field
test — how to inventory, classify, weight, and size the resulting release — was
written before any of the test material was read. Not out of ceremony: a
prioritization scheme invented after seeing the findings will rank whatever is most
interesting to build, and the front-end generators are the most interesting thing on
this roadmap while also being the least urgent.

**50. Publishing a repo with your home directory in it says you didn't read it.**
Preflight check 11 costs nothing per release and prevents a small leak with an
outsized signal. The general form: guards are cheapest to add when nothing is
currently wrong, because that is exactly when you can verify they work in both
directions — this one was tested by planting a path and watching it fail, then
removing it and watching it pass. It also flagged its own changelog entry on the
first run, which is the useful reminder that a checker matching *prose about* the
thing is a checker that will be switched off — the fix was to require a trailing
path segment, not to add an exemption.

**51. The bug you just fixed is probably also somewhere else.** One version after
correcting a workflow that silently skipped its own job, preflight check 10 was found
doing the same thing: an unreachable remote hit a `continue` and the check reported
green having compared nothing. Nothing connected the two except the shape — *a guard
that cannot see reports success*. After fixing a class of bug, it is worth spending
ten minutes grepping for the same shape elsewhere, because the habit that produced it
was not confined to one file.

## v3.9.0 — 2026-08-26 (field test)

*First lessons drawn from someone else building real cases with the kit, rather than
from the author testing his own work. Two complete four-document packages, both
against v3.8.0, both on the Claude Code path.*

**52. A threshold written in prose is not a threshold.** The skills state numeric
rules — `assess-bias` says company-affiliated voices above 50% make bias "at least
MEDIUM"; `verify-quotes` says a VERIFIED verdict requires a source file and line
number for each quote. Nothing computes either one. A model reads the prose and forms
a judgment, and across three separate gates in a single run every judgment drifted the
same direction: toward passing. A base at 62% company-affiliated was reported
"LOW–MEDIUM". A quote check that reasoned about source *categories* rather than
individual spans reported PASS, and a later span-by-span trace of the same documents
found five real defects — two misquotes, framing pulled inside the quotation marks,
dropped words, and constructed illustrations sitting in quotes. The rule was right
and present the whole time; nothing made it binding.

**53. Describing a problem is not gating it.** Faced with a source base that was
about 82% the subject's own material, `/assess-sources` diagnosed the situation
accurately and at length — it called the base one-sided, named it the opposite
failure mode from a thin base, and set bias to HIGH. Then it returned YELLOW and the
writing proceeded. The gate averages four dimensions, two of which reward volume, so
a prolific self-publisher scores high on Depth and Completeness and pulls the average
up past a RED reliability score. Independence entered the calculation only as a floor
of one source. The prose was excellent and load-bearing on nothing. **If a finding
should stop work, it has to be an input to the arithmetic, not a paragraph beside
it.**

**54. A summarized source is an unsourced source.** When research is delegated to
subagents or read live through a browser, what lands on disk is the agent's dossier,
and the dossier paraphrases. The verbatim wording stays in the session transcript and
dies with it. Quotations then trace to nothing — not because anyone fabricated them,
but because the only artifact that ever held the exact words was never a file. This
was the root cause of most of the quote defects above. **The raw capture is the
source; the dossier is a reading of it.** Save the capture before anything quotes
from it.

**55. Ignoring logs by default throws away the proof you did the work.** `*.log` sat
in `.gitignore` from the beginning, and the assessment and verification logs — the
evidence that the go/no-go gates ran and what they concluded — are written as `.log`.
Of the two field cases, one committed its gate logs only because the operator noticed
and forced the add; the other committed none, and its audit trail is simply gone. For
a kit whose entire claim is that its output can be defended, discarding the record of
the defence by default is the wrong side to err on. Generic ignore patterns inherited
from software projects do not know which of your files are the product.
