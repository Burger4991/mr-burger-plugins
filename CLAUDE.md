# mr-burger-plugins

Plugin ecosystem for Claude Code + Cowork. Source of truth for all IR teaching skills, agents, and classroom ops.

Full architecture: `README.md`

## Dev Commands

```bash
# Symlink everything into ~/.claude/ (live editing — no rebuild needed for Claude Code)
./scripts/setup.sh

# Build .plugin packages for Cowork after changes
./scripts/package.sh

# Remove orphan .md stub files from ~/.claude/skills/
./scripts/cleanup.sh
```

## Plugins

| Plugin | Folder | Notes |
|--------|--------|-------|
| ir-teaching | `ir-teaching/` | 62 skills, 11 agents — FL BEST ELA |
| ir-data-pipeline | `ir-data-pipeline/` | 9 skills, 2 agents — student data |
| ir-classroom-ops | `ir-classroom-ops/` | 6 skills — classroom logistics |
| mr-burger-music | `mr-burger-music/` | 7 skills, 2 agents — trumpet, guitar, jazz, band |
| mr-burger-workflow | `mr-burger-workflow/` | 7 skills, 1 agent, commands, hooks |
| ui-ux-pro-max | — | Official plugin, not in this repo |

## Adding Skills/Agents

- Skills: `[plugin]/skills/[skill-name]/skill.md`
- Agents: `[plugin]/agents/[agent-name].md`
- After adding: run `./scripts/setup.sh` to re-symlink; `./scripts/package.sh` for Cowork

## Key Facts

- Edits to skill files are picked up **immediately** by Claude Code via symlinks
- For Cowork: must rebuild packages after every change (`package.sh`)
- All teaching deliverables output as `.md` except slide decks (`.pptx`)
- GitHub: github.com/Burger4991/ir-teaching

## Skill-Loading Architecture (know this)

Three mechanisms load skills simultaneously in Claude Code:

| Mechanism | Source | Who manages it |
|-----------|--------|---------------|
| Custom symlinks | `~/.claude/skills/` → this repo via `setup.sh` | You (setup.sh) |
| Cowork community dirs | `~/.claude/skills/` — actual directories installed by Cowork | Cowork desktop app |
| Plugin cache | `~/.claude/plugins/cache/claude-plugins-official/` | Claude Code plugin system |

**Critical:** `setup.sh` silently skips a custom skill if a Cowork community directory with the same name already exists. If a custom skill stops loading after a Cowork update, check for a shadowing community dir. The warning will now say `WARNING: SKIP skill '...' — a directory already exists`.

**Superpowers dual-presence:** The 14 superpowers skills (brainstorming, executing-plans, etc.) exist as both Cowork-installed directories in `~/.claude/skills/` AND in the plugin cache. Both copies are loaded; the plugin cache version is authoritative for the Skill tool. This is expected behavior — no action needed unless versions drift.
