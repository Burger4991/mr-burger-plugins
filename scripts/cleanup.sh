#!/usr/bin/env bash
set -e

# ============================================================
# Cleanup orphan .md stub files from ~/.claude/skills/
#
# These are old flat-file skills that now have folder equivalents
# (symlinked from mr-burger-plugins). The stubs cause routing
# confusion because Claude Code sees two entries for the same skill.
# ============================================================

CLAUDE_SKILLS="$HOME/.claude/skills"
removed=0
skipped=0

echo ""
echo "  Cleanup: Remove orphan .md stubs from ~/.claude/skills/"
echo "  ======================================================="
echo ""

if [ ! -d "$CLAUDE_SKILLS" ]; then
  echo "  ERROR: $CLAUDE_SKILLS not found"
  exit 1
fi

for md in "$CLAUDE_SKILLS"/*.md; do
  [ -e "$md" ] || continue
  base="${md%.md}"
  name="$(basename "$base")"

  # Skip if there's no matching folder or symlink
  if [ -L "$base" ] || [ -d "$base" ]; then
    rm "$md" && echo "  Removed: $name.md" && ((removed++)) || true
  else
    ((skipped++)) || true
  fi
done

echo ""
echo "  Done: $removed stubs removed, $skipped standalone .md files kept"
echo ""
