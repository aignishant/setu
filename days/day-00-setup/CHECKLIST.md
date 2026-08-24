# Day 0 — definition of done

`./m done 0` refuses to commit while any box below is unticked. That refusal is the whole point
(part [3.3](parts/03-m-script/3.3-the-done-gate.md)) — and so is not ticking a box you did not do.
Nothing here is a time estimate; a box is ticked when the thing is true, however many sittings that
took.

**Demo command — the whole day in one line:**

```bash
./m check && git log --oneline -1
```

---

## The parts — read, run, answer

One box per document in `parts/`. Tick it when you have read it, run its **Check yourself**
command, and answered its out-loud question *without scrolling back up*.

### Section 1 — the tools that own things

- [x] [1.1 Why one tool must own the environment](parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md)
- [x] [1.2 Git, and why a Unix shell on a Windows machine](parts/01-toolchain/1.2-git-and-git-bash.md)
- [x] [1.3 `uv`, the one binary](parts/01-toolchain/1.3-uv-the-one-binary.md)
- [x] [1.4 Python 3.12, and why not the newest](parts/01-toolchain/1.4-python-3-12-under-uv.md)
- [x] [1.5 The editor, and the interpreter trap](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md)

### Section 2 — the skeleton on disk

- [x] [2.1 The folder skeleton](parts/02-skeleton/2.1-the-folder-skeleton.md)
- [x] [2.2 `.gitignore`, before anything secret exists](parts/02-skeleton/2.2-gitignore-before-secrets-exist.md)
- [x] [2.3 `git init`, and what a repository is](parts/02-skeleton/2.3-git-init-and-what-a-repo-is.md)
- [x] [2.4 `uv init`, `pyproject.toml`, and the lockfile](parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md)
- [x] [2.5 The `.venv` you never activate](parts/02-skeleton/2.5-the-venv-you-never-activate.md)

### Section 3 — the script that owns the routine

- [x] [3.1 `set -euo pipefail`](parts/03-m-script/3.1-set-euo-pipefail.md)
- [x] [3.2 The `case` dispatcher](parts/03-m-script/3.2-the-case-dispatcher.md)
- [x] [3.3 The `done` gate](parts/03-m-script/3.3-the-done-gate.md)

### Section 4 — closing the day

- [x] [4.1 The README that grows](parts/04-first-commit/4.1-the-readme-that-grows.md)
- [x] [4.2 The first commit, and reading a clean tree](parts/04-first-commit/4.2-the-first-commit.md)

---

## Setup — verified on disk

Each of these is checkable by a command, and each was checked.

- [x] Git configured — `user.name`, `user.email`, `core.autocrlf input`
- [x] `git config --global init.defaultBranch main` — set. It only decides the branch name of
      the *next* repo you create; this one was already on `main`.
- [x] `uv` installed and on `PATH` in a **reopened** shell — `uv --version`
- [x] Python 3.12 installed under `uv`, and `requires-python = "==3.12.*"` in `pyproject.toml`
- [x] Skeleton exists: `src/setu/`, `tests/`, `days/`, `docs/adr/`, `data/raw/`,
      `data/processed/`, `notebooks/`, `scripts/`, `.vscode/`
- [x] `src/setu/__init__.py` and `tests/__init__.py` exist
- [x] `.gitignore` written **before** `git init` — it ignores `.env` and `.env.*`, and re-includes
      `!.env.example`
- [x] `.env.example` is committed and `.env` is not — `git check-ignore -v .env`
- [x] `git init` done; the repository is on `main`
- [x] `uv init` done; `pyproject.toml` **and** `uv.lock` are both committed
- [x] Every dependency pinned with `==`: `python-dotenv==1.2.3`, `ruff==0.16.4`, `pytest==9.1.1`
      (plus `ipykernel==7.3.0`, added for `notebooks/` — also exactly pinned)
- [x] `.venv/` is ignored and never activated — every command goes through `uv run`

---

## Build brief — the three files that are yours

- [x] **`m`** exists, starts with a bash shebang, and is in strict mode (`set -euo pipefail`)
- [x] **`m`** is executable — `git ls-files -s m` shows mode `100755`, not `100644`
- [x] **`README.md`** written in your own words, not copied from the example in part 4.1
- [x] **`tests/test_setup.py`** created from the §4 skeleton
- [x] `test_pins_are_exact` — `TODO(me)` body implemented, test passes
- [x] `test_env_file_is_ignored` — `TODO(me)` body implemented, test passes
- [x] `test_daily_driver_is_executable` — `TODO(me)` body implemented, test passes

---

## The eval that must be able to fail (Principle 7)

- [x] Ran `uv run python -m pytest tests/test_setup.py -v` and watched all three go **RED** with
      `NotImplementedError` before implementing anything
- [x] **Broke `test_pins_are_exact` on purpose:** changed a pin to `>=1.2.3`, watched it go red,
      changed it back
- [x] **Broke `test_env_file_is_ignored` on purpose:** commented out the `.env` line in
      `.gitignore`, watched it go red, restored it
- [x] **Broke `test_daily_driver_is_executable` on purpose:** removed `set -euo pipefail` from `m`,
      watched it go red, put it back
- [x] `./m check` is green — ruff, ruff format, pytest, and the depth contract

---

## Budget (Principle 5)

- [x] LLM API calls today: **0**
- [x] Cost today: **$0** — no key exists yet; keys arrive on Day 3

---

## Commit

- [x] `git status --porcelain` **read** before staging, not after
- [x] `./m done 0` run, and it committed rather than refused
