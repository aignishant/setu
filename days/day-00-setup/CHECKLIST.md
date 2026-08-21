# Day 0 — CHECKLIST

**IDs covered:** none (toolchain) · **Principles served:** 1, 4, 6

## Demo command

```bash
./m check && git log --oneline -1
```

Expected: `✅ all green`, followed by one commit reading `day-00: toolchain, skeleton, ./m`.

## Tools

- [ ] Git installed; **Git Bash** opens from the Start menu
- [ ] `git --version` prints a version *inside Git Bash*
- [ ] `git config --global user.name` / `user.email` / `init.defaultBranch main` set
- [ ] `uv --version` prints a version (after reopening the shell)
- [ ] `uv python install 3.12` succeeded and `uv python list` shows a 3.12 entry
- [ ] Editor installed, with Python + Ruff extensions if using VS Code

## Skeleton

- [ ] `setu/` created in your Projects folder
- [ ] Folders exist: `src/setu/`, `tests/`, `days/`, `docs/adr/`, `data/raw/`, `data/processed/`, `notebooks/`, `scripts/`
- [ ] `src/setu/__init__.py` and `tests/__init__.py` exist (empty is correct)
- [ ] **`.gitignore` written *before* `.env` will ever exist** — and it contains a line that is exactly `.env`
- [ ] `git init` run
- [ ] `uv init --python 3.12` run; `pyproject.toml` exists with `requires-python` around 3.12

## Pins (Principle 4)

- [ ] `python-dotenv==1.2.3` added with `uv add` — appears in `pyproject.toml`
- [ ] `ruff==0.16.4` and `pytest==9.1.1` added with `uv add --dev`
- [ ] Every version uses `==`, not `>=` or `~=`
- [ ] `uv.lock` exists and is staged

## The `./m` script

- [ ] `m` written and `chmod +x m` applied
- [ ] `./m check` prints `✅ all green`
- [ ] `./m status` runs without error
- [ ] Read the `done` branch and can say **out loud** what makes it refuse

## Commit

- [ ] `git add -A && git commit -m "day-00: toolchain, skeleton, ./m"` made
- [ ] `git status --porcelain` prints **nothing**
- [ ] `.env` does **not** appear anywhere in `git ls-files`

## Understanding check — answer out loud

- [ ] Why does this project never use `pip install`?
- [ ] Why was `.gitignore` written before `.env` rather than after?
- [ ] What does `set -euo pipefail` protect you from that plain `set -e` does not?
- [ ] Why does `./m check` pass `-m "not live"` to pytest?
- [ ] What is the difference between `data/raw/` and `data/processed/`, and why is only one of them regenerable?
