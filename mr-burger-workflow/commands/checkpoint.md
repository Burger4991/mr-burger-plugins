---
description: Full save before clearing context — HANDOFF, tasks, CLAUDE.md, skills, knowledge, memory in one pass
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /checkpoint

Save everything worth keeping from this session before you lose context. Runs the full save sequence in one pass. Use when you've had a meaningful session and want to preserve it cleanly before `/clear`.

## Sequence

Work through each step in order. Be thorough but efficient — the goal is a complete save, not perfection.

---

### 1. HANDOFF.md

Write `./HANDOFF.md` in the current directory:

```markdown
# Handoff — [date]

## What we were doing
[1-3 sentences]

## Where we left off
[Specific stopping point]

## Decisions made
- [Decision + why — only if not obvious from files]

## What's next
1. [First step on resume]
2. ...

## Watch out for
[Gotchas — only if non-obvious]
```

---

### 2. TASKS.md

Scan the conversation for tasks and action items:
- New tasks → append to `~/Documents/TASKS.md` under `## Active` as `- [ ] [task]`
- Completed tasks → move to `## Done` with `(completed [date])`
- Skip if nothing changed

---

### 3. CLAUDE.md updates

Check: did anything change about this project that future sessions need to know?
- Read the current `./CLAUDE.md` (or nearest parent CLAUDE.md)
- Propose additions only if something genuinely new emerged — conventions, gotchas, structural changes
- Skip if nothing project-level changed

---

### 4. Skill/agent updates

Check: did any skill or agent have friction or gaps this session?
- If yes: read the relevant file in `~/Documents/Tech/mr-burger-plugins/`
- Propose targeted improvements
- Skip if skills performed as expected

---

### 5. Knowledge base

Check: did anything shift about *how you approach* something?
- Read relevant file in `~/Documents/Knowledge/`
- Propose updates if an approach evolved
- Skip if no pattern-level insights

---

### 6. Memory

Check: is there anything non-obvious and durable that future conversations should know?
- If yes: write to `~/.claude/projects/-Users-alexanderburger/memory/`
- Ask before saving — memory is for lasting lessons, not task notes
- Skip if nothing qualifies

---

### 7. Summary

Output:
```
## Checkpoint complete — [date]

✓ HANDOFF.md written
✓ TASKS.md — [N new tasks / no changes]
✓ CLAUDE.md — [proposed X additions / no changes]
✓ Skills — [flagged X for update / no changes]
✓ Knowledge — [updated X / no changes]
✓ Memory — [saved X / nothing to save]

Safe to /clear.
```

## Notes

- Skip any step where nothing changed — don't force updates
- The goal is signal, not completeness — a short checkpoint beats an exhaustive one
- If context is already degraded and you can't recall details, say so in the HANDOFF
