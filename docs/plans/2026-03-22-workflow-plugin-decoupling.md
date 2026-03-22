# Workflow Plugin Review — Cross-Project Applicability
*Created: 2026-03-22 | Source: Full review of mr-burger-workflow/*

## Current State

The workflow plugin has 7 skills, 1 agent, 11 commands, and 1 hook. It splits into two layers:

**Generic workflow infrastructure** (portable across any project/area):
- session-state-reader — reads PROJECT.md / TASKS.md / HANDOFF.md
- prompt-scaffold — 5-part prompt framework
- workflow-agent — session open/close lifecycle
- /wrap, /resume, /plan, /checkpoint, /revise, /skill-update, /brainstorm-capture, /reflect

**Personal routing configuration** (hardcoded to 6 life areas):
- area-context — defines Teaching, Career, Music, Dog Training, Personal, Tech
- work-logger — logging formats per area type
- second-brain-ops — routing rules to area-specific paths
- plugin-registry — hardcodes 5 plugins and their data flows
- /capture, /brain-dump — classify and route to area-specific files
- /daily — reads across areas

The problem: these two layers are tangled. The generic commands call area-coupled skills directly, and the area-coupled skills each independently define where things go.

---

## The Duplication Problem

Four files independently maintain area → destination mappings:

| File | What it hardcodes |
|------|------------------|
| area-context | 6 areas with file paths, tags, and descriptions |
| work-logger | Logging formats per area (teaching, data, career, music, dog training) |
| second-brain-ops | Routing rules to ~/Documents/[area]/notes.md, Knowledge/[area].md |
| /capture command | Classification routes (teaching ideas → Teaching/ideas.md, career → Career/notes.md, etc.) |

If you add a new area (coaching, side business, a new class), you'd need to update all 4 files. If you rename an area's file path, same thing — 4 edits.

**plugin-registry** has the same issue for plugin data: it hardcodes 5 plugins and their cross-flows. Adding or removing a plugin means manually updating this file.

---

## Recommendation: Single Source of Truth for Areas

### Option A: area-context becomes the registry (Recommended)

Make `area-context` the **one file** that defines all areas, their paths, tags, and routing rules. Then have `work-logger`, `second-brain-ops`, `/capture`, and `/daily` reference area-context instead of maintaining their own copies.

**What changes:**

1. **area-context/skill.md** — Already has the richest area definitions. Add a structured registry section at the top:

```markdown
## Area Registry

| Area | Tag | Base Path | Notes File | Knowledge File |
|------|-----|-----------|------------|----------------|
| Teaching | teaching | ~/Documents/Teaching | notes.md | Knowledge/teaching.md |
| Career | career | ~/Documents/Career | notes.md | Knowledge/career.md |
| Music | music | ~/Documents/Music | notes.md | Knowledge/music.md |
| Dog Training | dog-training | ~/Documents/Dog-Training | notes.md | Knowledge/dog-training.md |
| Personal | personal | ~/Documents/Personal | notes.md | Knowledge/personal.md |
| Tech | tech | ~/Documents/Tech | notes.md | Knowledge/tech.md |
```

2. **work-logger/skill.md** — Replace per-area format definitions with:
   - A generic logging format that works for any area
   - A "read area-context for area-specific paths" instruction
   - Keep the format *examples* by area (they're useful), but derive the routing from area-context

3. **second-brain-ops/skill.md** — Replace hardcoded routing tree with:
   - "Read area-context to determine the correct destination path for this area"
   - Keep the TASKS.md / notes.md / Knowledge/ structure (that's the system, not area-specific)

4. **capture command** — Replace the classification → destination mapping with:
   - Classify the item type (task, idea, note, brainstorm, etc.)
   - Classify the area (read area-context)
   - Route: type determines the file *within* the area, area-context determines the path *to* the area

5. **plugin-registry/skill.md** — This one is trickier. The cross-plugin data flows are genuinely complex. Consider:
   - Move the plugin list to plugin.json files (already done in Task 5!)
   - Keep plugin-registry as a human-readable summary, but note it's a snapshot, not the source of truth
   - The source of truth for "what plugins exist" is now the plugin.json files themselves

### Option B: Extract a config file

Create `config/areas.md` or `config/areas.json` that all skills read. This is cleaner in theory but adds a file that doesn't fit the skill/agent/command pattern and might confuse the plugin loading system.

**Not recommended** — area-context already exists and is the natural home for this.

### Option C: Do nothing

The current system works. The duplication is manageable for 6 stable areas. If areas rarely change, the cost of decoupling may not be worth it.

**When this breaks:** If you start working across multiple schools, take on coaching, or add any new life area. Also if you share this plugin pattern with others — they'd need to edit 4+ files to customize for their areas.

---

## Applicability Assessment by Component

### Works anywhere, no changes needed

| Component | Why it's portable |
|-----------|------------------|
| session-state-reader | Reads generic files (PROJECT.md, TASKS.md, HANDOFF.md) |
| prompt-scaffold | Generic prompt framework |
| workflow-agent | Open/close lifecycle, reads standard files |
| /wrap | Updates PROJECT.md, HANDOFF.md, TASKS.md — all generic |
| /resume | Reads PROJECT.md + HANDOFF.md hierarchy |
| /plan | Creates plan files in project directory |
| /checkpoint | Deep save to standard locations |
| /brainstorm-capture | Saves to project docs/brainstorm/ |
| /revise | Updates CLAUDE.md based on session |
| /skill-update | Reviews and proposes skill changes |
| capture-detector hook | Pattern matching is generic |

### Works but with area coupling

| Component | What's coupled | Decoupling effort |
|-----------|---------------|-------------------|
| area-context | Area definitions — but this IS the config, so it should be coupled | None (this is the source of truth) |
| /daily | Reads TASKS.md grouped by area tags | Low — just needs area-context reference |
| /reflect | Updates Knowledge/[area].md | Low — derive paths from area-context |

### Needs decoupling for portability

| Component | What's coupled | Decoupling effort |
|-----------|---------------|-------------------|
| work-logger | Per-area logging formats and destinations | Medium — extract generic format, reference area-context for paths |
| second-brain-ops | Hardcoded routing tree to 6 area paths | Medium — replace tree with area-context lookup |
| /capture | Classification → destination mapping for 6 areas | Medium — classify type + area separately, route via area-context |
| /brain-dump | Routes to area-specific destinations | Low — thin wrapper, mostly delegates to /capture |
| plugin-registry | Hardcoded 5 plugins and data flows | Low — note that plugin.json is now source of truth |
| notion-sync | Notion database structure tied to current areas | Low — already has graceful degradation |

---

## Suggested Execution Order

If you decide to decouple (Option A):

1. **Add structured registry table to area-context** (~5 min)
   - This is additive, doesn't break anything

2. **Update plugin-registry** to note plugin.json as source of truth (~5 min)
   - Already mostly done via Task 5

3. **Update /capture to use area-context** (~15 min)
   - Biggest user-facing improvement: new areas auto-route

4. **Update work-logger to reference area-context** (~15 min)
   - Generic format + area-context paths

5. **Update second-brain-ops to reference area-context** (~10 min)
   - Replace routing tree with area-context lookup

6. **Update /brain-dump** (~5 min)
   - Thin — mostly follows /capture changes

7. **Test all commands end-to-end** (~20 min)

**Total: ~75 min of changes, most of it in steps 3–5.**

---

## What NOT to Change

- **Don't abstract the file structure.** TASKS.md, PROJECT.md, HANDOFF.md, Knowledge/ — this is the system's skeleton. It works because it's simple and consistent. Don't make it configurable.
- **Don't template the commands.** Each command has specific personality and workflow logic. Making them generic would lose the opinionated design that makes them useful.
- **Don't remove area-specific examples from work-logger.** The examples (how to log a teaching unit vs. a music session) are valuable. Just make the routing dynamic while keeping the format guidance.
- **Don't over-engineer plugin-registry.** A human-readable summary that might be slightly stale is better than a complex auto-discovery system.
