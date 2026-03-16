---
name: interactive-lesson-builder
description: >
  Build interactive HTML lesson websites for Intensive Reading units that run on Promethean boards.
  Includes day-tab navigation, STOP protocol on all MC questions, CUBES annotation tools, timer,
  and teacher-controlled engagement features. Use when generating interactive lesson HTML files,
  building Promethean board lessons, or creating self-contained HTML lesson websites for any IR unit.
---

# Interactive Lesson Builder for Intensive Reading (v5 — Shakuntala Architecture)

---

## Frontmatter

**Name:** Interactive Lesson Builder for Intensive Reading (IR) — v5
**Description:** Generates a single self-contained interactive HTML website per IR unit. Replaces PowerPoint for teacher-led projection on the Promethean board. Supports both 4-day test prep and 6-day literary analysis units. Uses day-tab + section-pill navigation with topbar-controlled toggles (CUBES, Timer, Passage, Engage overlay). All interactions teacher-controlled. STOP protocol on every MC choice.
**Target Users:** 10th grade Intensive Reading teachers
**Output:** One self-contained `.html` file per unit (all CSS + JS inline, no external dependencies, works offline)

---

## Purpose

This skill generates interactive lesson-control websites that mirror the student packet, support real-time pacing and facilitation, and provide teachers with:

1. **Day-tab navigation** — horizontal tabs across the top, one per day
2. **Section-pill navigation** — colored pill buttons below day tabs for Bellringer / Teacher-Led / Independent / Closure
3. **STOP Protocol on MC choices** — Every MC choice has a STOP badge (Silly / Tricky / Opposite / Proven) that teachers cycle through with a single click
4. **Teacher-controlled answer reveal** — "Show Answer" / "Hide Answer" button on every MC question (replaces student click-to-lock)
5. **Topbar toggle buttons** — Split View, Passage, CUBES, Timer, Engage, Notes, Mode
6. **CUBES annotation bar** — Slide-down bar below section pills with 5 annotation tools (Circle, Underline, Box, Evidence, Summarize) + Clear All
7. **Annotations across entire website** — Not just passage; users can annotate any text on the page when CUBES mode is active
8. **Timer bar** — Slide-down bar with countdown, Start/Pause, Reset, and preset buttons
9. **Split view** — Passage (45%) + content (55%) side-by-side with independent scrolling
10. **Engage overlay** — Consolidated dialog containing discussion prompts, response tally (A/B/C/D), quick polls, and engagement presets
11. **Teacher notes overlay** — Press T to see per-view facilitation scripts (hidden from students)
12. **Dark/light mode** — dark default for Promethean boards, light toggle available
13. **Keyboard navigation** — ← → arrows move between sections, T = Notes, C = CUBES, R = Timer, P = Passage, E = Engage, Esc = Close all
14. **Interactive checklists** — click-to-check annotation requirements and self-assessment items

All content is self-contained (no external libraries, no internet required). Font sizes are readable from 75+ feet away on a Promethean board.

---

## File Naming

**Output filename pattern:**
`[TextTitle]_D[Start]-[End]_[UnitType]_Interactive_v[N].html`

**Examples:**
- `Shakuntala_D1-4_TestPrep_Interactive_v5.html`
- `Shakuntala_D1-6_InteractiveLesson_v5_20260309.html`

**Storage location:**
Save to the unit folder alongside other deliverables (lesson plan, student packet, answer key).

---

## Unit Types

### 4-Day Test Prep Unit
- **Days:** 4
- **Writing framework:** CER (Claim–Evidence–Reasoning)
- **Annotation system:** CUBES (used in topbar bar, not static sidebar)
- **Vocabulary:** 3 words, progressive bellringer format (Day 1: fill-blank, Day 2: context clues, Day 3: application, Day 4: quiz)
- **Core activity:** MC with STOP badges, teacher-controlled reveal, CER justification, wrong-answer analysis, extended CER response
- **Section labels:** Bellringer / Teacher-Led / Independent / Closure

### 6-Day Literary Analysis Unit
- **Days:** 6
- **Writing framework:** ACE (Answer–Cite–Explain)
- **Annotation system:** CUBES (topbar-controlled)
- **Vocabulary:** 18 words (3 per day), bellringer format progression
- **Core activity:** Graphic organizer with gradual release (I DO / WE DO / YOU DO), STOP protocol on MC, ACE writing
- **Section labels:** Bellringer / Teacher-Led / Independent / Closure (or Wrap-Up)

---

## Generation Workflow

### Prerequisites
- Teacher has completed the lesson plan (uploaded or in context)
- Teacher has student packet (uploaded or in context)
- Teacher has the passage text with assessment questions (if test prep)

### Step 1: Auto-Extract Content
Read all uploaded files and extract:
- Unit title, benchmark codes (e.g., R.1.1, R.1.2)
- Number of days (4 or 6) → determines unit type
- Writing framework (CER or ACE)
- Annotation system (CUBES)
- Vocabulary words with definitions and passage context
- Bellringer questions per day (from student packet)
- Teacher-Led content per day (from lesson plan) — extract phase labels (I DO, WE DO, YOU DO)
- Independent activity content per day (from student packet)
- Closure/exit ticket content per day
- Assessment questions with answer choices and correct answers
- CER/ACE model responses and justifications (from answer key or lesson plan)

### Step 2: Build — No Interview Needed
Do NOT ask the teacher 5 questions. Extract everything from the uploaded documents. If critical information is missing, ask ONE targeted question. Otherwise, generate directly.

### Step 3: Generate the HTML
Build a single self-contained HTML file following the architecture below.

### Step 4: Verify
Run a validation check:
- All days render (check DATA object has all day keys)
- All 4 sections per day have content (bell, tl, ind, closure)
- Teacher notes exist for every view (TEACHER_NOTES object has all d{day}-{section} entries)
- EVERY MC choice has a STOP badge (no exceptions)
- EVERY MC question has a "Show Answer" / "Hide Answer" button (teacher-controlled)
- Timer, CUBES bar, Passage toggle, Engage overlay all functional
- Keyboard navigation works (no shortcuts fire in text inputs)
- Split view works when both passage and content are visible
- Annotations persist when CUBES bar is toggled on/off
- passageInitialized flag prevents annotation wipe during navigation

---

## Website Architecture

### App Shell Layout (top to bottom)

```
┌──────────────────────────────────────────────────────────────┐
│ TOPBAR: [badges] [unit title]   [Split][Passage][CUBES][Timer][Engage][Notes][Mode] │
├──────────────────────────────────────────────────────────────┤
│ DAY BAR: [Day 1] [Day 2] [Day 3] [Day 4]                     │
├──────────────────────────────────────────────────────────────┤
│ SECTION BAR: [🔔 Bell] [📘 Teacher-Led] [✏️ Independent] [🏁 Closure]   │
├──────────────────────────────────────────────────────────────┤
│ CUBES BAR (slide-down, hidden by default)                   │
├──────────────────────────────────────────────────────────────┤
│ TIMER BAR (slide-down, hidden by default)                   │
├──────────────────────────────────────────────────────────────┤
│ ┌─PASSAGE (45%, split mode)──┐ ┌─CONTENT (55%)────┐         │
│ │ Scrollable passage text    │ │ Scrollable lesson │         │
│ │ (with annotations)         │ │ content           │         │
│ └──────────────────────────────┘ └─────────────────┘         │
├──────────────────────────────────────────────────────────────┤
│ FOOTER: keyboard hints                         Day X · Section │
└──────────────────────────────────────────────────────────────┘
```

**Fixed elements:** Topbar, day bar, section bar, CUBES bar (when shown), timer bar (when shown), footer (all `flex-shrink: 0`)
**Scrollable:** Content area only (`flex: 1; overflow-y: auto`)

### Navigation Model

- **Day tabs** — click to switch day (resets to Bellringer section)
- **Section pills** — click to switch section within current day
- **Topbar toggles** — split view, passage, CUBES, timer, engage, notes, mode
- **Keyboard** — ← → arrows move through sections sequentially across days
- **State:** `currentDay` (1-based), `currentSection` (0-3), `annoTool` (active CUBES tool), `annotationMode` (boolean)

### Section Types (index 0–3)

| Index | Name | Icon | Color | Render Function |
|-------|------|------|-------|-----------------|
| 0 | Bellringer | 🔔 | Orange | `renderBell()` |
| 1 | Teacher-Led | 📘 | Blue | `renderTL()` |
| 2 | Independent | ✏️ | Green | `renderInd()` |
| 3 | Closure | 🏁 | Teal | `renderClosure()` |

---

## Design System

### Color Tokens (CSS Custom Properties)

```css
:root {
  --bg: #0f172a;        /* dark background */
  --card: #1e293b;      /* card background */
  --card-hover: #334155; /* hover/secondary bg */
  --border: #334155;     /* borders */
  --text: #f1f5f9;       /* primary text */
  --muted: #94a3b8;      /* secondary text */
  --blue: #3b82f6;       /* Teacher-Led, claims, active states, CUBES Evidence */
  --green: #22c55e;      /* correct, Independent, CUBES Summarize */
  --orange: #f59e0b;     /* Bellringer, timer, reasoning, STOP T badge */
  --red: #ef4444;        /* incorrect, wrong answers, STOP S badge */
  --purple: #a855f7;     /* margin notes, badges, CUBES Evidence badge */
  --yellow: #eab308;     /* secondary highlights, STOP T badge */
  --teal: #14b8a6;       /* Closure, badges */
  --shadow: 0 4px 24px rgba(0,0,0,0.3);
  --radius: 12px;
}

.light-mode {
  --bg: #f8fafc;
  --card: #ffffff;
  --card-hover: #f1f5f9;
  --border: #e2e8f0;
  --text: #1e293b;
  --muted: #64748b;
  --shadow: 0 4px 24px rgba(0,0,0,0.06);
}
```

### Typography
- **Font:** `'Segoe UI', system-ui, -apple-system, sans-serif`
- **Line height:** 1.65 base, 1.8 for content blocks
- **Section headers:** 1.5rem, font-weight 800
- **Card titles:** 1.2rem, font-weight 700
- **Body text:** 1.05rem for readability from distance
- **Timer display:** 4.5rem, font-weight 800, tabular-nums
- **Badges:** 0.72rem, font-weight 700, letter-spacing 0.4px
- **STOP badge text:** 0.85rem, font-weight 800

### Core CSS Classes

| Class | Purpose |
|-------|---------|
| `.app` | Flex column, height 100vh |
| `.topbar` | Fixed top bar with badges and toggle buttons |
| `.topbar-right` | Flexbox container for topbar buttons |
| `.tb-btn` | Toggle button (inactive state) |
| `.tb-btn.active` | Toggle button (active state) |
| `.day-bar` | Day tab container |
| `.day-tab` / `.day-tab.active` | Individual day tabs, active = blue bottom border |
| `.section-bar` | Section pill container |
| `.pill` / `.pill.active` | Section pills, active = filled with section color |
| `.cubes-bar` / `.cubes-bar.show` | CUBES tool bar (slide-down) |
| `.cb-tool` / `.cb-tool.active` | Individual CUBES tools |
| `.cb-clear` | Clear All Annotations button |
| `.timer-bar` / `.timer-bar.show` | Timer control bar (slide-down) |
| `.timer-display` | Large countdown display |
| `.tmr-btn` | Timer control button |
| `.content` | Scrollable content area |
| `.split-view .passage-panel` / `.split-view .content` | Split view containers (45%/55%) |
| `.card` | Standard content card |
| `.timer-card` | Gradient border bellringer timer |
| `.vocab-card` | Left-border orange vocabulary entry |
| `.mc` / `.mc-choice` | MC question container and choices |
| `.mc-choice.correct` / `.mc-choice.incorrect` | Post-reveal states |
| `.stop-badge` / `.stop-badge.stop-s/t/o/p` | STOP badge with color states |
| `.reveal-btn` / `.revealed` | Teacher reveal toggle + hidden content |
| `.cer-block` / `.cer-claim` / `.cer-evidence` / `.cer-reasoning` | CER display blocks |
| `.anno-row` / `.anno-circle` / `.anno-box` / `.anno-underline` / `.anno-evidence` / `.anno-summarize` | Annotation guide rows |
| `.q-card` / `.q-num` / `.q-stem` | Assessment question display |
| `.wrong-row` / `.wrong-grid` | Wrong-answer analysis |
| `.highlight-box` / `.hb-blue` / `.hb-green` / `.hb-orange` / `.hb-purple` | Colored highlight boxes |
| `.passage-box` | Excerpt display with left border |
| `.passage-panel` | Right sidebar for passage text (split view) |
| `.frame-box` | CER/ACE sentence frames |
| `.phase-header` / `.phase-blue` / `.phase-green` / `.phase-orange` | I DO / WE DO / YOU DO accordion headers |
| `.check-group` / `.check-item` | Interactive checklist |
| `.celebration` | Unit-complete celebration card |
| `.notes-overlay` / `.notes-content` | Teacher notes overlay |
| `.engage-overlay` / `.engage-content` | Engage discussion overlay |
| `.tally-section` / `.tally-btn` / `.tally-bar` | Response tally system (inside Engage) |
| `.poll-item` | Individual poll entry |
| `.foot` | Fixed footer with keyboard hints |
| `mark.mark-circle` / `mark.mark-underline` / `mark.mark-box` / `mark.mark-evidence` / `mark.mark-summarize` | Global annotation marks |

---

## CSS for Annotations & STOP Badges

### STOP Badge Styling
```css
.stop-badge {
  min-width: 36px;
  min-height: 36px;
  border-radius: 6px;
  border: 2px solid var(--border);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.15s;
  margin-left: auto;
  flex-shrink: 0;
}

.stop-badge.stop-s {
  background: var(--red);
  color: #fff;
  border-color: var(--red);
}

.stop-badge.stop-t {
  background: var(--yellow);
  color: #000;
  border-color: var(--yellow);
}

.stop-badge.stop-o {
  background: var(--orange);
  color: #fff;
  border-color: var(--orange);
}

.stop-badge.stop-p {
  background: var(--green);
  color: #fff;
  border-color: var(--green);
}
```

### Global Annotation Marks
```css
mark.mark-circle {
  background-color: rgba(59, 130, 246, 0.4);
  color: inherit;
  border-radius: 4px;
  padding: 0.1rem 0.2rem;
}

mark.mark-underline {
  text-decoration: underline;
  text-decoration-color: rgba(245, 158, 11, 0.6);
  text-decoration-thickness: 3px;
  background: transparent;
}

mark.mark-box {
  border: 2px solid rgba(34, 197, 94, 0.6);
  background: transparent;
  border-radius: 4px;
  padding: 0.1rem 0.2rem;
}

mark.mark-evidence {
  background-color: rgba(168, 85, 247, 0.4);
  color: inherit;
  border-radius: 4px;
  padding: 0.1rem 0.2rem;
}

mark.mark-summarize {
  background-color: rgba(239, 68, 68, 0.4);
  color: inherit;
  border-radius: 4px;
  padding: 0.1rem 0.2rem;
}
```

### CUBES Bar Styling
```css
.cubes-bar {
  display: none;
  padding: 0.6rem 1.5rem;
  background: rgba(59, 130, 246, 0.08);
  border-bottom: 2px solid var(--blue);
  flex-shrink: 0;
  animation: slideDown 0.2s ease;
}

.cubes-bar.show {
  display: block;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Timer Bar Styling
```css
.timer-bar {
  display: none;
  padding: 1rem 1.5rem;
  background: rgba(245, 158, 11, 0.08);
  border-bottom: 2px solid var(--orange);
  flex-shrink: 0;
  animation: slideDown 0.2s ease;
}

.timer-bar.show {
  display: block;
}
```

### Split View Styling
```css
.split-view {
  display: flex;
  gap: 1rem;
  align-items: stretch;
}

.split-view .passage-panel {
  width: 45%;
  border-right: 1px solid var(--border);
  padding-right: 1rem;
  overflow-y: auto;
}

.split-view .content {
  width: 55%;
  overflow-y: auto;
}
```

---

## JavaScript Architecture

### State Variables
```javascript
let currentDay = 1;         // 1-based day number
let currentSection = 0;     // 0=Bell, 1=TL, 2=Ind, 3=Closure
let annoTool = 'circle';    // default CUBES tool (not null!)
let annotationMode = false; // global annotation toggle
let passageInitialized = false; // prevents render() from wiping annotations
let timerSec = 300;         // 5 minutes default
let timerRunning = false;
let timerInterval = null;
let pollVotes = [0, 0, 0, 0]; // A/B/C/D tallies
let tally = { A: 0, B: 0, C: 0, D: 0 };
```

### Constants
```javascript
const SEC_NAMES = ['Bellringer', 'Teacher-Led', 'Independent', 'Closure'];
const SEC_ICONS = ['🔔', '📘', '✏️', '🏁'];
const SEC_KEYS = ['bell', 'tl', 'ind', 'closure'];
const COLORS = {
  bell: '#f59e0b',      // orange
  tl: '#3b82f6',        // blue
  ind: '#22c55e',       // green
  closure: '#14b8a6'    // teal
};
```

### DATA Object Pattern

The `DATA` object is the single source of truth for all content. It is keyed by day number (1-based), with each day containing four section keys. Content for TL/Ind/Closure is HTML string format (not step objects):

```javascript
const DATA = {
  1: {
    bell: {
      title: 'Day 1 Bellringer — [Description] ([Time])',
      intro: 'Instructions text',
      passage: '...',  // optional passage excerpt for context
      items: [
        {
          stem: 'Question text with __________ blank',
          opts: [
            { l: 'A', t: 'answer text', c: false },
            { l: 'B', t: 'answer text', c: true },  // c:true = correct
            { l: 'C', t: 'answer text', c: false },
            { l: 'D', t: 'answer text', c: false }
          ]
        }
      ]
    },
    tl: {
      title: 'Day 1 Teacher-Led — [Description] ([Time])',
      content: `<div class="phase-header phase-blue">I DO (5 min)</div>
<div class="card">
  <h3>Step content as HTML string</h3>
  <p>Modeling text...</p>
</div>
<div class="phase-header phase-green">WE DO (8 min)</div>
<div class="card">
  <p>Guided practice...</p>
</div>
<div class="phase-header phase-orange">YOU DO (5 min)</div>
<div class="card">
  <p>Independent application...</p>
</div>`
    },
    ind: {
      title: 'Day 1 Independent — [Description] ([Time])',
      content: `<div class="card">
  <h2>Task Name</h2>
  <p>Activity instructions...</p>
</div>`
      // OR for question-based:
      // questions: [ { num: '11A', stem: '...', opts: [...], cer: {...}, wrong: {...} } ]
      // OR for writing tasks:
      // isWriting: true, prompt: '...', requirements: [...], frames: [...], checklist: {...}
    },
    closure: {
      title: 'Day 1 Closure — [Description] ([Time])',
      content: `<div class="card">
  <h2>Share-Out</h2>
  <p>Discussion prompt...</p>
</div>
<div class="card">
  <h2>Exit Ticket</h2>
  <!-- MC question with STOP badges and reveal button -->
</div>`
    }
  },
  2: { ... },
  // ... all days and sections
};
```

### Teacher Notes Object

Instead of a function, use a `TEACHER_NOTES` object keyed by `d{day}-{section}`:

```javascript
const TEACHER_NOTES = {
  'd1-bell': `<h3>Day 1 Bellringer — Script</h3>
<p><strong>Answer Key:</strong> 1. B, 2. A, 3. C</p>
<p><strong>ESOL Strategy:</strong> Pre-teach word forms...</p>
<p><strong>Monitoring Tip:</strong> Watch for...</p>`,
  'd1-tl': `<h3>Day 1 Teacher-Led — Step-by-Step Script</h3>
<p><strong>I DO (5 min):</strong> Model circling evidence by...</p>
<p><strong>Think-Aloud:</strong> "I notice the word... which suggests..."</p>`,
  'd1-ind': `<h3>Day 1 Independent — Monitoring</h3>
<p><strong>Task Summary:</strong> Students annotate...</p>
<p><strong>Circulation Checklist:</strong> Look for...</p>
<p><strong>Common Errors:</strong> Some students may...</p>`,
  'd1-closure': `<h3>Day 1 Closure</h3>
<p><strong>Share-Out Facilitation:</strong> Call on...</p>
<p><strong>Exit Ticket Answer:</strong> B is correct because...</p>`,
  // ... one entry per (day, section) combination
  // For 4-day unit: 16 total entries
  // For 6-day unit: 24 total entries
};
```

**Required:** Every single day-section view MUST have a teacher notes entry.

### STOP Badge Function

```javascript
function cycleSTOPBadge(badge) {
  const states = ['', 'S', 'T', 'O', 'P'];
  const classes = ['', 'stop-s', 'stop-t', 'stop-o', 'stop-p'];
  const current = states.indexOf(badge.textContent);
  const next = (current + 1) % states.length;
  classes.forEach(c => {
    if (c) badge.classList.remove(c);
  });
  badge.textContent = states[next];
  if (next > 0) badge.classList.add(classes[next]);
}
```

### Teacher-Controlled MC Reveal Function

```javascript
function toggleMCReveal(btn) {
  const qCard = btn.closest('.q-card') || btn.closest('.card');
  const choices = qCard.querySelector('.mc').querySelectorAll('.mc-choice');
  const isRevealed = btn.classList.contains('revealed');
  choices.forEach(c => {
    if (isRevealed) {
      c.classList.remove('correct', 'incorrect');
    } else {
      c.classList.add(c.dataset.correct === 'true' ? 'correct' : 'incorrect');
    }
  });
  btn.textContent = isRevealed ? '👁 Show Answer' : '🙈 Hide Answer';
  btn.classList.toggle('revealed');
}
```

### Annotation Functions

```javascript
function selectAnnoTool(tool, event) {
  event.stopPropagation();
  annoTool = tool;
  document.querySelectorAll('.cb-tool').forEach(btn => btn.classList.remove('active'));
  event.target.closest('.cb-tool').classList.add('active');
}

function toggleCubesBar() {
  const bar = document.getElementById('cubesBar');
  bar.classList.toggle('show');
  annotationMode = bar.classList.contains('show');
  document.body.style.cursor = annotationMode ? 'crosshair' : 'auto';
  document.getElementById('cubesBtn').classList.toggle('active');
}

function clearAnnotations() {
  document.querySelectorAll(`mark[class*="mark-"]`).forEach(mark => {
    while (mark.firstChild) {
      mark.parentNode.insertBefore(mark.firstChild, mark);
    }
    mark.parentNode.removeChild(mark);
  });
}
```

### Split View Function

```javascript
function toggleSplitView() {
  const btn = document.getElementById('splitViewBtn');
  const content = document.querySelector('.content');
  content.classList.toggle('split-view');
  const passagePanel = document.getElementById('passagePanel');
  if (passagePanel) {
    passagePanel.style.display = content.classList.contains('split-view') ? 'block' : 'none';
  }
  btn.classList.toggle('active');
}
```

### Passage Toggle Function

```javascript
function togglePassage() {
  const btn = document.getElementById('passageBtn');
  const passagePanel = document.getElementById('passagePanel');
  if (!passagePanel) {
    console.warn('Passage panel not found');
    return;
  }
  passagePanel.style.display = passagePanel.style.display === 'none' ? 'block' : 'none';
  btn.classList.toggle('active');
}
```

### Timer Functions

```javascript
function toggleTimerPlay() {
  if (timerRunning) pauseTimer();
  else startTimer(timerSec);
}

function startTimer(sec) {
  timerRunning = true;
  document.getElementById('timerPlayBtn').textContent = '⏸ Pause';
  timerInterval = setInterval(() => {
    timerSec--;
    if (timerSec <= 0) {
      clearInterval(timerInterval);
      timerRunning = false;
      timerSec = 0;
      document.getElementById('timerDisplay').textContent = '0:00';
      document.getElementById('timerPlayBtn').textContent = '▶ Start';
      // Optional: trigger alarm or notification
      return;
    }
    updTimer();
    // Add pulse warning at ≤60 seconds
    if (timerSec <= 60) {
      document.getElementById('timerDisplay').classList.add('warn');
    } else {
      document.getElementById('timerDisplay').classList.remove('warn');
    }
  }, 1000);
  updTimer();
}

function pauseTimer() {
  timerRunning = false;
  clearInterval(timerInterval);
  document.getElementById('timerPlayBtn').textContent = '▶ Start';
}

function resetTimer() {
  pauseTimer();
  timerSec = 300; // or extract from preset
  updTimer();
}

function updTimer() {
  const min = Math.floor(timerSec / 60);
  const sec = timerSec % 60;
  document.getElementById('timerDisplay').textContent =
    `${min}:${sec.toString().padStart(2, '0')}`;
}

function toggleTimerBar() {
  const bar = document.getElementById('timerBar');
  bar.classList.toggle('show');
  document.getElementById('timerBtn').classList.toggle('active');
}
```

### Engage Overlay Functions

```javascript
function toggleEngage() {
  const overlay = document.getElementById('engageOverlay');
  if (!overlay) {
    console.warn('Engage overlay not found');
    return;
  }
  overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
  document.getElementById('engageBtn').classList.toggle('active');
}

function addTally(choice) {
  tally[choice]++;
  updTallyBars();
}

function resetTally() {
  tally = { A: 0, B: 0, C: 0, D: 0 };
  updTallyBars();
}

function updTallyBars() {
  const total = tally.A + tally.B + tally.C + tally.D || 1;
  ['A', 'B', 'C', 'D'].forEach(letter => {
    const pct = (tally[letter] / total * 100).toFixed(0);
    const bar = document.getElementById(`tallyBar-${letter}`);
    if (bar) bar.style.width = pct + '%';
    document.getElementById(`tallyCount-${letter}`).textContent = tally[letter];
  });
}
```

### Render Functions

```javascript
function render() {
  // CRITICAL: Only init passage once to prevent annotation wipe
  if (!passageInitialized && document.getElementById('passageContent')) {
    document.getElementById('passageContent').innerHTML = PASSAGE_TEXT;
    passageInitialized = true;
  }

  const sec = SEC_KEYS[currentSection];
  const data = DATA[currentDay][sec];

  if (currentSection === 0) renderBell(data);
  else if (currentSection === 1) renderTL(data);
  else if (currentSection === 2) renderInd(data);
  else if (currentSection === 3) renderClosure(data);

  updFooter();
}

function renderBell(d) {
  let html = `<div class="card"><h2>${d.title}</h2><p>${d.intro}</p></div>`;
  if (d.passage) html += `<div class="passage-box"><p>${d.passage}</p></div>`;

  html += `<div class="timer-card"><span class="timer-display" id="bellTimer">5:00</span></div>`;

  d.items.forEach((item, idx) => {
    html += `<div class="card"><p><strong>Q${idx + 1}:</strong> ${item.stem}</p>
    <div class="mc">`;
    item.opts.forEach(opt => {
      const correct = opt.c ? 'true' : 'false';
      html += `<div class="mc-choice" data-correct="${correct}">
        <span class="mc-text">${opt.l}) ${opt.t}</span>
        <span class="stop-badge" onclick="event.stopPropagation(); cycleSTOPBadge(this)"></span>
      </div>`;
    });
    html += `</div><button class="reveal-btn" onclick="toggleMCReveal(this)">👁 Show Answer</button></div>`;
  });

  document.getElementById('contentArea').innerHTML = html;
  startBellTimer();
}

function renderTL(d) {
  const html = `<div class="card"><h2>${d.title}</h2></div>${d.content}`;
  document.getElementById('contentArea').innerHTML = html;
}

function renderInd(d) {
  let html = `<div class="card"><h2>${d.title}</h2></div>`;

  if (d.isWriting) {
    html += `<div class="card"><h3>Prompt</h3><p>${d.prompt}</p></div>`;
    html += `<div class="card"><h3>Requirements</h3><ul>`;
    d.requirements.forEach(req => html += `<li>${req}</li>`);
    html += `</ul></div>`;
    html += `<div class="card"><h3>Sentence Frames</h3>`;
    d.frames.forEach(frame => html += `<p><em>${frame}</em></p>`);
    html += `</div><div class="card"><h3>Self-Assessment</h3><div class="check-group">`;
    Object.keys(d.checklist).forEach(category => {
      d.checklist[category].forEach(item => {
        html += `<div class="check-item" onclick="toggleCheck(this)"><span>${item}</span></div>`;
      });
    });
    html += `</div></div>`;
  } else if (d.questions) {
    d.questions.forEach(q => {
      html += `<div class="q-card"><p><strong>Q${q.num}:</strong> ${q.stem}</p><div class="mc">`;
      q.opts.forEach(opt => {
        const correct = opt.c ? 'true' : 'false';
        html += `<div class="mc-choice" data-correct="${correct}">
          <span class="mc-text">${opt.l}) ${opt.t}</span>
          <span class="stop-badge" onclick="event.stopPropagation(); cycleSTOPBadge(this)"></span>
        </div>`;
      });
      html += `</div><button class="reveal-btn" onclick="toggleMCReveal(this)">👁 Show Answer</button>`;
      if (q.cer) {
        html += `<div class="cer-block"><div class="cer-claim">Claim: ${q.cer.c}</div>
        <div class="cer-evidence">Evidence: ${q.cer.e}</div>
        <div class="cer-reasoning">Reasoning: ${q.cer.r}</div></div>`;
      }
      if (q.wrong) {
        html += `<div class="wrong-grid">`;
        Object.keys(q.wrong).forEach(letter => {
          html += `<div class="wrong-row"><strong>${letter}:</strong> ${q.wrong[letter]}</div>`;
        });
        html += `</div>`;
      }
      html += `</div>`;
    });
  } else {
    html += d.content;
  }

  document.getElementById('contentArea').innerHTML = html;
}

function renderClosure(d) {
  const html = `<div class="card"><h2>${d.title}</h2></div>${d.content}`;
  document.getElementById('contentArea').innerHTML = html;
}

function updFooter() {
  const footerText = `${SEC_ICONS[currentSection]} ${SEC_NAMES[currentSection]} · Day ${currentDay}`;
  document.querySelector('.foot').textContent = `← → Sections | T Notes | C CUBES | R Timer | P Passage | E Engage | Esc Close All — ${footerText}`;
}
```

### Navigation Function

```javascript
function go(day, sec) {
  currentDay = Math.max(1, Math.min(day, Object.keys(DATA).length));
  currentSection = sec % 4;

  document.querySelectorAll('.day-tab').forEach((tab, i) => {
    tab.classList.toggle('active', i + 1 === currentDay);
  });

  document.querySelectorAll('.pill').forEach((pill, i) => {
    pill.classList.toggle('active', i === currentSection);
  });

  document.getElementById('contentArea').scrollTop = 0;
  render();
}
```

### Keyboard Navigation (with input protection)

```javascript
document.addEventListener('keydown', (e) => {
  // Don't fire shortcuts if user is typing in input/textarea/contentEditable
  if (['INPUT', 'TEXTAREA'].includes(e.target.tagName) || e.target.contentEditable === 'true') {
    return;
  }

  if (e.key === 'ArrowLeft') {
    e.preventDefault();
    currentSection = (currentSection - 1 + 4) % 4;
    if (currentSection === 3) currentDay = Math.max(1, currentDay - 1);
    go(currentDay, currentSection);
  } else if (e.key === 'ArrowRight') {
    e.preventDefault();
    currentSection = (currentSection + 1) % 4;
    if (currentSection === 0) currentDay = Math.min(Object.keys(DATA).length, currentDay + 1);
    go(currentDay, currentSection);
  } else if (e.key === 't' || e.key === 'T') {
    e.preventDefault();
    toggleNotes();
  } else if (e.key === 'c' || e.key === 'C') {
    e.preventDefault();
    toggleCubesBar();
  } else if (e.key === 'r' || e.key === 'R') {
    e.preventDefault();
    toggleTimerBar();
  } else if (e.key === 'p' || e.key === 'P') {
    e.preventDefault();
    togglePassage();
  } else if (e.key === 'e' || e.key === 'E') {
    e.preventDefault();
    toggleEngage();
  } else if (e.key === 'Escape') {
    e.preventDefault();
    document.getElementById('notesOverlay').style.display = 'none';
    document.getElementById('engageOverlay').style.display = 'none';
    document.getElementById('cubesBar').classList.remove('show');
    document.getElementById('timerBar').classList.remove('show');
  }
});
```

### Mode & Notes Functions

```javascript
function toggleMode() {
  document.body.classList.toggle('light-mode');
  const btn = document.getElementById('modeBtn');
  btn.textContent = document.body.classList.contains('light-mode') ? '🌙 Dark' : '☀️ Light';
}

function toggleNotes() {
  const overlay = document.getElementById('notesOverlay');
  const content = document.getElementById('notesContent');
  const key = `d${currentDay}-${currentSection}`;
  content.innerHTML = TEACHER_NOTES[key] || '<p>Notes not available.</p>';
  overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
}
```

### Misc Utilities

```javascript
function toggleCheck(el) {
  el.classList.toggle('checked');
}

function startBellTimer() {
  if (currentSection === 0) {
    timerSec = 300;
    timerRunning = true;
    updTimer();
    timerInterval = setInterval(() => {
      timerSec--;
      if (timerSec <= 0) {
        clearInterval(timerInterval);
        timerRunning = false;
        return;
      }
      updTimer();
    }, 1000);
  }
}
```

---

## HTML Structure Patterns

### MC Choice with STOP Badge

```html
<div class="mc-choice" data-correct="true">
  <span class="mc-text">B) answer text</span>
  <span class="stop-badge" onclick="event.stopPropagation(); cycleSTOPBadge(this)"></span>
</div>
```

**Never omit the STOP badge.** It is on EVERY MC choice across the entire website.

### MC Question with Teacher Reveal

```html
<div class="card">
  <p><strong>Question:</strong> Stem text</p>
  <div class="mc">
    <div class="mc-choice" data-correct="true">
      <span class="mc-text">A) Choice A</span>
      <span class="stop-badge" onclick="event.stopPropagation(); cycleSTOPBadge(this)"></span>
    </div>
    <div class="mc-choice" data-correct="false">
      <span class="mc-text">B) Choice B</span>
      <span class="stop-badge" onclick="event.stopPropagation(); cycleSTOPBadge(this)"></span>
    </div>
  </div>
  <button class="reveal-btn" onclick="toggleMCReveal(this)">👁 Show Answer</button>
</div>
```

### Phase Header (I DO / WE DO / YOU DO)

```html
<div class="phase-header phase-blue">I DO (5 min)</div>
<div class="card">
  <p>Modeling content...</p>
</div>
<div class="phase-header phase-green">WE DO (8 min)</div>
<div class="card">
  <p>Guided practice...</p>
</div>
<div class="phase-header phase-orange">YOU DO (5 min)</div>
<div class="card">
  <p>Independent application...</p>
</div>
```

### Topbar Layout

```html
<div class="topbar">
  <div class="topbar-left">
    [badges] Unit Title
  </div>
  <div class="topbar-right">
    <button class="tb-btn" id="splitViewBtn" onclick="toggleSplitView()">📖 Split</button>
    <button class="tb-btn" id="passageBtn" onclick="togglePassage()">📄 Passage</button>
    <button class="tb-btn" id="cubesBtn" onclick="toggleCubesBar()">🔍 CUBES</button>
    <button class="tb-btn" id="timerBtn" onclick="toggleTimerBar()">⏱ Timer</button>
    <button class="tb-btn" id="engageBtn" onclick="toggleEngage()">💬 Engage</button>
    <button class="tb-btn" onclick="toggleNotes()">📋 Notes</button>
    <button class="tb-btn" id="modeBtn" onclick="toggleMode()">☀️ Light</button>
  </div>
</div>
```

### CUBES Bar

```html
<div class="cubes-bar" id="cubesBar">
  <div class="cubes-bar-inner">
    <button class="cb-tool circle active" onclick="selectAnnoTool('circle', event)">⭕ Circle</button>
    <button class="cb-tool underline" onclick="selectAnnoTool('underline', event)">〰️ Underline</button>
    <button class="cb-tool box" onclick="selectAnnoTool('box', event)">🟩 Box</button>
    <button class="cb-tool evidence" onclick="selectAnnoTool('evidence', event)">🟣 Evidence</button>
    <button class="cb-tool summarize" onclick="selectAnnoTool('summarize', event)">🔴 Summarize</button>
    <button class="cb-clear" onclick="clearAnnotations()">🗑 Clear All</button>
  </div>
</div>
```

### Timer Bar

```html
<div class="timer-bar" id="timerBar">
  <div class="timer-bar-inner">
    <span class="timer-display" id="timerDisplay">5:00</span>
    <button class="tmr-btn" onclick="toggleTimerPlay()" id="timerPlayBtn">▶ Start</button>
    <button class="tmr-btn" onclick="resetTimer()">↺ Reset</button>
    <button class="tmr-btn" onclick="timerSec=60;updTimer()">1 min</button>
    <button class="tmr-btn" onclick="timerSec=120;updTimer()">2 min</button>
    <button class="tmr-btn" onclick="timerSec=300;updTimer()">5 min</button>
    <button class="tmr-btn" onclick="timerSec=600;updTimer()">10 min</button>
  </div>
</div>
```

### Engage Overlay (Consolidated)

```html
<div class="engage-overlay" id="engageOverlay" style="display:none;">
  <div class="engage-content">
    <h2>Engage</h2>

    <div class="tally-section">
      <h3>Response Tally</h3>
      <div class="tally-btn">
        <span>A:</span>
        <span id="tallyCount-A">0</span>
        <div class="tally-bar" id="tallyBar-A"></div>
      </div>
      <div class="tally-btn">
        <span>B:</span>
        <span id="tallyCount-B">0</span>
        <div class="tally-bar" id="tallyBar-B"></div>
      </div>
      <div class="tally-btn">
        <span>C:</span>
        <span id="tallyCount-C">0</span>
        <div class="tally-bar" id="tallyBar-C"></div>
      </div>
      <div class="tally-btn">
        <span>D:</span>
        <span id="tallyCount-D">0</span>
        <div class="tally-bar" id="tallyBar-D"></div>
      </div>
      <button onclick="resetTally()">Reset</button>
    </div>

    <div class="tally-section">
      <h3>Discussion Prompts</h3>
      <p>Context-aware prompts for this section...</p>
    </div>

    <div class="tally-section">
      <h3>Quick Presets</h3>
      <button onclick="addTally('A')">A</button>
      <button onclick="addTally('B')">B</button>
      <button onclick="addTally('C')">C</button>
      <button onclick="addTally('D')">D</button>
    </div>

    <button onclick="toggleEngage()" style="margin-top:1rem;">Close</button>
  </div>
</div>
```

---

## Content Population Rules

### Bellringer Content Per Day

**Test Prep (4-day):**
- Day 1: Vocabulary fill-in-the-blank (3 items)
- Day 2: Vocabulary in context from passage (2 items + passage excerpt)
- Day 3: Vocabulary application — correct usage (2 items)
- Day 4: Vocabulary quiz — definitions (3 items)

**Literary Analysis (6-day):**
- Days 1-6: Context clue bellringers (2 MC + 1 written response per day using 3 vocabulary words)

### Teacher-Led Content Per Day

Extract from lesson plan. Each day's TL should have accordion sections color-coded by phase:
- **I DO** (`phase-blue` header) — Teacher modeling content
- **WE DO** (`phase-green` header) — Guided practice content
- **YOU DO** (`phase-orange` header) — Independent application content

Include full HTML content with:
- Annotation displays (`.anno-row` classes)
- Passage excerpts (`.passage-box`)
- Question analysis cards (`.q-card`)
- CER/ACE model blocks
- Highlight boxes for key points
- Wrong-answer analysis grids

### Independent Content Per Day

Match student packet activities:
- **HTML-based** (`d.content`): Checklists, tables, annotation guides
- **Question-based** (`d.questions`): Q-cards with MC + CER reveals + wrong-answer analysis
- **Writing-based** (`d.isWriting`): Prompt display, requirements, sentence frames, self-assessment checklist

### Closure Content Per Day

- Share-out prompt (1-2 discussion questions)
- Exit ticket MC question with reveal button and STOP badges
- Final day: Reflection question + celebration card

---

## Quality Checklist

Before delivering the HTML file, verify:

- [ ] **STOP badges on EVERY MC choice** — no exceptions, entire website
- [ ] **Teacher-controlled reveal button on every MC question** — "Show Answer" / "Hide Answer"
- [ ] **All days render** — DATA object has keys for every day (1-4 or 1-6)
- [ ] **All sections populated** — Every day has bell, tl, ind, closure with real content
- [ ] **Teacher notes complete** — TEACHER_NOTES has entries for every (day, section) pair (16 or 24 total)
- [ ] **MC answers marked** — Every MC item has exactly one `c: true` option
- [ ] **CER/ACE blocks present** — Model responses included where lesson plan shows them
- [ ] **Wrong-answer analysis** — At least for the modeled questions in Teacher-Led
- [ ] **Vocabulary displayed** — All unit vocabulary words with definitions and passage context
- [ ] **CUBES bar toggles from topbar** — not floating, slide-down animation
- [ ] **Timer bar toggles from topbar** — not floating, slide-down animation
- [ ] **Annotations work across entire website** — not just passage
- [ ] **passageInitialized flag prevents annotation wipe** — when navigating sections
- [ ] **Keyboard shortcuts don't fire in text inputs** — check INPUT/TEXTAREA/contentEditable
- [ ] **Split view for passage + content** — 45%/55% layout, independent scroll
- [ ] **Engage overlay contains Tally + Polls** — consolidated, not separate panels
- [ ] **No external dependencies** — All CSS/JS inline, no CDN links
- [ ] **Dark mode default** — Light mode available via toggle
- [ ] **Font sizes readable** — Body text ≥1rem, headers ≥1.3rem, timer ≥4rem
- [ ] **ESOL accommodations** — Sentence starters, frames, and scaffolds included where lesson plan specifies

---

## Reference Implementation

**File:** `Shakuntala_D1-4_TestPrep_Interactive_v5.html`
**Unit:** Shakuntala — 4-Day Test Prep
**Benchmarks:** R.1.1, R.1.2, R.1.4
**Framework:** CER with CUBES annotation
**Size:** ~1,155 lines, ~100KB
**Features demonstrated:** All 14 core features listed above, including STOP badges on every MC, teacher-controlled reveal, topbar toggles, CUBES/Timer slide-down bars, split view, and consolidated Engage overlay

This file is the canonical reference for the v5 day-tab + section-pill architecture with topbar controls. All future interactive lessons should match its structure, design tokens, interaction patterns, and pedagogy.

---

## Key Differences from v1 (Ali Cogia)

| Aspect | v1 | v5 |
|--------|----|----|
| **MC Interaction** | Student click-to-lock | Teacher-controlled reveal button |
| **STOP Protocol** | Optional badge system | Mandatory on EVERY MC choice |
| **CUBES Interface** | Floating sidebar | Topbar toggle → slide-down bar |
| **Timer Interface** | Bellringer-only floating card | Topbar toggle → slide-down bar |
| **Passage Access** | Always visible | Topbar toggle + Split View option |
| **Annotation Scope** | Passage-only | Entire website |
| **Engage/Tally** | Separate panels | Consolidated overlay |
| **DATA Structure** | Step objects (TL) | HTML strings (TL/Ind/Closure) |
| **Teacher Notes** | Function (getNotes) | Object (TEACHER_NOTES) |
| **Gradual Release** | Step navigation | Phase headers (I DO/WE DO/YOU DO) |
| **Keyboard Shortcuts** | T, Y, Esc | T, C, R, P, E, Esc (with input protection) |
