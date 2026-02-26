# Case Study Development Prompts

Copy-paste these prompts to guide Claude Code through each phase of case study development.

---

## Phase 1: Source Transcription

### Prompt: Transcribe Audio/Video Source

```
I have a [YouTube video / podcast episode / audio file] about [TOPIC].

URL: [URL or file path]

Please:
1. Transcribe the content with speaker identification
2. Note timestamps for key quotes
3. Identify the main speakers and their roles
4. Flag any sections where audio quality affects transcription accuracy

If you cannot directly access the media, please provide instructions for transcription tools I can use (Whisper, Otter.ai, etc.) and the format I should provide the transcript in.
```

---

## Phase 2: Source Analysis

### Prompt: Analyze Primary Interview

```
I have a transcript of an interview with [NAME, TITLE] from [COMPANY] about [TOPIC].

[PASTE TRANSCRIPT OR PROVIDE FILE PATH]

Please analyze this transcript and extract:

## 1. Protagonist Profile
- Full name and current title
- Background (education, career path, relevant experience)
- Why they are positioned to speak on this topic
- What makes them compelling as a case study protagonist

## 2. Key Quotes (Exact Words)
Organize by theme, include:
- The exact quote (in quotation marks)
- The context (what question prompted this)
- Potential use in the case (opening, strategic decision, reflection)

## 3. Data Points
Extract all specific numbers, dates, and metrics:
| Metric | Value | Context |
|--------|-------|---------|

## 4. Timeline of Events
| Date/Period | Event | Quote/Evidence |
|-------------|-------|----------------|

## 5. Strategic Decisions Discussed
For each decision:
- What was decided
- What alternatives were considered (explicitly or implicitly)
- The stated rationale
- The outcome (if discussed)

## 6. Potential Strategic Tensions
Identify genuine dilemmas where reasonable people could disagree:
- Tension 1: [X] vs. [Y]
- Evidence for X:
- Evidence for Y:
- Why this is unresolved:

## 7. Information Gaps
What additional sources would strengthen this case study?
- Financial data needed:
- Competitive context needed:
- Technical details needed:
- Third-party validation needed:
```

### Prompt: Analyze Financial/SEC Sources

```
I have [financial report / SEC filing / earnings transcript] from [COMPANY] for [PERIOD].

[PASTE KEY SECTIONS OR PROVIDE FILE PATH]

Please extract:

## 1. Key Financial Metrics
| Metric | Value | YoY Change | Relevance to Case |
|--------|-------|------------|-------------------|

## 2. Management Commentary on [TOPIC]
Quote relevant sections with page/section references.

## 3. Risk Factors
What risks related to [TOPIC] are disclosed?

## 4. Investment/Spending Data
Specific figures related to [TOPIC] investment.

## 5. Competitive Positioning Statements
How management describes their position vs. competitors.

## 6. Forward-Looking Statements
Plans and expectations relevant to the case timeline.
```

### Prompt: Analyze Industry/Analyst Reports

```
I have [industry report / analyst research] about [TOPIC/INDUSTRY].

[PASTE KEY SECTIONS OR PROVIDE FILE PATH]

Please extract:

## 1. Market Size and Growth
- Current market size
- Projected growth
- Key drivers

## 2. Industry Trends
Trends relevant to the case study topic.

## 3. Competitive Landscape
- Key players
- Market positions
- Differentiation strategies

## 4. Frameworks and Models
Any frameworks mentioned that could be teaching tools.

## 5. Data Points for Context
Statistics that would ground the case study.

## 6. Expert Quotes
Attributable quotes from named analysts/researchers.
```

---

## Phase 3: Additional Sources Document

### Prompt: Compile Additional Sources Document

```
Based on the source analysis completed, please create the "Additional Sources and Data" document.

**Sources analyzed:**
1. [Source 1 name and description]
2. [Source 2 name and description]
3. [etc.]

**Structure the document as:**

# [Company Name] Case Study: Additional Sources and Data

## Executive Summary
Brief overview of sources compiled and key themes.

## Exhibit 1: Executive Interview Excerpts
### [Speaker 1 Name, Title]
Organized excerpts with source attribution.

### [Speaker 2 Name, Title]
Organized excerpts with source attribution.

## Exhibit 2: Financial Data
Tables with sourced financial metrics.

## Exhibit 3: Industry Context
Key statistics and trends from analyst reports.

## Exhibit 4: Competitive Landscape
Comparison data on competitors.

## Exhibit 5: Timeline
Chronological events with sources.

## Bibliography
Full citations in consistent format:
- Author/Speaker. "Title." Publication/Source, Date. URL (if applicable).

---

**Requirements:**
- Every data point must cite its source
- Quotes must be exact (use [...] for omissions)
- Include page numbers for PDF sources
- Organize for easy reference during case writing
```

---

## Phase 4: Main Case Narrative

### Prompt: Write Case Opening

```
Based on the source analysis, write the opening section of the case study (500-800 words).

**Protagonist:** [NAME, TITLE, COMPANY]
**Core tension:** [THE CENTRAL QUESTION]
**Compelling moment to open with:** [SPECIFIC SCENE/REALIZATION]

**Requirements:**
1. Open in medias res (middle of action, not background)
2. First paragraph should hook the reader
3. Introduce protagonist with specific credentials by paragraph 2-3
4. Use a direct quote within first 500 words
5. Create forward momentum toward the strategic question
6. Do NOT provide background history yet (that comes after the hook)

**Tone:** Business journalism (WSJ, HBR) - authoritative but engaging

**Example opening patterns:**
- A number that surprised the protagonist
- A decision moment with stakes
- A meeting where something shifted
- A realization that changed strategy
```

### Prompt: Write Case Body

```
Continue the case study narrative (2,500-4,000 words).

**The opening established:** [SUMMARY OF OPENING]

**Key sections to cover:**

1. **Company/Industry Context** (500-700 words)
   - Company background relevant to the case
   - Industry dynamics
   - Why this moment/challenge mattered

2. **The Challenge/Opportunity** (500-700 words)
   - What problem or opportunity emerged
   - Why traditional approaches wouldn't work
   - The protagonist's initial thinking

3. **Strategic Decisions** (800-1,200 words)
   - Key decision #1: What, why, how
   - Key decision #2: What, why, how
   - [Additional decisions as needed]
   - Include direct quotes showing rationale

4. **Implementation and Outcomes** (500-700 words)
   - How decisions played out
   - Specific results (numbers, metrics)
   - Unexpected developments

5. **Current State** (300-500 words)
   - Where things stand now
   - What's working, what's not
   - Emerging challenges

**Requirements:**
- Use verified quotes from source analysis
- Include specific numbers and dates
- Show multiple perspectives
- Maintain protagonist focus
- Build toward strategic tensions (don't resolve them)
```

### Prompt: Write Case Ending

```
Write the concluding section of the case study (500-800 words).

**The case has covered:** [SUMMARY]

**Requirements:**

1. **Looking Forward** (200-300 words)
   - What the protagonist is considering
   - Near-term decisions ahead
   - Uncertainties acknowledged

2. **Strategic Tensions** (200-300 words)
   - Articulate 2-3 genuine dilemmas
   - Show why reasonable people could disagree
   - Do NOT resolve these tensions

3. **Discussion Questions** (6-8 questions)
   - Questions that don't have obvious answers
   - Questions that require evidence from the case
   - Questions that connect to broader frameworks
   - Mix of analytical and values-based questions

**Ending tone:** Thoughtful uncertainty, not triumph or resolution

**Do NOT:**
- Summarize what the company "should" do
- Declare the protagonist's approach correct
- Provide a neat conclusion
```

---

## Phase 5: Technical Supplement

### Prompt: Write Technical Supplement

```
Write the technical supplement document for the [COMPANY] case study.

**The case narrative covers:** [BRIEF SUMMARY]
**Target audience:** MBA students who have read the case

**Structure:**

# [Company Name] Case Study: Technical and Industry Supplement

## Industry Context
### Market Overview
- Market size, growth rates, key drivers
- Major players and segments

### Relevant Trends
- Trends affecting the case topic
- How industry is evolving

## [Technical Topic] Architecture
### Overview
- How the system/process/product works
- Key components

### Evolution
- How it developed over time
- Generations or versions

### Technical Concepts
- Explain technical terms used in case
- Visual diagrams if helpful

## Competitive Landscape
### Key Competitors
For each relevant competitor:
- Their approach to similar challenge
- Key differences from protagonist's company
- Results/outcomes if known

### Competitive Analysis Table
| Company | Approach | Key Differentiator | Outcome |
|---------|----------|-------------------|---------|

## Regulatory Environment
- Relevant regulations
- Compliance requirements
- How protagonist's company addressed these

## Frameworks for Analysis
### [Framework 1 Name]
- Description
- How it applies to this case
- (Do not advocate for conclusions)

### [Framework 2 Name]
- Description
- Application to case

## Glossary
| Term | Definition |
|------|------------|

## Sources
Full citations for all data in this supplement.

---

**Requirements:**
- Support the case, don't duplicate it
- Provide tools for analysis, not answers
- All data must be sourced
- Target length: 2,500-4,000 words
```

---

## Phase 6: Teaching Note

### Prompt: Write Teaching Note

```
Write the teaching note for the [COMPANY] case study.

**Case synopsis (2-3 sentences):** [SUMMARY]
**Target session length:** 75-90 minutes
**Target audience:** MBA students

**Structure:**

# [Company Name] Case Study: Teaching Note

*For Instructor Use Only*

## Case Synopsis
[Expanded summary - 200 words]

## Learning Objectives
After discussing this case, students should be able to:
1. [Primary objective - tied to case content]
2. [Secondary objective]
3. [Tertiary objective]

## Suggested Assignment Questions
Questions for students to prepare before class:
1. [Question 1]
2. [Question 2]
3. [Question 3]

## Discussion Guide

### Opening (5-7 minutes)
**Question:** [Opening question]
**Purpose:** [What this surfaces]
**Expected responses:** [Range of answers]
**Transition:** [How to move to Section 1]

### Section 1: [Topic] (15-20 minutes)
**Focus:** [What to explore]
**Key questions:**
1. [Question] - Purpose: [Why ask this]
2. [Question] - Purpose: [Why ask this]

**Board plan:**
[What to write/draw on board]

**Expected discussion flow:**
- Students likely to say X
- Push back with Y
- Arrive at framework Z

### Section 2: [Topic] (15-20 minutes)
[Same structure]

### Section 3: [Topic] (15-20 minutes)
[Same structure]

### Closing (10-15 minutes)
**Options:**
- Option A: [Closing question focused on X]
- Option B: [Closing question focused on Y]
- Option C: [Closing question focused on Z]

**Do NOT provide "the answer"** - leave constructive tension

## Board Plan
Visual layout of what the board should look like by end of class:
[Describe or sketch the framework]

## Analysis Framework
### [Framework name] (2x2 or other structure)
[Describe the framework]
[How protagonist's company maps to it]
[How competitors map to it]
[What this reveals]

## Potential Student Positions
| Position | Argument | Counter |
|----------|----------|---------|
| [Position A] | [Why students might argue this] | [Challenge to raise] |
| [Position B] | [Why students might argue this] | [Challenge to raise] |

## Assessment Options

### Individual Write-Up
"[Question requiring 2-3 page analysis]"

**Strong responses will:**
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

### Group Presentation
"[Topic for 10-minute presentation]"

**Evaluation criteria:**
- [Criterion 1]
- [Criterion 2]

### Exam Question
"[Question suitable for timed exam]"

---

**Requirements:**
- Do NOT provide "correct" answers
- Show multiple valid positions
- Include specific timing
- Enable Socratic discussion
- Target length: 2,500-4,000 words
```

---

## Phase 7: Quality Verification

### Prompt: Verify Quote Attribution

```
Please verify the quotes in [DOCUMENT NAME].

For each quote:
1. Locate the exact text in the source documents
2. Confirm speaker attribution is correct
3. Confirm source/date is correct
4. Flag any paraphrases vs. exact quotes
5. Identify any quotes that cannot be verified

**Format your response as:**

## Quote Verification Report

### Verified Quotes
| Quote (first 10 words...) | Speaker | Source | Status |
|---------------------------|---------|--------|--------|
| "..." | [Name] | [Source, Date] | Exact match |

### Paraphrased (flagged for review)
| Document Quote | Source Quote | Difference |
|----------------|--------------|------------|

### Unverified (action needed)
| Quote | Claimed Source | Issue |
|-------|---------------|-------|
```

### Prompt: Verify Data Consistency

```
Please verify data consistency across all case study documents.

**Documents to check:**
1. case-study/[Company]_Case.md
2. case-study/[Company]_Supplement.md
3. case-study/[Company]_Teaching_Note.md
4. case-study/[Company]_Additional_Sources.md

**For each data point, verify:**
- Same number appears consistently (not "$2B" vs "$2 billion" vs "two billion")
- Same dates for same events
- Same names/titles for people
- Same terminology for key concepts

**Format your response as:**

## Data Consistency Report

### Consistent Data Points
| Data Point | Value | Documents |
|------------|-------|-----------|

### Inconsistencies Found
| Data Point | Document 1 | Document 2 | Recommendation |
|------------|------------|------------|----------------|

### Terminology Consistency
| Term | Preferred Form | Variations Found |
|------|---------------|------------------|
```

---

## Utility Prompts

### Prompt: Generate Missing Attribution

```
This quote appears in the case study but lacks full attribution:

"[QUOTE TEXT]"

Currently attributed to: [CURRENT ATTRIBUTION]

Please search for this quote to find:
1. The exact source (interview, article, report)
2. The date
3. The full context

If you cannot find the exact quote, suggest whether it should be:
- Marked as paraphrase
- Removed
- Replaced with a verified quote on the same topic
```

### Prompt: Expand Thin Section

```
This section of the case study needs more development:

[PASTE SECTION]

The section is thin because: [REASON - missing quotes, abstract language, etc.]

Please expand this section by:
1. Adding specific details from the source documents
2. Including a relevant direct quote
3. Providing concrete examples
4. Maintaining the narrative flow

**Available sources for this topic:**
[LIST RELEVANT SOURCES]
```

### Prompt: Convert to PDF-Ready Format

```
Please format the [DOCUMENT NAME] for PDF export.

**Requirements:**
1. Clean markdown that renders well
2. Consistent heading hierarchy
3. Properly formatted tables
4. Page break suggestions ([Page Break] markers)
5. Header/footer suggestions

**Do NOT change content** - only formatting for readability.
```

---

## Public Policy / Political Leadership Adaptations

For cases involving public officials, political leadership, or international development, use these adapted prompts. See `HKS_PUBLIC_POLICY_GUIDANCE.md` for full methodology.

### Prompt: Analyze Public Policy Interview (Adapted Phase 2)

```
I have a transcript of an interview with [NAME, TITLE] from [COUNTRY/INSTITUTION] about [POLICY TOPIC].

[PASTE TRANSCRIPT OR PROVIDE FILE PATH]

Please analyze this transcript and extract:

## 1. Decision Maker Profile
- Full name, title, and formal authority
- Background (education, career path, how they came to power)
- What political capital/constraints do they have?
- What makes them compelling as a case study protagonist?

## 2. Key Quotes (Exact Words)
Organize by theme, include:
- The exact quote (in quotation marks)
- The context (what question prompted this)
- Potential use in the case (opening, strategic decision, reflection)

## 3. Stakeholder Map
From the interview, identify key actors:
| Actor | Objectives | Power/Resources | Position |
|-------|-----------|-----------------|----------|

## 4. Data Points
Extract all specific numbers, dates, and metrics:
| Metric | Value | Context |
|--------|-------|---------|

## 5. Timeline of Events
| Date/Period | Event | Quote/Evidence |
|-------------|-------|----------------|

## 6. Policy Decisions Discussed
For each decision:
- What was decided
- What authority enabled it
- What opposition/constraints existed
- What stakeholders were affected
- The stated rationale
- The outcome (if discussed)

## 7. Values Trade-offs Identified
Identify genuine tensions between competing values:
- Tension 1: [Value A] vs. [Value B]
  - Evidence for prioritizing A:
  - Evidence for prioritizing B:
  - Why this remains unresolved:

## 8. Institutional Context Needed
What additional information is needed about:
- Political/governmental structure
- Legal/constitutional framework
- International relationships
- Historical background
```

### Prompt: Write Public Policy Case Opening

```
Based on the source analysis, write the opening section of the public policy case study (500-800 words).

**Decision Maker:** [NAME, TITLE, COUNTRY/INSTITUTION]
**Core decision:** [THE SPECIFIC DECISION THEY FACE]
**Compelling moment to open with:** [SPECIFIC SCENE/CRISIS]

**Requirements:**
1. Open with a decision moment or crisis (not biography)
2. First paragraph should establish stakes for affected populations
3. Introduce protagonist with their authority AND constraints by paragraph 2-3
4. Use a direct quote within first 500 words
5. Show multiple stakeholders with competing interests
6. Create forward momentum toward the policy question
7. Do NOT provide background history yet (that comes after the hook)

**Tone:** Serious journalism (Economist, Foreign Affairs) - authoritative, analytical, engaged

**Example opening patterns for public policy:**
- A crisis that forced immediate decision
- A meeting where competing interests clashed
- A moment when the leader faced impossible choice
- A vote/election result that changed everything
```

### Prompt: Write Country/Institutional Context (replaces Company Context)

```
Write the context section of the case study (500-700 words).

**Decision Maker:** [NAME, TITLE]
**Country/Institution:** [NAME]
**Policy Domain:** [TOPIC]

**Cover:**
1. **Historical Background** (150-200 words)
   - How did the current situation develop?
   - What path dependencies constrain options?
   - What previous attempts at reform/change?

2. **Political System** (100-150 words)
   - How does government work in this context?
   - What is the decision maker's formal authority?
   - What checks/balances exist?

3. **Economic/Social Context** (100-150 words)
   - Key economic indicators relevant to case
   - Social/demographic factors
   - Resource constraints

4. **International Context** (100-150 words)
   - Key external relationships
   - International obligations/constraints
   - Foreign actors' interests

**Requirements:**
- Provide only context needed to understand the case
- Do not advocate for any position
- Include specific data points with sources
- Connect to the protagonist's challenges
```

### Prompt: Write Stakeholder Analysis Section

```
Write a stakeholder analysis for the teaching note (300-500 words).

**The case involves these key actors:**
[LIST MAIN ACTORS]

**For each stakeholder, identify:**

| Actor | Objectives | Resources/Power | Constraints | Position |
|-------|-----------|-----------------|-------------|----------|

**Questions for class discussion:**
1. Whose support was essential for the protagonist?
2. Who could veto or block action?
3. What coalitions were possible?
4. How did the protagonist's actions affect different stakeholders?

**Board plan for stakeholder mapping exercise:**
[Describe visual layout]
```

### Prompt: Identify Values Trade-offs

```
Based on the case analysis, identify the core values trade-offs for the teaching note.

**Format each as:**

### Tension [N]: [Value A] vs. [Value B]

**The Dilemma:**
[1-2 sentence description of why these values conflict in this case]

**Evidence for Prioritizing [Value A]:**
- [Point 1 with case evidence]
- [Point 2 with case evidence]

**Evidence for Prioritizing [Value B]:**
- [Point 1 with case evidence]
- [Point 2 with case evidence]

**Why This Remains Unresolved:**
[Why reasonable people could disagree]

**Discussion Question:**
[Question that forces students to choose and defend]
```

---

---

## Phase 2.5: Source Quality Classification

### Prompt: Classify Source Tiers

```
Review the source materials I've gathered and classify each into quality tiers.

**Tier Definitions:**
- **T1 (Primary)**: Full-text source physically available — complete transcript, downloaded PDF, full article text. Can be read and quoted directly with high confidence.
- **T2 (Partial)**: Partial text available — extracted quotes, search snippets, paywalled content where only key passages were captured. Source exists but cannot be fully verified.
- **T3 (Referenced)**: Referenced only — cited but full source not available. May be from general knowledge, web search, or inaccessible sources. Requires verification.

**For each source, determine:**

| Source | Tier | Justification | Action Needed |
|--------|------|--------------|---------------|
| [Source name] | T1/T2/T3 | [Why this tier] | [None / Get full text / Verify claim] |

**Summary:**
- T1 sources: [count] — these are your foundation
- T2 sources: [count] — usable with caveats
- T3 sources: [count] — must verify or upgrade before publication

**Minimum viable source check:**
- [ ] At least 1 T1 primary source with protagonist's voice
- [ ] At least 1 T1 financial source
- [ ] At least 2 news/industry sources from different publications
```

---

## Phase 7.5: Financial Verification

### Prompt: Verify Financial Accuracy

```
Review all financial figures across the case study documents and verify accuracy.

**Check these specific items:**

1. **Arithmetic consistency**: When the case states "revenue grew from $X to $Y, a Z% increase" — does Z% actually equal (Y-X)/X × 100?

2. **Cross-document matching**: Financial figures in the Main Case, Supplement, and Additional Sources should be identical. Flag any discrepancies.

3. **Source verification**: For each financial figure, confirm it matches the original source document. List:
   - The figure as stated in the case
   - The figure as stated in the source
   - Whether they match

4. **Format consistency**: Choose one format and apply throughout:
   - Use "$X.X billion" not mixing "$XB" and "$X billion"
   - Use consistent decimal precision

**Output format:**

## Financial Verification Report

### Figures Checked
| Figure | Case Says | Source Says | Match? |
|--------|-----------|-------------|--------|

### Arithmetic Errors
[List any calculations that don't check out]

### Unsourced Financial Claims
[List any financial figures with no source backing]
```

---

## Phase 7.6: Bias Assessment

### Prompt: Assess Source and Narrative Bias

```
Analyze the case study for systematic bias in sources and framing.

**Source Composition:**
Count sources by origin:
- Company-generated (press releases, blog posts, investor materials): [count]
- Executive interviews: [count]
- Independent journalism: [count]
- Academic/analyst reports: [count]
- Employee perspectives: [count]
- Customer perspectives: [count]
- Critical/skeptical perspectives: [count]

**Bias Checks:**
1. **Selection bias**: Are sources disproportionately from one perspective?
2. **Survivorship bias**: Does the case only tell the success story?
3. **Framing bias**: Is the protagonist's strategy presented as obviously correct?
4. **Authority bias**: Are executive claims taken at face value?
5. **Recency bias**: Are recent events given disproportionate weight?

**Quote Balance:**
| Speaker Category | Quote Count | Favorable | Neutral | Critical |
|-----------------|-------------|-----------|---------|----------|

**Missing Perspectives:**
[List stakeholder groups not represented in sources]

**Recommendations:**
[How to address identified biases — additional sources, narrative adjustments, teaching note acknowledgments]
```

---

## Phase 8: Disclaimers and Final Preparation

### Prompt: Add AI-Generated Content Disclaimers

```
Add standardized disclaimers to each case study document.

**Header disclaimer** (top of each document, after title):
> This case study was developed with AI assistance using the Agentic AI Case Study
> Development methodology. All quotes and data points have been sourced from publicly
> available materials. This case is intended for classroom discussion and is not intended
> to serve as an endorsement, source of primary data, or illustration of effective or
> ineffective management.

**AI Methodology Note** (Additional Sources document only):
Include a section describing:
- How sources were collected (human research + AI analysis)
- What AI tools were used
- What verification procedures were followed
- What limitations exist (no direct interviews, publicly available only)

**Footer** (end of each document):
Include course info, development methodology, date, and verification status.
```

### Prompt: Convert to PDF-Ready Format

```
Please format the [DOCUMENT NAME] for PDF export.

**Requirements:**
1. Clean markdown that renders well
2. Consistent heading hierarchy
3. Properly formatted tables
4. Page break suggestions ([Page Break] markers)
5. Header/footer suggestions

**Do NOT change content** - only formatting for readability.
```

---

*These prompts are templates. Customize the bracketed sections for your specific case study.*

*For public policy cases, also consult templates/HKS_PUBLIC_POLICY_GUIDANCE.md*
