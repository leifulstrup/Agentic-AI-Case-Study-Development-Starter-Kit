# Assess Bias

Analyze source composition and case study content for systematic bias in perspectives, framing, and evidence selection.

## Usage

```
/assess-bias
```

## Instructions

### 1. Gather Materials

- Read `case-config.yaml` for case context
- Read `sources/Source_Registry.md` (or `Source_Links.md`) for source metadata
- Read all source files in `sources/` subdirectories
- Read all case study documents in `case-study/`
- If no sources or documents exist, report "Nothing to assess" and stop

### 2. Source Composition Analysis

Classify each source by origin:

| Category | Definition |
|----------|-----------|
| **Company-generated** | Press releases, blog posts, investor presentations, company-sponsored content |
| **Executive voice** | Interviews with company leadership, keynotes, earnings calls |
| **Independent journalism** | News articles by journalists not sponsored by the company |
| **Academic/analyst** | Research reports, academic papers, industry analysis |
| **Employee perspective** | Employee reviews, internal communications, whistleblower reports |
| **Customer/user perspective** | Customer case studies, user reviews, testimonials |
| **Critic/skeptic perspective** | Critical analysis, short-seller reports, investigative journalism |
| **Regulatory/government** | Government reports, regulatory filings, enforcement actions |

Count sources in each category. Calculate percentages.

### 3. Bias Type Assessment

Check for each type of bias:

**Selection Bias**
- Are sources disproportionately from one perspective?
- Are there important stakeholder groups with no representation?
- Were sources chosen to support a particular narrative?

**Survivorship Bias**
- Does the case only tell the success story?
- Are failures, setbacks, or abandoned initiatives mentioned?
- Are competitors who tried similar approaches and failed discussed?

**Framing Bias**
- Is language consistently positive/negative about the protagonist's decisions?
- Are challenges presented as obstacles overcome (triumphant framing) or genuine dilemmas?
- Does the case present the protagonist's strategy as obviously correct?

**Authority Bias**
- Are executive claims taken at face value without independent verification?
- Are impressive-sounding statistics verified against primary sources?
- Is the protagonist's self-assessment balanced with external perspectives?

**Recency Bias**
- Are recent developments given disproportionate weight?
- Is historical context adequately represented?
- Are long-term consequences considered alongside short-term results?

### 4. Quote Balance Analysis

From case study documents, count:
- Total quotes by speaker
- Quotes from company insiders vs. outsiders
- Quotes that support the protagonist's strategy vs. challenge it
- Unattributed claims that favor one perspective

### 5. Missing Perspectives Check

For the specific case, identify which perspectives are absent:
- Employees affected by decisions
- Customers/users
- Competitors
- Regulators
- Critics or skeptics
- Community members
- Investors with dissenting views
- Industry peers with different approaches

### 6. Generate Report

```
# Bias Assessment Report

Generated: [date]
Case: [company_name] — [topic]

## Source Composition

| Perspective | Count | % of Total | Assessment |
|-------------|-------|-----------|------------|
| Company-generated | X | X% | ⚠️ High / ✅ OK |
| Executive voice | X | X% | |
| Independent journalism | X | X% | |
| Academic/analyst | X | X% | |
| Employee | X | X% | |
| Customer/user | X | X% | |
| Critic/skeptic | X | X% | |
| Regulatory | X | X% | |

**Company vs. Independent ratio**: X:Y
**Bias risk from source composition**: LOW / MEDIUM / HIGH

## Bias Type Assessment

| Bias Type | Risk Level | Evidence |
|-----------|-----------|---------|
| Selection | LOW/MED/HIGH | [brief explanation] |
| Survivorship | LOW/MED/HIGH | [brief explanation] |
| Framing | LOW/MED/HIGH | [brief explanation] |
| Authority | LOW/MED/HIGH | [brief explanation] |
| Recency | LOW/MED/HIGH | [brief explanation] |

## Quote Balance

| Speaker/Category | Quotes | Favorable | Neutral | Critical |
|-----------------|--------|-----------|---------|----------|
| [Protagonist] | X | X | X | X |
| [Other insider] | X | X | X | X |
| [External voice] | X | X | X | X |
| **Total** | **X** | **X** | **X** | **X** |

## Missing Perspectives

{For each missing perspective:}
- **[Perspective]**: Not represented in sources or case documents
  - Why it matters: [explanation]
  - How to address: [specific source suggestion]

## Overall Bias Assessment

**Risk Level**: LOW / MEDIUM / HIGH

**Summary**: [2-3 sentence assessment]

## Recommendations

### Must Address (before publication)
- [Critical bias issues that undermine case quality]

### Should Address (strengthens the case)
- [Moderate bias issues with specific remedies]

### Acknowledge (acceptable for classroom use)
- [Minor issues that can be noted rather than fixed]
- [Suggest adding a "Limitations" note to teaching materials]
```

## Notes

- This skill was motivated by real testing: a Moderna case had 8 of 14 sources Moderna-generated, no employee voice, and no critic perspective
- Some bias is unavoidable in case studies (protagonist's voice is deliberately centered), but the Teaching Note should acknowledge limitations
- A high bias score doesn't mean the case is unusable — it means the instructor should be aware and may want to supplement with additional classroom materials
- For public policy cases, check for partisan/ideological balance as well

## Output

Display the report directly. Also save to `assess-bias-YYYY-MM-DD.log`.
