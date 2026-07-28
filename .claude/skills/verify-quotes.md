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

   **Step 0 - Establish the source's processing status.** Check `sources/Source_Registry.md` (and the source document itself) for whether it is VERBATIM, EDITED, ASR, or EXTRACTED. A quote from an EDITED or ASR source can never be VERIFIED — the best available verdict is MODIFIED.

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
   | **VERIFIED** | Exact quote found in a VERBATIM source, correct speaker | Source file + line number or timestamp |
   | **MODIFIED** | The speaker's words, but altered in assembly or presentation | The source text beside the quoted text |
   | **LIKELY** | Close paraphrase, or found only in T2/secondary coverage | Excerpt + source link |
   | **DISPUTED** | Sources conflict on wording, speaker, or date | Both conflicting citations shown |
   | **APOCRYPHAL** | Circulates but no primary source found | Summary of the search trail |

   **MODIFIED** covers the failure classes that look verbatim but aren't. Check every quote for all five:
   - **Spliced** — two passages from different parts of the source joined inside one quotation
   - **Silently corrected** — a word fixed without brackets (common with ASR sources)
   - **Smoothed** — disfluencies or filler removed without ellipsis
   - **Edited-source quotation** — the words come from a source that states it was edited for clarity/length, so they are the editor's arrangement, not the speaker's exact words
   - **Assent converted to assertion** — an interviewer stated the figure or claim and the subject agreed; the case presents it as the subject's own statement

5. **Apply the publication rule**:
   - Only **VERIFIED** quotes may appear inside quotation marks.
   - **MODIFIED** quotes must be repaired: restore the source wording, split a splice into separate quotations, add brackets around corrections, or convert to indirect speech. An edited-source quotation stays only if the document states the source was edited.
   - **LIKELY** quotes must be rewritten as indirect speech ("Doe noted that...") or upgraded by locating the primary source.
   - **DISPUTED** and **APOCRYPHAL** quotes must be logged to `verification-debt.yaml` and either resolved or removed before publication.
   - **Check the document's own integrity claims.** If any document asserts that all quotations are verbatim while any quote is MODIFIED — or while any quoted source is EDITED or ASR — that assertion is itself a defect. Report it.

6. **Generate a report** with:
   - Total quotes checked
   - Count by verdict (VERIFIED / MODIFIED / LIKELY / DISPUTED / APOCRYPHAL)
   - For each non-VERIFIED quote: the quote, its verdict, the evidence found, and the recommended fix
   - Items added to verification debt

## Output

Create a log file:
- Filename: `verify-quotes-YYYY-MM-DD.log`
