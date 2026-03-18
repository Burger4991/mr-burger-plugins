---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
---

# Requesting Code Review

The skill describes dispatching a "superpowers:code-reviewer subagent to catch issues before they cascade." The approach ensures reviewers receive focused context about the work product rather than session history, maintaining separation between review scope and developer context.

**Core principle stated:** "Review early, review often."

## When to Request Review

**Mandatory situations:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable times:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to Request

**Step 1 - Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**Step 2 - Dispatch code-reviewer subagent:**
Use Task tool with superpowers:code-reviewer type, fill template at `code-reviewer.md`

**Placeholders:**
- `{WHAT_WAS_IMPLEMENTED}` - What you just built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` - Starting commit
- `{HEAD_SHA}` - Ending commit
- `{DESCRIPTION}` - Brief summary

**Step 3 - Act on feedback:**
- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Example
The example workflow shows: completing Task 2, requesting review with specific git commits and implementation details, receiving feedback about architecture strengths and specific issues (missing progress indicators, magic number), then fixing flagged items before proceeding to Task 3.

## Integration with Workflows

**Subagent-Driven Development:** Review after each task; catch issues early; fix before next task

**Executing Plans:** Review after each batch (3 tasks); apply feedback; continue

**Ad-Hoc Development:** Review before merge; review when stuck

## Red Flags

**Never:**
- Skip review assuming simplicity
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue against valid technical feedback

**If reviewer is incorrect:**
- Push back with technical reasoning
- Show code/tests demonstrating it works
- Request clarification
