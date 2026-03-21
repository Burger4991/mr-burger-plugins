---
description: Save session state to HANDOFF.md and PROJECT.md before clearing context
allowed-tools: Read, Write, Edit, Glob
---

# /wrap Command

End a session cleanly. Updates `PROJECT.md` with current workflow state and writes a lean `HANDOFF.md` session bridge so you can `/clear` and resume without losing context.

## What to do

1. **Review the conversation** — scan for:
   - What was worked on, what decisions were made, what's unfinished
   - Current workflow phase: planning | implementing | reviewing | debugging | eval
   - Any plan files referenced, created, or modified
   - Implementation steps completed or in progress
   - Review/eval findings or status changes
   - Debugging hypotheses formed, tried, or resolved
   - Decisions made (especially ones not obvious from files)
   - Open questions still unresolved

2. **Update `./PROJECT.md`** — create it if it doesn't exist, update it if it does. This is the persistent project record across all sessions:

```markdown
# [Project Name] — Project State
*Last updated: [date HH:MM]*

## Phase
[planning | implementing | reviewing | debugging | eval | complete]

## Plan
- **File:** `[path/to/PLAN.md]` — or "none, discussed in conversation"
- **Current step:** [step name or number]
- **Decided:** [locked decisions — don't re-litigate]
- **Open:** [still undecided or in progress]

## Implementation
- **Active:** [what's being built or executed right now]
- **Done:** [completed steps — keep brief]
- **Blocked:** [any blockers]

## Review / Eval
- **Status:** not started | in progress | complete
- **Findings:** [key findings]
- **Actions needed:** [what needs to change]

## Debugging
- **Issue:** [what's broken or unclear]
- **Hypotheses:** [current best thinking]
- **Tried:** [approaches already attempted]

## Decisions Log
- [date HH:MM]: [decision + rationale]

## Open Questions
- [question]
```

   Only include sections relevant to the current phase. Skip empty ones.
   Append new entries to Decisions Log — don't overwrite existing ones.

3. **Write `./HANDOFF.md`** — lean and session-focused. PROJECT.md carries the workflow detail; HANDOFF bridges the session gap:

```markdown
# Handoff — [date]

## What we were doing
[1-3 sentences: the task, the goal, the session context]

## Where we left off
[Specific stopping point — what's done, what's half-done]

## This session's decisions
- [Decision + why — things already logged to PROJECT.md]

## What's next
1. [First action when resuming]
2. [Then this]

## Watch out for
[Gotchas or constraints — only if non-obvious]

## Project state → see PROJECT.md
Phase: [current phase] | Resume at: [exact next step or decision]
```

4. **Update TASKS.md** — scan for tasks, action items, or follow-ups:
   - New → append to `~/Documents/TASKS.md` under `## Active` as `- [ ] [task]`
   - Completed → move to `## Done` with `(completed [date])`
   - No changes → skip

5. **Check memory** — did anything happen this session that future-me should know across all conversations? If yes, write to `~/.claude/projects/-Users-alexanderburger/memory/`. Only what's non-obvious and durable — skip ephemeral task state.

6. **Confirm** — tell the user: PROJECT.md updated, HANDOFF.md written, tasks updated (or no changes), memory updated (or nothing worth saving), safe to `/clear`.

## Live update behavior

Don't wait for `/wrap` to update PROJECT.md. During normal work, update it when:
- A phase changes (e.g. planning → implementing)
- A significant decision is made
- An implementation step completes
- A debug hypothesis forms or resolves
- A review finding emerges

PROJECT.md should reflect current state at all times, not just at session end.

## Notes

- PROJECT.md: append to Decisions Log, never overwrite. Update all other sections to current state.
- HANDOFF.md: overwrite every time — it's always the current session state, never a log
- Keep HANDOFF short — 30-second read to get oriented. PROJECT.md has the detail.
- Don't document what's already obvious from the code or files
- If nothing meaningful happened (quick question, no changes), say so and skip both writes
