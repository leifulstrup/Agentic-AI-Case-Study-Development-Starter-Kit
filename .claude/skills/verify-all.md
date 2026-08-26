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

10. **Every sub-check must report how much it examined.** A check reports PASS only
    if it can state the number of units it actually inspected — quoted spans traced,
    figures recomputed, links requested, data points compared across documents. The
    unit count goes in the summary table beside the verdict.

    **A check that cannot state its unit count is reported as `NOT RUN`, never as
    PASS.** `NOT RUN` blocks publication exactly as a failure does, and says so in
    Critical Issues.

    This exists because of a specific failure. The quote check once returned PASS on
    a document set that a later span-by-span trace showed to contain five real
    defects — two misquotes, framing pulled inside the quotation marks, dropped
    words, and constructed illustrations sitting in quotes. It had reasoned about
    *source categories* rather than individual spans, and nothing in its output
    distinguished that from a real pass. The same shape had already been found twice
    in this project's release tooling: a workflow that silently did nothing for six
    versions, and a check that went green because it could not reach the remote it
    was meant to compare against.

    **A verdict is earned by an amount of work, and the report must show the
    amount.** "PASS" with no unit count is an opinion, not a result.

11. **Generate unified report**:

```
# Case Study Quality Report

Generated: [date]
Case: [company_name] — [topic]
Documents checked: [count]

## Executive Summary

| Check | Units examined | Pass | Warn | Fail |
|-------|----------------|------|------|------|
| Consistency | X data points compared | X | X | X |
| Sources | X claims checked | X | X | X |
| Quotes | X spans traced | X | X | X |
| Financials | X figures recomputed | X | X | X |
| Links | X URLs requested | X | X | X |
| Bias | X voices counted | — | LOW/MED/HIGH | — |
| Cross-Document | X alignments checked | X | X | X |

Any row whose "Units examined" cell is blank, "n/a", or unquantified is reported
as **NOT RUN** and listed under Critical Issues.

**Overall Status**: [Ready for Use / Needs Review / Significant Issues / Blocked — checks did not run]

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
