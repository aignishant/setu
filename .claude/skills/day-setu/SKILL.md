---
name: day-setu
description: Generate the hub, the parts/ sub-documents, the lab scaffold and the checklist for a given day of the Setu plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Setu plan (v2.3.0 — hub + `parts/`, folders named for their
subject, prose under contract)

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
4. **Plain words, real scenes, correct sentences** (Principle 20). The reader is learning
   something new, so the prose must never be the hard part. **The four story rules:** *ordinary, not
   clever* — the scene is a shared shopping list that changed while nobody was looking, a name
   spelled two ways in one file, a total that came out wrong; never a trading desk, never a cluster.
   *One small example, all the way through* — three rows, not three million, and the mechanism keeps
   using whatever the story picked up. *Short, common words* — `use` not `utilise`, `change` not
   `mutate` until the moment that term is being defined; the technical word waits for *the idea in
   plain language*, where it gets defined. *True, not staged* — the mistake people actually make, in
   the order they make it. **The prose rules:** complete sentences, correctly punctuated; define on
   first use or do not use; one idea per sentence. **A sentence the reader has to read twice is a
   defect.**

## Step 1 — gather

1. **Run `./m brief $ARGUMENTS` first.** It prints this day's working set — every ID slotted to
   the day with its full Part 4 matrix row, the phase theme, the day's `kind`, the gate that
   phase feeds, the part manifests of the two neighbouring written days, what is already in
   `src/setu/`, and a warning if the previous day's `CHECKLIST.md` has unticked boxes. Every
   line of it is copied verbatim from the plan, the index and the parts' own frontmatter —
   nothing in it is generated — so it is the plan, filtered, not a summary of the plan.
   **This replaces reading Part 4, Part 5, `docs/CURRICULUM_INDEX_DS.md` and `docs/TRACKER.md`
   whole.** Looking a day's IDs up by hand costs about 150 000 tokens and finds two table rows.
2. **Read `docs/00_MASTER_PLAN_DS_GENAI.md` Part 11 in full, every time. The brief does not
   contain it and never will.** Part 11 is the depth contract — the standard the day is judged
   against, not a fact to be looked up. Principle 20's prose rules and Part 11.4's ten required
   sections are judgement, and judgement does not survive being projected into a table. If you
   ever find yourself writing a day without having read Part 11 this session, stop and read it.
3. Read `days/INDEX.md` — one row per written part across every day, with its level and IDs —
   to find where an idea has already been taught, so you link to it rather than explaining it
   twice (Part 11's standalone test). Then open **only the specific parts it points you at**,
   for continuity of voice. Do not read neighbouring days whole; that is what the index is for.
4. Build on prior days' code in `src/setu/` — never duplicate it.
5. There is no previous draft to work from — the v1.0.0 lessons were deleted, deliberately. Every
   day is written fresh from the plan's matrices, the curriculum index, and the live documentation
   you verify on the day.

> **The rule behind steps 1–3.** A projection may stand in for a lookup; it may never stand in
> for the contract. `./m brief` and `days/INDEX.md` are generated files that copy — they can be
> trusted because they cannot invent. Part 11 is prose that judges — read it, always, in full.

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
10. **Choose the day's one running example, before writing a word of prose.** It is the thing
    every story on this day picks up and every mechanism keeps using: a four-line shopping list, a
    file of three names, one delivery address. Small enough to print in full, and ordinary enough
    that a reader has met it outside programming. A day that uses a different example in every part
    has made the reader learn six things instead of one.
11. Print the planned folder names, the part list and the running example to me before writing — as
    the tree you are about to create. If it looks thin, I will say so.

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
    - **frontmatter** — `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next`.
      Eight keys, no more. **No `kind:`, no `paper:`, no duration field of any kind** — v2.3.0
      retired the first two and `./m depth` fails on either.
    - **One-line answer** — the claim in one sentence, before anything else
    - **The story** — a concrete, ordinary scene first: a person, a mistake, a decision, told with
      the day's running example. No jargon at all in this section — not one term the reader has not
      already met. This is the hook the definition hangs on, and the four story rules above are the
      contract for it.
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

## Step 3b — cite the sources inline

18. Where a part rests on one dated document — a paper, a PEP, an RFC, an ISO or IEEE standard, a
    canonical implementation note — name it **in the sentence that needs it**, by **title · year ·
    permanent identifier · canonical URL**, and never by author, never "et al.", never by lab. One or
    two sentences about what the document decided is the whole budget. A part that turns into a
    summary of a specification has stopped teaching its own idea.
19. There is **no `papers/` directory** (retired in v2.3.0) and no `paper:` frontmatter key.
    `./m depth` fails on either, because both mean a day was written against the old contract and
    never migrated.

## Step 4 — write the hub (`days/day-NN-<slug>/LESSON.md`)

21. The hub orients and assembles; **it never teaches**. No `Line by line:` in the hub. Required
    sections, in order (Part 11.5):
    - YAML frontmatter (`day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
      `plan_version: "v2.3.0"`, `parts` (the count), `generated`, `status`, `lab_scaffolded`,
      `commit`)
    - a yesterday / today / tomorrow blockquote — **no time estimate**
    - `## §1 The story` — a scene and an analogy, plain language, NO code, NO jargon
    - `## §2 The map` — a table of every part: number, linked title
      (`parts/01-versions/1.1-<slug>.md`), what it answers, `level`, grouped by section with one
      line saying what each *section* means. That line and the section's folder slug must agree —
      the slug is the three-word version of it. **No minutes column, ever.**
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

22. Demo command, setup boxes, **one box per part document** (read it, run its check-yourself,
    answer its out-loud question), build-brief boxes, a test box per test **including at least one
    "break it, watch it go red, fix it"**, budget, and the commit box. No time estimates.

## Step 6 — verify

23. Run `./m depth $ARGUMENTS`. Fix every failure; never hand-wave past one — it is what catches
    an unslugged folder, a folder whose number disagrees with its filenames, a cross-day link
    written against a slug that does not exist, a leftover `kind:` or `paper:` key, and a `papers/`
    directory left behind by the retired v2.2.0 format.
    Then run `uv run ruff format days/day-NN-<slug>/` — **ruff formats Python code blocks inside
    Markdown**,
    so every ```python block in a lesson must already be canonically formatted or `./m check` fails.
    Fix `ruff check` findings in lesson code by hand rather than silencing them: teaching code that
    the project's own linter rejects is a bug in the lesson.
24. Run `./m tracker`. It regenerates `docs/TRACKER.md` **and** `days/INDEX.md` together — the new
    day's parts do not exist for step 3 of the next day until the index has been rebuilt, so a day
    that skips this makes the next day re-explain what it just taught.
25. Finish by printing: today's IDs, the day's folder name, its section folder names, the part
    count, the running example every part shares, the demo command, and the request budget.

## Always

- Honor `CLAUDE.md`: exact pins, split-before-fit, read-only by default, from-scratch-before-library,
  at least one failing-able test, zero-budget model calls.
- Do **not** solve the `TODO(me)` sections. Teach; don't do the reps.
- Never name a person, instructor, author, channel, academy, bootcamp or training company anywhere
  in the output. The plan is self-contained and cites no external course or author; do not invent a
  lineage for it. Tool and library names are fine, as is citing a paper by its title. **A citation is
  title · year · identifier · URL — never an author, never "et al.", never a lab.**
- **Never paste output you did not run.** Every transcript, every error string and every timing
  comes from an actual run on the day of writing, exactly like the docs URLs.
- **Read every paragraph back before moving on.** If it needs a second pass to parse, rewrite it
  rather than adding a parenthesis (Principle 20).
- The failures this format exists to prevent (Part 11.8): splitting without deepening · summary in
  place of explanation · **stopping at the toy example** · assuming the previous day · code without
  failure · **trimming to fit** · solved reps · **a story nobody has lived** · **prose that has to
  be read twice**. A part with no story, no mechanism, no real failure text and no production
  section is not done, however long it is.
