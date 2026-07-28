#!/usr/bin/env bash
# Executable version of the RELEASING.md checklist. Run before every push
# to the public template.
#
# Each check corresponds to something that actually went wrong, or nearly did,
# in a previous release: version drift across seven files, a red CI build that
# had been red so long it stopped being read, a release tag that predated the
# feature it was meant to ship, and — the unrecoverable one — the risk of
# publishing copyrighted eval corpus to a public repository.
#
# Usage:  scripts/release-preflight.sh

set -uo pipefail
cd "$(dirname "$0")/.."

PASS=0; WARN=0; FAILED=0
ok()   { printf '\033[32m  ok  \033[0m %s\n' "$*"; PASS=$((PASS+1)); }
warn() { printf '\033[33m warn \033[0m %s\n' "$*"; WARN=$((WARN+1)); }
bad()  { printf '\033[31m FAIL \033[0m %s\n' "$*"; FAILED=$((FAILED+1)); }

VERSION="$(tr -d '[:space:]' < TEMPLATE_VERSION)"
echo "Release preflight — template v$VERSION"
echo

# 1. Working tree
if [ -z "$(git status --porcelain)" ]; then ok "working tree clean"
else bad "uncommitted changes — commit or stash before releasing"; fi

# 2. Version consistency across all seven locations
if ./scripts/bump-version.sh --check >/dev/null 2>&1; then ok "version stated consistently in all 7 locations"
else bad "version drift — run: scripts/bump-version.sh --check"; fi

# 3. Markdown lint (as CI runs it)
if ./scripts/lint.sh >/dev/null 2>&1; then ok "markdown lint clean (tracked files)"
else bad "lint violations — run: scripts/lint.sh"; fi

# 4. CHANGELOG has a section for this version
if grep -q "^## \[$VERSION\]" CHANGELOG.md; then ok "CHANGELOG has a [$VERSION] section"
else bad "no [## $VERSION] section in CHANGELOG.md — releases need notes"; fi

# 5. THE UNRECOVERABLE ONE: no copyrighted eval material staged for publication
LEAK=$(git ls-files | grep -E 'evals/fixtures/[^/]+/(sources|golden)/' || true)
if [ -z "$LEAK" ]; then ok "no eval corpus or golden baselines tracked (copyright)"
else bad "TRACKED copyrighted material — DO NOT PUSH PUBLIC:"; echo "$LEAK" | sed 's/^/         /'; fi

# 6. Remotes configured as RELEASING.md describes
if git remote | grep -qx origin && git remote | grep -qx public; then
  ok "remotes: origin (dev) + public (template)"
  git remote get-url origin | grep -q -- '-dev' || warn "origin does not look like the private dev repo — verify with: git remote -v"
else warn "expected remotes 'origin' and 'public' — see RELEASING.md"; fi

# 7. Tag hygiene — will the release contain what you think it contains?
if git rev-parse "v$VERSION" >/dev/null 2>&1; then
  if [ "$(git rev-parse "v$VERSION^{commit}")" = "$(git rev-parse HEAD)" ]; then
    ok "tag v$VERSION points at HEAD"
  else
    BEHIND=$(git rev-list --count "v$VERSION..HEAD")
    bad "tag v$VERSION is $BEHIND commit(s) behind HEAD — a release from it would omit that work"
  fi
else warn "tag v$VERSION does not exist yet (create it after committing the release)"; fi

# 8. Public remote state
if git rev-parse --verify public/main >/dev/null 2>&1; then
  AHEAD=$(git rev-list --count public/main..HEAD 2>/dev/null || echo '?')
  BEHINDP=$(git rev-list --count HEAD..public/main 2>/dev/null || echo 0)
  [ "$BEHINDP" = "0" ] && ok "public/main has nothing you lack ($AHEAD commit(s) to publish)" \
    || bad "public/main has $BEHINDP commit(s) you don't — fetch and merge first (see RELEASING.md)"
else warn "no cached public/main — run: git fetch public"; fi

# 9. Skills referenced in docs actually exist
MISSING=0
# 'slash-commands' is the generic term for the mechanism, not a skill name.
for s in $(grep -oE '`/[a-z-]+`' README.md AGENTS.md 2>/dev/null | grep -oE '/[a-z-]+' | sort -u | tr -d '/' | grep -vx 'slash-commands'); do
  [ -f ".claude/skills/$s.md" ] || { [ "$MISSING" -eq 0 ] && echo "         missing skill files:"; echo "         .claude/skills/$s.md"; MISSING=1; }
done
[ "$MISSING" -eq 0 ] && ok "every skill named in README/AGENTS exists" || bad "docs reference skills that do not exist"

# 10. Published refs are immutable — local tags must match what remotes already have.
#     Recreating an annotated tag makes a NEW tag object even when it points at the
#     same commit; the push is then rejected mid-run. Amending a pushed commit does
#     the same thing to history. Both happened; both are caught here instead.
TAGDRIFT=0
for remote in origin public; do
  git remote | grep -qx "$remote" || continue
  while read -r sha ref; do
    tag="${ref#refs/tags/}"; tag="${tag%^\{\}}"
    case "$ref" in *'^{}') continue;; esac
    LOCAL=$(git rev-parse "$tag" 2>/dev/null) || continue
    if [ "$LOCAL" != "$sha" ]; then
      [ "$TAGDRIFT" -eq 0 ] && echo "         tag objects differ from remote (do NOT force-push):"
      echo "         $tag  local=${LOCAL:0:7}  $remote=${sha:0:7}"
      TAGDRIFT=1
    fi
  done < <(git ls-remote --tags "$remote" 2>/dev/null | grep -v '\^{}$')
done
if [ "$TAGDRIFT" -eq 0 ]; then ok "local tags match published tags"
else
  bad "local tag objects diverge from a remote — the push will be rejected"
  echo "         Fix: git tag -d <tag> && git fetch <remote> --tags   (adopt the published tag)"
  echo "         Never force-push a tag that others may have pulled."
fi

echo
echo "  $PASS passed, $WARN warning(s), $FAILED failure(s)"
if [ "$FAILED" -gt 0 ]; then
  echo
  printf '\033[31mNot ready to release.\033[0m Fix the failures above.\n'
  exit 1
fi
printf '\033[32mReady.\033[0m  git push origin main --tags  &&  git push public main --tags\n'
