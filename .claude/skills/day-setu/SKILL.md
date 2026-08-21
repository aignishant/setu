---
name: day-setu
description: Generate the lesson, lab scaffold, and checklist for a given day of the Setu plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Setu plan

1. Read `docs/00_MASTER_PLAN_DS_GENAI.md` (Part 4 matrices, Part 5 phase map) and
   `docs/CURRICULUM_INDEX_DS.md`. Collect every ID slotted to Day $ARGUMENTS, the phase
   theme, and the gate that phase feeds. Check `docs/TRACKER.md` for what is already written.
2. Read `days/` to see what exists. Build on prior days' code in `src/setu/` — never duplicate
   it. If the previous day's CHECKLIST.md has unticked boxes, warn me and ask before proceeding.
3. Create `days/day-NN/LESSON.md` matching `days/day-04/LESSON.md` exactly in shape:
   - YAML frontmatter (day, phase, phase_name, title, ids, principles, kind, plan_version,
     generated, status, lab_scaffolded, commit)
   - a yesterday / today / tomorrow blockquote
   - `## §1 The story` — analogy first, plain language, NO code
   - `## §2 Setup — run this` — every `mkdir`, `touch`, `uv add` the day needs, pinned
   - one section per ID: plain idea → why Setu needs it → runnable code → **Line by line:**
     explaining every non-obvious token → what it looks like when it breaks
   - `## Build brief` — files to create, with `TODO(me)` markers for the learner's reps
   - `## The eval that must be able to fail` — pytest that is RED before the TODOs are done
   - `## Request budget` — model calls, network, cost
   - `## Traps` — the mistakes that eat an evening
   - `## Verify before you code` — live docs URLs, actually fetched, never from memory
   - `## Say it in an interview` — one paragraph, spoken voice
   - `## Done when` — pointer to CHECKLIST.md
4. Create `days/day-NN/CHECKLIST.md`: demo command, setup boxes, per-ID boxes, build-brief
   boxes, a test box per test **including at least one "break it, watch it go red, fix it"**,
   budget, out-loud understanding questions, and the commit box.
5. Add a Mermaid diagram whenever the concept is spatial, sequential, or a state machine.
6. Honor `CLAUDE.md`: exact pins, split-before-fit, read-only by default, from-scratch-before-
   library, at least one failing-able test, zero-budget model calls.
7. Do NOT solve the `TODO(me)` sections. Teach; don't do the reps.
8. Run `uv run python scripts/tracker.py` at the end.
9. Finish by printing: today's IDs, the demo command, and the request budget.
