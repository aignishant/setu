---
day: 0
phase: 0
phase_name: "Foundry"
title: "Day 0 — the toolchain, the skeleton, and the ./m script"
ids: []
principles: ["P1 build daily", "P4 pin everything", "P6 the notebook is a scratchpad", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: setup
plan: setu
plan_version: "v2.2.0"
parts: 15
papers: 0
generated: "2026-08-23"
status: complete
lab_scaffolded: false
commit: "4de3995"
---

# Day 0 — the toolchain, the skeleton, and the `./m` script

**Phase 0 · Foundry** · This day has no curriculum IDs. It exists so Day 1 can start with work
instead of installation.

> **Yesterday:** nothing.
> **Today:** four tools installed, one skeleton created, one script written, one commit made.
> **Tomorrow:** the version pins, backed by evidence you generate yourself.

> **Read this hub first**, then work through `parts/` in order. There is no time estimate on this
> day or any other — a day is a unit of subject, not of hours (Principle 17). Take as many sittings
> as the material needs; the definition of done is the checklist, not the clock.

---

## §1 The story

There is a version of this project where you install things as you need them. On Day 26 you need
pandas, so you install pandas. On Day 155 you need a vector database, so you install that.

That version fails around Day 40, and here is exactly how. You will have three Python installations
on your machine — one from python.org, one that came with an editor, one from a distribution you
tried once. `pip install pandas` will put pandas into one of them. `python script.py` will run a
different one. You will spend an evening on an `ImportError` for a package you can see in your file
explorer, and nothing will be broken: two words on the same keyboard will simply be pointing at two
different machines that share a disk.

That evening is not bad luck. It is what happens when **nothing owns the environment** — when the
question "which Python is this?" is answered by an accumulated list of folders that every installer
you have ever run has appended itself to.

So today you do the boring thing, and it is the whole day:

- **One tool owns the environment.** `uv` installs the interpreter, creates the environment,
  resolves and locks every package, and runs your code inside it. You will never type `pip` here.
- **One folder owns the work.** Every file you write for 240 days lands inside a skeleton where the
  *location* of a file is a claim about what it is — code that must survive, a test, an input, an
  output, or a scratchpad.
- **One script owns the routine.** `./m start 4`, `./m check`, `./m done 4`. Three commands, every
  day, for 240 days — and `done` physically refuses while a checkbox is unticked or a check is red.

Three owners, one commit at the end. Everything in the fifteen parts below is one of those three
sentences, taken apart until there is nothing left to be surprised by.

```mermaid
flowchart LR
    S1["§1 the tools<br/>who owns the environment"] --> S2["§2 the skeleton<br/>what each folder claims"]
    S2 --> S3["§3 the routine<br/>the script that refuses"]
    S3 --> S4["§4 closing<br/>the first commit"]
    style S1 fill:#1f6feb,color:#fff
    style S4 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** This is a `setup` day, so sections are the *four owners*
above, in the order you build them: **1.x** the tools that own the environment, **2.x** the skeleton
on disk, **3.x** the script that owns the daily routine, **4.x** closing the day.

Read them in order — each part names its prerequisites and builds on the one before.

### Section 1 — the tools that own things

| Part | What it answers | Level |
|---|---|---|
| [1.1 Why one tool must own the environment](parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md) | Why does `pip install pandas` succeed and `import pandas` still fail? | `foundation` |
| [1.2 Git, and why a Unix shell on a Windows machine](parts/01-toolchain/1.2-git-and-git-bash.md) | What does Git actually record, and why is every command here bash? | `foundation` |
| [1.3 `uv`, the one binary](parts/01-toolchain/1.3-uv-the-one-binary.md) | What four jobs does `uv` replace, and why is it not a Python package? | `working` |
| [1.4 Python 3.12, and why not the newest](parts/01-toolchain/1.4-python-3-12-under-uv.md) | Why is being one version behind the right call? | `working` |
| [1.5 The editor, and the interpreter trap](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md) | Why does the editor disagree with the terminal, and which one is right? | `working` |

### Section 2 — the skeleton on disk

| Part | What it answers | Level |
|---|---|---|
| [2.1 The folder skeleton](parts/02-skeleton/2.1-the-folder-skeleton.md) | What claim does each folder make, and why is the package under `src/`? | `foundation` |
| [2.2 `.gitignore`, before anything secret exists](parts/02-skeleton/2.2-gitignore-before-secrets-exist.md) | Why write it now, and why does deleting a leaked key not remove it? | `production` |
| [2.3 `git init`, and what a repository is](parts/02-skeleton/2.3-git-init-and-what-a-repo-is.md) | What is inside `.git`, and what is a branch really? | `foundation` |
| [2.4 `uv init`, `pyproject.toml`, and the lockfile](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md) | What is the difference between intent and resolution, and why commit both? | `working` |
| [2.5 The `.venv` you never activate](parts/02-skeleton/2.5-the-venv-you-never-activate.md) | What does `activate` actually do, and why does this project skip it? | `working` |

### Section 3 — the script that owns the routine

| Part | What it answers | Level |
|---|---|---|
| [3.1 `set -euo pipefail`](parts/03-m-script/3.1-set-euo-pipefail.md) | Which three silent failures does bash do by default, and how do you turn them off? | `production` |
| [3.2 The `case` dispatcher](parts/03-m-script/3.2-the-case-dispatcher.md) | How do five commands live in one file, and why one entry point? | `working` |
| [3.3 The `done` gate](parts/03-m-script/3.3-the-done-gate.md) | Why does a refusal work where a checklist does not? | `production` |

### Section 4 — closing the day

| Part | What it answers | Level |
|---|---|---|
| [4.1 The README that grows](parts/04-first-commit/4.1-the-readme-that-grows.md) | Why write it on Day 0 rather than Day 239? | `foundation` |
| [4.2 The first commit, and reading a clean tree](parts/04-first-commit/4.2-the-first-commit.md) | What do you check in the last moment before a commit becomes permanent? | `working` |

---

## §3 Setup — run this

Every command below is explained in the part named beside it. **Do not paste this section blind** —
it is the summary, not the lesson. Work through the parts; this is here so you can re-run the day
from scratch later without re-reading.

All commands are **Git Bash** (Windows) or your normal terminal (macOS/Linux).

```bash
# --- section 1: the tools (parts 1.1-1.5) ---
# Install Git from https://git-scm.com/download/win, then in Git Bash:
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input

curl -LsSf https://astral.sh/uv/install.sh | sh
# close Git Bash, reopen it, then:
uv python install 3.12

code --install-extension ms-python.python
code --install-extension charliermarsh.ruff

# --- section 2: the skeleton (parts 2.1-2.5) ---
cd ~/OneDrive/Desktop/Projects && mkdir -p setu && cd setu
mkdir -p src/setu tests days docs/adr data/raw data/processed notebooks scripts .vscode
touch src/setu/__init__.py tests/__init__.py

# .gitignore FIRST - before git init, before any key exists (part 2.2)
# .env.example, .vscode/settings.json - see parts 2.2 and 1.5 for the contents

git init
uv init --python 3.12 --no-workspace
uv add "python-dotenv==1.2.3"
uv add --dev "ruff==0.16.4" "pytest==9.1.1"

# --- section 3: the routine (parts 3.1-3.3) ---
# write ./m - the full script is in parts 3.2 and 3.3
chmod +x m
./m check

# --- section 4: closing (parts 4.1-4.2) ---
# write README.md - see part 4.1
git status --porcelain          # LOOK at this before staging
git add -A
git commit -m "day-00: toolchain, skeleton, ./m"
```

Packages pinned today, and the part that explains each:

| Package | Version | Why today |
|---|---|---|
| `python-dotenv` | `==1.2.3` | Day 3 reads API keys from `.env` — [2.4](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md) |
| `ruff` | `==0.16.4` | linter + formatter, `--dev` — [2.4](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md) |
| `pytest` | `==9.1.1` | Principle 7 needs a test runner, `--dev` — [2.4](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md) |

---

## §4 Build brief

Three files are yours to write. The parts give you every command and every concept; these are the
reps, and the `TODO(me)` markers are deliberately unsolved.

**1. `m`** — the daily driver. Parts [3.2](parts/03-m-script/3.2-the-case-dispatcher.md) and
[3.3](parts/03-m-script/3.3-the-done-gate.md) contain the full script. Type it; do not copy it from this
repository. You will edit this file a dozen times over 240 days and you cannot edit what you have
never read.

**2. `README.md`** — part [4.1](parts/04-first-commit/4.1-the-readme-that-grows.md) has the shape. Write your own
one-sentence description rather than reusing the one in the example.

**3. `tests/test_setup.py`** — the eval. Create it with this skeleton, then fill in the `TODO(me)`
bodies yourself:

```python
"""Day 0: prove the setup is real, not assumed."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_pins_are_exact() -> None:
    """Every dependency in pyproject.toml uses == and not a range (Principle 4)."""
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    # TODO(me): collect every dependency specification from the [project] and
    # [dependency-groups] blocks, and assert each one contains "==".
    # Hint: the specs are the quoted strings inside the two list literals.
    raise NotImplementedError


def test_env_file_is_ignored() -> None:
    """.env is ignored BEFORE it exists (Principle 5, part 2.2)."""
    # TODO(me): assert that .gitignore contains a rule matching .env,
    # and that .env.example is re-included.
    raise NotImplementedError


def test_daily_driver_is_executable() -> None:
    """./m exists, is executable, and is in strict mode (part 3.1)."""
    # TODO(me): assert m exists, that its first line is a bash shebang,
    # and that "set -euo pipefail" appears in the first few lines.
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

The three tests above are **red right now** — each one raises `NotImplementedError`. That is the
correct starting state (Principle 7): a test that has never been red has never proved anything.

Run them and watch them fail:

```bash
uv run python -m pytest tests/test_setup.py -v
```

Then implement the bodies until they pass. Then — and this is the box on the checklist people skip —
**break each one on purpose and watch it go red again**:

- Change a pin in `pyproject.toml` from `==1.2.3` to `>=1.2.3`. `test_pins_are_exact` must fail.
  Change it back.
- Comment out the `.env` line in `.gitignore`. `test_env_file_is_ignored` must fail. Restore it.
- Remove `set -euo pipefail` from `m`. `test_daily_driver_is_executable` must fail. Put it back.

A test that does not go red when you break the thing it guards is not a test. It is a comment that
takes longer to run.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** |
| Network requests | installers only: Git, `uv`, one Python build, three pinned packages, two editor extensions |
| Free-tier quota consumed | **none** — no keys exist yet; they arrive on Day 3 |
| Cost | **$0**, as it will be on all 240 days (Principle 5) |

---

## §7 Traps

- **Running these commands in PowerShell.** `mkdir -p`, `touch`, heredocs and `chmod` are Git Bash.
  In PowerShell they either error or, worse, do something subtly different —
  [1.2](parts/01-toolchain/1.2-git-and-git-bash.md).
- **Not reopening the terminal after installing `uv`.** A shell reads `PATH` once, at start. This is
  the most common "the installer lied to me" moment — [1.3](parts/01-toolchain/1.3-uv-the-one-binary.md).
- **Typing `pip install` out of habit.** It installs into whichever interpreter that `pip` belongs
  to, and writes nothing down — [1.1](parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md).
- **Writing `.gitignore` after `git init` and after `.env`.** The ordering in §3 is not stylistic; a
  secret committed once is permanent — [2.2](parts/02-skeleton/2.2-gitignore-before-secrets-exist.md).
- **Committing `pyproject.toml` without `uv.lock`.** The two must move together or your machine and
  CI build different environments from the same commit —
  [2.4](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md).
- **Trusting a green test run from the editor's run button.** It may be using a different
  interpreter than your terminal — [1.5](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md).
- **Forgetting `chmod +x m`.** Permissions belong to the file, not the name, so deleting and
  recreating the script loses the bit — [3.2](parts/03-m-script/3.2-the-case-dispatcher.md).
- **Running `git add -A` without reading `git status --porcelain` first.** Five seconds, every time
  — [4.2](parts/04-first-commit/4.2-the-first-commit.md).
- **Ticking a checklist box you did not do.** The gate cannot tell, which is exactly why it is worth
  nothing if you do — [3.3](parts/03-m-script/3.3-the-done-gate.md).

---

## §8 Verify before you code

This day was written **2026-08-23**. Tool interfaces move; check these against the live pages before
you start, and if something has changed, say so and amend the plan rather than working around it
(Principle 14).

- <https://docs.astral.sh/uv/> — confirm `uv init`, `uv add`, `uv python install`, `uv sync --locked`
  and `uv run` still take these flags.
- <https://git-scm.com/download/win> — the current Git for Windows installer.
- <https://docs.astral.sh/ruff/> — `ruff check` and `ruff format` interfaces.
- <https://docs.pytest.org/> — marker syntax for `-m "not live"`.
- `docs/PINS_DS.md` — and note that Day 1's entire job is to re-verify it rather than trust it.

---

## §9 Say it in an interview

> "The repository is uv-managed on a pinned Python 3.12, with a lockfile committed alongside the
> project file, so any machine rebuilds the identical environment — including transitive
> dependencies, with hashes. The package sits under `src/`, which means tests import the installed
> package rather than the folder next to them, so what I test is what ships. There's a three-command
> daily loop — start, check, done — and `done` physically refuses to commit while the day's checklist
> has an unticked box or the lint-and-test gate is red. That sounds like ceremony, but it's the
> reason there are 240 green commits and not 240 half-finished branches: the standard is enforced by
> something that doesn't have a bad week."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green — not when a
particular amount of time has passed. Then:

```bash
./m done 0
```

Day 1 re-verifies every version pin against live PyPI and freezes whatever *today* says. It is
written when you get there — `./m status` and [`../../docs/TRACKER.md`](../../docs/TRACKER.md) show
how far the plan has been written out.
