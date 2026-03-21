---
description: Update knowledge base with evolving patterns, approaches, and understanding
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /reflect

Update the knowledge base at `~/Documents/Knowledge/` based on shifts in how you work, think, or approach things. Less frequent than `/capture` (ideas) or `/wrap` (session state) — use this when something about your *approach* has changed, not just what you did.

## When to use

- After a significant project reveals something about how you work
- When you notice a pattern across multiple sessions
- When your approach to something has evolved ("I used to do X, now I do Y because Z")
- Weekly or after major milestones — not every session

**Not for:** task notes, specific facts, or project status — those belong in TASKS.md, memory, or HANDOFF.md.

## What to do

### Step 0: Call session-state-reader

Get current project state. Use the result in Step 4 — if a project is active, the PROJECT.md directory gives you the path to the project's CLAUDE.md without re-searching.

### Step 1: Identify what changed

Ask: what do I understand differently now about how I work or think in one of these areas?
- Workflows & systems (`workflows.md`)
- Teaching practice (`teaching.md`)
- Tech & Claude Code systems (`tech-systems.md`)
- Career & edtech transition (`career.md`)
- Music (`music.md`)
- Dog training (`dog-training.md`)

If the user passed an argument (e.g. `/reflect teaching`), focus there. Otherwise scan the conversation or ask.

### Step 2: Read the current file

```bash
cat ~/Documents/Knowledge/[area].md
```

Understand what's already there before proposing anything.

### Step 3: Propose updates

Show exactly what you'd add or change:

```
### Proposed update to teaching.md

**What shifted:** [1 sentence — what understanding changed and why]

> [The addition or edit — written as "how I approach X" not "today I did X"]
```

Write in first person from Mr. Burger's perspective — these are his notes about himself, not observations about him.

**Add** new understanding. **Edit** sections that are now outdated. **Delete** approaches that no longer apply.

If nothing meaningfully changed: "Nothing in this session warrants a knowledge update."

### Step 4: Check project CLAUDE.md

If a project is active (PROJECT.md found), ask: does anything from this session belong in the **project's** CLAUDE.md rather than a general Knowledge file?

- Knowledge files (`~/Documents/Knowledge/`) → patterns that apply across all projects (how you think, general workflows)
- Project CLAUDE.md (e.g. `~/Desktop/gaby-portfolio/CLAUDE.md`) → conventions specific to that project (design rules, tech constraints, naming decisions)

If yes: read the project CLAUDE.md, propose the addition, apply with approval. Keep it terse — CLAUDE.md is scanned at session start, not read deeply.

### Step 5: Apply with approval

List proposed changes numbered, grouped by file. Apply only approved ones.

## Notes

- Knowledge files are living documents — they should get better over time, not just longer
- Prefer updating existing sections over always appending — outdated approaches should be replaced
- These files are read by Claude at session start via `~/CLAUDE.md` — keep them scannable
- If an area doesn't have a file yet, propose creating one
