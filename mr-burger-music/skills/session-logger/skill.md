---
name: session-logger
description: >
  Captures a practice session brain dump and appends a formatted entry to the Practice Log.
  Use when the user has finished practicing and wants to log what they did, what worked,
  what was hard, or what to focus on next.
version: 1.0.0
---

# Session Logger

Format a practice session entry and append it to the Practice Log.

## When to Use This vs music-coach

| Use this skill | Use music-coach agent |
|----------------|----------------------|
| Already practiced, just logging | Want planning + logging in one session |
| Quick brain dump only | Want history-informed next-session advice |
| Mid-conversation log request | Starting a full coaching session |

## Log File

`~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md`

**If the file does not exist:** Create it using the full journal template (header section with instructions + weekly structure template), then append the entry.

## Process

1. Accept the user's brain dump (freeform — blocks practiced, how it went, struggles, wins)
2. Extract or infer:
   - Date (use today's date if not stated)
   - Time practiced (duration, if mentioned; otherwise "not recorded")
   - Blocks used (list them by name if mentioned)
   - What worked
   - What's still hard
   - Tomorrow's focus
3. Format using the entry template below
4. Append to the log file — do not overwrite or modify existing entries
5. Confirm: "Logged to Practice-Log.md ✓"

## Entry Template

```
### Day __
**Date:** [date]  **Time Practiced:** [duration or "not recorded"]

**Blocks Used:** [comma-separated list]

**What Worked:** [1-2 sentences]

**What's Still Hard:** [1-2 sentences]

**Tomorrow's Focus:** [1 sentence]

---
```

## Notes

- Keep entries brief — 1-2 sentences per field max
- If the user didn't mention a field, mark it as "—" rather than leaving blank
- If this appears to start a new week in the log, add a week header above the entry
