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
failed at scale. Day 127's lesson ran to 40 668 characters and put the entire
derivation of backpropagation under one `##` heading. Days 120–132 average ~38 000 characters. A
reader cannot revisit one subtopic without re-reading its neighbours, and there is no way to tell a
thinly-covered subtopic from a missing one.

**Amendment.**

- New **Principle 16 — depth over density**. A day is taught as a hub plus one document per
  subtopic, never as one long page.
- New **Principle 17 — a day is a unit of subject, not a unit of time**. No document carries a time
  estimate, a duration or a pace; nothing is ever trimmed to fit a schedule. A topic may take one
  sitting or five.
- New **Principle 18 — assume no prior knowledge, finish at production**. Every subtopic opens where
  a reader who has never met the idea can stand and closes with the real-system version of it: what
  changes at scale, what a senior engineer does differently, what a reviewer and an interviewer
  probe. Strong basics and advanced technique are the same document, in that order.
- New **Part 11 — the depth contract**: the three commitments, the folder shape, the
  `<section>.<subtopic>` numbering rule, the **ten** required sections of a part document (adding
  *The story* and a mandatory *In production*), the twelve required sections of a hub, the `level`
  ladder (`foundation → working → production`), splitting by idea boundary rather than length, and
  the seven failure modes this replaces.
- Days become `days/day-NN/{LESSON.md, CHECKLIST.md, parts/, lab/}`, with one folder per
  section inside `parts/` — `parts/01/1.1-<slug>.md`, `parts/02/2.3-<slug>.md` — so a day with
  twenty parts stays navigable.
- New `scripts/depth_check.py` and `./m depth [NN]` enforce the contract mechanically, including a
  hard failure on any time estimate found in a day folder (Principle 17) and on a `level` outside
  the three allowed values.
- `scripts/tracker.py` now reports a part count per day, so a thin day is visible from the progress
  table alone.

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset or principle 1–15 is
touched. The 240-day arc and all 276 IDs are identical to v1.0.0. This is a documentation-format
and documentation-depth amendment only.

**On the 240 days.** Principle 17 does not shorten or lengthen the plan — it removes the *clock*
from it. Day numbers remain an index into the subject. A day whose subject is large is not
compressed to fit an evening; it is read across as many sittings as it needs, and `./m done N` is
gated on a ticked checklist and green checks, never on elapsed time.

**Migration.** All 133 v1.0.0 lessons were **deleted** on 2026-08-22 (commit `2b290ba`; recoverable
from git history if ever needed). They were not converted, because splitting a shallow page into
shallower pages is not depth — see Part 11.8. Every day is rewritten from the plan, from Day 0
forward, so `days/` refills gradually and `docs/TRACKER.md` reports the real position.

---

## v1.0.0 — 2026-08-21 — initial DS/GenAI plan

240 days, 30 phases (0–29), 27 modules, 276 IDs, 15 operating principles. Stack pins read from live
PyPI on 2026-08-21. Companion documents: `CURRICULUM_INDEX_DS.md`, `PINS_DS.md`,
`CAPSTONE_SETU.md`.
