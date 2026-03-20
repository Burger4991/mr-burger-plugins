---
description: Save session state to HANDOFF.md before clearing context
allowed-tools: Read, Write, Edit, Glob
---

# /wrap Command

End a session cleanly. Writes `HANDOFF.md` in the current working directory so you can `/clear` and resume later without losing where you were.

## What to do

1. **Review the conversation** — scan what was worked on, what decisions were made, what's unfinished

2. **Write `./HANDOFF.md`** in the current working directory using this format:

```markdown
# Handoff — [date]

## What we were doing
[1-3 sentences: the task, the goal, the context]

## Where we left off
[Specific stopping point — what's done, what's half-done]

## Decisions made
- [Decision + why, only if not obvious from the code/files]

## What's next
1. [First thing to do when resuming]
2. [Then this]
3. [Then this]

## Watch out for
[Any gotchas, constraints, or things that tripped us up — only if non-obvious]
```

3. **Check memory** — ask: did anything happen this session that future-me should know across all conversations? If yes, write it to the appropriate memory file at `~/.claude/projects/-Users-alexanderburger/memory/`. Use judgment — only save what's non-obvious and durable. Skip ephemeral task state.

4. **Confirm** — tell the user: HANDOFF.md is written, memory is updated (or nothing worth saving), safe to `/clear`.

## Notes

- Overwrite any existing HANDOFF.md — it's always the current state, never a log
- Keep it short — the goal is a 30-second read to get back up to speed
- Don't document what's already obvious from the code or files
- If nothing meaningful happened (quick question, no changes), say so and skip the write
