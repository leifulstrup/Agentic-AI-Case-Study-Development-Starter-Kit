# Validate Financials

Extract all financial figures from case study documents, check arithmetic, and cross-reference against source documents.

## Usage

```
/validate-financials
```

## Instructions

### 1. Gather Documents

- Read all `.md` files in `case-study/` (excluding `.gitkeep`)
- Read all files in `sources/financial/`
- Read `sources/Source_Registry.md` for financial source references
- If no case study documents exist, report "No documents to validate" and stop

### 2. Extract Financial Figures

From each case study document, extract:
- **Dollar amounts**: Revenue, profit, investment, cost, market cap, funding, etc.
- **Percentages**: Growth rates, margins, market share, adoption rates, etc.
- **Counts**: Employees, users, customers, products, etc.
- **Dates with financial context**: Fiscal years, quarter references, etc.

For each figure, record:
- The exact text (e.g., "$2.885 billion")
- The document and approximate location
- The claimed source (if any)

### 3. Check Arithmetic

For related figures, verify mathematical consistency:

- **Percentage calculations**: If "revenue grew from $X to $Y, a Z% increase" — does Z% match?
- **Subtotals**: Do component figures add up to stated totals?
- **Year-over-year**: Are YoY changes consistent with the base and result figures?
- **Margins**: Do margin percentages match the revenue and profit figures?
- **Per-unit calculations**: Do per-user/per-employee figures match totals and counts?

### 4. Cross-Reference Against Sources

For each financial figure:
- Search source documents for the same or related figure
- Verify the figure matches the source
- Note any discrepancies between the case document and the source
- Flag figures with no source document backing

### 5. Check Cross-Document Consistency

For financial figures appearing in multiple case study documents:
- Verify the same number appears everywhere
- Flag format inconsistencies ("$2.9B" vs "$2.885 billion" vs "$2,885 million")

### 6. Generate Report

```
# Financial Validation Report

Generated: [date]
Case: [company_name]
Documents checked: [count]

## Figures Extracted

| # | Figure | Document | Source | Status |
|---|--------|----------|--------|--------|
| 1 | $X revenue | Main Case | 10-K p.42 | ✅ Verified |
| 2 | Y% growth | Main Case | Earnings call | ⚠️ Discrepancy |
| 3 | Z employees | Supplement | None found | 🔴 Unsourced |

## Arithmetic Checks

| Calculation | Expected | Found | Status |
|-------------|----------|-------|--------|
| Revenue growth $X → $Y | Z% | W% | ✅ / 🔴 |
| Margin = Profit/Revenue | X% | Y% | ✅ / 🔴 |

## Arithmetic Errors Found
{For each error:}
- **[Description]**: [Document] states [X] but arithmetic shows [Y]
  - Source says: [what the source actually says]
  - Recommended fix: [specific correction]

## Unsourced Financial Claims
{For each unsourced figure:}
- **[Figure]** in [Document]: No source document found
  - Suggested source: [where to look]

## Cross-Document Consistency
{For each inconsistency:}
- **[Figure]**: [Doc1] says [X], [Doc2] says [Y]
  - Source says: [correct value]
  - Fix: Update [which document] to [correct value]

## Summary

| Category | Count |
|----------|-------|
| Figures checked | X |
| Verified against source | X |
| Arithmetic errors | X |
| Unsourced claims | X |
| Cross-doc inconsistencies | X |

**Status**: [Clean / Issues Found — X items need attention]
```

### 7. Update Verification Debt

For any unsourced financial claims or arithmetic errors:
- Add to `verification-debt.yaml` with status "flagged"
- Set `source_needed` to describe what source would verify the claim

## Notes

- This skill was motivated by real errors found in testing: a $2.885B arithmetic error and 27% vs 35% percentage discrepancy
- Be especially careful with percentage calculations — they are the most common error
- Format consistency matters: recommend one format per document (e.g., always "$X.X billion" not mixing "$XB" and "$X billion")

## Output

Display the report directly. Also save to `validate-financials-YYYY-MM-DD.log`.
