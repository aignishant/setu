---
day: 0
phase: 0
phase_name: "Foundry"
title: "Day 0 — the toolchain, the skeleton, and the ./m script"
ids: []
principles: ["P1 build daily", "P4 pin everything", "P6 the notebook is a scratchpad"]
kind: setup
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 0 — the toolchain, the skeleton, and the `./m` script

**Phase 0 · Foundry** · This day has no curriculum IDs. It exists so Day 1 can start with work
instead of installation.

> **Yesterday:** nothing.
> **Today:** four tools installed, one folder created, one script written. No Python code yet.
> **Tomorrow:** the version pins, backed by evidence you generate yourself.

**Time:** 60–90 minutes, most of it downloads.

---

## §1 The story

There is a version of this project where you install things as you need them. On Day 26 you need
pandas, so you install pandas. On Day 155 you need a vector database, so you install that.

That version fails on about Day 40, and here is exactly how. You will have three Python
installations on your machine — one from python.org, one that came with an IDE, one from a `conda`
you tried once. `pip install pandas` will put pandas into one of them. `python script.py` will run a
different one. You will spend an evening on an `ImportError` for a package you can see in your file
explorer.

So today you do the boring thing: **one tool that owns the environment, one folder that owns the
work, one command that owns the routine.**

- **`uv`** owns the environment. It creates the virtual environment, installs packages, writes the
  lockfile, and runs your code — all in one binary. You will never type `pip` in this project.
- **`setu/`** owns the work. Every file you write for 240 days lands inside it.
- **`./m`** owns the routine. `./m start 4`, `./m check`, `./m done 4`. Three commands, every day,
  for 240 days. When a habit is one word long, you keep it.

That is the whole day.

---

## §2 Install the four tools

You are on **Windows 11**. Everything in these 241 documents is written for **Git Bash**, which
comes with Git. Open it from the Start menu after step 2.1.

> Using macOS or Linux? Every command below works unchanged except the installer URLs — use
> `brew install git` / your package manager, and the `curl` installer for `uv`.

### 2.1 Git (which gives you Git Bash)

Download and run the installer from <https://git-scm.com/download/win>. Accept the defaults, with
one exception: when it asks about the default editor, pick one you actually know.

Verify — open **Git Bash** (not PowerShell, not CMD):

```bash
git --version
```

**Line by line:**

- `git --version` — prints the installed version and, more importantly, proves Git Bash can find
  `git` on its `PATH`. If this errors, the install did not finish; nothing else today will work.

Now tell Git who you are, because every commit for 240 days carries this:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

- `--global` — writes to `~/.gitconfig`, so it applies to every repo on this machine, not just this one.
- `init.defaultBranch main` — new repos start on `main` instead of `master`. Set it once now; it
  removes a warning you would otherwise see 240 times.

### 2.2 `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- `curl -LsSf <url>` — download. `-L` follows redirects, `-s` is silent, `-S` still shows real
  errors, `-f` fails on an HTTP error instead of piping an HTML error page into your shell.
- `| sh` — run the downloaded script. (Piping the internet into a shell deserves suspicion in
  general; `astral.sh` is the official installer domain for `uv`, which is why the URL is written out
  in full here rather than shortened.)

Close Git Bash and reopen it, then:

```bash
uv --version
```

Reopening is not optional — the installer edits your `PATH`, and a shell reads `PATH` once, at start.

### 2.3 Python 3.12, managed by `uv`

```bash
uv python install 3.12
uv python list
```

- `uv python install 3.12` — downloads a standalone CPython 3.12 that `uv` manages. It does not
  touch, replace, or fight with any Python already on your machine. That isolation is the point.
- `uv python list` — shows every interpreter `uv` can see. You should see a 3.12 entry.

**Why 3.12 and not the newest release:** `numpy` needs ≥ 3.12, and `tensorflow` currently caps at
3.13. 3.12 sits comfortably inside every window this plan needs (`docs/PINS_DS.md` has the table).
Being one minor version behind the bleeding edge is a feature in a 240-day project.

### 2.4 An editor

Use whatever you already know. If you have no preference, VS Code (<https://code.visualstudio.com>)
plus the official **Python** and **Ruff** extensions is the path of least friction, and it opens
`.md` lessons with a preview pane so you can read a lesson beside your terminal.

---

## §3 Create the skeleton

```bash
cd ~/OneDrive/Desktop/Projects
mkdir -p setu
cd setu
```

- `cd ~/OneDrive/Desktop/Projects` — `~` is your Windows home folder in Git Bash. Adjust the path if
  your projects live elsewhere.
- `mkdir -p setu` — `-p` means "no error if it already exists", which makes the command safe to re-run.

Now the folders:

```bash
mkdir -p src/setu tests days docs/adr data/raw data/processed notebooks scripts
touch src/setu/__init__.py tests/__init__.py
touch README.md
```

- `src/setu/` — **the library.** Every function that survives past the day it was written lives here.
- `tests/` — mirrors `src/`. One test module per source module.
- `days/` — the 241 lesson folders.
- `docs/adr/` — decision records. Thirteen of them by Day 240.
- `data/raw/` — downloaded, never edited. `data/processed/` — generated, always reproducible.
- `notebooks/` — the scratchpad (Principle 6). Nothing in here is a deliverable.
- `src/setu/__init__.py` — the empty file that makes `setu` an importable package.

### 3.1 `.gitignore` — before anything secret exists

```bash
cat > .gitignore <<'EOF'
.venv/
__pycache__/
*.py[cod]
.env
.ipynb_checkpoints/
data/raw/
data/processed/
mlruns/
.chroma/
*.db
.ruff_cache/
.pytest_cache/
EOF
```

- `cat > .gitignore <<'EOF' … EOF` — a heredoc: everything between the marker lines is written to the
  file literally. The **quotes** around `'EOF'` matter: they stop the shell expanding `$` or backticks
  inside the block.
- `.env` — the file that will hold your API keys tomorrow. It is ignored *before* it exists. That
  ordering is deliberate and it is the whole point of doing this now.
- `data/raw/` — datasets are not source code. A `SOURCE.md` describing where the data came from
  **is** committed (Principle 9); the gigabytes are not.

### 3.2 Initialise the repo and the environment

```bash
git init
uv init --python 3.12 --no-workspace
uv add "python-dotenv==1.2.3"
uv add --dev "ruff==0.16.4" "pytest==9.1.1"
```

- `uv init` — writes a starter `pyproject.toml` pinned to the 3.12 you installed.
- `uv add "<pkg>==<version>"` — installs, records the exact pin in `pyproject.toml`, **and** updates
  `uv.lock`. Three effects, one command. That third effect is why you never use `pip install` here:
  `pip` installs without writing anything down.
- `--dev` — puts ruff and pytest in the dev dependency group, so they are not dependencies of the
  thing you ship.
- `==` — exact. Not `>=`, not `~=`. Principle 4: a range is a wish, not a pin.

Check it landed:

```bash
cat pyproject.toml
```

You should see `requires-python` around 3.12 and your three pinned packages.

---

## §4 The `./m` script

`make` is not installed on Windows and is not used anywhere in this project. `./m` replaces it.

```bash
cat > m <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

DAY="${2:-}"
pad() { printf "%02d" "$1"; }

case "${1:-help}" in
  start)
    [ -z "$DAY" ] && { echo "usage: ./m start <day>"; exit 1; }
    D="days/day-$(pad "$DAY")"
    [ -d "$D" ] || { echo "no lesson at $D"; exit 1; }
    echo "→ open $D/LESSON.md"
    ;;
  scaffold)
    [ -z "$DAY" ] && { echo "usage: ./m scaffold <day>"; exit 1; }
    mkdir -p "days/day-$(pad "$DAY")/lab"
    echo "→ created days/day-$(pad "$DAY")/lab"
    ;;
  check)
    uv run ruff check .
    uv run ruff format --check .
    uv run python -m pytest -q -m "not live"
    echo "✅ all green"
    ;;
  status)
    last=$(git log --oneline --grep='^day-' -1 --pretty=%s 2>/dev/null || echo "none")
    echo "last completed: $last"
    ;;
  done)
    [ -z "$DAY" ] && { echo "usage: ./m done <day>"; exit 1; }
    C="days/day-$(pad "$DAY")/CHECKLIST.md"
    if grep -q '^\- \[ \]' "$C"; then
      echo "❌ unticked boxes remain in $C"; grep -n '^\- \[ \]' "$C"; exit 1
    fi
    "$0" check
    git add -A && git commit -m "day-$(pad "$DAY"): complete"
    echo "✅ day $DAY committed"
    ;;
  *)
    echo "usage: ./m {start|scaffold|check|status|done} [day]"
    ;;
esac
EOF
chmod +x m
```

**Line by line, the parts that matter:**

- `set -euo pipefail` — the four-character habit that makes bash safe. `-e` exit on any error,
  `-u` error on an undefined variable, `-o pipefail` make a pipeline fail if *any* stage fails, not
  just the last one. Without `pipefail`, `uv run pytest | tee log` reports success when pytest fails.
- `DAY="${2:-}"` — the second argument, defaulting to empty. Without `:-` this would trip `-u`.
- `pad()` — `printf "%02d"` turns `4` into `04` so `day-04` sorts correctly next to `day-40`.
- `-m "not live"` — skips any test marked `live` (one that hits a real API). CI runs this. Your
  free-tier quota is never spent by a test run (Principle 5).
- The `done` branch **refuses to commit while any `- [ ]` remains**, and refuses again if `check` is
  red. That refusal is the entire value of the script. A checklist you can skip is decoration.
- `chmod +x m` — marks the file executable so `./m` works instead of `bash m`.

Try it:

```bash
./m check
```

It should pass trivially — there is no code yet — and print `✅ all green`.

---

## §5 The README stub

```bash
cat > README.md <<'EOF'
# Project Setu

A 240-day journey from Python to a multi-agent research system.
Plan: `docs/00_MASTER_PLAN_DS_GENAI.md` · Index: `docs/CURRICULUM_INDEX_DS.md`

## Daily rhythm
```bash
./m status      # which day is next
./m start N     # open today's lesson
./m scaffold N  # create today's lab folder
./m check       # lint + format + offline tests
./m done N      # refuses to commit until the checklist is ticked and checks are green
```
EOF
```

On Day 239 this file becomes your portfolio. Today it is four lines. That is fine — it grows with
the repo instead of being written from a blank page at the end.

---

## §6 Commit

```bash
git add -A
git commit -m "day-00: toolchain, skeleton, ./m"
git status --porcelain
```

- `git add -A` — stage everything, including deletions.
- `git status --porcelain` — machine-readable status. **Empty output means a clean tree.** Get used
  to reading this: if `.env` ever shows up here in a later phase, stop and fix `.gitignore` before
  doing anything else.

---

## §7 Traps

- **Running these commands in PowerShell.** `mkdir -p`, `touch`, heredocs and `chmod` are Git Bash.
  In PowerShell they either error or, worse, do something subtly different.
- **Installing packages with `pip` out of habit.** `pip install X` puts X in the environment and
  writes it down nowhere. On Day 100 you will not know why your code works and CI's does not.
- **Skipping `.gitignore` "for now".** A key in git history outlives the commit that deleted it.
  §3.1 runs before §3.2 for exactly this reason.
- **Committing `data/raw/`.** A 400 MB CSV in git history is permanent and makes every future clone slow.
- **Editing `m` without `chmod +x` afterwards** — it survives edits, but not a delete-and-recreate.
- **Putting real work in `notebooks/`.** Principle 6. A notebook cell that matters graduates to
  `src/setu/` with a test, the same day.

---

## §8 Verify before you code

This lesson was written **2026-08-21**. Check these before you start:

- <https://docs.astral.sh/uv/> — the `uv` CLI surface moves fast; confirm `uv init`, `uv add`,
  `uv python install` still have these flags.
- <https://git-scm.com/download/win> — current Git for Windows installer.
- `docs/PINS_DS.md` — and note that Day 1's whole job is to re-verify it.

---

## §9 Say it in an interview

> "The repo is uv-managed on a pinned Python, with a lockfile committed. There's a three-command
> daily loop — start, check, done — and `done` physically refuses to commit while the day's checklist
> has an unticked box or the lint-and-test gate is red. That sounds like ceremony, but it's the
> reason there are 240 green commits and not 240 half-finished branches."

---

## §10 Done when

Tick every box in [`CHECKLIST.md`](CHECKLIST.md), then move to
[`../day-01/LESSON.md`](../day-01/LESSON.md).
