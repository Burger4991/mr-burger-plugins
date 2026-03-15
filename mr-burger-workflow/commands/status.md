---
description: Unified view across all areas — teaching, data, tasks, goals
allowed-tools: Read, Bash, Grep, Glob
---

# /status

Generate a unified status dashboard by executing the following steps exactly.

## Procedural Instructions

### Step 1: Read Tasks
1. Read `~/Desktop/SecondBrain/TASKS.md`
2. Count items under each section:
   - Count lines under `## Active` (items without [x])
   - Count lines under `## Waiting On` (items without [x])
   - Count lines under `## Someday` (items without [x])
   - Count lines under `## Done` (items with [x])
3. Extract the first 3 active items (copy exact text)

### Step 2: Read Goals
1. Read `~/Desktop/SecondBrain/GOALS.md`
2. Find and copy the line that says "Current Focus:" or the content under "## Current Focus"
3. Note any area-specific goals that have content (Teaching, Career, Music, Dog Training)

### Step 3: Find Recent Teaching Files
1. Run: `ls -lt ~/Documents/Teaching/*.md 2>/dev/null | head -5`
2. Extract the 3 most recent files with their modification dates (format: "filename (date)")

### Step 4: Check Classroom Logs
1. Check if `~/Documents/Teaching/logs/` exists
2. If yes:
   - Read `~/Documents/Teaching/logs/parent-contacts.md` (if exists) and find the most recent date entry
   - Read `~/Documents/Teaching/logs/behavior-notes.md` (if exists) and find the most recent date entry
   - Run: `grep -c "Y\|Yes" ~/Documents/Teaching/logs/parent-contacts.md 2>/dev/null` to count pending follow-ups
3. If no: note "Classroom logs not set up yet"

### Step 5: Check Data Pipeline
1. Run: `find ~/Documents/Teaching/data/ -name "*.md" -o -name "*.csv" 2>/dev/null | sort -r | head -3`
2. Extract the most recent file with its path
3. If no files found, note "No recent analyses"

### Step 6: Present as Dashboard
Format output exactly as follows:

```
## Status Dashboard — [TODAY'S DATE]

### Tasks
Active: [count] | Waiting: [count] | Someday: [count] | Done: [count]

**Active Items:**
- [item 1]
- [item 2]
- [item 3]

### Current Focus
[from GOALS.md Current Focus line, or "Not set up yet"]

### Teaching
Last 3 recent files:
- [filename] ([date])
- [filename] ([date])
- [filename] ([date])

### Classroom Operations
Parent contacts — Last entry: [date] | Follow-ups pending: [count]
Behavior notes — Last entry: [date]

### Data Pipeline
Last analysis: [filename] or "No recent analyses"
```

### Step 7: Error Handling
- If a file doesn't exist, show "[section name] — Not set up yet" instead of erroring
- If a directory doesn't exist, show "Not set up yet"
- If a grep/find command returns nothing, show "None" or "0"

---

## Notes

- This is a pulse check for quick clarity — do not add interpretation or commentary
- If GOALS.md doesn't exist, write "Goals not yet set up"
- Keep the dashboard scannable (use exact formatting above)
