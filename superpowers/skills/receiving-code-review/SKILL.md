---
name: receiving-code-review
description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
---

# Receiving Code Review

## Core Content

**Overview:** Code review demands technical evaluation rather than emotional performance. The principle is: verify before implementing, ask before assuming, prioritize technical correctness over social comfort.

## The Response Pattern:
1. READ complete feedback without reacting
2. UNDERSTAND by restating requirements in your own words
3. VERIFY against actual codebase reality
4. EVALUATE whether it's technically sound for this specific codebase
5. RESPOND with technical acknowledgment or reasoned pushback
6. IMPLEMENT one item at a time, testing each

## Forbidden Responses:
- "You're absolutely right!" (violates core principles)
- "Great point!" or "Excellent feedback!" (performative)
- "Let me implement that now" (before verification)

**Instead:** Restate technical requirements, ask clarifying questions, push back with reasoning if needed, or just start working.

## Handling Unclear Feedback
Stop before implementing anything. Ask for clarification on unclear items, as they may be interdependent.

## Source-Specific Handling:

*From your human partner:* Implement after understanding, still ask if scope is unclear, avoid performative agreement, proceed to action.

*From External Reviewers:* Before implementing, verify technical correctness for THIS codebase, check for broken functionality, understand why current implementation exists, confirm cross-platform compatibility, assess context awareness.

## YAGNI Check
When reviewers suggest "implementing properly," grep the codebase for actual usage. If unused, question necessity.

## Implementation Order
Clarify unclear items first, then address blocking issues, simple fixes, then complex ones. Test individually and verify no regressions.

## When To Push Back
When suggestions break functionality, lack context, violate YAGNI, are technically incorrect, have legacy reasons, or conflict with architectural decisions. Use technical reasoning, ask specific questions, reference working code.

## Acknowledging Correct Feedback:
- ✅ "Fixed. [description]" or "Good catch - [issue]. Fixed in [location]."
- ❌ Never use gratitude expressions or "You're absolutely right!"

## Correcting Your Pushback
"You were right - I checked [X] and it does [Y]. Implementing now." Avoid apologies or over-explaining.

## Common Mistakes
Performative agreement, blind implementation, batch processing without testing, assuming reviewer correctness, avoiding pushback, partial implementation, proceeding without verification capability.

## Real Examples:
- Bad: Performative agreement to remove legacy code
- Good: Technical verification addressing backward compatibility concerns
- Good: YAGNI questioning about unused endpoints
- Good: Requesting clarification on ambiguous multi-item feedback

## GitHub Thread Replies
Use comment thread replies, not top-level PR comments.

## Bottom Line
External feedback represents suggestions to evaluate, not mandates to follow. Verify, question, then implement—never performative agreement.
