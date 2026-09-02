#!/usr/bin/env bash
# Propagate a new template version to every location that restates it,
# then verify nothing was missed.
#
# The version lives in six files. Three consecutive releases were bumped by
# hand and each one needed a follow-up grep to catch stragglers. This script
# exists so that never has to be remembered again.
#
# Usage:  maintainer/scripts/bump-version.sh 3.5.0
#         maintainer/scripts/bump-version.sh --check      (verify consistency, change nothing)

set -euo pipefail
cd "$(dirname "$0")/../.."

fail() { printf '\033[31mFAIL\033[0m  %s\n' "$*" >&2; exit 1; }
ok()   { printf '\033[32m  ok\033[0m  %s\n' "$*"; }

CURRENT="$(tr -d '[:space:]' < TEMPLATE_VERSION)"

# ---- --check mode: is the current version stated consistently everywhere? ----
if [ "${1:-}" = "--check" ]; then
  echo "Checking version consistency (expecting $CURRENT)"
  missing=0
  grep -q "template-v${CURRENT}-blue" README.md          || { echo "  README badge"; missing=1; }
  grep -q "Template Version: ${CURRENT}" README.md       || { echo "  README footer"; missing=1; }
  grep -q "version: \"${CURRENT}\"" case-config.yaml     || { echo "  case-config.yaml"; missing=1; }
  grep -q "version: \"${CURRENT}\"" .claude/skills/setup-case.md || { echo "  setup-case.md"; missing=1; }
  grep -q "^version: \"${CURRENT}\"" CITATION.cff        || { echo "  CITATION.cff"; missing=1; }
  grep -q "\*\*Template version\*\*: ${CURRENT}" VERIFICATION_PLEDGE.md || { echo "  VERIFICATION_PLEDGE.md"; missing=1; }
  [ "$missing" -eq 0 ] || fail "version $CURRENT is not stated consistently (see above)"
  ok "all 6 locations agree on $CURRENT"
  exit 0
fi

NEW="${1:-}"
[ -n "$NEW" ] || fail "usage: maintainer/scripts/bump-version.sh X.Y.Z   (or --check)"
[[ "$NEW" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "'$NEW' is not semver (X.Y.Z)"
[ "$NEW" != "$CURRENT" ] || fail "already at $NEW"

echo "Bumping $CURRENT -> $NEW"

printf '%s\n' "$NEW" > TEMPLATE_VERSION
sed -i.bak "s/template-v${CURRENT}-blue/template-v${NEW}-blue/; s/\*Template Version: ${CURRENT}\*/*Template Version: ${NEW}*/" README.md
sed -i.bak "s/^  version: \"${CURRENT}\"/  version: \"${NEW}\"/" case-config.yaml
sed -i.bak "s/version: \"${CURRENT}\"/version: \"${NEW}\"/" .claude/skills/setup-case.md
sed -i.bak "s/^version: \"${CURRENT}\"/version: \"${NEW}\"/; s/^date-released: .*/date-released: \"$(date +%F)\"/" CITATION.cff
sed -i.bak "s/^\*\*Template version\*\*: ${CURRENT}/**Template version**: ${NEW}/" VERIFICATION_PLEDGE.md
find . -name '*.bak' -not -path './.git/*' -delete

"$0" --check

# Stragglers anywhere else? Historical records legitimately keep old versions.
STRAY=$(grep -rn "${CURRENT}" --include='*.md' --include='*.yaml' --include='*.cff' . 2>/dev/null \
  | grep -v '^\./\.git/' \
  | grep -vE 'CHANGELOG|log\.md|lessons_learned|test-log|examples/|golden/|RELEASING' || true)
if [ -n "$STRAY" ]; then
  echo
  echo "Remaining references to $CURRENT outside historical records — review each:"
  echo "$STRAY" | cut -c1-120
  echo "(Historical mentions in CHANGELOG/logs/examples are expected and not shown.)"
fi

echo
echo "Next: add a [$NEW] section to CHANGELOG.md, then run maintainer/scripts/release-preflight.sh"
