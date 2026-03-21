---
name: score-transformer
description: >
  Applies musical transformations to existing MuseScore (.mscz) files — enclosures,
  transpositions, pattern variations — and exports PDF. Use when asked to "add enclosures",
  "generate a variation", "transpose this worksheet", or "build on this score".
  Distinct from score-writer (net-new scores): this skill modifies existing scores.
version: 1.0.0
---

# Score Transformer

Read an existing `.mscz` file, apply a musical transformation, and export a new score.

## When to Use vs. score-writer

| Task | Use |
|------|-----|
| "Add enclosures to this worksheet" | score-transformer |
| "Generate a variation of this score" | score-transformer |
| "Transpose this to all 12 keys" | score-transformer |
| "Make me a new trumpet exercise" | score-writer agent |
| "Create a scale sheet from scratch" | score-writer agent |

## How It Works

`.mscz` files are zip archives containing `.mscx` (XML). The transformer:
1. Unzips the `.mscz` to a temp directory
2. Parses the `.mscx` XML
3. Applies the requested transformation (Python)
4. Repackages as `.mscz`
5. Exports PDF via MuseScore CLI

All scripts live in `tools/` in this plugin directory.

## Bb Trumpet TPC Convention

Critical for any script that adds notes:
- `<pitch>` = MIDI concert pitch (60 = middle C)
- `<tpc>` = concert TPC (C=14, D=16, Eb=11, F=13, G=15, A=17, Bb=12, B=19)
- `<tpc2>` = written TPC = concert TPC + 2 (Bb trumpet sounds a major 2nd lower than written)

Prefer flat spellings for chromatic notes: Ab=10, Bb=12, Eb=11, Db=9, Gb=8.

## Phrase Structure (Ligon Outlines)

Each 4-measure group = one ii-V-I-rest phrase:
- Measure 1: ii chord (4 beats of notes)
- Measure 2: V chord (4 beats of notes)
- Measure 3: I chord (half note + half rest)
- Measure 4: whole rest

Guide tone voice leading: 7th of ii → 3rd of V (half step), 7th of V → 3rd of I (half step).

## Available Transformations

### Chromatic Enclosures (`tools/add_enclosures.py`)

Adds chromatic enclosures to Bert Ligon outline worksheets in all 12 keys.

**What it does:**
- Replaces the last beat of each ii chord measure with 2 eighth notes: [V_target+1] [V_target-1] → V beat 1
- Replaces each rest measure with: dotted half rest + [ii_target+1] [ii_target-1] → next ii beat 1

**Inputs:** any Ligon outline `.mscz` with 4-measure phrase structure
**Output:** new `.mscz` + PDF

```python
# Run directly:
python3 ~/Documents/Music/musescore-tools/add_enclosures.py
# Or from tools/:
python3 tools/add_enclosures.py
```

**To adapt for a new worksheet:** update `INPUT` and `OUTPUT` paths at bottom of script.

### Diatonic Enclosures (`tools/diatonic_enclosures.py`)

Bebop-style enclosures: diatonic step above + chromatic half step below → target.
More idiomatic than pure chromatic enclosures.

**What it does:** Same phrase targets as chromatic version, but approach note above is
the next scale degree (not chromatic) — gives a more bebop-authentic sound.

**Key detection:** Infers major key from first ii chord root (root − minor 3rd = tonic).

```python
python3 tools/diatonic_enclosures.py
```

### Guide Tones (`tools/add_guide_tones.py`)

Adds Voice 2 (stems down) showing the 3rd and 7th of each chord as half notes.
Makes the classic 7→3 voice leading skeleton visible alongside the outline.

**What it inserts per phrase:**
- ii measure: ii_3rd (half) + ii_7th (half)
- V measure: v_3rd (half) + v_7th (half)
- I measure: i_3rd (whole)

```python
python3 tools/add_guide_tones.py
```

### 12-Key Transposer (`tools/transpose_pattern.py`)

Takes any single-key pattern (any `.mscz`) and generates all 12 keys in
cycle-of-fifths order. Keeps pitches in trumpet range (C4–C6) automatically.

**Usage:**
```python
# Update INPUT/OUTPUT paths at bottom of script, then:
python3 tools/transpose_pattern.py
```

### Planned

- `rhythmic_variation.py` — triplet or displaced-rhythm version of outline

## Workflow for a New Transformation

1. Import shared utilities from `tools/mscz_utils.py` — don't redefine helpers
2. Write a Python script in `tools/` using:
   - `open_mscz(path, work_dir)` → tree, mscx_path, names
   - `save_mscz(tree, mscx_path, names, work_dir, output)` → repackages
   - `get_measures(root)` → list of Measure elements
   - `iter_phrases(measures)` → (idx, m_ii, m_v, m_i, m_rest) per phrase
   - `make_chord(pitch, duration)`, `make_rest(duration, dotted)`, `gen_eid()`
   - `pitch_to_tpc(midi_pitch)` → (tpc_concert, tpc_written)
3. Write tests in `tools/tests/test_mscz_utils.py` before implementing
4. Test: export PNG first (`-o output.png`), then PDF
5. Add to this skill's "Available Transformations" section

## PDF Export

```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -f -o output.pdf input.mscz
```

Exit code 1 with QML warnings is normal — check that the output file exists and is > 0 bytes.

## File Locations

- Source scores: `~/Documents/MuseScore4/Scores/`
- Generated PDFs: `~/Desktop/` (working) → `~/Documents/Music/Practice/Generated/` (long-term)
- Scripts: `~/Documents/Tech/mr-burger-plugins/mr-burger-music/tools/`
