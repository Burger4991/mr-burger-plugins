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

## When to Use This vs band-materials

| Use this skill | Use band-materials skill |
|----------------|-------------------------|
| Planning a full class period | Need a single exercise or chorale |
| Structuring the whole rehearsal arc | Creating a worksheet or drill |
| Multi-segment plan with timing | Generating handoff material for score-writer |

## Audience

First-year beginning band students. Trumpet-focused (Mr. Burger's instrument), but plans should be usable for a full band class.

## Knowledge File

`knowledge/band/beginning-band-essentials.md`

If missing: notify user, proceed using standard beginning band structure.

## Inputs

- **Class length**: 30 / 45 / 50 minutes
- **Concept focus**: tone production / fingerings / rhythms / scales / articulation / ensemble playing
- **Music in progress**: title of piece or "none yet"
- **Recent struggles**: what the class has been stuck on (optional)

## Output Format

```
# Band Rehearsal Plan — [date or "Template"] — [duration]
**Focus:** [concept]

## Warm-Up ([X] min)
[Specific exercise or activity. What to listen for.]

## Technique/Drill ([X] min)
[Specific exercise targeting the concept. Include exact teaching cues — what to say to students.]

## Music Work ([X] min)
[Specific measures or passage. Today's goal for this section.]

## Cool-Down / Reflection ([X] min)
[Closing activity — listening, discussion question, or quick exit review.]

---
**Materials needed:** [list anything to prepare]
**Next rehearsal focus:** [one sentence]
```

## Timing Guidelines

- **30 min:** Warm-Up 5 min, Technique 10 min, Music 10 min, Cool-Down 5 min
- **45 min:** Warm-Up 8 min, Technique 12 min, Music 20 min, Cool-Down 5 min
- **50 min:** Warm-Up 10 min, Technique 15 min, Music 20 min, Cool-Down 5 min

## Notes

- Include specific things to say to students, not just what to do
- Flag any materials to prepare (worksheets, recordings, etc.)
- If "music in progress" is "none yet," substitute a sight-reading or unison exercise for the Music Work block
