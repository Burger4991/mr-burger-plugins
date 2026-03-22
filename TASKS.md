# TASKS — Post-Audit Remediation
*Created: 2026-03-22 | Source: audit + evaluation reports in `docs/audits/`*
*Plan: `docs/plans/2026-03-22-post-audit-remediation-plan.md`*

## Quick Wins

### ~~1. Clean FUSE artifacts~~ ✓ DONE
- [x] Already clean — 0 FUSE artifacts found anywhere in `~/.claude/`

### ~~2. Fix collaborative-protocols naming~~ ✓ DONE
- [x] Renamed `SKILL.md` → `skill.md` in `ir-teaching/skills/collaborative-protocols/` (commit d5fcdd4)

### ~~3. Create ear-training knowledge file~~ ✓ DONE
- [x] Removed broken symlink, created directory structure, wrote `Ear-Training-Protocol.md`
- Content: 5 outlines, 3 levels (sing-then-play / sing-with-chord / full-audiation), instrument adaptations, practice sequence, key progression, intervals reference

### ~~4. Populate band-materials knowledge file~~ ✓ DONE
- [x] Already populated — `knowledge/band/beginning-band-essentials.md` is 400+ lines with fingering charts, warm-up sequences, chorale content, rhythm curriculum, and 12-week lesson sequence.

## Standardization

### ~~5. Standardize plugin.json convention~~ ✓ DONE
- [x] Added explicit `skills`, `agents`, `commands` arrays to all 4 plugins:
  - `ir-teaching` — 61 skills, 11 agents
  - `ir-data-pipeline` — 9 skills, 2 agents
  - `ir-classroom-ops` — 6 skills
  - `mr-burger-workflow` — 7 skills, 1 agent, 11 commands

### ~~6. Decide on GWS plugin~~ ✓ DONE
- [x] `~/.agents/skills/` no longer exists — GWS plugin was already removed.

## Hardening

### 7. Build runtime smoke tests
- [ ] Create top-level `eval/` directory for cross-plugin smoke tests
- [ ] Write generalized rubric (adapt from `mr-burger-music/eval/rubric.md`)
- [ ] Write test cases: 2 per plugin (10 total across 5 plugins)
- [ ] Write eval subagent prompt (`eval/smoke-test-eval.md`)
- **Why:** Audit verified existence only. Component evaluation verified instruction quality. Neither confirmed runtime behavior.
- **Pattern:** Existing `mr-burger-music/eval/` framework (rubric + test cases + subagent + results dir)
- **Test skills:**
  - ir-teaching: `bellringer-builder`, `benchmarks`
  - ir-data-pipeline: `data-quality-checker`, `growth-analyzer`
  - ir-classroom-ops: `observation-prep`, `sub-folder-builder`
  - mr-burger-music: `band-materials`, `score-transformer`
  - mr-burger-workflow: `work-logger`, `plugin-registry`

### 8. Expand regression suite
- [ ] Create `eval/regression/` with workflow definitions
- [ ] Document 10 canonical multi-skill workflows with expected behavior
- [ ] Write regression eval subagent prompt
- **Why:** Audit Phase 5 tested only 3 workflows. 90 skills + 16 agents need broader coverage.
- **Workflows:**
  1. IR Unit Build: unit-planner → unit-builder-protocol → quality-reviewer
  2. Student Data Pipeline: student-data-processor → data-quality-checker → growth-analyzer → report-builder
  3. Bellringer Generation: bellringer-builder → vocabulary-instruction → mc-question-generation
  4. Observation Prep: observation-prep → ir-framework → esol-core
  5. Sub Plan: sub-folder-builder → sub-plan-generator agent
  6. Data Analysis: data-analyst agent (orchestrates 9 skills)
  7. Music Practice: music-coach agent → practice-planner → session-logger
  8. Session Lifecycle: workflow-agent OPEN → [work] → /wrap → workflow-agent CLOSE
  9. Capture Flow: /capture → work-logger → TASKS.md
  10. Score Transformation: score-transformer → score-writer agent
