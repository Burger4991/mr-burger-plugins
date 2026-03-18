---
name: unit-distribution
description: >
  Structured "ship it" workflow for a completed IR unit after the quality gate passes. Presents
  options: print for class, upload to OneDrive school folder, adapt for ESOL, archive as a reusable
  template, or share with department. Use after unit-quality-gate passes. Triggered by phrases like
  "ship it", "ready to print", "upload to OneDrive", "archive this unit".
---

# Unit Distribution

## Purpose

Once the quality gate passes, decide what to do with the unit. Don't just build it — ship it.

## When to Use

- After unit-quality-gate passes
- When you say "ready to print", "upload this", "archive for next year"
- After unit-reviser completes a revision and unit is ready again

## Options

Present these options using AskUserQuestion (multiSelect: true — can pick more than one):

**Option A: Print for Class**
- Which files to print: StudentPacket (class set), TeacherPlan (1 copy), FeedbackForm (class set)
- Print instructions:
  - StudentPacket: double-sided, stapled, 1 per student
  - TeacherPlan: single-sided (teacher reference)
  - FeedbackForm: single-sided, 1 per student

**Option B: Upload to OneDrive**
- Target folder: `OneDrive > MDCPS > Teaching > Units > [Unit Folder Name]`
- Upload all 4 core .md files
- Naming convention: already correct if unit-builder-protocol was used

**Option C: Adapt for ESOL**
- Route to esol-adapter agent: "Adapt [unit name] StudentPacket for Level [1-5] ESOL students"
- Specify which levels are in your class
- esol-adapter produces modified StudentPacket with additional scaffolds

**Option D: Archive as Template**
- Copy unit folder to: `~/Documents/Teaching/Templates/`
- Rename files: remove date suffix, add `_TEMPLATE`
  - Example: `StoryOfAnHour_StudentPacket_TEMPLATE.md`
- Add entry to `~/Documents/Teaching/Templates/_index.txt`:
  ```
  [Date] [Unit Name] — [Benchmark] — [Text Title]
  Folder: Templates/[UnitFolderName]/
  Notes: [any special features of this unit]
  ```

**Option E: Share with Department**
- Export as PDF for sharing (keep .md for yourself)
- Files to share: StudentPacket + AnswerKey (not TeacherPlan — keep internal)
- Save PDFs to: `~/Documents/Teaching/Shared/`

## After Selection

Provide specific step-by-step instructions for each chosen option. Do not just say "upload it" —
give the exact path, the exact steps, and confirm when done.

If Option C (ESOL adapt) is chosen: route to esol-adapter agent immediately.
