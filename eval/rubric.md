# Cross-Plugin Smoke Test Rubric

Each skill output is scored on four dimensions. Scores are 1–3.

| Score | Meaning |
|-------|---------|
| 1 | Fail — clear problem, needs fix |
| 2 | Acceptable — works but could be better |
| 3 | Strong — correct, specific, usable as-is |

---

## Dimension 1: Instruction Following

Does the output follow the skill's own instructions? Does it produce the format, sections,
and structure the skill.md specifies?

- **3:** Output matches the skill's specified format and includes all required sections
- **2:** Minor deviation — one missing section or format issue, but output is still usable
- **1:** Output ignores the skill's format or misses multiple required sections

---

## Dimension 2: Specificity

Is the output tailored to the context provided in the prompt, or is it generic filler?

- **3:** Output uses concrete details from the prompt — names, dates, standards, data values
- **2:** Mostly specific; one or two generic placeholder elements
- **1:** Generic — could have been produced without the prompt context

---

## Dimension 3: Completeness

Is the output a finished, usable deliverable — or does it trail off, leave placeholders,
or require significant human completion?

- **3:** Output is complete and ready to use (or ready to hand off to the next skill/agent)
- **2:** Mostly complete; one section needs minor human editing
- **1:** Incomplete — placeholders, TODO markers, or missing critical sections

---

## Dimension 4: Quality

Is the output well-crafted? For teaching materials: pedagogically sound, grade-appropriate.
For data outputs: accurate calculations, clear formatting. For workflow outputs: actionable, clear.

- **3:** High quality — usable as-is by a teacher, analyst, or musician
- **2:** Adequate quality; minor issues that don't block usage
- **1:** Quality issues that make the output misleading or unusable

---

## Flag Threshold

An output is **flagged** if:
- Any single dimension scores **1**, OR
- The exact average score across all four dimensions is **below 2.0**

The threshold is applied to the exact average before rounding for display.
