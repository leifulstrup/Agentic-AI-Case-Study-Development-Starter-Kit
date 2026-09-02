# Releasing — the two-remote workflow

*How development work stays private while the public template stays stable for students and other faculty.*

## The shape of it

GitHub visibility is per-repository — a repo is entirely public or entirely private; there is no private branch inside a public repo. So this project uses **two GitHub repos and one local clone**. Your laptop is the junction; the two repos never talk to each other directly.

```
local clone (single git history)
   ├── git push              →  PRIVATE dev repo   (daily work, eval assets, experiments)
   └── git push public main  →  PUBLIC template    (curated releases only)
```

Because both remotes receive the *same commits* from one history, the public repo's lineage, tags, and CHANGELOG stay continuous. This is deliberately not a fork: forking creates two histories that drift and must be reconciled by hand.

The repos in use:

| Remote | Repository | Role |
|--------|-----------|------|
| `origin` | `leifulstrup/Agentic-AI-Case-Study-Starter-Kit-dev` (private) | Daily work, eval corpus, experiments. Always the newest state. |
| `public` | `leifulstrup/Agentic-AI-Case-Study-Development-Starter-Kit` (public template) | What students and other faculty clone. Always behind, by design. |

## Direction of flow — read this first

**Development flows dev → public, never the reverse.** The public template is a *publishing target*, not a source. It contains only what you deliberately push to it, so the dev repo is always the newest version of the kit. There is no routine step for "updating dev from public" — dev is already ahead.

```
dev repo  ──── you publish ────►  public template
(always ahead)                     (always behind, by design)
```

The one exception is covered under [When the public repo gets ahead](#when-the-public-repo-gets-ahead).

## One-time setup

```bash
# make the private repo the default push target
git remote rename origin public
git remote add origin https://github.com/<you>/<private-dev-repo>.git
git push -u origin main --tags
```

Verify with `git remote -v` — you should see `origin` (private) and `public`.

## Daily work

```bash
git add -A && git commit -m "..."
git push                    # → private repo. Safe. Invisible to students.
```

## Publishing a release

Only when a version is tested and stable:

```bash
git push public main --tags
```

Pushing the tag publishes the GitHub Release automatically — `.github/workflows/release.yml` is triggered by the tag, extracts the matching CHANGELOG section, and creates the release. Publishing a version and publishing its notes are the same action, so neither can be forgotten without the other.

If the Actions run goes red, it is almost certainly a missing `## [X.Y.Z]` CHANGELOG section. The workflow fails on purpose rather than shipping empty boilerplate; fix the changelog and re-run the job. `scripts/release-notes.sh` plus `gh release create` remains the manual fallback.

Also verify the repo's "Template repository" setting is still enabled.

> **Design note.** This workflow used to trigger on changes to `TEMPLATE_VERSION` and then skip if the tag already existed. Because releases are pushed as `git push main --tags`, the tag always arrived with the commit and the workflow stood down every time — silently, for six consecutive releases. Triggering on the tag removes the failure mode. It also keeps tags authored locally, so there is one authority for tags and preflight check 10 stays meaningful.

**Pre-publish checks are executable.** Do not run this list by hand:

```bash
scripts/release-preflight.sh
```

Eleven checks, each corresponding to something that previously went wrong: uncommitted changes, version drift across the seven files that restate it, lint failures, a missing CHANGELOG section, **copyrighted eval material staged for publication** (the one unrecoverable error), misconfigured remotes, a release tag that lags HEAD, a public remote you are behind, documentation referencing skills that do not exist, a local tag object that diverges from a published one, and **machine-specific paths in tracked files** — this is a public template, and a maintainer's home directory structure has no business in it.

The one thing the script cannot judge: whether `evals/test-log.md` has a passing run for behavior changes. Documentation-only releases do not need one; anything touching a skill does.

**Supporting scripts:**

| Script | Purpose |
|--------|---------|
| `scripts/bump-version.sh X.Y.Z` | Propagate a version to all six locations and verify; `--check` audits consistency without changing anything |
| `scripts/lint.sh` | Lint tracked markdown exactly as CI does (`--fix` applies safe autofixes) |
| `scripts/release-preflight.sh` | The eleven checks above |
| `scripts/release-notes.sh X.Y.Z` | Extract a CHANGELOG section for `gh release create --notes-file` |

Claude Code users: `/release-kit` runs this whole workflow, making the judgment calls (version number, changelog prose) and delegating the deterministic parts to these scripts.

## When the public repo gets ahead

Only happens if changes are made *directly on GitHub* in the public repo — a README typo fixed in the web UI, or a merged pull request from another professor. That commit exists in `public` but not in your history. Bring it back before your next release:

```bash
git fetch public
git merge public/main      # bring that commit into local history
git push origin main       # dev now has it too
```

Skip this and the next `git push public main` is rejected for divergent histories.

**The habit that avoids it entirely:** never edit the public repo on GitHub. Make every change locally, commit, push to dev, publish when ready. If a contributor opens a PR, merging it on GitHub is fine — just remember to fetch/merge afterward.

## Eval assets and copyright

`.gitignore` excludes `evals/fixtures/*/sources/` and `golden/` because those hold copyrighted source material and derived baselines that must not be publicly redistributed.

In the **private** repo it is reasonable to commit them (private ≠ distribution) so the corpus and blessed baselines are backed up and versioned rather than living on one laptop. To do that, copy `.gitignore-private` over `.gitignore` **on a branch that is never pushed to `public`**, or simply force-add the paths:

```bash
git add -f evals/fixtures/jpm-llm-suite/sources evals/fixtures/jpm-llm-suite/golden
git commit -m "Back up eval corpus and golden baselines (private only)"
git push origin main
```

**Never push those commits to `public`.** If they were ever added to a shared history, removing them requires a history rewrite. Safer alternative if you're unsure: keep them out of git entirely and back them up to your own storage — see `evals/EVALS.md`.

## Published refs are immutable

Once a commit or tag has been pushed, treat it as permanent.

- **Amending a pushed commit** creates a divergent commit with the same version number. Ship a patch release instead.
- **Recreating a pushed tag** makes a new tag object even when it points at the same commit, and the push is rejected part-way through, after other refs have already landed. Adopt the published tag instead: `git tag -d <tag> && git fetch <remote> --tags`.
- If a tag genuinely must move, delete it on the remote deliberately (`git push --delete public vX.Y.Z`) so the change is visible, rather than force-pushing over it.

Preflight checks 8 and 10 catch both cases. Push targets with a semicolon rather than `&&` — they are independent remotes, and a rejected ref on one should not silently skip the other.

## Why these are scripts

Three consecutive releases were done by hand, and each manual step failed at least once: version drift needed a follow-up grep every time, local linting disagreed with CI because it included gitignored files, and a release was nearly cut from a tag that predated the feature it was named for. None of those were hard problems — they were memory problems. The scripts exist so the next release does not depend on remembering.

## Versioning

The template follows semantic versioning with a continuous lineage (v3.1.0 → v3.2.0 → …), recorded in `TEMPLATE_VERSION`, `CHANGELOG.md`, and `case-config.yaml`. Marketing names for public relaunches ("Starter Kit 2.0") are separate from this internal version number; don't restart the number sequence, or the logs, tags, and eval history stop lining up.
