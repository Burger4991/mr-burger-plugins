# mr-burger-music Plugin Updates — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the mr-burger-music plugin with 6 targeted updates: LHS stage tracking, skill/agent clarification, ear-training skill, cross-plugin flow, band-rehearsal skill, and score-writer v2 lead sheet support.

**Architecture:** All changes are markdown file edits/additions within `mr-burger-plugins/mr-burger-music/`. New skills require a `skill.md` + `plugin.json` entry + symlink via `setup.sh`. No code compilation needed — edits are live via symlinks immediately in Claude Code.

**Tech Stack:** Markdown skill files, YAML frontmatter, MuseScore MusicXML (Task 6), `~/.claude/skills/` symlinks managed by `scripts/setup.sh`.

---

## File Map

| File | Task | Action |
|------|------|--------|
| `mr-burger-music/skills/practice-planner/skill.md` | 1, 2 | Modify |
| `mr-burger-music/skills/session-logger/skill.md` | 2 | Modify |
| `mr-burger-music/agents/music-coach.md` | 1, 4 | Modify |
| `mr-burger-music/knowledge/linear-harmony-system/Journal/Current-Stage.md` | 1 | Create |
| `mr-burger-music/skills/ear-training/skill.md` | 3 | Create |
| `mr-burger-music/skills/band-rehearsal/skill.md` | 5 | Create |
| `mr-burger-music/agents/score-writer.md` | 6 | Modify |
| `mr-burger-music/plugin.json` | 3, 5 | Modify |
| `mr-burger-workflow/skills/plugin-registry/skill.md` | 4 | Modify |

---

## Task 1: LHS Stage Tracking

**Goal:** Track which LHS Part each instrument is currently on so `music-coach` can sequence blocks appropriately.

**Files:**
- Create: `mr-burger-music/knowledge/linear-harmony-system/Journal/Current-Stage.md`
- Modify: `mr-burger-music/agents/music-coach.md`
- Modify: `mr-burger-music/skills/practice-planner/skill.md`

- [ ] **Step 1: Create the stage tracking file**

Create `mr-burger-music/knowledge/linear-harmony-system/Journal/Current-Stage.md`:

```markdown
# Current LHS Stage

Last updated: YYYY-MM-DD

## Trumpet
**Part:** 1
**Focus:** Fundamentals + Outline 1 in major keys
**Notes:** Embouchure rebuilding — prioritize long tones and sing-before-play.

## Guitar
**Part:** 1
**Focus:** Fretboard geography + shell voicings in root position
**Notes:** Beginner. Open chords solid. Shell voicings in progress.

---

## LHS Part Reference

| Part | Trumpet Focus | Guitar Focus |
|------|--------------|--------------|
| 1 | Fundamentals + Outline 1 major | Fretboard + Shell voicings root pos |
| 2 | Outline 1–3 major, cycle of keys | Shells all inversions, Outline 1 pos 1 |
| 3 | Outline 1–3 major + minor | Connect positions, Outline 1–3 |
| 4 | Embellishment + Application | Full integration, Standards |

Update this file after each LHS progression decision.
```

- [ ] **Step 2: Add stage reading to music-coach**

In `mr-burger-music/agents/music-coach.md`, after the existing "Read Practice History" section, add a new step:

```markdown
### Step 1b: Read Current Stage

Read `knowledge/linear-harmony-system/Journal/Current-Stage.md`.

Surface:
- Current Part for each instrument
- Any stage-specific notes

Use this to sequence blocks from the correct LHS Part. Don't suggest Part 3 blocks if the player is in Part 1.

If the file is missing: note it and proceed using Part 1 defaults.
```

- [ ] **Step 3: Add stage reading to practice-planner**

In `mr-burger-music/skills/practice-planner/skill.md`, add to the "How to Use This Skill" section:

```markdown
4. If `knowledge/linear-harmony-system/Journal/Current-Stage.md` is available, read it and limit block selection to the current LHS Part for each instrument.
```

- [ ] **Step 4: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add mr-burger-music/knowledge/linear-harmony-system/Journal/Current-Stage.md
git add mr-burger-music/agents/music-coach.md
git add mr-burger-music/skills/practice-planner/skill.md
git commit -m "feat(mr-burger-music): add LHS stage tracking file and hook into music-coach + practice-planner"
```

---

## Task 2: Clarify Skill vs Agent Decision

**Goal:** Document when to use `practice-planner` / `session-logger` as standalone skills vs `music-coach` as the full agent. Prevent confusion.

**Files:**
- Modify: `mr-burger-music/skills/practice-planner/skill.md`
- Modify: `mr-burger-music/skills/session-logger/skill.md`

- [ ] **Step 1: Add "When to use this vs music-coach" to practice-planner**

Add to the top of the `## How to Use This Skill` section in `practice-planner/skill.md`:

```markdown
## When to Use This vs music-coach

| Use this skill | Use music-coach agent |
|----------------|----------------------|
| Quick plan, no history context needed | Want history-informed recommendations |
| Mid-conversation plan request | Starting a full practice session |
| Light overhead preferred | Want post-session logging too |
```

- [ ] **Step 2: Add "When to use this vs music-coach" to session-logger**

Add to the top of `session-logger/skill.md` after the frontmatter:

```markdown
## When to Use This vs music-coach

| Use this skill | Use music-coach agent |
|----------------|----------------------|
| Already practiced, just logging | Want planning + logging in one session |
| Quick brain dump only | Want history-informed next-session advice |
| Mid-conversation log request | Starting a full coaching session |
```

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/skills/practice-planner/skill.md
git add mr-burger-music/skills/session-logger/skill.md
git commit -m "docs(mr-burger-music): clarify skill vs agent decision for practice-planner and session-logger"
```

---

## Task 3: Ear Training Skill

**Goal:** Create an `ear-training` skill that invokes the Ear-Training-Protocol.md to guide singing-before-playing exercises.

**Files:**
- Create: `mr-burger-music/skills/ear-training/skill.md`
- Modify: `mr-burger-music/plugin.json`

- [ ] **Step 1: Read the source document**

Read `mr-burger-music/knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` fully before writing the skill.

- [ ] **Step 2: Create the skill file**

Create `mr-burger-music/skills/ear-training/skill.md`:

```markdown
---
name: ear-training
description: >
  Guides a sing-before-play ear training exercise using the LHS Ear Training Protocol.
  Use when asked to "work on ear training", "practice singing outlines", "do ear training",
  or when the user wants to strengthen the connection between ear and instrument.
version: 1.0.0
---

# Ear Training

Guide an ear training exercise using the LHS Ear Training Protocol.

## Knowledge File

Read `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` for the full protocol before generating any exercise.

If the file is missing: notify the user and proceed using the core rule: **if you can't sing it, you can't play it with intention.**

## Player Status

- **Trumpet**: Comeback player, range C4–C5, embouchure rebuilding
- **Guitar**: Beginner, shell voicings in progress

## Inputs

- **Instrument**: trumpet or guitar (or voice-only)
- **Outline/focus**: which outline or interval to work on
- **Level**: Level 1 (basic sing-then-play) / Level 2 (sing with chord) / Level 3 (full audiation)

## Output Format

1. **Exercise title** — specific and brief
2. **Protocol level** — which level of the protocol this targets
3. **Setup** — metronome BPM, which outline/key
4. **Steps** — numbered, plain language, following the protocol
5. **Success criterion** — one clear signal that it's working

## Core Rule

Always begin by stating: "If you can't sing it, you can't play it with intention."
```

- [ ] **Step 3: Update plugin.json**

In `mr-burger-music/plugin.json`, add `"ear-training"` to the `skills` array:

```json
{
  "name": "mr-burger-music",
  "plugin_id": "mr-burger-music",
  "version": "1.0.0",
  "skills": ["practice-planner", "session-logger", "exercise-generator", "band-materials", "ear-training"],
  "agents": ["music-coach", "score-writer"]
}
```

- [ ] **Step 4: Run setup.sh to create the symlink**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

Verify: `ls -la ~/.claude/skills/ear-training` should show a symlink.

- [ ] **Step 5: Commit**

```bash
git add mr-burger-music/skills/ear-training/skill.md
git add mr-burger-music/plugin.json
git commit -m "feat(mr-burger-music): add ear-training skill from LHS Ear Training Protocol"
```

---

## Task 4: Cross-Plugin Flow (Music → Workflow)

**Goal:** Register the music → workflow data flow and add optional weekly summary logging to `music-coach`.

**Files:**
- Modify: `mr-burger-workflow/skills/plugin-registry/skill.md`
- Modify: `mr-burger-music/agents/music-coach.md`

- [ ] **Step 1: Add music data flow to plugin-registry**

In `mr-burger-workflow/skills/plugin-registry/skill.md`, add to the Cross-Plugin Data Flows table:

```markdown
| mr-burger-music | Session log entry | → mr-burger-workflow | Note in notes/music/ |
| mr-burger-music | Weekly practice summary | → mr-burger-workflow | Journal entry |
```

Also add a flow example in the Cross-Plugin Data Flows section:

```markdown
PRACTICE LOGGING → NOTES
  music-coach session completed (optional weekly summary)
  → Summary: "Week of YYYY-MM-DD — X sessions, trumpet blocks, guitar blocks, key struggles"
  → Route to: ~/Documents/Music/Practice/notes/weekly-summary-YYYY-MM-DD.md
```

- [ ] **Step 2: Add optional weekly summary to music-coach**

After Step 4 (log prompt) in `music-coach.md`, add:

```markdown
### Step 5: Weekly Summary (optional, Fridays or on request)

If today is Friday or the user says "log a weekly summary":

Ask: "Want me to write a weekly practice summary?"

If yes: review the last 7 entries in Practice-Log.md and generate:

**File:** `~/Documents/Music/Practice/notes/weekly-summary-[YYYY-MM-DD].md`

```
# Practice Week — [date range]

**Sessions:** [count]
**Total time:** [estimate if logged]

**Trumpet:** [what was practiced, any progress noted]
**Guitar:** [what was practiced, any progress noted]

**Recurring struggles:** [what keeps showing up as "still hard"]
**Next week's priority:** [1 sentence]
```

Confirm: "Saved to weekly-summary-[date].md ✓"
```

- [ ] **Step 3: Create the notes directory**

```bash
mkdir -p ~/Documents/Music/Practice/notes/
```

- [ ] **Step 4: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add mr-burger-workflow/skills/plugin-registry/skill.md
git add mr-burger-music/agents/music-coach.md
git commit -m "feat(mr-burger-music): add cross-plugin flow and weekly summary to music-coach"
```

---

## Task 5: Band Rehearsal Skill

**Goal:** Create a `band-rehearsal` skill that generates a full beginning band rehearsal plan (warm-up → technique → music → cool-down).

**Files:**
- Create: `mr-burger-music/skills/band-rehearsal/skill.md`
- Modify: `mr-burger-music/plugin.json`

- [ ] **Step 1: Read the band knowledge file**

Read `mr-burger-music/knowledge/band/beginning-band-essentials.md` fully before writing the skill.

- [ ] **Step 2: Create the skill file**

Create `mr-burger-music/skills/band-rehearsal/skill.md`:

```markdown
---
name: band-rehearsal
description: >
  Generates a full beginning band rehearsal plan with warm-up, technique, music, and cool-down.
  Use when planning a class period for beginning band students, not for personal practice.
  Distinct from band-materials which generates individual exercises.
version: 1.0.0
---

# Band Rehearsal Planner

Generate a full rehearsal plan for a beginning band class period.

## Audience

First-year beginning band students. Trumpet focus (Mr. Burger's instrument), but plans should work for full band.

## Knowledge File

`knowledge/band/beginning-band-essentials.md`

If stub: notify user, proceed using standard beginning band structure.

## Inputs

- **Class length**: 30 / 45 / 50 minutes
- **Concept focus**: tone production / fingerings / rhythms / scales / articulation / ensemble
- **Music in progress**: title of piece or "none yet"
- **Recent struggles**: what the class has been stuck on (optional)

## Output Format

Full rehearsal plan with time blocks:

```
# Band Rehearsal Plan — [date or "Template"] — [duration]
**Focus:** [concept]

## Warm-Up ([X] min)
[Specific exercise or activity. Include what to listen for.]

## Technique/Drill ([X] min)
[Specific exercise targeting the concept focus. Include teaching cues.]

## Music Work ([X] min)
[Specific measures or passage from the piece in progress. Include goal for today.]

## Cool-Down / Reflection ([X] min)
[Closing activity — listening, discussion question, or quick exit review.]

---
**Materials needed:** [list anything to prepare]
**Next rehearsal focus:** [one sentence]
```

## Notes

- Keep language concrete — what to say to students, not just what to do
- Flag any materials needed (worksheets, recordings, etc.)
- For 30-min classes: compress technique and music, keep warm-up and cool-down
```

- [ ] **Step 3: Update plugin.json**

Add `"band-rehearsal"` to the skills array:

```json
{
  "name": "mr-burger-music",
  "plugin_id": "mr-burger-music",
  "version": "1.0.0",
  "skills": ["practice-planner", "session-logger", "exercise-generator", "band-materials", "ear-training", "band-rehearsal"],
  "agents": ["music-coach", "score-writer"]
}
```

- [ ] **Step 4: Run setup.sh**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

Verify: `ls -la ~/.claude/skills/band-rehearsal` shows symlink.

- [ ] **Step 5: Commit**

```bash
git add mr-burger-music/skills/band-rehearsal/skill.md
git add mr-burger-music/plugin.json
git commit -m "feat(mr-burger-music): add band-rehearsal skill for full class period planning"
```

---

## Task 6: score-writer v2 — Lead Sheet Support

**Goal:** Expand `score-writer` to support simple lead sheets: melody line + chord symbols above the staff, for one-instrument + chord output from jazz standards.

**Files:**
- Modify: `mr-burger-music/agents/score-writer.md`

- [ ] **Step 1: Review the existing score-writer agent**

Read `mr-burger-music/agents/score-writer.md` fully, focusing on: scope constraints, MusicXML generation template, Step 1 (parse/validate), and output locations.

- [ ] **Step 2: Update scope section**

Replace the Scope (v1) section with:

```markdown
## Scope (v2)

**Supported:**
- Trumpet exercises (personal practice)
- Simple single-line beginning band trumpet exercises
- Lead sheets: single melody line + chord symbols above the staff (trumpet or C concert pitch)

**NOT supported:**
- Guitar scores or tab
- Multi-instrument ensemble parts
- Full arrangements or backing tracks
- Complex chord voicings or extended harmonies

If asked for an unsupported type, explain the scope and suggest `exercise-generator` for text-based alternatives. Do not proceed.
```

- [ ] **Step 3: Add lead sheet input handling**

After the existing input format section, add:

```markdown
### Lead Sheet Input

Accept either free description or structured format:

```
Title: [title]
Instrument: lead sheet (trumpet) OR lead sheet (concert pitch)
Time signature: [e.g., 4/4]
Key signature: [e.g., Bb major]
Tempo: [BPM]
Melody: [C4 quarter, D4 quarter, F4 half, ...]
Chords: [measure 1: Cm7 | measure 2: F7 | measure 3: BbMaj7 | ...]
```
```

- [ ] **Step 4: Add lead sheet MusicXML generation instructions**

Add a new section after the existing MusicXML template:

```markdown
### Lead Sheet MusicXML Notes

To add chord symbols above the staff, use the `<harmony>` element before the note it falls on:

```xml
<harmony>
  <root>
    <root-step>C</root-step>
    <root-alter>0</root-alter>
  </root>
  <kind text="m7">minor-seventh</kind>
</harmony>
<note>
  <pitch><step>C</step><octave>4</octave></pitch>
  <duration>4</duration>
  <type>quarter</type>
</note>
```

**Common kind values:**
| Symbol | `<kind>` value | `text` attr |
|--------|---------------|-------------|
| maj7 | major-seventh | maj7 |
| m7 | minor-seventh | m7 |
| 7 | dominant | 7 |
| m7b5 | half-diminished | m7b5 |
| dim7 | diminished-seventh | dim7 |

Output location for lead sheets: `~/Documents/Music/Jazz/Lead-Sheets/Generated/`

```bash
mkdir -p ~/Documents/Music/Jazz/Lead-Sheets/Generated/
```
```

- [ ] **Step 5: Update output locations section**

Add to the Output Locations section:

```markdown
- Lead sheets → `~/Documents/Music/Jazz/Lead-Sheets/Generated/`
```

- [ ] **Step 6: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add mr-burger-music/agents/score-writer.md
git commit -m "feat(mr-burger-music): score-writer v2 — add lead sheet support with chord symbols"
```

---

## Final Step: Package and Verify

- [ ] **Run setup.sh one final time**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

- [ ] **Verify all new symlinks**

```bash
ls -la ~/.claude/skills/ear-training
ls -la ~/.claude/skills/band-rehearsal
ls -la ~/.claude/agents/music-coach.md
ls -la ~/.claude/agents/score-writer.md
```

- [ ] **Update plugin version in plugin.json to 1.1.0**

```json
{
  "name": "mr-burger-music",
  "plugin_id": "mr-burger-music",
  "version": "1.1.0",
  "skills": ["practice-planner", "session-logger", "exercise-generator", "band-materials", "ear-training", "band-rehearsal"],
  "agents": ["music-coach", "score-writer"]
}
```

- [ ] **Final commit**

```bash
git add mr-burger-music/plugin.json
git commit -m "chore(mr-burger-music): bump version to 1.1.0 after updates"
```
