---
name: plugin-registry
description: >
  This skill documents which PLUGIN owns what data and how plugins connect to each other.
  Clarifies PLUGIN ownership, data routing, and inter-plugin coordination.
  Use when commands need to find and coordinate data sources,
  or when you need to understand what each plugin tracks and where to look for outputs.
  Distinct from area-context which is about personal life areas and project file locations.
version: 2.0.0
---

# Plugin Registry

This is the central registry of Mr. Burger's plugin ecosystem and how they connect.

## Installed Plugins

| Plugin | What It Tracks | Key Files/Locations |
|--------|---------------|-------------------|
| **ir-teaching** | Lesson plans, units, benchmarks, ESOL materials | `~/Documents/Teaching/` |
| **mr-burger-music** | Practice sessions, exercises, band materials, LHS system | `~/Documents/Music/` |
| **ir-data-pipeline** | Student assessment data, growth analysis, reports | `~/Documents/Teaching/Student-Data/` (inputs), `~/Documents/Teaching/` (outputs) |
| **mr-burger-workflow** | Tasks, captures, session state across all areas | `~/Documents/TASKS.md`, `~/Documents/[area]/notes.md` |
| **ir-classroom-ops** | Parent contacts, behavior notes, PD hours, observation prep | `~/Documents/Teaching/logs/`, `~/Documents/Teaching/observation-prep/` |

## Cross-Plugin Data Flows

| Source Plugin | Output | → Destination Plugin | Input |
|--------------|--------|---------------------|-------|
| ir-teaching | Completed unit | → mr-burger-workflow | Task marked done in TASKS.md |
| ir-data-pipeline | Analysis report | → mr-burger-workflow | Entry in Teaching/notes.md |
| ir-data-pipeline | Risk students identified | → ir-classroom-ops | Parent contact needed in TASKS.md |
| ir-data-pipeline | Growth summary | → mr-burger-workflow | Entry in Teaching/notes.md |
| ir-classroom-ops | Contact log entries | → mr-burger-workflow | Task follow-ups in TASKS.md |
| ir-classroom-ops | Observation prep | → ir-teaching | Lesson plan reference |
| mr-burger-music | Session log entry | → mr-burger-workflow | Note in notes/music/ |
| mr-burger-music | Weekly practice summary | → mr-burger-workflow | Journal entry |

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
| `TASKS.md` | mr-burger-workflow | Master task file — don't double-log |

## Cross-Plugin Flow Examples

```
DATA ANALYSIS → TASKS
  growth-analyzer output shows Student X is Tier 3
  → Action item: "Schedule parent conference for Student X re: Tier 3 reading support"
  → Route to: ~/Documents/TASKS.md Active + parent-contact-log (pending follow-up)

UNIT BUILDING → TASKS
  unit-builder-protocol completes Unit 3
  → Task update: Move "Build Unit 3: Poetry" from Active to Done in TASKS.md
  → Add dated entry to ~/Documents/Teaching/notes.md (what worked, what didn't)

OBSERVATION PREP → NOTES
  /obs-prep generates walkthrough sheet for Period 3, Day 4
  → Add dated entry to ~/Documents/Teaching/notes.md: observation context, period, unit day
  → Route to: Teaching/notes.md with date header

BEHAVIOR LOGGING → PARENT CONTACT
  /log captures multiple behavior entries for Student X
  → Identify pattern (3+ entries about disruption)
  → Action: Add task "Schedule parent conference re: [Student X] behavior support"
  → Route to: TASKS.md Active + parent-contacts-log (pending follow-up)

PRACTICE LOGGING → NOTES
  music-coach session completed (optional weekly summary)
  → Summary: "Week of YYYY-MM-DD — X sessions, trumpet blocks, guitar blocks, key struggles"
  → Route to: ~/Documents/Music/Practice/notes/weekly-summary-YYYY-MM-DD.md
```

## Bash Commands for File Discovery

```bash
# Find recent teaching work (last 24h)
find ~/Documents/Teaching/ -name "*.md" -mtime -1 2>/dev/null | sort

# Find recent data outputs
find ~/Documents/Teaching/Student-Data/ \( -name "*.csv" -o -name "*.xlsx" \) -mtime -1 2>/dev/null

# Count active tasks
grep -c "^- \[ \]" ~/Documents/TASKS.md 2>/dev/null || echo "0"

# Find pending follow-ups in contact log
grep -i "yes\|pending" ~/Documents/Teaching/logs/parent-contacts.md 2>/dev/null | wc -l

# List all recent observation prep documents
find ~/Documents/Teaching/observation-prep/ -name "*obs-prep*.md" -mtime -7 2>/dev/null | sort -r

# Check for recently completed lessons/units
find ~/Documents/Teaching/Units/ -name "*.md" -mtime -3 2>/dev/null
```

## Detection Patterns

### Unit/Lesson Completion
- New files matching: `*-lesson-plan.md`, `*-student-packet.md`, `*-unit-plan.md`
- Location: `~/Documents/Teaching/Units/`
- Action: Mark task done in TASKS.md, add entry to Teaching/notes.md if major unit

### Data Analysis Completion
- New CSV/Excel files in `~/Documents/Teaching/Student-Data/`
- Files matching: `*-report.*`, `*-analysis.*`, `*-growth.*`
- Action: Create entry in data-analysis-log, extract action items to TASKS.md

### Parent Contact Log Updates
- File: `~/Documents/Teaching/logs/parent-contacts.md`
- Look for student names, contact dates, methods, topics, follow-up flags
- Action: Extract follow-ups as tasks in TASKS.md if not already there

### Task Completion Detection
- File: `~/Documents/TASKS.md`
- Look for items with `[x]` that weren't marked complete before
- Action: Cross-reference with other plugins to understand what was completed

## Data Format Standards

### Task Entry Format (TASKS.md)
```
- [x] [Area] Task description (completed YYYY-MM-DD)
- [ ] [Area] Task description
```
Areas: Teaching, Career, Music, Dog Training, Personal, Tech

### Data Analysis Log Entry (Teaching/Resources/data-analysis-log.md)
```
### [Date] — [Analysis Title]
- **Analyzed:** [What was assessed/analyzed]
- **Key Findings:** [Summary of results]
- **Action Items:** [Any follow-ups needed, student interventions, contacts]
```

### Notes Entry (Documents/[area]/notes.md)
```
## [YYYY-MM-DD] — [Topic]

[Content — summary of completed work, key observations, next steps]
```

### Parent Contact Log Entry (logs/parent-contacts.md)
```
| [Date] | [Student/Initials] | [Method] | [Topic] | [Outcome] | [Follow-up] |
```

## File Structure Reference

```
~/Documents/
├── TASKS.md                        # Master task list
├── Teaching/
│   ├── Units/
│   │   ├── unit-name-unit-plan.md
│   │   ├── unit-name-lesson-plan.md
│   │   └── unit-name-student-packet.md
│   ├── Student-Data/
│   │   └── [raw assessment data, FAST scores, analysis outputs]
│   ├── Resources/
│   │   └── data-analysis-log.md
│   ├── logs/
│   │   ├── parent-contacts.md
│   │   ├── behavior-notes.md
│   │   └── pd-log.md
│   ├── observation-prep/
│   │   └── [lesson plans, materials for observations]
│   └── notes.md                    # Teaching captures and working notes
├── Career/
│   └── notes.md
├── Music/
│   └── notes.md
├── Dog-Training/
│   └── notes.md
└── Personal/
    └── notes.md
```

---

## Using This Registry

**For finding where data lives:**
- Check the Plugin column in Installed Plugins table
- Use Key Files/Locations to find the right folders

**For understanding how outputs move between plugins:**
- Use Cross-Plugin Data Flows table
- Use Flow Examples for specific scenarios

**For custom queries:**
- "Where does [X] get tracked?" → look in What It Tracks column
- "What does plugin [Y] output?" → look in Data Flows section
- "How do I recognize [completed work type]?" → look in Detection Patterns
