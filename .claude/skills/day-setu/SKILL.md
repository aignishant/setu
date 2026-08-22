---
name: day-setu
description: Generate the hub, the parts/ sub-documents, the lab scaffold and the checklist for a given day of the Setu plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Setu plan (v2.0.0 — hub + `parts/`)

> **Read `docs/00_MASTER_PLAN_DS_GENAI.md` Part 11 before writing a single line.** It is the depth
> contract this skill implements. This skill is the procedure; Part 11 is the standard.

## Step 1 — gather

1. Read the plan (Part 4 matrices, Part 5 phase map, **Part 11 depth contract**) and
   `docs/CURRICULUM_INDEX_DS.md`. Collect every ID slotted to Day $ARGUMENTS, the phase theme, the
   day's `kind`, and the gate that phase feeds.
2. Read `docs/TRACKER.md` for what is already written and at what depth.
3. Read `days/` for what exists. Build on prior days' code in `src/setu/` — never duplicate it.
   If the previous day's `CHECKLIST.md` has unticked boxes, warn me and ask before proceeding.
4. If `days/day-NN/_legacy/LESSON.md` exists, read it. It is the v1.0.0 draft: **mine it for
   correctness, then discard its structure.** Everything it covered must survive into the parts, and
   each surviving topic must gain the mechanism, failure text and check it did not have. Never
   copy a `_legacy` section across wholesale.

## Step 2 — plan the split (do this before writing prose)

5. List the day's subtopics. Group them into **sections** that share one mental model — usually one
   section per curriculum ID, per pipeline stage, or per phase of a derivation. State the grouping;
   an unexplained numbering is a bug.
6. Size it against Part 11.5: `setup` 8–12 parts · `lab` (1 ID) 4–7 · `lab` (2 IDs) 6–10 ·
   `concept` 4–6 · `gate` 5–8 · `project` 8–14. These are shapes, not quotas — a part is finished
   when its one idea is fully explained, not when it hits a length.
7. Apply **the one-idea test** to each planned part: if it needs "also" to introduce its second
   half, split it again before you start writing.
8. Print the planned part list to me before writing. If it looks thin, I will say so.

## Step 3 — write the parts (`days/day-NN/parts/<section>.<sub>-<slug>.md`)

9. One file per subtopic, named `<section>.<subtopic>-<kebab-slug>.md`. The slug says what the part
   *teaches*, never where it sits. Numbering starts at `1`, has no gaps.
10. Every part carries all eight sections of Part 11.3, in this order:
    - **frontmatter** — `day`, `part`, `title`, `ids`, `reading_minutes`, `prev`, `next`
    - **One-line answer** — the claim in one sentence, before anything else
    - **The idea in plain language** — analogy first, jargon defined on first use, no code
    - **Why Setu needs it** — the concrete downstream day that breaks without this
    - **The mechanism** — runnable code, or the derivation, or the diagram
    - **Line by line** — every non-obvious token, and *why that line and not another*
    - **When it breaks** — the **real** error text, what it means, the smallest fix
    - **Check yourself** — one command to run now, one question to answer out loud
11. Mermaid diagram whenever the concept is spatial, sequential, or a state machine.
12. Each part must pass **the standalone test**: readable cold, with its prerequisite part named
    and linked.

## Step 4 — write the hub (`days/day-NN/LESSON.md`)

13. The hub orients and assembles; **it never teaches**. No `Line by line:` in the hub. Required
    sections, in order (Part 11.4):
    - YAML frontmatter (`day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
      `plan_version: "v2.0.0"`, `parts`, `generated`, `status`, `lab_scaffolded`, `commit`)
    - a yesterday / today / tomorrow blockquote
    - `## §1 The story` — analogy first, plain language, NO code
    - `## §2 The map` — a table of every part: number, linked title, what it answers, minutes,
      plus one line saying what each *section* number means
    - `## §3 Setup — run this` — every `mkdir`, `touch`, `uv add` the day needs, pinned
    - `## §4 Build brief` — files to create, with `TODO(me)` markers for the learner's reps
    - `## §5 The eval that must be able to fail` — pytest that is RED before the TODOs are done
    - `## §6 Request budget` — model calls, network, cost (`0` is an answer; state it)
    - `## §7 Traps` — the mistakes that eat an evening
    - `## §8 Verify before you code` — live docs URLs, actually fetched, never from memory
    - `## §9 Say it in an interview` — one paragraph, spoken voice
    - `## §10 Done when` — pointer to `CHECKLIST.md`

## Step 5 — the checklist (`days/day-NN/CHECKLIST.md`)

14. Demo command, setup boxes, **one box per part document** (read it, run its check-yourself),
    build-brief boxes, a test box per test **including at least one "break it, watch it go red, fix
    it"**, budget, out-loud understanding questions, and the commit box.

## Step 6 — verify

15. Run `./m depth $ARGUMENTS`. Fix every failure; never hand-wave past one.
16. Run `uv run python scripts/tracker.py`.
17. Finish by printing: today's IDs, the part count, the demo command, and the request budget.

## Always

- Honor `CLAUDE.md`: exact pins, split-before-fit, read-only by default, from-scratch-before-library,
  at least one failing-able test, zero-budget model calls.
- Do **not** solve the `TODO(me)` sections. Teach; don't do the reps.
- Never name a person, instructor, author, channel, academy, bootcamp or training company anywhere
  in the output. The plan is self-contained and cites no external course or author; do not invent a
  lineage for it. Tool and library names are fine, as is citing a paper by its title.
- Splitting without deepening is the failure this format exists to prevent (Part 11.6). If a part
  gained no mechanism, no failure text and no check versus the `_legacy` prose, it is not done.
