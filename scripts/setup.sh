#!/usr/bin/env bash
set -e

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "mr-burger-plugins setup"
echo "Repo: $REPO"
echo ""

# --- Gemini CLI symlink ---
GEMINI_EXT="$HOME/.gemini/extensions"
GEMINI_SRC="$REPO/gemini"

if [ -L "$GEMINI_EXT" ]; then
  echo "[gemini] Already symlinked: $GEMINI_EXT -> $(readlink "$GEMINI_EXT")"
elif [ -d "$GEMINI_EXT" ]; then
  if [ -d "$GEMINI_EXT.bak" ]; then
    echo "[gemini] ERROR: $GEMINI_EXT.bak already exists from a prior run. Remove it and re-run."
    exit 1
  fi
  echo "[gemini] Backing up existing extensions to $GEMINI_EXT.bak"
  mv "$GEMINI_EXT" "$GEMINI_EXT.bak"
  ln -s "$GEMINI_SRC" "$GEMINI_EXT"
  echo "[gemini] Symlinked: $GEMINI_EXT -> $GEMINI_SRC"
else
  ln -s "$GEMINI_SRC" "$GEMINI_EXT"
  echo "[gemini] Symlinked: $GEMINI_EXT -> $GEMINI_SRC"
fi

# --- Obsidian symlink (deferred until vault migration completes) ---
# To enable: set OBSIDIAN_VAULT below and uncomment
# OBSIDIAN_VAULT=""
# if [ -n "$OBSIDIAN_VAULT" ] && [ -d "$OBSIDIAN_VAULT" ]; then
#   OBSIDIAN_LINK="$OBSIDIAN_VAULT/Teaching Skills"
#   if [ ! -L "$OBSIDIAN_LINK" ]; then
#     ln -s "$REPO/ir-teaching/skills" "$OBSIDIAN_LINK"
#     echo "[obsidian] Symlinked: $OBSIDIAN_LINK -> $REPO/ir-teaching/skills"
#   else
#     echo "[obsidian] Already symlinked."
#   fi
# else
#   echo "[obsidian] Skipped — vault path not set (pending vault migration)"
# fi

echo ""
echo "Done. Update Claude Code marketplace path in ~/.claude/settings.json if not already done."
echo "  Set: extraKnownMarketplaces.mr-burger-plugins.source.path = $REPO"
