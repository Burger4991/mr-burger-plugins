---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

"Announce at start: I'm using the executing-plans skill to implement this plan."

Note: Superpowers performs significantly better with subagent access. If available on your platform (Claude Code, Codex), use superpowers:subagent-driven-development instead.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically—identify questions or concerns about the plan
3. If concerns exist: Raise them with your human partner before proceeding
4. If no concerns: Create TodoWrite and continue

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan includes bite-sized steps)
3. Run specified verifications
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verification passes:
- "Announce: I'm using the finishing-a-development-branch skill to complete this work."
- Use superpowers:finishing-a-development-branch (required)
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

Stop immediately when encountering:
- Blockers (missing dependencies, test failures, unclear instructions)
- Critical plan gaps preventing startup
- Unclear instructions
- Repeated verification failures

"Ask for clarification rather than guessing."

## When to Revisit Earlier Steps

Return to Step 1 review when:
- Partner updates plan based on feedback
- Fundamental approach requires rethinking

"Don't force through blockers—stop and ask."

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan indicates
- Stop when blocked; don't guess
- Never start implementation on main/master without explicit user consent

## Integration

Required workflow skills:
- superpowers:using-git-worktrees (REQUIRED: isolated workspace setup)
- superpowers:writing-plans (creates the plan this skill executes)
- superpowers:finishing-a-development-branch (complete development after all tasks)
