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

Then **classify independence** — who produced this, and what do they gain? Read the document itself for evidence: sponsor reads ("this episode is brought to you by…"), editorial notes, author affiliation, disclosure statements, and whether the producer sells something related to the subject.

- **INDEPENDENT** — no commercial, employment, or personal stake in how the subject is portrayed
- **INTERESTED** — producer has a stake (consultancy summarizing its own report; sponsored episode; vendor content; interviewer with a long tie to the subject; firm selling related services)
- **COMPANY** — produced or controlled by the case subject
- **UNKNOWN** — could not establish; treat as INTERESTED until resolved

Record the *specific* interest, not just the label — "INTERESTED — episode sponsored by [vendor]" is useful; "INTERESTED" alone is not. Independence is **independent of tier**: a full-text vendor-sponsored transcript is T1 and INTERESTED at the same time.

Then **classify processing status** — how did this text reach its current form? Scan for editorial notes and transcription artifacts:

- **VERBATIM** — official transcript, published article text, filing
- **EDITED** — the source says so (e.g., "this interview has been edited for clarity and length"). **Flag loudly**: this source cannot support verbatim quotation
- **ASR** — machine speech-to-text, uncorrected, no audio available (tell-tale signs: garbled proper nouns, no speaker labels, no punctuation structure, run-on text)
- **EXTRACTED** — text pulled from PDF

If a source is EDITED or ASR, say so to the user at registration time, not later:
```
Note: {source} states it was edited for clarity and length. It's still T1 for access,
but quotations from it cannot be presented as verbatim. I'll flag this in the registry
and use indirect speech unless you want to quote it with an explicit "edited transcript" note.
```

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

- Add each source to the appropriate table in `sources/Source_Registry.md`, filling the **Independence** column with label + specific interest
- Record processing status (VERBATIM / EDITED / ASR / EXTRACTED) in the Key Content column or a note
- Assign sequential numbers continuing from existing entries
- Update the **Source Summary** counts at the top of the file
- Update the "Last updated" timestamp at the bottom

### 5. Report and Suggest Next Step

```
## Sources Registered

| # | Source | Tier | Independence | Processing | Type |
|---|--------|------|--------------|------------|------|
| {n} | {description} | T{tier} | {label — specific interest} | {status} | {type} |

### Source Summary
- T1 (Primary): {count}
- T2 (Partial): {count}
- T3 (Referenced): {count}
- Total: {total}

### Suggested Next Step
{If enough sources}: Run `/assess-sources` to evaluate whether you have enough material to start writing.
{If few sources}: You may want to add more sources before assessment. See `templates/SOURCE_ACQUISITION.md` for guidance on finding sources.
```

## The raw capture is the source; a reading of it is not

When a source is read live — a page fetched in a browser, a profile scrolled, a
result set gathered by a delegated search — **save the captured text to a file in
`sources/` before registering it, and register the file rather than the reading.**

The failure this prevents: research delegated to subagents or read through a browser
comes back as a *dossier* — an accurate, useful digest written by the agent that read
the page. The digest paraphrases. The exact wording stays in the session transcript
and is gone when the session ends. Quotations drawn from it then trace to nothing,
not because anyone fabricated anything, but because **the only artifact that ever
held the verbatim text was never a file.** This produced real quote defects in field
testing, in a case whose verification had otherwise passed.

So, when registering anything read live:

1. Write the raw capture to `sources/reports/<slug>-capture-YYYY-MM-DD.md` (or the
   fitting subdirectory) with a provenance header: URL, access date, how it was
   retrieved, and whether the text is VERBATIM, EXTRACTED, or ASR.
2. Register **that file**. The dossier or summary, if kept, is a working note — not
   a registered source, and never the target of a citation.
3. If only a summary exists and the original can no longer be reached, register it
   as **T3 (referenced)** and record that no verbatim text is held. Nothing may be
   quoted from it.

A source you cannot re-read is a source you cannot verify. Chain of custody for a
quotation runs page → committed file → document, and a hop that exists only in a
session breaks it.

## Notes

- This skill never asks the user to edit `Source_Registry.md` directly
- When fetching URLs, be transparent about limitations (paywalls, bot blocking)
- If user has both `Source_Links.md` (v2) and `Source_Registry.md` (v3), offer to migrate entries from the old file
- Accept natural language descriptions and parse into structured metadata

## Output

Display the report directly. No log file needed.
