#!/bin/bash
# ============================================================
# Mr. Burger Plugins — Install + Recovery Script
# ============================================================
#
# This script:
#   1. Installs plugin zips into ~/.claude/plugins/
#   2. Recovers missing files from your original source
#
# Usage:
#   chmod +x install-plugins.sh
#   ./install-plugins.sh
#
# Or install specific plugins:
#   ./install-plugins.sh ir-teaching mr-burger-workflow
# ============================================================

set -euo pipefail

PLUGIN_DIR="$HOME/.claude/plugins"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKUP_DIR="$HOME/Documents/Tech/mr-burger-plugins"

ALL_PLUGINS=(
  "ir-teaching"
  "ir-classroom-ops"
  "ir-data-pipeline"
  "mr-burger-workflow"
  "ui-ux-pro-max"
)

if [ $# -gt 0 ]; then
  PLUGINS=("$@")
else
  PLUGINS=("${ALL_PLUGINS[@]}")
fi

echo ""
echo "  Mr. Burger Plugins — Installer"
echo "  ==============================="
echo ""

mkdir -p "$PLUGIN_DIR"

installed=0
recovered=0
failed=0

for plugin in "${PLUGINS[@]}"; do
  zip_file="$SCRIPT_DIR/${plugin}.zip"
  target_dir="$PLUGIN_DIR/$plugin"
  backup_plugin="$BACKUP_DIR/$plugin"

  if [ ! -f "$zip_file" ]; then
    echo "  SKIP  $plugin (zip not found)"
    ((failed++)) || true
    continue
  fi

  # Remove old install
  [ -d "$target_dir" ] && rm -rf "$target_dir"

  # Extract packaged files
  unzip -qo "$zip_file" -d "$PLUGIN_DIR"

  # Verify plugin.json
  if [ -f "$target_dir/.claude-plugin/plugin.json" ]; then
    version=$(python3 -c "import json; print(json.load(open('$target_dir/.claude-plugin/plugin.json'))['version'])" 2>/dev/null || echo "?")
    echo "  OK    $plugin v$version"
    ((installed++)) || true
  else
    echo "  WARN  $plugin — plugin.json missing"
    ((installed++)) || true
  fi

  # Recovery: copy missing files from backup
  if [ -d "$backup_plugin" ]; then
    count=0
    while IFS= read -r -d '' file; do
      rel="${file#$backup_plugin/}"
      dest="$target_dir/$rel"
      if [ ! -f "$dest" ] || [ ! -s "$dest" ]; then
        mkdir -p "$(dirname "$dest")"
        cp "$file" "$dest" 2>/dev/null && ((count++)) || true
      fi
    done < <(find "$backup_plugin" -type f ! -path '*/.git/*' ! -name '.DS_Store' -print0)

    if [ "$count" -gt 0 ]; then
      echo "        + recovered $count files from backup"
      recovered=$((recovered + count))
    fi
  fi
done

echo ""
echo "  Done: $installed plugins installed"
[ "$recovered" -gt 0 ] && echo "        $recovered files recovered from backup"
[ "$failed" -gt 0 ] && echo "        $failed plugins skipped"
echo ""
echo "  Installed to: $PLUGIN_DIR"
echo ""

# Final check
total_files=0
for plugin in "${PLUGINS[@]}"; do
  target_dir="$PLUGIN_DIR/$plugin"
  if [ -d "$target_dir" ]; then
    pcount=$(find "$target_dir" -type f ! -name '.DS_Store' | wc -l)
    total_files=$((total_files + pcount))
  fi
done
echo "  Total files across all plugins: $total_files"
echo ""
