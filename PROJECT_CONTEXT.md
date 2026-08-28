# Project Context

Quick reference for session continuity. Auto-maintained by skills — you do not need to edit this manually.

## Project Overview

**Repository**: Agentic AI Case Study Development Starter Kit
**Type**: GitHub template repository
**Version**: 4.5.0
**Course**: ITEC-617, American University Kogod School of Business, Spring 2026
**Purpose**: Template for developing business school MBA case studies from digital sources using AI tools

## Current Status

**Phase**: Adoption (v4.0.0). Claude Cowork is now the recommended path and document scope is course-configurable, both adopted from a teaching colleague's fork for non-technical students. **The Cowork path has not been field-tested** — one end-to-end run is the next release's first job. The first field test was classified, converted into seeded regression tests (defect-set v3), and released as fixes. Blind compliance testing then showed that only one of the release's two quote fixes had any measurable effect; v3.9.1 withdraws the other claim. The `/verify-all` orchestration change is confirmed effective under the condition that matters. **The incident that motivated the release remains unexplained.**

**Agentic Tool Paths**:
- [x] Claude Cowork — **recommended**; reads `AGENTS.md` directly, no setup (untested end-to-end)
- [x] Claude Code — 20 `/slash-commands` via `.claude/skills/`
- [x] VS Code + GitHub Copilot — Agent Mode via `.github/copilot-instructions.md`
- [x] Chat Tools — Starter prompt via `STARTER_PROMPT.md`

**Documents** (template placeholders):
- [ ] Additional Sources - placeholder
- [ ] Main Case - placeholder
- [ ] Supplement - placeholder
- [ ] Teaching Note - placeholder

## Source Quality

**Source Registry**: Template placeholder (not populated)
**Tier Breakdown**: T1: 0 | T2: 0 | T3: 0
**Last Assessment**: N/A (template repo)
**Assessment Result**: N/A

## Verification Debt

**Open Items**: 0
**Last Updated**: N/A
See `verification-debt.yaml` for details.

## Key Decisions Made

- v3.0.0: Conversation-first, skill-driven architecture with 16 slash commands
- v3.1.0: Added VS Code + GitHub Copilot as second agentic path (free via GitHub Education)
- Copilot instructions mirror CLAUDE.md behavioral guidance with skill equivalents table
- README Step 3 presents three options: Option A (Claude Code), Option B (VS Code + Copilot), Option C (Chat Tools)
- v3.2.0: Relicensed kit to MIT (produced cases remain author's choice, CC BY-NC default); AGENTS.md is now the canonical instruction file (CLAUDE.md imports it; copilot-instructions.md points to it); verification story promoted to top of README; confidence verdicts added to /verify-quotes; VERIFICATION_PLEDGE, CITATION.cff, CONTRIBUTING added; development log.md + lessons_learned.md + evals/ regression framework introduced

## Testing History

- Rob Silverman (beginner): Chat tool path tested — exposed UX issues fixed in v3.0.0
- Leif's Moderna case (power-user): Full Claude Code path tested — exposed verification and bias issues fixed in v3.0.0
- Copilot Agent Mode (v3.1.0): Two tests passed — status check and source assessment both used correct terminology and process model

### Classroom adoption (v3.1.x-era releases)

**The kit has been used in teaching, and this record previously did not say so.**
Approximately **30 MBA students and 3 faculty** have built cases with it. Students used
it in both roles the kit supports — authoring their own cases, and critiquing them as
part of learning to work with AI. **Faculty have taught with the output of at least two
case developments, successfully.**

Two things follow. First, the pedagogical premise is not speculative: the workflow
survives contact with a real cohort, and students critiquing their own AI-assisted work
is an established use rather than an aspiration. Second, this adoption ran on **v3.1.x-era
releases** — before source integrity (v3.3), the independence cap, the freeze protocol,
the verification-independence rule, and the halved document lengths. Feedback from those
users describes an earlier kit, and the newer verification machinery has correspondingly
*less* classroom evidence behind it than the workflow as a whole.

**Nothing since v3.1.x has been taught.** Keep the two claims distinct: the method is
classroom-proven; the current verification pipeline is not.

## Next Steps

1. **Explain the original incident.** Three hypotheses tested across four blind agent runs; none reproduces the field verification's PASS. Untested candidates: a long preceding authoring session, a verifier checking documents it authored itself, a real case with no planted defects to find
2. Convert every field-found defect into a permanent seeded regression test
3. Size and ship the next version from the ranked findings
4. Standing backlog: n=2 eval variance run; three grading rubrics; student-facing
   verification-literacy guide; quoting rules carried into `/write-document`;
   cross-path parity check; v4.0 front-end generators
