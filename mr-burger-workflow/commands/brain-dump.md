---
description: Universal brain dump — accepts anything, decides what to do with it. Routes to /capture, /brainstorm-capture, a skill, or multiple at once.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /brain-dump

The smart brain dump. Throw anything at it — tasks, ideas, brainstorms, skill friction, half-formed thoughts. It reads the context, classifies everything, and routes to the right place or skill.

## What to do

1. **Call session-state-reader** — know what project/phase we're in

2. **Classify every item** in the dump:

| Classification | Triggers | Routes to |
|---------------|----------|-----------|
| Task/reminder | Action verb, deadline, "I need to" | TASKS.md via /capture |
| Teaching idea | Unit, lesson, student, benchmark | Teaching/ideas.md via /capture |
| Career note | Job, edtech, application, networking | Career/notes.md via /capture |
| Brainstorm | Options being weighed, "should we", exploratory | /brainstorm-capture |
| Skill friction | "The skill didn't", "that didn't work" | /skill-update flag |
| Memory-worthy | Durable preference or lesson | Memory (ask first) |
| Needs a skill | Benchmark code, data keyword, unit topic | Route to relevant skill |
| Mixed | Multiple types | Split and route each part |

3. **For items that need a skill** — identify which skill applies, then actually invoke it using the Skill tool:
   - Benchmark codes → appropriate benchmark skill (e.g. `ir-teaching:benchmark-central-idea`)
   - Data keywords (PM, FAST, NWEA) → `ir-data-pipeline:student-data-processor`
   - Unit topics → `ir-teaching:menu-mode-planner` or relevant skill
   - Plugin friction → `skill-update`

   **Invocation pattern — do not just describe, actually run it:**
   1. Say: "Routing [item] to [skill-name] — it will [1-sentence preview of what it does]"
   2. Get confirmation
   3. Use the Skill tool: `skill: "[skill-name]"`

4. **Present routing for all items in one message** — same confirm pattern as /capture:

```
I'll route these:
→ TASKS.md: [item]
→ /brainstorm-capture: [item]
→ benchmark skill: [item]
→ Career/notes.md: [item]
Anything to change?
```

5. **Execute on approval**

## Examples

```
/dump LAFS.8.RI.1.2 — students are struggling with central idea. Also I need
to grade PM data this week. Been thinking about whether to add a new skill
for vocabulary — not sure if esol-core covers it or we need something new.
```

Routes:
→ benchmark skill: LAFS.8.RI.1.2 (central idea instruction)
→ TASKS.md: grade PM data this week
→ /brainstorm-capture: vocabulary skill gap question

## Notes
- /brain-dump is the entry point; /capture and /brainstorm-capture are its execution layer
- If everything in the dump is clearly one type, just do it — don't over-route
- For skill invocations: always use the Skill tool — never just describe what the skill would do
