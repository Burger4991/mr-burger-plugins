---
name: prompt-scaffold
description: Use when building a prompt for something not covered by an existing skill. Surfaces the 5-part framework (Identity, Task, Context, Constraints, Output Format) to structure any ad-hoc Claude request. Also covers chunking strategy for large or multi-step work.
---

# Prompt Scaffold

Use this when no existing skill fits — you need to prompt Claude directly and want the output to be useful on the first try.

## The 5-Part Framework

Every effective prompt has some combination of these five parts. You don't need all five every time — but knowing them tells you which one is missing when the output is off.

| Part | What it does | Example |
|------|-------------|---------|
| **Identity** | Tells Claude what role to fill — shapes vocabulary, depth, assumptions | "You are a 10th grade ELA teacher writing for MDCPS students." |
| **Task** | What needs to get done — action + scope + enough detail a stranger could start | "Write a 3-question exit ticket for ELA.10.R.1.2 (Theme) at DOK 2." |
| **Context** | Background Claude needs that it wouldn't know on its own — constraints, audience, prior decisions | "This is for a test prep day. Students have already read the passage twice." |
| **Constraints** | What to avoid — saves editing time, prevents known failure modes | "No bullet points. No jargon. Keep total length under one page." |
| **Output Format** | The shape of the answer — list, table, draft with placeholders, options to choose from | "Give me 3 versions, each labeled, followed by a one-sentence rationale." |

## When to Use Which Parts

| If the task is... | Include... |
|-------------------|------------|
| Simple and quick (rename, fix a typo) | Task only |
| Creative (write, draft, design) | Identity + Task + Constraints + Output Format |
| Complex (build a system, analyze data) | All five |
| Ongoing project work | Identity + Context in your CLAUDE.md/CONTEXT.md. Task + Constraints in each prompt. |

## Chunking: One Prompt, One Thing

If your task is too big for one prompt, break it into steps. Each prompt asks for one clear thing.

**Too much at once:**
> "Write the full unit plan with lesson plans, student packet, and assessments for Shakuntala."

**Chunked:**
1. "Here's the text and benchmark. Draft the 6-day pacing overview."
2. [Review + adjust]
3. "Write Day 1 lesson plan using this pacing."
4. [Review + adjust]
5. "Generate the student packet for Days 1–2."

Each step builds on the last. If step 3 needs redoing, you only redo step 3.

## When NOT to use this

If a skill exists for the task, use the skill instead. Check `skill-index` or `benchmarks` first. This scaffold is for gaps — when no skill fits and you need to prompt directly.
