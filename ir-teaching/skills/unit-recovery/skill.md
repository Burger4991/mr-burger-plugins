---
name: unit-recovery
description: MUST USE this skill when you need to restore a previous unit version. Trigger on: "restore the old version", "undo this revision", "get back the student packet from before", "previous version", "I want the old benchmark back", "rollback the unit"... Restore unit deliverables from _archive/ snapshots or git history, with options to restore all files or specific deliverables and automatic changelog logging.
---

# Unit Recovery

## Purpose

Restore a unit deliverable (or all deliverables) from a previous snapshot created by unit-reviser.

## When to Use

- "I need the old version of this unit"
- "The revision made things worse — restore it"
- "Get back the student packet from before the benchmark change"

## Step 1: Find the Unit Folder

Ask: "Which unit? Give me the text title and benchmark."

Then locate: `~/Documents/Teaching/Units/[UnitFolderName]/`

## Step 2: List Available Snapshots

Check `_archive/` folder inside the unit folder:

```bash
ls ~/Documents/Teaching/Units/[UnitFolderName]/_archive/
```

Display results to user:

```
Available snapshots for [Unit Name]:

1. 2026-03-07_pre-benchmark-change
   Files: TeacherPlan, StudentPacket, AnswerKey, FeedbackForm

2. 2026-03-05_pre-text-swap
   Files: TeacherPlan, StudentPacket, AnswerKey

Which snapshot do you want to restore from?
```

Also check git history if Teaching folder is a git repo:

```bash
git -C ~/Documents/Teaching log --oneline -- Units/[UnitFolderName]/
```

## Step 3: Confirm What to Restore

Ask: "Do you want to restore ALL files from that snapshot, or just specific ones?"

Options:
- All files (full rollback)
- Just the StudentPacket
- Just the TeacherPlan
- Just the AnswerKey

## Step 4: Restore

Copy files from archive back to unit folder:

```bash
cp ~/Documents/Teaching/Units/[UnitFolderName]/_archive/[snapshot-name]/[file].md \
   ~/Documents/Teaching/Units/[UnitFolderName]/[file].md
```

## Step 5: Log the Recovery

Append to `_ChangeLog.txt`:

```
[DATE] RECOVERY: restored [files] from [snapshot-name]
  Reason: [user's reason]
```

## Step 6: Git Commit (if Teaching folder is a git repo)

```bash
cd ~/Documents/Teaching
git add Units/[UnitFolderName]/
git commit -m "recover(unit): restore [files] from [snapshot] — [reason]"
```

## Step 7: Confirm

Tell the user exactly what was restored and what the current file state is.
