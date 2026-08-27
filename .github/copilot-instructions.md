# Copilot Instructions

**The canonical behavioral guidance for this repository lives in [`AGENTS.md`](../AGENTS.md) at the repo root — read and follow it.** It covers your role (conversation-first case study development guide), how to behave, the iterative process model, file structure, source tiers (T1/T2/T3), verification-debt tracking, the quoting rules, who should verify a package and what to disclose when the author verifies their own work, why a check that could not run must never report a pass, and writing standards.

This file adds only what's Copilot-specific.

## Skill Equivalents

This repo includes `/slash-commands` for Claude Code (defined in `.claude/skills/`). Copilot does not support slash commands, but you can perform the same actions when the user asks in natural language — read the corresponding skill file and follow its procedure:

| Claude Code Skill | What to Ask Copilot |
|-------------------|---------------------|
| `/scout-case` | "Help me scout whether these companies can support a teaching case" |
| `/setup-case` | "Help me configure my case study" |
| `/add-sources` | "Scan the sources folder and register any new files" |
| `/assess-sources` | "Evaluate my source quality and give me a go/no-go assessment" |
| `/coach-case` | "Coach me on strengthening my sources — find the gaps and help me research them" |
| `/write-document` | "Help me write the next document in my case study" |
| `/check-status` | "Show me my project status and what to do next" |
| `/verify-all` | "Run all quality checks on my case study" |
| `/verify-consistency` | "Check for data consistency across my documents" |
| `/verify-quotes` | "Verify that all quotes are properly attributed" |
| `/verify-sources` | "Check that all claims have source attribution" |
| `/verify-links` | "Validate all URLs in my documents" |
| `/validate-financials` | "Check the arithmetic and financial figures" |
| `/assess-bias` | "Analyze my sources for perspective balance" |
| `/verify-cross-document` | "Check structural alignment between my documents" |
| `/add-disclaimers` | "Add AI methodology disclaimers to my documents" |
| `/export-pdf` | "Prepare my documents for PDF export" |
| `/git-update` | "Commit and push my changes" |
