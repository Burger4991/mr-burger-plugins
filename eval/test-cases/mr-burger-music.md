# mr-burger-music Smoke Test Cases

## Test Case 7: band-materials

**Skill:** `mr-burger-music/skills/band-materials/skill.md`

**Prompt:** Generate a beginner-level warm-up exercise for trumpet that focuses on
lip slurs between C4 and G4. Students have been playing for about 6 weeks.

**Expected concept:** A warm-up exercise using lip slurs (no tongue, air-only note changes)
within the C4–G4 range. Should include specific notes, rhythms, and teaching tips
for 6-week beginners.

**Key checks:**
- All notes within C4–G4 (early beginner / beginner range)
- Lip slur patterns specified (e.g., C4–E4–G4 or C4–G4)
- Rhythm values appropriate for 6 weeks in (whole notes, half notes, maybe quarters)
- Teaching tips included
- Score-writer handoff format present
- No notes above G4 for this level

---

## Test Case 8: score-transformer

**Skill:** `mr-burger-music/skills/score-transformer/skill.md`

**Prompt:** I have an Outline 1 exercise in C at `~/Documents/Music/Practice/outlines/outline-1-C.mscz`.
Apply the chromatic enclosure transformation to it.

**Expected concept:** A step-by-step walkthrough of reading the .mscz file, applying chromatic
enclosures (approach each target note from a half step above and below), and exporting PDF.
Should reference the correct tools/ scripts and TPC conventions.

**Key checks:**
- References the correct .mscz file path from the prompt
- Explains chromatic enclosure transformation correctly (half step above + below target)
- Mentions the Bb trumpet TPC convention (tpc2 = tpc + 2)
- References tools/ directory scripts
- Includes PDF export step via MuseScore CLI
- Follows the 4-measure phrase structure (ii-V-I-rest) if applicable
