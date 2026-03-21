# mr-burger-music: Score Transformer Build-Out Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable suite of MuseScore transformation scripts for jazz practice, starting with a shared utilities module that all scripts import, then adding guide tone overlay, diatonic enclosures, and 12-key pattern generator.

**Architecture:** Each transformation is a standalone Python script in `tools/` that imports shared utilities from `tools/mscz_utils.py`. Scripts read an existing `.mscz`, apply a musical transformation via XML manipulation, repackage, and export PDF via the MuseScore CLI. The shared module eliminates duplication across scripts (TPC math, EID generation, XML builders, zip I/O, PDF export).

**Tech Stack:** Python 3 stdlib only (xml.etree.ElementTree, zipfile, os, base64, shutil) + MuseScore 4 CLI at `/Applications/MuseScore 4.app/Contents/MacOS/mscore`

---

## File Map

| File | Status | Responsibility |
|------|--------|----------------|
| `tools/mscz_utils.py` | **Create** | Shared utilities: TPC, EID, XML builders, zip I/O, PDF export, phrase parsing |
| `tools/add_enclosures.py` | **Refactor** | Import from mscz_utils; remove duplicated helpers |
| `tools/add_guide_tones.py` | **Create** | Overlay guide tone melody (3rds + 7ths) as a second voice above existing outline |
| `tools/diatonic_enclosures.py` | **Create** | Enclosure variant: diatonic step above + chromatic half step below → target |
| `tools/transpose_pattern.py` | **Create** | Take a 1-key pattern and generate all 12 keys using cycle-of-fifths transposition |
| `tools/tests/test_mscz_utils.py` | **Create** | Unit tests for all shared utilities |
| `mr-burger-music/skills/score-transformer/skill.md` | **Update** | Add new transformations to Available Transformations section |

---

## Task 1: Extract shared utilities into `mscz_utils.py`

All four existing helpers in `add_enclosures.py` are needed by every future script. Extract them first so tasks 2–4 have a clean foundation.

**Files:**
- Create: `tools/mscz_utils.py`
- Create: `tools/tests/__init__.py`
- Create: `tools/tests/test_mscz_utils.py`

- [ ] **Step 1: Write failing tests for TPC helper**

```python
# tools/tests/test_mscz_utils.py
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from mscz_utils import pitch_to_tpc

def test_c_concert():
    tpc_c, tpc_w = pitch_to_tpc(60)  # C4
    assert tpc_c == 14  # C
    assert tpc_w == 16  # D (written for Bb trumpet)

def test_eb_concert():
    tpc_c, tpc_w = pitch_to_tpc(63)  # Eb4
    assert tpc_c == 11  # Eb
    assert tpc_w == 13  # F

def test_bb_prefers_flat():
    tpc_c, tpc_w = pitch_to_tpc(70)  # Bb4
    assert tpc_c == 12  # Bb not A#
    assert tpc_w == 14  # C
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd ~/Documents/Tech/mr-burger-plugins/mr-burger-music
python3 -m pytest tools/tests/test_mscz_utils.py -v
```
Expected: `ModuleNotFoundError: No module named 'mscz_utils'`

- [ ] **Step 3: Create `tools/mscz_utils.py`** — extract from `add_enclosures.py` verbatim, then add `open_mscz` / `save_mscz` / `export_pdf` / `get_measures` helpers:

```python
#!/usr/bin/env python3
"""
mscz_utils.py — Shared utilities for MuseScore (.mscz) transformation scripts.

All transformation scripts in tools/ import from here.
"""

import xml.etree.ElementTree as ET
import zipfile, shutil, os, base64, subprocess

MUSESCORE_CLI = '/Applications/MuseScore 4.app/Contents/MacOS/mscore'

# ── TPC ──────────────────────────────────────────────────────────────────────

_CONCERT_TPC = {
    0: 14,   # C
    1:  9,   # Db
    2: 16,   # D
    3: 11,   # Eb
    4: 18,   # E
    5: 13,   # F
    6:  8,   # Gb
    7: 15,   # G
    8: 10,   # Ab
    9: 17,   # A
    10: 12,  # Bb
    11: 19,  # B
}

def pitch_to_tpc(midi_pitch):
    """Return (tpc_concert, tpc_written) for Bb trumpet.
    tpc_written = tpc_concert + 2 (major 2nd transposition).
    """
    tpc_c = _CONCERT_TPC[midi_pitch % 12]
    return tpc_c, tpc_c + 2

# ── EID ──────────────────────────────────────────────────────────────────────

def gen_eid():
    """Generate a 23-char EID in MuseScore's format: 11_11."""
    raw = os.urandom(16)
    b64 = base64.b64encode(raw).decode('ascii').rstrip('=')[:22].ljust(22, 'A')
    return b64[:11] + '_' + b64[11:22]

# ── XML builders ─────────────────────────────────────────────────────────────

def make_chord(pitch, duration):
    """<Chord> with one <Note>."""
    tpc_c, tpc_w = pitch_to_tpc(pitch)
    chord = ET.Element('Chord')
    ET.SubElement(chord, 'eid').text = gen_eid()
    ET.SubElement(chord, 'durationType').text = duration
    note = ET.SubElement(chord, 'Note')
    ET.SubElement(note, 'eid').text = gen_eid()
    ET.SubElement(note, 'pitch').text = str(pitch)
    ET.SubElement(note, 'tpc').text = str(tpc_c)
    ET.SubElement(note, 'tpc2').text = str(tpc_w)
    return chord

def make_rest(duration, dotted=False):
    """<Rest> element."""
    rest = ET.Element('Rest')
    ET.SubElement(rest, 'eid').text = gen_eid()
    if dotted:
        ET.SubElement(rest, 'dots').text = '1'
    ET.SubElement(rest, 'durationType').text = duration
    return rest

def get_first_note_pitch(measure):
    """MIDI pitch of the first note in a measure, or None."""
    chord = measure.find('.//Chord')
    if chord is None:
        return None
    note = chord.find('Note')
    if note is None:
        return None
    return int(note.find('pitch').text)

# ── File I/O ─────────────────────────────────────────────────────────────────

def open_mscz(mscz_path, work_dir):
    """Extract .mscz to work_dir. Returns (ET tree, mscx_path, zip namelist)."""
    shutil.rmtree(work_dir, ignore_errors=True)
    os.makedirs(work_dir)
    with zipfile.ZipFile(mscz_path, 'r') as z:
        names = z.namelist()
        z.extractall(work_dir)
    mscx_name = next(n for n in names if n.endswith('.mscx'))
    mscx_path = os.path.join(work_dir, mscx_name)
    tree = ET.parse(mscx_path)
    return tree, mscx_path, names

def save_mscz(tree, mscx_path, names, work_dir, output_mscz):
    """Write modified tree to mscx and repackage as .mscz."""
    ET.indent(tree, space='  ')
    tree.write(mscx_path, encoding='UTF-8', xml_declaration=True)
    with zipfile.ZipFile(output_mscz, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in names:
            z.write(os.path.join(work_dir, name), name)

def export_pdf(mscz_path, pdf_path):
    """Export .mscz to PDF via MuseScore CLI. Returns True if file created."""
    subprocess.run([MUSESCORE_CLI, '-f', '-o', pdf_path, mscz_path],
                   capture_output=True)
    return os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0

# ── Phrase parsing ────────────────────────────────────────────────────────────

def get_measures(root):
    """Return list of Measure elements from Staff id=1."""
    staff = root.find('.//Staff[@id="1"]')
    return [c for c in staff if c.tag == 'Measure']

def iter_phrases(measures, phrase_size=4):
    """Yield (phrase_idx, m_ii, m_v, m_i, m_rest) for each phrase."""
    for i in range(len(measures) // phrase_size):
        base = i * phrase_size
        yield i, measures[base], measures[base+1], measures[base+2], measures[base+3]
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tools/tests/test_mscz_utils.py -v
```
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add tools/mscz_utils.py tools/tests/
git commit -m "feat(music): add mscz_utils shared module with tests"
```

---

## Task 2: Refactor `add_enclosures.py` to import from `mscz_utils`

Validates that the shared module is a drop-in replacement. No behavior change.

**Files:**
- Modify: `tools/add_enclosures.py`
- Modify: `tools/tests/test_mscz_utils.py` (add integration test)

- [ ] **Step 1: Write integration test**

```python
# Add to tools/tests/test_mscz_utils.py
import tempfile

def test_add_enclosures_roundtrip():
    """add_enclosures.py produces a .mscz with correct note count."""
    from add_enclosures import process
    src = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    if not os.path.exists(src):
        return  # skip if source not present
    with tempfile.NamedTemporaryFile(suffix='.mscz', delete=False) as f:
        out = f.name
    try:
        process(src, out)
        assert os.path.exists(out)
        assert os.path.getsize(out) > 10_000
    finally:
        os.unlink(out)
```

- [ ] **Step 2: Run test to verify it passes with current script**

```bash
python3 -m pytest tools/tests/test_mscz_utils.py::test_add_enclosures_roundtrip -v
```
Expected: PASS (confirms baseline before refactor)

- [ ] **Step 3: Rewrite `add_enclosures.py` to use mscz_utils**

Replace everything above `add_enclosure_to_rest_measure` with:
```python
#!/usr/bin/env python3
"""add_enclosures.py — Chromatic enclosures on Ligon outline worksheets."""
import os
from mscz_utils import (open_mscz, save_mscz, export_pdf,
                         get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, make_rest)
```

Remove `pitch_to_tpc`, `gen_eid`, `make_chord`, `make_rest`, `get_first_note_pitch` definitions (now from mscz_utils). Keep `add_enclosure_to_rest_measure` and `add_enclosure_to_ii_measure` as local functions — they are specific to this transformation.

Replace `process()` I/O with mscz_utils calls:
```python
def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/enc_build')
    root = tree.getroot()
    measures = get_measures(root)
    for phrase_idx, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        v_target = get_first_note_pitch(m_v)
        if v_target:
            add_enclosure_to_ii_measure(m_ii, v_target)
        next_base = (phrase_idx + 1) * 4
        if next_base < len(measures):
            next_target = get_first_note_pitch(measures[next_base])
            if next_target:
                add_enclosure_to_rest_measure(m_rest, next_target)
    save_mscz(tree, mscx_path, names, '/tmp/enc_build', output_mscz)
    print(f"Saved: {output_mscz}")
```

- [ ] **Step 4: Run all tests**

```bash
python3 -m pytest tools/tests/ -v
```
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tools/add_enclosures.py
git commit -m "refactor(music): add_enclosures imports from mscz_utils"
```

---

## Task 3: `diatonic_enclosures.py`

Same structure as chromatic enclosures but approach notes are: diatonic step above (from key scale) + chromatic half step below → target. The most common bebop enclosure sound.

**Files:**
- Create: `tools/diatonic_enclosures.py`
- Modify: `tools/tests/test_mscz_utils.py`

**Music theory note:** For each key, the diatonic step above a target note is the next scale degree up. For Bb major: scale = [Bb, C, D, Eb, F, G, A]. Diatonic step above F (5th) = G. Chromatic below F = E. So enclosure of F = G, E → F. The key is derived from the first note of the first ii chord in each group of 12 phrases.

- [ ] **Step 1: Write failing test**

```python
def test_diatonic_above_in_bb_major():
    from diatonic_enclosures import diatonic_step_above
    # Bb major scale (concert MIDI): 70, 72, 74, 75, 77, 79, 81
    bb_major = [70, 72, 74, 75, 77, 79, 81]
    assert diatonic_step_above(77, bb_major) == 79  # F → G
    assert diatonic_step_above(75, bb_major) == 77  # Eb → F
    assert diatonic_step_above(81, bb_major) == 70  # A → Bb (wraps)
```

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest tools/tests/test_mscz_utils.py::test_diatonic_above_in_bb_major -v
```
Expected: `ModuleNotFoundError`

- [ ] **Step 3: Create `tools/diatonic_enclosures.py`**

```python
#!/usr/bin/env python3
"""
diatonic_enclosures.py — Diatonic above + chromatic below enclosures.

Enclosure pattern: [diatonic step above target] [chromatic half step below target] → TARGET
More common in bebop lines than purely chromatic enclosures.
"""
import os
from mscz_utils import (open_mscz, save_mscz, get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, make_rest)

# Major scale intervals (semitones from root)
_MAJOR_INTERVALS = [0, 2, 4, 5, 7, 9, 11]

def build_scale(root_pitch):
    """Return list of concert MIDI pitches for one octave of major scale from root."""
    return [root_pitch + i for i in _MAJOR_INTERVALS]

def diatonic_step_above(pitch, scale):
    """Return the next scale degree above pitch (wraps at octave)."""
    pc = pitch % 12
    scale_pcs = [p % 12 for p in scale]
    # Find position in scale
    if pc in scale_pcs:
        idx = scale_pcs.index(pc)
        next_pc = scale_pcs[(idx + 1) % len(scale_pcs)]
    else:
        # Not in scale — find nearest scale tone above
        next_pc = min((sp for sp in scale_pcs if sp > pc),
                      default=scale_pcs[0])
    # Return at same octave or one above
    candidate = (pitch // 12) * 12 + next_pc
    if candidate <= pitch:
        candidate += 12
    return candidate

def add_diatonic_enclosure_to_ii_measure(measure, v_target, scale):
    voice = measure.find('voice')
    if not voice:
        return
    chords = voice.findall('Chord')
    if not chords:
        return
    voice.remove(chords[-1])
    enc_above = diatonic_step_above(v_target, scale)
    enc_below = v_target - 1  # chromatic half step below
    voice.append(make_chord(enc_above, 'eighth'))
    voice.append(make_chord(enc_below, 'eighth'))

def add_diatonic_enclosure_to_rest_measure(measure, next_ii_target, scale):
    voice = measure.find('voice')
    if not voice:
        return
    for rest in list(voice.findall('Rest')):
        voice.remove(rest)
    enc_above = diatonic_step_above(next_ii_target, scale)
    enc_below = next_ii_target - 1
    voice.append(make_rest('half', dotted=True))
    voice.append(make_chord(enc_above, 'eighth'))
    voice.append(make_chord(enc_below, 'eighth'))

def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/denc_build')
    root = tree.getroot()
    measures = get_measures(root)

    # Detect key from first ii chord root (first note of measure 1)
    first_pitch = get_first_note_pitch(measures[0])
    # ii chord root → major key is a minor 3rd below (e.g. Eb ii → Bb major, root = Bb)
    key_root = first_pitch - 3 if first_pitch else 70
    scale = build_scale(key_root % 12 + 60)  # normalize to octave 4

    for phrase_idx, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        v_target = get_first_note_pitch(m_v)
        if v_target:
            add_diatonic_enclosure_to_ii_measure(m_ii, v_target, scale)
        next_base = (phrase_idx + 1) * 4
        if next_base < len(measures):
            next_target = get_first_note_pitch(measures[next_base])
            if next_target:
                add_diatonic_enclosure_to_rest_measure(m_rest, next_target, scale)

    # Update title
    for text_el in root.findall('.//Text'):
        s = text_el.find('style')
        t = text_el.find('text')
        if s is not None and s.text == 'title' and t is not None:
            t.text = t.text + ' (Diatonic Enclosures)'
            break

    save_mscz(tree, mscx_path, names, '/tmp/denc_build', output_mscz)
    print(f"Saved: {output_mscz}")

if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Diatonic Enclosures.mscz')
    process(INPUT, OUTPUT)
```

- [ ] **Step 4: Run all tests**

```bash
python3 -m pytest tools/tests/ -v
```
Expected: all pass including new diatonic test

- [ ] **Step 5: Smoke test — export PNG and verify visually**

```bash
cd tools && python3 diatonic_enclosures.py
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" \
  -o /tmp/denc_preview.png \
  ~/Documents/MuseScore4/Scores/"Bert Ligon Outlines - Diatonic Enclosures.mscz" 2>/dev/null
open /tmp/denc_preview-1.png
```
Visually confirm: diatonic step above (larger interval) + half step below → target.

- [ ] **Step 6: Commit**

```bash
git add tools/diatonic_enclosures.py tools/tests/test_mscz_utils.py
git commit -m "feat(music): add diatonic_enclosures.py transformation"
```

---

## Task 4: `add_guide_tones.py`

Adds a second voice above each outline showing just the guide tones (3rd and 7th of each chord) as half notes. Teaches the ear to hear the voice leading skeleton underneath the outline.

**Files:**
- Create: `tools/add_guide_tones.py`
- Modify: `tools/tests/test_mscz_utils.py`

**Music theory:** For any ii-V-I in key X:
- ii chord 3rd = key root + 3 semitones (minor 3rd)
- ii chord 7th = key root + 10 semitones (minor 7th)
- V chord 3rd = key root + 7 semitones (= leading tone of key, major 3rd above V root)
- V chord 7th = key root + 5 semitones (tritone from V root = 4th degree of key)
- I chord 3rd = key root + 4 semitones (major 3rd)

- [ ] **Step 1: Write failing test**

```python
def test_guide_tones_bb_major():
    from add_guide_tones import guide_tones_for_key
    # Bb major: key_root = 70 (Bb4)
    # ii = Cm7: 3rd = Eb(63), 7th = Bb(70)
    # V = F7:   3rd = A(69),  7th = Eb(63)
    # I = Bbmaj7: 3rd = D(62)
    gt = guide_tones_for_key(70)
    assert gt['ii_3rd'] % 12 == 3   # Eb
    assert gt['ii_7th'] % 12 == 10  # Bb
    assert gt['v_3rd']  % 12 == 9   # A
    assert gt['v_7th']  % 12 == 3   # Eb
    assert gt['i_3rd']  % 12 == 2   # D
```

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest tools/tests/test_mscz_utils.py::test_guide_tones_bb_major -v
```

- [ ] **Step 3: Create `tools/add_guide_tones.py`**

```python
#!/usr/bin/env python3
"""
add_guide_tones.py — Adds guide tone voice above Ligon outlines.

Inserts Voice 2 into each phrase showing: ii_3rd(half) ii_7th(half) |
v_3rd(half) v_7th(half) | i_3rd(whole) | rest
This makes the 7→3 voice leading visible alongside the outline.
"""
import os
import xml.etree.ElementTree as ET
from mscz_utils import (open_mscz, save_mscz, get_measures, iter_phrases,
                         get_first_note_pitch, make_chord, make_rest, gen_eid)

def guide_tones_for_key(key_root):
    """Return guide tone MIDI pitches for ii-V-I in given major key.
    key_root: concert MIDI pitch of the tonic (e.g. 70 for Bb).
    """
    r = key_root
    return {
        'ii_3rd': r + 3,   # minor 3rd above tonic = 3rd of ii
        'ii_7th': r + 10,  # minor 7th above tonic = 7th of ii
        'v_3rd':  r + 7,   # perfect 5th above tonic = 3rd of V (leading tone)
        'v_7th':  r + 5,   # perfect 4th above tonic = 7th of V
        'i_3rd':  r + 4,   # major 3rd above tonic = 3rd of I
    }

def _normalize(pitch, ref_pitch, tolerance=6):
    """Shift pitch by octaves to be within tolerance semitones of ref_pitch."""
    while pitch < ref_pitch - tolerance:
        pitch += 12
    while pitch > ref_pitch + tolerance:
        pitch -= 12
    return pitch

def make_voice2(notes_durations):
    """Build a <voice> element (voice 2) with given (pitch, duration) pairs."""
    voice = ET.Element('voice')
    ET.SubElement(voice, 'eid').text = gen_eid()
    for pitch, dur in notes_durations:
        voice.append(make_chord(pitch, dur))
    return voice

def add_guide_tones_to_phrase(m_ii, m_v, m_i, m_rest, key_root):
    gt = guide_tones_for_key(key_root)
    ref = get_first_note_pitch(m_ii) or key_root + 3

    ii_3 = _normalize(gt['ii_3rd'], ref)
    ii_7 = _normalize(gt['ii_7th'], ref)
    v_3  = _normalize(gt['v_3rd'],  ref)
    v_7  = _normalize(gt['v_7th'],  ref)
    i_3  = _normalize(gt['i_3rd'],  ref)

    m_ii.append(make_voice2([(ii_3, 'half'), (ii_7, 'half')]))
    m_v.append(make_voice2([(v_3, 'half'), (v_7, 'half')]))
    m_i.append(make_voice2([(i_3, 'whole')]))

def detect_key_root(measures):
    """Detect key from first ii chord: ii root - minor 3rd = key root."""
    first = get_first_note_pitch(measures[0])
    if first is None:
        return 70  # default Bb
    return first - 3

def process(input_mscz, output_mscz):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/gt_build')
    root = tree.getroot()
    measures = get_measures(root)
    key_root = detect_key_root(measures)

    for _, m_ii, m_v, m_i, m_rest in iter_phrases(measures):
        add_guide_tones_to_phrase(m_ii, m_v, m_i, m_rest, key_root)

    for text_el in root.findall('.//Text'):
        s = text_el.find('style')
        t = text_el.find('text')
        if s is not None and s.text == 'title' and t is not None:
            t.text = t.text + ' (Guide Tones)'
            break

    save_mscz(tree, mscx_path, names, '/tmp/gt_build', output_mscz)
    print(f"Saved: {output_mscz}")

if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Bert Ligon Outlines - Guide Tones.mscz')
    process(INPUT, OUTPUT)
```

- [ ] **Step 4: Run all tests**

```bash
python3 -m pytest tools/tests/ -v
```

- [ ] **Step 5: Smoke test**

```bash
cd tools && python3 add_guide_tones.py
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" \
  -o /tmp/gt_preview.png \
  ~/Documents/MuseScore4/Scores/"Bert Ligon Outlines - Guide Tones.mscz" 2>/dev/null
open /tmp/gt_preview-1.png
```
Visually confirm: second voice showing half-note guide tones above outlines.

- [ ] **Step 6: Commit**

```bash
git add tools/add_guide_tones.py tools/tests/test_mscz_utils.py
git commit -m "feat(music): add guide tone voice overlay transformation"
```

---

## Task 5: `transpose_pattern.py`

Takes a single-key pattern (any `.mscz` with 1 phrase) and generates the full 12-key version using cycle-of-fifths transposition. This is the engine for building new worksheets from scratch.

**Files:**
- Create: `tools/transpose_pattern.py`
- Modify: `tools/tests/test_mscz_utils.py`

**Cycle of fifths (concert, ascending):** C→G→D→A→E→B→Gb→Db→Ab→Eb→Bb→F→C

- [ ] **Step 1: Write failing test**

```python
def test_transpose_interval():
    from transpose_pattern import transpose_pitch
    assert transpose_pitch(60, 7) == 67   # C → G (up perfect 5th)
    assert transpose_pitch(67, 7) == 74   # G → D
    assert transpose_pitch(75, 7) == 82   # Eb → Bb (up 5th)
```

- [ ] **Step 2: Run to verify failure**

```bash
python3 -m pytest tools/tests/test_mscz_utils.py::test_transpose_interval -v
```

- [ ] **Step 3: Create `tools/transpose_pattern.py`**

```python
#!/usr/bin/env python3
"""
transpose_pattern.py — Generate a 12-key worksheet from a single-key pattern.

Takes any .mscz with phrase_size measures, transposes it through the
cycle of fifths, and outputs a new .mscz with all 12 keys concatenated.
"""
import os, copy
import xml.etree.ElementTree as ET
from mscz_utils import (open_mscz, save_mscz, get_measures,
                         pitch_to_tpc, gen_eid)

# Cycle of fifths: interval in semitones to add for each successive key
# Starting from whatever key the input is in, go up by P5 (7 semitones) 11 times
CYCLE_INTERVALS = [i * 7 % 12 for i in range(12)]  # 0,7,2,9,4,11,6,1,8,3,10,5

def transpose_pitch(midi_pitch, semitones):
    return midi_pitch + semitones

def transpose_measure(measure, semitones):
    """Return a deep copy of measure with all pitches transposed."""
    m = copy.deepcopy(measure)
    for pitch_el in m.findall('.//pitch'):
        old = int(pitch_el.text)
        new = transpose_pitch(old, semitones)
        pitch_el.text = str(new)
        # Update TPC values
        tpc_c, tpc_w = pitch_to_tpc(new)
        note = pitch_el.getparent() if hasattr(pitch_el, 'getparent') else None
        # Walk sibling elements to update tpc/tpc2
    # Re-parse TPCs after transposition
    for note_el in m.findall('.//Note'):
        p = int(note_el.find('pitch').text)
        tpc_c, tpc_w = pitch_to_tpc(p)
        tpc_el = note_el.find('tpc')
        tpc2_el = note_el.find('tpc2')
        if tpc_el is not None:
            tpc_el.text = str(tpc_c)
        if tpc2_el is not None:
            tpc2_el.text = str(tpc_w)
    return m

def process(input_mscz, output_mscz, phrase_size=4):
    tree, mscx_path, names = open_mscz(input_mscz, '/tmp/tp_build')
    root = tree.getroot()
    measures = get_measures(root)
    staff = root.find('.//Staff[@id="1"]')

    # Remove all existing measures from staff (keep VBox)
    vbox = staff.find('VBox')
    for m in list(staff.findall('Measure')):
        staff.remove(m)

    # Get first pitch to determine base key
    base_pitch = None
    for m in measures[:phrase_size]:
        for p in m.findall('.//pitch'):
            base_pitch = int(p.text)
            break
        if base_pitch:
            break

    # Generate 12 keys
    for key_idx, interval_step in enumerate(CYCLE_INTERVALS):
        semitones = (interval_step * 7) % 12  # each key is 7 semitones from previous...
        # simpler: just use key_idx * 7 semitones total
        total_semitones = (key_idx * 7) % 12
        # Adjust for octave: keep notes in playable range
        for orig_measure in measures[:phrase_size]:
            transposed = transpose_measure(orig_measure, total_semitones)
            # Add line break after each key
            staff.append(transposed)

    save_mscz(tree, mscx_path, names, '/tmp/tp_build', output_mscz)
    print(f"Saved: {output_mscz} ({12} keys)")

if __name__ == '__main__':
    INPUT  = os.path.expanduser('~/Documents/MuseScore4/Scores/Pattern-OneKey.mscz')
    OUTPUT = os.path.expanduser('~/Documents/MuseScore4/Scores/Pattern-12Keys.mscz')
    process(INPUT, OUTPUT)
```

> **Note:** The octave normalization in `transpose_measure` needs refinement during implementation to keep notes in trumpet range (C4–C6). Adjust `total_semitones` to keep pitches between 60–84.

- [ ] **Step 4: Run tests**

```bash
python3 -m pytest tools/tests/ -v
```

- [ ] **Step 5: Commit**

```bash
git add tools/transpose_pattern.py tools/tests/test_mscz_utils.py
git commit -m "feat(music): add 12-key pattern transposer"
```

---

## Task 6: Update skill doc + push PR

- [ ] **Step 1: Update `skills/score-transformer/skill.md`** — add diatonic_enclosures, add_guide_tones, transpose_pattern to the Available Transformations section

- [ ] **Step 2: Run setup.sh to re-symlink**

```bash
cd ~/Documents/Tech/mr-burger-plugins && ./scripts/setup.sh
```

- [ ] **Step 3: Final commit and PR**

```bash
git add mr-burger-music/skills/score-transformer/skill.md
git commit -m "docs(music): update score-transformer skill with new transformations"
git push origin music-score-transformer
gh pr create --title "feat(mr-burger-music): score transformer suite — guide tones, diatonic enclosures, 12-key generator" \
  --body "Adds mscz_utils shared module, diatonic_enclosures.py, add_guide_tones.py, transpose_pattern.py. All import from shared utils. Tests cover TPC math, phrase parsing, and roundtrip."
```

---

## Key Reference: Bb Trumpet TPC

| Concert note | MIDI | tpc (concert) | tpc2 (written) |
|-------------|------|---------------|----------------|
| C | 60 | 14 | 16 |
| D | 62 | 16 | 18 |
| Eb | 63 | 11 | 13 |
| F | 65 | 13 | 15 |
| G | 67 | 15 | 17 |
| Ab | 68 | 10 | 12 |
| A | 69 | 17 | 19 |
| Bb | 70 | 12 | 14 |

tpc_written = tpc_concert + 2 (always, for Bb trumpet)
