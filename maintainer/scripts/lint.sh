#!/usr/bin/env bash
# Lint markdown exactly the way CI does — against TRACKED files only.
#
# Why this exists: CI checks out the repository, so gitignored content (the eval
# corpus, golden baselines) never reaches it. Linting the working directory
# locally reported 78 violations where CI saw 10; the 68 phantoms hid the real
# ones and cost a full diagnostic cycle. Lint what CI lints.
#
# Usage:  maintainer/scripts/lint.sh            lint tracked markdown
#         maintainer/scripts/lint.sh --fix      apply markdownlint's safe autofixes

set -euo pipefail
cd "$(dirname "$0")/../.."

if command -v markdownlint >/dev/null 2>&1; then
  MDL="markdownlint"
elif command -v npx >/dev/null 2>&1; then
  MDL="npx --yes markdownlint-cli"
else
  echo "markdownlint not found. Install with:  npm install -g markdownlint-cli" >&2
  exit 127
fi

# .github is excluded in CI; match that.
# Read into the array with a while-read loop rather than `mapfile`: mapfile is a
# bash 4+ builtin, and macOS still ships bash 3.2 as /bin/bash. Under 3.2 the
# script aborted here, and because release-preflight.sh discarded stderr it
# reported the crash as "lint violations" — a substantive verdict it never
# reached. Same shape as the release workflow that silently no-opped and the
# preflight check that passed without reaching a remote. Keep this POSIX-ish.
FILES=()
while IFS= read -r f; do
  [ -n "$f" ] && FILES+=("$f")
done < <(git ls-files '*.md' | grep -v '^\.github/')
[ "${#FILES[@]}" -gt 0 ] || { echo "no tracked markdown files"; exit 0; }

echo "Linting ${#FILES[@]} tracked markdown files (gitignored content excluded, as in CI)"

if [ "${1:-}" = "--fix" ]; then
  $MDL --fix "${FILES[@]}" || true
  echo "Autofixes applied. Re-running check:"
fi

if $MDL "${FILES[@]}"; then
  printf '\033[32m  ok\033[0m  0 violations\n'
else
  printf '\033[31mFAIL\033[0m  see violations above\n' >&2
  echo >&2
  echo "Note: rules are configured in .markdownlint.json. If a rule is wrong for" >&2
  echo "procedural documents rather than the document being wrong, change the rule" >&2
  echo "and say why in the commit message." >&2
  exit 1
fi
