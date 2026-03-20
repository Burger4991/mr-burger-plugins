---
description: Resume a previous session by reading HANDOFF.md in the current directory
allowed-tools: Read, Glob
---

# /resume

Pick up where you left off. Reads `HANDOFF.md` in the current working directory and orients you for the session ahead.

## What to do

1. **Check for HANDOFF.md**

```bash
cat ./HANDOFF.md 2>/dev/null
```

2. **Check active tasks**

```bash
grep -A 50 "## Active" ~/Documents/TASKS.md 2>/dev/null | grep -B 0 "## Waiting" | grep "^\- \[ \]" | head -5
```

3. **If HANDOFF.md found** — read it and deliver a brief orientation:
   - What we were working on
   - Where we left off
   - What's next (in order)
   - Any watch-outs to keep in mind

   Then surface active tasks relevant to the current project context (skip unrelated ones).

   Keep it short — one paragraph max. End with: "Ready to continue. What would you like to start with?"

4. **If no HANDOFF.md** — say so: "No HANDOFF.md found in [current directory]. Starting fresh."
   Still show active tasks if any exist.

5. **If no HANDOFF.md and no tasks** — just ask what they'd like to work on.

## Notes

- Don't recite the HANDOFF.md verbatim — summarize and orient
- If the handoff mentions memory updates were saved, no need to re-read them; they're already in context
- If the handoff is stale (date is old), flag it: "This handoff is from [date] — things may have changed."
