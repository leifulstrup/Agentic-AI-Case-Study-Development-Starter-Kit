#!/usr/bin/env bash
# Print the CHANGELOG section for a version, ready to pipe into `gh release create`.
#
# Usage:  maintainer/scripts/release-notes.sh 3.4.0
#         maintainer/scripts/release-notes.sh            (uses TEMPLATE_VERSION)
#         maintainer/scripts/release-notes.sh 3.4.0 > /tmp/notes.md

set -euo pipefail
cd "$(dirname "$0")/../.."

VERSION="${1:-$(tr -d '[:space:]' < TEMPLATE_VERSION)}"

grep -q "^## \[$VERSION\]" CHANGELOG.md || {
  echo "No [## $VERSION] section in CHANGELOG.md. Available:" >&2
  grep -oE '^## \[[0-9]+\.[0-9]+\.[0-9]+\]' CHANGELOG.md | tr -d '#[] ' | sed 's/^/  /' >&2
  exit 1
}

# From this version's heading to the next version heading, dropping both.
awk -v v="$VERSION" '
  $0 ~ "^## \\[" v "\\]" { inside=1; next }
  inside && /^## \[/     { exit }
  inside                 { print }
' CHANGELOG.md | sed -e '/./,$!d' | awk 'NF {p=1} p' | sed -e :a -e '/^\n*$/{$d;N;ba' -e '}'
