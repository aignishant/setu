# Day 1 — CHECKLIST

**IDs covered:** none (Phase-0 infrastructure) · **Principles served:** 1, 4, 9, 14

## Demo command

```bash
uv run python days/day-01/lab/verify_pins.py | head -5
uv run python -m pytest -q
```

Expected: a dated PyPI report, then all tests green.

## Setup

- [ ] `./m start 1` and `./m scaffold 1` run
- [ ] Files created: `days/day-01/lab/verify_pins.py`, `src/setu/paths.py`, `src/setu/versions.py`, `tests/test_paths.py`, `tests/test_versions.py`, `docs/CHANGELOG_PLAN_DS.md`
- [ ] **No new packages installed today** — `pyproject.toml` is unchanged from Day 0

## Evidence (Principles 4 & 9)

- [ ] `verify_pins.py` written and runs clean
- [ ] Output saved to `days/day-01/lab/pins-<today>.txt` with `tee` — and **committed**
- [ ] Every line of your output compared against the table in `docs/PINS_DS.md`
- [ ] Each difference classified: none / patch / minor / major / missing
- [ ] Patch drift → pinned and logged in `docs/CHANGELOG_PLAN_DS.md`
- [ ] Minor or major drift → **addendum written before pinning** (or "none" recorded explicitly)
- [ ] `docs/CHANGELOG_PLAN_DS.md` has a `v1.0.0` entry and a Day-1 verification entry

## Code

- [ ] `src/setu/paths.py` written — `ROOT`, `RAW`, `PROCESSED`, `ensure_dirs()`
- [ ] Counted the `parents[2]` levels **by hand** and confirmed against the repo layout
- [ ] `src/setu/versions.py` written — `PINNED`, `installed()`, `drift()`
- [ ] `PINNED` filled from **your own run**, not from the docs table
- [ ] No module in `src/setu/` does anything at import time except define names

## Tests that must be able to fail

- [ ] `test_root_is_the_repo_root` — green
- [ ] **Changed `parents[2]` to `parents[1]`, watched it go red, changed it back** ← do not skip this
- [ ] `test_data_dirs_are_under_root` — green
- [ ] `test_ensure_dirs_is_idempotent` — green, and does not touch the real `data/`
- [ ] `test_no_drift_between_pinned_and_installed` — green
- [ ] `test_pinned_versions_are_exact` — green (add `">=1.0"` to `PINNED` temporarily and confirm it goes red)
- [ ] `uv run python -m pytest -q` run from **inside `days/`** and still green

## Budget

- [ ] Actual PyPI request count logged (should be ~36, run once)
- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does this project regenerate the version table instead of trusting `docs/PINS_DS.md`?
- [ ] What exactly breaks under pandas 3.0's Copy-on-Write, and why is *silence* worse than an exception?
- [ ] Why does `latest()` set a `timeout`, and what happens without one?
- [ ] Why is the `except` in `verify_pins.py` broad while the one in `versions.py` is narrow?
- [ ] Why does `main()` return an exit code instead of calling `sys.exit()` itself?
- [ ] Why must `ensure_dirs()` be a function rather than top-level code?
- [ ] What does `if __name__ == "__main__":` buy you here specifically?

## Commit

```bash
./m check
./m done 1
```

- [ ] `./m done 1` succeeded — commit made, evidence file included
