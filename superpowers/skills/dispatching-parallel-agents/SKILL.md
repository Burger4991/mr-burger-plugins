---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
---

# Dispatching Parallel Agents

## Overview
The skill teaches delegating tasks to specialized agents with isolated context. The core principle: "Dispatch one agent per independent problem domain. Let them work concurrently." This approach addresses situations where multiple unrelated failures exist across different test files, subsystems, or bugs—sequential investigation wastes time when work can happen in parallel.

## When to Use
**Use when:**
- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- Each problem can be understood without context from others
- No shared state between investigations

**Don't use when:**
- Failures are related
- Need to understand full system state
- Agents would interfere with each other

## The Pattern (4 Steps)

**1. Identify Independent Domains** - Group failures by what's broken (e.g., tool approval flow, batch completion behavior, abort functionality)

**2. Create Focused Agent Tasks** - Each agent receives specific scope, clear goal, constraints, and expected output format

**3. Dispatch in Parallel** - Multiple Task() calls execute concurrently rather than sequentially

**4. Review and Integrate** - Read summaries, verify no conflicts, run full test suite, integrate changes

## Agent Prompt Structure
Effective prompts are focused on one problem domain, self-contained with all necessary context, and specific about required output.

## Common Mistakes
- Too broad scope vs. specific, focused assignments
- Missing context vs. including error messages and test names
- No constraints vs. explicit boundaries
- Vague output vs. requesting summaries of findings

## Real Example from Session
A debugging scenario with 6 test failures across 3 files resulted in 3 parallel agents fixing timing issues, event structure bugs, and async execution problems with zero conflicts.

## Key Benefits
1. Parallelization - simultaneous investigations
2. Focus - narrow scope reduces cognitive load
3. Independence - no agent interference
4. Speed - solve multiple problems concurrently

## Verification Steps
Review summaries, check for code conflicts, run comprehensive tests, spot-check for systematic errors.
