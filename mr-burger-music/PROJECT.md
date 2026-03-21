# mr-burger-music — Project State
*Last updated: 2026-03-21*

## Phase
complete — score transformer suite shipped (PRs #1 + #2 merged)

## Plan
- **File:** `docs/superpowers/plans/2026-03-21-mr-burger-music-score-transformer.md`
- **Current step:** complete — all tasks done
- **Decided:** `tools/` lives inside the plugin; two-track approach (score-writer agent for net-new, score-transformer skill + tools/ for modifications); flat chromatic TPC spellings (Ab not G#, Bb not A#); `mscz_utils.py` is the shared module

## Implementation
- **Active:** None
- **Done:**
  - `mscz_utils.py` — shared utilities (TPC, EID, XML builders, zip I/O, PDF export, phrase iterator)
  - `test_mscz_utils.py` — test suite
  - `add_enclosures.py` — chromatic enclosure transformations
  - `add_guide_tones.py` — guide tone voice overlay
  - `diatonic_enclosures.py` — diatonic enclosure variant
  - `transpose_pattern.py` — 12-key pattern transposer
  - `score-transformer` skill — live and symlinked
  - PR #1 (music-score-transformer → main) merged 2026-03-21
  - PR #2 (feat/score-transformer-suite → main) merged 2026-03-21
  - band-materials v2.0.0 — jazz leadsheets + theory worksheets, 19 eval test cases
- **Blocked:** None

## Decisions Log
- 2026-03-21: `tools/` inside plugin — scripts outside get forgotten
- 2026-03-21: Two-track approach: score-writer (net-new) vs score-transformer + tools/ (modifications)
- 2026-03-21: Flat chromatic TPC spellings preferred (Ab not G#, Bb not A#)
- 2026-03-21: `mscz_utils.py` = shared module; extract before adding new scripts

## Open Questions
- What other transformations are useful? (guide tones, transpositions, enclosures done)
- Knowledge file stubs (trumpet/, guitar/, jazz/, band/) — populate from PDFs when ready

## Watch Out For
- `ET.indent()` requires Python 3.9+
- MuseScore CLI exit code 1 is normal (QML warnings) — check file exists and size > 0
- `iter_phrases()` yields 5 values: `(phrase_idx, m_ii, m_v, m_i, m_rest)`
- Octave normalization in `transpose_pattern.py` — keep trumpet pitches MIDI 60–84
- Run `./scripts/setup.sh` from repo root after any structural changes
