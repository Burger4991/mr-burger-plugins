---
name: writing-skills
description: Use when creating new skills or modifying existing ones - applies test-driven development principles to skill documentation to ensure agents can find, understand, and apply skills correctly
---

# Writing Skills

This document is a comprehensive guide for creating and testing skills using Test-Driven Development (TDD) principles applied to documentation.

## Key Sections

**Overview & Core Concept**
Writing skills IS TDD for process documentation. The fundamental principle: "If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing."

## Skill Types
- Technique: Concrete methods with steps
- Pattern: Ways of thinking about problems
- Reference: API docs, syntax guides, tool documentation

## SKILL.md Structure
Frontmatter includes `name` and `description` fields (max 1024 chars total). The description should answer "when to use" without summarizing the skill's workflow. This prevents Claude from following the description instead of reading the full content.

## Claude Search Optimization (CSO)
Four critical elements:
1. Rich descriptions focused on triggering conditions
2. Keyword coverage matching error messages and symptoms
3. Descriptive, active naming (e.g., "condition-based-waiting" not "async-test-helpers")
4. Token efficiency—especially for frequently-loaded skills

## The Iron Law
"NO SKILL WITHOUT A FAILING TEST FIRST"—applies to new skills and edits. No exceptions for "simple additions" or "documentation updates."

## Testing Approach
Different skill types require different tests:
- Discipline-enforcing skills: pressure scenarios with combined stressors
- Technique skills: application and variation scenarios
- Pattern skills: recognition and counter-example scenarios
- Reference skills: retrieval and application testing

## Anti-Patterns & Common Mistakes
- Narrative examples (should be reusable, not one-off stories)
- Multi-language dilution
- Code in flowcharts
- Generic labels
- Untested deployments

## Directory Structure
Keep SKILL.md as the main file. Separate files only for heavy reference (100+ lines) or reusable tools.

## Flowchart Usage
Use flowcharts only for non-obvious decision points or process loops. Never for reference material, code examples, or linear instructions.
