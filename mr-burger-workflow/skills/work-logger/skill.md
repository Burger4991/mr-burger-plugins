---
name: work-logger
description: >
  Use this skill when "logging completed work", "syncing session results",
  or converting the output of any teaching or data session into task updates,
  journal entries, or notes. Essential for the /sync command and sync hooks.
version: 1.0.0
---

# Work Logger

This skill defines how to take output from any session (teaching, data analysis, career work, etc.) and distill it into the right format for the Second Brain system.

## Logging Formats by Work Type

### Teaching: Unit/Lesson Completion
**Format for TASKS.md:**
```
- [x] [Teaching] Built [unit name] — [benchmark code] (completed YYYY-MM-DD)
```

**Example:**
```
- [x] [Teaching] Built Unit 2: Narrative Nonfiction — LAFS.910.RL.2.4 (completed 2026-02-24)
```

**Also create a journal entry** at `~/Desktop/SecondBrain/journal/YYYY-MM-DD-unit-[unit-name].md`:
```
# Unit: [Unit Name] — [Date]

## What Was Built
- Lesson plan: [link or reference]
- Student packet: [description]
- Benchmarks addressed: [list]
- ESOL scaffolds: [levels addressed, if any]

## Key Components
- [Day 1-2 summary]
- [Day 3-4 summary]
- [Day 5-6 summary]

## Notes
- Any special considerations
- Resources used
- Next unit or follow-ups
```

### Teaching: Lesson Plan Completion
**Format for TASKS.md:**
```
- [x] [Teaching] Built lesson plan — [topic/date] (completed YYYY-MM-DD)
```

### Teaching: Student Packet Creation
**Format for TASKS.md:**
```
- [x] [Teaching] Created student packet — [unit/topic] (completed YYYY-MM-DD)
```

### Data Analysis: Complete Analysis Session
**Format for notes/teaching/data-analysis-log.md:**
```
### [Date] — [Analysis Title]
- **Analyzed:** [What assessments or data, e.g., "FAST PM data for Q3"]
- **Scope:** [Which students/classes, e.g., "Period 3 IR"]
- **Key Findings:**
  - [Finding 1 with count/percentage if applicable]
  - [Finding 2]
  - [Finding 3 — focus on actionable insights]
- **Action Items:**
  - [Intervention needed for X students]
  - [Parent contacts required: [count]]
  - [Lesson adjustments needed]
- **Follow-ups:** [Any tasks to add to TASKS.md]
```

**Example:**
```
### 2026-02-24 — Q3 FAST PM Analysis (Period 3 IR)
- **Analyzed:** FAST PM Reading Levels for 25 students
- **Scope:** Period 3 Intensive Reading
- **Key Findings:**
  - 8 students (32%) showing growth to Level 3+
  - 5 students (20%) still at Level 1 — intervention needed
  - 3 students showing regression (need parent contact)
- **Action Items:**
  - Implement small group instruction for Level 1 cohort
  - Schedule parent conferences: Maria S., Juan R., Ashley M.
  - Differentiate Packet 3 for advanced tier
- **Follow-ups:** Add parent contact tasks to TASKS.md
```

**Also add to TASKS.md if action items exist:**
```
- [ ] [Teaching] Follow up on PM data — contact parents (due by 2026-02-28)
- [ ] [Teaching] Small group instruction — Tier 1 students (Period 3)
- [ ] [Teaching] Differentiate Unit 2 Packet 3 for advanced tier
```

### Data Analysis: Growth Report
**Format for TASKS.md:**
```
- [x] [Teaching] Completed growth analysis — [grade/period/timeframe] (completed YYYY-MM-DD)
```

**Add summary to journal** if significant:
```
# Growth Report: [Period/Grade] — [Date]

## Overall Growth
[Summary of growth metrics]

## By Tier
- **Tier 1 (Intervention):** [count and status]
- **Tier 2 (Core):** [count and status]
- **Tier 3 (Advanced):** [count and status]

## Standout Findings
- [Notable improvements]
- [Areas of concern]

## Next Steps
[Instructional adjustments, interventions, etc.]
```

### Teaching: Parent Contact
**Format for logs/parent-contacts.md:**
```
| [YYYY-MM-DD] | [Student Name/Initials] | [Method: Phone/Email/In-Person] | [Topic] | [Outcome] | [Follow-up] |
```

**Example:**
```
| 2026-02-24 | Maria S. | Phone | FAST PM regression | Discussed intervention plan, parent agreed | Schedule 2-week check-in |
```

**Also add to TASKS.md if follow-up is needed:**
```
- [ ] [Teaching] Follow up with Maria S. re: intervention plan (due by 2026-03-10)
```

### Career Work
**Format for TASKS.md:**
```
- [x] [Career] [description] (completed YYYY-MM-DD)
```

**Examples:**
```
- [x] [Career] Applied to teaching position — Jefferson High (completed 2026-02-24)
- [x] [Career] Completed portfolio update with new unit designs (completed 2026-02-24)
- [x] [Career] Networking call with Dr. Patterson — discussed EdTech roles (completed 2026-02-24)
```

**Also add to journal** if it's a major milestone:
```
# [Career Milestone] — [Date]

## What Happened
[Summary of work or conversation]

## Key Takeaways
[Insights, next steps, contacts]

## Follow-ups
[Applications, follow-up conversations, materials to send]
```

### Music Work
**Format for TASKS.md:**
```
- [x] [Music] [description] (completed YYYY-MM-DD)
```

**Examples:**
```
- [x] [Music] Practiced Adam routine — [tempo/duration] (completed 2026-02-24)
- [x] [Music] Transcribed [tune name] (completed 2026-02-24)
```

### Dog Training Work
**Format for TASKS.md:**
```
- [x] [Dog Training] [description] (completed YYYY-MM-DD)
```

**Examples:**
```
- [x] [Dog Training] J-Walk practice with Olive — [duration/outcome] (completed 2026-02-24)
- [x] [Dog Training] Reviewed Recallers course module [X] (completed 2026-02-24)
```

## Core Rules

1. **Check Before Logging**
   - Always search TASKS.md for a matching task before creating a new completion entry
   - If a task already exists, update it instead of duplicating

2. **Don't Log Trivial Work**
   - One-off questions
   - Quick lookups
   - Routine answering of emails
   - Exploratory browsing
   - Short conversations under 5 minutes with no deliverable

3. **Use Consistent Area Tags**
   - Always use exactly one tag: `[Teaching]`, `[Career]`, `[Music]`, `[Dog Training]`, `[Personal]`, `[Tech]`
   - Do not mix or create new tags

4. **Date Format**
   - Always use `YYYY-MM-DD` format
   - Use `(completed YYYY-MM-DD)` for task completions
   - Use `[YYYY-MM-DD]` for log entries like parent contacts
   - Use `YYYY-MM-DD-[topic]` for journal file names

5. **Journal Entries Are Selective**
   - Use for significant completions and milestones
   - Examples: finished unit, major analysis, significant career progress, breakthrough in dog training
   - Do NOT journal every daily task
   - Limit to 1-2 per week typically

6. **Extract and Distribute**
   - Data analysis outputs often have multiple action items
   - Extract action items and add them as separate tasks to TASKS.md
   - Route parent contacts from analysis sessions to both logs/parent-contacts.md AND TASKS.md
   - Don't lose follow-ups in long analysis notes

## Special Cases

### Multiple Outputs from One Session
If a session produces multiple outputs (e.g., data analysis + parent contacts + lesson adjustments):
1. Log the primary completion (e.g., analysis) to TASKS.md and data-analysis-log.md
2. Extract secondary items as separate tasks
3. Log parent contacts separately
4. Create ONE journal entry if it was a significant session

### Retroactive Logging
If you're syncing work that was completed in a previous session:
- Use the actual completion date if known
- If unknown, use the date you discovered/logged it
- Add a note if significant time has passed: "(completed [actual date], logged [current date])"

### Cross-Plugin Outputs
If a plugin session produces outputs that should go to another plugin:
- Log in current plugin's native format
- Also add task or note in destination plugin
- Example: ir-data-pipeline produces analysis → add note to mr-burger-workflow's data-analysis-log AND create action item task

---

## Quick Reference Table

| Work Type | Primary Log | Secondary Log | Task Format |
|-----------|------------|---------------|------------|
| Unit built | TASKS.md | journal/ | `[Teaching] Built [unit] — [benchmark]` |
| Lesson plan | TASKS.md | (optional journal/) | `[Teaching] Built lesson plan — [topic]` |
| Data analysis | data-analysis-log.md | journal/ (if major) | `[Teaching] Completed analysis — [scope]` |
| Parent contact | parent-contacts.md | TASKS.md (if follow-up) | `[Teaching] Follow up with [name]` |
| Career work | TASKS.md | journal/ (if major) | `[Career] [description]` |
| Music work | TASKS.md | — | `[Music] [description]` |
| Dog training | TASKS.md | — | `[Dog Training] [description]` |
| Personal | TASKS.md | notes/ | `[Personal] [description]` |
| Tech | TASKS.md | notes/ | `[Tech] [description]` |
