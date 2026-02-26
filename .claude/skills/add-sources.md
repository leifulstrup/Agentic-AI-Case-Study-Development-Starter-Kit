# Add Sources

Detect new source files, collect metadata, classify into tiers, and update the Source Registry.

## Usage

```
/add-sources
```

## Instructions

### 1. Scan for Unregistered Files

- Read `sources/Source_Registry.md` to get the list of already-registered sources
- Scan all files in `sources/` and its subdirectories (`transcripts/`, `financial/`, `news/`, `reports/`)
- Exclude: `.gitkeep`, `Source_Links.md`, `Source_Registry.md`
- Identify files NOT yet listed in the Source Registry

### 2. If New Files Found

For each unregistered file, ask the user (one at a time):

**"I found `{filename}` in `sources/{subfolder}/`. Can you tell me:"**
- What is this source? (brief description)
- When was it published or accessed? (date)
- Who are the key speakers/authors?
- What key content does it contain for the case?

Then **classify the tier automatically**:
- **T1**: File is physically present in the repo AND contains full text (transcript, full article, complete report)
- **T2**: File is present but contains only excerpts, summaries, or partial content
- **T3**: Should not normally apply to files in the repo (reserved for URL-only references)

**Determine the source type** from the subfolder and content:
- `transcripts/` → Primary Interviews & Transcripts
- `financial/` → Financial Sources
- `news/` → News Coverage
- `reports/` → Industry & Analyst Reports
- Other → Other Sources

### 3. If No New Files Found

Tell the user:
```
No new unregistered files found in sources/.

You can:
1. **Drop files** into `sources/transcripts/`, `sources/financial/`, `sources/news/`, or `sources/reports/` and run `/add-sources` again
2. **Give me a URL** and I'll try to fetch it (note: some sites block automated access)
3. **Paste text** directly and I'll save it as a source file

Which would you like to do?
```

**If user provides a URL**:
- Attempt to fetch with WebFetch
- If successful: save content to appropriate `sources/` subfolder, then register it
- If blocked: explain the limitation and suggest:
  ```
  I couldn't access that URL directly. You can:
  - Open the URL in your browser and copy-paste the text here
  - Download the page as PDF and drop it in sources/
  - Use a browser extension to save the article text
  ```

**If user pastes text**:
- Ask for a filename and source metadata
- Save to appropriate `sources/` subfolder
- Register in Source Registry

### 4. Update Source Registry

After collecting metadata for all new sources:

- Add each source to the appropriate table in `sources/Source_Registry.md`
- Assign sequential numbers continuing from existing entries
- Update the **Source Summary** counts at the top of the file
- Update the "Last updated" timestamp at the bottom

### 5. Report and Suggest Next Step

```
## Sources Registered

| # | Source | Tier | Type |
|---|--------|------|------|
| {n} | {description} | T{tier} | {type} |

### Source Summary
- T1 (Primary): {count}
- T2 (Partial): {count}
- T3 (Referenced): {count}
- Total: {total}

### Suggested Next Step
{If enough sources}: Run `/assess-sources` to evaluate whether you have enough material to start writing.
{If few sources}: You may want to add more sources before assessment. See `templates/SOURCE_ACQUISITION.md` for guidance on finding sources.
```

## Notes

- This skill never asks the user to edit `Source_Registry.md` directly
- When fetching URLs, be transparent about limitations (paywalls, bot blocking)
- If user has both `Source_Links.md` (v2) and `Source_Registry.md` (v3), offer to migrate entries from the old file
- Accept natural language descriptions and parse into structured metadata

## Output

Display the report directly. No log file needed.
