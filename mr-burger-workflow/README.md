# mr-burger-workflow

Personal productivity and second brain system with Notion integration.

5 skills for task capture, Notion sync, work logging, area context, and plugin coordination. 6 slash commands for daily briefings, weekly planning, reviews, status checks, capture, and cross-plugin sync. 1 hook for automatic capture detection.

## Install

### Claude Code

```
/plugin marketplace add Burger4991/mr-burger-plugins
/plugin install mr-burger-workflow@mr-burger-plugins
```

### Cowork

1. Download `mr-burger-workflow.plugin` from [Releases](https://github.com/Burger4991/mr-burger-plugins/tree/main/packages)
2. Open Cowork settings → Plugins → Install from file

### Development (local symlinks)

```bash
cd mr-burger-plugins && ./scripts/setup.sh
```

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

1.2.0
