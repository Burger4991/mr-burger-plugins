---
description: Start planning a new phase of work — invokes brainstorming to design first, then writing-plans to produce the implementation plan
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /plan

Start planning a new phase of work. Invokes the brainstorming skill to design the approach before writing a plan — design first, plan second.

## What to do

1. **Call session-state-reader** — get project name, current phase, and project directory path

2. **Check for existing plans**
```bash
ls [project-dir]/docs/plans/ 2>/dev/null | tail -5
```
Substitute `[project-dir]` with the PROJECT.md directory path from session state. If a recent plan exists for the same topic, ask: continuing the existing plan or starting fresh?

3. **Invoke brainstorming skill** — this is the primary path:
   - Use the Skill tool to invoke `superpowers:brainstorming`
   - Brainstorming handles: explore context → clarify → propose approaches → present design → write spec → invoke writing-plans
   - writing-plans produces the implementation plan file — no need to scaffold it manually

4. **After brainstorming + writing-plans complete** — update PROJECT.md:
   - `Plan.File` → absolute path to the new plan file
   - `Plan.Current step` → Task 1, Step 1
   - `Phase` → planning → implementing (update as appropriate)

## Fallback: design already clear

If the user is picking up mid-project (a plan file already exists and the next step is clear), or they explicitly say to skip brainstorming, skip brainstorming and scaffold the plan directly at `[project-dir]/docs/plans/YYYY-MM-DD-[topic-slug].md`:

```markdown
# [Topic] Implementation Plan
*Created: [date]*

**Goal:** [1-2 sentences — what this plan accomplishes and why]

---

## File Map

| Action | File |
|--------|------|
| Create | `[path]` |
| Modify | `[path]` |

---

## Tasks

### Task 1: [Name]

**Files:**
- [Create/Modify]: `[path]`

- [ ] **Step 1:** [action]
- [ ] **Step 2:** [action]
- [ ] **Step 3:** Commit

---

## Execution Order

1. Task 1 — [reason first]
2. Task 2 — [depends on Task 1]
```

Then update PROJECT.md as in step 4 above.

## Notes

- Plan files go in `[project-dir]/docs/plans/` — create the directory if it doesn't exist
- Filename: `YYYY-MM-DD-[short-topic-slug].md` — lowercase, hyphens, no spaces
- If no project context (no PROJECT.md found): use `~/Documents/Tech/mr-burger-plugins/docs/plans/` and warn
- Steps inside tasks should be atomic and end with a Commit step where appropriate
- Execution Order section is required — even a single task benefits from stating why it comes first
- `/resume` will surface Task 1 automatically once PROJECT.md is updated
