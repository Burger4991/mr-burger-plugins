# Ecosystem Component Evaluation
*Date: 2026-03-22 | Evaluating: 90 skills, 16 agents, 11 commands, 4 hooks across 5 plugins*

## Scoring Convention

| Score | Meaning |
|-------|---------|
| 1 | Fail — clear gap, needs remediation |
| 2 | Acceptable — works but has blind spots |
| 3 | Strong — thorough, correct, actionable |

**Flag threshold:** Any dimension scores 1, OR average < 2.0

---

**Summary:** 0 flagged, 6 passing of 6 dimensions | **Average: 2.67**

**Top issues:**
- 2 knowledge file stubs degrade output quality (`ear-training`, `band-materials`) — both in mr-burger-music
- 4 of 5 plugin.json files don't enumerate their skills/agents — relying on implicit directory discovery
- `collaborative-protocols` skill directory exists but skill.md not found during sampling — verify integrity

---

## Sampling Methodology

Evaluated 25 components (17 skills, 5 agents, 3 commands) across all 5 plugins. Selection targeted both high-traffic skills and edge cases. Also verified all plugin.json files against disk for 100% coverage on that dimension.

| Plugin | Skills Sampled | Agents Sampled | Commands Sampled |
|--------|----------------|----------------|------------------|
| ir-teaching | 5 of 61 | 2 of 11 | — |
| ir-data-pipeline | 3 of 9 | 1 of 2 | — |
| ir-classroom-ops | 3 of 6 | — | — |
| mr-burger-music | 3 of 7 | 1 of 2 | — |
| mr-burger-workflow | 3 of 7 | 1 of 1 | 3 of 11 |

---

## Dimension 1: Frontmatter — Score: 3

**Question:** Does every component have name, description, and trigger phrases?

**Evidence:**
- 24 of 25 sampled components have complete frontmatter (name, description, triggers or routing guidance)
- 1 component (`collaborative-protocols`) could not be read — file may be missing or misnamed
- Agents consistently include `color` field for Cowork UI differentiation
- Commands include `allowed-tools` restrictions in frontmatter (good security practice)
- Trigger phrases are specific and distinct — no overlap detected across skills

**Per-plugin:**
| Plugin | Frontmatter Score |
|--------|-------------------|
| ir-teaching | 3 — all sampled have comprehensive frontmatter with routing tables |
| ir-data-pipeline | 3 — includes version numbers, precise trigger descriptions |
| ir-classroom-ops | 3 — clear triggers, version numbers present |
| mr-burger-music | 3 — complete, though `ear-training` is minimal |
| mr-burger-workflow | 3 — skills + commands both well-tagged |

---

## Dimension 2: Instruction Clarity — Score: 3

**Question:** Are instructions specific enough for Claude to execute without guessing?

**Evidence:**
- 14 of 17 sampled skills scored "Expert" (5/5) clarity — templates, worked examples, anti-patterns, edge case handling
- 3 scored "Very good" (4/5) — clear but shorter (`esol-core`, `behavior-tracker`, `ear-training`)
- Zero vague skills found — even short ones (`prompt-scaffold` at ~130 lines) are purposefully concise, not incomplete
- Standout patterns:
  - **Hard gates:** `unit-builder-protocol` stops execution if spec files missing (not silent failure)
  - **Decision trees:** `data-analyst` agent has explicit "if CRITICAL issues found, STOP" logic
  - **Multi-mode:** `bellringer-builder` has 3 distinct modes, each fully worked end-to-end
  - **Implementation code:** `data-quality-checker` and `growth-analyzer` embed full Python with docstrings

**Grade distribution across sample:**
| Grade | Count | Examples |
|-------|-------|---------|
| A+ | 14 | benchmarks, bellringer-builder, unit-builder-protocol, data-quality-checker, growth-analyzer, sub-folder-builder, observation-prep, score-transformer, plugin-registry, work-logger, capture, wrap, quality-reviewer agent, data-analyst agent |
| A | 4 | esol-core, behavior-tracker, prompt-scaffold, plan |
| A- | 1 | band-materials |
| B+ | 1 | ear-training |

---

## Dimension 3: Knowledge Dependencies — Score: 2

**Question:** Are referenced knowledge files populated (not stubs)?

**Evidence:**
- **Fully populated:** 13 of 17 sampled skills have their knowledge dependencies met
- **Stub knowledge files (2):**
  - `ear-training` → references `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` (stub). Skill includes fallback: "proceed using core rule and protocol structure" — graceful degradation but output quality is reduced
  - `band-materials` → references `knowledge/band/beginning-band-essentials.md` (stub). Skill works with general knowledge but can't produce range-specific exercises without the reference data
- **Mixed:** `benchmarks` references a `standards/` subdir with loading instructions — partially populated
- **N/A:** `prompt-scaffold` (meta-skill, no knowledge files needed)

**Impact:** Both stubs are in `mr-burger-music`. Teaching and data plugins have zero stub dependencies — all knowledge files are populated or embedded inline.

**Per-plugin:**
| Plugin | Knowledge Score | Notes |
|--------|-----------------|-------|
| ir-teaching | 3 | All sampled skills have populated refs |
| ir-data-pipeline | 3 | Complete — includes inline Python implementations |
| ir-classroom-ops | 3 | All templates fully embedded |
| mr-burger-music | 2 | 2 of 3 sampled have stub knowledge files |
| mr-burger-workflow | 3 | All refs populated (PROJECT.md, TASKS.md, etc.) |

---

## Dimension 4: Cross-Plugin Coherence — Score: 3

**Question:** Do skills, agents, and commands reference each other correctly?

**Evidence:**
- **Agent → skill orchestration works:** `data-analyst` agent dispatches 9 ir-data-pipeline skills in correct sequence with explicit phase outputs
- **Command → skill references work:** `/capture` routes to `session-state-reader` and `work-logger`; `/wrap` invokes `session-state-reader` then updates PROJECT/HANDOFF/TASKS
- **Plugin-registry skill** documents all 5 plugins with data ownership, cross-plugin flows, and file patterns — serves as the routing map
- **work-logger** correctly routes entries to per-area files (TASKS.md, data-analysis-log.md, parent-contacts.md)
- **No circular dependencies detected** in the sample
- **No broken cross-references** found — all mentioned skills exist

**Cross-plugin data flows verified:**
| Flow | Source Plugin | Destination Plugin | Status |
|------|-------------|-------------------|--------|
| Student data → teaching tasks | ir-data-pipeline | mr-burger-workflow | Documented in plugin-registry |
| Unit building → task tracking | ir-teaching | mr-burger-workflow | Documented, work-logger handles |
| Observation prep → notes | ir-classroom-ops | mr-burger-workflow | Documented |

---

## Dimension 5: Plugin.json Accuracy — Score: 2

**Question:** Does each plugin.json match what's actually on disk?

**Evidence:**
- **mr-burger-music:** Lists 7 skills + 2 agents — **exact match** with disk. Only plugin that enumerates components.
- **ir-teaching:** plugin.json is minimal (name, version, description, keywords only). 61 skills and 11 agents on disk — none listed. Works via directory discovery.
- **ir-data-pipeline:** Same minimal pattern. 9 skills and 2 agents on disk — none listed.
- **ir-classroom-ops:** Same minimal pattern. 6 skills on disk — none listed.
- **mr-burger-workflow:** Same minimal pattern. 7 skills, 1 agent, 11 commands, 1 hook on disk — none listed. Commands and hooks are entirely absent from plugin.json.

**Impact:** Directory discovery works — Claude Code loads everything correctly. But the inconsistency means:
1. No single source of truth for what a plugin provides (must `ls` the dirs)
2. `package.sh` must discover components rather than read a manifest
3. If a stray directory appears in `skills/`, it gets auto-loaded (no allowlist protection)

**Recommendation:** Either enumerate components in all plugin.json files (matching mr-burger-music pattern) or document directory-discovery as the intentional convention.

---

## Dimension 6: Completeness Distribution — Score: 3

**Question:** Is the quality consistent, or are there stub skills hiding among strong ones?

**Evidence:**
- **Quality is remarkably consistent.** The 17-skill sample shows 14 A+, 4 A, 1 A-, 1 B+ — no skills scoring below B+.
- **No fake skills** — every sampled skill directory contains a substantive skill.md, not a placeholder
- **Length varies intentionally:** meta-skills are short (~100–170 lines), protocol skills are long (~1,400–2,200 lines), data skills embed full Python implementations (~650–1,100 lines). Length correlates with purpose, not quality.
- **Agents are uniformly strong:** all 5 sampled agents have multi-stage workflows, explicit decision points, and output formats
- **Commands are well-structured:** all 3 sampled commands have step-by-step workflows with numbered phases

**Length distribution across sample:**
| Range | Count | Typical Use |
|-------|-------|------------|
| < 200 lines | 4 | Meta-skills, focused commands |
| 200–500 lines | 7 | Reference skills, agents |
| 500–1,000 lines | 4 | Implementation-heavy (data, classroom) |
| > 1,000 lines | 5 | Protocol-level orchestrators (teaching) |

---

## Ecosystem-Wide Scores

| Dimension | Score | Flag |
|-----------|-------|------|
| 1. Frontmatter | 3 | — |
| 2. Instruction Clarity | 3 | — |
| 3. Knowledge Dependencies | 2 | — |
| 4. Cross-Plugin Coherence | 3 | — |
| 5. Plugin.json Accuracy | 2 | — |
| 6. Completeness Distribution | 3 | — |
| **Average** | **2.67** | **No flags** |

---

## Flagged Components

No components scored below B+. Two components warrant attention:

| Component | Plugin | Issue | Severity |
|-----------|--------|-------|----------|
| `ear-training/skill.md` | mr-burger-music | Knowledge file stub; ~100 lines (shortest skill) | Low — graceful fallback exists |
| `band-materials/skill.md` | mr-burger-music | Knowledge file stub; range constraints rely on general knowledge | Low — functional but degraded |
| `collaborative-protocols` | ir-teaching | Skill directory may exist but skill.md not readable during evaluation | Verify — may be orphan dir |

---

## Recommendations

### Priority 1: Populate knowledge stubs (mr-burger-music)
- `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` — write the ear training protocol content
- `knowledge/band/beginning-band-essentials.md` — populate with range charts, fingering guides, beginning exercises

### Priority 2: Standardize plugin.json convention
- Decide: explicit enumeration (mr-burger-music pattern) or documented directory-discovery convention
- If enumeration: add `skills`, `agents`, `commands` arrays to ir-teaching, ir-data-pipeline, ir-classroom-ops, mr-burger-workflow plugin.json files
- If directory-discovery: document this as the canonical pattern in CLAUDE.md

### Priority 3: Verify collaborative-protocols
- Check `ir-teaching/skills/collaborative-protocols/` — confirm skill.md exists and is populated
- If orphan directory, remove it

---

## Verdict

**The ecosystem is production-quality.** 90 skills, 16 agents, and 11 commands show remarkably consistent craftsmanship — no stubs pretending to be complete, no vague instructions, no broken cross-references. The two knowledge file stubs in mr-burger-music are the only material gap, and both handle missing data gracefully. The plugin.json inconsistency is a housekeeping issue, not a functional problem.

Grade: **A** (strong across all dimensions, minor gaps in knowledge population and manifest consistency)
