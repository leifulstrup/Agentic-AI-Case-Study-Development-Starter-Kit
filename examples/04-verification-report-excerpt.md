# Example — `/verify-all` quality report excerpt

*Produced by an independent verification pass over the finished package. This is the artifact you hand a colleague, a department chair, or an editor.*

---

```text
# Case Study Quality Report

Generated: 2026-07-08
Case: JPMorgan Chase & Co. — Enterprise AI Transformation, LLM Suite
Documents checked: 4
Verifier: independent verification agent (fresh eyes; did not author the documents)
Run conditions: OFFLINE — local source corpus only; no web search used.
Corpus integrity: all five files in sources/ byte-identical to frozen copies. No source tampering.

## Executive Summary

| Check          | Pass                | Warn                        | Fail |
|----------------|---------------------|-----------------------------|------|
| Consistency    | 38 data points      | 2                           | 0    |
| Sources        | ~230 attributed     | 1                           | 0    |
| Quotes         | ~225 VERIFIED       | 4 (LIKELY)                  | 1    |
| Financials     | 87 figures / 14 recomputed | 0                    | 0    |
| Links          | 0 checked           | 3 (offline run)             | 0    |
| Bias           | —                   | MEDIUM (HIGH composition)   | —    |
| Cross-Document | 15 checks           | 3                           | 1    |

**Overall Status**: Needs Review — no fabricated quotes, invented numbers, or
arithmetic errors found; the package is unusually well grounded. But one
quote-integrity violation and one cross-document mismatch block publication.

## Critical Issues (Must Fix)

1. **Spliced composite quote — Main Case, Section VIII, line 102.**
   The case renders as one quotation a passage that, in the McKinsey transcript
   (lines 133–138), belongs to a different answer three sentences earlier. The
   six-domain list is real and Waldron said it — but not there, and not in that
   sentence. The package's own Additional Sources exhibit has it correct, so the
   documents disagree with each other.
   FIX: restore the source wording; present the domain list as paraphrase outside
   the quotation marks, with its own citation.

2. **Companion-title mismatch — Additional Sources, line 3.**
   Refers to the Main Case as "Scaling Enterprise AI"; the actual title is
   "Thirty Thousand Assistants and the Limits of Bottom-Up AI."
```

*[Warnings, per-check detail, bias assessment, and the pre-publication checklist omitted.]*

---

## What to notice in this excerpt

**The verifier is a different pass than the writer.** Fresh eyes, no ownership of the prose. In this run the writer had followed the rules carefully and still produced a spliced quote — which is the entire argument for keeping the two roles separate.

**"Needs Review" blocked publication.** The kit's gate is not advisory. The findings above were repaired and re-checked before this package was accepted as a reference baseline; the fix log lives beside it.

**Errors are reported with the evidence to adjudicate them.** File, line, what the source actually says, and what to do about it. A reviewer can confirm the finding without re-reading the corpus.

**Nothing was fabricated.** Across ~230 attributed claims and 87 financial figures, with arithmetic independently recomputed, the run found zero invented quotes and zero invented numbers. That is the outcome the workflow exists to produce — and the reason the two real defects are worth taking seriously rather than waving through.
