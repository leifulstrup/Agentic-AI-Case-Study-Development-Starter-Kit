# Check Status

Generate a comprehensive project dashboard showing phase progress, verification debt, source quality, and recommended next action.

## Usage

```
/check-status
```

## Instructions

### 1. Gather Project State

Read these files (handle missing files gracefully — this skill must work with v2 and v3 projects):

- **`case-config.yaml`** — Is the project configured? Extract company name and topic.
- **`sources/Source_Registry.md`** — Source tier breakdown. If missing, fall back to `sources/Source_Links.md`.
- **`verification-debt.yaml`** — Open verification debt items. If missing, report "not tracked".
- **`case-study/`** — Which documents exist? List all `.md` files (excluding `.gitkeep`).
- **`assess-sources-*.log`** — Most recent source assessment date and result.
- **`verify-all-*.log`** — Most recent full verification date and result.
- **`PROJECT_CONTEXT.md`** — Current phase and decisions.

### 2. Determine Current Phase

Based on what exists:

| Phase | Condition |
|-------|-----------|
| **Not Started** | Config has placeholder values |
| **Configured** | Config populated, no sources registered |
| **Collecting Sources** | Sources exist but not assessed, or assessed RED |
| **Sources Ready** | Sources assessed GREEN or YELLOW, no documents written |
| **Writing** | 1-3 documents exist in case-study/ |
| **Drafts Complete** | All 4 documents exist |
| **Verification** | All 4 documents exist, verify-all has been run |
| **Ready to Publish** | All 4 documents + verify-all shows "Ready for Use" |

### 3. Generate Dashboard

```
# Project Status Dashboard

Generated: [date]
Case: [company_name] — [topic]
Phase: [current phase]

## Phase Progress

| Step | Status | Details |
|------|--------|---------|
| 1. Configure | ✅ Done / ⬜ Needed | /setup-case |
| 2. Add Sources | ✅ Done / 🔄 In Progress / ⬜ Needed | X files registered |
| 3. Assess Sources | ✅ GREEN / ⚠️ YELLOW / 🔴 RED / ⬜ Not run | [date or N/A] |
| 4. Additional Sources | ✅ Written / ⬜ Not started | [word count if exists] |
| 5. Main Case | ✅ Written / ⬜ Not started | [word count if exists] |
| 6. Supplement | ✅ Written / ⬜ Not started | [word count if exists] |
| 7. Teaching Note | ✅ Written / ⬜ Not started | [word count if exists] |
| 8. Verify Quality | ✅ Passed / ⚠️ Warnings / 🔴 Issues / ⬜ Not run | [date or N/A] |
| 9. Publish | ✅ Done / ⬜ Not started | |

## Source Quality

| Tier | Count |
|------|-------|
| T1 — Primary (in repo) | X |
| T2 — Partial | X |
| T3 — Referenced only | X |
| **Total** | **X** |

{If Source_Registry.md doesn't exist: "Source tracking not set up. Run /add-sources to create the registry."}

## Verification Debt

| Status | Count |
|--------|-------|
| Unverified | X |
| Flagged | X |
| Verified | X |
| Removed | X |
| **Open (needs action)** | **X** |

{If verification-debt.yaml doesn't exist: "Verification debt not tracked. It will be created automatically when you run /write-document."}

{If open items > 0, list the top 5:}
### Top Open Items
1. [claim] — in [document] — needs [source]
2. ...

## Recommended Next Action

**[Specific, actionable instruction]**

[Explain why this is the right next step. Include the exact skill command to run.]

## After That

1. [Next upcoming step with skill command]
2. [Step after that]
3. [Step after that]
```

### 4. Handle Edge Cases

- **v2 project (no Source_Registry, no verification-debt.yaml)**: Work with what's available. Note missing v3 files and offer to create them: "This project uses v2 format. Want me to set up v3 tracking? Run `/add-sources` to create the Source Registry."
- **Empty project**: Show all steps as "Needed", recommend `/setup-case` as first action.
- **Partially complete project**: Accurately reflect what exists and what's next.
- **All done**: Congratulate and suggest final review or export.

## Notes

- This skill replaces `/guide-next-step` from v2
- Always check for files before reporting on them — never assume files exist
- Use emoji status indicators for quick scanning (✅ ⚠️ 🔴 ⬜ 🔄)
- Word counts for existing documents should be approximate (count words in the file)

## Output

Display the dashboard directly. No log file needed.
