---
description: Scaffold a new plan file for the active project — creates docs/plans/YYYY-MM-DD-[topic].md with standard structure, then updates PROJECT.md
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /plan

Create a new implementation plan for the current project. Call this before starting a new phase of work.

## What to do

1. **Call session-state-reader** — get project name, current phase, and project directory path

2. **Get the topic** — use the argument if provided (e.g. `/plan auth refactor`), otherwise ask: "What are we planning?"

3. **Check for existing plans**
```bash
ls [project-dir]/docs/plans/ 2>/dev/null | tail -5
```
If a recent plan exists for the same topic, ask: continuing the existing plan or starting a new one?

4. **Scaffold the plan file** at `[project-dir]/docs/plans/YYYY-MM-DD-[topic-slug].md`:

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

### Task 2: [Name]

...

---

## Execution Order

1. Task 1 — [reason first]
2. Task 2 — [depends on Task 1]
```

Fill in what's known from context. Leave File Map and Tasks skeletal if the scope isn't clear yet — the user will fill in details.

5. **Update PROJECT.md** — set:
   - `Plan.File` → absolute path to the new plan file
   - `Plan.Current step` → Task 1, Step 1
   - `Phase` → planning (if not already implementing)

6. **Confirm** — output:
```
Plan created: [project-dir]/docs/plans/YYYY-MM-DD-[topic].md
PROJECT.md updated — resume point set to Task 1.

Next: flesh out the tasks, then start executing. /resume will surface Task 1 automatically.
```

## Notes

- Plan files always go in `[project-dir]/docs/plans/` — create the directory if it doesn't exist
- Filename: `YYYY-MM-DD-[short-topic-slug].md` — lowercase, hyphens, no spaces
- If no project context (no PROJECT.md found): create plan at `~/Documents/Tech/mr-burger-plugins/docs/plans/` and warn that PROJECT.md wasn't found
- Steps inside tasks should be atomic and end with a Commit step where appropriate
- Execution Order section is required — even a single task benefits from stating why it comes first
