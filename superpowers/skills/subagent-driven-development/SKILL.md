---
name: subagent-driven-development
description: Use when you have a written implementation plan and want each task executed by a dedicated subagent with review checkpoints
---

# Subagent-Driven Development

## Overview

Based on the GitHub repository content, this skill document outlines a methodology for executing implementation plans by dispatching specialized agents (subagents) to handle individual tasks within a single session.

## Core Concept

The document describes a process where: "Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration." Each task receives dedicated implementation, followed by sequential validation stages—first checking specification compliance, then evaluating code quality.

## Key Process Elements

**When to Apply:**
This approach suits scenarios with implementation plans containing mostly independent tasks that stay within the current session. It differs from parallel session execution ("Executing Plans") through its same-session focus and automatic review checkpoints.

**Subagent Workflow Per Task:**
1. Dispatch implementation subagent with complete task text and context
2. Handle questions or context requests before implementation
3. Receive completed work with self-review
4. Deploy spec compliance reviewer (separate subagent)
5. If issues found, implementer fixes and reviewer re-checks
6. Deploy code quality reviewer
7. Iterate until approval
8. Mark task complete

**Model Selection Strategy:**
The guidance recommends matching model capability to task complexity—mechanical implementation (1-2 files, clear specs) uses faster/cheaper models, while integration tasks and architectural decisions require more capable models.

**Status Handling:**
Implementers report four possible statuses: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED. Each requires distinct responses ranging from proceeding to review, addressing concerns, providing information, or escalating with task restructuring.

## Critical Requirements

The document emphasizes never: skipping either review stage, proceeding with unfixed issues, making subagents read plan files directly (provide extracted text instead), ignoring subagent questions, or conducting code quality review before spec compliance approval.

## Integration Dependencies

Required supporting skills include git worktree usage, plan writing, code review requests, and development branch completion. Subagents should apply test-driven development independently.
