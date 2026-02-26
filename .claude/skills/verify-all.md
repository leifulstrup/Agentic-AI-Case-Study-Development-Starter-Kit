# Verify All

Run comprehensive quality checks on all case study documents, including data consistency, source attribution, quote verification, link validation, financial accuracy, bias assessment, and cross-document alignment.

## Usage

```
/verify-all
```

## Instructions

Execute all verification skills in sequence:

1. **Pre-flight check**:
   - List `.md` files in `case-study/` (excluding `.gitkeep`)
   - If none found, generate a "No Documents Found" report with next steps and stop:
     ```
     # Case Study Quality Report — No Documents Found

     The `case-study/` directory does not contain any case study documents yet.

     ## Next Steps
     1. Run `/setup-case` to configure your project
     2. Add sources and run `/add-sources` to register them
     3. Run `/write-document` to create your first document
     ```
   - If some but not all 4 expected documents found, note missing ones but proceed

2. **Run /verify-consistency** — Cross-document data point matching
3. **Run /verify-sources** — Attribution completeness
4. **Run /verify-quotes** — Quote traceability
5. **Run /validate-financials** — Arithmetic and financial figure accuracy
6. **Run /verify-links** — External URL validation
7. **Run /assess-bias** — Source composition and perspective balance
8. **Run /verify-cross-document** — Structural alignment between documents

9. **Check verification debt**: Read `verification-debt.yaml` and summarize open items.

10. **Generate unified report**:

```
# Case Study Quality Report

Generated: [date]
Case: [company_name] — [topic]
Documents checked: [count]

## Executive Summary

| Check | Pass | Warn | Fail |
|-------|------|------|------|
| Consistency | X | X | X |
| Sources | X | X | X |
| Quotes | X | X | X |
| Financials | X | X | X |
| Links | X | X | X |
| Bias | — | LOW/MED/HIGH | — |
| Cross-Document | X | X | X |

**Overall Status**: [Ready for Use / Needs Review / Significant Issues]

## Verification Debt Summary

| Status | Count |
|--------|-------|
| Unverified claims | X |
| Flagged items | X |
| Verified (resolved) | X |
| Removed | X |
| **Open (needs action)** | **X** |

{If verification-debt.yaml doesn't exist: "Verification debt not tracked. Run /write-document to enable automatic tracking."}

## Critical Issues (Must Fix)
[List any failing checks — these block publication]

## Warnings (Should Review)
[List items to review — publication possible but quality improves with fixes]

## Bias Assessment Summary
[Brief summary from /assess-bias — source composition and risk level]

## Detailed Reports
[Summaries from each check, with key findings]

## Recommendations
[Prioritized list of fixes, most important first]

## Pre-Publication Checklist

- [ ] All critical issues resolved
- [ ] Verification debt at zero (or acknowledged)
- [ ] Financial figures verified against sources
- [ ] Bias acknowledged in teaching materials
- [ ] Disclaimers added (/add-disclaimers)
- [ ] Cross-document alignment confirmed
- [ ] PDF exports generated (/export-pdf)
```

## Output

Create a log file:
- Filename: `verify-all-YYYY-MM-DD.log`
