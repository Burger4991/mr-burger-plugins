# mr-burger-plugins

Claude Code plugin marketplace for Mr. Burger's teaching system.

## Plugins

| Plugin | Purpose |
|--------|---------|
| `ir-teaching` | 10th grade IR instruction — benchmarks, lesson planning, ESOL, assessments, rubrics |
| `ir-data-pipeline` | Student data — FAST PM, NWEA, growth analysis, mastery tracking, reporting |
| `ir-classroom-ops` | Classroom ops — parent logs, behavior, observation prep, PD tracking, sub folders |
| `mr-burger-workflow` | Personal productivity — briefings, capture, planning, Notion sync |
| `ui-ux-pro-max` | UI/UX design system |

## Setup

```bash
bash scripts/setup.sh
```

Wires Claude Code marketplace path and Gemini CLI symlink. Run once after cloning.

## Targets

- **Claude Code:** marketplace reads this directory directly (via `settings.json`)
- **Gemini CLI:** `~/.gemini/extensions/` symlinked to `gemini/`
- **Obsidian:** symlink from vault pending vault migration

## Deferred

- GSD plugin (get-stuff-done) — to be wrapped in follow-up session
- GWS plugin (google workspace) — to be wrapped in follow-up session
