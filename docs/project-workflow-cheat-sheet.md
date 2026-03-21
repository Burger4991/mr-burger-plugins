# Project Workflow Cheat Sheet

## The Habit Loop

```
Start session → /resume
Work → update PROJECT.md live as things change
Capture ideas/tasks → /capture or /dump
End session → /wrap → /clear
```

---

## What Goes Where

| Info | File | When to update |
|------|------|---------------|
| Persistent project state | `PROJECT.md` (in project dir) | Live — as things happen |
| Session bridge | `HANDOFF.md` (in project dir) | At /wrap, every session |
| Tasks + action items | `~/Documents/TASKS.md` | At /capture or /wrap |
| Brainstorm thinking | `docs/brainstorm/YYYY-MM-DD-topic.md` | At /brainstorm-capture |
| Durable preferences/lessons | `~/.claude/projects/.../memory/` | At /wrap (ask first) |

---

## Git → Project State Mapping

| Git event | What to do |
|-----------|-----------|
| Start new feature | `git checkout -b feat/name` → update PROJECT.md phase |
| Finish a step | Commit → update PROJECT.md "Done" + "Current step" |
| Make a decision | Commit note → append to PROJECT.md Decisions Log |
| PR merged | Update PROJECT.md → note in HANDOFF.md if session ends |
| Release | Tag it → update PROJECT.md phase to "complete" or next phase |

---

## Branch → Commit → PR → Merge Sequence

```
1. git checkout -b feat/description
2. Do the work
3. git add [specific files]
4. git commit -m "feat(scope): description"
5. git push -u origin feat/description
6. gh pr create (or merge locally if token can't merge)
7. git checkout main && git merge --squash feat/description
8. git commit && git push
9. git branch -d feat/description
```

---

## When to Update Which File

**Update PROJECT.md immediately when:**
- Phase changes (planning → implementing → reviewing)
- A significant decision is made
- An implementation step completes
- A blocker is found or resolved

**Write HANDOFF.md at /wrap:**
- What happened this session (brief)
- Where we stopped
- What's next (first action)
- Watch-outs (only if non-obvious)

**Add to TASKS.md when:**
- A new action item surfaces (use /capture)
- A task is completed (move to Done with date)

---

## Commands

| Command | Use it when |
|---------|------------|
| `/resume` | Starting a session — get oriented |
| `/wrap` | Ending a session — save state |
| `/capture [text]` | You have tasks, ideas, or notes to file |
| `/dump [text]` | Mixed brain dump — Claude sorts it |
| `/brainstorm-capture` | After exploratory discussion, before /clear |

---

## Narration Rule

When doing git operations, say what you're doing and why — not just the command.
> "Committing the session-state-reader skill — this is Task 1 of the knowledge system plan. Pushing to main so it's live in the plugin repo."

Goal: build the mental model alongside the automation.
