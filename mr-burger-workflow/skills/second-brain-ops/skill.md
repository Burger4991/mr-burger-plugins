---
name: second-brain-ops
description: >
  This skill should be used when "capturing tasks", "organizing notes",
  "updating the second brain", or routing content to the correct file location.
  Use when any command needs to read or write Second Brain files.
version: 1.0.0
---

# Second Brain Operations Skill

## Overview

The Second Brain is Mr. Burger's personal knowledge and task management system, centered at `~/Desktop/SecondBrain/`. This skill provides guidance on file layout, naming conventions, content structure, and routing rules for all Second Brain operations.

## Master Location

```
~/Desktop/SecondBrain/
├── TASKS.md              # Master task list (all areas, one file)
├── INBOX.md              # Unsorted capture inbox
├── GOALS.md              # Current focus and area-specific goals
├── journal/              # Date-stamped reflection and review entries
├── knowledge/            # Reference material, checklists, frameworks
├── memory/               # Context, preferences, glossary, project notes
├── notes/                # Organized by life area (6 subfolders)
│   ├── teaching/
│   ├── career/
│   ├── music/
│   ├── dog-training/
│   ├── personal/
│   └── tech/
└── plans/                # Project and initiative planning documents
```

## Key Files & Format Rules

### TASKS.md (Master Task List)

**Location**: `~/Desktop/SecondBrain/TASKS.md`

**Structure**: Four main sections, separated by headers:

```markdown
# TASKS

## Active
- [ ] [Teaching] Grade PM2 data for Week 4
- [ ] [Career] Finalize portfolio updates
- [ ] [Music] Practice Adam routine (30 min)
- [x] [Personal] Schedule doctor appointment (completed 2026-02-20)

## Waiting
- [ ] [Dog Training] Awaiting feedback on Recallers course submission
- [ ] [Career] Waiting to hear back from MDCPS on interview

## Someday
- [ ] [Tech] Learn new keyboard layout system
- [ ] [Music] Explore jazz guitar basics

## Done
- [x] [Teaching] Unit outline for short stories (completed 2026-02-14)
- [x] [Career] Submit 2 job applications (completed 2026-02-18)
```

**Format Rules**:
- Each task is a checkbox item: `- [ ] Task description` or `- [x] Task description`
- **Area tags required**: `[Area]` prefix in brackets. Valid areas: Teaching, Career, Music, Dog Training, Personal, Tech
- **Completion format**: When done, mark `[x]` and append `(completed YYYY-MM-DD)`
- **One master file**: Do NOT create separate task files per area. Use area tags for filtering.
- **Optional**: Add urgency markers: `★ Urgent task` or due dates `(due YYYY-MM-DD)` inline
- **No nesting**: Keep tasks at one level. If complex, break into subtasks on separate lines

### INBOX.md (Unsorted Capture)

**Location**: `~/Desktop/SecondBrain/INBOX.md`

**Purpose**: Quick capture without routing. Items here are processed later during `/plan` sessions.

**Structure**:

```markdown
# INBOX

## Unsorted
- Need to review ESOL adaptations for the new benchmark
- Olive's training is going well with Recallers
- Check that new trumpet article someone shared
- Follow up on salary negotiation email from last week
- Design idea for lesson plan gamification

## Questions
- How do I format CER responses for 9th graders?
- What's the best way to integrate AI tools in the IR classroom?
```

**Format Rules**:
- Items are bullet points, not tasks (no checkboxes in Unsorted)
- Keep items short and raw (this is brain dump territory)
- Optional subsection for questions or clarifications
- Process during `/plan`: route each item to correct location or delete

### GOALS.md (Focus & Area Goals)

**Location**: `~/Desktop/SecondBrain/GOALS.md`

**Purpose**: High-level focus for the current week and longer-term goals per area.

**Structure**:

```markdown
# GOALS

## Current Focus (This Week: Feb 24 - Mar 2)
- [Teaching] Complete PM data analysis and unit lesson planning
- [Career] Finalize 3 job applications and update portfolio
- [Music] Practice Adam routine 3x this week
- [Personal] Health checkup appointment

## Teaching
- Quarterly: Build complete short story unit with ESOL adaptations
- Current: PM2 data analysis, weekly lesson planning
- Projects: Unit-planner agent in Claude Code

## Career
- Job search: 2-3 applications per week, portfolio updates
- Goal: New teaching or tech-adjacent role by end of semester
- Current focus: K-12 tech integration or edtech companies

## Music
- Trumpet: Develop jazz vocabulary, play in beginning band
- Guitar: Basic exploration
- Current: Adam routine daily practice

## Dog Training
- Main goal: Continue Susan Garrett methods with Olive
- Courses: Complete Recallers, J Walking, HSTD
- Current: Recallers course in progress

## Personal
- Finance: Monthly budgeting, track expenses
- Health: Regular checkups, wellness routine
- Current: Schedule annual physical

## Tech
- Claude Code: Master teaching skills (30+), agents (19+)
- Cowork: Build personal productivity plugins
- Current: Finalizing mr-burger-workflow plugin
```

**Format Rules**:
- Start with "Current Focus" (weekly priorities, 3-5 items)
- One section per life area (Teaching, Career, Music, Dog Training, Personal, Tech)
- Use bullet points: quarterly/annual goals, then current focus
- Update "Current Focus" every `/plan` session
- Update area goals as needed; review during `/review` sessions

### journal/ (Reflection Entries)

**Location**: `~/Desktop/SecondBrain/journal/`

**Naming**: `YYYY-MM-DD-topic.md` (e.g., `2026-02-24-weekly-review.md`, `2026-02-20-teaching-reflection.md`)

**Purpose**: Dated reflection entries, reviews, and learnings.

**Structure** (example):

```markdown
# Weekly Review — Feb 24, 2026

## What Got Done ✓
- Completed PM2 data analysis and submitted
- Finished lesson outline for short story unit
- Applied to 2 teaching positions
- Practiced Adam routine 4 times this week

## What Didn't Move
- ESOL adaptations (need more time for detailed work)
- Portfolio update (deprioritized for exam week)

## Blockers & Learnings
- PM data tool was slower than expected → plan more time next cycle
- Noticed I'm more focused when I block music practice to specific days
- Interview feedback suggested emphasizing tech skills more in resume

## Next Week's Focus
- Start ESOL adaptations (Week 5)
- Polish portfolio before weekend
- 2 more job applications
- Dog training: submit Recallers project

## Energy & Mood
Productive week overall. Felt rushed on Friday but recovered Saturday morning.
```

**Format Rules**:
- Created during `/review` sessions (typically weekly, `YYYY-MM-DD-weekly-review.md`)
- Optional topics for specific reflections (teaching insights, career notes, etc.)
- Free-form content: celebrate wins, note blockers, capture learnings
- Link to related tasks or goals if helpful

### knowledge/ (Reference Material)

**Location**: `~/Desktop/SecondBrain/knowledge/`

**Purpose**: Checklists, frameworks, templates, and reference docs (e.g., RACE writing rubric, ESOL strategies, dog training principles).

**Naming**: Topic-based (e.g., `RACE-framework.md`, `esol-strategies.md`, `susan-garrett-principles.md`)

**Format**: Whatever makes sense for the content (lists, tables, detailed docs). Keep it findable.

### memory/ (Context & Preferences)

**Location**: `~/Desktop/SecondBrain/memory/`

**Purpose**: Mr. Burger's context, preferences, project info, glossary.

**Key Files**:
- `CLAUDE.md` — Full context document (synced from project root)
- `glossary.md` — Terms and acronyms (IR, PM, FAST, BEST, ESOL, etc.)
- `projects/` — Subdirectory with active project notes
- `preferences.md` — Tools, workflows, priorities, communication style

### notes/ (Area-Specific Notes)

**Location**: `~/Desktop/SecondBrain/notes/[area]/`

**Subfolders**:
- `notes/teaching/` — Lesson notes, unit planning, ESOL strategies, PM data
- `notes/career/` — Resume notes, job search tracking, interview insights
- `notes/music/` — Practice logs, song ideas, technique notes
- `notes/dog-training/` — Training logs, course notes, Olive's progress
- `notes/personal/` — Finance, health, wellness, life logistics
- `notes/tech/` — Claude Code notes, plugin ideas, GitHub projects, keyboard configs

**Naming**: Descriptive, date-based when relevant (e.g., `notes/teaching/week-5-short-story-unit.md`)

**Format**: Free-form per area. Teaching might be structured with headers. Career might be tables (jobs applied to). Dog training might be dated logs.

### plans/ (Project Planning)

**Location**: `~/Desktop/SecondBrain/plans/`

**Purpose**: Detailed planning documents for specific projects or initiatives.

**Examples**:
- `unit-short-story-planning.md` — Full unit outline, lessons, assessments
- `job-search-strategy.md` — Application timeline, target companies, interview prep
- `mr-burger-workflow-plugin.md` — Plugin development roadmap
- `recallers-course-plan.md` — Dog training project timeline

**Format**: Structured docs with goals, phases, deadlines, deliverables.

---

## Routing Rules

When capturing new content, use the `area-context` skill to determine the right area, then apply these routing rules:

| Input Type | Destination | Format |
|------------|------------|--------|
| Task (action item, deadline) | TASKS.md "Active" or "Someday" | `- [ ] [Area] Task description` |
| Waiting item (blocked, awaiting) | TASKS.md "Waiting" | `- [ ] [Area] Task description` |
| Completed task | TASKS.md "Done" | `- [x] [Area] Task description (completed YYYY-MM-DD)` |
| Unsorted/raw capture | INBOX.md "Unsorted" | Bullet point, no formatting |
| Question | INBOX.md "Questions" | Bullet point |
| Reference/framework | knowledge/ | Markdown doc, descriptive name |
| Area-specific note | notes/[area]/ | Markdown doc, descriptive name |
| Reflection/review | journal/ | `YYYY-MM-DD-topic.md` |
| Project plan | plans/ | Detailed markdown doc |
| Context/preference | memory/ | Appropriate subfile |

---

## Common Operations

### Adding a Task

1. Determine area using `area-context` skill
2. Decide if it's Active, Waiting, or Someday
3. Append to TASKS.md under the right section
4. Format: `- [ ] [Area] Task description` or `- [ ] [Area] Task description (due YYYY-MM-DD)`
5. If urgent or time-sensitive, add `★` prefix: `- [ ] ★ [Area] Urgent task`

### Completing a Task

1. Find the task in TASKS.md under "Active" or "Waiting"
2. Change from `- [ ]` to `- [x]` and append `(completed YYYY-MM-DD)`
3. Move the entire line to "Done" section
4. Sync to Notion if available

### Processing Inbox

1. Read all items in INBOX.md "Unsorted"
2. For each item:
   - If it's a task → move to TASKS.md with area tag
   - If it's a note → move to notes/[area]/
   - If it's a question → keep in "Questions" or answer + archive
   - If it's outdated → delete
3. Clear the Unsorted section

### Creating a Reflection Entry

1. After your week or a significant event, create `YYYY-MM-DD-topic.md` in journal/
2. Write freely: what happened, what you learned, how you feel
3. Optional: link to related tasks in TASKS.md or goals in GOALS.md
4. Keep it for later review and pattern recognition

---

## Preferences & Principles

- **One Master Task File**: All tasks live in TASKS.md with area tags. No separate to-do lists per project.
- **Brain Dump First**: INBOX.md is for raw capture without overthinking. Process during `/plan` sessions.
- **Area-Tagged Everything**: Every task, note, goal is clearly tagged by life area for filtering and context.
- **Dated Completions**: When tasks are done, mark the completion date for historical tracking.
- **Simple Format**: Markdown, plain text, no complex tools. Easy to read, easy to maintain.
- **Sync-Ready**: Structure supports bidirectional sync with Notion (when available) and other tools.
- **Review Rhythm**: Weekly review creates journal entries and updates GOALS.md. Monthly/quarterly review optional.

---

## Routing Decision Tree

Use this decision tree to route captured content correctly:

```
INPUT → Is it a task (has a clear action)?
  YES → Has a deadline or is time-sensitive?
    YES → TASKS.md under "## Active"
    NO → Is it something to do eventually?
      YES → TASKS.md under "## Someday"
      NO → TASKS.md under "## Active" (default to action)
  NO → Is it a thought/note/reference?
    YES → Which area does it belong to?
      Teaching → notes/teaching/
      Career → notes/career/
      Music → notes/music/
      Dog Training → notes/dog-training/
      Personal → notes/personal/
      Tech → notes/tech/
      Unclear → INBOX.md (for later sorting)
    NO → Is it a goal or plan?
      YES → GOALS.md under the matching area section
      NO → INBOX.md
```

## Worked Examples

Real examples of how to route different inputs:

1. **"I need to grade the theme unit by Friday"**
   - Route: `TASKS.md` → **Active** section
   - Format: `- [ ] [Teaching] Grade theme unit (due 2026-02-28)`
   - Reasoning: Has a deadline, clear action, time-sensitive

2. **"Maybe I should look into Google Certified Educator"**
   - Route: `TASKS.md` → **Someday** section
   - Format: `- [ ] [Career] Explore Google Certified Educator program`
   - Reasoning: Aspirational, no urgency, something to consider eventually

3. **"Students struggled with figurative language today — compound metaphors were the issue"**
   - Route: `notes/teaching/` → Create or update daily teaching notes
   - Format: Create file like `2026-02-24-figurative-language-observations.md`
   - Reasoning: Observation about student learning, not an action. Informs future lesson planning

4. **"Remind me to call Maria's mom about the conference"**
   - Route: `TASKS.md` → **Active** section
   - Format: `- [ ] [Teaching] Call Maria's mom to confirm conference attendance`
   - Reasoning: Clear action item, time-sensitive, needs follow-up

5. **"Jazz voicings: Cm7 uses C Eb G Bb, rootless voicing drops the C"**
   - Route: `notes/music/` → Create or update music reference notes
   - Format: Add to file like `jazz-voicings-reference.md`
   - Reasoning: Reference knowledge, not an action. Useful for future study/practice

---

## Troubleshooting

**Q: Where does this go?**
Use the Routing Decision Tree above. If unsure, ask: Is it an action (task), a thought (note), or unclear (inbox)?

**Q: Task or note?**
- **Task**: Has a deadline, action item, checkbox → TASKS.md
- **Note**: Reference, reflection, context → notes/ or journal/
- **Unsure**: INBOX.md first, decide during `/plan`

**Q: How many active tasks is too many?**
Typically 8-12 active across all areas. If more, consider moving some to "Someday" or reviewing during `/plan`.

**Q: Should I link between files?**
Yes! In journal entries or project plans, reference related tasks (e.g., "See TASKS.md: PM data analysis") or goals. This creates traceability.

---

## Integration with Plugin Commands

- **`/capture`**: Routes items to TASKS.md, INBOX.md, notes/, or knowledge/ based on content
- **`/plan`**: Reads TASKS.md, GOALS.md, INBOX.md; updates Current Focus and processes Unsorted
- **`/review`**: Reads and archives TASKS.md; creates journal entry; updates GOALS.md
- **`/briefing`**: Reads TASKS.md, GOALS.md, INBOX.md; presents scannable summary

This skill is the reference for all Second Brain file operations across the entire plugin.
