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

1. **Additional Sources** → must be first (compiles raw materials)
2. **Main Case** → requires Additional Sources
3. **Technical Supplement** → requires Main Case
4. **Teaching Note** → requires Main Case (can parallel with Supplement)

Identify the next document in sequence. If the user asks for a specific document out of order, explain the recommended sequence and ask if they want to proceed anyway.

If all four documents exist, report that and ask if the user wants to revise an existing document.

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

### 4. Write in Sections

**Do NOT write the entire document at once.** Write section by section:

- Present each section (500-1000 words at a time)
- After each section, pause and ask: "How does this look? Any changes before I continue?"
- Accept feedback, revise, then move to the next section

### 5. Inline Verification (After Each Section)

After writing each section, perform lightweight checks:

- **Quote check**: Does every quote have a named speaker and dated source?
- **Number check**: Does every statistic or financial figure cite its source?
- **Claim check**: Are there any claims that came from AI knowledge rather than source documents?

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

- The detailed phase-by-phase prompts in `templates/PROMPTS.md` inform this skill's behavior — the student doesn't need to read PROMPTS.md directly
- This skill is the primary way students create documents in v3
- Always write to `case-study/` directory, never to the root or other locations
- If the user wants to revise an existing document, read it first, ask what they want to change, and edit in place

## Output

Display each section to the user as it's written. Save completed document to `case-study/`. Update `PROJECT_CONTEXT.md` and `verification-debt.yaml` as needed.
