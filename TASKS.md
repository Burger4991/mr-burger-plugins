# TASKS — Post-Audit Remediation
*Created: 2026-03-22 | Source: audit + evaluation reports in `docs/audits/`*
*Plan: `docs/plans/2026-03-22-post-audit-remediation-plan.md`*

## Quick Wins

### 1. Clean FUSE artifacts
- [ ] Delete `~/.claude/commands/.fuse_hidden*` (183 files)
- [ ] Delete `~/.claude/skills/.fuse_hidden*` (10 files)
- **Why:** Flagged in audit Phase 1, left unresolved in Phase 4. Harmless but adds noise to future audits and `ls` output.
- **How:** `find ~/.claude/commands -name '.fuse_hidden*' -delete && find ~/.claude/skills -name '.fuse_hidden*' -delete`
- **Verify:** `find ~/.claude -name '.fuse_hidden*' | wc -l` should return 0

### 2. Fix collaborative-protocols naming
- [ ] Rename `SKILL.md` → `skill.md` in `ir-teaching/skills/collaborative-protocols/`
- **Why:** File exists but uses uppercase `SKILL.md` while every other skill in the repo uses lowercase `skill.md`. This caused the component evaluation to fail reading it.
- **How:** `mv ir-teaching/skills/collaborative-protocols/SKILL.md ir-teaching/skills/collaborative-protocols/skill.md`
- **Verify:** `head -5 ir-teaching/skills/collaborative-protocols/skill.md`

### 3. Create ear-training knowledge file
- [ ] Remove broken symlink: `rm mr-burger-music/knowledge/linear-harmony-system`
- [ ] Create directory structure: `mkdir -p mr-burger-music/knowledge/linear-harmony-system/04-Reference`
- [ ] Write `Ear-Training-Protocol.md` with LHS ear training protocol content
- **Why:** `knowledge/linear-harmony-system` is a broken symlink → `/Users/alexanderburger/Documents/Music/Practice/Linear Harmony System` (macOS path). The `ear-training` skill references `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` and falls back to general knowledge when missing.
- **Content needed:** Core rule, 3-level protocol, outline progressions, instrument adaptations (trumpet comeback / guitar beginner), success criteria, example exercises
- **Source:** The skill.md itself has the framework — the knowledge file should expand with specifics

### ~~4. Populate band-materials knowledge file~~ ✓ DONE
- [x] Already populated — `knowledge/band/beginning-band-essentials.md` is 400+ lines with fingering charts, warm-up sequences, chorale content, rhythm curriculum, and 12-week lesson sequence.

## Standardization

### 5. Standardize plugin.json convention
- [ ] Add explicit `skills`, `agents`, `commands` arrays to all 4 plugins that lack them (matching the mr-burger-music pattern)
- **Why:** Only mr-burger-music enumerates components. The other 4 rely on implicit directory discovery — works but inconsistent.
- **Affected files:**
  - `ir-teaching/.claude-plugin/plugin.json` — add skills (62), agents (11)
  - `ir-data-pipeline/.claude-plugin/plugin.json` — add skills (9), agents (2)
  - `ir-classroom-ops/.claude-plugin/plugin.json` — add skills (6)
  - `mr-burger-workflow/.claude-plugin/plugin.json` — add skills (7), agents (1), commands (11)

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
