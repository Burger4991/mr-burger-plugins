---
description: Lightweight daily view — top tasks across all projects, urgent flags, suggested focus for today
allowed-tools: Read, Bash, Glob
---

# /daily

Quick daily orientation. Surfaces what matters today across all projects without the full session context of /resume.

## What to do

1. **Call session-state-reader** — get active project and phase

2. **Read active tasks from TASKS.md**
```bash
awk '/^## Active/{found=1; next} /^## /{found=0} found && /^\- \[ \]/{print}' ~/Documents/TASKS.md 2>/dev/null
```

3. **Scan for urgency signals** — flag any task that has:
   - A date or deadline in the text
   - Words like "today", "tomorrow", "this week", "before Friday", "urgent"
   - A `[!]` or similar marker

4. **Build the daily view** — output this structure:

```
## Daily — [date]

### Today's focus
[1 sentence: what the active project is and where it is in the cycle]

### Urgent / time-sensitive
- [task] — [why urgent]
(or: nothing flagged)

### Top tasks
[Project A]
- [ ] [task]
- [ ] [task]

[Project B]
- [ ] [task]

### Parked
[Any Waiting tasks worth surfacing]
```

**Filtering rules:**
- Show max 3 tasks per project — most important first, not just top of list
- Skip Done items entirely
- If a project has no active tasks, omit it
- Waiting/blocked items: only surface if they've been waiting more than a week (check date if tagged) or the blocker may have resolved

5. **Suggest a start** — end with one line:
   > "Suggested start: [specific task] — [one reason why now]"

   Base the suggestion on: urgency > active project momentum > quick wins.

## Notes

- This is a read-only command — no writes, no updates
- Keep the output short — this should take 20 seconds to read, not 2 minutes
- Don't recite every task — curate. The goal is clarity about today, not completeness
- If TASKS.md doesn't exist or is empty, say so and suggest running /capture
