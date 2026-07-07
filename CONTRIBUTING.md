# Contributing

Contributions from professors, students, and case-method practitioners are welcome — new skills, rubrics, templates, harness support, bug fixes, and documentation improvements.

## Ground rules

**1. The verified-body invariant.** Any skill that generates content for students or instructors (documents, slides, personas, quizzes) must draw only from the four verified case documents and `case-config.yaml` — never from raw sources directly and never from model general knowledge without logging verification debt. PRs adding generator skills must state what the skill reads and what provenance it emits.

**2. Conversation-first.** Skills ask questions conversationally and write files programmatically. Never require the user to hand-edit `.yaml` or `.md` files.

**3. Every claim in kit documentation needs a source.** We hold the kit's own docs to the standard the kit enforces. If you cite a statistic, adoption figure, or vendor capability, link the primary source. Capability claims about AI harnesses decay quickly — date-stamp them.

**4. Cross-harness awareness.** Canonical behavioral guidance lives in `AGENTS.md`. `CLAUDE.md` and `.github/copilot-instructions.md` are thin adapters — don't duplicate content into them; extend `AGENTS.md` instead.

## How to contribute

1. Open an issue first for anything larger than a typo fix (use the issue templates).
2. Fork, branch, and keep PRs focused — one skill or one template per PR.
3. For new skills: follow the format of existing files in `.claude/skills/`, add the skill to the tables in `AGENTS.md`, `README.md`, and `WORKFLOW.md`, and add a natural-language equivalent to `.github/copilot-instructions.md`.
4. Test your change with at least one agentic harness and say which one (and which model) in the PR description.
5. Update `CHANGELOG.md` under `[Unreleased]`.

## What we especially want

- Rubrics with classroom validation experience
- Discipline-specific adaptations (finance, marketing, operations, public policy)
- Worked example excerpts (with publication rights cleared)
- Harness test reports for the compatibility matrix
- Engagement survey results from real course use

## Licensing of contributions

By contributing, you agree your contribution is licensed under the repository's MIT license.
