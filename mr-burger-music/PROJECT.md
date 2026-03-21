# mr-burger-music — Project State
*Last updated: 2026-03-21 09:38*

## Phase
implementing — score transformer suite (Tasks 1–5 remaining)

## Plan
- **File:** `docs/superpowers/plans/2026-03-21-mr-burger-music-score-transformer.md`
- **Current step:** Task 1 — create `tools/mscz_utils.py` (shared utilities: TPC, EID, XML builders, zip I/O, PDF export, phrase iterator). Tests first.
- **Decided:** `tools/` lives inside the plugin (not in `~/Documents/Music/`); two-track approach (score-writer agent for net-new, score-transformer skill + tools/ for modifications); flat preference for chromatic TPC spellings (Ab not G#, Bb not A#); `mscz_utils.py` is the shared module all scripts import
- **Open:** Nothing — ready to execute Task 1

## Implementation
- **Active:** Task 1 — `tools/mscz_utils.py`
- **Done:** `add_enclosures.py` working and committed; `score-transformer` skill live and symlinked; PR #1 open (`music-score-transformer` → `main`)
- **Blocked:** None

## Decisions Log
- 2026-03-21: `tools/` inside plugin — scripts outside the plugin get forgotten
- 2026-03-21: Two-track approach: score-writer agent (net-new) vs score-transformer + tools/ (modifications)
- 2026-03-21: Flat chromatic TPC spellings preferred (Ab not G#, Bb not A#)
- 2026-03-21: `mscz_utils.py` = shared module; extract before adding new scripts

## Open Questions
- After suite is complete: what other transformations are useful? (guide tones, transpositions done; what else?)
- Knowledge file stubs (trumpet/, guitar/, jazz/, band/) — when to populate from PDFs?

## Watch Out For
- `ET.indent()` requires Python 3.9+ — confirmed working
- MuseScore CLI exit code 1 is normal (QML warnings) — check file exists and size > 0 instead
- `iter_phrases()` yields 5 values: `(phrase_idx, m_ii, m_v, m_i, m_rest)` — match the unpack
- Octave normalization in `transpose_pattern.py` needs refinement — keep trumpet pitches MIDI 60–84
- PR #1 open — merge before or alongside Task 1
- Run `./scripts/setup.sh` from repo root after any structural changes
