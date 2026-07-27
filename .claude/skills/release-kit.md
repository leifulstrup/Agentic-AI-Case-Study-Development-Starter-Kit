# Release Kit

Cut a new version of the starter kit itself. **This is a maintainer skill, not a case-authoring skill** — it is for people developing the template, not for professors or students writing case studies.

## Usage

```
/release-kit
```

## Role

The scripts handle what is deterministic; you handle what requires judgment. Never do by hand what `scripts/` already does — that is how version drift and phantom lint failures got introduced in the first place.

| Decision | Who |
|----------|-----|
| Which version number | You + the user (semver judgment) |
| What the changelog says | You (prose) |
| Whether the release is safe to publish | `scripts/release-preflight.sh` |
| Propagating the version | `scripts/bump-version.sh` |
| Whether markdown is clean | `scripts/lint.sh` |

## Instructions

### 1. Establish what changed

Read `git log <last-tag>..HEAD --oneline` and the `[Unreleased]` section of `CHANGELOG.md`. Summarize the actual change set for the user before proposing anything.

### 2. Propose the version number

Apply semver to a template repository:

- **Major** — a change that breaks existing case projects (renamed config keys, removed skills, restructured directories)
- **Minor** — new skills, new templates, new user-facing capability, additive documentation like `examples/`
- **Patch** — fixes and corrections with no new capability

State your reasoning and let the user confirm. When it is genuinely borderline, say so rather than pretending the rule decides it.

### 3. Write the CHANGELOG section

Promote `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a one-paragraph lead explaining *why* this release exists, not just what is in it. Group under Added / Changed / Fixed / Removed.

Standards for the prose:
- **Every entry says what changed and why it matters.** "Added independence column" is a fact; "tier measures access but nothing measured interest, so a vendor-sponsored transcript looked like a neutral primary source" is a reason.
- **Cite the evidence when a change came from a test.** Real regression numbers belong in the release notes.
- **Report fixes honestly**, including how long a defect had been present. A changelog that only lists wins is marketing.

### 4. Bump

```bash
scripts/bump-version.sh X.Y.Z
```

Do not edit the seven version locations by hand. If the script reports stragglers, resolve each one — historical references in CHANGELOG, logs, and `examples/` are expected and should stay.

### 5. Update the running records

- `log.md` — what changed this session and *why*, including anything surprising. Note environment quirks that cost time; the next session should not rediscover them.
- `lessons_learned.md` — only if something was genuinely learned. Not every release teaches something; padding this file makes it useless.
- `evals/test-log.md` — if the release changes behavior, it needs a regression run first (see `run-eval`). Documentation-only releases do not.

### 6. Preflight

```bash
scripts/release-preflight.sh
```

Nine checks; every one corresponds to something that previously went wrong. Do not proceed past a FAIL, and do not "fix" a check by weakening it. The copyright check in particular is the one error that cannot be undone once published.

### 7. Commit, tag, push

```bash
git add -A && git commit -m "vX.Y.Z — <release name>

<why this release exists, 2-4 lines>"
git tag -a vX.Y.Z -m "<release name>"
scripts/release-preflight.sh          # re-run: the tag check now has something to check
git push origin main --tags           # private dev repo first
git push public main --tags           # public template only when ready
```

Order matters: dev first, so a mistake is caught somewhere invisible.

### 8. Publish the release notes

`.github/workflows/release.yml` creates a GitHub Release automatically when `TEMPLATE_VERSION` changes — *unless the tag already exists*, which it will if you pushed tags in step 7. Check whether the release appeared; if not, create it manually:

```bash
scripts/release-notes.sh X.Y.Z > /tmp/notes-X.Y.Z.md
gh release create vX.Y.Z --repo <public-repo> --title "vX.Y.Z — <name>" \
  --notes-file /tmp/notes-X.Y.Z.md --latest
```

### 9. Verify what shipped

Confirm on the public repository: the check is green, the Latest release points at this version, and the release actually contains the headline feature. A tag cut before the feature landed produces a release missing the thing it was named for — this has happened.

## Notes

- Some environments leave stale `.git/*.lock` files after operations. If git reports a lock error and no other git process is running, remove them.
- If a lint rule is wrong for procedural documents rather than the document being wrong, change the rule in `.markdownlint.json` and justify it in the commit message.
