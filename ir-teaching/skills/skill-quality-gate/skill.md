---
name: skill-quality-gate
description: >
  Quality checklist for IR teaching skills before deploying them to ~/.claude/skills/. Use when
  writing a new skill, editing an existing skill, or before syncing any skill to the live config.
  Checks frontmatter completeness, description specificity for auto-routing, structural completeness,
  non-duplication with existing skills, and skill-index/hooks currency.
---

# Skill Quality Gate

## Purpose

IR teaching skills direct Claude's behavior. A poorly written skill causes bad unit builds.
Run this before deploying any new or updated skill.

## Checklist

### 1. Frontmatter

- [ ] `name:` field is present and matches the folder name
- [ ] `description:` is specific enough that Claude's auto-routing would trigger correctly
  - BAD: "Use when building units"
  - GOOD: "Use when building full 6-day IR units after menu-mode-planner collects preferences. Produces TeacherPlan, StudentPacket, AnswerKey, FeedbackForm."
- [ ] Description includes trigger phrases and exclusion phrases ("Use when X. Do NOT use when Y.")

### 2. Structure

- [ ] Has "When to Use" section
- [ ] Has "When NOT to Use" section (prevents skill from being invoked in wrong context)
- [ ] Has a clear process or step-by-step section
- [ ] Has at least one example of correct output or behavior
- [ ] Does NOT have vague instructions like "handle appropriately" or "address as needed"

### 3. Non-Duplication

- [ ] Check existing skills in `skill-index` — does this overlap with an existing skill?
- [ ] If overlap exists: either merge into existing skill or clearly differentiate scope
- [ ] No contradictions with existing skills (e.g., two skills with different rules for the same situation)

### 4. Routing Currency

- [ ] `skill-index/SKILL.md` updated to include this skill in the routing table
- [ ] `hooks/hooks.json` updated if this skill has new trigger phrases
- [ ] If this skill is DEPRECATED: description updated with "DEPRECATED — use [X] instead"

### 5. Manual Test

- [ ] Invoke the skill and give it a realistic scenario
- [ ] Verify it produces the expected output (correct format, correct behavior)
- [ ] If it fails: identify where the instructions are ambiguous and fix them

## Reporting

**If all checks pass:**
```
SKILL QUALITY GATE: PASSED
[skill-name] is ready to sync to ~/.claude/skills/
```

**If any check fails:**
```
SKILL QUALITY GATE: FAILED
[skill-name] has issues:
- [2. Structure] Missing "When NOT to Use" section
- [4. Routing] skill-index not updated
Fix before syncing.
```
