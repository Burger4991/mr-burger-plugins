---
name: student-packet-design-guide
description: >
  Formatting and visual design standards for all student-facing materials in 10th grade
  Intensive Reading. Covers typography, layout, sentence frame boxes, organizer structure,
  and visual hierarchy. Referenced by student-packet-builder agent during builds.
  Use when creating or reviewing any student packet, exit ticket, or assessment.
---

# Student Packet Design Guide

## Purpose

This skill defines the visual design and formatting standards for all student-facing materials. Every student packet, exit ticket, assessment, and handout should follow these specs for consistency and accessibility.

**IMPORTANT:** This skill works in concert with two other design-related skills:
- **`brand-identity`** — The master brand guide. Defines the design philosophy, complete color system, typography hierarchy, spacing system, terminology standards, and design self-critique checklist for ALL deliverables (not just packets). **Read brand-identity FIRST** for the foundational design decisions.
- **`teaching-templates`** — Defines the 8 reusable components (Day Header Block, Section Separator, Bellringer Block, Organizer Table, Writing Area, Sentence Frame Box, Self-Check Box, Need Help Box) with exact design token values and docx-js implementation code.

This skill (student-packet-design-guide) provides the **detailed layout patterns and organizer structures** specific to student packets. When in doubt about a value (font size, spacing, color), defer to `brand-identity` as the single source of truth.

**Design philosophy:** IR student materials should be closer to the scaffolding level of Read 180 RealBook (heavy structure, sentence frames, visual supports) than Savvas Realize (grade-level, less scaffolding). However, the layout should be slightly denser than Read 180 to fit within the 1 front/back page per day budget.

**Reference textbooks:**
- **Read 180 RealBook Stage C** — scaffolding model (sentence frames, fill-in-the-blank, visual concept maps, Key Idea boxes)
- **Savvas Realize 10th Grade** — design patterns (color-coded section headers, margin vocabulary, Close Read sidebars, Build Insight question progressions)

---

## Typography Standards

### Font
- **Font family:** Arial (primary) or Helvetica (fallback)
- **Never use:** Times New Roman, Calibri, Comic Sans, decorative fonts

### Sizes (must match `brand-identity` type scale)
| Element | Size | Weight |
|---------|------|--------|
| Day header ("DAY 1 — Focus Title") | 16pt | Bold |
| Section headers (BELLRINGER, TEACHER-LED, INDEPENDENT) | 14pt | Bold, ALL CAPS |
| Body text / directions / questions | 12pt | Regular |
| Table text | 11pt | Regular |
| Sentence frames and starters | 12pt | Italic |
| Timer tags, footer, margin notes | 10pt | Italic |

### Spacing (must match `brand-identity` spacing system)
- **Line spacing:** 1.15 (body text, directions, questions); single for tables
- **Between sections (BR → TL → IND):** 18pt minimum
- **Between items within a section:** 6pt
- **Before a section header:** 12pt
- **After a section header:** 6pt

### Margins
- **All margins:** 1 inch (top, bottom, left, right)
- **Exception:** If content is extremely tight on a page, margins may be reduced to 0.75" — but 1" is the default

---

## Page Layout Standards

### Page Budget
- **1 front/back page per day** (2 sides of a single sheet)
- **6-day unit = 6 sheets maximum** for the student packet (not counting the text passage itself)
- If content exceeds the budget, cut lower-priority activities first (see prioritization below)

### Content Prioritization (What to Cut First)
When a day's activities exceed 1 front/back page:
1. Cut extension/bonus activities first
2. Reduce white space (but never below readability)
3. Shorten directions (but keep numbered steps)
4. Reduce response line count (but keep minimum 3 lines per written response)
5. **Never cut:** Bellringer, organizer rows, sentence frames, STOP/CR response space

### Visual Hierarchy
Every page should have a clear top-to-bottom visual flow. See `teaching-templates` for the 8 reusable components that implement this hierarchy.

```
┌──────────────────────────────────────────────────┐
│  DAY [#] — [Focus Title]           (16pt bold)   │
│  Benchmark: [code] — [description] (12pt)        │
│  Name: _____________ Date: ______ Period: ___    │
└──────────────────────────────────────────────────┘
                                        ↑ #E6E6E6 fill, 1pt border

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ (1.5pt rule)
CONTEXT CLUES BELLRINGER — Day [#]       ⏱ 4 min
─────────────────────────────────────── (14pt ALL CAPS bold)
[Bellringer content — 3 items]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ (1.5pt rule)
TEACHER-LED                              ⏱ 20 min
───────────────────────────────────────
[Organizer or guided activity]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ (1.5pt rule)
INDEPENDENT                              ⏱ 20 min
───────────────────────────────────────
[Self-running task with micro-step directions]
[Self-Check Box + Need Help? Box at bottom]

─────────────────────────────────────────────────
[Unit Title] — Day [#] | [Benchmark] | Page [#]   (10pt footer)
```

### Section Dividers
- Use a **horizontal rule** (1pt line, full width) between major sections
- Add **6pt space** above and below each rule
- Section headers should be **14pt bold** with the section name

### White Space
- Maintain adequate white space between sections — don't cram
- Response areas should have **minimum 3 lines** (approximately 1 inch) for written responses
- Organizer cells should have enough space for 1-2 sentences minimum

---

## Sentence Frame Boxes

### Two Types of Frame Boxes

**Type 1: "Language to..." Boxes (for discussion and partner talk)**
Modeled after Read 180's "Language to React / Discuss / Compare" format. Used during partner work, group discussion, and oral rehearsal.

```
┌──────────────────────────────────────────┐
│  💬 LANGUAGE TO DISCUSS:                 │
│                                          │
│  • "I think the author is saying         │
│    that __________ because __________."  │
│                                          │
│  • "I agree/disagree with __________     │
│    because __________."                  │
│                                          │
│  • "The text supports this because       │
│    in paragraph ___, it says ________."  │
└──────────────────────────────────────────┘
```

**Formatting specs:**
- Bordered box with 1pt solid border
- Light gray or light blue background fill (optional, for visual distinction)
- Header in **bold** with discussion icon or label
- 2-3 sentence frames per box
- Placed directly before the partner/discussion activity
- Blanks shown as underscores: __________

**When to use:** Days 1-4 during partner talk, We Do discussions, collaborative annotation, and oral rehearsal before writing.

---

**Type 2: CR-Step Frames (for written responses)**
Labeled by RACE or CER step. Used directly above the response space for written constructed responses.

```
┌──────────────────────────────────────────┐
│  ✏️ TO WRITE YOUR RESPONSE:              │
│                                          │
│  R (Restate): "The question is asking    │
│    about __________. [Key words] ______."│
│                                          │
│  A (Answer): "__________."               │
│                                          │
│  C (Cite): "In paragraph ___,           │
│    the text states, '__________.' "      │
│                                          │
│  E (Explain): "This shows that ________  │
│    because __________."                  │
└──────────────────────────────────────────┘
```

**Formatting specs:**
- Bordered box with 1pt solid border
- No background fill (keep it clean against the white response area below)
- Each step labeled with its letter abbreviation in **bold**
- Placed directly above the lined response space
- Frame complexity matches the current ACE/RACE tier:
  - **Lite:** Show R + A only
  - **Standard:** Show R + A + C
  - **Full:** Show R + A + C + E (or C + E + R for CER units)

**When to use:** Days 3-6 for any written CR response (organizer analysis rows, exit tickets, assessment CR prompts).

---

### Frame Progression Across 6-Day Cycle

| Days | Discussion Frames | CR Writing Frames |
|------|-------------------|-------------------|
| Days 1-2 | Full "Language to..." boxes for all partner talk | R + A frames only (Restate practice) |
| Days 3-4 | "Language to..." boxes for We Do discussion | Full CR frames at current tier (R+A+C or R+A+C+E) |
| Days 5-6 | No discussion frames (independent work) | No CR frames (independent writing) — ESOL students keep frames |

---

## Visual Concept Maps and Organizers

### Organizer Structure Rules

**Column count:** Flexible by benchmark, but always capped at **3 columns maximum**.
- Some benchmarks need 2 columns (e.g., Evidence | Explanation)
- Some benchmarks need 3 columns (e.g., Evidence | Technique | Effect)
- Never exceed 3 columns — if the benchmark requires more elements, stack them into rows or use a multi-step format instead

**Row structure:** 4-5 rows with gradual release labels.

| Row | Label | Scaffolding |
|-----|-------|-------------|
| Row 1 | **I Do (Teacher models)** | Pre-filled by teacher during modeling |
| Row 2 | **We Do (Class together)** | Students fill with teacher guidance |
| Row 3 | **You Do w/ Partner** | Students complete with a partner |
| Row 4 | **You Do (Independent)** | Students complete alone |
| Row 5 | **You Do (Independent)** | Optional 5th row for extension or additional practice |

**Cell sizing:**
- Minimum cell height: ~0.75 inches (enough for 1-2 sentences)
- Column widths proportional to content (Evidence columns wider, label columns narrower)
- Use table borders (1pt solid) for all cells

**Pre-filled I Do row:**
- The I Do row should ALWAYS be pre-filled with a model response
- Use a slightly different background (light gray) to distinguish it from student rows
- Students annotate/study this row, not fill it in

### Concept Map Format

For vocabulary or concept-connection activities, use a visual radial map modeled after both Read 180's inference organizers and Savvas's Word Network:

```
┌────────────────┐     ┌────────────────┐
│  [Related      │     │  [Related      │
│   Concept 1]   │     │   Concept 2]   │
└───────┬────────┘     └────────┬───────┘
        │                      │
        └──────┐    ┌──────────┘
               │    │
          ┌────┴────┴────┐
          │  CENTRAL     │
          │  CONCEPT     │
          └────┬────┬────┘
               │    │
        ┌──────┘    └──────────┐
        │                      │
┌───────┴────────┐     ┌───────┴────────┐
│  [Related      │     │  [Related      │
│   Concept 3]   │     │   Concept 4]   │
└────────────────┘     └────────────────┘
```

**When to use:** Vocabulary connections, theme mapping, character relationship mapping.
**When NOT to use:** Evidence-based analysis (use table organizers instead).

### Two-Column Inference Organizer

Modeled after Read 180's inference chart. Use for reading comprehension and inference tasks:

```
┌─────────────────────┬─────────────────────┐
│ WHAT THE TEXT SAYS   │ WHAT I ALREADY KNOW │
│                      │                     │
│ (Direct quote or     │ (Background         │
│  detail from text)   │  knowledge)         │
├─────────────────────┼─────────────────────┤
│                      │                     │
├─────────────────────┴─────────────────────┤
│            ↓ MY INFERENCE ↓               │
│                                           │
│ (Combine text evidence + prior knowledge) │
└───────────────────────────────────────────┘
```

---

## Bellringer Section Design

Every day starts with a bellringer. The bellringer section should be visually distinct and quick to locate.

### Bellringer Layout

```
┌─────────────────────────────────────────────┐
│  📖 BELLRINGER — Day [#]          (5 min)   │
│                                             │
│  WORD 1: __________                         │
│  Read the sentence. Circle the context      │
│  clues. Choose the best meaning.            │
│                                             │
│  "[Sentence with word in bold]"             │
│                                             │
│  ○ A. [choice]                              │
│  ○ B. [choice]                              │
│  ○ C. [choice]                              │
│  ○ D. [choice]                              │
│                                             │
│  WORD 2: __________                         │
│  [Same format as above]                     │
│                                             │
│  WORD 3: __________ (Written Response)      │
│  Read the sentence. Write the meaning       │
│  using context clues.                       │
│                                             │
│  "[Sentence with word in bold]"             │
│                                             │
│  This word means: _________________________ │
│  Context clues I used: ____________________ │
└─────────────────────────────────────────────┘
```

**Formatting specs:**
- Bordered box around entire bellringer section
- Time estimate in parentheses (5 min)
- Words 1-2: Multiple choice (4 options, circle format)
- Word 3: Written response (definition + context clue identification)
- Bold the target word in each sentence
- Adequate space between words (don't cram all 3 onto half a page)

---

## Assessment Section Design

### Multiple Choice Format

```
**1. [Question stem]** (paragraph [#])

   ○ A. [Silly choice]
   ○ B. [Tricky choice]
   ○ C. [Opposite choice]
   ○ D. [Proven choice]

   My answer: _____ Why it's Proven: _________________________
   ___________________________________________________________
```

- Open circles (○) for answer bubbles — not filled, not checkboxes
- Question stem in **bold**
- Paragraph reference in parentheses
- STOP analysis line: "My answer: _____ Why it's Proven: _____" (Simplified STOP mode)
- Full STOP mode (once per unit): Add 4 lines for S/T/O/P labeling with justification

### Constructed Response Format

```
**[CR Prompt — always benchmark-aligned]**

┌──────────────────────────────────────────┐
│  ✏️ TO WRITE YOUR RESPONSE:              │
│  [CR frames at current tier level]       │
└──────────────────────────────────────────┘

R (Restate): _________________________________________

A (Answer): __________________________________________

C (Cite): "___________________________________________
________________________________" (paragraph _____)

E (Explain): _________________________________________
__________________________________________________________
__________________________________________________________

Score: _____ / 4 points
```

- CR frame box directly above response lines
- Each RACE/CER step on its own labeled line
- Minimum 2 lines per step (3 for Explain)
- Score line at bottom
- Frame complexity matches current tier (hide steps not yet introduced)

---

## ESOL Visual Supports

For ESOL-modified packets (see esol-adapter agent for full adaptation process):

### "Need Help?" Boxes
Small margin boxes with L1 translations or cognate bridges:

```
┌─────────────────┐
│ 💡 NEED HELP?   │
│                 │
│ persevere =     │
│ perseverar (Sp) │
│                 │
│ to keep trying  │
│ even when it's  │
│ hard            │
└─────────────────┘
```

- 11pt font
- Positioned in margin next to relevant activity
- Include L1 translation (Spanish) + simple English definition
- Use for Tier 2/3 vocabulary at point of use

### Direction Simplification
For ESOL Levels 1-3, simplify directions using this format:

```
DIRECTIONS:
1. READ the passage on page 2.
2. UNDERLINE key details.
3. ANSWER questions 1-3.
```

- Numbered steps (maximum 1 action per step)
- Action verbs in **BOLD CAPS**
- Short sentences (under 10 words each)

---

## Color and Visual Coding

### When Creating in .md
Since student packets are .md files, use these visual coding methods:

- **Section headers:** Bold, 14pt, with a horizontal rule above
- **Frame boxes:** 1pt solid border, optional light fill
- **Organizer tables:** 1pt borders, header row in bold with light gray fill
- **I Do rows:** Light gray cell fill to distinguish from student rows
- **Bellringer section:** Bordered box around entire section
- **Important notes:** Bold text, or boxed callout

### What NOT to Do (see `brand-identity` for the complete list)
- Don't rely on color/shading alone to convey meaning — always pair with a text label
- Don't use colored text for emphasis — use **bold** instead
- Don't use more than 2 fill shades per page (day header gray + one component gray)
- Don't use decorative borders, clip art, or emojis in headers
- Don't use different fonts within the same document (Arial only)
- Don't exceed 75 characters per line
- Don't go below 10pt for any text element
- Don't use inconsistent terminology (see `brand-identity` naming standards)

---

## Page Footer Standard

Every page should include a footer with:

```
[Unit Name] — Day [#] | [Benchmark Code] | Page [#] of [#]
```

Example:
```
Story of an Hour — Day 3 | ELA.10.R.1.2 | Page 3 of 6
```

- 10pt Arial
- Centered or right-aligned
- Consistent across all pages in the packet

---

## Quick Reference: Design Checklist

Before finalizing any student packet, verify:

- [ ] Font is Arial, 12pt body / 14pt headers
- [ ] Margins are 1 inch on all sides
- [ ] Line spacing is 1.15
- [ ] Each day fits on 1 front/back page (2 sides)
- [ ] Bellringer section is boxed and clearly labeled
- [ ] Organizer has max 3 columns, 4-5 rows with gradual release labels
- [ ] I Do row is pre-filled with model response (gray fill)
- [ ] "Language to..." boxes present for Days 1-4 discussion activities
- [ ] CR-step frames present for Days 3-6 written responses (at current tier)
- [ ] ESOL "Need Help?" boxes in margins for key vocabulary
- [ ] Directions are numbered steps with bolded action verbs
- [ ] Response areas have minimum 3 lines
- [ ] Footer present on every page with unit name, day, benchmark, page number
- [ ] No decorative fonts, clip art, or colored text
- [ ] Assessment MC uses open circles (○) with STOP analysis line

---

*Reference textbooks: Read 180 RealBook Stage C (scaffolding model), Savvas Realize 10th Grade Unit 1 (design patterns)*
*Last Updated: 2026-03-08*
*Version: 2.0 - Aligned to brand-identity system, updated type scale (16pt day headers), added cross-references to brand-identity and teaching-templates*
