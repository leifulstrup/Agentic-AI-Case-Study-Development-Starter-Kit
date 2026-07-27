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

Then on GitHub: create a Release from the new tag so the CHANGELOG entry is visible to adopters. Verify the repo's "Template repository" setting is still enabled.

**Pre-publish checklist**
- [ ] `evals/test-log.md` has a passing run for this version
- [ ] `CHANGELOG.md` entry written; `TEMPLATE_VERSION`, README badge, `case-config.yaml` template version all bumped and consistent
- [ ] `log.md` and `lessons_learned.md` updated
- [ ] No copyrighted source material staged (see below)
- [ ] Skills referenced in README/AGENTS/WORKFLOW all exist

## Eval assets and copyright

`.gitignore` excludes `evals/fixtures/*/sources/` and `golden/` because those hold copyrighted source material and derived baselines that must not be publicly redistributed.

In the **private** repo it is reasonable to commit them (private ≠ distribution) so the corpus and blessed baselines are backed up and versioned rather than living on one laptop. To do that, copy `.gitignore-private` over `.gitignore` **on a branch that is never pushed to `public`**, or simply force-add the paths:

```bash
git add -f evals/fixtures/jpm-llm-suite/sources evals/fixtures/jpm-llm-suite/golden
git commit -m "Back up eval corpus and golden baselines (private only)"
git push origin main
```

**Never push those commits to `public`.** If they were ever added to a shared history, removing them requires a history rewrite. Safer alternative if you're unsure: keep them out of git entirely and back them up to your own storage — see `evals/EVALS.md`.

## Versioning

The template follows semantic versioning with a continuous lineage (v3.1.0 → v3.2.0 → …), recorded in `TEMPLATE_VERSION`, `CHANGELOG.md`, and `case-config.yaml`. Marketing names for public relaunches ("Starter Kit 2.0") are separate from this internal version number; don't restart the number sequence, or the logs, tags, and eval history stop lining up.
