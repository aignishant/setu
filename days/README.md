# 📅 days/ — the 241 written days

**Never done this before?** Start at [`day-00-setup/LESSON.md`](day-00-setup/LESSON.md).
**Already set up?** Run `./m status`, it tells you where you are.
**Want the map?** [`../docs/CURRICULUM_INDEX_DS.md`](../docs/CURRICULUM_INDEX_DS.md).
**Want progress?** [`../docs/TRACKER.md`](../docs/TRACKER.md).

---

## The three rules these docs follow

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

## What's in a day folder

```
days/day-NN/
  LESSON.md      # the teaching + every line of code + every command
  CHECKLIST.md   # the definition of done. `./m done NN` refuses to commit until it's ticked.
  lab/           # you create this; `./m scaffold NN` makes the folder
```

### The shape of every LESSON.md

| Section | What it's for |
|---|---|
| **frontmatter** | machine-readable tracking. **`./m` and `scripts/tracker.py` read this, not you.** |
| **yesterday / today / tomorrow** | where this day sits, in one line each |
| **§1 The story** | the idea in plain English with an analogy, before any code |
| **§2 Setup — run this** | every `mkdir`, `touch`, `uv add` today needs |
| **per-ID sections** | plain idea → why Setu needs it → the code → **line by line** → how it breaks |
| **Build brief** | the file list, and which parts are yours to write (`TODO(me)`) |
| **The eval** | the test that must be able to **fail** (Principle 7) |
| **Request budget** | how many free-tier calls today costs (Principle 5) |
| **Traps** | the mistakes that eat an evening |
| **Verify before you code** | the live docs pages to check — these files were written 2026-08-21 |
| **Say it in an interview** | one paragraph, spoken voice |
| **Done when** | pointer to `CHECKLIST.md` |

---

## The daily rhythm

```bash
./m status         # where am I
./m start 12       # open today's lesson
./m scaffold 12    # create days/day-12/lab/
# ... work through the lesson, implement every TODO(me) ...
./m check          # ruff + offline pytest
./m done 12        # refuses until the checklist is ticked and checks are green
```

## Generating the days that aren't written yet

`docs/TRACKER.md` lists every day and its status. To write the next one:

```
/day-setu 12
```

That skill (`.claude/skills/day-setu/SKILL.md`) reads the plan, the index, the tracker and the
existing days, and produces the lesson, the lab scaffold and the checklist in this exact format.
