---
name: brainstorming
description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
---

# Brainstorming Skill - Complete Content

## Brainstorming Ideas Into Designs

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

Start by understanding the current project context, then ask questions one at a time to refine the idea. Once you understand what you're building, present the design and get user approval.

**Critical constraint:** "Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it."

## Anti-Pattern: "This Is Too Simple To Need A Design"

Every project requires this process. Simple projects are where unexamined assumptions waste the most effort. Designs can be brief for truly simple projects, but presentation and approval are mandatory.

## Checklist

Nine sequential tasks required:

1. Explore project context via files, documentation, recent commits
2. Offer visual companion (separate message only)
3. Ask clarifying questions one-by-one
4. Propose 2-3 approaches with trade-offs
5. Present design in complexity-scaled sections
6. Write design doc to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
7. Execute spec review loop via subagent
8. Request user review of written spec
9. Invoke writing-plans skill for implementation

## Process Flow

Flowchart showing:
- Context exploration → Visual decision → Companion offering (if needed) → Clarifying questions → Approach proposals → Design presentation → User approval loop → Design documentation → Spec review → User review → Writing-plans invocation

**Terminal state requirement:** "The ONLY skill you invoke after brainstorming is writing-plans."

## The Process

**Understanding:**
- Assess scope early; decompose multi-subsystem projects
- Ask one question per message
- Prefer multiple-choice when feasible
- Focus on purpose, constraints, success criteria

**Approaches:**
- Present 2-3 options with trade-offs
- Lead with recommendation and reasoning

**Design presentation:**
- Scale sections to complexity (few sentences to 300 words)
- Request approval after each section
- Cover architecture, components, data flow, error handling, testing

**Design principles:**
- Isolate units with single purposes
- Define clear interfaces
- Enable independent understanding and testing
- Improve existing code when it affects the work
- Avoid unrelated refactoring

## After the Design

**Documentation:**
- Write spec document
- Use available writing-clarity skills
- Commit to git

**Spec review loop:**
- Dispatch spec-document-reviewer subagent
- Fix issues and re-dispatch (max 3 iterations)
- Surface to human if exceeded

**User gate:**
- Request spec review before proceeding
- Process any requested changes through review loop

**Implementation:**
- Invoke writing-plans skill only

## Key Principles

- One question at a time
- Multiple-choice preferred
- YAGNI ruthlessly
- Explore alternatives
- Incremental validation
- Flexibility for clarification

## Visual Companion

Browser-based tool for mockups, diagrams, and visual options.

**Offering (standalone message):** "Some of what we're working on might be easier to explain if I can show it to you in a web browser...Want to try it?"

**Per-question decision:** Use browser for visual content (mockups, wireframes, diagrams); use terminal for text (requirements, tradeoffs, options).

Reference: `skills/brainstorming/visual-companion.md`
