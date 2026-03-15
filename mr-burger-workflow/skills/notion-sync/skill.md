---
name: notion-sync
description: >
  This skill should be used when "syncing to Notion", "pushing tasks to Notion",
  or when any command needs to read or write Notion data. Requires the Notion
  MCP connector to be active.
version: 1.0.0
---

# Notion Sync Skill

## Overview

Notion is an optional integration point for Mr. Burger's productivity system. When available, it serves as a cloud-based mirror and dashboard for tasks, projects, and goals. This skill provides guidance on how to sync between the Second Brain (file-based system) and Notion, including availability checks, sync workflows, and data mapping.

## Important: Graceful Degradation

**The Second Brain (file-based system) is always the source of truth.** Notion is a convenience layer when the MCP connector is available.

- **If Notion is unavailable**: Fall back to file-based operations only and note "Notion sync skipped — connector not active" in the operation summary.
- **If Notion is available**: Sync bidirectionally to keep both systems in alignment.
- **Never block operations waiting for Notion**: If the Notion connector fails, the file-based system continues unaffected.

---

## Checking Notion Availability

Before any Notion operation, verify that Notion tools are accessible:

1. Attempt a simple test operation (e.g., `notion-search` for the task database)
2. If successful: Notion is available; proceed with sync operations
3. If failed or times out: Notion is unavailable; use file-based system only
4. **Always inform the user**: "Notion sync active" or "Notion sync skipped — connector not active"

**Example availability check**:
```
Try: notion-search query: "TASKS" (or similar)
If found: Notion available → proceed with syncing
If error: Notion unavailable → file-based only, note in output
```

---

## Notion Structure & Properties

### Task Database

Mr. Burger's primary Notion database is a unified **Task** database with the following properties:

| Property | Type | Values |
|----------|------|--------|
| **Title** | Text | Task description (e.g., "Grade PM2 data for Week 4") |
| **Area** | Select | Teaching, Career, Music, Dog Training, Personal, Tech |
| **Status** | Select | To Do, In Progress, Done |
| **Due Date** | Date | Optional deadline (YYYY-MM-DD format) |
| **Priority** | Select | Low, Medium, High, Urgent |
| **Tags** | Multi-Select | Optional: additional categorization (urgent, waiting, someday, etc.) |
| **Notes** | Text | Optional: additional context, links, details |
| **Completed Date** | Date | When marked Done (auto-populate or manual) |
| **Created Date** | Date | When the task was created (auto-populate) |

### Database View

The user typically works from views like:
- **This Week** (filtered Status ≠ Done, Area tags, sorted by Priority)
- **By Area** (filtered by each Area, shows all statuses)
- **Done** (filtered Status = Done, sorted by Completed Date descending)
- **Waiting** (filtered with "waiting" tag or Status = Waiting)

---

## Sync Workflows

### Workflow 1: Pushing Tasks from Second Brain to Notion

**When**: After `/capture` (add tasks), during `/plan` (add weekly priorities), or after `/review` (archive completed tasks)

**Steps**:

1. **Check Notion availability** → If unavailable, skip to file-based only
2. **Identify new/modified tasks** in TASKS.md (items without a Notion link or flagged as changed)
3. **For each new task**:
   - Extract: Title, Area tag, Status (from section: Active → To Do, Waiting → Waiting, Someday → someday tag)
   - Create page in Notion using `notion-create-pages` or equivalent
   - Add properties: Title, Area, Status, Tags (if applicable), Notes (if needed)
   - Optional: Link from TASKS.md to Notion page (e.g., comment with URL) for traceability
4. **Confirm**: "Synced N new tasks to Notion"

**Example**:
```
TASKS.md Active section:
- [ ] [Teaching] Grade PM2 data (due 2026-02-28)

→ Notion: Create task "Grade PM2 data"
   - Area: Teaching
   - Status: To Do
   - Due Date: 2026-02-28
   - Priority: High (inferred from due date)
```

### Workflow 2: Pulling Completed Tasks from Notion

**When**: During `/review` or periodic sync checks to ensure file system reflects Notion updates

**Steps**:

1. **Check Notion availability** → If unavailable, skip
2. **Query Notion**: `notion-search` or `notion-fetch` for tasks with Status = Done, filtered to recent (e.g., last 7 days)
3. **For each completed task in Notion**:
   - Find matching task in TASKS.md (by title or Notion link)
   - If not marked done in TASKS.md: update with `(completed YYYY-MM-DD)` and move to Done section
   - If already done: confirm and update Completed Date if needed
4. **Confirm**: "Synced N completed tasks from Notion to Second Brain"

**Example**:
```
Notion: "Submit 2 job applications" marked Done (Completed Date: 2026-02-20)

→ TASKS.md Done section:
   - [x] [Career] Submit 2 job applications (completed 2026-02-20)
```

### Workflow 3: Weekly Sync (During /plan)

**When**: Every `/plan` session (weekly planning)

**Steps**:

1. **Check Notion availability**
2. **Pull from Notion**: Fetch all tasks with Status = To Do or In Progress
3. **Merge with TASKS.md**:
   - Tasks in Notion but not TASKS.md → add to TASKS.md Active section
   - Tasks in TASKS.md but not Notion → create in Notion
   - Modified properties in Notion (Priority, Due Date) → update TASKS.md if different
4. **Push priorities**: Update Status and Priority in Notion for this week's focus from GOALS.md
5. **Confirm**: "Weekly sync complete: X tasks reviewed, Y changes synced"

### Workflow 4: End-of-Week Sync (During /review)

**When**: Every `/review` session (weekly review)

**Steps**:

1. **Check Notion availability**
2. **Pull completed tasks** from Notion (Workflow 2 above)
3. **Push archived tasks** to Notion (mark Done, set Completed Date)
4. **Update GOALS.md reflection** → Optional: create a linked page in Notion "Weekly Review" for visibility
5. **Confirm**: "Weekly review synced: X tasks completed, archived to Notion"

---

## Data Mapping: Second Brain ↔ Notion

| Second Brain | → | Notion | ← | Second Brain |
|--------------|---|--------|---|--------------|
| TASKS.md section | → | Status | ← | Notion Status property |
| Active | = | To Do | = | Active |
| Waiting | = | Waiting* | = | Waiting (tag or custom status) |
| Someday | = | someday tag | = | Items tagged "someday" |
| Done | = | Done | = | Done |
| [Area] tag | → | Area | ← | Notion Area property |
| Task due date (inline) | → | Due Date | ← | Notion Due Date property |
| ★ prefix (urgent) | → | Priority: High/Urgent | ← | Notion Priority property |
| Completion date (inline) | → | Completed Date | ← | Notion Completed Date property |

*Note: If Notion doesn't have a "Waiting" status, use a tag "waiting" or custom status.

---

## Availability-First Approach

### If Notion is Available:

```
/capture → Routes to files AND syncs to Notion
/plan → Reads files, pulls from Notion for sync, pushes updates
/review → Archives files and Notion, syncs both ways
/briefing → Optional: pulls from Notion dashboard if available for richer display
```

**User sees**: "Syncing to Notion... ✓ Done"

### If Notion is Unavailable:

```
/capture → Routes to files only
/plan → Reads files, no Notion operations
/review → Archives files only
/briefing → Reads files only
```

**User sees**: "Notion sync skipped — connector not active. Using file-based system."

**Retry logic**: On next command, automatically check Notion again. If it comes back online, full sync resumes.

---

## Common Notion Operations

### notion-search

Search for tasks by keyword, area, or status:

```
notion-search query: "Teaching" → returns all tasks with Area = Teaching
notion-search query: "Status = Done last week" → returns recent completed tasks
```

### notion-fetch

Fetch a specific page (task) by ID or URL:

```
notion-fetch page_id: [id] → returns full task details
```

### notion-create-pages

Create a new task (page) in the task database:

```
notion-create-pages
  database_id: [task-db-id]
  properties:
    Title: "Grade PM2 data"
    Area: "Teaching"
    Status: "To Do"
    Due Date: "2026-02-28"
    Priority: "High"
```

### notion-update-page

Update an existing task:

```
notion-update-page page_id: [id]
  properties:
    Status: "Done"
    Completed Date: "2026-02-20"
```

---

## Important Notes

### Connector Status

- **Currently**: Notion MCP connector is on hold (mentioned in CLAUDE.md as "connector issues")
- **Expectation**: May be re-integrated later; system gracefully handles offline state
- **User preference**: File-based system is sufficient until Notion reconnects

### Conflict Resolution

If Second Brain and Notion have conflicting data:

1. **File-based system wins** (it's the source of truth)
2. **Overwrite Notion** with file data during next sync
3. **Notify user**: "Conflict detected in task 'X' — file version used"
4. **Keep it simple**: If conflicts occur frequently, investigate why (manual edits in both systems?)

### Manual Edits

If the user edits tasks in both TASKS.md and Notion:

- Recommend: Edit primarily in TASKS.md, let sync push to Notion
- Or: Edit in Notion, let `/plan` or `/review` pull changes back
- Avoid: Simultaneous edits in both (causes conflicts)

### Notion Best Practices

For Mr. Burger:

- **Use Notion as a dashboard**: Read-heavy (checking progress, seeing week at a glance)
- **Edit in Second Brain**: Write primarily to files, sync pushes to Notion
- **Weekly syncs**: `/plan` and `/review` keep both systems aligned
- **Archive aggressively**: Completed tasks archived to Notion's "Done" view keeps active list clean

---

## Integration with Plugin Commands

- **`/capture`**: Detects Notion availability; if active, creates task page and returns Notion link
- **`/plan`**: Syncs GOALS.md focus with Notion task statuses and priorities; marks this week's focus in Notion
- **`/review`**: Pulls completed tasks from Notion; archives both files and Notion; creates reflection entry
- **`/briefing`**: Reads TASKS.md primarily; can pull from Notion dashboard if available for richer context

---

## Fallback Messaging

When Notion is unavailable, use these messages to keep the user informed:

- **During operations**: "Notion sync skipped — connector not active. Using file-based system only."
- **In summaries**: "Tasks saved to Second Brain. Notion sync will resume when the connector is available."
- **As a note**: "All operations completed successfully with file-based system. Notion will sync when ready."

**Goal**: User understands the system is working, just without the Notion layer, and knows it will resume automatically if Notion becomes available.

---

## Summary

**When Notion is available**: Seamless bidirectional sync, cloud dashboard, and additional context.

**When Notion is unavailable**: System degrades gracefully to file-based operations with no loss of functionality.

**Philosophy**: Simple, resilient, user-focused. Notion enhances but doesn't require the workflow.
