# Implementation Plan — Runtime Eval Testing (Tasks 7 & 8)
*Created: 2026-03-22 | Source: TASKS.md tasks 7–8, mr-burger-music/eval/ framework*

## Approach: Test First, Report, Then Fix

The audit verified structure. The component evaluation verified instruction quality.
Neither confirmed runtime behavior. This plan tests runtime behavior **before**
recommending changes — findings drive recommendations, not assumptions.

**Sequence:**
1. Build eval infrastructure (rubric, test cases, workflow definitions, subagent prompts)
2. Run all evaluations (10 smoke tests + 10 regression workflows)
3. Write findings report with evidence-based recommendations
4. Only then make changes based on findings

---

## Phase 1: Infrastructure (Complete)

### Generalized Rubric (`eval/rubric.md`)

Adapted from `mr-burger-music/eval/rubric.md`. Changed domain-specific dimensions
(Range/Notes, Level Appropriateness) to cross-plugin dimensions:

| Dimension | What it measures |
|-----------|-----------------|
| Instruction Following | Does output match the skill's specified format and sections? |
| Specificity | Is output tailored to prompt context, or generic filler? |
| Completeness | Is it a finished deliverable, or placeholders/trailing off? |
| Quality | Is it well-crafted, accurate, pedagogically/analytically sound? |

Scoring: 1–3 per dimension. Flagged if any = 1 or average < 2.0.

### Smoke Test Cases (`eval/test-cases/`)

2 test cases per plugin, 10 total. Skills selected for coverage breadth:

| Plugin | Skill 1 | Skill 2 |
|--------|---------|---------|
| ir-teaching | bellringer-builder | benchmarks |
| ir-data-pipeline | data-quality-checker | growth-analyzer |
| ir-classroom-ops | observation-prep | sub-folder-builder |
| mr-burger-music | band-materials | score-transformer |
| mr-burger-workflow | work-logger | plugin-registry |

Each test case includes: realistic prompt, expected concept, key checks (what to verify).

### Regression Workflow Definitions (`eval/regression/workflows.md`)

10 canonical multi-skill chains covering all 5 plugins:

| # | Workflow | Chain | Stages |
|---|---------|-------|--------|
| 1 | IR Unit Build | unit-planner → unit-builder-protocol → quality-reviewer | 3 |
| 2 | Student Data Pipeline | student-data-processor → data-quality-checker → growth-analyzer → report-builder | 4 |
| 3 | Bellringer Generation | bellringer-builder → vocabulary-instruction → mc-question-generation | 3 |
| 4 | Observation Prep | observation-prep → ir-framework → esol-core | 3 |
| 5 | Sub Plan | sub-folder-builder → sub-plan-generator agent | 2 |
| 6 | Data Analysis (Agent) | data-analyst agent → 9 skills | 6 phases |
| 7 | Music Practice | music-coach → practice-planner → session-logger | 3 |
| 8 | Session Lifecycle | workflow-agent OPEN → /wrap → workflow-agent CLOSE | 3 |
| 9 | Capture Flow | /capture → work-logger → TASKS.md + area notes | 3 |
| 10 | Score Transformation | score-transformer → tools/ → score-writer agent | 3 |

Each workflow defines: trigger prompt, chain with handoff points, expected behavior at each stage.

### Eval Subagent Prompts

- `eval/smoke-test-eval.md` — runs 10 test cases, scores on rubric, writes results
- `eval/regression/regression-eval.md` — simulates workflow chains, scores handoffs, writes results

---

## Phase 2: Execution (In Progress)

### Smoke Tests
- Agent reads each skill.md + knowledge files, generates output for each prompt, scores on 4 dimensions
- Results written to `eval/results/2026-03-22-smoke-test.md`

### Regression Workflows
- Agent reads all chain components, simulates each stage, scores handoff integrity (1–3)
- Overall: PASS (all handoffs 2+), PARTIAL (some 2, degraded output), FAIL (any handoff 1)
- Results written to `eval/results/2026-03-22-regression.md`

---

## Phase 3: Report (Pending)

Findings report goes to `docs/audits/2026-03-22-runtime-eval-report.md`.

Report structure:
1. Executive summary (flagged/passing counts, pass/partial/fail counts)
2. Smoke test findings — per-plugin results with evidence
3. Regression findings — workflow results with handoff analysis
4. Knowledge file gaps — skills referencing missing/stub files
5. Cross-cutting patterns — issues that affect multiple skills or workflows
6. Recommendations — evidence-based, prioritized by impact
7. Recommended changes — specific files + what to change, with rationale from findings

**Key principle:** Every recommendation must cite a specific test result or handoff failure.
No speculative improvements — only changes motivated by observed behavior.

---

## Files Created

| File | Purpose |
|------|---------|
| `eval/rubric.md` | 4-dimension scoring rubric |
| `eval/smoke-test-eval.md` | Smoke test subagent prompt |
| `eval/test-cases/ir-teaching.md` | bellringer-builder + benchmarks test cases |
| `eval/test-cases/ir-data-pipeline.md` | data-quality-checker + growth-analyzer test cases |
| `eval/test-cases/ir-classroom-ops.md` | observation-prep + sub-folder-builder test cases |
| `eval/test-cases/mr-burger-music.md` | band-materials + score-transformer test cases |
| `eval/test-cases/mr-burger-workflow.md` | work-logger + plugin-registry test cases |
| `eval/regression/workflows.md` | 10 workflow definitions |
| `eval/regression/regression-eval.md` | Regression eval subagent prompt |
| `eval/results/` | Timestamped results (populated by eval runs) |
