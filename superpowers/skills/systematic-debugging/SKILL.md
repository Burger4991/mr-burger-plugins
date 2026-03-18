---
name: systematic-debugging
description: Use when debugging failing tests or broken functionality, before attempting fixes - requires root cause investigation in four phases: investigation, pattern analysis, hypothesis testing, and implementation
---

# Systematic Debugging

## Core Principle
The document emphasizes: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST" - a foundational rule that prohibits attempting solutions before completing Phase 1 investigation.

## The Four Phases Framework

**Phase 1: Root Cause Investigation** requires:
- Carefully reading error messages and stack traces
- Reproducing issues consistently with documented steps
- Checking recent code changes and dependencies
- Gathering diagnostic evidence in multi-component systems by logging data at component boundaries
- Tracing data flow backward through call stacks to find original triggers

**Phase 2: Pattern Analysis** involves:
- Locating similar working implementations in the codebase
- Thoroughly reviewing reference implementations without skimming
- Documenting every difference between working and broken code
- Understanding all dependencies and assumptions

**Phase 3: Hypothesis and Testing** requires:
- Stating theories explicitly with reasoning
- Making minimal, isolated changes to test each hypothesis
- Stopping and reformulating if tests fail rather than adding more fixes

**Phase 4: Implementation** means:
- Creating failing test cases before fixing
- Implementing single, focused solutions
- Verifying fixes resolved the actual issue
- Questioning architectural soundness if 3+ fix attempts fail

## Critical Red Flags

The document warns against common rationalizations like "quick fix for now," attempting multiple simultaneous changes, or skipping test creation. When 3+ fixes have failed, the guidance explicitly states to "STOP and question the architecture" rather than continuing symptom-based repairs.

## Real-World Impact

Systematic debugging reportedly achieves 15-30 minute resolution times versus 2-3 hours of "thrashing," with 95% first-time fix rates compared to 40% when guessing.
