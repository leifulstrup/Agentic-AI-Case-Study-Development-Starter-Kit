# Verify All

Run comprehensive quality checks on all case study documents, including data consistency, source attribution, quote verification, link validation, financial accuracy, bias assessment, and cross-document alignment.

## Usage

```
/verify-all
```

## Instructions

Execute all verification skills in sequence:

0. **Freeze the tree before you look at anything.**

   A verification report describes the package *as it was at one moment*. If the
   documents change while you are checking them — or while the author is reading your
   findings and fixing them — the report describes a version that no longer exists, and
   every line in it becomes a claim about a vanished tree.

   This is not hypothetical. In testing, a `/verify-all` log was written at 10:51, the
   documents it described were edited at 11:05, and by the time a second pass read that
   log four of its statements were false about the files on disk. The log was not wrong
   when written. It was wrong when read, which is worse, because nothing in it said so.

   Before the first check:

   - **Record the frozen state** in the report header: every file in `case-study/`, with
     its **word count**. Word count is the fingerprint — it needs no terminal, and any
     edit that matters will move it. Add file sizes or modification times too if you can
     read them.
   - **Tell the author the tree is frozen**: *"I'm checking the package as it stands now.
     Please don't edit the documents until I report — if they change under me, I'll have
     to start again."* Say it once, plainly, before starting.
   - **Do not fix anything you find.** You are reading, not writing. A verifier who
     repairs as it goes is checking a moving target and cannot report what it examined.

   At the end of the run, **re-read the word counts and compare**. If any changed:
   **the report is void.** Say so at the top in those words, name which files moved, and
   re-run against the new state. Do not publish findings against a tree that moved under
   you, and do not quietly patch the report to match.

1. **Pre-flight check**:
   - **State who is verifying.** If this session also wrote the documents, say so in the
     report header and in the Executive Summary — see *Who Verifies* in `AGENTS.md`. A
     self-review is a draft check, not a publication gate, and an undisclosed one is
     indistinguishable from an independent review. This does not block the run; it
     labels it.
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
   - **Read `documents.required` from `case-config.yaml` to learn what "complete" means
     for this course.** Do not assume four. A document the course does not require is
     not a missing document, and reporting it as one trains authors to ignore the check
   - If a document named in `documents.required` is missing, note it and proceed

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
Verifier: [independent — did not author these documents | SAME SESSION AS AUTHOR]

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
- [ ] Verification debt at zero (or acknowledged) — **see the note below before treating
      this as a blocker**
- [ ] Financial figures verified against sources
- [ ] Bias acknowledged in teaching materials
- [ ] Disclaimers added (/add-disclaimers)
- [ ] Cross-document alignment confirmed
- [ ] PDF exports generated (/export-pdf)
```

## After the Author Fixes What You Found

**A correction round is a change round, and it carries the same defect risk as writing
did.** This is the step the workflow used to be missing, and it is not optional.

Measured, not supposed: in testing, fixing 25 findings introduced **11 new defects** —
stale counts copied from an interim draft, a footer contradicting the header in its own
file, speaker miscounts, a quotation breaking a convention the same round had just added.
Roughly two new problems for every five fixed. And the author's own report of the round
said *"Fixed. All 15 converted"* when **eight were still live**.

So, after corrections:

1. **Freeze again.** Same procedure as step 0. The state you verified is gone; this is a
   different package.
2. **Re-verify with someone who did not make the fixes.** A fresh session, per
   *Who Verifies* in `AGENTS.md`. **The person who made a correction is the worst
   available judge of whether it worked** — they know what they intended to change, so
   they read the intention rather than the text.
3. **Check two things, not one.** Whether each reported fix actually landed — verified
   against the source, not against the author's account of it — **and** whether the
   correction round introduced anything new. The second is where the defects are.
4. **Never accept "all fixed" as evidence.** It is a claim to be checked like any other.
   Verify each one against the source. In the case above, ten of fifteen were fixed and
   the summary said fifteen.

Repeat until a pass returns clean **against a tree nobody edited during it**. Until that
happens, the honest status is that no one has read the package end to end without also
changing it.

## When zero debt is not reachable

**Some debt cannot be closed from inside the workflow, and the kit should say so rather
than let an author grind against it.** Working offline, a claim needing a reference work,
a filing, or a paywalled article cannot be settled — no amount of re-running checks will
move it. In testing, a package sat with five definitional passages needing a source that
could not be fetched, against a publication bar of zero open debt. Those two facts are
incompatible, and nothing in the kit admitted it.

So: **"zero or acknowledged" means acknowledged is a real option**, not a euphemism for
failure. An item is legitimately acknowledged when the author can say what would settle
it, why it cannot be settled now, and what the document does in the meantime — normally
labelling the claim as a claim rather than asserting it as fact.

What acknowledgement does **not** cover: debt the author simply did not work through, or a
check that was never run. **A check that could not run is `NOT RUN` and still blocks** —
that is a different thing from a claim that cannot currently be sourced, and the
distinction is the whole point. One is unfinished work; the other is a limit of the
available evidence, disclosed.

## Output

Create a log file:
- Filename: `verify-all-YYYY-MM-DD.log`
