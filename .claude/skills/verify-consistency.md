# Verify Consistency

Check that key data points, statistics, and facts are consistent across all case study documents. Updates verification debt when inconsistencies are found.

## Usage

```
/verify-consistency
```

## Instructions

1. **Determine company name and find documents**:
   - Read `case-config.yaml` and extract `case.company_short`
   - List all `.md` files in `case-study/` directory
   - Expected files: `{company_short}_Case.md`, `{company_short}_Supplement.md`,
     `{company_short}_Teaching_Note.md`, `{company_short}_Additional_Sources.md`
   - If `case-study/` is empty or only has `.gitkeep`, skip to report and output:
     "No case study documents found in case-study/. Run `/write-document` to create documents."

2. **Extract key data points** from each document:
   - Financial figures (revenue, profit, investment amounts, savings)
   - Headcounts and percentages (employees, adoption rates, user counts)
   - Dates and timelines (launch dates, milestones)
   - Named statistics (specific metrics mentioned)
   - Framework terminology (ensure consistent naming)

3. **Cross-reference each data point**:
   - Flag any inconsistencies where the same metric differs across documents
   - Note which document has which value
   - Check against source documents to determine correct value

4. **Check framework consistency**:
   - Key concepts - same in all documents?
   - Key terminology - spelled and capitalized consistently?

5. **Check against verification debt**:
   - Read `verification-debt.yaml` (if it exists)
   - For data points being verified, check if related debt items exist
   - If new inconsistencies found, add them to `verification-debt.yaml`:
     ```yaml
     - claim: "[the inconsistent data point]"
       document: "[documents involved]"
       source_needed: "Verify correct value against primary source"
       status: flagged
       date_added: "[today's date]"
     ```

6. **Generate a report** with:

```
## Consistency Verification Report

Generated: [date]
Case: [company_name]

### Data Points Checked
| Metric | Case | Supplement | Teaching Note | Sources | Status |
|--------|------|------------|---------------|---------|--------|

### Inconsistencies Found
[List each inconsistency with document locations and recommended fix]

### Framework Terminology
| Term | Consistent? | Notes |
|------|-------------|-------|

### Verification Debt Updated
- New items added: X
- Existing items checked: Y
- Total open debt items: Z

### Recommendations
[Prioritized list of fixes]
```

## Output

Create a log file in the repository root:
- Filename: `verify-consistency-YYYY-MM-DD.log`
- Log files are excluded from git via .gitignore
