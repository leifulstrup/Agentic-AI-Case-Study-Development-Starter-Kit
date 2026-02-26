# Source Acquisition Guide

How to find, transcribe, and organize source materials for case study development.

---

## Overview

Strong case studies require diverse, authoritative sources:
- **Primary sources**: Direct interviews with decision-makers
- **Financial sources**: SEC filings, earnings calls, annual reports
- **News sources**: Business journalism from trusted outlets
- **Industry sources**: Analyst reports, market research

---

## Source Discovery

### Finding Primary Interview Content

**Video Sources:**
- YouTube executive interviews (conferences, podcasts)
- Company investor day presentations
- Earnings call webcasts
- TED talks and keynotes

**Audio Sources:**
- Business podcasts featuring executives
- Conference panel recordings
- Webinar archives

**Search strategies:**
```
"[executive name]" interview
"[company name]" CEO keynote
"[topic]" panel discussion [company]
"[company name]" investor day
```

### Finding Financial Data

**SEC Filings (EDGAR):**
- 10-K (annual report) - comprehensive data
- 10-Q (quarterly) - recent performance
- 8-K (current events) - significant announcements
- DEF 14A (proxy) - executive compensation, governance

**Earnings Resources:**
- Earnings call transcripts (Seeking Alpha, company IR pages)
- Earnings presentations (investor relations websites)
- Analyst day materials

### Finding Business News

**Trusted Sources:**
| Source | Strength | Access |
|--------|----------|--------|
| Wall Street Journal | Comprehensive business coverage | Subscription |
| Financial Times | Global perspective, financial depth | Subscription |
| The Economist | Strategic analysis | Subscription |
| CNBC | Quick news, video interviews | Free + subscription |
| Bloomberg | Financial data, executive interviews | Subscription |
| New York Times Business | Broader context | Subscription |
| Reuters | News wire, financials | Free |
| Company press releases | Official announcements | Free |

**Industry-Specific:**
- McKinsey Quarterly (strategy)
- Harvard Business Review (management)
- MIT Sloan Management Review (technology)
- Industry trade publications

---

## Transcription Methods

### Option 1: Google NotebookLM (Recommended)

**Best for:** YouTube videos, MP3/MP4 files

**How to use:**
1. Go to [notebooklm.google.com](https://notebooklm.google.com)
2. Create a new notebook
3. Upload source:
   - Paste YouTube URL, or
   - Upload MP3/MP4 file
4. NotebookLM generates transcript automatically
5. Export transcript to text file

**Advantages:**
- High accuracy
- Speaker identification
- Searchable within NotebookLM
- Can ask questions about content

### Option 2: OpenAI Whisper

**Best for:** Local files, privacy-sensitive content

**Setup:**
```bash
pip install openai-whisper
```

**Usage:**
```bash
whisper audio_file.mp3 --model medium --output_format txt
```

**Model options:**
- `tiny` - fastest, less accurate
- `base` - good balance
- `small` - better accuracy
- `medium` - recommended for interviews
- `large` - best accuracy, slowest

### Option 3: Otter.ai

**Best for:** Live meetings, quick transcription

**Features:**
- Real-time transcription
- Speaker identification
- Integration with Zoom/Teams
- Free tier available

### Option 4: YouTube Auto-Captions

**Best for:** Quick extraction when accuracy is less critical

**How to access:**
1. Open video on YouTube
2. Click "..." below video
3. Select "Show transcript"
4. Copy text

**Note:** Auto-captions have errors; always verify quotes.

### Option 5: Manual Transcription

**When necessary:**
- Audio quality is poor
- Technical terminology needs precision
- Legal/compliance requirements

**Best practices:**
- Use 0.75x playback speed
- Timestamp every 2-3 minutes
- Mark unclear sections with [inaudible] or [?]
- Note speaker changes

---

## Organizing Source Materials

### File Naming Convention

```
[Source]_[Speaker/Topic]_[Type].[ext]

Examples:
- McKinsey_Waldron_Interview.pdf
- Bloomberg_Dimon_Interview.txt
- CNBC_JPMorgan_AI_Blueprint.pdf
- JPMorgan_Q3_2025_Earnings.pdf
- VentureBeat_Interview_Transcript.txt
```

### Folder Structure

```
sources/
├── transcripts/           # Interview transcripts
│   ├── VentureBeat_Interview_Transcript.txt
│   └── Bloomberg_Dimon_Interview.txt
├── financial/             # SEC filings, earnings
│   ├── JPMorgan_10K_2025.pdf
│   └── JPMorgan_Q3_2025_Earnings.pdf
├── news/                  # News articles
│   ├── CNBC_JPMorgan_AI_Blueprint.pdf
│   └── WSJ_AI_Banking_Analysis.pdf
├── reports/               # Analyst/industry reports
│   └── McKinsey_Waldron_Interview.pdf
└── Source_Links.md        # URLs and references
```

### Source_Links.md Template

```markdown
# Source Links and References

## Primary Interviews

### [Interview Name]
- **URL**: [full URL]
- **Date**: [date accessed]
- **Duration**: [if video/audio]
- **Key speakers**: [names and titles]
- **Local file**: [path to transcript]

## Financial Sources

### [Company] SEC Filings
- **10-K (Annual)**: [URL]
- **10-Q (Q3 2025)**: [URL]
- **Earnings transcript**: [URL]

## News Articles

### [Publication] - [Headline]
- **URL**: [URL]
- **Date**: [publication date]
- **Author**: [if available]
- **Paywall**: Yes/No
```

---

## Source Evaluation

### Credibility Checklist

For each source, assess:

| Criterion | Questions |
|-----------|-----------|
| Authority | Who wrote/spoke this? What's their expertise? |
| Currency | When was this published? Is it still accurate? |
| Accuracy | Can claims be verified? Does it cite sources? |
| Purpose | Why was this created? Marketing vs. journalism? |
| Bias | What perspective is represented? What's missing? |

### Source Hierarchy

**Most authoritative → Least authoritative:**

1. **SEC filings** - Legally required accuracy
2. **Direct interviews** - First-hand account
3. **Earnings calls** - Formal corporate communication
4. **Press releases** - Official but promotional
5. **Major business publications** - Vetted journalism
6. **Trade publications** - Industry expertise, may have bias
7. **Blog posts/social media** - Verify independently

---

## Source Tier Classification

When registering sources, classify them into quality tiers:

| Tier | Definition | Examples | Citation Confidence |
|------|-----------|----------|-------------------|
| **T1 — Primary** | Full-text source physically in `sources/` folder. Can be read and quoted directly. | Complete transcript, downloaded PDF, full article text | High — quote directly |
| **T2 — Partial** | Partial text available. Key passages captured but full source not in repo. | Paywalled article (key quotes saved), search excerpts, summary notes | Medium — verify quotes |
| **T3 — Referenced** | Cited but full source not available. May be from AI knowledge or inaccessible sources. | AI-recalled statistics, broken URLs, sources you've read but can't download | Low — must verify |

### Minimum Viable Sources

Before starting to write, ensure you have at minimum:
- **1 T1 primary source** with the protagonist's own words (interview, keynote, podcast)
- **1 T1 financial source** (10-K, earnings report, investor presentation)
- **2+ news/industry sources** from different publications

### Upgrading Tiers

- **T3 → T2**: Find and save key excerpts from the source
- **T2 → T1**: Download or transcribe the full source into `sources/`
- Use `/add-sources` to register and classify sources automatically

---

## Research Workflow

Research is **iterative**. You'll cycle through these phases multiple times as writing reveals gaps.

### Phase 1: Initial Discovery

1. **Identify the story** - What decision/situation is compelling?
2. **Find the protagonist** - Who made the key decisions?
3. **Locate primary interview** - YouTube, podcast, conference talk
4. **Transcribe** - Use NotebookLM or Whisper
5. **Register** - Run `/add-sources` to classify and track

### Phase 2: Context Building

1. **Company financials** - 10-K, quarterly reports
2. **Industry context** - Analyst reports, market data
3. **Competitive landscape** - How do competitors approach this?
4. **Timeline** - News articles for chronology

### Phase 3: Verification

1. **Cross-reference claims** - Do multiple sources agree?
2. **Check dates** - Are timelines consistent?
3. **Verify quotes** - Can you trace to original source?
4. **Note gaps** - What couldn't you verify?

### Research Loops (During Writing)

When writing reveals a source gap:
1. **Pause writing** at the current section
2. **Identify the gap** - What specific information is missing?
3. **Search for the source** - Use the discovery strategies above
4. **Register the new source** - Run `/add-sources`
5. **Resume writing** from where you left off

Budget 2-4 research loops per document. This is normal, not a sign of poor preparation.

---

## Working with AI Web Access Limitations

AI tools have limited ability to access web content directly. Some sites block automated access, and paywalled content is generally inaccessible.

### What AI CAN usually access
- Public company press releases
- SEC filings on EDGAR
- Some news sites without hard paywalls
- Wikipedia and public reference sites

### What AI CANNOT usually access
- Paywalled articles (WSJ, FT, Bloomberg)
- Content behind login walls
- Some sites with bot protection
- Video/audio content (needs transcription first)

### Workarounds
1. **Download and save locally**: Save articles as PDF in `sources/`
2. **Copy-paste key passages**: Extract relevant quotes into a text file
3. **Use transcription tools**: Convert video/audio to text (NotebookLM, Whisper)
4. **University library access**: Many paywalled sources are available through institutional databases
5. **Tell the AI what you found**: Paste or describe content directly in conversation

---

## Working with Paywalled Content

### Legitimate Access

- University library database access
- Institutional subscriptions
- Free article limits (WSJ, FT often allow 3-5/month)
- Press release versions of news stories
- Author's personal site may have copy

### Alternatives When Paywalled

- Company's own press releases often cover same story
- SEC filings contain financial data
- Earnings call transcripts available on multiple sites
- Search for executive quotes in other publications

### Documentation

When citing paywalled sources:
- Note in Source_Links.md that paywall exists
- Archive key quotes in Additional Sources document
- Include full citation for readers with access

---

## Legal and Ethical Considerations

### Fair Use in Education

Case studies for classroom use generally qualify as fair use when:
- Used for non-commercial educational purposes
- Using limited portions with attribution
- Not substituting for the original work
- Transforming content into teaching material

### Attribution Requirements

- Always cite sources
- Use quotation marks for direct quotes
- Distinguish between quotes and paraphrases
- Include publication dates

### What NOT to Do

- Don't reproduce entire articles
- Don't claim quotes that aren't in sources
- Don't fabricate or composite quotes
- Don't use confidential/leaked documents without permission

---

## Tools Summary

| Task | Recommended Tool |
|------|------------------|
| YouTube transcription | NotebookLM |
| Audio file transcription | Whisper or NotebookLM |
| SEC filings | EDGAR database |
| News research | Library databases |
| PDF text extraction | Adobe Acrobat, PDF tools |
| Quote verification | Grep/search tools |
| Source organization | Markdown files in sources/ |

---

*Good sources make good case studies. Invest time in finding authoritative primary materials.*
