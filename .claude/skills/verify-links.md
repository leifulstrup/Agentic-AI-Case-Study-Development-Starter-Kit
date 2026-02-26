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
   - Redirected links

4. **For each problem**, provide:
   - Document and line where link appears
   - Expected content vs. found
   - Suggested fix

## Output

Create a log file:
- Filename: `verify-links-YYYY-MM-DD.log`
