# Plugin System Audit — Evaluation Report
*Date: 2026-03-22 | Evaluating: `docs/audits/2026-03-21-plugin-system-audit.md`*

## Scoring Convention

| Score | Meaning |
|-------|---------|
| 1 | Fail — clear gap, needs remediation |
| 2 | Acceptable — works but has blind spots |
| 3 | Strong — thorough, correct, actionable |

**Flag threshold:** Any dimension scores 1, OR average < 2.0

---

**Summary:** 0 flagged, 7 passing of 7 dimensions | **Average: 2.71**

**Top issues:**
- Skill count discrepancy (audit says 91, post-cleanup actual is 90 — off-by-one from the `benchmark-guides` removal happening mid-audit)
- FUSE artifact cleanup was flagged but not executed in Phase 4 (193 `.fuse_hidden` files left in place)
- No load-testing or behavioral invocation of skills — audit verified existence, not runtime behavior

---

## Dimension 1: Coverage — Score: 3

**Question:** Did the audit inventory all relevant components?

**Evidence:**
- Skills: All 5 plugins inventoried with per-plugin counts (63+9+6+7+7 = 92 pre-cleanup, 91 reported with `benchmark-guides` flagged). Verified against repo: 90 skill dirs post-removal. The 91→90 gap is explained by `benchmark-guides` removal happening during the audit.
- Agents: All 16 enumerated by name, plugin, and status. Verified: exact match to repo.
- Commands: All 11 listed with trigger names. Verified.
- Hooks: 4 hooks documented (2 script files + 2 inline bash). Events and trigger conditions noted.
- Plugins cache: Full inventory of 12 cached plugins with version numbers, skill/agent/command counts.
- Settings: Both `settings.json` and `settings.local.json` audited. Path validation performed.
- Memory: 5 project directories checked. Stale counts identified.
- Project-level configs: All 5 checked for `settings.json` overrides.

**Verdict:** Comprehensive. Every layer of the Claude Code configuration was inventoried. Nothing structurally missed.

---

## Dimension 2: Collision Detection — Score: 3

**Question:** Did it catch name conflicts, overlaps, and shadowing risks?

**Evidence:**
- Custom vs. community: All 91 custom skill names checked against 1259 Cowork dirs, 14 superpowers, and all official plugin skills. Result: 0 collisions.
- Custom vs. custom: 8 overlap candidates analyzed with specific reasoning for keep/remove. `benchmark-guides` correctly identified as a strict subset of `benchmarks` with factual errors.
- Agent collisions: 16 custom vs. 6 community — 0 matches.
- Command collisions: Verified Notion `tasks/plan.md` does NOT collide with custom `/plan` (different namespace).
- Hook conflicts: Verified no community plugin registers hooks for the same 4 events.
- **Systemic risk surfaced:** `setup.sh` silent shadowing behavior documented — if Cowork installs a community skill with the same name as a custom skill, the custom skill is silently dropped. This is a forward-looking architectural risk, not just a current-state check.

**Verdict:** Thorough collision detection across all component types. The shadowing risk documentation is especially valuable — it catches a class of future bugs, not just current ones.

---

## Dimension 3: Actionability — Score: 3

**Question:** Were findings specific enough to act on?

**Evidence:**
- `benchmark-guides` removal: Named the specific errors (R.1.2 mislabeled, dead file paths), explained why `benchmarks` is the replacement, and confirmed it's a strict subset.
- Settings cleanup: Listed specific dead permissions (`Skill(gsd:*)`, stale `5.0.2` paths), gave before/after counts (160 → 78).
- Memory fix: Exact stale values ("69 skills, 14 agents") and correct values ("91 skills, 16 agents").
- GWS plugin: Specific path (`~/.agents/skills/`), count (92), and decision options (integrate or leave).
- Setup.sh fix: Warning message text specified.
- Each finding has a clear **Action** column (Remove / Update / Leave / Decide).

**Verdict:** Every finding is paired with a specific action. No vague "review this" recommendations.

---

## Dimension 4: Follow-Through — Score: 3

**Question:** Were Phase 4 cleanup actions actually executed and verified?

**Evidence:**
- `benchmark-guides` removed from source AND symlink. Verified in repo: directory no longer exists.
- `settings.local.json` cleaned: 160 → 78 entries. GSD, Obsidian, stale superpowers permissions removed.
- Memory updated: skill counts corrected.
- `setup.sh` re-run post-cleanup: confirmed clean (no errors, no skips).
- `CLAUDE.md` updated with architecture documentation (3-mechanism table, shadowing warning, superpowers dual-presence note). Verified: all present in current file.
- `gemini/` directory deleted, symlink block removed from `setup.sh`.
- 10 stale plan/spec files deleted.
- All changes committed and pushed per PROJECT.md.

**One gap:** FUSE artifacts (10 in skills, 183 in commands) were flagged but NOT cleaned up in Phase 4. These are harmless but the audit noted them without resolving them. This is a minor omission — the artifacts don't affect functionality.

**Verdict:** Strong execution. All material findings were acted on. The FUSE artifact gap is cosmetic only.

---

## Dimension 5: Architecture Documentation — Score: 3

**Question:** Did the audit surface and document systemic patterns?

**Evidence:**
- **3-mechanism loading table** added to `CLAUDE.md`: Custom symlinks, Cowork community dirs, Plugin cache — with source, who manages each, and how they interact.
- **Shadowing risk** documented with specific warning: `setup.sh` silently skips if a Cowork dir exists with the same name. Warning message updated in `setup.sh` itself.
- **Superpowers dual-presence** explained: 14 skills exist in both Cowork dirs and plugin cache. Plugin cache is authoritative. This is expected behavior.
- **Plugin cache vs. symlinks** clarified: `mr-burger-plugins` packaged versions (1.0.0, 3.0.0) in cache are NOT loaded; custom skills load exclusively via symlinks.

**Verdict:** The architecture documentation is the most valuable output of this audit. It prevents a class of "why did my skill stop working?" debugging sessions.

---

## Dimension 6: Residual Risk — Score: 2

**Question:** Are there things the audit should have caught but didn't?

**Blind spots identified:**

1. **No runtime/behavioral testing:** The audit verified file existence and naming but never invoked a skill to confirm it actually loads and executes correctly. A skill file can exist, be symlinked, and still fail at runtime (bad frontmatter, missing references, malformed markdown). Phase 5 checked workflows at the reference level only.

2. **Skill quality variance not assessed:** 90 skills range from heavily developed (benchmarks, unit-builder-protocol) to stubs (some classroom-ops skills). The audit treated all equally — it didn't flag under-developed skills that might produce poor output.

3. **Knowledge file completeness not checked:** `mr-burger-music/CLAUDE.md` notes several knowledge directories as "Stubs — pending PDF extraction" (trumpet, guitar, jazz, band). Skills referencing these stubs would produce degraded output. The audit didn't cross-reference skill→knowledge dependencies.

4. **Plugin.json accuracy not verified:** 5 `plugin.json` files exist but the audit didn't check whether their skill/agent lists match actual directories. A stale `plugin.json` could cause Cowork packaging issues.

5. **FUSE artifacts left unresolved:** 193 `.fuse_hidden` files in commands/ flagged but not cleaned.

**Verdict:** The audit was strong on structural integrity but didn't test functional quality. This is a known limitation — structural audits don't replace behavioral evals. Items 1-4 are real blind spots worth addressing in a follow-up.

---

## Dimension 7: Regression Safety — Score: 2

**Question:** Did Phase 5 eval confirm no breakage from changes?

**Evidence:**
- Phase 5 checked 3 known-good workflows (IR Unit Build, Student Data Pipeline, IR Teaching Core) — all passed.
- `benchmark-guides` removal verified: no other skill references it, replacement `benchmarks` covers the same functionality.
- Cross-file reference check confirmed no broken dependencies from the removal.

**Gaps:**
- Only 3 workflows tested out of many possible chains. The 90-skill ecosystem has dozens of potential invocation paths — 3 is a narrow sample.
- No negative test: didn't verify that invoking `benchmark-guides` by name now correctly fails (rather than silently returning nothing or hitting a cached version).
- Agent chains not tested: 16 agents were verified to exist but none were tested for correct skill dispatch.

**Verdict:** Adequate for the single removal that was made (`benchmark-guides`). But the regression suite is narrow relative to the ecosystem size. For a larger cleanup round, this would be insufficient.

---

## Score Summary

| # | Dimension | Score | Status |
|---|-----------|-------|--------|
| 1 | Coverage | 3 | PASSING |
| 2 | Collision Detection | 3 | PASSING |
| 3 | Actionability | 3 | PASSING |
| 4 | Follow-Through | 3 | PASSING |
| 5 | Architecture Documentation | 3 | PASSING |
| 6 | Residual Risk | 2 | PASSING |
| 7 | Regression Safety | 2 | PASSING |

**Average: 2.71 | Flagged: 0 of 7 | Passing: 7 of 7**

---

## Final Verdict: PASSING — audit was thorough and well-executed

The audit excels at structural inventory, collision detection, and architecture documentation. Its main limitation is the lack of behavioral/runtime testing — it confirmed that everything *exists* correctly but didn't confirm everything *works* correctly.

## Recommendations for Next Round

1. **Add runtime smoke tests:** Pick 5–10 representative skills across plugins and invoke them with a standard prompt. Verify output is non-empty and on-topic. (This is exactly what the band-materials eval framework is designed for — extend the pattern.)

2. **Cross-reference plugin.json ↔ actual directories:** Verify each `plugin.json` lists exactly the skills and agents that exist on disk. Flag any drift.

3. **Knowledge dependency audit:** For each skill that references a knowledge file, verify the knowledge file is populated (not a stub). Flag skills with stub dependencies.

4. **Expand regression suite:** Before the next cleanup round, define 8–10 canonical workflows (not just 3) and test all of them pre- and post-change.

5. **Clean FUSE artifacts:** `find ~/.claude/commands -name '.fuse_hidden*' -delete` and same for skills. These are harmless but add noise to future audits.
