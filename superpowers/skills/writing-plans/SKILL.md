---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code
---

# Writing Plans

## Overview Section
The skill instructs comprehensive implementation planning for engineers with minimal codebase context. Key guidance: document file touchpoints per task, provide complete code examples, emphasize bite-sized tasks following DRY, YAGNI, TDD principles with frequent commits.

**Opening announcement required:** "I'm using the writing-plans skill to create the implementation plan."

**Execution context:** Dedicated worktree (created via brainstorming skill)

**Default save location:** `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md` (user preferences override)

## Scope Check
Plans covering multiple independent subsystems should have been separated during brainstorming. If not, recommend splitting into individual subsystem plans, each producing independently testable, working software.

## File Structure Principles
- Design units with clear boundaries and single responsibilities
- Prefer smaller, focused files over large multifunctional ones
- Co-locate files that change together
- Follow established codebase patterns; avoid unilateral restructuring unless necessary
- Structure informs task decomposition; each task produces self-contained, independently meaningful changes

## Bite-Sized Task Granularity
Each step represents one 2-5 minute action:
- Write failing test
- Verify test failure
- Implement minimal passing code
- Verify test passage
- Commit changes

## Plan Document Header Template
```
# [Feature Name] Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement task-by-task.
> Steps use checkbox syntax for tracking.

**Goal:** [One-sentence description of what this builds]

**Architecture:** [2-3 sentences describing approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure Template
```
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Write the failing test**

[Python code block with test]

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

[Python code block]

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

[Bash commands for git add/commit]
```

## Remember Checklist
- Always use exact file paths
- Include complete code (not vague descriptions)
- Provide exact commands with expected outputs
- Reference related skills using @ syntax
- Apply DRY, YAGNI, TDD, frequent commits

## Plan Review Loop Process
1. Dispatch plan-document-reviewer subagent with plan and spec document paths (never session history)
2. If issues found: fix and re-dispatch reviewer for complete plan
3. If approved: proceed to execution handoff

**Loop guidance:**
- Original author fixes identified issues
- Escalate to human if loop exceeds 3 iterations
- Treat reviewer feedback as advisory; explain disagreements respectfully

## Execution Handoff Options
After plan completion and saving:

**Option 1: Subagent-Driven (Recommended)**
- REQUIRED SUB-SKILL: superpowers:subagent-driven-development
- Fresh subagent per task with inter-task reviews

**Option 2: Inline Execution**
- REQUIRED SUB-SKILL: superpowers:executing-plans
- Batch execution with checkpoint reviews
