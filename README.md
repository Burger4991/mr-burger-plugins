# mr-burger-plugins

A plugin ecosystem for 10th grade Intensive Reading instruction, student data analysis, classroom operations, and personal productivity. Built for Claude Code and Cowork.

## Plugins

### ir-teaching
Complete instructional design system for Florida BEST ELA 10th grade reading benchmarks. 62 skills covering all 10 ELA.10.R benchmarks, 6-day unit building, lesson planning, ESOL support, assessments, bellringers, test prep, and rubrics. 11 agents handle multi-step workflows like building student packets, answer keys, assessments, and full unit reviews.

### ir-data-pipeline
Student assessment data processing and analysis. 10 skills for ingesting FAST PM and NWEA data, validating quality, calculating growth, assigning intervention tiers, tracking benchmark mastery, generating reports, and building visualizations. 2 agents for full pipeline orchestration and parent-facing communications.

### ir-classroom-ops
Day-to-day classroom logistics. 6 skills for behavior tracking, parent contact logging, observation prep, PD tracking, substitute folder building, and unit distribution workflows.

### mr-burger-workflow
Personal productivity and second brain system. 5 skills for task capture, Notion sync, work logging, area context, and plugin coordination. 11 slash commands for daily briefings, weekly planning, reviews, status checks, capture, brain dumps, reflection, and cross-plugin sync.

## Architecture

```
mr-burger-plugins/              <- Single source of truth
  ir-teaching/
    skills/                     <- Skill folders, each with skill.md
    agents/                     <- Agent .md files
  ir-data-pipeline/
    skills/
    agents/
  ir-classroom-ops/
    skills/
  mr-burger-workflow/
    skills/
    commands/
    hooks/
  packages/                     <- Built .plugin + .zip files for Cowork
  scripts/
    setup.sh                    <- Symlinks everything into Claude Code
```

### How it connects

**Claude Code** reads skills and agents via symlinks from `~/.claude/skills/` and `~/.claude/agents/` pointing back to this repo. Edits here are picked up immediately.

**Cowork** reads from installed `.plugin` packages (zip archives). After editing source files, run `scripts/package.sh` to rebuild and `packages/install-plugins.sh` to install.

**Obsidian** can optionally symlink `ir-teaching/skills/` into a vault for browsing skill content alongside teaching notes.

## Installation

### Claude Code (from GitHub — for anyone)

Add the marketplace and install plugins:

```
/plugin marketplace add Burger4991/mr-burger-plugins
/plugin install ir-teaching@mr-burger-plugins
/plugin install ir-data-pipeline@mr-burger-plugins
/plugin install ir-classroom-ops@mr-burger-plugins
/plugin install mr-burger-workflow@mr-burger-plugins
```

You only need to add the marketplace once. After that, install whichever plugins you need.

### Cowork

Download `.plugin` files from [`packages/`](https://github.com/Burger4991/mr-burger-plugins/tree/main/packages), then:

1. Open Cowork settings → Plugins
2. Click "Install from file"
3. Select each `.plugin` file

Available packages: `ir-teaching.plugin`, `ir-data-pipeline.plugin`, `ir-classroom-ops.plugin`, `mr-burger-workflow.plugin`

### Development (local symlinks — for contributors)

If you've cloned the repo and want live-editing:

```bash
cd mr-burger-plugins
./scripts/setup.sh
```

This symlinks all skills into `~/.claude/skills/` and agents into `~/.claude/agents/`. Edits are picked up immediately — no rebuild needed for Claude Code. For Cowork, run `./scripts/package.sh` to rebuild packages after changes.

## Development workflow

1. Edit skill/agent files in this repo (the source of truth)
2. Claude Code picks up changes immediately via symlinks
3. When ready to update Cowork, run `./scripts/package.sh` to rebuild packages
4. Test in Cowork, iterate

### Cleanup

To remove orphan `.md` stub files from `~/.claude/skills/` (old flat-file skills that now have folder equivalents):

```bash
./scripts/cleanup.sh
```

## Deliverable format

All teaching deliverables (lesson plans, student packets, answer keys, feedback forms, exit tickets, cover pages) are generated as Markdown (`.md`). Slide decks remain as PowerPoint (`.pptx`).

## Design principles

This system follows a UNIX-inspired philosophy for LLM skill design:

- **Each skill does one thing well.** STOP handles STOP. RACE handles RACE. Bellringers build bellringers.
- **Text is the universal interface.** Skills communicate through markdown files and structured config, not conversational memory.
- **Composability over monoliths.** Small focused skills chain together through orchestrators (`unit-builder-protocol`, `menu-mode-planner`) rather than one giant skill trying to do everything.
- **Skills describe themselves.** Clear trigger descriptions enable accurate routing without keyword collisions.
