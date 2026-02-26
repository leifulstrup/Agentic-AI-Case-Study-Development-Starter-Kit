# Case Development Workflow

This document explains the end-to-end workflow for creating a case study using this template.

---

## The Process Model

Case study development is **iterative**, not linear. You'll cycle between gathering sources and writing as gaps are discovered. This is called a **research loop** — and it's normal.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  SETUP → SOURCES → ASSESS → WRITE ──┬── VERIFY → PUBLISH
│                ↑                     │                  │
│                └─── RESEARCH LOOP ←──┘                  │
│                  (gap found during writing)              │
└─────────────────────────────────────────────────────────┘
```

---

## Phase 1: Setup

Create your repository and configure the case study.

### Create Repository

1. Click **"Use this template"** on the template repository
2. Name it `[company]-case-study` and set to **Private**
3. Clone to your computer (see README.md for commands)

### Configure

**Claude Code users** — run the setup skill:
```
/setup-case
```
This asks you questions conversationally and writes all config files automatically.

**VS Code + Copilot users** — open the Copilot chat panel (Agent Mode) and say:
> "Help me configure my case study"

Copilot reads `.github/copilot-instructions.md` and walks you through the same setup process.

**Chat tool users** — the starter prompt asks you about your case when you begin.

**Manual** — edit `case-config.yaml` with your case details.

### Git Checkpoint
```bash
git add -A && git commit -m "Configure case study for [Company]" && git push
```

---

## Phase 2: Source Collection

Add research materials to the `sources/` folder:

| Subfolder | What Goes Here |
|-----------|---------------|
| `sources/transcripts/` | Interview transcripts, podcast notes, conference talk notes |
| `sources/financial/` | SEC filings, earnings reports, investor presentations |
| `sources/news/` | News articles, press releases, media profiles |
| `sources/reports/` | Industry reports, analyst research, market data |

**What makes good source material:**
- A named protagonist who made interesting decisions under uncertainty
- Direct quotes from interviews, podcasts, or conference talks
- Concrete numbers (revenue, investment, headcount, timeline)
- Multiple perspectives (executive, industry, customer)
- Strategic tension with no obvious "right answer"

### Register Sources

**Claude Code users:**
```
/add-sources
```
This scans for new files, asks metadata, assigns quality tiers (T1/T2/T3), and updates the Source Registry.

**VS Code + Copilot users:** Say *"Scan the sources folder and register any new files"* in Agent Mode.

**Chat tool users:** Upload or paste your source materials into the chat.

See `templates/SOURCE_ACQUISITION.md` for detailed guidance on finding and transcribing sources.

### Assess Source Quality

**Claude Code users:**
```
/assess-sources
```

**VS Code + Copilot users:** Say *"Evaluate my source quality and give me a go/no-go assessment"*.

This evaluates depth, breadth, reliability, and completeness with a **go/no-go gate**:
- **GREEN**: Ready to write
- **YELLOW**: Can proceed with caution
- **RED**: Need more sources first

### Git Checkpoint
```bash
git add -A && git commit -m "Add source materials" && git push
```

---

## Phase 3: Writing

Create the four documents **in order**. Each document builds on the previous ones.

| Order | Document | Prerequisites |
|-------|----------|--------------|
| 1 | Additional Sources | Sources collected and assessed |
| 2 | Main Case | Additional Sources complete |
| 3 | Technical Supplement | Main Case complete |
| 4 | Teaching Note | Main Case complete |

**Claude Code users** — the writing skill handles prerequisites and sequencing:
```
/write-document
```

**VS Code + Copilot users** — say *"Help me write the next document in my case study"* in Agent Mode.

This will:
- Check prerequisites are met
- Determine the next document to write
- Ask document-specific setup questions
- Write section by section, pausing for your feedback
- Check attribution and flag unverified claims
- Save to `case-study/` when complete

**Chat tool users** — use the prompts in `templates/PROMPTS.md` to guide writing.

### Research Loops

During writing, you'll often discover gaps: a missing competitor's revenue, an unverifiable claim, a date you can't confirm. When this happens:

1. **Pause writing** at the current section
2. **Find the source** — search online, check your materials, or use `/add-sources`
3. **Register the new source** in the Source Registry
4. **Resume writing** from where you left off

This is expected behavior, not a problem. Budget 2-4 research loops per document.

### Verification Gates

Between documents, Claude Code automatically:
- Runs a quick consistency check across existing documents
- Reports current verification debt count
- Flags any critical issues to resolve before proceeding

### Git Checkpoint (after each document)
```bash
git add -A && git commit -m "Complete [Document Name] draft" && git push
```

---

## Phase 4: Targeted Edits

After completing all four documents, review and refine:

1. **Cross-document consistency**: Do the same numbers appear everywhere?
2. **Teaching Note alignment**: Do discussion questions reference actual case content?
3. **Quote accuracy**: Are all quotes exact and properly attributed?
4. **Financial accuracy**: Do percentages match the underlying numbers?

This phase is about precision, not rewriting.

---

## Phase 5: Verification

Run quality checks before sharing or publishing.

**Claude Code users** — run the comprehensive check:
```
/verify-all
```

**VS Code + Copilot users** — say *"Run all quality checks on my case study"* in Agent Mode.

This runs all checks in sequence:
- `/verify-consistency` — data point matching
- `/verify-sources` — attribution completeness
- `/verify-quotes` — quote traceability
- `/validate-financials` — arithmetic accuracy
- `/verify-links` — URL validation
- `/assess-bias` — perspective balance
- `/verify-cross-document` — structural alignment

**Chat tool users** — use the quality checklist in `templates/QA_WORKFLOW.md`.

Address any issues and re-run until clean.

---

## Phase 6: Publication

### Add Disclaimers
```
/add-disclaimers
```

### Export to PDF
```
/export-pdf
```

### Final Commit
```bash
git add -A && git commit -m "Final case study package" && git push
```

---

## Quick Reference: Skills

These `/slash-commands` work in **Claude Code**. **VS Code + Copilot** users: ask for the same action in natural language (see `.github/copilot-instructions.md` for the full equivalents table).

| Phase | Command | When to Use |
|-------|---------|-------------|
| Setup | `/setup-case` | First thing after cloning |
| Sources | `/add-sources` | After adding files to `sources/` |
| Assessment | `/assess-sources` | Before writing |
| Writing | `/write-document` | To create each document |
| Status | `/check-status` | Anytime — see where you are |
| Verification | `/verify-all` | Before publication |
| Financials | `/validate-financials` | After writing documents with numbers |
| Bias | `/assess-bias` | After all documents are complete |
| Disclaimers | `/add-disclaimers` | Before final export |
| Export | `/export-pdf` | When ready to distribute |
| Git | `/git-update` | To commit and push changes |

> **Public Policy Cases**: If your case involves public policy or political leadership, tell your AI tool during setup (select "public policy") and reference `templates/HKS_PUBLIC_POLICY_GUIDANCE.md` for adapted frameworks.
