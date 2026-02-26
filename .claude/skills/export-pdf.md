# Export PDF

Guide formatting for PDF export and save prepared files to `exports/`.

## Usage

```
/export-pdf
```

## Instructions

### 1. Check Documents

- Read `case-config.yaml` for `company_short`
- List all `.md` files in `case-study/` (excluding `.gitkeep`)
- If no documents exist, report "No documents to export" and stop

### 2. Ask Export Scope

```
Which documents do you want to export to PDF?
1. All documents (recommended)
2. Specific document(s) — tell me which
```

### 3. Format Each Document for PDF

For each document to export, create a PDF-ready version:

**Formatting steps:**
1. **Clean heading hierarchy**: Ensure H1 → H2 → H3 (no skipped levels)
2. **Table formatting**: Ensure all tables render cleanly with aligned columns
3. **Page break markers**: Insert `<!-- pagebreak -->` comments at logical section boundaries
4. **Header/footer suggestions**:
   - Header: Document title + Company name
   - Footer: "Confidential — For classroom use only" + page number
5. **Remove internal comments**: Strip any `<!-- VERIFY -->` or other development comments
6. **Consistent formatting**: Ensure quotes use proper quotation marks, em-dashes are consistent

**Do NOT change any content** — only formatting for PDF readability.

### 4. Save to Exports

Save each formatted document to `exports/`:
- `exports/{Company}_Case.md` (PDF-ready markdown)
- `exports/{Company}_Supplement.md`
- `exports/{Company}_Teaching_Note.md`
- `exports/{Company}_Additional_Sources.md`

### 5. Provide PDF Conversion Instructions

```
## PDF-Ready Files

Saved to exports/:
- exports/{Company}_Case.md
- exports/{Company}_Supplement.md
- exports/{Company}_Teaching_Note.md
- exports/{Company}_Additional_Sources.md

### Converting to PDF

**Option 1: VS Code** (recommended)
1. Open each .md file in VS Code
2. Install "Markdown PDF" extension (yzane.markdown-pdf)
3. Right-click → "Markdown PDF: Export (pdf)"

**Option 2: Pandoc** (command line)
```bash
pandoc exports/{Company}_Case.md -o exports/{Company}_Case.pdf --pdf-engine=wkhtmltopdf
```

**Option 3: Online converter**
1. Go to markdowntopdf.com or similar
2. Paste the markdown content
3. Download the PDF

**Option 4: Print from browser**
1. Open the .md file in a Markdown preview (GitHub, VS Code preview)
2. Print → Save as PDF
```

### 6. Report

```
## Export Complete

| Document | Status | Location |
|----------|--------|----------|
| Main Case | ✅ Formatted | exports/{Company}_Case.md |
| Supplement | ✅ Formatted | exports/{Company}_Supplement.md |
| Teaching Note | ✅ Formatted | exports/{Company}_Teaching_Note.md |
| Additional Sources | ✅ Formatted | exports/{Company}_Additional_Sources.md |

PDF conversion instructions provided above.
Reminder: Run /add-disclaimers before final distribution if not already done.
```

## Notes

- This skill prepares markdown for PDF conversion — it does not generate PDFs directly
- The "Convert to PDF-Ready Format" prompt in `templates/PROMPTS.md` has additional formatting guidance
- Teaching Note exports should include a "FOR INSTRUCTOR USE ONLY" header
- Remove any verification debt comments before export

## Output

Display the report directly. Save formatted files to `exports/`.
