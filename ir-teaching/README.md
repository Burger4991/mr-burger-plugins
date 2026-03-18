# ir-teaching

Complete 10th grade Intensive Reading teaching system for Florida BEST ELA benchmarks.

62 skills covering all 10 ELA.10.R benchmarks, 6-day unit building, lesson planning, ESOL support, assessments, bellringers, test prep, and rubrics. 11 agents for multi-step workflows.

## Install

### Claude Code

Add the marketplace, then install:

```
/plugin marketplace add Burger4991/mr-burger-plugins
/plugin install ir-teaching@mr-burger-plugins
```

### Cowork

Install the `.plugin` file through the Cowork plugin manager:

1. Download `ir-teaching.plugin` from [Releases](https://github.com/Burger4991/mr-burger-plugins/tree/main/packages)
2. Open Cowork settings → Plugins
3. Click "Install from file"
4. Select `ir-teaching.plugin`

### Development (local symlinks)

If you've cloned the repo locally and want live-editing:

```bash
cd mr-burger-plugins
./scripts/setup.sh
```

This symlinks all skills into `~/.claude/skills/` and agents into `~/.claude/agents/`. Edits to source files are picked up immediately.

## What's included

### Key skills
- **menu-mode-planner** — Entry point for unit planning (collects all preferences upfront)
- **unit-builder-protocol** — Orchestrates full 6-day unit builds with context management
- **attack-the-passage** — Master test-taking protocol (4 phases + year-long progression)
- **10 benchmark skills** — One per ELA.10.R standard with achievement levels and question stems
- **bellringer-builder** — 3 modes (context clue, word parts, benchmark vocab)
- **stop-strategy / race-strategy / cer-writing-guide** — Core instructional strategies
- **esol-core** — ESOL scaffolding with daily minimums

### Key agents
- **student-packet-builder** — Generates day-by-day student materials
- **assessment-builder** — Creates MC + CR assessments with answer keys
- **quality-reviewer** — Two-stage review (spec compliance + quality)
- **unit-reviser** — Handles text swaps, benchmark changes, mid-cycle adjustments

## Version

3.0.0
