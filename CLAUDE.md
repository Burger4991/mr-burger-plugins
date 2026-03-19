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
| ir-teaching | `ir-teaching/` | 55+ skills, 11 agents — FL BEST ELA |
| ir-data-pipeline | `ir-data-pipeline/` | 10 skills, 2 agents — student data |
| ir-classroom-ops | `ir-classroom-ops/` | 6 skills — classroom logistics |
| mr-burger-workflow | `mr-burger-workflow/` | 5 skills, commands, hooks |
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
