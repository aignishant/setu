---
name: changelog-plan-ds
plan: setu
---

# 📓 Plan changelog — Project Setu

Principle 14: *if reality changes, the plan is amended first.* Every amendment lands here before any
code or lesson changes. Newest first.

---

## v2.0.0 — 2026-08-22 — the depth contract

**Trigger.** Review of the written days (0–132) found the v1.0.0 single-file lesson format had
failed at scale. `days/day-127/_legacy/LESSON.md` is 40 668 characters and puts the entire
derivation of backpropagation under one `##` heading. Days 120–132 average ~38 000 characters. A
reader cannot revisit one subtopic without re-reading its neighbours, and there is no way to tell a
thinly-covered subtopic from a missing one.

**Amendment.**

- New **Principle 16 — depth over density**. A day is taught as a hub plus one document per
  subtopic, never as one long page.
- New **Part 11 — the depth contract**: the folder shape, the `<section>.<subtopic>` numbering rule,
  the eight required sections of a part document, the twelve required sections of a hub, the sizing
  guide per day kind, and the five failure modes this replaces.
- Days become `days/day-NN/{LESSON.md, CHECKLIST.md, parts/, lab/}`.
- New `scripts/depth_check.py` and `./m depth [NN]` enforce the contract mechanically.
- `scripts/tracker.py` now reports a part count per day and distinguishes `🗃️ legacy` (written under
  v1.0.0, awaiting regeneration) from `⬜ pending` (never written).

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset or principle 1–15 is
touched. The 240-day arc and all 276 IDs are identical to v1.0.0. This is a documentation-format
amendment only.

**Migration.** All 133 v1.0.0 lessons were moved to `days/day-NN/_legacy/LESSON.md` on 2026-08-22
(nothing deleted; git history intact). Days are regenerated in the v2.0.0 shape from Day 0 forward.
A day whose `parts/` directory does not exist yet is still workable from its `_legacy/LESSON.md`.

---

## v1.0.0 — 2026-08-21 — initial DS/GenAI plan

240 days, 30 phases (0–29), 27 modules, 276 IDs, 15 operating principles. Stack pins read from live
PyPI on 2026-08-21. Companion documents: `CURRICULUM_INDEX_DS.md`, `PINS_DS.md`,
`CAPSTONE_SETU.md`.
