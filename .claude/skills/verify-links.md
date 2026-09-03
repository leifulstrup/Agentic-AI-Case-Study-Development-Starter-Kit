# Verify Links

Validate all external URLs in case study documents.

## Usage

```
/verify-links [filename]
```

If no filename provided, verify links in all .md files.

## Instructions

1. **Extract all URLs** from the specified document(s):
   - Markdown links: `[text](url)`
   - Raw URLs: `https://...`
   - Reference-style links

2. **For each URL found**:
   - Record the URL and context
   - Use WebFetch to check accessibility
   - Verify page contains expected content

3. **Generate a report** with:
   - Total links checked
   - Working links (with expected content)
   - Working links (content mismatch)
   - Broken links (404, timeout)

   **Sort the failures — they are not the same finding.** A URL that answered is not a URL
   that is gone, and reporting them together tells the author nothing about what to do.

   | What happened | Verdict | What it means |
   |---|---|---|
   | 200, content matches the citation | **OK** | Nothing to do |
   | **403 / 429 / login wall / bot check** | **BLOCKED — not verified, not broken** | The host answered and refused. The source may be perfectly fine; you could not check it from here |
   | 404, 410, DNS failure | **DEAD** | A real defect. The citation points at nothing |
   | No network at all | **NOT RUN** | You did not look. Blocks publication |

   **BLOCKED is the common case and the kit previously had no word for it.** In a real run,
   `cnbc.com` returned 403 and `youtu.be` returned 429 — both live, both refusing automated
   requests. Reporting those as "broken" would send an author hunting for a replacement
   source that is not actually missing; reporting them as "checked" would claim a
   verification that did not happen.

   For each BLOCKED link: say the host answered, give the status code, and tell the author
   this one needs a human with a browser. That is a thirty-second task they can do and you
   cannot. **Do not retry in a loop and do not work around a bot check** — that is what the
   403 is for.

   A run where every link is BLOCKED is **not** a clean link check. Report the check as
   NOT RUN with the blocked count, so the pre-publication checklist stays honest.
   - Redirected links

4. **For each problem**, provide:
   - Document and line where link appears
   - Expected content vs. found
   - Suggested fix

## Output

Create a log file:
- Filename: `verify-links-YYYY-MM-DD.log`
