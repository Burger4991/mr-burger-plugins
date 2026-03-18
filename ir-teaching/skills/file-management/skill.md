---
name: file-management
description: File naming conventions, version control, and archive procedures for IR unit materials. Use when organizing files or managing unit updates.
---

# File Management for IR Units

## Naming Conventions

### Standard Format
`[UnitName]_[Days]_[Type]_YYYYMMDD.extension`

**Components:**
- **UnitName**: Short descriptor, no spaces (use camelCase or underscores)
- **Days**: Day range covered (D1-6, D1-2, D3-4, D5-6, or single day D1)
- **Type**: Deliverable type (see below)
- **YYYYMMDD**: Date created (year-month-day for proper sorting)
- **extension**: .md, .pptx, .pdf, etc.

### Deliverable Type Codes

- **TeacherPlan** - Complete lesson plans
- **StudentPacket** - Student activity packet
- **AnswerKey** - Answer key with exemplars
- **Slides** - PowerPoint slide deck
- **ExitTicket** - Daily exit tickets (specify day: D1, D2, etc.)
- **CoverPage** - Unit overview cover page
- **Assessment** - Mini-assessment (for end-of-unit)
- **Rubric** - Scoring rubric or checklist

### Examples

**Full Units:**
```
ThemeAnalysis_D1-6_TeacherPlan_20250104.md
ThemeAnalysis_D1-6_StudentPacket_20250104.md
ThemeAnalysis_D1-6_AnswerKey_20250104.md
ThemeAnalysis_D1-6_Slides_20250104.pptx
```

**Partial/Daily Materials:**
```
ThemeAnalysis_D1_ExitTicket_20250104.md
ThemeAnalysis_D3-4_Organizer_20250104.md
ThemeAnalysis_D5-6_Assessment_20250104.md
```

**Special Materials:**
```
ThemeAnalysis_VocabList_20250104.md
ThemeAnalysis_BenchmarkCard_Reference.pdf
ThemeAnalysis_DistrictText_Original.pdf
```

## Folder Structure

### Recommended Organization

```
Teaching/
├── Units/
│   ├── Theme_StoryOfAnHour/
│   │   ├── 01-LessonPlans/
│   │   │   ├── StoryOfAnHour_D1-6_TeacherPlan_20250104.md
│   │   │   └── _archive/
│   │   │       └── StoryOfAnHour_D1-6_TeacherPlan_20241215.md
│   │   ├── 02-StudentPackets/
│   │   │   ├── StoryOfAnHour_D1-6_StudentPacket_20250104.md
│   │   │   └── _archive/
│   │   ├── 03-AnswerKeys/
│   │   │   └── StoryOfAnHour_D1-6_AnswerKey_20250104.md
│   │   ├── 04-SlideDecks/
│   │   │   └── StoryOfAnHour_D1-6_Slides_20250104.pptx
│   │   ├── 05-District-Files/
│   │   │   ├── original_text.pdf
│   │   │   └── district_organizer.pdf
│   │   └── _ChangeLog.txt
│   │
│   ├── CentralIdea_SpeechAnalysis/
│   │   └── [same structure]
│   │
│   └── Argument_DebateTexts/
│       └── [same structure]
│
├── Resources/
│   ├── Standards/
│   ├── BenchmarkCards/
│   └── KnowledgeBase/
│
└── _ToOrganize/
    └── [temporary holding area for new materials]
```

### Folder Purposes

- **01-LessonPlans** - All teacher-facing lesson plan documents
- **02-StudentPackets** - All student-facing packets and worksheets
- **03-AnswerKeys** - Answer keys, exemplars, rubrics
- **04-SlideDecks** - PowerPoint/Google Slides presentations
- **05-District-Files** - Original materials from district (read-only reference)
- **_archive/** - Old versions of files (one archive folder per deliverable type)
- **_ChangeLog.txt** - Record of all updates to unit

## Version Control

### Creating New Versions

When updating any deliverable:

1. **Create new file** with today's date
2. **Keep old file** - don't delete
3. **Move old file to _archive/** subfolder
4. **Update _ChangeLog.txt** with what changed

**Example:**
```
# Starting point
StoryOfAnHour_D1-6_StudentPacket_20250104.md

# After making edits on Jan 10
StoryOfAnHour_D1-6_StudentPacket_20250110.md  ← new version
_archive/StoryOfAnHour_D1-6_StudentPacket_20250104.md  ← archived
```

### Change Log Format

**File:** `_ChangeLog.txt` in root of unit folder

**Format:**
```
[Unit Name] - Change Log

=== 2025-01-10 ===
UPDATED: Student Packet
Changes:
- Added 5th row to theme organizer (You Do independent)
- Expanded vocabulary practice with sentence writing

Files affected:
✓ StoryOfAnHour_D1-6_StudentPacket_20250110.md (NEW)
✓ StoryOfAnHour_D1-6_TeacherPlan_20250110.md (UPDATED - Day 4 procedures)
✓ StoryOfAnHour_D1-6_AnswerKey_20250110.md (UPDATED - added exemplar for row 5)
○ StoryOfAnHour_D1-6_Slides_20250104.pptx (NO CHANGE)
○ District files (NO CHANGE)

=== 2025-01-04 ===
CREATED: Initial unit build
Files created:
- Teacher Plan (6 days)
- Student Packet (6 days)
- Answer Key with exemplars
- Slide deck (Days 1-5)
- Exit tickets (Days 1-6)
- Cover page

Benchmark: ELA.10.R.1.2 - Theme
Text: "The Story of an Hour" by Kate Chopin
```

### Archive Management

**When to archive:**
- After creating updated version of existing file
- At end of school year (archive entire unit folder)
- When major revisions are made (keep old version as reference)

**Archive folder rules:**
- One `_archive/` folder per deliverable type subfolder
- Keep only the 2 most recent old versions (delete older)
- If file hasn't changed in 1+ years, consider deleting

**Example archive:**
```
02-StudentPackets/
├── StoryOfAnHour_D1-6_StudentPacket_20250110.md  ← CURRENT
└── _archive/
    ├── StoryOfAnHour_D1-6_StudentPacket_20250104.md  ← keep (most recent old)
    └── StoryOfAnHour_D1-6_StudentPacket_20241220.md  ← keep (2nd most recent)
    [DELETE older versions unless needed for reference]
```

## File Format Standards

### Editable Formats (Preferred)
- **Teaching documents:** .md (Markdown format)
- **PowerPoint slides:** .pptx (NOT .ppt or .pdf)
- **Excel trackers:** .xlsx (NOT .xls)

### Read-Only Formats
- **District materials:** Keep as received (often .pdf)
- **Final published versions:** Export to .pdf after completing edits

### Avoid
- **Google Docs links** - Download as .md instead
- **Pages/Keynote** - Export to .md/.pptx for compatibility
- **Scanned images** - Convert to editable text when possible

## Syncing and Alignment

### When Files Must Match

If you update ONE deliverable, check if others need updates:

**Student Packet updated** → Check:
- Lesson Plan (Independent rotation procedures)
- Answer Key (new questions/tasks need answers)
- Slides (student tasks shown on slides?)

**Lesson Plan updated** → Check:
- Student Packet (activities match what lesson plan says?)
- Answer Key (teacher script examples need answers?)

**Organizer structure changed** → Update:
- Lesson Plan (I Do/We Do/You Do scripts)
- Student Packet (organizer with scaffolds)
- Answer Key (completed exemplar organizer)
- Slides (organizer structure shown)

### Manual Synchronization Verification

After making updates, manually verify alignment across deliverables:
1. Check that vocabulary, organizer content, and examples match across lesson plan (.md), student packet (.md), and slides (.pptx)
2. Ensure all files have consistent dates (same day or same update date)
3. Review lesson plan procedures to confirm they match student packet activities
4. Verify answer keys reflect any changes made to student organizers or questions

## Sharing and Printing

### For Printing
- **Student packets:** Print 1 per student, stapled
- **Lesson plans:** Print or keep digital on teaching laptop
- **Answer keys:** Print 1 for teacher reference
- **Slides:** Present digitally, don't print

### For Sharing (with other teachers)
- Share entire unit folder (zip file)
- Include `_ChangeLog.txt` so they know version history
- Include district files in `05-District-Files/` for reference
- Don't share individual files without context

### For Submission (to admin/district)
- Create .pdf versions of final deliverables
- Name: `[UnitName]_[Type]_FINAL_YYYYMMDD.pdf`
- Don't share archived versions or change log

## Critical Rules

1. **NEVER delete old versions** without moving to archive first
2. **ALWAYS update _ChangeLog.txt** when making changes
3. **ALWAYS create dated versions** (never overwrite existing files)
4. **ALWAYS verify alignment** before reporting "complete"
5. **NEVER rename files** after creation (breaks file tracking)
6. **ALWAYS use consistent naming** (follow format exactly)
