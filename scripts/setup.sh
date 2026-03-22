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
OBSIDIAN_VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Teaching/Teaching"
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

# --- Claude Code: symlink skills and agents from all plugins ---
CLAUDE_SKILLS="$HOME/.claude/skills"
CLAUDE_AGENTS="$HOME/.claude/agents"
CLAUDE_COMMANDS="$HOME/.claude/commands"

mkdir -p "$CLAUDE_SKILLS" "$CLAUDE_AGENTS" "$CLAUDE_COMMANDS"

link_skills() {
  local plugin="$1"
  local skills_dir="$REPO/$plugin/skills"
  if [ ! -d "$skills_dir" ]; then return; fi
  for skill in "$skills_dir"/*/; do
    local name="$(basename "$skill")"
    local target="$CLAUDE_SKILLS/$name"
    if [ -L "$target" ]; then
      : # already linked
    elif [ -e "$target" ]; then
      echo "[claude-code] WARNING: SKIP skill '$name' — a directory already exists at $target (likely Cowork community install). Custom skill is shadowed and will NOT load."
    else
      ln -s "$skill" "$target"
      echo "[claude-code] Linked skill: $name"
    fi
  done
  # also handle .md file skills (flat files)
  for skill in "$skills_dir"/*.md; do
    [ -e "$skill" ] || continue
    local name="$(basename "$skill")"
    local target="$CLAUDE_SKILLS/$name"
    if [ -L "$target" ] || [ -e "$target" ]; then : ; else
      ln -s "$skill" "$target"
      echo "[claude-code] Linked skill: $name"
    fi
  done
}

link_agents() {
  local plugin="$1"
  local agents_dir="$REPO/$plugin/agents"
  if [ ! -d "$agents_dir" ]; then return; fi
  for agent in "$agents_dir"/*.md; do
    [ -e "$agent" ] || continue
    local name="$(basename "$agent")"
    local target="$CLAUDE_AGENTS/$name"
    if [ -L "$target" ]; then
      : # already linked
    elif [ -e "$target" ]; then
      echo "[claude-code] WARNING: SKIP agent '$name' — a file already exists at $target (not a symlink). Custom agent is shadowed."
    else
      ln -s "$agent" "$target"
      echo "[claude-code] Linked agent: $name"
    fi
  done
}

link_commands() {
  local plugin="$1"
  local commands_dir="$REPO/$plugin/commands"
  if [ ! -d "$commands_dir" ]; then return; fi
  for cmd in "$commands_dir"/*.md; do
    [ -e "$cmd" ] || continue
    local name="$(basename "$cmd")"
    local target="$CLAUDE_COMMANDS/$name"
    if [ -L "$target" ]; then
      : # already linked
    elif [ -e "$target" ]; then
      echo "[claude-code] WARNING: SKIP command '$name' — a file already exists at $target (not a symlink). Custom command is shadowed."
    else
      ln -s "$cmd" "$target"
      echo "[claude-code] Linked command: $name"
    fi
  done
}

for plugin in ir-teaching ir-data-pipeline ir-classroom-ops mr-burger-workflow mr-burger-music; do
  link_skills "$plugin"
  link_agents "$plugin"
  link_commands "$plugin"
done

echo "[claude-code] Skills: $(ls "$CLAUDE_SKILLS" | wc -l | tr -d ' ') linked"
echo "[claude-code] Agents: $(ls "$CLAUDE_AGENTS" | wc -l | tr -d ' ') linked"
echo "[claude-code] Commands: $(ls "$CLAUDE_COMMANDS" | wc -l | tr -d ' ') linked"

echo ""
echo "Done. Update Claude Code marketplace path in ~/.claude/settings.json if not already done."
echo "  Set: extraKnownMarketplaces.mr-burger-plugins.source.path = $REPO"
