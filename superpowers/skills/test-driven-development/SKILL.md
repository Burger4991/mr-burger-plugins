---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

## Core Principle
The document emphasizes: "Write the test first. Watch it fail. Write minimal code to pass." The foundational concept is that without observing a test fail initially, you cannot verify it actually tests the intended behavior.

## When to Use TDD
**Always apply to:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions** (requiring human partner approval):
- Throwaway prototypes
- Generated code
- Configuration files

## The Iron Law
"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"

Any code written before tests must be deleted entirely—not kept as reference, adapted, or reviewed. Implementation must be fresh from test specifications.

## Red-Green-Refactor Cycle

**RED Phase:** Write one minimal test demonstrating desired behavior using real code (not mocks unless unavoidable) with clear naming.

**Verify RED:** Run tests and confirm failure occurs for the right reason (missing feature, not syntax errors).

**GREEN Phase:** Write the simplest possible code satisfying the test without adding extra features or refactoring unrelated code.

**Verify GREEN:** Confirm the test passes, all other tests remain passing, and output shows no errors or warnings.

**REFACTOR Phase:** After achieving green, eliminate duplication, improve names, and extract helpers—maintaining all passing tests.

**Repeat:** Continue with the next failing test.

## Good Tests
Tests should be minimal (one behavior), clear (names describe behavior), and demonstrate desired API using actual implementation code.

## Why Order Matters
Testing after implementation produces immediately-passing tests proving nothing. The sequence matters because:
- Pre-written tests force discovery of edge cases before implementation
- Watching tests fail proves they measure something real
- Post-implementation testing verifies remembered cases, not all cases

## Common Rationalizations (All Invalid)
The document directly addresses excuses like "too simple to test," "manual testing sufficient," "deleting code is wasteful," and "TDD is dogmatic"—rejecting each with reasoning.

## Red Flags Requiring Restart
Indicators of skipped TDD include: code written before tests, tests added after implementation, immediately-passing tests, inability to explain test failures, and any rationalizations about "just this once."

## Practical Example: Bug Fix
Demonstrates complete cycle for empty email validation bug using test → fail verification → code → pass verification → refactor pattern.

## Verification Checklist
Before completion: every function has tests, each test was watched failing, minimal code was used, all tests pass, output is clean, real code is tested (minimal mocking), and edge cases are covered.

## Additional Guidance
When stuck, the document provides solutions: hard tests indicate unclear design; mocking everything suggests coupling issues; complex test setup requires interface simplification.
