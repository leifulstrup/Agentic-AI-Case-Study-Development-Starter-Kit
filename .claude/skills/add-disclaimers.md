# Add Disclaimers

Add standardized AI-generated content disclaimers and methodology notes to case study documents.

## Usage

```
/add-disclaimers
```

## Instructions

### 1. Check Context

- Read `case-config.yaml` for company name and course info
- Read `case-study/` for existing documents
- If no documents exist, report "No documents to add disclaimers to" and stop

### 2. Ask Disclaimer Context

Ask the user:
```
What context will these documents be used in?
1. Classroom use only (standard academic disclaimer)
2. Draft for review (includes "DRAFT" watermark language and verification notes)
3. Publication-ready (formal disclaimer with full methodology)
```

### 3. Apply Disclaimers

For each document in `case-study/`:

#### Header Disclaimer (top of document, after title)

**Classroom use**:
```markdown
> **AI-Assisted Case Study**: This case study was developed with AI assistance using the
> Agentic AI Case Study Development methodology. All quotes and data points have been
> sourced from publicly available materials. This case is intended for classroom
> discussion and is not intended to serve as an endorsement, source of primary data,
> or illustration of effective or ineffective management.
```

**Draft for review**:
```markdown
> **DRAFT — AI-Assisted Case Study**: This is a working draft developed with AI
> assistance. Quotes, data points, and claims are being verified against source
> documents. Items marked with `<!-- VERIFY -->` comments require additional
> source confirmation before publication.
```

**Publication-ready**:
```markdown
> **AI-Assisted Case Study**: This case study was developed using AI-assisted research
> and writing tools as part of the Agentic AI Case Study Development methodology
> (v3.0). All factual claims, quotes, and data points have been verified against
> primary source documents. The case is intended for educational discussion purposes.
> It does not represent the views of [company_name] or any individuals mentioned herein.
```

#### Footer Disclaimer (end of document, before bibliography if present)

```markdown
---

### About This Case

**Prepared for**: [course_name] at [institution], [semester]
**Development methodology**: Agentic AI Case Study Development Starter Kit v3.0
**AI tools used**: [Claude Code / ChatGPT / etc. — ask user]
**Source verification**: All quotes and data points traced to dated, publicly available sources
**Date completed**: [today's date]
```

#### AI Methodology Note (Additional Sources document only)

Add a section to the Additional Sources document:

```markdown
## AI Development Methodology Note

This case study package was developed using the Agentic AI Case Study Development
methodology, which combines human research judgment with AI-assisted writing and
verification. The development process included:

1. **Source Collection**: Human researcher identified and gathered primary sources
   including interviews, financial reports, news articles, and industry analyses.

2. **AI-Assisted Analysis**: AI tools helped extract key quotes, data points,
   and themes from source materials.

3. **AI-Assisted Writing**: Case documents were drafted with AI assistance,
   following HBR-style case study conventions.

4. **Verification Procedures**:
   - Quote verification: All quoted text traced to source documents
   - Data consistency: Financial figures cross-checked across documents
   - Source attribution: All claims attributed to dated sources
   - Bias assessment: Source composition analyzed for perspective balance

5. **Quality Checks Performed**:
   - [List verification skills run and dates]
   - Verification debt items resolved: [count]

### Limitations

- Primary sources are limited to publicly available materials
- No direct interviews were conducted with company personnel
- AI-generated analysis may reflect biases in training data
- Financial projections and forward-looking statements reflect source material as of [date]
```

### 4. Report Changes

```
## Disclaimers Added

| Document | Header | Footer | Methodology Note |
|----------|--------|--------|-----------------|
| [filename] | ✅ Added | ✅ Added | N/A |
| [Additional Sources] | ✅ Added | ✅ Added | ✅ Added |

Context: [classroom / draft / publication-ready]

All disclaimers are standardized. To change the context level, run /add-disclaimers again.
```

## Notes

- If disclaimers already exist in a document, ask before overwriting
- The methodology note only goes in the Additional Sources document
- The user should confirm which AI tools were used for the methodology note
- For public policy cases, adjust language: "management" → "decision-making" in the header disclaimer

## Output

Display the report directly. No log file needed.
