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

7. **Check minimum viable source gate**:
   - At least 1 T1 primary source with protagonist's voice (interview, podcast, keynote)
   - At least 1 T1 financial source (10-K, earnings, investor presentation)
   - At least 2 news/industry sources from different publications
   - If any minimum not met, flag as blocking gap

8. **Early bias detection**:
   - Count sources by origin: company-generated vs. independent
   - If >50% from single perspective (e.g., all company PR), flag bias risk
   - Note missing perspectives: employee, customer, critic, regulator, competitor

9. **Identify gaps**: For each dimension scoring below 4, list specific types of sources that would improve the score, with concrete search suggestions.

10. **Generate report**:

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
