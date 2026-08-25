---
name: day-setu
description: Generate the hub, the parts/ sub-documents, the lab scaffold and the checklist for a given day of the Setu plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Setu plan (v2.2.0 — hub + `parts/` + `papers/`, folders named
for their subject)

> **Read `docs/00_MASTER_PLAN_DS_GENAI.md` Part 11 before writing a single line.** It is the depth
> contract this skill implements. This skill is the procedure; Part 11 is the standard.

## The four commitments (Part 11.1 — everything below follows from these)

1. **One idea per document.** If it needs "also" to introduce its second half, it is two documents.
2. **No clocks.** Never write a time estimate, a duration, a "should take ~2 hours", or a pace —
   not in frontmatter, not in prose, not in the checklist. A topic is finished when it is
   understood, and a reader may spend five sittings on one part. **Never trim an explanation
   because the day is getting long — split it into another part instead.**
3. **Zero to production, in one document.** Open where a reader who has never heard of the idea can
   stand. End where a professional stands: the real-system version, what breaks at scale, what a
   senior reviewer says, what an interviewer probes.
4. **Every idea has an address, and a source is an idea.** Where a subtopic rests on one dated
   document — a paper, a specification, a standard — that document is taught in **its own document
   in the day's `papers/`**, never summarised inside the part that uses it. Where a subtopic rests
   on no such document, its frontmatter says `paper: none` out loud.

## Step 1 — gather

1. Read the plan (Part 4 matrices, Part 5 phase map, **Part 11 depth contract**) and
   `docs/CURRICULUM_INDEX_DS.md`. Collect every ID slotted to Day $ARGUMENTS, the phase theme, the
   day's `kind`, and the gate that phase feeds.
2. Read `docs/TRACKER.md` for what is already written and at what depth.
3. Read `days/` for what exists. Build on prior days' code in `src/setu/` — never duplicate it.
   If the previous day's `CHECKLIST.md` has unticked boxes, warn me and ask before proceeding.
4. There is no previous draft to work from — the v1.0.0 lessons were deleted, deliberately. Every
   day is written fresh from the plan's matrices, the curriculum index, and the live documentation
   you verify on the day. Read the neighbouring written days instead, for continuity of voice and to
   see which ideas have already been introduced and can be linked rather than re-explained.

## Step 2 — plan the split (do this before writing prose)

5. List the day's subtopics. Group them into **sections** that share one mental model — usually one
   section per curriculum ID, per pipeline stage, or per phase of a derivation. State the grouping;
   an unexplained numbering is a bug.
6. Split by **idea boundaries, never by length or pace**. There is no target part count. Four parts
   if the subject needs four; twenty-two if it needs twenty-two. `setup` days split per tool or
   file; `lab` days per mechanism → behaviour → edge case → failure mode → production use;
   `concept` days one claim per part; `gate` days one acceptance criterion per part.
7. Assign each part a `level` — `foundation` (knows what it is), `working` (can use it on their own
   data), `production` (knows what changes in a real system). A day should climb. A day that is all
   `foundation` is a tutorial; a day opening at `production` has skipped the reader.
8. Apply the **one-idea test** and the **no-shortcut test** (no "for now, just accept that" without
   a forward link to the part that explains it) to each planned part *before* writing.
9. **Name the day and its sections before writing a word.** The day folder is
   `days/day-NN-<slug>/` and each section folder is `parts/NN-<slug>/`, where the slug is one to
   three kebab-case words for **what is inside**, never for where it sits. `01-versions`,
   `02-pypi-index`, `03-freezing`, `04-drift` — not `01-section-one`, not `01-part-a`, not a bare
   `01`. The section slug and the sentence the hub's §2 map uses to introduce that section must
   agree; if you cannot name a section in three words, the grouping is wrong, not the name.
10. **List the day's primary sources.** For every subtopic, ask: *is there one dated document that
    decided this?* A paper, a PEP, an RFC, an ISO/IEEE standard, a canonical implementation note.
    Most Python-fundamentals subtopics have none, and `paper: none` is the correct, common answer —
    but the question is asked for every part, and never left silent. Each source found becomes one
    document in `papers/`, numbered from `01` in reading order, and every part that leans on it
    declares its identifier in `paper:`.
11. Print the planned folder names, the part list **and the paper list** to me before writing — as
    the tree you are about to create. If either looks thin, I will say so.

## Step 3 — write the parts (`days/day-NN-<slug>/parts/<NN>-<slug>/<section>.<sub>-<slug>.md`)

12. **One folder per section, named `<NN>-<slug>`** — the zero-padded section number, a hyphen, and
    the name you chose in step 9: `parts/01-versions/`, `parts/02-pypi-index/`, `parts/12-<slug>/`.
    Every part lives inside its section's folder; none is ever loose in `parts/`, and the folder's
    number must match the number before the dot in the filename.
13. One file per subtopic, named `<section>.<subtopic>-<kebab-slug>.md` — **unchanged by v2.1.0**;
    only the folders gained slugs. The slug says what the part *teaches*, never where it sits.
    Numbering starts at `1`, has no gaps.
14. **Links are relative to the part's own folder**: a sibling in the same section is
    `1.2-<slug>.md`; a part in another section is `../01-versions/1.5-<slug>.md`; the hub is
    `../../LESSON.md`; a part in another day is
    `../../../day-NN-<slug>/parts/NN-<slug>/<file>.md`. `prev` and `next` in the frontmatter use
    the same form. The hub's §2 map links the full path from the day folder:
    `parts/01-versions/1.1-<slug>.md`. **Read the neighbouring day's real folder names before
    linking into it** — never guess a slug, and never assume another day numbers its sections the
    way this one does.
15. Every part carries all ten sections of Part 11.4, in this order:
    - **frontmatter** — `day`, `part`, `title`, `ids`, `level`, `kind`, `paper`, `prerequisites`,
      `prev`, `next`. `kind: concept` for a part. `paper:` is `none` or a list of identifiers, and
      **has no default** — an absent key is a failure. **No duration field of any kind.**
    - **One-line answer** — the claim in one sentence, before anything else
    - **The story** — a concrete scene first: a person, a machine, a failure, a decision. No jargon
      at all in this section. This is the hook the definition hangs on.
    - **The idea in plain language** — the concept assuming zero prior knowledge; every term defined
      on first use, **including terms from earlier days**, with a link to the part that introduced
      them. No code.
    - **Why Setu needs it** — the concrete downstream day that breaks without this
    - **The mechanism** — how it actually works: runnable code, or the derivation with every
      algebraic step shown, or the diagram. Nothing skipped as "obvious".
    - **Line by line** — a `**Line by line:**` list **immediately after each code block**: every
      non-obvious token, and *why that line and not another*
    - **When it breaks** — the **real** error text verbatim, what it means, the smallest fix
    - **In production** — the real-system version of this idea: what a professional writes instead
      of the teaching version, what degrades at scale or under concurrency, the failure that only
      shows with real data, the review comment a senior engineer leaves, and the interview question
      that finds out whether you have actually used it. **Not optional. This is the section that
      makes the document professional rather than introductory.**
    - **Check yourself** — one command to run now, one question to answer out loud
16. Mermaid diagram whenever the concept is spatial, sequential, or a state machine.
17. Each part must pass the **standalone test**: readable cold, with its prerequisite part named
    and linked.

## Step 3b — write the papers (`days/day-NN-<slug>/papers/<NN>-<slug>.md`)

Skip this step only when the day genuinely rests on no primary source — and say so, rather than
skipping silently.

18. One flat, numbered document per source: `papers/01-<slug>.md`, `papers/02-<slug>.md`. No section
    folders — a source belongs to the day, not to one stage of its teaching. Frontmatter is the
    part's, with `part: "P1"` matching the file number, `kind: paper`, and a non-empty `paper:` list
    of identifiers.
19. **Thirteen sections, in this order** — the part's ten, plus three:
    - **One-line answer** — what this document established, in one sentence
    - **The citation** — title · year · permanent identifier (arXiv, DOI, PEP, RFC, annex) ·
      canonical URL **you fetched today** · and *what to actually read*: "Figure 2 and Section 3.2",
      never "read the paper". **Never name an author, a lab or an "et al."**
    - **The story** — the world before the document: the problem, what people did instead, the cost
    - **The idea in plain language** — the claim, no maths, no code, zero prior knowledge
    - **Why Setu needs it** — the parts of this day, and the downstream day, that rest on it
    - **The mechanism** — the method as the document defines it, derived or coded
    - **Line by line** — after every code block, as everywhere else
    - **The demo** — a **runnable end-to-end mini project implementing this paper's one contribution
      and nothing else**: a named folder, every file in full with no elisions, one command, and the
      **real** output pasted from an actual run. Close it with one sentence naming what it
      deliberately leaves out. Three files is a good size; more than five means it grew a feature the
      paper did not contribute. **Run it before you paste the output.**
    - **When it breaks** — the real error text, verbatim
    - **What did not survive** — the hyperparameter everyone ignores, the ablation later work
      reversed, the claim that only holds at the paper's scale. A paper is a dated document, not
      scripture, and saying so is what separates teaching a source from reciting it.
    - **In production** — what a real system does with this idea today
    - **Check yourself** — one command, one out-loud question
20. Each citing part links **forward** to its paper, and the paper links back to the parts. A part
    may only cite an identifier this day has a paper for — `./m depth` fails otherwise.

## Step 4 — write the hub (`days/day-NN-<slug>/LESSON.md`)

21. The hub orients and assembles; **it never teaches**. No `Line by line:` in the hub. Required
    sections, in order (Part 11.5):
    - YAML frontmatter (`day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
      `plan_version: "v2.2.0"`, `parts`, `papers` (the count — `0` is an answer), `generated`,
      `status`, `lab_scaffolded`, `commit`)
    - a yesterday / today / tomorrow blockquote — **no time estimate**
    - `## §1 The story` — a scene and an analogy, plain language, NO code, NO jargon
    - `## §2 The map` — a table of every part: number, linked title
      (`parts/01-versions/1.1-<slug>.md`), what it answers, `level`, grouped by section with one
      line saying what each *section* means. That line and the section's folder slug must agree —
      the slug is the three-word version of it. **No minutes column, ever.** When the day has
      papers, the map ends with a separate `### The papers — papers/` block listing each one —
      never mixed into a section's table, because a source is not a subtopic.
    - `## §3 Setup — run this` — every `mkdir`, `touch`, `uv add` the day needs, pinned
    - `## §4 Build brief` — files to create, with `TODO(me)` markers for the learner's reps
    - `## §5 The eval that must be able to fail` — pytest that is RED before the TODOs are done
    - `## §6 Request budget` — model calls, network, cost (`0` is an answer; state it)
    - `## §7 Traps` — the mistakes that eat an evening
    - `## §8 Verify before you code` — live docs URLs, actually fetched, never from memory
    - `## §9 Say it in an interview` — one paragraph, spoken voice
    - `## §10 Done when` — pointer to `CHECKLIST.md`, defined by understanding and green checks,
      never by elapsed time

## Step 5 — the checklist (`days/day-NN-<slug>/CHECKLIST.md`)

22. Demo command, setup boxes, **one box per part document and one per paper** (read it, run its
    check-yourself,
    answer its out-loud question), build-brief boxes, a test box per test **including at least one
    "break it, watch it go red, fix it"**, budget, and the commit box. No time estimates.

## Step 6 — verify

23. Run `./m depth $ARGUMENTS`. Fix every failure; never hand-wave past one — it is what catches
    an unslugged folder, a folder whose number disagrees with its filenames, a cross-day link
    written against a slug that does not exist, a missing `kind:`/`paper:` key, and a part citing an
    identifier the day has no paper for.
    Then run `uv run ruff format days/day-NN-<slug>/` — **ruff formats Python code blocks inside
    Markdown**,
    so every ```python block in a lesson must already be canonically formatted or `./m check` fails.
    Fix `ruff check` findings in lesson code by hand rather than silencing them: teaching code that
    the project's own linter rejects is a bug in the lesson.
24. Run `uv run python scripts/tracker.py`.
25. Finish by printing: today's IDs, the day's folder name, its section folder names, the part
    count, **the papers written (or the explicit statement that this day rests on none)**, the demo
    command, and the request budget.

## Always

- Honor `CLAUDE.md`: exact pins, split-before-fit, read-only by default, from-scratch-before-library,
  at least one failing-able test, zero-budget model calls.
- Do **not** solve the `TODO(me)` sections. Teach; don't do the reps.
- Never name a person, instructor, author, channel, academy, bootcamp or training company anywhere
  in the output. The plan is self-contained and cites no external course or author; do not invent a
  lineage for it. Tool and library names are fine, as is citing a paper by its title. **A citation is
  title · year · identifier · URL — never an author, never "et al.", never a lab.**
- **Never paste output you did not run.** Every demo transcript, every error string and every timing
  in a paper document comes from an actual run on the day of writing, exactly like the docs URLs.
- The failures this format exists to prevent (Part 11.8): splitting without deepening · summary in
  place of explanation · **stopping at the toy example** · assuming the previous day · code without
  failure · **trimming to fit** · solved reps. A part with no story, no mechanism, no real failure
  text and no production section is not done, however long it is.
