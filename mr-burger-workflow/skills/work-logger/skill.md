---
name: work-logger
description: >
  Use this skill when "logging completed work" or converting the output of any
  teaching or data session into task updates and notes. Defines how to record
  completions in TASKS.md and area notes.md files.
version: 2.0.0
---

# Work Logger

This skill defines how to take output from any session (teaching, data analysis, career work, etc.) and distill it into the right format for TASKS.md and area notes files.

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

**For significant units**, append a dated entry to `~/Documents/Teaching/notes.md`:
```markdown
## YYYY-MM-DD — Unit: [Unit Name]

- Lesson plan: [reference]
- Student packet: [description]
- Benchmarks addressed: [list]
- ESOL scaffolds: [levels addressed, if any]
- Day-by-day: [brief summary]
- Notes: [special considerations, resources used, next unit]
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

**Format for `~/Documents/Teaching/Resources/data-analysis-log.md`:**
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

**For significant analyses**, append to `~/Documents/Teaching/notes.md`:
```markdown
## YYYY-MM-DD — Growth Report: [Period/Grade]

**Overall Growth:** [Summary of growth metrics]

**By Tier:**
- Tier 1 (Intervention): [count and status]
- Tier 2 (Core): [count and status]
- Tier 3 (Advanced): [count and status]

**Standout Findings:** [Notable improvements, areas of concern]

**Next Steps:** [Instructional adjustments, interventions]
```

### Teaching: Parent Contact

**Format for `~/Documents/Teaching/logs/parent-contacts.md`:**
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

**For major milestones**, append to `~/Documents/Career/notes.md`:
```markdown
## YYYY-MM-DD — [Career Milestone]

[Summary of work or conversation, key takeaways, follow-ups]
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

---

## Core Rules

1. **Check Before Logging**
   - Always search TASKS.md for a matching task before creating a new completion entry
   - If a task already exists, update it instead of duplicating

2. **Don't Log Trivial Work**
   - One-off questions
   - Quick lookups
   - Routine email answering
   - Short conversations under 5 minutes with no deliverable

3. **Use Consistent Area Tags**
   - Always use exactly one tag: `[Teaching]`, `[Career]`, `[Music]`, `[Dog Training]`, `[Personal]`, `[Tech]`
   - Do not mix or create new tags

4. **Date Format**
   - Always use `YYYY-MM-DD`
   - Use `(completed YYYY-MM-DD)` for task completions
   - Use `[YYYY-MM-DD]` for log entries like parent contacts
   - Use `## YYYY-MM-DD — Topic` for notes.md entries

5. **Notes Entries Are Selective**
   - Use for significant completions and milestones
   - Examples: finished unit, major analysis, significant career progress, training breakthrough
   - Don't log every daily task to notes.md
   - Limit to 1-2 per week typically

6. **Extract and Distribute**
   - Data analysis outputs often have multiple action items
   - Extract action items and add them as separate tasks to TASKS.md
   - Route parent contacts from analysis sessions to both `logs/parent-contacts.md` AND TASKS.md
   - Don't lose follow-ups in long analysis notes

---

## Special Cases

### Multiple Outputs from One Session
If a session produces multiple outputs (e.g., data analysis + parent contacts + lesson adjustments):
1. Log the primary completion (e.g., analysis) to TASKS.md and data-analysis-log.md
2. Extract secondary items as separate tasks
3. Log parent contacts separately
4. Add ONE notes.md entry if it was a significant session

### Retroactive Logging
If you're syncing work completed in a previous session:
- Use the actual completion date if known
- If unknown, use the date you discovered/logged it
- Add a note if significant time has passed: `(completed [actual date], logged [current date])`

### Cross-Plugin Outputs
If a plugin session produces outputs that should go to another plugin:
- Log in current plugin's native format
- Also add task or note in destination plugin
- Example: ir-data-pipeline produces analysis → add entry to Teaching/notes.md AND create action item task

---

## Quick Reference Table

| Work Type | Primary Log | Secondary Log | Task Format |
|-----------|------------|---------------|------------|
| Unit built | TASKS.md | Teaching/notes.md (if major) | `[Teaching] Built [unit] — [benchmark]` |
| Lesson plan | TASKS.md | — | `[Teaching] Built lesson plan — [topic]` |
| Data analysis | data-analysis-log.md | Teaching/notes.md (if major) | `[Teaching] Completed analysis — [scope]` |
| Parent contact | parent-contacts.md | TASKS.md (if follow-up) | `[Teaching] Follow up with [name]` |
| Career work | TASKS.md | Career/notes.md (if major) | `[Career] [description]` |
| Music work | TASKS.md | Music/notes.md (if notable) | `[Music] [description]` |
| Dog training | TASKS.md | Dog-Training/notes.md (if notable) | `[Dog Training] [description]` |
| Personal | TASKS.md | Personal/notes.md | `[Personal] [description]` |
| Tech | TASKS.md | Tech/notes.md | `[Tech] [description]` |
