# 📅 days/ — the 241 written days

**Never done this before?** Start at [`day-00-setup/LESSON.md`](day-00-setup/LESSON.md).
**Already set up?** Run `./m status`, it tells you where you are.
**Want the map?** [`../docs/CURRICULUM_INDEX_DS.md`](../docs/CURRICULUM_INDEX_DS.md).
**Want progress?** [`../docs/TRACKER.md`](../docs/TRACKER.md).

---

## The four rules these docs follow

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

4. **One idea per document.** *(new in plan v2.0.0 — Principle 16)*
   A day is not one long page. It is a short hub plus one document per subtopic, in `parts/`. If a
   document needs the word "also" to introduce its second half, it should have been two documents.

---

## What's in a day folder

```
days/day-NN/
├── LESSON.md      # the hub — the story, the map of parts, setup, build brief, the eval, the budget
├── CHECKLIST.md   # the definition of done. `./m done NN` refuses to commit until it's ticked.
├── parts/         # THE TEACHING — one document per subtopic
│   ├── 1.1-<slug>.md
│   ├── 1.2-<slug>.md
│   └── 2.1-<slug>.md
├── _legacy/       # the old v1.0.0 single-file lesson, kept until the day is regenerated
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

### The shape of every part document

Eight sections, always in this order. This is the depth contract (plan Part 11.3), and
`./m depth NN` fails the day if any of them is missing.

| Section | What it's for |
|---|---|
| **frontmatter** | `day`, `part`, `title`, `ids`, `reading_minutes`, `prev`, `next` — machine-read |
| **One-line answer** | the whole claim in one sentence, before anything else |
| **The idea in plain language** | analogy first, jargon defined on first use, no code |
| **Why Setu needs it** | the specific later day that breaks without this |
| **The mechanism** | the runnable code, the derivation, or the diagram |
| **Line by line** | every non-obvious token, and why it is that line and not another |
| **When it breaks** | the **real** error text, what it means, the smallest fix |
| **Check yourself** | one command to run now, one question to answer out loud |

### The shape of every hub (`LESSON.md`)

The hub orients and assembles. **It never teaches** — there is no line-by-line walkthrough in it.

| Section | What it's for |
|---|---|
| **frontmatter** | machine-readable tracking. **`./m` and `scripts/tracker.py` read this, not you.** |
| **yesterday / today / tomorrow** | where this day sits, in one line each |
| **§1 The story** | the idea in plain English with an analogy, before any code |
| **§2 The map** | every part, what it answers, how long it takes — the reading order |
| **§3 Setup — run this** | every `mkdir`, `touch`, `uv add` today needs |
| **§4 Build brief** | the file list, and which parts are yours to write (`TODO(me)`) |
| **§5 The eval** | the test that must be able to **fail** (Principle 7) |
| **§6 Request budget** | how many free-tier calls today costs (Principle 5) |
| **§7 Traps** | the mistakes that eat an evening |
| **§8 Verify before you code** | the live docs pages to check |
| **§9 Say it in an interview** | one paragraph, spoken voice |
| **§10 Done when** | pointer to `CHECKLIST.md` |

---

## About `_legacy/`

Plan v1.0.0 taught each day as a single `LESSON.md`. Those files grew to 40 000 characters, and by
Phase 15 an entire subject — deriving backpropagation — sat under one heading. Plan **v2.0.0**
replaced that format with the hub-plus-`parts/` shape above.

The 133 v1.0.0 lessons were **moved, not deleted**, to `days/day-NN/_legacy/LESSON.md` on
2026-08-22. Days are being regenerated from Day 0 forward.

- A day with `parts/` is on the current format. Read `LESSON.md`.
- A day with only `_legacy/` still works — read `_legacy/LESSON.md` — but it has not been split or
  deepened yet. `./m start N` will tell you which one you are looking at, and `docs/TRACKER.md`
  marks it 🗃️ legacy.

When a day is regenerated its `_legacy/` folder is deleted, because the content has by then been
mined into the parts.

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
days and any `_legacy/` draft, and produces the hub, the `parts/` documents, the lab scaffold and
the checklist in the format above. It ends by running `./m depth 12`, which is what stops a thin day
from being called written.
