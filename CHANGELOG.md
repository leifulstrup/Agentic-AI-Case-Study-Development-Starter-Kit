# Changelog

All notable changes to this template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **`/scout-case` skill** — pre-commitment coaching: scouts 1–4 candidate topics for whether they can support a case at all (protagonist voice and decision moment are fatal-if-absent; quantitative base, independent coverage, and perspective range grade quality), scores each on the same four dimensions `/assess-sources` uses later, and returns PURSUE / VIABLE WITH WORK / REDIRECT / AVOID with a starter source list. Prevents the most expensive failure in case development — discovering three weekends in that the company can't support a case
- **`learning-context.yaml`** — optional classroom-context config (audience program and per-domain fluency, session length/size/modality/format, prep expectations, teaching themes and target skill, which front-ends to generate, persona behavior, accessibility, and machine-readable guardrails). Front-end generators read it so one verified case body renders differently for different audiences — the mechanism behind mass customization
- **`RELEASING.md`** — two-remote workflow (private dev repo for daily work, public template for curated releases) with pre-publish checklist and guidance on eval assets vs. copyright
- **`/coach-case` skill** — the kit now acts as a coach and advisor, not just a pipeline: diagnoses gaps across five lenses (source-type coverage, voice-based perspective coverage, foundational confidence of load-bearing claims, biographical grounding for every named person/organization, rubric-facing weaknesses), offers targeted research help with proposed queries, runs a QA/QC gate (provenance/independence/corroboration/tier/risk) on everything gathered before it counts, measures before/after assessment deltas so additions that hurt are caught honestly, and logs every iteration to `coaching/coaching-log.md` with a git checkpoint
- **`templates/COACHING_LOG.md`** — iteration log template: gap map, QA/QC verdicts, teachable discrepancies, score deltas, helped/neutral/hurt judgment
- **`evals/`** baseline results: v3.2.0 baseline run vs frozen JPM corpus (10/10 seeded-defect recall, 31/35 judged; golden blessed after surgical fixes)

## [3.2.0] - 2026-07-07

Trust and standards release: relicense to MIT, lead with the verification story, and adopt the AGENTS.md cross-tool standard so the kit works consistently across Claude Code, Copilot, Codex, Cursor, Gemini CLI, and other agentic harnesses.

### Changed
- **LICENSE** — Relicensed the kit from CC BY-NC 4.0 to **MIT** (loosening restrictions; sole-copyright-holder change). The kit's license now explicitly covers only the kit itself; case studies produced with it remain the author's work under the author's chosen license (`case-config.yaml` still suggests CC BY-NC 4.0 as a sensible default for educational materials)
- **CLAUDE.md** — Now imports canonical guidance from `AGENTS.md` (`@AGENTS.md`) and keeps only Claude Code-specific content (slash commands, between-document gates)
- **.github/copilot-instructions.md** — Slimmed to a pointer at `AGENTS.md` plus the Copilot skill-equivalents table (removes duplicated guidance that could drift)
- **.claude/skills/verify-quotes.md** — Added confidence verdicts (VERIFIED / LIKELY / DISPUTED / APOCRYPHAL) with required evidence per verdict, a publication rule (only VERIFIED ships in quotation marks), and an explicit trace-to-primary-source requirement (quote-aggregator sites are not verification)
- **README.md** — New "Built for Verification" section explaining verification debt, source tiers/gates, and the seven-check pipeline; new License section; updated badges to v3.2.0/MIT
- **templates/SOURCE_ACQUISITION.md** — Expanded legal guidance: keep case repos private during development, prefer links + excerpts for T2 sources, educational fair use is a balancing test not a blanket exemption

### Added
- **AGENTS.md** — Canonical, tool-neutral agent guidance following the Linux Foundation-stewarded AGENTS.md convention (read natively by OpenAI Codex, Cursor, Copilot coding agent, Windsurf, Zed, and others; Gemini CLI via one-line settings entry)
- **VERIFICATION_PLEDGE.md** — Author sign-off checklist converting the verification workflow into a shareable statement for colleagues, chairs, and editors
- **CITATION.cff** — Makes the kit citable (GitHub renders a "Cite this repository" button)
- **CONTRIBUTING.md** — Contribution path for other professors and practitioners, including the verified-body invariant for generator skills

## [3.1.0] - 2026-02-23

Add VS Code + GitHub Copilot as a second agentic AI path alongside Claude Code. Students with GitHub Education get Copilot Pro free, making this an accessible alternative with Agent Mode (file read/write, terminal commands, custom instructions).

### Added
- `.github/copilot-instructions.md` — Custom instructions for VS Code + GitHub Copilot Agent Mode, with skill equivalents table mapping all 16 `/slash-commands` to natural-language requests

### Changed
- **README.md** — Rewrote Step 3 with three tool options: Claude Code (Option A), VS Code + Copilot (Option B), Chat Tools (Option C). Added comparison table, "Getting Tech Help" subsection, Copilot references in Step 4, Skills Reference, file listing, and Troubleshooting
- **WORKFLOW.md** — Added VS Code + Copilot parallel instructions to each phase (Configure, Register Sources, Assess, Write, Verify). Updated Quick Reference section title and notes
- **STARTER_PROMPT.md** — Updated header to list VS Code + Copilot as another agentic tool that doesn't need this file
- **CLAUDE.md** — Added Copilot Compatibility section noting `.github/copilot-instructions.md`
- **templates/FOLDER_TEMPLATE.md** — Added `.github/copilot-instructions.md` to directory tree

## [3.0.0] - 2026-02-23

Major upgrade to conversation-first, skill-driven experience. Students interact through `/slash-commands` that handle all file creation/editing. Verification built into every phase.

Motivated by two rounds of testing:
- **Rob Silverman** (beginner): Exposed chat-tool breakage, code block confusion, decision overload, missing git checkpoints
- **Leif's Moderna case** (power-user, 17 steps): Exposed source friction, verification debt, financial errors, bias discovered late

### Added

#### New Skills (11)
- `/setup-case` — Conversational project setup (replaces `/setup-project`). Asks questions one-at-a-time, writes `case-config.yaml`, `PROJECT_CONTEXT.md`, and `verification-debt.yaml` programmatically
- `/add-sources` — Detects new files in `sources/`, asks metadata, classifies into quality tiers (T1/T2/T3), updates Source Registry
- `/write-document` — Interactive document writing with prerequisites checking, section-by-section writing, inline verification, and research loop support
- `/check-status` — Project dashboard with phase progress, verification debt summary, source tier breakdown, recommended next action (replaces `/guide-next-step`)
- `/validate-financials` — Extracts financial figures, checks arithmetic, cross-references against sources
- `/assess-bias` — Analyzes source composition for perspective balance: selection bias, survivorship bias, framing bias, authority bias, recency bias
- `/verify-cross-document` — Structural alignment between documents: Teaching Note references case content, Supplement frameworks used in analysis, timeline consistency
- `/add-disclaimers` — Standardized AI-generated content disclaimers (classroom/draft/publication contexts) and AI methodology notes
- `/export-pdf` — Formats documents for PDF export with heading hierarchy, page breaks, and conversion instructions

#### New Files
- `verification-debt.yaml` — Tracks unverified AI-generated claims with statuses (unverified/verified/removed/flagged)
- `sources/Source_Registry.md` — Source catalog with quality tiers (T1 primary, T2 partial, T3 referenced), replacing `Source_Links.md`

#### New Concepts
- **Source Tiers**: T1 (full-text in repo), T2 (partial/paywalled), T3 (referenced only)
- **Verification Debt**: Automatic tracking of unsourced AI claims during writing
- **Research Loops**: Named concept for iterative source-gathering during writing
- **Go/No-Go Gates**: GREEN/YELLOW/RED assessment for source readiness
- **Verification Gates**: Lightweight checks between documents

### Changed

#### Skills Enhanced
- `/assess-sources` — Added source tier breakdown, go/no-go gates (GREEN/YELLOW/RED), minimum viable source check, early bias detection
- `/verify-all` — Added `/validate-financials`, `/assess-bias`, `/verify-cross-document` to sequence; added verification debt summary and pre-publication checklist
- `/verify-consistency` — Added integration with `verification-debt.yaml`
- `/git-update` — Updated Co-Authored-By to Opus 4.6

#### Entry Points Rewritten
- **README.md** — One default path (not "choose"), separate code blocks per platform (Mac/Windows), troubleshooting section, agentic vs chat tool distinction, git checkpoints in workflow
- **STARTER_PROMPT.md** — Rewritten for chat tools only. Clear header distinguishing chat vs agentic tools. File upload workflow. No local file path references. Self-contained prompt
- **CLAUDE.md** — Removed overlap with STARTER_PROMPT. Added conversation-first behavioral instructions, iterative process model, verification debt tracking, source tier definitions, updated skill table (16 skills)
- **WORKFLOW.md** — Replaced linear 6-step with iterative model showing research loops. Added verification gates between documents. Added skill-driven workflow. Added "Targeted Edits" phase

#### Templates Updated
- **PROMPTS.md** — Added Phase 2.5 (Source Tier Classification), Phase 7.5 (Financial Verification), Phase 7.6 (Bias Assessment), Phase 8 (Disclaimers and Final Preparation)
- **QA_WORKFLOW.md** — Added `/validate-financials`, `/assess-bias`, `/verify-cross-document` to check schedule; added verification debt section; updated pre-publication checklist
- **SOURCE_ACQUISITION.md** — Added Source Tier Classification section, "Working with AI Web Access Limitations" section, expanded research workflow with iterative loops
- **FOLDER_TEMPLATE.md** — Updated directory structure with `verification-debt.yaml` and `Source_Registry.md`; updated skill list (16 skills); updated post-clone setup to reference `/setup-case`

#### Configuration
- `case-config.yaml` — Added `case.case_type` field ("business" or "public_policy"); added auto-generated header comment; updated template version to 3.0.0

#### Infrastructure
- `validate-template.yml` — Updated required files list for all new skills and files; added verification-debt.yaml validation

### Removed
- `.claude/skills/setup-project.md` — Replaced by `/setup-case`
- `.claude/skills/guide-next-step.md` — Replaced by `/check-status`

## [2.0.0] - 2026-02-21

Major simplification. Refocused the starter kit around an AI-guided workflow with a clear entry point, removing premature community infrastructure.

### Added
- `STARTER_PROMPT.md` — The centerpiece entry point. Students copy this prompt into any AI tool (Claude Code, ChatGPT, Gemini, Perplexity) to get guided through the entire case study development process
- `/assess-sources` skill — Evaluates source materials across four dimensions (depth, breadth, reliability, completeness) and produces a Source Assessment Report
- `/guide-next-step` skill — Checks project state and recommends the specific next action to take

### Changed
- **README.md** — Rewritten from 823 lines to ~140 lines. Now a student-focused quick start guide instead of a full methodology reference (detailed prompts remain in `templates/PROMPTS.md`)
- **CLAUDE.md** — Rewritten with "Your Role" and "How to Behave" sections that define Claude as an interactive case study development guide
- **WORKFLOW.md** — Simplified from 352 lines to ~120 lines. Six clear steps: Gather, Configure, Prompt, Develop, Verify, Publish
- **case-config.yaml** — Added prominent header with concrete example (Tesla factory automation) to make the first-edit experience more approachable
- **validate-template.yml** — Updated required files list (removed deleted files, added new ones)
- **FOLDER_TEMPLATE.md** — Removed reference to deleted `SKILLS_SETUP.md`
- **PULL_REQUEST_TEMPLATE.md** — Removed reference to deleted `CONTRIBUTING.md`

### Removed
- `CONTRIBUTING.md` — Premature community infrastructure
- `HALL_OF_FAME.md` — Premature community infrastructure
- `COMMUNITY_REGISTRY.md` — Premature community infrastructure
- `docs/ECOSYSTEM.md` — Premature community infrastructure
- `docs/GITHUB_PAGES.md` — Premature community infrastructure
- `docs/patterns/` — Entire pattern library directory (premature)
- `_config.yml`, `Gemfile`, `index.md` — Jekyll/GitHub Pages files
- `.github/workflows/update-registry.yml` — Community workflow
- `.github/workflows/stale.yml` — Community workflow
- `.github/workflows/issue-labeler.yml` — Community workflow
- `.github/workflows/pages.yml` — GitHub Pages workflow
- `.github/ISSUE_TEMPLATE/register-project.yml` — Community issue template
- `.github/ISSUE_TEMPLATE/submit-innovation.yml` — Community issue template
- `templates/SKILLS_SETUP.md` — Redundant (skills already exist in `.claude/skills/`)
- `templates/workflows/` — Downstream project workflow (premature)

## [1.1.0] - 2026-02-20

### Added

#### GitHub Pages Website (Disabled)
- **Just the Docs theme** - Professional documentation site configuration
- `_config.yml` - Jekyll configuration with remote theme
- `index.md` - Attractive landing page with methodology overview
- `Gemfile` - Ruby dependencies for Jekyll
- `.github/workflows/pages.yml` - Auto-deployment workflow (currently disabled)
- Front matter added to README.md, WORKFLOW.md, docs/ECOSYSTEM.md for navigation
- `docs/GITHUB_PAGES.md` - Documentation for enabling/disabling the feature

#### Ecosystem Hub Features
- **Community Registry** (`COMMUNITY_REGISTRY.md`) - Voluntary project registration system
- **Pattern Library** (`docs/patterns/`) - Curated collection of community-contributed patterns
- **Hall of Fame** (`HALL_OF_FAME.md`) - Recognition for contributors
- **Ecosystem Guide** (`docs/ECOSYSTEM.md`) - How to participate in the community

#### Issue Templates
- `register-project.yml` - Register case study projects to join community
- `submit-innovation.yml` - Submit prompts, skills, or workflow improvements

#### Automation Workflows
- `release.yml` - Auto-create GitHub releases when TEMPLATE_VERSION changes
- `update-registry.yml` - Auto-update community registry from registration issues
- `issue-labeler.yml` - Auto-label issues based on title and content
- `stale.yml` - Manage stale issues and PRs

#### Downstream Project Support
- `templates/workflows/check-template-updates.yml` - Workflow for case repos to check for template updates

### Changed
- Enhanced `templates/RETROSPECTIVE.md` with AI-Specific Innovations section

### Previous
- WORKFLOW.md with complete end-to-end workflow documentation

## [1.0.0] - 2026-01-12

### Added

- Initial template release
- 8-phase case study development methodology in README.md
- Template files:
  - `PROMPTS.md` - Copy-paste prompts for each development phase
  - `SKILLS_SETUP.md` - Claude Code verification skill templates
  - `QA_WORKFLOW.md` - Quality assurance procedures
  - `SOURCE_ACQUISITION.md` - Research and materials management guide
  - `FOLDER_TEMPLATE.md` - Project structure quick-start
  - `RETROSPECTIVE.md` - Post-case-study feedback capture
- Parameterized configuration via `case-config.yaml`
- Claude Code verification skills in `.claude/skills/`
- GitHub Actions CI/CD:
  - Markdown linting
  - Link validation
  - Template structure validation
- GitHub Issue templates for continuous improvement
- Contributing guidelines
