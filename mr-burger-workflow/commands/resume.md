---
description: Resume a previous session by reading PROJECT.md and HANDOFF.md in the current directory
allowed-tools: Read, Glob
---

# /resume

Pick up where you left off. Reads `PROJECT.md` (persistent workflow state) and `HANDOFF.md` (session bridge) from the current working directory and orients you for the session ahead.

## What to do

1. **Check for PROJECT.md and HANDOFF.md**

```bash
cat ./PROJECT.md 2>/dev/null
cat ./HANDOFF.md 2>/dev/null
```

2. **Check active tasks**

```bash
awk '/^## Active/{found=1; next} /^## /{found=0} found && /^\- \[ \]/{print}' ~/Documents/TASKS.md 2>/dev/null | head -5
```

3. **Orient based on what's found:**

   **If PROJECT.md exists** — lead with this. It's the authoritative project state:
   - Surface current phase and what it means for today's work
   - Surface the resume point (current step, open decisions, active implementation, debug state — whatever the phase calls for)
   - Note any open questions that need resolution
   - If a plan file is referenced, read it and summarize where in it we are

   **If HANDOFF.md exists** — layer this on top of PROJECT.md:
   - What happened last session (the session summary)
   - Any session-specific watch-outs
   - Confirm the resume point matches PROJECT.md (flag if they conflict)

   **If only HANDOFF.md** (no PROJECT.md) — use it as before:
   - What we were working on, where we left off, what's next, any watch-outs

   **If neither** — "No HANDOFF.md or PROJECT.md found in [current directory]. Starting fresh."

4. **Surface relevant active tasks** from TASKS.md — only ones related to the current project context. Skip unrelated ones.

5. **Deliver the orientation** — combine everything into a brief summary:
   - Current phase and where we are in it
   - What happened last session (from HANDOFF)
   - Exact next action
   - Any open questions or watch-outs

   Keep it short. End with: "Ready to continue. What would you like to start with?"

## Notes

- Don't recite files verbatim — synthesize and orient
- PROJECT.md takes precedence over HANDOFF.md when they conflict — it's the persistent record
- If PROJECT.md or HANDOFF.md is stale (date is old), flag it: "This is from [date] — things may have changed."
- If the handoff mentions memory updates were saved, no need to re-read them; they're already in context
