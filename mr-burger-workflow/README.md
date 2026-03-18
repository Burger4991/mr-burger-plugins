# mr-burger-workflow

Personal productivity and second brain system with Notion integration.

5 skills for task capture, Notion sync, work logging, area context, and plugin coordination. 6 slash commands for daily briefings, weekly planning, reviews, status checks, capture, and cross-plugin sync. 1 hook for automatic capture detection.

## Install

### Claude Code (via marketplace)

```bash
claude plugin install mr-burger-workflow --marketplace mr-burger-plugins
```

### Claude Code (via symlinks)

```bash
cd /path/to/mr-burger-plugins
./scripts/setup.sh
```

### Cowork

Install `packages/mr-burger-workflow.plugin` through the Cowork plugin manager.

## What's included

### Skills
- **second-brain-ops** — Capture tasks, organize notes, route content to correct locations
- **notion-sync** — Bidirectional sync between file-based system and Notion
- **work-logger** — Convert session outputs into task updates and journal entries
- **area-context** — Maps life areas (teaching, personal, tech) to project file locations
- **plugin-registry** — Documents plugin ownership, data routing, inter-plugin coordination

### Commands
- `/briefing` — Daily what's-on-deck priorities and reminders
- `/capture` — Brain dump anything, Claude routes it to the right place
- `/plan` — Weekly planning session
- `/review` — End-of-week review
- `/status` — Unified view across all areas
- `/sync` — Push recent work into the right places across all plugins

### Hooks
- **UserPromptSubmit** — Auto-detects capture-worthy content in user messages

## Version
1.2.0 — Sync command updated for .md deliverables.
