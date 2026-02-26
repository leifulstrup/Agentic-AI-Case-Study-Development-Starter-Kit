# Quality Assurance Workflow

A step-by-step guide to verifying case study quality before publication.

---

## Overview

Quality verification ensures that case studies are:
- **Accurate**: All facts and quotes trace to sources
- **Consistent**: Data points match across documents
- **Complete**: All attributions are present
- **Functional**: All links work

---

## When to Run Quality Checks

| Milestone | Check | Purpose |
|-----------|-------|---------|
| After drafting a section | `/verify-quotes [file]` | Catch attribution issues early |
| After completing a document | `/verify-sources [file]` | Ensure full attribution |
| After documents with numbers | `/validate-financials` | Arithmetic and figure accuracy |
| Before internal review | `/verify-consistency` | Cross-document alignment |
| After all documents written | `/assess-bias` | Source perspective balance |
| After all documents written | `/verify-cross-document` | Structural alignment |
| Before publication | `/verify-all` | Comprehensive validation (runs all checks) |
| After updating URLs | `/verify-links` | Ensure links work |

---

## Quality Check Details

### 1. Consistency Verification (`/verify-consistency`)

**What it checks:**
- Financial figures match across documents (e.g., "$2B" vs "$2 billion")
- Dates for events are consistent
- Names and titles are spelled the same way
- Key terminology is uniform (e.g., "LLM Suite" vs "LLM suite")

**Common issues found:**
- Case says "150,000 users" but Supplement says "150K users"
- Teaching Note references "Phase 2" but Case calls it "Stage 2"
- Different dates for same milestone

**How to fix:**
1. Identify the authoritative source (usually the primary interview)
2. Choose one format (prefer specific over rounded: "150,000" over "150K")
3. Update all documents to match
4. Re-run `/verify-consistency` to confirm

### 2. Quote Verification (`/verify-quotes`)

**What it checks:**
- Every quote in quotation marks has an attributed speaker
- The quote text matches what the speaker actually said
- Paraphrases are distinguished from exact quotes

**Common issues found:**
- Quote attributed to CEO but spoken by CAO
- Quote slightly paraphrased without indicating this
- Quote has no source citation

**How to fix:**
1. Locate the exact quote in source documents
2. Verify speaker identity
3. If paraphrased, either:
   - Find the exact quote and use it, or
   - Rewrite as indirect speech ("Waldron noted that...")
4. Add source citation if missing

### 3. Source Verification (`/verify-sources`)

**What it checks:**
- All factual claims have attribution
- Specific statistics cite their source
- Bibliography matches in-text citations

**Common issues found:**
- Statistic like "$700B savings potential" with no source
- Quote mentions "according to analysts" without naming them
- Source cited in text but missing from bibliography

**How to fix:**
1. Trace claim to original source
2. Add proper citation (Speaker, Publication, Date)
3. Update bibliography if needed
4. If source cannot be found, either:
   - Remove the claim, or
   - Mark as "industry estimate" with appropriate hedging

### 4. Link Verification (`/verify-links`)

**What it checks:**
- All URLs return 200 status
- Page content matches expected topic
- No broken or redirected links

**Common issues found:**
- 404 errors (page removed)
- Paywall blocks content
- URL redirects to different page

**How to fix:**
1. For 404s: Search for archived version (Wayback Machine) or updated URL
2. For paywalls: Note paywall status or find alternative source
3. For redirects: Update to canonical URL
4. If unfixable, remove link or replace with alternative source

---

## Full Quality Audit (`/verify-all`)

Run this before any publication or sharing. It executes all checks and produces a unified report.

**Report structure:**

```
# Case Study Quality Report

Generated: [date]
Documents checked: 4

## Executive Summary

| Check | Pass | Warn | Fail |
|-------|------|------|------|
| Consistency | X | X | X |
| Sources | X | X | X |
| Quotes | X | X | X |
| Links | X | X | X |

**Overall Status**: [Ready for Use / Needs Review / Significant Issues]

## Critical Issues (Must Fix)
[List any failing checks]

## Warnings (Should Review)
[List items to review]

## Detailed Reports
[Summaries from each check]

## Recommendations
[Prioritized list of fixes]
```

**Interpreting results:**

| Status | Meaning | Action |
|--------|---------|--------|
| Ready for Use | No critical issues | Safe to publish |
| Needs Review | Warnings present | Review each warning, decide if acceptable |
| Significant Issues | Failures present | Must fix before publication |

---

## Log Files

Each verification creates a log file:
- `verify-consistency-YYYY-MM-DD.log`
- `verify-quotes-YYYY-MM-DD.log`
- `verify-sources-YYYY-MM-DD.log`
- `verify-links-YYYY-MM-DD.log`
- `verify-all-YYYY-MM-DD.log`

**Log file management:**
- Log files are excluded from git via `.gitignore`
- Keep recent logs for reference during editing
- Delete old logs periodically to reduce clutter

---

## Quality Standards

### Minimum Requirements (Must Pass)

1. **All quotes verified** - No unattributed quotes in final documents
2. **Data consistency** - Same numbers across all documents
3. **Critical links work** - Links to primary sources must function
4. **Bibliography complete** - Every cited source in bibliography

### Best Practices (Should Aim For)

1. **Exact quotes preferred** - Minimize paraphrasing
2. **Primary sources** - Cite original interviews over news summaries
3. **Date specificity** - Include month/year, not just year
4. **Multiple perspectives** - Include quotes from different stakeholders

---

## Troubleshooting

### "Quote not found in sources"

1. Check for minor variations (capitalization, punctuation)
2. Search for key phrases rather than full quote
3. Verify you have all source documents
4. Quote may be from a source not yet added to sources/ folder

### "Inconsistency detected but I want different formats"

Sometimes variation is intentional (e.g., "150,000" in narrative, "150K" in chart). Document these exceptions and override the warning.

### "Link works in browser but fails in check"

Some sites block automated requests. Options:
1. Add note that manual verification was done
2. Take screenshot of working page
3. Find alternative source without blocking

### "Source document not readable"

PDFs may need OCR or may be image-based. Options:
1. Manually transcribe key quotes
2. Use OCR tool to extract text
3. Reference page numbers for manual verification

---

## Verification Debt

The `/write-document` skill automatically tracks unverified AI-generated claims in `verification-debt.yaml`. Each item includes:

- **claim**: The unverified statement
- **document**: Which document contains it
- **source_needed**: What type of source would verify it
- **status**: unverified / verified / removed / flagged
- **date_added**: When the item was logged

### Managing Verification Debt

1. **During writing**: Claims are auto-logged when `/write-document` detects unsourced content
2. **During verification**: `/verify-consistency` and `/verify-sources` update debt status
3. **Before publication**: All items should be verified, removed, or explicitly acknowledged

### Checking Debt Status

Run `/check-status` to see a summary, or read `verification-debt.yaml` directly.

**Goal**: Zero open debt items before publication (or explicitly acknowledged items in teaching materials).

---

## Pre-Publication Checklist

Before sharing case study materials:

- [ ] `/verify-all` shows "Ready for Use" or all warnings reviewed
- [ ] All four documents checked: Case, Supplement, Teaching Note, Sources
- [ ] `/validate-financials` shows no arithmetic errors
- [ ] `/assess-bias` reviewed and acknowledged in teaching materials
- [ ] `/verify-cross-document` confirms structural alignment
- [ ] Verification debt at zero (or all items acknowledged)
- [ ] Disclaimers added via `/add-disclaimers`
- [ ] PDF exports generated via `/export-pdf`
- [ ] CHANGELOG.md updated with version number
- [ ] Final commit and push

---

*Run quality checks frequently during development—catching issues early is easier than fixing them at the end.*
