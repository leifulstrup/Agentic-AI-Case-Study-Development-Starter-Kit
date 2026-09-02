# maintainer/

Everything here is for **developing the kit itself**, not for writing a case. If you
cloned this template to build a case study, you can delete this whole directory —
nothing in the authoring or verification workflow depends on it.

| | |
|---|---|
| `scripts/` | Release tooling: version bump, lint, preflight, release notes. Run from the repo root as `maintainer/scripts/<name>.sh` |
| `evals/` | Regression framework: a frozen source corpus (gitignored, copyrighted), 19 seeded defects, and an append-only log of every run |
| `RELEASING.md` | The two-remote release workflow and the rule that published refs are immutable |
| `log.md` | Development log — what changed in each session and why |
| `lessons_learned.md` | What the maintainers got wrong and what it taught. Cited by `READING_A_CASE.md` as teaching material |
| `.gitignore-private` | Alternate ignore file for backing eval assets to the private remote |

The two maintainer skills — `release-kit` and `run-eval` — stay in `.claude/skills/`
because slash-commands must live there. `AGENTS.md` lists them separately and tells
agents not to offer them to case authors.
