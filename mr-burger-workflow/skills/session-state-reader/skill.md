---
description: Read current project state hierarchy — PROJECT.md, TASKS.md, HANDOFF.md, plan files. Called by all workflow commands before acting.
---

# Session State Reader

A shared skill — not user-facing. Called internally by all workflow commands before they act: /resume, /capture, /wrap, /plan, /brainstorm-capture, /reflect, /skill-update, /daily.

## What to do

Read the following in order. Return a structured state block.

### 1. Find PROJECT.md
- Check current working directory for `PROJECT.md`
- If not found, walk up directories to `~/`
- If found, extract: project name, phase, resume_at point

### 2. Find TASKS.md
- Always at `~/Documents/TASKS.md`
- Extract active items only (lines under `## Active` that are unchecked `- [ ]`)
- Filter to current project if PROJECT.md found (match `[ProjectName]` tag)

### 3. Find HANDOFF.md
- Check current working directory only
- Note if it exists — don't read it (that's /resume's job)

### 4. Find plan file
- If PROJECT.md references a plan file path, note it
- Don't read it yet — just note the path

### 5. Find brainstorm doc
- Check `docs/brainstorm/` in current directory
- Note most recent file if present

## Output

Return this structured block (fill in what's found, use "none" for missing):

---
SESSION STATE
Project: [name] | none
Phase: [phase] | none
Resume at: [exact next step] | none
Active tasks: [comma-separated list filtered to project] | none
Handoff: exists | not found
Plan file: [path] | none
Brainstorm doc: [path] | none
---

## Notes
- If no PROJECT.md found anywhere: return all fields as "none"
- If multiple PROJECT.md files are found walking up the directory tree, use the one closest to the current working directory
- Never read HANDOFF.md — that's /resume's responsibility
- Never read the plan file — just surface the path
- This skill is fast — it reads metadata, not full file contents
