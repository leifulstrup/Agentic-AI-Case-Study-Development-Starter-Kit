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
   - Prioritize authoritative and primary sources
   - **Trace to the primary source.** Quote-aggregator sites copy each other — a quote appearing on three quote websites is NOT verification. Find the original interview, transcript, filing, or article.

4. **Assign each quote a confidence verdict**:

   | Verdict | Meaning | Evidence required |
   |---------|---------|-------------------|
   | **VERIFIED** | Exact quote found in a T1 source | Source file + line number or timestamp |
   | **LIKELY** | Close paraphrase, or found only in T2/secondary coverage | Excerpt + source link |
   | **DISPUTED** | Sources conflict on wording, speaker, or date | Both conflicting citations shown |
   | **APOCRYPHAL** | Circulates but no primary source found | Summary of the search trail |

5. **Apply the publication rule**:
   - Only **VERIFIED** quotes may appear inside quotation marks.
   - **LIKELY** quotes must be rewritten as indirect speech ("Waldron noted that...") or upgraded by locating the primary source.
   - **DISPUTED** and **APOCRYPHAL** quotes must be logged to `verification-debt.yaml` and either resolved or removed before publication.

6. **Generate a report** with:
   - Total quotes checked
   - Count by verdict (VERIFIED / LIKELY / DISPUTED / APOCRYPHAL)
   - For each non-VERIFIED quote: the quote, its verdict, the evidence found, and the recommended fix
   - Items added to verification debt

## Output

Create a log file:
- Filename: `verify-quotes-YYYY-MM-DD.log`
