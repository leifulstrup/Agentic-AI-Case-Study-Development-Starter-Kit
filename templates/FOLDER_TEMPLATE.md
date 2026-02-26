# Case Study Project Folder Template

Quick-start template for organizing a new case study project.

> **Note**: If you created your project using the GitHub "Use this template" button, most of this structure is already in place. See the **Post-Clone Setup** section below.

---

## Directory Structure

```
[company-name]-case-study/
│
├── README.md                          # Project overview
├── CHANGELOG.md                       # Version history
├── CLAUDE.md                          # Claude Code instructions
├── case-config.yaml                   # Central configuration (UPDATE THIS FIRST)
├── PROJECT_CONTEXT.md                 # Session continuity document
├── .gitignore                         # Git exclusions
│
├── .github/
│   └── copilot-instructions.md        # VS Code Copilot custom instructions
│
├── case-study/                        # Core case documents (edit these)
│   ├── [Company]_Case.md              # Main narrative (~5,000 words)
│   ├── [Company]_Supplement.md        # Technical/industry context
│   ├── [Company]_Teaching_Note.md     # Instructor guide
│   └── [Company]_Additional_Sources.md # Compiled research
│
├── verification-debt.yaml             # Tracks unverified AI claims
│
├── sources/                           # Research materials (reference)
│   ├── transcripts/                   # Interview transcripts
│   ├── financial/                     # SEC filings, earnings
│   ├── news/                          # News articles
│   ├── reports/                       # Analyst reports
│   └── Source_Registry.md             # Source catalog with quality tiers
│
├── exports/                           # PDF exports (generated)
│   ├── [Company]_Case.pdf
│   ├── [Company]_Supplement.pdf
│   ├── [Company]_Teaching_Note.pdf
│   └── [Company]_Additional_Sources.pdf
│
└── .claude/                           # Claude Code configuration
    └── skills/                        # Skills (slash commands)
        ├── setup-case.md              # /setup-case
        ├── add-sources.md             # /add-sources
        ├── assess-sources.md          # /assess-sources
        ├── write-document.md          # /write-document
        ├── check-status.md            # /check-status
        ├── verify-all.md              # /verify-all
        ├── verify-consistency.md      # /verify-consistency
        ├── verify-quotes.md           # /verify-quotes
        ├── verify-sources.md          # /verify-sources
        ├── verify-links.md            # /verify-links
        ├── validate-financials.md     # /validate-financials
        ├── assess-bias.md             # /assess-bias
        ├── verify-cross-document.md   # /verify-cross-document
        ├── add-disclaimers.md         # /add-disclaimers
        ├── export-pdf.md              # /export-pdf
        └── git-update.md              # /git-update
```

---

## Setup Commands

### 1. Create Directory Structure

```bash
# Create project folder
mkdir [company-name]-case-study
cd [company-name]-case-study

# Create subdirectories
mkdir -p case-study
mkdir -p sources/transcripts sources/financial sources/news sources/reports
mkdir -p exports
mkdir -p .claude/skills
```

### 2. Initialize Git

```bash
git init
```

### 3. Create .gitignore

```bash
cat > .gitignore << 'EOF'
# macOS
.DS_Store

# Logs
*.log

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.venv/
venv/

# Editor
.vscode/
.idea/

# Temporary files
*.tmp
*~
EOF
```

### 4. Skills Files

Skills are already included in `.claude/skills/` when you create your repository from the template. No manual copying is needed.

---

## Post-Clone Setup (GitHub Template Users)

If you created your repository using the "Use this template" button:

### Recommended: Use `/setup-case`

In Claude Code, run:
```
/setup-case
```

This asks you questions conversationally and writes all configuration files automatically. No manual editing needed.

### Alternative: Manual Setup

If not using Claude Code:

1. Open `case-config.yaml` and replace placeholder values
2. Update `PROJECT_CONTEXT.md` with your case details
3. Add sources to `sources/` folders
4. Update `sources/Source_Registry.md` as you add sources

### Initial Commit

```bash
git add -A
git commit -m "Configure case study for [Company Name]"
git push
```

---

## Template Files

### README.md

```markdown
# [Company Name] Case Study

MBA case study examining [brief description].

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Company]_Case.md | Main narrative | Draft |
| [Company]_Supplement.md | Technical context | Draft |
| [Company]_Teaching_Note.md | Instructor guide | Draft |
| [Company]_Additional_Sources.md | Research compilation | In Progress |

## Sources

Primary sources are in `sources/` folder. See `sources/Source_Links.md` for URLs.

## Usage

This case study is designed for a 75-90 minute MBA classroom discussion.

## Quality Verification

Run `/verify-all` to check quality before publication.

## License

[Specify license - typically educational use]
```

### CHANGELOG.md

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Initial project structure
- Source materials collected
```

### CLAUDE.md

```markdown
# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Purpose

MBA case study package for [COURSE] examining [COMPANY]'s [TOPIC].

## Document Architecture

**Core Case Study Documents** (in `case-study/`):
- `case-study/[Company]_Case.md` - Main narrative
- `case-study/[Company]_Supplement.md` - Technical supplement
- `case-study/[Company]_Teaching_Note.md` - Instructor guide
- `case-study/[Company]_Additional_Sources.md` - Source compilation

**Source Materials** (in `sources/`):
- Interview transcripts and PDFs
- See `sources/Source_Links.md` for URLs

## Key Data Points

Ensure these are consistent across documents:
- [Key metric 1]: [Value]
- [Key metric 2]: [Value]
- [Key date]: [Date]

## Quality Verification

| Command | Purpose |
|---------|---------|
| `/verify-all` | Run all quality checks |
| `/verify-consistency` | Check data consistency |
| `/verify-quotes` | Verify quote attribution |
| `/verify-sources` | Check source attribution |
| `/verify-links` | Validate URLs |
```

### PROJECT_CONTEXT.md

```markdown
# Project Context

Quick reference for session continuity.

## Project Overview

**Case Study**: [Company] - [Topic]
**Course**: [Course name and number]
**Target Audience**: [MBA students, executives, etc.]
**Session Length**: 75-90 minutes

## Current Status

**Phase**: [Source Collection / Drafting / Review / Complete]

**Documents**:
- [ ] Additional Sources - [status]
- [ ] Main Case - [status]
- [ ] Supplement - [status]
- [ ] Teaching Note - [status]

## Key Decisions Made

- [Decision 1]
- [Decision 2]

## Open Questions

- [Question 1]
- [Question 2]

## Next Steps

1. [Next step]
2. [Next step]
```

### sources/Source_Links.md

```markdown
# Source Links and References

## Primary Interviews

### [Source Name]
- **URL**:
- **Date accessed**:
- **Duration**:
- **Key speakers**:
- **Local file**: `transcripts/[filename]`

## Financial Sources

### [Company] SEC Filings
- **10-K**:
- **10-Q**:
- **Earnings call**:

## News Articles

### [Publication] - [Headline]
- **URL**:
- **Date**:
- **Paywall**: Yes/No

## Industry Reports

### [Report Name]
- **Source**:
- **URL**:
- **Date**:
```

---

## File Naming Convention

### Case Study Documents
```
[Company]_[Document Type].md
[Company]_[Document Type].pdf

Examples:
- Acme_Case.md
- Acme_Supplement.md
- Acme_Teaching_Note.md
- Acme_Additional_Sources.md
```

### Source Materials
```
[Source]_[Speaker/Topic]_[Type].[ext]

Examples:
- McKinsey_CEO_Interview.pdf
- Bloomberg_Earnings_Transcript.txt
- WSJ_Industry_Analysis.pdf
- Company_Q3_2025_Earnings.pdf
```

---

## Development Workflow

### Order of Document Creation

1. **Source_Links.md** - Catalog all sources with URLs
2. **Additional Sources** - Compile and organize research
3. **Main Case** - Write narrative
4. **Supplement** - Add technical context
5. **Teaching Note** - Create instructor guide

### Quality Gates

| Gate | Check | Command |
|------|-------|---------|
| After each document | Sources attributed | `/verify-sources [file]` |
| After completing case | Consistency | `/verify-consistency` |
| Before internal review | Full audit | `/verify-all` |
| Before publication | Links work | `/verify-links` |

---

## Checklist: New Project Setup

- [ ] Create folder structure
- [ ] Initialize git repository
- [ ] Create .gitignore
- [ ] Copy/create skills files
- [ ] Update skills with correct file paths
- [ ] Create README.md
- [ ] Create CHANGELOG.md
- [ ] Create CLAUDE.md
- [ ] Create PROJECT_CONTEXT.md
- [ ] Create sources/Source_Links.md
- [ ] Initial commit

---

*Use this template as a starting point. Adjust structure based on project needs.*
