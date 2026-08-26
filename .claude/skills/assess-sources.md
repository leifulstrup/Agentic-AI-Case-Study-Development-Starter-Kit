# Assess Sources

Evaluate the source materials in `sources/` and produce a Source Assessment Report with tier breakdown and go/no-go recommendation.

## Usage

```
/assess-sources
```

## Instructions

1. **Read configuration**: Load `case-config.yaml` to understand the case topic, company, and protagonist.

2. **Read source registry**: Load `sources/Source_Registry.md` for registered sources with tiers. Also scan `sources/` subdirectories for any files not yet registered (suggest running `/add-sources` first if unregistered files are found).

3. **If using legacy format**: If `Source_Registry.md` doesn't exist but `Source_Links.md` does, use that instead and note that `/add-sources` should be run to create the registry.

4. **Compile source tier breakdown**:

   Count sources by tier:
   - **T1 (Primary)**: Full-text sources physically in repo
   - **T2 (Partial)**: Partial text, paywalled, or search-derived
   - **T3 (Referenced)**: Cited but not in repo

   Count sources by type:
   - Primary interviews/transcripts
   - Financial documents
   - News articles
   - Industry/analyst reports
   - Other

5. **Evaluate across four dimensions** (1-5 score each):

   **Depth** (1-5):
   - Are there primary sources with the protagonist's own words?
   - Do sources include first-person accounts of key decisions?
   - Is there enough detail to reconstruct the decision-making process?
   - Can we attribute specific quotes to specific people and dates?

   **Breadth** (1-5):
   - How many distinct source types? (interviews, financials, news, reports, filings)
   - Are multiple perspectives represented? (executive, industry, customer, employee)
   - Is there competitive/industry context beyond the focal company?
   - Do sources span the relevant time period?

   **Reliability** (1-5):
   - Are sources from authoritative publications or first-party records?
   - Are sources dated and verifiable?
   - Can key claims be cross-referenced across multiple sources?
   - What proportion are T1 vs T2/T3?

   **Completeness** (1-5):
   - Enough for Additional Sources document? (quotes, data, timeline, bibliography)
   - Enough for Main Case? (protagonist, decisions, tension, outcomes)
   - Enough for Supplement? (industry context, competitive landscape, frameworks)
   - Enough for Teaching Note? (discussion questions, multiple valid perspectives)

6. **Apply go/no-go gate** per dimension:
   - **GREEN** (score 4-5): Strong, ready to proceed
   - **YELLOW** (score 3): Adequate but would benefit from more sources
   - **RED** (score 1-2): Insufficient, must improve before writing

   **Then compute the independence ratio and apply it as a cap on the overall
   gate.** Independence is not a fifth dimension to be averaged with the others —
   it is a ceiling on what the average is allowed to conclude:

   ```
   independent_share = INDEPENDENT sources / total citable sources
   ```

   | independent_share | Overall gate may not exceed |
   |-------------------|-----------------------------|
   | 0 | **RED** — blocking, regardless of count |
   | below 1/5 (20%) | **RED** |
   | 1/5 to 1/3 | **YELLOW** — the outcome/impact layer stays blocked |
   | above 1/3 | no cap; the dimension average stands |

   State the computed share and the cap it triggers as a line in the report, even
   when no cap binds. **A base can be deep and one-sided at the same time, and the
   dimension average cannot see the difference.** Depth and Completeness both reward
   volume, so a subject who publishes prolifically about themselves scores high on
   two of four dimensions and pulls the average to YELLOW while Reliability is RED
   and the base is four-fifths their own material. That case occurred: 33 sources,
   about 82% self and company, correctly described in prose as one-sided — and it
   passed, because describing is not gating.

   **Two failure modes, not one.** A thin base fails for scarcity: few sources, RED
   on Breadth and Completeness, obvious. A one-sided base fails for concentration:
   many sources, high Depth, and no independent check on any factual claim. The
   second looks like progress and is the harder one to catch, so it needs the
   arithmetic rather than the judgment.

   **Separate the two kinds of claim before deciding what the cap blocks.** Self and
   company sources are legitimate evidence of *what the subject thinks* — the
   narrative of reasoning, the decisions, the stated strategy. They are not evidence
   of *outcomes, market facts, or firm scale*. A capped YELLOW may proceed with the
   reasoning narrative while the outcome layer stays blocked; say which is which.

7. **Check source integrity** (processing status and independence — do this before the gates):

   **Processing check.** For every T1 source, scan the document for evidence of how the text was produced:
   - Editorial notes: "edited for clarity and length", "condensed", "lightly edited", "excerpts from"
   - ASR artifacts: no speaker labels, no sentence punctuation, run-on paragraphs, garbled proper nouns and technical terms
   - PDF extraction artifacts: column bleed, header/footer intrusion

   A source that is EDITED or ASR remains T1 for *access*, but **cannot support verbatim quotation**. Flag each one explicitly:
   ```
   ⚠ {source} is an {edited transcript / uncorrected ASR transcript}. It is T1 for access,
   but quotations from it must not be presented as verbatim. Use indirect speech, or quote
   with an explicit note about the source's processing status.
   ```
   Downgrade the **Reliability** score by at least one point if more than one T1 source carrying quotations is EDITED or ASR without audio available for adjudication.

   **Independence check.** For each source, establish who produced it and what they gain. Look for sponsor reads, disclosure statements, author affiliation, and whether the producer sells services related to the subject. Classify INDEPENDENT / INTERESTED / COMPANY / UNKNOWN and name the specific interest.

   Report:
   ```
   | Source | Tier | Independence | Specific interest | Processing |
   ```
   If no source is INDEPENDENT, that is a blocking gap regardless of how many sources exist — say so.

   **Presence is not proportion.** One independent source among forty clears a
   floor-of-one test as easily as one among three, and the floor was the only
   independence rule this gate applied for several versions. Report the computed
   `independent_share` (step 6) alongside the raw count, and apply its cap.

8. **Check minimum viable source gate**:
   - At least 1 T1 primary source with protagonist's voice (interview, podcast, keynote)
   - At least 1 T1 financial source (10-K, earnings, investor presentation)
   - At least 2 news/industry sources from different publications
   - If any minimum not met, flag as blocking gap

9. **Early bias detection**:
   - Count sources by origin: company-generated vs. independent
   - If >50% from single perspective (e.g., all company PR), flag bias risk
   - Note missing perspectives: employee, customer, critic, regulator, competitor

10. **Identify gaps**: For each dimension scoring below 4, list specific types of sources that would improve the score, with concrete search suggestions.

11. **Generate report**:

```
# Source Assessment Report

Generated: [date]
Case: [company_name] — [topic]

## Source Tier Breakdown

| Tier | Count | Sources |
|------|-------|---------|
| T1 — Primary (in repo) | X | [list] |
| T2 — Partial | X | [list] |
| T3 — Referenced only | X | [list] |
| **Total** | **X** | |

## Source Type Distribution

| Type | Count | T1 | T2 | T3 |
|------|-------|----|----|----|
| Primary Interviews | X | X | X | X |
| Financial Documents | X | X | X | X |
| News Coverage | X | X | X | X |
| Industry Reports | X | X | X | X |
| Other | X | X | X | X |

## Assessment Scores

| Dimension | Score | Gate | Summary |
|-----------|-------|------|---------|
| Depth | X/5 | GREEN/YELLOW/RED | [one-line summary] |
| Breadth | X/5 | GREEN/YELLOW/RED | [one-line summary] |
| Reliability | X/5 | GREEN/YELLOW/RED | [one-line summary] |
| Completeness | X/5 | GREEN/YELLOW/RED | [one-line summary] |
| **Overall** | **X/5** | **[gate]** | |

## Source Integrity

| Source | Tier | Independence | Specific interest | Processing |
|--------|------|--------------|-------------------|------------|

- Independent sources: X of Y — **independent_share = Z%**, cap: [RED / YELLOW / none]
- Sources that cannot support verbatim quotation (EDITED/ASR): X — [list]
- **Integrity flags**: [any source whose independence or processing was missed by earlier registration]

## Minimum Viable Source Check

| Requirement | Status | Details |
|-------------|--------|---------|
| T1 primary with protagonist voice | MET/NOT MET | [details] |
| T1 financial source | MET/NOT MET | [details] |
| 2+ news/industry from different pubs | MET/NOT MET | [details] |

## Bias Check

- Company-generated sources: X of Y (Z%)
- Independent sources: X of Y (Z%)
- **Bias risk**: [LOW/MEDIUM/HIGH]
- Missing perspectives: [list]

## Strengths
- [What's strong about the current sources]

## Gaps and Recommendations

### HIGH PRIORITY (blocking — must fix before writing)
- [Sources needed before writing can begin]

### MEDIUM PRIORITY (would strengthen the case)
- [Sources that would improve quality]

### NICE TO HAVE
- [Sources that would add depth]

## Go / No-Go Recommendation

**[GREEN: Ready to write / YELLOW: Can proceed with caution / RED: Need more sources first]**

[Explanation of recommendation]

## Suggested Next Steps
1. [Specific action with search terms or URLs]
2. [Specific action]
3. [Specific action]
```

## Output

Display the report directly. Also save to `assess-sources-YYYY-MM-DD.log`.
