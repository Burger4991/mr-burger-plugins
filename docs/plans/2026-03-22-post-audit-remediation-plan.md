# Implementation Plan — Post-Audit Remediation
*Created: 2026-03-22 | Source: TASKS.md + research findings*

## Research Findings (updated from original TASKS.md)

| Task | Original Assessment | Actual State |
|------|-------------------|--------------|
| 1. FUSE cleanup | 193 files to delete | Confirmed — straightforward |
| 2. collaborative-protocols | May be orphan | **Not orphan** — file exists as `SKILL.md` (uppercase). Convention is `skill.md` (lowercase). Rename needed. |
| 3. ear-training knowledge | Stub to populate | **Broken symlink** — `knowledge/linear-harmony-system` → `/Users/alexanderburger/Documents/Music/Practice/Linear Harmony System` (macOS path, broken on this machine). Need to create the directory structure and write the file. |
| 4. band-materials knowledge | Stub to populate | **Already done** — `knowledge/band/beginning-band-essentials.md` is fully populated (400+ lines). Remove from task list. |
| 5. plugin.json standardization | Decision needed | Confirmed — 4 of 5 plugins lack explicit arrays |
| 6. GWS plugin | 92 skills to decide on | **Already gone** — `~/.agents/skills/` doesn't exist. Remove from task list. |
| 7. Smoke tests | Build from scratch | Eval framework already exists at `mr-burger-music/eval/` with rubric, 19 test cases, subagent. Extend this pattern. |
| 8. Regression suite | Design from scratch | Needs design; suggested workflows in TASKS.md are solid starting point |

**Net: 6 real tasks remain (tasks 4 and 6 are already resolved).**

---

## Task 1: Clean FUSE Artifacts

**What:** Delete `.fuse_hidden*` files from `~/.claude/commands/` and `~/.claude/skills/`
**Steps:**
1. `find ~/.claude/commands -name '.fuse_hidden*' -delete`
2. `find ~/.claude/skills -name '.fuse_hidden*' -delete`
3. Verify: `find ~/.claude -name '.fuse_hidden*' | wc -l` → 0
**Risk:** None — these are FUSE filesystem leftovers, not functional files
**Time:** 2 min

---

## Task 2: Fix collaborative-protocols Naming

**What:** Rename `SKILL.md` → `skill.md` in `ir-teaching/skills/collaborative-protocols/`
**Steps:**
1. `mv ir-teaching/skills/collaborative-protocols/SKILL.md ir-teaching/skills/collaborative-protocols/skill.md`
2. Verify content is intact: `head -5 ir-teaching/skills/collaborative-protocols/skill.md`
3. Commit the rename
**Risk:** Low — git tracks renames; symlink points to directory not file
**Time:** 2 min

---

## Task 3: Create Ear-Training Knowledge File

**What:** The `linear-harmony-system` knowledge directory is a broken symlink to a macOS path. Need to:
- Remove the broken symlink
- Create the directory structure
- Write `04-Reference/Ear-Training-Protocol.md` with content derived from the ear-training skill

**Steps:**
1. Remove broken symlink: `rm mr-burger-music/knowledge/linear-harmony-system`
2. Create directory: `mkdir -p mr-burger-music/knowledge/linear-harmony-system/04-Reference`
3. Write `Ear-Training-Protocol.md` with:
   - Core rule ("if you can't sing it, you can't play it with intention")
   - 3-level protocol (Level 1: sing-then-play, Level 2: sing with chord, Level 3: full audiation)
   - Outline progressions (Outline 1 through 3+)
   - Instrument-specific adaptations (trumpet comeback, guitar beginner)
   - Success criteria per level
   - Example exercises for each level
4. Verify: skill references `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` — confirm path matches
5. Commit

**Risk:** Medium — writing pedagogical content requires accuracy. The skill.md has a graceful fallback ("If the file is missing: proceed using the core rule"), so bad content is worse than no content. Keep it concise and accurate.
**Time:** 20 min

---

## Task 5: Standardize plugin.json

**What:** Add explicit `skills`, `agents`, `commands` arrays to the 4 plugins that currently lack them, matching the mr-burger-music pattern.

**Steps:**
1. For each plugin, inventory actual directories:
   - `ls ir-teaching/skills/` → list all skill names
   - `ls ir-teaching/agents/` → list all agent names (strip .md)
   - Repeat for ir-data-pipeline, ir-classroom-ops, mr-burger-workflow
2. Update each plugin.json with arrays
3. Cross-check: array count must match directory count
4. Also verify mr-burger-music's existing arrays are current
5. Commit all 4 (or 5) plugin.json changes together

**Files to modify:**
- `ir-teaching/.claude-plugin/plugin.json` — add skills (62), agents (11)
- `ir-data-pipeline/.claude-plugin/plugin.json` — add skills (9), agents (2)
- `ir-classroom-ops/.claude-plugin/plugin.json` — add skills (6)
- `mr-burger-workflow/.claude-plugin/plugin.json` — add skills (7), agents (1), commands (11)

**Risk:** Low — additive change, no functional impact until Cowork packaging
**Time:** 30 min

---

## Task 7: Build Runtime Smoke Tests

**What:** Extend the band-materials eval pattern to cover 8-10 skills across all 5 plugins.

**Existing pattern** (in `mr-burger-music/eval/`):
- `rubric.md` — 4-dimension scoring (Range/Notes, Specificity, Pedagogical Soundness, Level Appropriateness)
- `test-cases/*.md` — input prompts with expected output characteristics
- `band-materials-eval.md` — subagent that runs tests and scores output
- `results/` — timestamped run files

**Steps:**
1. Create top-level `eval/` directory for cross-plugin smoke tests
2. Write `eval/rubric.md` — generalized rubric (adapt from band-materials):
   - Dimension 1: Instruction Following (did output match the prompt?)
   - Dimension 2: Specificity (tailored vs generic?)
   - Dimension 3: Completeness (all expected sections present?)
   - Dimension 4: Quality (actionable, accurate, well-structured?)
3. Write `eval/test-cases/` — one file per plugin with 2 test cases each:
   - `ir-teaching.md`: bellringer-builder + benchmarks
   - `ir-data-pipeline.md`: data-quality-checker + growth-analyzer
   - `ir-classroom-ops.md`: observation-prep + sub-folder-builder
   - `mr-burger-music.md`: band-materials + score-transformer
   - `mr-burger-workflow.md`: work-logger + plugin-registry
4. Write `eval/smoke-test-eval.md` — subagent prompt
5. Create `eval/results/` with `.gitkeep`
6. Commit

**Risk:** Medium — test case design requires understanding each skill's expected output
**Time:** 2 hrs

---

## Task 8: Expand Regression Suite

**What:** Define 8-10 canonical multi-skill workflows and document expected behavior for pre/post-change regression testing.

**Steps:**
1. Create `eval/regression/` directory
2. Write `eval/regression/README.md` — purpose, how to run, when to run
3. Write `eval/regression/workflows.md` — 10 canonical workflows:
   - Each workflow: name, skills/agents involved, trigger sequence, expected behavior, pass criteria
4. Write `eval/regression/regression-eval.md` — subagent that runs workflow tests
5. Create `eval/regression/results/` with `.gitkeep`
6. Commit

**Workflows (from TASKS.md):**
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

**Risk:** Low — documentation only, no code changes
**Time:** 2 hrs

---

## Execution Order

1. **Task 1** — FUSE cleanup (2 min, zero risk)
2. **Task 2** — collaborative-protocols rename (2 min, low risk)
3. **Task 3** — ear-training knowledge file (20 min, medium risk)
4. **Task 5** — plugin.json standardization (30 min, low risk)
5. **Task 7** — smoke tests (2 hrs, medium risk)
6. **Task 8** — regression suite (2 hrs, low risk)

**After all tasks:** Update TASKS.md (mark completed), update PROJECT.md, commit and push.

---

## TASKS.md Updates Needed

- Task 4 (band-materials knowledge): Mark done — file already populated
- Task 6 (GWS plugin): Mark done — directory no longer exists
- Task 2: Update description — rename, not verify
- Task 3: Update description — broken symlink, not stub
