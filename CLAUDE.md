@AGENTS.md

## Claude Code Specifics

The canonical behavioral guidance above comes from `AGENTS.md` (shared across all AI tools). This section covers what's specific to Claude Code.

### Slash Commands

Every workflow action in AGENTS.md is available as a `/slash-command` — the skill definitions live in `.claude/skills/`. Prefer running the skill over improvising the procedure:

`/scout-case` · `/setup-case` · `/add-sources` · `/assess-sources` · `/coach-case` · `/write-document` · `/check-status` · `/verify-all` · `/verify-consistency` · `/verify-quotes` · `/verify-sources` · `/verify-links` · `/validate-financials` · `/assess-bias` · `/verify-cross-document` · `/add-disclaimers` · `/export-pdf` · `/git-update`

### Between-Document Gates

After completing each document, automatically run a quick consistency check across existing documents, report the current verification-debt count, and flag critical issues before proceeding to the next document.

### Repository Purpose

This is the **template repository**. Individual case study projects are created from it via GitHub's "Use this template" feature. When working in the template itself (rather than a case project), you are doing template development — check `PROJECT_CONTEXT.md` for status.
