# Verify Quotes

Verify all quoted text can be traced to the attributed speaker in source documents.

## Usage

```
/verify-quotes [filename]
```

If no filename provided, verify quotes in all .md files in the case-study/ folder.

## Instructions

1. **Extract all quotes** from the specified document(s):
   - Block quotes (lines starting with `>`)
   - Inline quotes (text within quotation marks followed by attribution)
   - Look for attribution patterns: "—Speaker", "said Speaker", "Speaker noted"

2. **For each quote found**, record:
   - The exact quote text
   - The attributed speaker
   - The claimed source if mentioned
   - The document and line number

3. **Verify each quote**:

   **Step A - Check local source documents first:**
   - Search transcripts and PDFs in sources/ folder
   - Use fuzzy matching (quotes may be slightly paraphrased)
   - Check that speaker attribution matches

   **Step B - If not found locally, search the web:**
   - Use WebSearch to find the quote attributed to the speaker
   - Prioritize authoritative sources

4. **Generate a report** with:
   - Total quotes checked
   - Verified quotes (found with matching speaker)
   - Unverified quotes (not found or speaker mismatch)
   - Paraphrased quotes (similar content but not exact)

## Output

Create a log file:
- Filename: `verify-quotes-YYYY-MM-DD.log`
