#!/bin/bash
# ============================================================
# Restore Mr. Burger Plugins for Claude Code from GitHub
# ============================================================
# Clones the repo, copies each plugin into ~/.claude/plugins/,
# then merges any local-only files from your source folder.
#
# Usage:
#   chmod +x restore-claude-code.sh
#   ./restore-claude-code.sh
# ============================================================

set -euo pipefail

PLUGIN_DIR="$HOME/.claude/plugins"
LOCAL_SRC="$HOME/Documents/Tech/mr-burger-plugins"
REPO="https://github.com/burger4991/mr-burger-plugins.git"
TMP_CLONE="/tmp/mr-burger-plugins-restore"

ALL_PLUGINS=(
  "ir-teaching"
  "ir-classroom-ops"
  "ir-data-pipeline"
  "mr-burger-workflow"
  "ui-ux-pro-max"
)

echo ""
echo "  Mr. Burger Plugins — Claude Code Restore"
echo "  ========================================="
echo ""

# Step 1: Clone from GitHub
echo "  [1/4] Cloning from GitHub..."
rm -rf "$TMP_CLONE"
git clone --depth 1 "$REPO" "$TMP_CLONE" 2>/dev/null
echo "        Done."

# Step 2: Create plugins directory
echo "  [2/4] Preparing ~/.claude/plugins/..."
mkdir -p "$PLUGIN_DIR"

# Step 3: Install each plugin
echo "  [3/4] Installing plugins..."
installed=0

for plugin in "${ALL_PLUGINS[@]}"; do
  src="$TMP_CLONE/$plugin"
  dest="$PLUGIN_DIR/$plugin"

  if [ ! -d "$src" ]; then
    echo "        SKIP: $plugin (not in repo)"
    continue
  fi

  # Remove old install
  [ -d "$dest" ] && rm -rf "$dest"

  # Copy from clone
  cp -r "$src" "$dest"

  # Remove any .DS_Store
  find "$dest" -name '.DS_Store' -delete 2>/dev/null || true

  # Verify
  if [ -f "$dest/.claude-plugin/plugin.json" ]; then
    version=$(python3 -c "import json; print(json.load(open('$dest/.claude-plugin/plugin.json'))['version'])" 2>/dev/null || echo "?")
    echo "        OK: $plugin v$version"
    ((installed++)) || true
  else
    echo "        WARN: $plugin (no plugin.json)"
    ((installed++)) || true
  fi
done

# Step 4: Merge local-only files (ones never pushed to GitHub)
echo "  [4/4] Merging local-only files from $LOCAL_SRC..."
merged=0

if [ -d "$LOCAL_SRC" ]; then
  for plugin in "${ALL_PLUGINS[@]}"; do
    local_plugin="$LOCAL_SRC/$plugin"
    dest="$PLUGIN_DIR/$plugin"

    if [ ! -d "$local_plugin" ] || [ ! -d "$dest" ]; then
      continue
    fi

    # Find files that exist locally but not in the installed copy
    while IFS= read -r -d '' file; do
      rel="${file#$local_plugin/}"
      target="$dest/$rel"
      if [ ! -f "$target" ]; then
        mkdir -p "$(dirname "$target")"
        cp "$file" "$target" 2>/dev/null && ((merged++)) || true
      fi
    done < <(find "$local_plugin" -type f ! -path '*/.git/*' ! -name '.DS_Store' -print0)
  done

  if [ "$merged" -gt 0 ]; then
    echo "        Merged $merged local-only files"
  else
    echo "        No extra local files to merge"
  fi
else
  echo "        Local source not found at $LOCAL_SRC — skipping merge"
fi

# Cleanup
rm -rf "$TMP_CLONE"

echo ""
echo "  Done: $installed plugins installed to $PLUGIN_DIR"
echo ""

# Summary
echo "  Installed plugins:"
for plugin in "${ALL_PLUGINS[@]}"; do
  dest="$PLUGIN_DIR/$plugin"
  if [ -d "$dest" ]; then
    files=$(find "$dest" -type f ! -name '.DS_Store' | wc -l | tr -d ' ')
    skills=$(find "$dest/skills" -name 'skill.md' -o -name 'SKILL.md' 2>/dev/null | wc -l | tr -d ' ')
    agents=$(find "$dest/agents" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
    echo "    $plugin — $files files, $skills skills, $agents agents"
  fi
done
echo ""
