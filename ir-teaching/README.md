# ir-teaching

Complete 10th grade Intensive Reading teaching system for Florida BEST ELA benchmarks.

62 skills covering all 10 ELA.10.R benchmarks, 6-day unit building, lesson planning, ESOL support, assessments, bellringers, test prep, and rubrics. 11 agents for multi-step workflows.

## Install

### Claude Code (via marketplace)

```bash
claude plugin install ir-teaching --marketplace mr-burger-plugins
```

Or if using the local directory marketplace, add to `~/.claude/plugins/known_marketplaces.json`:

```json
{
  "mr-burger-plugins": {
    "source": { "source": "directory", "path": "/path/to/mr-burger-plugins" },
    "autoUpdate": true
  }
}
```

Then: `claude plugin install ir-teaching`

### Claude Code (via symlinks — for development)

```bash
cd /path/to/mr-burger-plugins
./scripts/setup.sh
```

This symlinks all skills into `~/.claude/skills/` and agents into `~/.claude/agents/`. Edits to source files are picked up immediately.

### Cowork

Install the `.plugin` file through the Cowork plugin manager:

1. Open Cowork settings
2. Go to Plugins
3. Click "Install from file"
4. Select `packages/ir-teaching.plugin`

Or rebuild from source: `./scripts/package.sh ir-teaching`

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
3.0.0 — UNIX philosophy overhaul: .md deliverables, `_unit-spec.md` handoff pattern, context refresh protocol, trigger keyword deduplication.
