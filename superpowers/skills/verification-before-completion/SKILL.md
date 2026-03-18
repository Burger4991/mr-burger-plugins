---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
---

# Verification Before Completion

## Overview
The document establishes that making completion claims without verification constitutes dishonesty rather than efficiency. The central tenet is "Evidence before claims, always," with the principle that violating the letter of this rule violates its spirit.

## The Iron Law
> "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"

This section mandates that you cannot claim something passes without having executed the verification command within the current context.

## The Gate Function
A five-step verification process:
1. Identify what command proves the claim
2. Execute the full command (fresh, complete)
3. Read full output, check exit code, count failures
4. Verify output confirms the claim
5. Only then make the claim

## Common Failures Table
Documents seven categories of insufficient verification methods, including relying on previous test runs, partial checks, agent reports, and code inspection alone.

## Red Flags
Eight warning signs indicating verification violations, including tentative language ("should," "probably"), expressing satisfaction prematurely, and approaching commits/PRs without verification.

## Rationalization Prevention
A table addressing eight common excuses with their actual reality, such as "Confidence ≠ evidence" and "Partial proves nothing."

## Key Patterns
Five domain-specific examples:
- **Tests**: Requires actual test command output showing pass counts
- **Regression tests**: Demands red-green cycle verification
- **Build**: Requires exit code confirmation
- **Requirements**: Needs line-by-line checklist verification
- **Agent delegation**: Demands independent verification of agent-reported success

## Why This Matters
References 24 failure memories, including trust erosion, shipped undefined functions, incomplete features, and wasted time.

## When To Apply
Always applies before any success/completion variations, satisfaction expressions, positive work statements, commits, or task transitions.

## The Bottom Line
"No shortcuts for verification. Run the command. Read the output. THEN claim the result. This is non-negotiable."
