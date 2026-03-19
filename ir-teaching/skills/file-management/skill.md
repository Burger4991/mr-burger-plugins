---
name: file-management
description: File naming conventions, version control, and archive procedures for IR unit materials. Use when organizing files or managing unit updates.
---

# File Management for IR Units

## Naming Conventions

### Unit Folder Names

Format: `[TextName]-[Benchmark]`

Use the text's short name and the benchmark topic, joined by a hyphen.

**Examples:**
```
Necklace-Theme
Daedalus-LiteraryElements
ObamaEducation-PurposePerspective
NixonCheckers-Rhetoric
SchoolStartTimes-Argument
Orpheus-FigurativeLanguage
AliCogia-LiteraryElements
```

**Rules:**
- No spaces in folder names — use PascalCase for multi-word names
- Benchmark topic should match the standard terminology (Theme, LiteraryElements, FigurativeLanguage, CentralIdea, TextStructure, PurposePerspective, Argument, Rhetoric, Poetry)
- If a text is reused for a different benchmark, create a separate folder

### File Names

Format: `[TextName]-[Type]-[MMDDYY]-v[#].[ext]`

**Components:**
- **TextName**: Short descriptor matching the folder name (e.g., `AliCogia`, `Necklace`)
- **Type**: Deliverable type (see codes below)
- **MMDDYY**: Date created (month-day-year, 6 digits)
- **v[#]**: Version number starting at v1, incremented on each revision
- **ext**: File extension (.md, .docx, .pptx, .html, .pdf)

### Deliverable Type Codes

- **LessonPlan** — Complete teacher lesson plan
- **StudentPacket** — Student activity packet
- **AnswerKey** — Answer key with exemplars
- **Slides** — PowerPoint slide deck
- **InteractiveLesson** — HTML interactive lesson for Promethean board
- **ExitTickets** — Exit ticket set
- **CoverPage** — Unit overview cover page
- **Assessment** — Mini-assessment or end-of-unit test
- **FeedbackForm** — Student feedback form
- **BenchmarkLesson** — Standalone benchmark lesson HTML
- **AnchorCharts** — Visual reference materials
- **TestPrep-StudentPacket** — 4-day test prep student packet
- **TestPrep-TeacherPlan** — 4-day test prep teacher plan
- **TestPrep-AnswerKey** — 4-day test prep answer key
- **SubPlan** — Substitute teacher plan

### Examples

**Core unit deliverables:**
```
AliCogia-LessonPlan-030826-v1.docx
AliCogia-StudentPacket-030826-v1.docx
AliCogia-AnswerKey-030826-v1.docx
AliCogia-Slides-030826-v1.pptx
AliCogia-InteractiveLesson-030826-v1.html
AliCogia-ExitTickets-030826-v1.docx
AliCogia-CoverPage-030826-v1.docx
AliCogia-FeedbackForm-030826-v1.docx
```

**Revised versions:**
```
AliCogia-StudentPacket-030826-v2.docx    ← revised after Day 2 feedback
AliCogia-InteractiveLesson-030926-v3.html ← third iteration
```

**Test prep materials:**
```
AliCogia-TestPrep-StudentPacket-031526-v1.md
AliCogia-TestPrep-TeacherPlan-031526-v1.md
AliCogia-TestPrep-AnswerKey-031526-v1.md
```

**Sub plans:**
```
BlueJeans-SubPlan-D3-011026-v1.md
BlueJeans-SubPlan-D3D4-011026-v1.md
```

## Folder Structure

### Unit Folder Layout (Flat)

All deliverables live directly in the unit folder. Only district source files and archived versions go in subfolders.

```
Teaching/
├── Units/
│   ├── AliCogia-LiteraryElements/
│   │   ├── AliCogia-LessonPlan-030826-v1.docx
│   │   ├── AliCogia-StudentPacket-030826-v1.docx
│   │   ├── AliCogia-AnswerKey-030826-v1.docx
│   │   ├── AliCogia-Slides-030826-v1.pptx
│   │   ├── AliCogia-InteractiveLesson-030826-v1.html
│   │   ├── AliCogia-ExitTickets-030826-v1.docx
│   │   ├── AliCogia-CoverPage-030826-v1.docx
│   │   ├── AliCogia-FeedbackForm-030826-v1.docx
│   │   ├── AliCogia-TestPrep-StudentPacket-031526-v1.md
│   │   ├── AliCogia-TestPrep-TeacherPlan-031526-v1.md
│   │   ├── AliCogia-TestPrep-AnswerKey-031526-v1.md
│   │   ├── _district/
│   │   │   └── Ali_Cogia-student_copy.pdf
│   │   ├── _archive/
│   │   │   └── AliCogia-StudentPacket-030826-v1.docx
│   │   └── _ChangeLog.txt
│   │
│   ├── Necklace-Theme/
│   │   └── [same flat structure]
│   │
│   ├── _Archive_PreReorganization/
│   │   └── [old units from before this system]
│   │
│   └── _Assessments/
│       └── [standalone assessments not tied to a specific unit]
│
├── Student-Data/
│   └── 2025-2026/
├── Resources/
├── Curriculum-Guides/
├── Programs/
└── Professional/
```

### Subfolder Purposes

- **`_district/`** — Original materials from the district (PDFs, teacher copies). Read-only reference. Never edit these.
- **`_archive/`** — Old versions of files after revision. Only keep the 2 most recent old versions.
- **`_ChangeLog.txt`** — Record of all updates to the unit (see format below).

### Top-Level Teaching Folders

| Folder | Purpose |
|--------|---------|
| `Units/` | All IR units (current and working) |
| `Student-Data/` | FAST, PM, NWEA data organized by school year |
| `Resources/` | Shared teaching resources (anchor charts, strategy references) |
| `Curriculum-Guides/` | District curriculum documents |
| `Programs/` | Program-specific materials |
| `Professional/` | PD, observations, professional docs |
| `Data-Archive/` | Historical data archives |

## Version Control

### Creating New Versions

When revising any deliverable:

1. **Increment the version number** in the filename (v1 → v2)
2. **Move the old version** to `_archive/`
3. **Update `_ChangeLog.txt`** with what changed and why

**Example:**
```
# Original
AliCogia-StudentPacket-030826-v1.docx

# After revision
AliCogia-StudentPacket-030826-v2.docx            ← current version
_archive/AliCogia-StudentPacket-030826-v1.docx    ← archived
```

**If revising on a different date** (e.g., making changes a week later), use the new date:
```
AliCogia-StudentPacket-031526-v1.docx             ← fresh version with new date
_archive/AliCogia-StudentPacket-030826-v2.docx    ← archived
```

### Change Log Format

**File:** `_ChangeLog.txt` in the root of each unit folder.

```
[Unit Name] - Change Log

=== 03-15-26 ===
UPDATED: Student Packet (v1 → v2)
Changes:
- Added 5th row to theme organizer (You Do independent)
- Expanded vocabulary practice with sentence writing

Files affected:
✓ AliCogia-StudentPacket-030826-v2.docx (NEW VERSION)
✓ AliCogia-LessonPlan-030826-v2.docx (UPDATED - Day 4 procedures)
✓ AliCogia-AnswerKey-030826-v2.docx (UPDATED - added exemplar for row 5)
○ AliCogia-Slides-030826-v1.pptx (NO CHANGE)
○ District files (NO CHANGE)

=== 03-08-26 ===
CREATED: Initial unit build
Files created:
- Lesson Plan (6 days)
- Student Packet (6 days)
- Answer Key with exemplars
- Slide deck (Days 1-6)
- Interactive Lesson (HTML)
- Exit tickets (Days 1-6)
- Cover page
- Feedback form

Benchmark: ELA.10.R.1.1 - Literary Elements
Text: "Ali Cogia" (adapted myth)
```

### Archive Management

**Archive rules:**
- Keep only the **2 most recent old versions** in `_archive/`
- Delete older versions unless they represent a fundamentally different approach
- At end of school year, consider archiving entire unit folders to `_Archive_PreReorganization/`

## File Format Standards

### Preferred Formats

| Material | Format | Notes |
|----------|--------|-------|
| Lesson plans | .docx | Primary delivery format |
| Student packets | .docx | For printing and distribution |
| Answer keys | .docx | Matches student packet format |
| Slides | .pptx | Never .ppt or .pdf |
| Interactive lessons | .html | Self-contained, single file |
| Test prep materials | .md | Markdown for quick iteration |
| Sub plans | .md | Markdown for quick creation |
| District originals | .pdf | Keep as received, never edit |

### Format Notes

- **.docx is the standard** for final print-ready deliverables (student packets, lesson plans, answer keys)
- **.md is for drafts and quick-turnaround materials** (test prep, sub plans, working documents)
- **.html is for interactive content** (Promethean board lessons, anchor charts)
- **.gdoc files** may appear as Google Doc download artifacts — these are not primary deliverables

## Syncing and Alignment

### When Files Must Match

If you update ONE deliverable, check if others need updates:

**Student Packet updated →** Check: Lesson Plan (procedures), Answer Key (new questions need answers), Slides (student tasks shown on slides)

**Lesson Plan updated →** Check: Student Packet (activities match what lesson plan says), Answer Key (teacher script examples)

**Organizer structure changed →** Update ALL: Lesson Plan (I Do/We Do/You Do scripts), Student Packet (organizer with scaffolds), Answer Key (completed exemplar organizer), Slides (organizer structure shown)

### Verification After Updates

After making updates, verify alignment:
1. Vocabulary, organizer content, and examples match across lesson plan, student packet, and slides
2. All updated files share the same version number or update date
3. Lesson plan procedures match student packet activities
4. Answer keys reflect any changes to student organizers or questions

## Sharing and Printing

### For Printing
- Student packets: Print 1 per student, stapled
- Lesson plans: Keep digital on teaching laptop
- Answer keys: Print 1 for teacher reference
- Slides/interactive lessons: Present digitally, don't print

### For Sharing (with other teachers)
- Share the entire unit folder (zip file)
- Include `_ChangeLog.txt` for version context
- Include `_district/` files for reference
- Don't share `_archive/` contents

### For Submission (to admin/district)
- Export final versions to .pdf if requested
- Name: `[TextName]-[Type]-FINAL.[pdf]`
- Don't share archived versions or change logs

## Critical Rules

1. **NEVER delete files** without moving to `_archive/` first
2. **ALWAYS update `_ChangeLog.txt`** when making changes
3. **ALWAYS increment version numbers** when revising (never overwrite)
4. **ALWAYS verify alignment** across deliverables before reporting "complete"
5. **ALWAYS keep district originals untouched** in `_district/`
6. **ONE flat folder per unit** — no nested subfolders except `_district/` and `_archive/`
