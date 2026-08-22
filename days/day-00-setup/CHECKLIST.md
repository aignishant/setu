# Day 0 — CHECKLIST

**IDs covered:** none (toolchain) · **Principles served:** 1, 4, 5, 6, 7, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 15, in [`parts/`](parts/)

> `./m done 0` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see [3.3](parts/03/3.3-the-done-gate.md).
>
> **There is no time budget on this day.** Work through it across as many sittings as it takes
> (Principle 17). Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
./m check && git log --oneline -1 && uv run python scripts/depth_check.py 0
```

Expected: `OK all green`, one commit reading `day-00: toolchain, skeleton, ./m`, and the depth check
reporting the day's parts.

---

## Section 1 — the tools that own things

- [ ] Read [1.1 — why one tool must own the environment](parts/01/1.1-why-one-tool-owns-the-environment.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — Git and Git Bash](parts/01/1.2-git-and-git-bash.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `uv`, the one binary](parts/01/1.3-uv-the-one-binary.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — Python 3.12 under `uv`](parts/01/1.4-python-3-12-under-uv.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — the editor and the interpreter trap](parts/01/1.5-the-editor-and-the-interpreter-trap.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] `git --version` prints a version **inside Git Bash** (not PowerShell)
- [ ] `git config --global --list` shows `user.name`, `user.email`, `init.defaultBranch=main`, and (on Windows) `core.autocrlf=input`
- [ ] `uv --version` prints a version **after reopening the shell**
- [ ] `uv python list` shows a 3.12 entry
- [ ] `uv run --python 3.12 python -c "import sys; print(sys.version_info[:2])"` prints `(3, 12)`
- [ ] The editor's interpreter path and `uv run python -c "import sys; print(sys.executable)"` print the **same string**

## Section 2 — the skeleton on disk

- [ ] Read [2.1 — the folder skeleton](parts/02/2.1-the-folder-skeleton.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `.gitignore` before secrets exist](parts/02/2.2-gitignore-before-secrets-exist.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `git init` and what a repo is](parts/02/2.3-git-init-and-what-a-repo-is.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `uv init`, `pyproject.toml`, the lockfile](parts/02/2.4-uv-init-pyproject-and-the-lockfile.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — the `.venv` you never activate](parts/02/2.5-the-venv-you-never-activate.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Eight folders exist and `src/setu/__init__.py` + `tests/__init__.py` are present
- [ ] `.gitignore` was written **before** `git init` and before any `.env` existed
- [ ] `git check-ignore -v .env` names the rule that ignores it
- [ ] `git check-ignore -v .env.example` prints **nothing** — the negation works
- [ ] `cat .git/HEAD` prints `ref: refs/heads/main`, and you can say why it is a branch name and not a hash
- [ ] `pyproject.toml` has `requires-python = "==3.12.*"` and every dependency uses `==`
- [ ] `uv.lock` exists and holds **more** packages than you asked for (the transitive ones)
- [ ] `rm -rf .venv && uv sync --frozen` rebuilds the environment and `uv run python -c "import dotenv"` works
- [ ] `echo "$VIRTUAL_ENV"` is **empty** while `uv run python` still finds the project interpreter

## Section 3 — the script that owns the routine

- [ ] Read [3.1 — `set -euo pipefail`](parts/03/3.1-set-euo-pipefail.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — the `case` dispatcher](parts/03/3.2-the-case-dispatcher.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — the `done` gate](parts/03/3.3-the-done-gate.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the `-e` demo and watched `step 2` stop printing when `set -e` was added
- [ ] Ran the `pipefail` demo and watched the same pipeline report `0`, then `1`
- [ ] `ls -l m` shows the executable bit, and `./m` with no arguments prints usage
- [ ] `./m nonsense-command` prints usage and does **not** half-do anything
- [ ] **Watched the gate refuse:** left a box unticked, ran `./m done 0`, saw `FAIL unticked boxes remain` with line numbers, and confirmed `git log` gained no commit

## Section 4 — closing the day

- [ ] Read [4.1 — the README that grows](parts/04/4.1-the-readme-that-grows.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the first commit](parts/04/4.2-the-first-commit.md), ran its check-yourself, answered its out-loud question

---

## Build brief — the reps that are yours

- [ ] **Typed** `m` from [3.2](parts/03/3.2-the-case-dispatcher.md) and [3.3](parts/03/3.3-the-done-gate.md) — not copied from this repository
- [ ] Wrote `README.md` with **your own** one-sentence description, not the example's
- [ ] Created `tests/test_setup.py` with the three `TODO(me)` bodies from the hub's §4
- [ ] Implemented `test_pins_are_exact` yourself
- [ ] Implemented `test_env_file_is_ignored` yourself
- [ ] Implemented `test_daily_driver_is_executable` yourself

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_setup.py -v` **before** implementing, and watched all three fail with `NotImplementedError`
- [ ] All three pass after implementing
- [ ] **Break it, watch it go red, fix it —** changed a pin from `==` to `>=`, saw `test_pins_are_exact` go red, restored it
- [ ] **Break it, watch it go red, fix it —** commented out `.env` in `.gitignore`, saw `test_env_file_is_ignored` go red, restored it
- [ ] **Break it, watch it go red, fix it —** removed `set -euo pipefail` from `m`, saw `test_daily_driver_is_executable` go red, restored it
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls made today — confirmed, because no keys exist yet
- [ ] **$0** spent, no card on file anywhere (Principle 5)

## Understand it out loud

Say each of these to an empty room, in your own words, without re-reading:

- [ ] Why `pip install pandas` can succeed while `import pandas` fails — using *interpreter*, *site-packages* and *PATH*
- [ ] Why this project pins Python 3.12 rather than the newest release — using *wheel*, *floor* and *ceiling*
- [ ] What is in `.git`, and why a branch is not a copy of the code
- [ ] Why `.gitignore` was written before `git init`, and what you would do **first** if a key were pushed
- [ ] The difference between `pyproject.toml` and `uv.lock`, and why committing one without the other is a bug
- [ ] What `activate` actually does, and why this project never uses it
- [ ] Each of `-e`, `-u`, `-o pipefail` and the silent failure it prevents
- [ ] Why a gate that refuses beats a checklist that reminds

## Commit

- [ ] `git status --porcelain` read **before** staging — `.env`, `.venv/` and `data/` do not appear
- [ ] `git ls-files` confirms what is tracked, and nothing secret or generated is in it
- [ ] `uv run python scripts/depth_check.py 0` passes
- [ ] `./m done 0` ran green and created the commit
