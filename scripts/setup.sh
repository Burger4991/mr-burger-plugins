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

# --- Obsidian symlink ---
OBSIDIAN_VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
OBSIDIAN_LINK="$OBSIDIAN_VAULT/Teaching Skills"

if [ -d "$OBSIDIAN_VAULT" ]; then
  if [ -L "$OBSIDIAN_LINK" ]; then
    echo "[obsidian] Already symlinked: $OBSIDIAN_LINK -> $(readlink "$OBSIDIAN_LINK")"
  else
    ln -s "$REPO/ir-teaching/skills" "$OBSIDIAN_LINK"
    echo "[obsidian] Symlinked: $OBSIDIAN_LINK -> $REPO/ir-teaching/skills"
  fi
else
  echo "[obsidian] Skipped — vault not found at $OBSIDIAN_VAULT"
fi

echo ""
echo "Done. Update Claude Code marketplace path in ~/.claude/settings.json if not already done."
echo "  Set: extraKnownMarketplaces.mr-burger-plugins.source.path = $REPO"
