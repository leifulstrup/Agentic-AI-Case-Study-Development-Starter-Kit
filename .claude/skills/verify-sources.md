# Verify Sources

Ensure all quotes and factual claims have proper source attribution.

## Usage

```
/verify-sources [filename]
```

If no filename provided, check all .md files in case-study/ folder.

## Instructions

1. **Identify items requiring attribution**:
   - Direct quotes (text in quotation marks or block quotes)
   - Specific statistics and numbers
   - Factual claims about events, decisions, or outcomes
   - Paraphrased statements attributed to individuals

2. **For each item, check for attribution**:
   - Is a speaker/source named?
   - Is a date or time period provided?
   - Is a publication or interview cited?
   - Can the attribution be traced to bibliography?

3. **Categorize findings**:

   **Properly attributed**: Quote + Speaker + Source + Date
   **Partially attributed**: Missing one or more elements
   **Unattributed**: No source information

4. **Generate a report**:

```
## Source Attribution Report

### Summary
- Items requiring attribution: X
- Fully attributed: X
- Partially attributed: X
- Unattributed: X

### Partially Attributed (needs enhancement)
[List with document, line, and what's missing]

### Unattributed (needs source)
[List with document, line, and recommendation]

### Bibliography Cross-Check
- Sources cited in text but missing from bibliography: [list]
- Sources in bibliography not cited in text: [list]
```

## Output

Create a log file:
- Filename: `verify-sources-YYYY-MM-DD.log`
