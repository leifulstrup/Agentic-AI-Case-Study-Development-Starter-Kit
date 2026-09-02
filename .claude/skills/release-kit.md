# Release Kit

Cut a new version of the starter kit itself. **This is a maintainer skill, not a case-authoring skill** — it is for people developing the template, not for professors or students writing case studies.

## Usage

```
/release-kit
```

## Role

The scripts handle what is deterministic; you handle what requires judgment. Never do by hand what `maintainer/scripts/` already does — that is how version drift and phantom lint failures got introduced in the first place.

| Decision | Who |
|----------|-----|
| Which version number | You + the user (semver judgment) |
| What the changelog says | You (prose) |
| Whether the release is safe to publish | `maintainer/scripts/release-preflight.sh` |
| Propagating the version | `maintainer/scripts/bump-version.sh` |
| Whether markdown is clean | `maintainer/scripts/lint.sh` |

## The one rule that is not negotiable

**Anything already pushed is immutable — commits and tags alike.**

Both halves of that have been violated once and cost a cleanup:

- **Never `git commit --amend` a commit that has been pushed.** The amend creates a different commit carrying the same version number as one already published. Ship the correction as a patch release instead.
- **Never recreate or move a tag that has been pushed.** An annotated tag is an object; recreating it produces a *new object* even when it points at the same commit, and the push is rejected mid-run — after some refs have already landed. If a local tag has drifted, adopt the published one: `git tag -d <tag> && git fetch <remote> --tags`.

Before any `--amend` or `git tag -f`, ask one question: *has this been pushed?* If yes or unsure, don't. `maintainer/scripts/release-preflight.sh` checks 8 and 10 catch both, but the check is a backstop, not permission to skip the question.

**Push targets separately.** Use `git push origin main --tags; git push public main --tags` with a semicolon, not `&&`. They are independent remotes, and a rejected ref on the first should not silently skip the second.

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
maintainer/scripts/bump-version.sh X.Y.Z
```

Do not edit the seven version locations by hand. If the script reports stragglers, resolve each one — historical references in CHANGELOG, logs, and `examples/` are expected and should stay.

### 5. Update the running records

- `maintainer/log.md` — what changed this session and *why*, including anything surprising. Note environment quirks that cost time; the next session should not rediscover them.
- `maintainer/lessons_learned.md` — only if something was genuinely learned. Not every release teaches something; padding this file makes it useless.
- `maintainer/evals/test-log.md` — if the release changes behavior, it needs a regression run first (see `run-eval`). Documentation-only releases do not.

### 6. Preflight

```bash
maintainer/scripts/release-preflight.sh
```

Nine checks; every one corresponds to something that previously went wrong. Do not proceed past a FAIL, and do not "fix" a check by weakening it. The copyright check in particular is the one error that cannot be undone once published.

### 7. Commit, tag, push

```bash
git add -A && git commit -m "vX.Y.Z — <release name>

<why this release exists, 2-4 lines>"
git tag -a vX.Y.Z -m "<release name>"
maintainer/scripts/release-preflight.sh          # re-run: the tag check now has something to check
git push origin main --tags; \
git push public main --tags           # semicolon: independent targets, don't chain
```

Order matters: dev first, so a mistake is caught somewhere invisible.

### 8. Confirm the release published

Pushing the tag in step 7 triggers `.github/workflows/release.yml`, which reads the CHANGELOG section for that version and creates the GitHub Release. There is no separate publish step — the tag push *is* the publish.

Check the Actions tab. Two outcomes:

- **Green** — the release exists with the changelog as its body. Done.
- **Red** — almost always a missing or empty `## [X.Y.Z]` section in CHANGELOG.md. The workflow fails deliberately rather than shipping "see CHANGELOG for details" boilerplate, because an empty release looks fine and tells a reader nothing. Fix the changelog, then re-run the job from the Actions tab.

Manual fallback, if the workflow is broken or the tag was pushed before the workflow existed:

```bash
maintainer/scripts/release-notes.sh X.Y.Z > /tmp/notes-X.Y.Z.md
gh release create vX.Y.Z --repo <public-repo> --title "vX.Y.Z" \
  --notes-file /tmp/notes-X.Y.Z.md --latest
```

### 9. Verify what shipped

Confirm on the public repository: the check is green, the Latest release points at this version, and the release actually contains the headline feature. A tag cut before the feature landed produces a release missing the thing it was named for — this has happened.

## Notes

- Some environments leave stale `.git/*.lock` files after operations. If git reports a lock error and no other git process is running, remove them.
- If a lint rule is wrong for procedural documents rather than the document being wrong, change the rule in `.markdownlint.json` and justify it in the commit message.
