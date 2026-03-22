# TASKS — Post-Audit Remediation
*Created: 2026-03-22 | Source: audit + evaluation reports in `docs/audits/`*

## Quick Wins

### 1. Clean FUSE artifacts
- [ ] Delete `~/.claude/commands/.fuse_hidden*` (183 files)
- [ ] Delete `~/.claude/skills/.fuse_hidden*` (10 files)
- **Why:** Flagged in audit Phase 1, left unresolved in Phase 4. Harmless but adds noise to future audits and `ls` output.
- **How:** `find ~/.claude/commands -name '.fuse_hidden*' -delete && find ~/.claude/skills -name '.fuse_hidden*' -delete`
- **Verify:** `find ~/.claude -name '.fuse_hidden*' | wc -l` should return 0

### 2. Verify collaborative-protocols
- [ ] Check `ir-teaching/skills/collaborative-protocols/` — confirm `skill.md` exists and is populated
- [ ] If orphan directory (no skill.md or stub only), remove it and re-run `setup.sh`
- **Why:** Component evaluation couldn't read this file. Either it's missing or misnamed.
- **How:** `cat ir-teaching/skills/collaborative-protocols/skill.md`

### 3. Populate ear-training knowledge file
- [ ] Write content for `mr-burger-music/knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md`
- **Why:** `ear-training` skill references this file but it's a stub. Skill degrades to general knowledge fallback.
- **Content needed:** Singing protocol steps, level progression (Level 1-3), instrument-specific adaptations (trumpet comeback, guitar beginner), success criteria per level
- **Source material:** The skill.md itself has the framework — the knowledge file should expand on it with specific exercises, intervals, and progressions

### 4. Populate band-materials knowledge file
- [ ] Write content for `mr-burger-music/knowledge/band/beginning-band-essentials.md`
- **Why:** `band-materials` skill references this for range constraints and exercise design. Currently a stub.
- **Content needed:** Bb trumpet range charts by level (Early Beginner/Beginner/Developing), fingering chart, common beginning band exercises, rhythm patterns by difficulty, key signature progression
- **Source material:** Band method books, existing range constraint table in skill.md (expand it)

## Standardization

### 5. Standardize plugin.json convention
- [ ] Decide: explicit enumeration (mr-burger-music pattern) vs. documented directory-discovery
- [ ] If enumeration: add `skills`, `agents`, `commands` arrays to all 4 other plugin.json files
- [ ] If directory-discovery: add a note to CLAUDE.md documenting this as the canonical convention
- **Why:** Only mr-burger-music enumerates components. The other 4 rely on directory discovery — works but is implicit and inconsistent.
- **Affected files:**
  - `ir-teaching/.claude-plugin/plugin.json` (needs: 61 skills, 11 agents)
  - `ir-data-pipeline/.claude-plugin/plugin.json` (needs: 9 skills, 2 agents)
  - `ir-classroom-ops/.claude-plugin/plugin.json` (needs: 6 skills)
  - `mr-burger-workflow/.claude-plugin/plugin.json` (needs: 7 skills, 1 agent, 11 commands)

### 6. Decide on GWS plugin
- [ ] Inspect `~/.agents/skills/` — verify 92 Google Workspace skills are still there
- [ ] Decide: integrate into mr-burger-plugins, move to a separate repo, or delete
- **Why:** Orphaned at `~/.agents/skills/` since the audit. Not loaded by Claude Code. Taking up space.
- **Context:** These are Google Workspace automation skills (Sheets, Docs, Drive, etc.). If still useful, they need a proper plugin wrapper. If not, delete them.

## Hardening

### 7. Build runtime smoke tests
- [ ] Design test harness extending the band-materials eval pattern (`mr-burger-music/eval/`)
- [ ] Select 8-10 representative skills across all 5 plugins
- [ ] Write test cases with input prompts and expected output characteristics
- [ ] Create eval subagent that runs each test and scores output
- **Why:** Audit verified existence only. Component evaluation verified quality of instructions. Neither confirmed runtime behavior — skills could have bad frontmatter or broken references that only surface during invocation.
- **Pattern to follow:** `mr-burger-music/eval/rubric.md` (4-dimension, 1-3 scale)
- **Suggested test skills:**
  - ir-teaching: `bellringer-builder`, `benchmarks`, `unit-builder-protocol`
  - ir-data-pipeline: `data-quality-checker`, `growth-analyzer`
  - ir-classroom-ops: `observation-prep`
  - mr-burger-music: `band-materials`, `score-transformer`
  - mr-burger-workflow: `work-logger`, `plugin-registry`

### 8. Expand regression suite
- [ ] Define 8-10 canonical workflows (multi-skill chains)
- [ ] Document expected behavior for each
- [ ] Run before and after any future cleanup/refactoring
- **Why:** Audit Phase 5 tested only 3 workflows. With 90 skills and 16 agents, 3 is too narrow to catch regressions from structural changes.
- **Suggested workflows:**
  1. IR Unit Build: unit-planner → unit-builder-protocol → quality-reviewer
  2. Student Data Pipeline: student-data-processor → data-quality-checker → growth-analyzer → report-builder
  3. Bellringer Generation: bellringer-builder (Mode 1) → vocabulary-instruction → mc-question-generation
  4. Observation Prep: observation-prep → ir-framework → esol-core
  5. Sub Plan: sub-folder-builder → sub-plan-generator agent
  6. Data Analysis: data-analyst agent (orchestrates 9 skills)
  7. Music Practice: music-coach agent → practice-planner → session-logger
  8. Session Lifecycle: workflow-agent OPEN → [work] → /wrap command → workflow-agent CLOSE
  9. Capture Flow: /capture command → work-logger → TASKS.md
  10. Score Transformation: score-transformer → score-writer agent
