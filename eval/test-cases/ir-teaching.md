# ir-teaching Smoke Test Cases

## Test Case 1: bellringer-builder

**Skill:** `ir-teaching/skills/bellringer-builder/skill.md`

**Prompt:** Create a Context Clue bellringer for the word "resilience" for a 10th grade
Intensive Reading class. This is Week 3 of a unit on informational text about overcoming
adversity. Students are mid-level readers (Level 2–3).

**Expected concept:** A 5-question multiple-choice bellringer using context clues to define
"resilience." STOP-style distractors. Answer key included. Scaffolding appropriate for
Level 2–3 readers.

**Key checks:**
- Uses Context Clue mode (not Word Parts or Benchmark Vocab)
- Exactly 5 MC questions with 4 answer choices each
- Distractors follow the STOP pattern (Surface-level, Too broad, Opposite, Partially correct)
- Answer key present with explanations
- ESOL modifications mentioned or included

---

## Test Case 2: benchmarks

**Skill:** `ir-teaching/skills/benchmarks/skill.md`

**Prompt:** Give me the full standard guide for ELA.10.R.2.1 (central idea and relevant details).

**Expected concept:** A structured 15-section standard guide for the Central Idea benchmark,
either generated inline or correctly routing to the `benchmark-central-idea` skill.

**Key checks:**
- Correctly identifies R.2.1 as Central Idea
- Routes to or produces the standard guide format (standard statement, clarifications,
  analytical process, organizers, question stems, achievement levels, vocabulary, feedback checkpoints)
- Grade 10 specific — not generic ELA
- Includes Florida BEST-specific language and clarifications
