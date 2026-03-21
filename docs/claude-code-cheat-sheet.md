# Claude Code Cheat Sheet

## How Commands vs Skills Work

| Thing | How to invoke | Lives in |
|-------|--------------|----------|
| **Command** | `/command-name` — triggers like a slash command | `~/.claude/commands/` |
| **Skill** | Claude invokes it automatically, or say "use the X skill" | `~/.claude/skills/` |
| **Agent** | Say "use the X agent" or Claude auto-routes | `~/.claude/agents/` |

Commands are user-facing. Skills are called by Claude (or by other commands). Agents run autonomously for longer tasks.

---

## Your Custom Commands (mr-burger-workflow)

| Command | What it does |
|---------|-------------|
| `/resume` | Orient for a new session — reads PROJECT.md → HANDOFF.md → plan file |
| `/capture [text]` | Route a brain dump to TASKS.md, notes files, or brainstorm docs |
| `/brain-dump [text]` | Smart router — classifies anything and routes to /capture, /brainstorm-capture, or a skill |
| `/brainstorm-capture` | Lock in thinking from a brainstorm before /clear |
| `/wrap` | End session cleanly — updates PROJECT.md + HANDOFF.md |
| `/reflect` | Update knowledge files (workflows.md, teaching.md, etc.) |
| `/checkpoint` | Mid-session save to PROJECT.md |

**Shared skill all commands use:** `session-state-reader` (reads PROJECT.md → TASKS.md → HANDOFF.md, returns structured state)

---

## Your Plugins

### ir-teaching
**What:** All 10 FL BEST ELA standards, ESOL, assessment, vocab, rubrics, bellringers, unit building

Key skills: `menu-mode-planner` → `unit-builder-protocol` (full unit build)
Key agents: `unit-planner`, `lesson-plan-coordinator`, `student-packet-builder`, `assessment-builder`, `esol-adapter`, `interactive-lesson-builder`, `answer-key-builder`, `quality-reviewer`, `unit-reviewer`, `unit-reviser`, `sub-plan-generator`

**Auto-routes:** Benchmark codes (LAFS.X.X.X) trigger the right benchmark skill automatically.

### ir-data-pipeline
**What:** Student data processing, growth analysis, reports, visualizations

Key skills: `student-data-processor` → `data-quality-checker` → `growth-analyzer`
Key agents: `data-analyst`, `parent-reporter`

**Auto-routes:** Data keywords (PM, FAST, NWEA) trigger the pipeline automatically.

### ir-classroom-ops
**What:** Classroom logistics — behavior, parent contacts, sub folders, observation prep

Skills: `behavior-tracker`, `parent-contact-log`, `sub-folder-builder`, `observation-prep`, `pd-tracker`, `unit-distribution`

### mr-burger-music
**What:** Trumpet practice, jazz, beginning band materials, score transformers

Key skills: `band-materials`, `practice-planner`, `score-transformer`
Key agents: `music-coach`, `score-writer`

### mr-burger-workflow
**What:** Second brain, session management, capture, brainstorm, PROJECT.md/HANDOFF.md system

Key skills: `session-state-reader`, `area-context`, `plugin-registry`, `work-logger`, `second-brain-ops`, `notion-sync`

### ui-ux-pro-max (official plugin)
**What:** UI/UX design intelligence — invoke for design work, component design, visual polish

---

## Session Workflow

```
Open Claude Code (from project dir) → SessionStart hook shows context block
→ /resume (get oriented)
→ do work
→ /capture or /brain-dump (capture ideas/tasks as you go)
→ /checkpoint (optional mid-session save)
→ /wrap → /clear
```

---

## Tips

- **Start Claude from the project directory** — the SessionStart hook reads PROJECT.md from cwd and injects context automatically
- **Skills vs commands:** If something isn't working as a `/command`, try invoking it as a skill: "use the X skill"
- **Agent for long tasks:** "Use the unit-planner agent to..." — agents run autonomously and return a result
- **Benchmark auto-routing:** Just include the benchmark code (e.g. LAFS.8.RI.1.2) in your prompt — the hook routes it to the right skill
- **Data auto-routing:** Include PM, FAST, NWEA in your prompt — routes to data pipeline skills

---

## Key File Locations

| What | Where |
|------|-------|
| Plugin source | `~/Documents/Tech/mr-burger-plugins/` |
| Commands | `~/.claude/commands/` (symlinked) |
| Skills | `~/.claude/skills/` (symlinked) |
| Agents | `~/.claude/agents/` (symlinked) |
| Hooks | `~/.claude/hooks/` |
| Memory | `~/.claude/projects/-Users-alexanderburger/memory/` |
| After changes | Run `./scripts/setup.sh` to re-symlink |
