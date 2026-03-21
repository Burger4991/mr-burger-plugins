# mr-burger-music

Plugin for Claude Code. Personal music practice system — trumpet, jazz, beginning band.

**Working directory for development:** `~/Documents/Tech/mr-burger-plugins/mr-burger-music/`

## What's Here

| Component | Path | What it does |
|-----------|------|-------------|
| Skills (4) | `skills/` | practice-planner, session-logger, exercise-generator, band-materials, score-transformer |
| Agents (2) | `agents/` | music-coach, score-writer |
| Knowledge | `knowledge/` | LHS docs, trumpet/guitar/jazz refs, MuseScore CLI docs |
| Tools | `tools/` | Python scripts for MuseScore automation |

## Plugin Config

`plugin.json` — lists skills + agents. Update this when adding/removing either.

Symlinked into `~/.claude/skills/` and `~/.claude/agents/` via `../scripts/setup.sh`.

## MuseScore Automation

Two approaches — use the right one:

| Approach | When to use | Where |
|----------|-------------|-------|
| **score-writer agent** | Net-new scores from description | `agents/score-writer.md` |
| **score-transformer skill** | Variations of existing `.mscz` files | `skills/score-transformer/` + `tools/` |

**Tools:** Python scripts in `tools/` — read `.mscz` (zip → XML), apply musical logic, repackage, export via CLI.

MuseScore CLI: `/Applications/MuseScore 4.app/Contents/MacOS/mscore`
Export PDF: `mscore -f -o output.pdf input.mscz`

**Bb trumpet TPC convention** (critical for new scripts):
- `<pitch>` = MIDI concert pitch
- `<tpc>` = concert TPC
- `<tpc2>` = written TPC = concert TPC + 2

## Knowledge Files

| File | Status |
|------|--------|
| `knowledge/musescore-cli.md` | Populated |
| `knowledge/linear-harmony-system/` | Populated |
| `knowledge/trumpet/` | Stubs — pending PDF extraction |
| `knowledge/guitar/` | Stubs — pending PDF extraction |
| `knowledge/jazz/` | Stubs — pending PDF extraction |
| `knowledge/band/` | Stubs |

## Dev Workflow

```bash
# After editing any skill or agent:
cd ~/Documents/Tech/mr-burger-plugins && ./scripts/setup.sh

# Test a skill in Claude Code — just use it
# No rebuild needed — skills are symlinked live
```
