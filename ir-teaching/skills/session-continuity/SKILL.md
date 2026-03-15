---
name: session-continuity
description: >
  Resume an in-progress IR unit build after a context reset or new session. Reads _build-state.json
  from the active unit folder to determine which batches are complete and which are pending, then
  resumes from the next incomplete batch without re-asking menu-mode-planner questions. Use when
  starting a new session and a unit build was interrupted. Triggered by "resume build", "continue
  unit", "pick up where we left off", or when _build-state.json is detected in a unit folder.
---

# Session Continuity

## Purpose

Unit builds can take time. If a session ends mid-build, this skill picks up exactly where you left off.

## When to Use

- Opening a new session after a unit build was interrupted
- You say "resume", "continue", "pick up where we left off"
- A _build-state.json is found in a unit folder

## Step 1: Find Active Builds

Check common unit folder locations for `_build-state.json`:

```bash
find ~/Documents/Teaching/Units -name "_build-state.json" 2>/dev/null
```

## Step 2: Read State

For each found state file, read and display:

```json
{
  "status": "in_progress",
  "unit_name": "StoryOfAnHour-LitElements",
  "benchmark": "ELA.10.R.1.1",
  "text": "The Story of an Hour",
  "started": "2026-03-08T14:30:00",
  "batches_complete": ["batch_1"],
  "batches_pending": ["batch_2", "batch_3"],
  "last_updated": "2026-03-08T14:45:00",
  "unit_folder": "~/Documents/Teaching/Units/StoryOfAnHour-LitElements/"
}
```

Display to user:

```
Active build found:

Unit: The Story of an Hour (ELA.10.R.1.1)
Started: 2026-03-08 at 2:30 PM
Completed: Batch 1 (Bellringers + Vocabulary)
Pending: Batch 2 (Organizer + GR Scripts), Batch 3 (Assessment + Feedback Form)

Resume from Batch 2? (yes / start fresh)
```

## Step 3: Resume

If user says yes: invoke `unit-builder-protocol` skill, passing the state context.
Start from the first pending batch. Skip the menu-mode-planner questions — all preferences
are already encoded in the state file.

If user says start fresh: note that the current `_build-state.json` will be overwritten.
Invoke `menu-mode-planner` to start over.

## _build-state.json Schema

```json
{
  "status": "in_progress | complete | abandoned",
  "unit_name": "string",
  "benchmark": "string (e.g. ELA.10.R.1.1)",
  "text": "string (text title)",
  "cr_framework": "RACE | CER",
  "esol_levels": ["1", "2"],
  "started": "ISO timestamp",
  "batches_complete": ["batch_1"],
  "batches_pending": ["batch_2", "batch_3"],
  "last_updated": "ISO timestamp",
  "unit_folder": "absolute path to unit folder"
}
```
