# Git Update Cycle

Complete a git update cycle with documentation updates and quality checks.

## Usage

```
/git-update
```

## Pre-Flight Checks

1. **Check current branch**
   ```bash
   git branch --show-current
   git status
   ```

2. **Check for uncommitted changes**

3. **Check remote status**
   ```bash
   git fetch origin
   git status -uno
   ```

4. **Check for sensitive files**
   - Scan for credentials, API keys
   - Verify .gitignore excludes sensitive patterns

## Documentation Updates

### CHANGELOG.md
- Add entry for today's changes
- Follow Keep a Changelog format
- Use categories: Added, Changed, Removed, Fixed

### README.md
- Update if structure changed
- Update if new documents added

## Quality Checks

For case study projects:
- Run `/verify-consistency` if .md files changed
- Verify all new quotes have attribution

## Commit Process

1. Stage files: `git add -A`
2. Review: `git diff --staged`
3. Commit with message format:
   ```
   [Type]: Brief description

   - Change 1
   - Change 2

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```

4. Push: `git push origin [branch]`

## Output

Create a log file:
- Filename: `git-update-YYYY-MM-DD.log`
