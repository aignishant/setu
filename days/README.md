# 📅 days/ — the 241 written days

**Never done this before?** Start at [`day-00-setup/LESSON.md`](day-00-setup/LESSON.md).
**Already set up?** Run `./m status`, it tells you where you are.
**Want the map?** [`../docs/CURRICULUM_INDEX_DS.md`](../docs/CURRICULUM_INDEX_DS.md).
**Want progress?** [`../docs/TRACKER.md`](../docs/TRACKER.md).

---

## The six rules these docs follow

1. **All the code lives in the docs. None of it is pre-written in the repo.**
   You type it, you own it. There is no `src/setu/*.py` waiting for you — every line you will ever
   run is written out in a lesson, and you create the file yourself. You cannot debug on Day 200
   what you never read on Day 26.

2. **Every code block is followed by a line-by-line walkthrough.**
   Not a summary — an explanation of what each line does and *why it is that line and not another*.
   If a line is unexplained anywhere in these documents, that is a bug in the doc.

3. **Every command is given in full.**
   `mkdir -p`, `touch`, `uv add package==1.2.3`, the run command, the test command. You should never
   have to infer "and now presumably I create a folder".

4. **One idea per document.** *(plan v2.0.0 — Principle 16)*
   A day is not one long page. It is a short hub plus one document per subtopic, in `parts/`. If a
   document needs the word "also" to introduce its second half, it should have been two documents.

5. **There are no clocks here.** *(Principle 17)*
   You will not find "this takes 90 minutes" anywhere in these documents, because it would be a lie
   and because it invites trimming. **A day is a unit of subject, not a unit of time.** Day 26 might
   take you one evening or four; both are the day being done properly. Nothing is ever cut short to
   fit a schedule — if a subject needs twenty-two documents, it gets twenty-two. `./m done N` is
   gated on a ticked checklist and green checks, never on hours elapsed.

6. **Zero prior knowledge in, production knowledge out.** *(Principle 18)*
   Every document starts where someone who has never heard of the idea can stand — the jargon is
   defined the first time it appears, including jargon from earlier days, with a link back. And no
   document stops at the toy example: each one ends with **In production** — what a professional
   writes instead of the teaching version, what breaks at scale or under concurrency, the comment a
   senior engineer leaves on that code, and the question an interviewer asks to find out whether you
   have really used it. Strong fundamentals and advanced technique are the same page, in that order.

---

## What's in a day folder

```
days/day-NN/
├── LESSON.md      # the hub — the story, the map of parts, setup, build brief, the eval, the budget
├── CHECKLIST.md   # the definition of done. `./m done NN` refuses to commit until it's ticked.
├── parts/         # THE TEACHING — one document per subtopic
│   ├── 01/        # section 1 — its own folder
│   │   ├── 1.1-<slug>.md
│   │   └── 1.2-<slug>.md
│   └── 02/        # section 2
│       └── 2.1-<slug>.md
└── lab/           # you create this; `./m scaffold NN` makes the folder
```

**Read the hub first, then the parts in numerical order.** The hub's §2 map is the table of contents
and tells you what each section number means for that day.

### What `1.1`, `1.2`, `2.1` mean

The number is `<section>.<subtopic>`, both scoped to that day.

- The **section** (the digit before the dot) groups subtopics that share one mental model — usually
  one curriculum ID, one stage of a pipeline, or one phase of a derivation.
- The **subtopic** (after the dot) is the reading order inside that section.

So on a two-ID day, `1.x` is the first ID, `2.x` is the second, and a `3.x` is usually the synthesis
— the trap you can only see once both ideas are true at the same time. Whatever the grouping is, the
hub says so explicitly.

**Each section gets its own folder**, numbered with two digits: section 1 is `parts/01/`, section 12
is `parts/12/`. So the third subtopic of section 2 is `parts/02/2.3-<slug>.md`. On a day with twenty
parts this is the difference between a readable folder and a wall of filenames — and a section is
exactly the chunk you will want to sit down with at once.

### The shape of every part document

Ten sections, always in this order. They trace one path: from a reader who has never heard of the
idea, to one who could defend it in a design review. This is the depth contract (plan Part 11.4),
and `./m depth NN` fails the day if any of them is missing.

| Section | What it's for |
|---|---|
| **frontmatter** | `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next` — machine-read. No duration field; see rule 5. |
| **One-line answer** | the whole claim in one sentence, before anything else |
| **The story** | a concrete scene — a person, a machine, a failure, a decision — with no jargon at all. The hook the definition hangs on. |
| **The idea in plain language** | the concept from zero, every term defined the first time it appears, no code |
| **Why Setu needs it** | the specific later day that breaks without this |
| **The mechanism** | the runnable code, the derivation with every step shown, or the diagram |
| **Line by line** | every non-obvious token, and why it is that line and not another |
| **When it breaks** | the **real** error text, what it means, the smallest fix |
| **In production** | what changes in a real system: the professional's version, what degrades at scale, the senior reviewer's comment, the interviewer's question |
| **Check yourself** | one command to run now, one question to answer out loud |

### `level` — where a part leaves you

Every part declares one, and a well-built day climbs through them:

| `level` | You can… |
|---|---|
| `foundation` | say what the thing *is*, without using the word itself |
| `working` | use it correctly on your own data, and recognise its error messages on sight |
| `production` | say what changes when it runs in a real system — scale, concurrency, cost, failure — and defend the choice |

### The shape of every hub (`LESSON.md`)

The hub orients and assembles. **It never teaches** — there is no line-by-line walkthrough in it.

| Section | What it's for |
|---|---|
| **frontmatter** | machine-readable tracking. **`./m` and `scripts/tracker.py` read this, not you.** |
| **yesterday / today / tomorrow** | where this day sits, in one line each |
| **§1 The story** | the idea in plain English with an analogy, before any code |
| **§2 The map** | every part, what it answers, its `level` — the reading order |
| **§3 Setup — run this** | every `mkdir`, `touch`, `uv add` today needs |
| **§4 Build brief** | the file list, and which parts are yours to write (`TODO(me)`) |
| **§5 The eval** | the test that must be able to **fail** (Principle 7) |
| **§6 Request budget** | how many free-tier calls today costs (Principle 5) |
| **§7 Traps** | the mistakes that eat an evening |
| **§8 Verify before you code** | the live docs pages to check |
| **§9 Say it in an interview** | one paragraph, spoken voice |
| **§10 Done when** | pointer to `CHECKLIST.md` — defined by understanding, never by elapsed time |

---

## Why days appear one at a time

Plan v1.0.0 taught each day as a single `LESSON.md`. Those files grew past 40 000 characters, and by
Phase 15 an entire subject — deriving backpropagation — sat under one heading. Plan **v2.0.0**
replaced that format with the hub-plus-`parts/` shape above, and the v1.0.0 lessons were **deleted
rather than converted**: splitting a shallow page into shallower pages is not depth (plan Part 11.8),
so every day is rewritten from the plan itself.

That means `days/` fills up gradually. `docs/TRACKER.md` is the honest picture of how far it has got,
and `./m status` prints the one-line version.

---

## Which shell

These docs are written for **Git Bash** on Windows (installed with Git). macOS and Linux users:
everything works unchanged except the installer URLs.

| Git Bash (used in these docs) | PowerShell |
|---|---|
| `mkdir -p a/b/c` | `New-Item -ItemType Directory -Force a/b/c` |
| `touch f.py` | `if (-not (Test-Path f.py)) { New-Item -ItemType File f.py }` |
| `cat > f <<'EOF' … EOF` | `@'…'@ \| Set-Content -Encoding utf8 f` |
| `rm -rf folder` | `Remove-Item -Recurse -Force folder` |
| `./m status` | `bash ./m status` |
| `cmd1 && cmd2` | `cmd1; if ($?) { cmd2 }` |

**`make` is not used anywhere in this project.** The `./m` script replaces it.

---

## The daily rhythm

```bash
./m status         # where am I
./m start 12       # open the hub, and list its parts
./m parts 12       # just the sub-topic list
./m scaffold 12    # create days/day-12/lab/
# ... read the hub's §1 and §2, then every part in order, then implement every TODO(me) ...
./m check          # ruff + offline pytest + the depth contract
./m done 12        # refuses until the checklist is ticked and checks are green
```

## Generating the days that aren't written yet

`docs/TRACKER.md` lists every day, its status, and how many sub-topic documents it has. To write the
next one:

```
/day-setu 12
```

That skill (`.claude/skills/day-setu/SKILL.md`) reads the plan, the index, the tracker, the existing
days, and produces the hub, the `parts/` documents, the lab scaffold and the checklist in the
format above. It ends by running `./m depth 12`, which is what stops a thin day
from being called written.
