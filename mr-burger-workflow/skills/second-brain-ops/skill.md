---
name: second-brain-ops
description: >
  Use when routing content to the correct file location, capturing tasks,
  or organizing notes. Covers TASKS.md, area notes.md files, Knowledge/, and
  memory. Reference for all personal knowledge management operations.
version: 2.0.0
---

# Personal Knowledge System

## Overview

Mr. Burger's knowledge system is file-based, organized across three layers:

| Layer | What | Where |
|-------|------|-------|
| **Tasks** | Action items across all areas | `~/Documents/TASKS.md` |
| **Notes** | Area-specific captures and working notes | `~/Documents/[area]/notes.md` |
| **Knowledge** | Long-term patterns and evolving understanding | `~/Documents/Knowledge/[area].md` |
| **Memory** | Durable facts for Claude across sessions | `~/.claude/projects/.../memory/` |

No INBOX.md, no GOALS.md, no journal folder, no SecondBrain directory.

---

## File Structure

```
~/Documents/
├── TASKS.md                    # Master task list (all areas)
├── Teaching/
│   ├── notes.md                # Teaching captures, running notes
│   └── Resources/
│       └── data-analysis-log.md  # Structured PM/FAST data log
├── Career/
│   └── notes.md
├── Music/
│   └── notes.md
├── Dog-Training/
│   └── notes.md
├── Personal/
│   └── notes.md
└── Knowledge/
    ├── workflows.md
    ├── teaching.md
    ├── tech-systems.md
    ├── career.md
    ├── music.md
    └── dog-training.md
```

---

## TASKS.md — Master Task List

**Location**: `~/Documents/TASKS.md`

**Structure**:

```markdown
# TASKS

## Active
- [ ] [Teaching] Grade PM2 data for Week 4
- [ ] [Career] Finalize portfolio updates

## Waiting
- [ ] [Dog Training] Awaiting feedback on Recallers course submission

## Someday
- [ ] [Tech] Learn new keyboard layout system

## Done
- [x] [Teaching] Unit outline for short stories (completed 2026-02-14)
```

**Format Rules**:
- Checkbox item: `- [ ] [Area] Task description`
- Area tags required — valid areas: `Teaching`, `Career`, `Music`, `Dog Training`, `Personal`, `Tech`
- Completion: mark `[x]` and append `(completed YYYY-MM-DD)`, move to Done
- Optional: urgency marker `★` prefix, due dates `(due YYYY-MM-DD)` inline
- No nesting — break complex tasks into separate lines

---

## Area Notes (`notes.md`)

**Location**: `~/Documents/[area]/notes.md`

**Purpose**: Running captures for each life area. Created and updated by `/capture`.

**Format** (each entry):

```markdown
## [Date] — [Topic or brief label]

[Content — free-form. Observations, brain dumps, reference material, dated reflections.]
```

**Rules**:
- Append new entries at the top (most recent first) or bottom — pick one and stay consistent
- For significant work completions (major unit, analysis session), add a dated summary entry
- Keep raw — this is capture territory, not polished documentation
- Use `/reflect` to promote durable patterns to `~/Documents/Knowledge/`

---

## Knowledge Base (`Knowledge/[area].md`)

**Location**: `~/Documents/Knowledge/`

**Purpose**: Long-term, evolving understanding of how Mr. Burger works and thinks. Updated via `/reflect` — not every session.

**Files**:
- `workflows.md` — session patterns, system design philosophy
- `teaching.md` — IR approach, unit design, skill-building
- `tech-systems.md` — Claude Code systems, plugin architecture
- `career.md` — edtech transition strategy
- `music.md` — practice philosophy
- `dog-training.md` — Olive, Susan Garrett methods

**Rules**:
- Update when an *approach* has changed, not just what happened
- Edit outdated sections — don't just append
- Prefer updating over adding

---

## Routing Rules

When capturing new content, use the `area-context` skill to determine the right area, then apply:

| Input Type | Destination | Format |
|------------|-------------|--------|
| Task (action item, deadline) | TASKS.md "Active" or "Someday" | `- [ ] [Area] Task` |
| Waiting item | TASKS.md "Waiting" | `- [ ] [Area] Task` |
| Completed task | TASKS.md "Done" | `- [x] [Area] Task (completed YYYY-MM-DD)` |
| Area-specific note, observation, brain dump | `~/Documents/[area]/notes.md` | Dated entry |
| Long-term pattern or approach shift | `~/Documents/Knowledge/[area].md` | Via `/reflect` |
| Durable fact for Claude | `~/.claude/projects/.../memory/` | Via `/wrap` or `/checkpoint` |
| Teaching data analysis | `~/Documents/Teaching/Resources/data-analysis-log.md` | Structured entry |

---

## Routing Decision Tree

```
INPUT → Is it an action item?
  YES → Urgent or time-sensitive?
    YES → TASKS.md "Active"
    NO → Someday or clear intention?
      SOMEDAY → TASKS.md "Someday"
      ACTIVE → TASKS.md "Active"
  NO → Is it a pattern or approach shift?
    YES → Knowledge/[area].md via /reflect
    NO → Is it a durable fact for Claude?
      YES → memory/ via /wrap or /checkpoint
      NO → ~/Documents/[area]/notes.md
```

---

## Common Operations

### Adding a Task
1. Determine area using `area-context` skill
2. Choose Active, Waiting, or Someday
3. Append to TASKS.md: `- [ ] [Area] Task description`

### Completing a Task
1. Find in TASKS.md under Active or Waiting
2. Change to `[x]` and append `(completed YYYY-MM-DD)`
3. Move line to Done section

### Capturing a Note
Run `/capture` — it reads existing notes first, then appends new content to the right `notes.md`.

### Logging Completed Work
Use `work-logger` skill. Significant completions get a dated entry appended to the area's `notes.md`.

### Updating Knowledge
Run `/reflect` — reads the relevant `Knowledge/[area].md` and proposes updates based on what shifted.

---

## Preferences & Principles

- **One master task file**: All tasks in TASKS.md with area tags. No per-project to-do lists.
- **Notes are raw**: notes.md is for capture, not polished docs. Polish happens in Knowledge/.
- **Knowledge is selective**: Don't update Knowledge/ every session — only when an approach evolves.
- **Simple format**: Markdown, plain text. Easy to read, easy to maintain.
- **Commands do the routing**: /capture, /wrap, /checkpoint, /reflect handle where things go.

---

## Integration with Commands

- **`/capture`**: Routes brain dumps to TASKS.md and the right area notes.md
- **`/wrap`**: Writes HANDOFF.md, updates TASKS.md, checks memory
- **`/checkpoint`**: Full save — HANDOFF + tasks + CLAUDE.md + skills + knowledge + memory
- **`/resume`**: Reads HANDOFF.md and surfaces active tasks
- **`/reflect`**: Updates Knowledge/[area].md when understanding shifts
- **`/revise`**: Proposes CLAUDE.md updates from the session

This skill is the reference for all personal knowledge management operations across the plugin.
