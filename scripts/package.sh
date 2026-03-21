#!/usr/bin/env bash
set -e

# ============================================================
# Package plugins for Cowork installation
#
# Builds .plugin and .zip files from source directories.
# Run this after editing skills/agents to update Cowork packages.
#
# Usage:
#   ./scripts/package.sh                    # Package all plugins
#   ./scripts/package.sh ir-teaching        # Package one plugin
# ============================================================

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGES_DIR="$REPO/packages"

ALL_PLUGINS=(
  "ir-teaching"
  "ir-classroom-ops"
  "ir-data-pipeline"
  "mr-burger-workflow"
)

if [ $# -gt 0 ]; then
  PLUGINS=("$@")
else
  PLUGINS=("${ALL_PLUGINS[@]}")
fi

echo ""
echo "  mr-burger-plugins — Package Builder"
echo "  ===================================="
echo ""

mkdir -p "$PACKAGES_DIR"

built=0
failed=0

for plugin in "${PLUGINS[@]}"; do
  plugin_dir="$REPO/$plugin"

  if [ ! -d "$plugin_dir" ]; then
    echo "  SKIP  $plugin (directory not found)"
    ((failed++)) || true
    continue
  fi

  # Check for .claude-plugin manifest or create minimal one
  manifest_dir="$plugin_dir/.claude-plugin"
  if [ ! -d "$manifest_dir" ]; then
    mkdir -p "$manifest_dir"
    # Read version from existing manifest if available, otherwise default
    cat > "$manifest_dir/manifest.json" <<MANIFEST
{
  "name": "$plugin",
  "version": "3.0.0",
  "description": "Mr. Burger plugin: $plugin",
  "author": { "name": "Mr. Burger" }
}
MANIFEST
    echo "  NOTE  Created manifest for $plugin"
  fi

  # Build .zip (used by install script)
  zip_file="$PACKAGES_DIR/${plugin}.zip"
  rm -f "$zip_file"
  (cd "$REPO" && zip -rq "$zip_file" "$plugin/" \
    -x "$plugin/.git/*" \
    -x "$plugin/.DS_Store" \
    -x "$plugin/**/.DS_Store" \
    -x "$plugin/.mcpb-cache/*" \
    -x "$plugin/*-eval-review.html")

  # Build .plugin (same as .zip, just renamed for Cowork)
  plugin_file="$PACKAGES_DIR/${plugin}.plugin"
  cp "$zip_file" "$plugin_file"

  # Also copy .plugin to repo root for easy access
  cp "$plugin_file" "$REPO/${plugin}.plugin"

  size=$(du -h "$zip_file" | cut -f1)
  echo "  OK    $plugin ($size)"
  ((built++)) || true
done

echo ""
echo "  Done: $built plugins packaged"
[ "$failed" -gt 0 ] && echo "        $failed plugins skipped"
echo ""
echo "  Packages written to: $PACKAGES_DIR/"
echo ""
echo "  Next steps:"
echo "    - Install to Cowork:  ./packages/install-plugins.sh"
echo "    - Or drag .plugin files into Cowork plugin manager"
echo ""
