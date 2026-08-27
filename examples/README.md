# Examples — what this kit actually produces

Before you invest a weekend, look at the output.

These are excerpts from a real case package built with this kit: **JPMorgan Chase and LLM Suite**, developed for ITEC-617 at American University's Kogod School of Business. Five sources went in — three interview transcripts, one earnings release, one news article. Four documents came out, then went through an independent verification pass that blocked publication until two real defects were repaired.

## Start here

| File | What it shows | Read it if you want to know… |
|------|---------------|------------------------------|
| [01 — Main Case](01-main-case-excerpt.md) | Opening section of the student-facing narrative | …whether the prose is teachable or reads like AI |
| [02 — Teaching Note](02-teaching-note-excerpt.md) | Learning objectives, 80-minute session plan, discussion questions | …whether you could walk into a classroom with this |
| [03 — Source Registry](03-source-registry-excerpt.md) | Every source tiered, with independence and processing status | …how the kit decides what a source can and cannot support |
| [04 — Verification Report](04-verification-report-excerpt.md) | The `/verify-all` quality report, including what it caught | …what "verified" actually means here |
| [05 — Verification Debt](05-verification-debt-excerpt.md) | Unsourced claims tracked and resolved | …how the kit keeps AI general knowledge from passing as research |

## The short version

**What went in.** Five sources, roughly 22,000 words: a VentureBeat podcast interview with the protagonist, a McKinsey interview, a Bloomberg TV interview with the CEO, a quarterly earnings release, and a CNBC feature.

**What came out.** Four documents, roughly 16,900 words — Main Case (5,800), Additional Sources and Data (5,000), Technical Supplement (3,000), Teaching Note (3,050) — plus a source registry, a verification-debt ledger, and a quality report.

> **These excerpts are longer than the kit now targets.** This package was built before
> v4.2.0 halved the default lengths, and it is kept at its original size because it is a
> record of a real run rather than a model to match. The current defaults are a Main Case
> near 2,500 words with a package near 7,500 — see `documents.target_word_counts` in
> `case-config.yaml`. **Read these for what a finished document looks like: how a
> protagonist is introduced, how a quotation is attributed, how a session plan is timed.
> Do not read them as a length to hit.**

**What the verification found.** Across ~230 attributed claims and 87 financial figures with arithmetic independently recomputed: **zero fabricated quotes, zero invented numbers, zero arithmetic errors.** It did find one spliced composite quotation and one cross-document title mismatch, and it blocked publication until both were fixed. That is the system working as designed — the writing pass erred, the verification pass caught it.

**What an independent quality judge said.** Scored against a seven-dimension case rubric by a different model than the one that wrote it: 31/35, "would teach with minor edits." Strongest on evidence discipline, teachability, and balance. Weakest on data sufficiency — the case gives students figures to argue about but no quantitative exhibit to compute with, which is exactly the kind of gap the kit's coaching workflow is designed to surface.

## Honest caveats

**This package has a thin source base and the documents say so.** Four of five sources are the company's own executives; only one is independent journalism, and even that reporter had company-granted access. The kit measured this, reported it as MEDIUM-to-HIGH bias risk, and the Teaching Note turns it into the closing classroom segment rather than hiding it. A stronger case would add employee, customer, regulator, and critic voices — which is what `/coach-case` exists to help you go find.

**Excerpts, not full documents.** The sources are copyrighted; the full case quotes them heavily. Enough is shown here to judge the quality of the output, which is the point.

**These are v3.2.0-era artifacts.** The current release applies a stricter quotation standard — a source that was editor-processed or machine-transcribed can no longer support a claim of verbatim quotation. The excerpts here are annotated to current standards, and the difference is explained in [01](01-main-case-excerpt.md).

## What to do next

If the output looks like something you would teach, the [main README](../README.md) has the quick start. If you are still choosing a topic, run `/scout-case` first — it will tell you in twenty minutes whether a company can support a case at all, which is the cheapest failure to avoid.
