---
name: plugin-registry
description: >
  This skill documents the plugin ecosystem and how to route data between plugins.
  Use when /status or /sync commands need to find and coordinate data sources,
  or when you need to understand what each plugin tracks and where to look for outputs.
version: 1.0.0
---

# Plugin Registry

This is the central registry of Mr. Burger's plugin ecosystem and how they connect.

## Installed Plugins

| Plugin | What It Tracks | Key Files/Locations |
|--------|---------------|-------------------|
| **ir-teaching** | Lesson plans, units, benchmarks, ESOL materials | `~/Documents/Teaching/` |
| **ir-data-pipeline** | Student assessment data, growth analysis, reports | `~/Documents/Teaching/data/` (outputs) |
| **mr-burger-workflow** | Tasks, goals, inbox, journal, notes across all areas | `~/Desktop/SecondBrain/` |
| **ir-classroom-ops** | Parent contacts, behavior notes, PD hours, observation prep | `~/Documents/Teaching/logs/`, `~/Documents/Teaching/observation-prep/` |
| **cross-plugin-bridge** (this plugin) | Coordination and sync across all plugins | Hooks, commands, registry |

## Cross-Plugin Data Flows

| Source Plugin | Output | → Destination Plugin | Input |
|--------------|--------|---------------------|-------|
| ir-teaching | Completed unit | → mr-burger-workflow | Task marked done in TASKS.md |
| ir-data-pipeline | Analysis report | → mr-burger-workflow | Note in notes/teaching/ |
| ir-data-pipeline | Risk students identified | → ir-classroom-ops | Parent contact needed in TASKS.md |
| ir-data-pipeline | Growth summary | → mr-burger-workflow | Journal entry |
| ir-classroom-ops | Contact log entries | → mr-burger-workflow | Task follow-ups in TASKS.md |
| ir-classroom-ops | Observation prep | → ir-teaching | Lesson plan reference |

## File Detection Patterns

Use this table to map file patterns to their source plugins and routing:

| Pattern | Plugin | Action |
|---------|--------|--------|
| `*-unit-*.md`, `*lesson-plan*` | ir-teaching | Log as teaching work, check for completion |
| `*-packet*`, `*bellringer*` | ir-teaching | Log as student materials |
| `*analysis*`, `*growth*`, `*report*` | ir-data-pipeline | Log as data work, check for action items |
| `*-sub-plan*` | ir-teaching (sub-plan-generator) | Log as sub plan, reference in daily prep |
| `parent-contacts.md`, `behavior-notes.md` | ir-classroom-ops | Already logged, check for follow-up tasks |
| `obs-prep*.md` | ir-classroom-ops | Log as observation prep, note date of observation |
| `TASKS.md`, `INBOX.md`, `GOALS.md` | mr-burger-workflow | Core Second Brain files, don't double-log |

## Cross-Plugin Data Flows

Use these specific flow examples to understand how data moves between plugins:

```
DATA ANALYSIS → TASKS
  growth-analyzer output shows Student X is Tier 3
  → Action item: "Schedule parent conference for Student X re: Tier 3 reading support"
  → Route to: TASKS.md Active + parent-contact-log (pending follow-up)

UNIT BUILDING → TASKS
  unit-builder-protocol completes Unit 3
  → Task update: Move "Build Unit 3: Poetry" from Active to Done
  → Route to: TASKS.md Done + journal entry (what worked, what didn't)

OBSERVATION PREP → JOURNAL
  /obs-prep generates walkthrough sheet for Period 3, Day 4
  → Journal entry: "Prepared for admin observation, Period 3, Theme unit Day 4"
  → Route to: journal/YYYY-MM-DD.md with date and observation context

BEHAVIOR LOGGING → PARENT CONTACT
  /log captures multiple behavior entries for Student X
  → Identify pattern (3+ entries about disruption)
  → Action: Add task "Schedule parent conference re: [Student X] behavior support"
  → Route to: TASKS.md Active + parent-contacts-log (pending follow-up)
```

## Bash Commands for File Discovery

Use these commands to detect when work has been completed and needs syncing:

```bash
# Find recent teaching work (last 24h)
find ~/Documents/Teaching/ -name "*.md" -mtime -1 2>/dev/null | sort

# Find recent data outputs
find ~/Documents/Teaching/data/ \( -name "*.csv" -o -name "*.xlsx" \) -mtime -1 2>/dev/null

# Count active tasks in Second Brain
grep -c "^- \[ \]" ~/Desktop/SecondBrain/TASKS.md 2>/dev/null || echo "0"

# Find pending follow-ups in contact log (look for "Follow-up: Yes" or similar)
grep -i "yes\|pending" ~/Documents/Teaching/logs/parent-contacts.md 2>/dev/null | wc -l

# List all recent observation prep documents
find ~/Documents/Teaching/observation-prep/ -name "*obs-prep*.md" -mtime -7 2>/dev/null | sort -r

# Check for recently completed lessons/units
find ~/Documents/Teaching/units/ -name "*.md" -mtime -3 2>/dev/null
```

## Detection Patterns

Use these patterns to identify when work has been completed and needs syncing:

### Unit/Lesson Completion
- New files matching patterns: `*-lesson-plan.md`, `*-student-packet.md`, `*-unit-plan.md`
- Location: `~/Documents/Teaching/units/`, `~/Documents/Teaching/lesson-plans/`
- Action: Mark task done in TASKS.md, add to journal if major unit

### Data Analysis Completion
- New CSV/Excel files in `~/Documents/Teaching/data/outputs/`
- Files matching patterns: `*-report.*`, `*-analysis.*`, `*-growth.*`
- Check modification time against last sync
- Action: Create data-analysis-log entry, extract action items to TASKS.md

### Parent Contact Log Updates
- File: `~/Documents/Teaching/logs/parent-contacts.md`
- Check modification time and new entries since last sync
- Look for student names, contact dates, methods, topics, follow-up flags
- Action: Extract follow-ups as tasks in TASKS.md if not already there

### Task Completion Detection
- File: `~/Desktop/SecondBrain/TASKS.md`
- Look for items with `[x]` that weren't marked complete before
- Check date stamps if available
- Action: Cross-reference with other plugins to understand what was completed

## Data Format Standards

### Task Entry Format (TASKS.md)
```
- [x] [Area] Task description (completed YYYY-MM-DD)
- [ ] [Area] Task description
```
Areas: Teaching, Career, Music, Dog Training, Personal, Tech

### Data Analysis Log Entry (notes/teaching/data-analysis-log.md)
```
### [Date] — [Analysis Title]
- **Analyzed:** [What was assessed/analyzed]
- **Key Findings:** [Summary of results]
- **Action Items:** [Any follow-ups needed, student interventions, contacts]
```

### Journal Entry (journal/YYYY-MM-DD-[topic].md)
```
# [Topic] — [Date]

## What Happened
[Summary of completed work]

## Key Takeaways
[Lessons learned, insights, next steps]

## Related Tasks
[Links or references to TASKS.md items]
```

### Parent Contact Log Entry (logs/parent-contacts.md)
```
| [Date] | [Student/Initials] | [Method] | [Topic] | [Outcome] | [Follow-up] |
```

## File Structure Reference

```
~/Documents/Teaching/
├── units/
│   ├── unit-name-unit-plan.md
│   ├── unit-name-lesson-plan.md
│   └── unit-name-student-packet.md
├── lesson-plans/
│   └── [individual lesson plans]
├── data/
│   ├── inputs/
│   │   └── [raw assessment data, FAST scores, etc.]
│   └── outputs/
│       └── [analysis reports, growth reports, tier reports]
├── logs/
│   ├── parent-contacts.md
│   ├── behavior-notes.md
│   └── pd-log.md
└── observation-prep/
    └── [lesson plans, materials for observations]

~/Desktop/SecondBrain/
├── TASKS.md
├── GOALS.md
├── INBOX.md
├── journal/
│   └── YYYY-MM-DD-[topic].md
└── notes/
    ├── teaching/
    │   ├── data-analysis-log.md
    │   ├── unit-build-log.md
    │   └── [other teaching notes]
    ├── career/
    ├── music/
    ├── dog-training/
    ├── personal/
    └── tech/
```

---

## Using This Registry

**For /status command:**
1. Check plugin column to see where data lives
2. Use Key Files/Locations to find the right folders
3. Pull counts and recent items from each location

**For /sync command:**
1. Use Detection Patterns to identify completed work
2. Use Cross-Plugin Data Flows to understand where to route outputs
3. Use Data Format Standards to format entries correctly

**For custom queries:**
- Ask "Where does [X] get tracked?" → look in What It Tracks column
- Ask "What does plugin [Y] output?" → look in Data Flows section
- Ask "How do I recognize [completed work type]?" → look in Detection Patterns
