---
name: benchmarks
description: >
  Routing hub and cross-benchmark reference for all 10 Florida BEST ELA 10th grade reading standards.
  Use this skill when the user needs to COMPARE multiple benchmarks, see ALL benchmarks at once,
  or when you need to route to the correct standalone benchmark skill by code or topic.
  For a SINGLE specific benchmark (e.g., "tell me about R.1.2" or "theme achievement levels"),
  prefer the standalone benchmark-* skill instead (benchmark-theme, benchmark-argument, etc.).
  This skill routes to: R.1.1 Literary Elements, R.1.2 Theme, R.1.3 Point of View,
  R.1.4 Poetry, R.2.1 Text Structure, R.2.2 Central Idea, R.2.3 Purpose & Perspective,
  R.2.4 Argument, R.3.1 Figurative Language, R.3.4 Rhetoric.
  Use when comparing benchmarks, viewing the full benchmark map, or when unsure which
  specific benchmark applies to a user's request.
---

# Florida BEST ELA Benchmarks — 10th Grade

## How to Use

This skill serves as a **routing table and quick-reference hub**. Each benchmark also has a standalone skill (`benchmark-argument`, `benchmark-theme`, etc.) that can be triggered directly. The `standards/` sub-directory mirrors their content for consolidated access.

When a user mentions a benchmark code (e.g., ELA.10.R.1.2) or topic (e.g., "theme"), either load the corresponding guide from `standards/` OR trigger the standalone `benchmark-*` skill directly. Each guide contains the full standard, clarifications, analytical process, organizer structures, question stems, achievement levels, ESOL scaffolds, mini-lessons, and feedback checkpoints.

## Benchmark Routing Table

| Code | Topic | File | Standalone Skill |
|------|-------|------|-----------------|
| ELA.10.R.1.1 | Literary Elements (character, setting, plot) | `standards/literary-elements.md` | `benchmark-literary-elements` |
| ELA.10.R.1.2 | Theme (universal themes, theme development) | `standards/theme.md` | `benchmark-theme` |
| ELA.10.R.1.3 | Coming of Age & Conflicting Perspectives (perspective transformation) | `standards/point-of-view.md` | `benchmark-point-of-view` |
| ELA.10.R.1.4 | Layers of Meaning & Ambiguity in Poetry (multiple meanings, unresolved ideas) | `standards/poetry.md` | `benchmark-poetry` |
| ELA.10.R.2.1 | Text Structure & Features (organizational patterns) | `standards/text-structure.md` | `benchmark-text-structure` |
| ELA.10.R.2.2 | Central Idea (informational texts) | `standards/central-idea.md` | `benchmark-central-idea` |
| ELA.10.R.2.3 | Purpose & Perspective (author's purpose, historical) | `standards/purpose-perspective.md` | `benchmark-purpose-perspective` |
| ELA.10.R.2.4 | Argument (claims, evidence, reasoning) | `standards/argument.md` | `benchmark-argument` |
| ELA.10.R.3.1 | Figurative Language & Mood (metaphor, simile, mood) | `standards/figurative-language.md` | `benchmark-figurative-language` |
| ELA.10.R.3.4 | Understanding Rhetoric (appeals, devices) | `standards/rhetoric.md` | `benchmark-rhetoric` |

## Quick Reference

For a high-level overview of all benchmarks and Planning Card question stems, see `reference-guide.md` in this directory.

## Standard Guide Format

Every benchmark guide follows this structure:

1. **Standard** — Official benchmark statement
2. **Benchmark Clarifications** — What students must do, key terminology, common misconceptions
3. **Prerequisite Skills & Common Gaps** — What to remediate before teaching
4. **Analytical Process** — 4-6 step sequence for students to follow
5. **Sample Organizer Structures** — 2-3 organizer options with I Do / We Do / You Do rows
6. **Question Stems** — From Planning Cards, categorized by type
7. **Achievement Level Descriptors** — Levels 2-5 with specific criteria
8. **Assessment Limits** — What's appropriate and not appropriate to test
9. **Common Vocabulary** — Academic terms students need
10. **Sample I Do Row** — Fully worked teacher model
11. **ESOL Scaffolds** — Sentence frames, vocabulary support, Think-Pair-Share
12. **Prerequisite Mini-Lessons** — Daily remediation focus areas
13. **Integration with Other Skills** — Cross-references
14. **Quick Reference** — One-page summary
15. **Feedback Checkpoints** — Day 4 organizer and Day 6 ACE response criteria

## Usage Examples

**User says:** "Build a unit for benchmark ELA.10.R.1.2"
→ Load `standards/theme.md` for the full theme guide

**User says:** "I need an organizer for figurative language"
→ Load `standards/figurative-language.md`, go to Sample Organizer Structures section

**User says:** "What are the achievement levels for rhetoric?"
→ Load `standards/rhetoric.md`, go to Achievement Level Descriptors section

**User says:** "Show me all the benchmarks"
→ Load `reference-guide.md` for the overview

## Output Specification

When a benchmark is requested, Claude should:

1. **Locate the full standard guide** from the `standards/` subdirectory using the benchmark code or topic name
2. **Load the complete guide** which contains 15 sections:
   - Standard (official benchmark statement)
   - Clarifications (what students must do, key terminology, misconceptions)
   - Analytical Process (4-6 step sequence)
   - Organizer Structures (2-3 options with I Do/We Do/You Do rows)
   - Question Stems (Planning Card stems by type)
   - Achievement Levels (Levels 2-5 descriptors)
   - Assessment Limits (what's appropriate to test)
   - Vocabulary (academic terms students need)
   - Sample I Do Row (fully worked teacher model)
   - ESOL Scaffolds (sentence frames, vocabulary support)
   - Prerequisite Mini-Lessons (daily remediation)
   - Integration with Other Skills (cross-references)
   - Quick Reference (one-page summary)
   - Feedback Checkpoints (Day 4 organizer and Day 6 ACE response criteria)

3. **Use the full guide** to inform unit planning, assessment design, and organizer creation—not just excerpts
4. **Provide context** about how the benchmark fits into the reading standards (Reading: R.1, R.2, R.3; Vocabulary: V.1)

## Error Handling

**Invalid benchmark code provided:**
- List the valid benchmark codes from the routing table
- Ask which benchmark the user meant
- Offer to search by topic name if code is unclear

**Benchmark not in 10th grade ELA set:**
- Explain: "This skill covers ELA.10.R and ELA.10.V benchmarks only"
- Offer alternative benchmarks that might address similar skills
- Ask if user wants to search in a different grade level

**Topic name without code (e.g., "theme"):**
- Match the topic to the appropriate standard file
- Example: "theme" → ELA.10.R.1.2 → `standards/theme.md`
- Provide the full guide automatically

## Related Skills

- `ir-framework` — 6-day cycle structure these benchmarks fit into
- `organizer-design` — Design principles for the organizers referenced in each guide
- `unit-builder-protocol` — Full unit build process that uses these benchmarks
- `cer-writing-guide` — CER writing framework used in Day 5-6 assessments
- `gradual-release-scripts` — Teacher talk scripts for the I Do / We Do / You Do phases
- `feedback-checkpoint-builder` — Generates benchmark-specific feedback checklists
