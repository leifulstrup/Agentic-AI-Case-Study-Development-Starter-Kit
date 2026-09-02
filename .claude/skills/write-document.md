# Write Document

Interactive skill that guides the user through writing case study documents one at a time, with built-in verification and research loop support.

## Usage

```
/write-document
```

## Instructions

### 1. Check Prerequisites

Before writing anything, verify:

- **Configuration**: Read `case-config.yaml`. If it contains placeholder values, stop and suggest running `/setup-case` first.
- **Sources**: Check `sources/Source_Registry.md` (or `Source_Links.md` for v2 projects). If no sources are registered, stop and suggest running `/add-sources`.
- **Assessment**: Look for recent `assess-sources-*.log`. If none exists, recommend running `/assess-sources` first but don't block — the user may choose to proceed.

### 2. Determine Which Document to Write

Check `case-study/` for existing documents. The required sequence is:

**Read `documents.required` in `case-config.yaml` first.** It lists which documents this
course expects, in order. Do not assume four — a course may scope its authors to fewer,
and the Teaching Note is frequently written by the instructor rather than the author.
Offer only what that list names; if the user asks for a document not on the list, write
it, but say it is outside their course's required set. **If `documents.required` is not
in the file at all**, the project predates the setting: fall back to all four, mention
once that the setting exists and can scope the set, and continue. Never treat the absent
key as a problem to stop on.

Dependency order, applied to whatever the list contains:

1. **Additional Sources** → must be first (compiles raw materials)
2. **Main Case** → requires Additional Sources
3. **Technical Supplement** → requires Main Case
4. **Teaching Note** → requires Main Case (can parallel with Supplement)

**Use the word-count targets from `documents.target_word_counts`**, not a remembered
figure. They are deliberately sized for an author working alongside a full-time job.

**Then hold yourself to them.** Measured behaviour, not a hypothetical: in testing, an
agent following this skill overshot every target it was given by 23-55%, averaging 41%
over on the package. Nobody intended that — long drafts simply feel thorough while you
are writing them. So:

- **Budget before you write.** Divide the target across the planned sections and note
  each section's share. A 2,500-word Main Case is roughly 250 words per section across
  ten sections; that is a short section, and knowing it in advance changes what you draft.
- **Count when each document is finished** and compare against the target. Over by more
  than 10%, cut before showing the author — do not hand them an over-length draft and an
  apology.
- **Cut by deleting, not by compressing.** Remove the weakest example, the third
  supporting quotation, the paragraph restating the previous one. Squeezing prose to hit
  a number makes it worse; dropping the least load-bearing material makes it better.
- **Never cut evidence to hit a number.** This rule applies to *prose* — the Main Case,
  the Supplement, the Teaching Note's discussion. **The Additional Sources document is
  not prose; it is the evidence file**, and every quotation the other documents rely on
  has to be traceable through it. Deleting an entry there does not shorten an argument,
  it severs a chain of custody — and it does so silently, because the quotation still
  reads fine in the Main Case with nothing left behind it.

  This is measured, not cautionary. In testing, an agent hit the Additional Sources
  target exactly as instructed and **broke traceability for four quotations the Main
  Case went on to use**. Asked to do it again, it refused and overran the target instead.
  That was the right call.

  So when the evidence file runs long: **let it.** Report the overage and why, and put
  the reduction into the prose documents where cutting removes words rather than proof.
  If it is very long, the honest fix is usually fewer sources or a narrower case, which
  is the author's decision and not one to make silently by deleting rows.
- **Report the number.** End with the actual word count against the target, so the author
  can see the constraint was honoured rather than take it on trust.

Going over is a real cost, not a stylistic preference: the author has other work, and the
professor reviewing it has a stack of these. A case too long to revise does not get
revised.

Identify the next document in sequence. If the user asks for a specific document out of order, explain the recommended sequence and ask if they want to proceed anyway.

If every document named in `documents.required` exists, report that and ask if the user wants to revise one.

### 3. Document-Specific Setup

Before writing, ask document-specific questions:

#### Additional Sources Document
- Read ALL source files in `sources/` and the Source Registry
- Present an outline of exhibits and sections for user approval:
  ```
  Here's how I'd organize the Additional Sources document:

  1. Executive Summary — themes across all sources
  2. Exhibit 1: Executive Interview Excerpts — [speaker names]
  3. Exhibit 2: Financial Data — [key metrics]
  4. Exhibit 3: Industry Context — [trends and data]
  5. Exhibit 4: Competitive Landscape — [competitors found]
  6. Exhibit 5: Timeline — [date range]
  7. Bibliography — [X sources]

  Does this structure work? Any sections to add or remove?
  ```

#### Main Case
- Read the Additional Sources document
- Identify 2-3 core tensions from the sources
- Offer opening scene options:
  ```
  I see several compelling opening moments:
  1. [Specific scene/decision/moment from sources]
  2. [Another moment]
  3. [Another moment]

  Which resonates most? Or describe a different opening you prefer.
  ```
- Confirm the protagonist and their central decision/dilemma

#### Technical Supplement
- Read the Main Case document
- Ask: "What technical concepts from the case need deeper explanation for MBA students?"
- Suggest concepts based on what appears in the case
- Confirm competitive landscape scope

#### Teaching Note
- Read the Main Case and Supplement
- Ask for learning objectives:
  ```
  Based on the case, I suggest these learning objectives:
  1. [Objective derived from case tensions]
  2. [Objective derived from strategic decisions]
  3. [Objective derived from industry context]

  Do these work? Want to modify or add any?
  ```
- Ask about analytical frameworks to include
- Confirm session length from config

### 3b. Before You Type a Quotation Mark

**Read the Quoting Rules in `AGENTS.md` before drafting any section that quotes a
source.** They are canonical and live in one place; do not work from memory and do not
restate them here.

What matters at *drafting* time — the rules exist to be applied now, not to be
discovered later by the verifier:

1. **Check the source's processing status before you quote it, not after.**
   `sources/Source_Registry.md` records whether each source is VERBATIM, EDITED, ASR or
   EXTRACTED. An EDITED source ("edited for clarity and length") and an uncorrected ASR
   transcript **cannot** support a plain verbatim quotation. If the source you are about
   to quote is either, use indirect speech or the bracket convention *as you write it*.
2. **Paste, then trim — never retype.** Copy the exact span from the source file and
   remove what you do not need with an ellipsis. Retyping from memory or from a research
   summary is how words go missing from the middle of a quotation.
3. **Never quote from a summary, dossier, or research note.** Those paraphrase. Quote
   only from a committed source file; if the verbatim wording is not in `sources/`, it is
   not quotable yet.
4. **Keep your own framing outside the marks.** If the sentence needs "the core problem
   is that" or "a fixed fee is" to read well, those are your words — they go before the
   opening quotation mark.
5. **Resist smoothing.** Spoken sources stutter and repeat. Removing a disfluency inside
   quotation marks without an ellipsis is a silent edit, and dozens of them across a
   package turn a quotation into a reconstruction.

**Why this is a drafting step and not a verification step.** Every one of these defects
has been found repeatedly by verification and could have been prevented here at no cost:
unmarked smoothing has been counted in the dozens on three separate occasions, and a
single package has carried dropped words, a reversed comparison, framing pulled inside
the marks, and a constructed illustration presented as a quotation. The verifier
catching them is the expensive path. **You are the cheap one.**

### 4. Write in Sections

**Do NOT write the entire document at once.** Write section by section:

- Present each section (500-1000 words at a time)
- After each section, pause and ask: "How does this look? Any changes before I continue?"
- Accept feedback, revise, then move to the next section

### 5. Inline Verification (After Each Section)

After writing each section, perform lightweight checks:

- **Quote check**: Does every quote have a named speaker and dated source — *and* does
  its wording match the source file exactly? Attribution and fidelity are separate
  questions; a correctly attributed quotation can still be misquoted. If the source is
  EDITED or ASR, is the convention applied here rather than deferred?
- **Number check**: Does every statistic or financial figure cite its source?
- **Claim check**: Are there any claims that came from AI knowledge rather than source documents?
- **Length check**: Is this section within its share of the document's word budget? If the
  document is trending long, correct it now — over-length is far cheaper to fix a section
  at a time than in one pass at the end.

For any unverified claims found:
- Flag them inline with a comment: `<!-- VERIFY: [claim] — source needed -->`
- Add them to `verification-debt.yaml` with status "unverified"
- Tell the user: "I flagged X items that need source verification. These are tracked in verification-debt.yaml."

### 6. Research Loop

If a source gap is discovered during writing (e.g., need competitor revenue data, need a specific date):

```
I need [specific information] to write this section accurately.
I don't have a source for this in the registry.

Options:
1. I'll write around the gap and flag it as verification debt
2. Let's pause and find this source — run /add-sources
3. Do you know this information? Tell me and I'll cite you as the source

Which do you prefer?
```

If user chooses option 2, pause writing, help find the source, register it, then resume writing from where you left off.

### 7. Document Completion

After the full document is written:

1. **Save the document** to `case-study/{company_short}_{document_type}.md`
   - Use naming convention: `Company_Additional_Sources.md`, `Company_Case.md`, `Company_Supplement.md`, `Company_Teaching_Note.md`

2. **Update `PROJECT_CONTEXT.md`**:
   - Mark the document as complete in the status section
   - Update the phase
   - Update next steps

3. **Report verification debt**:
   ```
   ## Document Complete: {document_name}

   Saved to: case-study/{filename}
   Word count: ~{count}

   ### Verification Debt
   - {N} items flagged for verification
   - Run /verify-sources to check attribution
   - Run /validate-financials to check arithmetic (if applicable)

   ### Next Step
   {Recommend next document or verification step}
   ```

4. **Offer git checkpoint**: "Want me to commit this progress? Run `/git-update`"

### 8. Between-Document Verification Gate

When 2+ documents exist and the user starts the next document:

- Run a quick consistency check (similar to `/verify-consistency` but lighter)
- Report any data mismatches between existing documents
- Report current verification debt count
- Ask user to resolve critical issues before proceeding, or acknowledge and continue

## Writing Standards (Applied to All Documents)

- **Protagonist-centered**: Name a specific person, show their reasoning
- **Concrete**: "$2B investment" not "invested heavily"
- **Attributed**: Every quote and data point traced to a dated source
- **No advocacy**: Present tensions, don't resolve them
- **Show, don't tell**: Specifics and quotes, not generalizations
- **Never acceptable**: "Industry experts suggest...", "The company reportedly...", "Analysts believe..." — always name the source

For public policy cases (case_type = "public_policy"), also reference `templates/HKS_PUBLIC_POLICY_GUIDANCE.md` for adapted frameworks.

## Notes

- This skill is the primary way students create documents in v3
- Always write to `case-study/` directory, never to the root or other locations
- If the user wants to revise an existing document, read it first, ask what they want to change, and edit in place

## Output

Display each section to the user as it's written. Save completed document to `case-study/`. Update `PROJECT_CONTEXT.md` and `verification-debt.yaml` as needed.
