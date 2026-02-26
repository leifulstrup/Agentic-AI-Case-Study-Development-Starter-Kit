# Verify Cross-Document

Check structural alignment and content references across the four case study documents.

## Usage

```
/verify-cross-document
```

## Instructions

### 1. Load Documents

- Read all `.md` files in `case-study/` (excluding `.gitkeep`)
- If fewer than 2 documents exist, report "Need at least 2 documents for cross-document verification" and stop
- Read `case-config.yaml` for case context

### 2. Teaching Note ↔ Main Case Alignment

If both exist, check:

- **Discussion questions reference actual case content**: Each discussion question in the Teaching Note should relate to specific events, data, or tensions in the Main Case. Flag any question that references content not in the case.
- **Learning objectives are supported**: Each learning objective should be achievable from the case content alone. Flag objectives that require information not present.
- **Timeline alignment**: Events referenced in the Teaching Note discussion guide appear in the case.
- **Character references**: People mentioned in the Teaching Note exist in the case.
- **Timing feasibility**: Do the Teaching Note's discussion sections fit within the configured session length?

### 3. Supplement ↔ Main Case Alignment

If both exist, check:

- **Frameworks applied**: Frameworks introduced in the Supplement should be referenced or applicable in the Teaching Note analysis. Flag orphan frameworks.
- **Technical terms defined**: Technical terms used in the Main Case should be defined in the Supplement glossary. Flag undefined terms.
- **Industry data supports case**: Industry context in the Supplement should be relevant to the case narrative. Flag disconnected sections.
- **Competitive landscape matches**: Competitors mentioned in the case appear in the Supplement's competitive analysis.

### 4. Teaching Note ↔ Supplement Alignment

If both exist, check:

- **Frameworks in analysis**: Frameworks from the Supplement should appear in the Teaching Note's board plans or analysis sections.
- **Assessment questions**: Assessment options should be answerable using case + supplement content.

### 5. Additional Sources ↔ All Documents

If the Additional Sources document exists:

- **Bibliography completeness**: Sources cited in other documents should appear in the Additional Sources bibliography.
- **Quote traceability**: Key quotes in the Main Case should have corresponding excerpts in Additional Sources.
- **Data point traceability**: Financial figures in any document should trace to exhibits in Additional Sources.

### 6. Generate Report

```
# Cross-Document Verification Report

Generated: [date]
Case: [company_name]
Documents checked: [list]

## Teaching Note ↔ Main Case

| Check | Status | Details |
|-------|--------|---------|
| Discussion questions reference case content | ✅/⚠️/🔴 | X of Y questions verified |
| Learning objectives supported by case | ✅/⚠️/🔴 | [details] |
| Timeline alignment | ✅/⚠️/🔴 | [details] |
| Character references match | ✅/⚠️/🔴 | [details] |
| Session timing feasible | ✅/⚠️/🔴 | [total minutes vs configured] |

## Supplement ↔ Main Case

| Check | Status | Details |
|-------|--------|---------|
| Frameworks applicable | ✅/⚠️/🔴 | X of Y frameworks used |
| Technical terms defined | ✅/⚠️/🔴 | X undefined terms |
| Industry context relevant | ✅/⚠️/🔴 | [details] |
| Competitive landscape matches | ✅/⚠️/🔴 | [details] |

## Teaching Note ↔ Supplement

| Check | Status | Details |
|-------|--------|---------|
| Frameworks in analysis | ✅/⚠️/🔴 | [details] |
| Assessment answerable | ✅/⚠️/🔴 | [details] |

## Additional Sources ↔ All

| Check | Status | Details |
|-------|--------|---------|
| Bibliography complete | ✅/⚠️/🔴 | X sources cited, Y in bibliography |
| Quotes traceable | ✅/⚠️/🔴 | [details] |
| Data points traceable | ✅/⚠️/🔴 | [details] |

## Issues Found

### Must Fix
- [Critical alignment issues]

### Should Review
- [Items that may be intentional but should be confirmed]

## Summary

| Category | Pass | Warn | Fail |
|----------|------|------|------|
| Structural alignment | X | X | X |
| Content references | X | X | X |
| Completeness | X | X | X |
```

## Notes

- This skill checks structural relationships, not data consistency (that's `/verify-consistency`)
- It's normal for not every framework in the Supplement to appear in the Teaching Note — but orphaned frameworks should be reviewed
- Session timing is checked against `documents.session_length_minutes` in `case-config.yaml`

## Output

Display the report directly. Also save to `verify-cross-document-YYYY-MM-DD.log`.
