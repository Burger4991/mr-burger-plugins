---
description: Resume a previous session — reads full context hierarchy (PROJECT.md → HANDOFF.md → plan file) and delivers a synthesized orientation
allowed-tools: Read, Glob, Bash
---

# /resume

Pick up where you left off. Reads the full context hierarchy and orients you for the session ahead.

## What to do

1. **Call session-state-reader** — get structured project state before reading anything else

2. **Read HANDOFF.md** (if it exists in current dir):
```bash
cat ./HANDOFF.md 2>/dev/null
```

3. **Read plan file** (if session state has a plan_file path):
   - Read it
   - Find the first unchecked `- [ ]` line — that is the exact next action
   - If all steps are checked: note "plan complete" and surface the next project from PROJECT.md instead

4. **Check active tasks**:
```bash
awk '/^## Active/{found=1; next} /^## /{found=0} found && /^\- \[ \]/{print}' ~/Documents/TASKS.md 2>/dev/null | head -5
```

5. **Synthesize orientation** — combine all sources into a brief summary:
   - Current phase + where in it (from PROJECT.md — authoritative)
   - What happened last session (from HANDOFF.md)
   - Exact next action (from plan file current step, or PROJECT.md resume_at)
   - Relevant active tasks only (filtered to current project)
   - Open questions or watch-outs

   **Conflict rule:** PROJECT.md beats HANDOFF.md when they conflict.

   Keep it short. End with: "Ready to continue. What would you like to start with?"

6. **If no PROJECT.md and no HANDOFF.md** — say so and show active tasks.

## Notes
- Don't recite files verbatim — synthesize and orient
- If files are stale (old date), flag it
- If a brainstorm doc exists for the active topic, mention it
