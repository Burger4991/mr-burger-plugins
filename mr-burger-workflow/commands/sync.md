---
description: Push recent work into the right places across all plugins
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /sync

Sync recently completed work across the plugin ecosystem into the Second Brain system by executing the following steps exactly.

## Procedural Instructions

### Step 1: Detect Recent Work (Last 24 Hours)
1. Run: `find ~/Documents/Teaching/ -name "*.md" -mtime -1 2>/dev/null`
2. Run: `find ~/Documents/Teaching/ -name "*.docx" -mtime -1 2>/dev/null`
3. Run: `find ~/Desktop/SecondBrain/ -type f -mtime -1 2>/dev/null`
4. Collect all file paths returned. If no files found, stop here and report "No recent work detected in the last 24 hours."

### Step 2: Classify Each File
For each file found, determine its category:

- **Teaching work**: filename contains `unit`, `lesson-plan`, `lesson_plan`, `packet`, or is in `~/Documents/Teaching/` (excluding logs/)
- **Data work**: filename contains `analysis`, `report`, `growth`, `intervention`, `FAST`, `NWEA`, `data`, or is in `~/Documents/Teaching/data/`
- **Logs**: file is in `~/Documents/Teaching/logs/` → Skip (already logged)
- **Sub plan**: filename contains `sub-plan` or `sub_plan`
- **Tasks**: file is `TASKS.md` or is in `~/Desktop/SecondBrain/` → Check if it was manually edited
- **Other**: any file not categorized above

Create a list: `[category] → [filename]`

### Step 3: Update TASKS.md
1. Read `~/Desktop/SecondBrain/TASKS.md`
2. For each classified piece of work (Teaching, Data, Sub plan):
   - Search the file for keywords from the filename (e.g., if file is "unit-3-lesson-plan.md", search for "unit 3" or "unit-3")
   - If entry exists and is in `## Active` → Move it to `## Done` with today's date: `- [x] [description] (completed YYYY-MM-DD)`
   - If entry doesn't exist → Add to `## Done`: `- [x] [Brief description of work] (completed YYYY-MM-DD)`
   - Do not modify entries already in `## Done`
3. Write the updated file back to `~/Desktop/SecondBrain/TASKS.md`

### Step 4: Create/Update Journal Entry
1. Get today's date in YYYY-MM-DD format
2. Check if `~/Desktop/SecondBrain/journal/YYYY-MM-DD.md` exists
3. If not, create it with header: `# Journal — [date]`
4. Append a new section:
   ```
   ## Work Completed
   - [item 1 with category tag, e.g., "[Teaching] Completed unit 3 lesson plan"]
   - [item 2]
   - [item 3]
   ```
5. If the file already has `## Work Completed`, append items to the existing list

### Step 5: Extract Action Items from Data Work
1. For each file classified as "Data work":
   - Read the file
   - Search for keywords: "needs intervention", "at risk", "schedule conference", "Tier 2", "Tier 3", "follow-up needed", "action item"
   - If any keywords found, extract the full sentence/context
2. Present to user:
   ```
   Found action items in [filename]:
   - [action item 1]
   - [action item 2]

   Should I add these to TASKS.md under Active? (yes/no)
   ```
3. Wait for user confirmation
4. If yes, add each as a new active item in TASKS.md: `- [ ] [action item description]`
5. Write updated TASKS.md

### Step 6: Sync to Notion (If Available)
1. Check if `notion-sync` skill is available by running: `skills available | grep -i notion`
2. If available:
   - Use `notion-sync` skill to push task updates to Notion
   - Note success in summary
3. If not available:
   - Note in summary: "Notion sync skipped — connector not available"

### Step 7: Report Summary
Output exactly:

```
## Sync Complete — [YYYY-MM-DD]

**Work Synced:**
- [X] Teaching items → TASKS.md
- [X] Data items → TASKS.md + journal
- [X] Action items extracted (yes/no)
- [X] Journal entry created

**Details:**
- [count] teaching file(s) logged
- [count] data file(s) logged
- [count] action item(s) added (if applicable)
- Notion: [synced / skipped — connector unavailable]

**Next Actions:**
[If action items were added, list them. Otherwise: "None — all work logged."]
```

---

## Error Handling

- If `find` returns no files: "No recent work detected in the last 24 hours."
- If TASKS.md doesn't exist: "TASKS.md not found. Please set up ~/Desktop/SecondBrain/TASKS.md first."
- If journal directory doesn't exist: Create `~/Desktop/SecondBrain/journal/` before writing
- If a file can't be read: Skip it and continue with others

---

## Important Notes

- Always read files before overwriting
- Do not sync trivial work (quick questions, one-off lookups, test files)
- Preserve exact formatting when editing TASKS.md and journal files
- Use consistent area tags: [Teaching], [Career], [Music], [Dog Training], [Personal], [Tech]
