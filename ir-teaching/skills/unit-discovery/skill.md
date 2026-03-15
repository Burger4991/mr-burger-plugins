---
name: unit-discovery
description: >
  Optional pre-planning context gathering before menu-mode-planner. Reads district files, surfaces
  student data patterns, checks recent units to avoid repetition, and notes text complexity before
  planning decisions are made. Use when starting a unit with a district-provided text, when student
  data should inform planning, or when you want to avoid repeating texts/benchmarks from recent units.
  Feeds directly into menu-mode-planner as pre-loaded context.
---

# Unit Discovery

## Purpose

Gather context before planning so that menu-mode-planner choices are informed, not guessed.

## When to Use

- Starting a unit with a district-provided text or PDF
- You have PM/FAST data you want to factor into planning
- You want to check what you've taught recently to avoid repetition
- You're unsure which benchmark to target and want to check data first

## When NOT to Use

- You already know exactly what you want to build (skip straight to menu-mode-planner)
- You're doing a quick revision (skip straight to unit-reviser)

## Step 1: District Files

Ask: "Do you have any district-provided materials for this unit? (PDF, Word doc, benchmark guide)"

If yes: invoke `district-files-reader` skill to extract:
- Text passage (exact wording)
- Margin questions (preserve exact wording)
- Vocabulary words (if listed)
- Benchmark reference (if specified)
- Any district organizers

## Step 2: Student Data Check

Ask: "Do you have recent PM or FAST data I should factor in?"

If yes, ask for:
- Most recent PM scores by student (or class average)
- Which benchmarks showed the biggest gaps
- ESOL distribution (how many Level 1-5 students)

Summarize: "Based on your data, these benchmarks need the most attention: [list]. These ESOL levels are in your class: [levels]."

## Step 3: Recent Units Check

Ask: "What have you taught in the last 3-4 units? Benchmark and text title."

Check for:
- Benchmark repetition (avoid same benchmark back-to-back)
- Text genre repetition (alternate literary/informational)
- Vocabulary overlap (avoid reusing same tier-2 words)

Note: "You've recently taught [benchmarks]. Good options for next unit: [alternatives]."

## Step 4: Text Complexity Check

If a text has been identified, ask:
- "What's the approximate Lexile level of this text?" (if known)
- "Are there any content concerns (violence, mature themes) I should know about?"

## Step 5: Discovery Summary

Produce a one-page summary:

```
DISCOVERY SUMMARY
Unit: [Text Title] — [Benchmark if known]
Date: [today]

District Materials: [yes/no — files found: list]
Key findings: [margin questions, vocab, district organizer]

Student Data:
- PM average: [score]
- Benchmark gaps: [list]
- ESOL levels in class: [levels]

Recent Units:
- Last 3 benchmarks: [list]
- Recommendation: [which benchmark to target next]

Text:
- Lexile: [if known]
- Content flags: [if any]

Recommended starting point for menu-mode-planner:
- Benchmark: [recommendation]
- Text: [confirmed]
- ESOL modifications: [yes/no, levels]
```

## Step 6: Hand off to menu-mode-planner

Say: "Discovery complete. Here's what I found: [summary]. Ready to start planning? I'll open menu-mode-planner with this context pre-loaded."

Then invoke `menu-mode-planner` skill.
