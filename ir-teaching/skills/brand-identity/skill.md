---
name: brand-identity
description: >
  Use when generating IR materials that need consistent branding. Use this before creating
  ANY student packet, lesson plan, answer key, slide deck, exit ticket, or cover page.
  Visual brand identity for Mr. Burger's 10th grade Intensive Reading materials.
  Defines the design language, color system, typography hierarchy, and visual identity
  that ALL unit deliverables must follow — student packets, lesson plans, answer keys,
  slides, exit tickets, and cover pages. Reference this skill before generating any
  deliverable to ensure brand consistency across all units.
---

# Mr. Burger's IR — Brand Identity Guide

## Design Philosophy: "Structured Clarity"

Every piece of material that leaves Mr. Burger's classroom should feel like it came from the same source — clean, consistent, and meticulously crafted. Students should never have to relearn a layout. Teachers should never have to decode a format. The design serves the learning, not the other way around.

This philosophy is built on four commitments:

**Craftsmanship over decoration.** Every element on the page exists because it helps someone learn or teach. If it doesn't serve a purpose, it doesn't belong. No clipart, no decorative borders, no busy backgrounds. The care shows in the spacing, the alignment, the consistency — not in ornament.

**Predictability as a feature.** When a student opens Day 4 of any unit, they should immediately know where the bellringer is, where the organizer is, and where their writing space begins. This is achieved through rigid structural consistency: same fonts, same spacing, same section order, same component designs — every unit, every time.

**Accessibility first.** Design for the student with the weakest vision, the shortest attention span, and the most need for scaffolding. High contrast, large type, generous white space, and clear visual landmarks. If a design choice makes the page harder to scan for even one student, it's the wrong choice.

**Professional respect.** These are 10th graders, not elementary students. The materials should look like published workbooks — serious, clean, and worthy of their effort. No condescending visuals, no childish layouts. Professional design communicates that the work matters.

---

## Brand Color System

### Print Materials (Student Packets, Answer Keys, Exit Tickets)

All printed materials assume **grayscale printing only**. The color palette is built entirely around grays and black.

```
PRIMARY
  Text:               #000000 (black)
  Backgrounds:        #FFFFFF (white)

STRUCTURAL GRAYS (from darkest to lightest)
  Day header fill:    #E6E6E6 (light gray, ~10% black)
  I DO row fill:      #F0F0F0 (very light gray, ~6%)
  WE DO row fill:     #F7F7F7 (barely gray, ~3%)
  Sentence frame box: #F2F2F2 (light fill, ~5%)
  YOU DO rows:        #FFFFFF (white — clean, open)

BORDERS
  Primary (outer):    #000000 (black), 1pt
  Secondary (inner):  #CCCCCC (medium gray), 0.5pt
  Section separator:  #000000 (black), 1.5pt
  Day header block:   #000000 (black), 1pt all sides
```

**Rule:** Every gray shade has a distinct purpose. Never use a shade for two different meanings. Never introduce a new gray — if a component needs visual distinction, use borders or typography weight, not a new fill color.

### Digital Materials (Slides, Projected Content)

Slides and projected content may use **one accent color** in addition to the grayscale palette. This accent is used sparingly — timer tags, day numbers, and key callouts only.

```
ACCENT COLOR (slides only)
  Primary accent:     #2B5797 (navy blue — serious, readable on projector)
  Accent use:         Day numbers on separator slides, timer icons, key callouts
  Never use for:      Body text, backgrounds, borders, or anything students need to read on paper
```

### Color Rules

1. **No colored text** in any printed material — black only. Use bold, italic, or shading for emphasis.
2. **No color-dependent meaning** — every shaded element must also have a text label (e.g., "I DO" label + gray fill, never just gray fill alone).
3. **Maximum 2 fill shades per page** in print materials (the day header gray + one component gray).
4. **Accent color appears only on slides** — never in .md files.

---

## Typography System

### Font Family

**Arial** is the only font used across all deliverables. No exceptions.

- Arial is universally installed on all systems (Windows, Mac, Chromebook, Google Docs)
- Arial renders cleanly at small sizes and on projectors
- Arial has a complete weight family (Regular, Bold, Italic, Bold Italic)

**Never use:** Times New Roman, Calibri, Comic Sans, Helvetica, Poppins, Lora, or any decorative/serif font.

### Type Scale

```
STUDENT-FACING MATERIALS (Packets, Exit Tickets, Assessments)
  Level 1 — Day Header:      Arial Bold, 16pt
  Level 2 — Section Label:   Arial Bold, 14pt, ALL CAPS
  Level 3 — Body/Directions: Arial Regular, 12pt
  Level 4 — Table Text:      Arial Regular, 11pt
  Level 5 — Timer/Tag/Footer: Arial Italic, 10pt

TEACHER-FACING MATERIALS (Lesson Plans, Answer Keys)
  Level 1 — Day Header:      Arial Bold, 14pt (or Calibri Bold 14pt)
  Level 2 — Section Label:   Arial Bold, 12pt
  Level 3 — Body Text:       Arial Regular, 11pt (or Calibri 11pt)
  Level 4 — Notes/Asides:    Arial Italic, 10pt

SLIDES (Projected)
  Level 1 — Slide Title:     Arial Bold, 32pt+
  Level 2 — Section Label:   Arial Bold, 24pt
  Level 3 — Body Text:       Arial Regular, 20pt+
  Level 4 — Caption/Timer:   Arial Italic, 16pt
```

### Typography Rules

1. **Never go below 10pt** in any deliverable for any reason.
2. **Bold is for structure** (headers, labels, key action words in directions). Never bold entire paragraphs.
3. **Italic is for scaffolding** (I DO exemplar text, sentence starters, timer tags). Never italicize directions.
4. **ALL CAPS is for section labels only** ("BELLRINGER", "TEACHER-LED", "INDEPENDENT"). Never ALL CAPS body text.
5. **Underline is reserved for vocabulary target words** in bellringer sentences. Never underline for emphasis.
6. **Maximum 75 characters per line** for readability. If a line runs longer, adjust column width or margins.

---

## Spacing System

Consistent spacing is what separates a professional document from a word processor dump. These values are non-negotiable.

```
PAGE LAYOUT
  Paper size:         US Letter (8.5" × 11")
  Margins:            1.0" all sides (minimum 0.75" if content is tight)
  Content width:      6.5" (at 1" margins)

LINE SPACING
  Body text:          1.15 line spacing
  Tables/organizers:  Single (1.0)
  Slide body text:    1.5

PARAGRAPH SPACING
  Between sections (BR → TL → IND):  18pt minimum
  Between items within a section:     6pt
  After a section header:             6pt
  Before a section header:            12pt

TABLE SPACING
  Cell padding (all sides):           6pt minimum
  Minimum row height:                 0.75" (organizers — enough for handwriting)
  Writing line spacing:               0.4" between ruled lines

COMPONENT SPACING
  Between response lines:             0.4"
  Between MC answer choices:          6pt
  Between bellringer items:           12pt
  Between self-check items:           4pt
```

---

## Component Library

Every unit uses the same reusable components. These are defined in `teaching-templates` with ASCII mockups. Here is the master list with brand identity requirements:

| # | Component | Used In | Brand Requirements |
|---|-----------|---------|-------------------|
| 1 | Day Header Block | Every day page | #E6E6E6 fill, 1pt border, 16pt bold day number, 12pt benchmark line, name/date/period fields |
| 2 | Section Separator | Between BR/TL/IND | 1.5pt rule above, 14pt ALL CAPS bold label, 10pt italic timer right-aligned |
| 3 | Bellringer Block | Every day | 3 items, consistent MC formatting, bold target words, ¶ references |
| 4 | Graphic Organizer Table | Days 3-4 TL/IND | Alternating row shading, row labels, 0.75" min height, 3-col max |
| 5 | Writing Response Area | Days 3-6 | 1pt border, 0.4" ruled lines, 8+ lines for CR, 3+ for short answer |
| 6 | Sentence Frame Box | Days 1-4 discussion, Days 3-6 CR | #F2F2F2 fill, 0.5pt border, "Language to..." or CR-step label |
| 7 | Self-Check Box | End of IND sections | 0.75pt border, checkboxes, first-person action language |
| 8 | Need Help? Box | Bottom of IND sections | 0.75pt border, 4-step numbered scaffold chain |

**Critical:** These 8 components must look identical in every unit. If a new component is needed, define it here first before using it.

---

## Naming and Terminology

Consistent language is part of the brand. Use these terms exactly — never substitute synonyms.

### Section Names (Always)
| Always Use | Never Use |
|-----------|-----------|
| BELLRINGER | Warm-Up, Do Now, Bell Work, Opener |
| TEACHER-LED | Teacher Center, Small Group, Mini-Lesson, Direct Instruction |
| INDEPENDENT | Independent Center, Solo Work, Practice, Seatwork |
| TECHNOLOGY | Tech Center, Computer Time, Digital Station |

### Framework Names (Always)
| Always Use | Never Use |
|-----------|-----------|
| RACE (Restate-Answer-Cite-Explain) | RACES, RAC, RE |
| CER (Claim-Evidence-Reasoning) | CER paragraph, argumentative response |
| ACE (Answer-Cite-Explain) | Short ACE, mini-response |
| STOP (Silly-Tricky-Opposite-Proven) | Process of elimination, POE |
| CUBES | Annotation strategy, close reading strategy |

### Direction Language (Verb-First, Always)
| Pattern | Example |
|---------|---------|
| Read... | "Read paragraphs 3-5 silently." |
| Circle... | "Circle the context clues in each sentence." |
| Write... | "Write your response using the RACE format." |
| Complete... | "Complete rows 3 and 4 of the organizer." |
| Check... | "Check your work using the self-check box below." |
| Cross out... | "Cross out the two answers that are MOST wrong." |

**Rule:** Every direction starts with an action verb. Never start with "You will..." or "Students should..." or "In this activity..."

---

## Document Headers and Footers

### Student Packet Header (Day Pages)
The Day Header Block serves as the page header. No additional header needed.

### Student Packet Footer (Every Page)
```
[Unit Text Title] — Day [#] | [Benchmark Code] | Page [#] of [#]
```
- Arial 10pt, centered
- Consistent on every page

### Lesson Plan Header (Every Page)
```
[Unit Text Title] — Teacher Lesson Plan | [Benchmark Code]
```
- Calibri or Arial 10pt, left-aligned

### Lesson Plan Footer (Every Page)
```
Mr. Burger | 10th Grade Intensive Reading | Page [#]
```
- 10pt, right-aligned

### Answer Key Header (Every Page)
```
ANSWER KEY — [Unit Text Title] | [Benchmark Code]
```
- Arial Bold 10pt, left-aligned
- "ANSWER KEY" in bold to distinguish from student packet

### Slides Footer (Every Slide)
```
[Unit Text Title] — Day [#] | Mr. Burger | 10th Grade IR
```
- Arial 12pt, bottom-left of every slide

---

## Design Self-Critique Checklist

Before finalizing ANY deliverable, run this 5-point check (adapted from UX design critique frameworks):

### 1. First Impression Test (2 Seconds)
Open the document. Look at any page for 2 seconds, then look away.
- Could you identify which day it is?
- Could you identify which section (BR/TL/IND) you were in?
- Did anything feel cluttered or overwhelming?

If any answer is "no," the visual hierarchy needs work.

### 2. Consistency Scan
Flip through every page quickly.
- Do all day headers look identical?
- Do all section separators look identical?
- Are fonts, spacing, and shading consistent throughout?
- Does the packet look like it came from one source?

If anything looks "different" on one page, fix it.

### 3. Scannability Check
Hand the packet to someone unfamiliar with it.
- Can they find Day 3 in under 5 seconds?
- Can they find the Independent section on any page in under 3 seconds?
- Can they identify what to do without reading all directions?

If any answer is "no," add visual landmarks or improve section separation.

### 4. Accessibility Audit
- Is all text 10pt or larger?
- Is there sufficient contrast (black text on white/light gray backgrounds)?
- Does every shaded element also have a text label?
- Are lines 75 characters or fewer?
- Can a student with low vision navigate the page?

### 5. Craftsmanship Check
- Are all table borders aligned and consistent?
- Is spacing uniform (no random extra gaps or cramped areas)?
- Are all checkboxes the same size?
- Are all writing lines evenly spaced?
- Would you be proud to hand this to an administrator?

**If ANY check fails, revise before delivering.**

---

## Deliverable-Specific Brand Applications

### Student Packet (.md)
- Full brand system applies (all design tokens, all 8 components, all typography levels)
- Grayscale formatting
- 1 front/back page per day budget when printed
- Must pass all 5 self-critique checks
- See `teaching-templates` for complete component specifications
- See `student-packet-design-guide` for detailed layout patterns

### Lesson Plan (.md)
- Teacher-facing typography scale (clear hierarchy)
- Clean section breaks between days
- Arial-equivalent formatting
- Bold key timing and activity names for quick scanning
- No decorative elements
- Include Mr. Burger footer metadata

### Answer Key (.md)
- Mirror student packet structure exactly (day-by-day)
- "ANSWER KEY" header in bold at top to prevent mix-ups
- Correct answers in **bold** for quick teacher scanning
- Use same organizer tables as student packet with exemplar responses filled in
- Visual distinction for exemplar rows

### Teacher Slides (.pptx)
- White background, black text
- Navy accent (#2B5797) for day numbers and key callouts only
- Arial only — no system theme fonts
- No animations, no transitions, no busy backgrounds
- One slide per activity segment
- Content matches lesson plan and student packet word-for-word
- Footer on every slide

### Exit Tickets (.md)
- Half-page format (2 exit tickets per printed page)
- Same typography as student packet (Arial-equivalent, same type scale)
- Include name/date/period line
- Bordered box around entire ticket
- 1-2 questions aligned to daily objective
- Match student packet visual style

### Cover Pages (.md)
- Unit title: Bold, 24pt-equivalent, centered
- Benchmark focus in student-friendly language
- Days 1-6 label
- Student name/date/period fields
- Practice work note: "This is PRACTICE work..."
- Table of contents listing each day's focus
- Clean, uncluttered — this is the first thing students see

---

## Implementation Notes for Document Generators

When generating Markdown (.md) files, these brand values translate to specific formatting parameters. This design system is applied through consistent Markdown formatting and optional CSS styling when the files are converted to PDF or other formats.

---

*This brand identity guide is the single source of truth for all visual design decisions in Mr. Burger's IR materials. When any other skill or agent references "brand guidelines" or "visual standards," they mean THIS document.*

*Last Updated: 2026-03-08*
*Version: 1.0*
