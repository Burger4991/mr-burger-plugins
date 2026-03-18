---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
---

# Finishing a Development Branch

## Overview

The skill guides developers through completing work by verifying tests, presenting clear options, and executing the chosen workflow.

**Core principle:** "Verify tests → Present options → Execute choice → Clean up"

**Opening announcement:** "I'm using the finishing-a-development-branch skill to complete this work."

## The Process

### Step 1: Verify Tests

Before offering options, run the project's test suite:
```bash
npm test / cargo test / pytest / go test ./...
```

If tests fail, display failures and block progression. If tests pass, continue to Step 2.

### Step 2: Determine Base Branch

Identify the base branch using:
```bash
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

Or ask for confirmation directly.

### Step 3: Present Options

Present exactly 4 options without additional explanation:

1. Merge back to base-branch locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

### Step 4: Execute Choice

**Option 1** (Merge Locally): Switch to base, pull latest, merge feature branch, verify tests, delete branch locally.

**Option 2** (Push & PR): Push branch upstream and create PR with summary and test plan sections.

**Option 3** (Keep As-Is): Report branch preservation without cleanup.

**Option 4** (Discard): Require typed "discard" confirmation, then delete branch.

### Step 5: Cleanup Worktree

For Options 1, 2, and 4: Remove worktree if applicable using `git worktree remove`.

For Option 3: Preserve worktree.

## Quick Reference Table

| Option | Merge | Push | Keep Worktree | Cleanup |
|--------|-------|------|---------------|---------|
| 1. Merge locally | ✓ | — | — | ✓ |
| 2. Create PR | — | ✓ | ✓ | — |
| 3. Keep as-is | — | — | ✓ | — |
| 4. Discard | — | — | — | ✓ (force) |

## Common Mistakes & Red Flags

**Never proceed** with failing tests, merge without re-verifying, delete without confirmation, or force-push without explicit request.

**Always verify** tests, present 4 options, obtain typed confirmation for discard, and only cleanup worktrees for Options 1 & 4.

## Integration

Called by: subagent-driven-development (Step 7) and executing-plans (Step 5)

Pairs with: using-git-worktrees skill
