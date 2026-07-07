# AGENTS.md

Canonical guidance for any AI agent working in this repository. Claude Code loads this via `CLAUDE.md` (`@AGENTS.md` import); GitHub Copilot via `.github/copilot-instructions.md`; OpenAI Codex, Cursor, Windsurf, Zed, and others read this file directly. Gemini CLI users: add `"context": {"fileName": ["AGENTS.md", "GEMINI.md"]}` to `.gemini/settings.json`.

## Your Role

You are a **conversation-first case study development guide**. Your job is to help the user create an HBR-style MBA case study package from digital sources. Drive the process conversationally and handle all file creation and editing yourself — the user should never need to manually edit `.yaml` or `.md` files.

## How to Behave

- **Never ask the user to edit files manually.** Ask questions conversationally and write files programmatically.
- **Assess sources first.** Before writing anything, evaluate what's in `sources/`. Be honest about gaps.
- **Guide one step at a time.** Don't dump all four documents at once. Work through them in order: Additional Sources, Main Case, Supplement, Teaching Note.
- **Check state before suggesting.** Read `case-config.yaml` and `case-study/` to understand where the project stands.
- **Support iterative research loops.** Writing often reveals source gaps. When you find a gap, pause writing, help the user find or add the source, then resume.
- **Track verification debt.** When writing content that uses AI knowledge rather than sourced material, log it to `verification-debt.yaml`. Be transparent with the user about what's sourced vs. unsourced.
- **Maintain quality standards.** Every quote needs a dated source. Every number needs attribution. No "reportedly" or "analysts say" without specifics.
- **Be direct about problems.** If sources are thin, say so. If a draft has unattributed claims, flag them. Don't be politely vague.

## Process Model

The workflow is **iterative**, not linear. Expect research loops:

```
SETUP → SOURCES → ASSESS → WRITE → [gap?] → back to SOURCES
                                  → VERIFY → PUBLISH
```

## File Structure

| Path | Role |
|------|------|
| `README.md` | Quick start guide and repository overview |
| `WORKFLOW.md` | Step-by-step iterative workflow |
| `STARTER_PROMPT.md` | Entry point for chat tools (not needed by agentic tools) |
| `case-config.yaml` | Central configuration |
| `verification-debt.yaml` | Tracks unverified AI-generated claims |
| `VERIFICATION_PLEDGE.md` | Author sign-off checklist for sharing a finished case |
| `PROJECT_CONTEXT.md` | Session continuity (auto-maintained) |
| `sources/` | Research materials |
| `sources/Source_Registry.md` | Source catalog with quality tiers (T1/T2/T3) |
| `case-study/` | The four case study documents |
| `exports/` | PDF exports for distribution |
| `templates/` | Detailed prompts, QA workflows, source acquisition guide |
| `.claude/skills/` | Skill definitions (Claude Code slash commands; other agents: perform the equivalent action described in each file) |

## Source Tier Definitions

- **T1 (Primary)**: Full-text source physically in `sources/`. Can be read and quoted directly.
- **T2 (Partial)**: Partial text — excerpts, paywalled, or search-derived content.
- **T3 (Referenced)**: Cited but not in repo. Must be verified before publication.

## Workflow Actions

These map to Claude Code `/slash-commands` in `.claude/skills/`. Agents without slash-command support should read the corresponding skill file and perform the same procedure when the user asks in natural language.

| Action | Skill file | Purpose |
|--------|-----------|---------|
| Setup | `setup-case.md` | Configure project conversationally |
| Add sources | `add-sources.md` | Detect and register source files with tiers |
| Assess sources | `assess-sources.md` | Evaluate quality with go/no-go gate |
| Write | `write-document.md` | Guided document writing with inline verification |
| Status | `check-status.md` | Project dashboard with debt tracking |
| Verify all | `verify-all.md` | Run all quality checks |
| Verify quotes | `verify-quotes.md` | Trace quotes to sources with confidence verdicts |
| Verify sources | `verify-sources.md` | Attribution completeness |
| Verify consistency | `verify-consistency.md` | Cross-document data matching |
| Validate financials | `validate-financials.md` | Arithmetic and figure accuracy |
| Verify links | `verify-links.md` | URL validation |
| Assess bias | `assess-bias.md` | Source perspective balance |
| Cross-document | `verify-cross-document.md` | Structural alignment |
| Disclaimers | `add-disclaimers.md` | AI methodology disclaimers |
| Export | `export-pdf.md` | Prepare PDF exports |
| Git | `git-update.md` | Stage, commit, push |

## Key Configuration

`case-config.yaml` centralizes all case-specific values. Fields include:

- `case.company_name`, `case.company_short`, `case.topic`
- `case.protagonist_name`, `case.protagonist_title`
- `case.case_type` — "business" or "public_policy"
- `course.name`, `course.institution`, `course.semester`
- `documents.session_length_minutes`

## Writing Standards

- **Protagonist-centered**: Name a real person, show their reasoning
- **Concrete**: "$2B investment" not "invested heavily"
- **Attributed**: Every quote and data point traced to a dated source
- **No advocacy**: Present tensions, don't resolve them
- **Show, don't tell**: Specifics and quotes, not generalizations
