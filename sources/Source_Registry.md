# Source Registry

Central registry of all source materials for the case study, with quality tier classification.

> **Note**: This file is auto-maintained by `/add-sources`. You do not need to edit it manually.
>
> If you previously used `Source_Links.md`, that file is kept for reference. This registry replaces it.

---

## Source Summary

| Tier | Count | Description |
|------|-------|-------------|
| T1 — Primary | 0 | Full-text source in `sources/` folder |
| T2 — Partial | 0 | Partial text, search-derived, or paywalled |
| T3 — Referenced | 0 | Cited but not in repo; unverified |
| **Total** | **0** | |

### Tier Definitions

- **Tier 1 (T1)**: Full-text primary source physically present in the `sources/` folder. Can be read and quoted directly. Examples: full transcript, downloaded PDF, complete article text.
- **Tier 2 (T2)**: Partial text available — extracted quotes, search snippets, or paywalled content where only key passages were captured. Source exists but cannot be fully verified.
- **Tier 3 (T3)**: Referenced only — cited in the case but the full source is not in the repository. May be from AI general knowledge, web search results, or sources that could not be downloaded. Requires verification before publication.

### Independence Classification

Tier measures **access** (do we have the full text?). Independence measures **interest** (who made this, and what do they gain?). A full-text transcript of a vendor-sponsored podcast is T1 *and* compromised — both facts must be recorded.

- **INDEPENDENT** — No commercial, employment, or personal interest in how the subject is portrayed. Example: a staff reporter at a general-interest outlet.
- **INTERESTED** — Producer has a stake: a consultancy summarizing its own report, a vendor whose product appears, a law firm selling related counsel, a podcast episode with a sponsor in the same industry, an interviewer with a long professional relationship to the subject.
- **COMPANY** — Produced or controlled by the case subject: press releases, filings, blog posts, official bios, company-supplied roadmaps.
- **UNKNOWN** — Could not establish. Treat as INTERESTED until resolved.

Record the *specific* interest, not just the label: "INTERESTED — episode sponsored by Outshift by Cisco (AI vendor)" or "INTERESTED — McKinsey partner summarizing McKinsey's own report; 18-year colleague of the protagonist."

Note: a company-produced source can be excellent evidence *of what the company says*. The classification is not a quality judgment — it is a caution about which claims the source can settle on its own.

### Processing Status

Record how the text reached its current form. This governs whether it can support verbatim quotation:

- **VERBATIM** — Official transcript, published article text, or filing. Quotable directly.
- **EDITED** — The source states it was edited (e.g., "edited for clarity and length"). **Cannot support verbatim quotation** — use indirect speech, or quote with an explicit note that the source is an edited transcript.
- **ASR** — Machine speech-to-text with no human correction and no audio available for adjudication. Expect corrupted names and terms. Quote only with the bracket convention, and never claim verbatim accuracy.
- **EXTRACTED** — Text pulled from a PDF (layout artifacts possible, content faithful). Quotable with care.

A source that is EDITED or ASR may still be T1 for access purposes, but the case must not assert that its quotations are verbatim.

---

## Primary Interviews & Transcripts

| # | Source | Tier | Date | Speakers | Independence | Local File | Key Content |
|---|--------|------|------|----------|--------------|------------|-------------|

---

## Financial Sources

| # | Source | Tier | Date | Type | Independence | Local File | Key Data |
|---|--------|------|------|------|--------------|------------|----------|

---

## News Coverage

| # | Source | Tier | Date | Publication | Author | Independence | Key Content |
|---|--------|------|------|-------------|--------|--------------|-------------|

---

## Industry & Analyst Reports

| # | Source | Tier | Date | Publisher | Independence | Local File | Key Data |
|---|--------|------|------|-----------|--------------|------------|----------|

---

## Other Sources

| # | Source | Tier | Date | Type | Independence | URL/File | Key Content |
|---|--------|------|------|------|--------------|----------|-------------|

---

## Source Credibility Notes

| Source Type | Typical Credibility | Typical Tier | Notes |
|-------------|-------------------|--------------|-------|
| SEC Filings | Highest | T1 | Legally required accuracy |
| Direct Interviews | High | T1 | First-hand accounts, verify transcript accuracy |
| Earnings Calls | High | T1-T2 | Official statements; T1 if full transcript available |
| Major Publications | Medium-High | T1-T2 | T1 if full text downloaded; T2 if paywalled |
| Company Blog/PR | Medium | T1-T2 | Self-reported; useful for quotes and dates |
| Industry Reports | Medium-High | T1-T2 | T1 if full report; T2 if excerpts only |
| Social Media | Low | T3 | Verify independently before citing |
| AI-generated claims | Unverified | T3 | Must be sourced before publication |
| Sponsored podcasts/webinars | Medium | T1-T2 | Check for a sponsor read; classify INTERESTED and name the sponsor |
| Consultancy interviews/reports | Medium-High | T1-T2 | INTERESTED when the firm summarizes its own research or sells related services |
| Vendor technical content | Medium | T2-T3 | INTERESTED by construction; useful for product facts, not for market claims |

---

*Updated by `/add-sources`. Last updated: not yet.*
