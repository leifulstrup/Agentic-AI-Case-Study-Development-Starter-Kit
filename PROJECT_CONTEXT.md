# Project Context

Quick reference for session continuity. Auto-maintained by skills — you do not need to edit this manually.

## Project Overview

**Repository**: Agentic AI Case Study Development Starter Kit
**Type**: GitHub template repository
**Version**: 3.8.1
**Course**: ITEC-617, American University Kogod School of Business, Spring 2026
**Purpose**: Template for developing business school MBA case studies from digital sources using AI tools

## Current Status

**Phase**: Field testing (v3.8.x). The template is complete and released; it is now being exercised against independent case examples so that the next version is driven by observed use rather than by the author's roadmap.

**Agentic Tool Paths**:
- [x] Claude Code — 18 `/slash-commands` via `.claude/skills/`
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

## Next Steps

1. Review field-test results and classify findings (defect / gap / friction / misfit)
2. Convert every field-found defect into a permanent seeded regression test
3. Size and ship the next version from the ranked findings
4. Standing backlog: n=2 eval variance run; three grading rubrics; student-facing
   verification-literacy guide; quoting rules carried into `/write-document`;
   cross-path parity check; v4.0 front-end generators
