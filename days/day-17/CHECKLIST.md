# Day 17 — CHECKLIST

**IDs covered:** PY-21 · **Principles served:** 1, 6, 7

## Demo command

```bash
uv run python days/day-17/lab/imports.py
uv run python -m pytest tests/test_package.py -v
```

Expected: the import report, then all package-structure tests green.

## Setup

- [ ] `./m start 17` and `./m scaffold 17` run
- [ ] Files created: `days/day-17/lab/imports.py`, `src/setu/text/`, `tests/test_package.py`
- [ ] No new packages installed

## PY-21 — the import system

- [ ] Can list the **four** steps an import performs
- [ ] Confirmed two imports of the same module give the **same object**
- [ ] Inspected `sys.modules` and `sys.path`
- [ ] Used all three import forms and confirmed they reach the same function object
- [ ] Understood that `from X import y` still executes **all** of X
- [ ] Read `__name__`, `__file__`, `__package__` on a real module
- [ ] Can explain the circular-import failure **step by step**, without notes
- [ ] Can name three things that must never happen at module level

## Layering

- [ ] `src/setu/ARCHITECTURE.md` written with the four-layer table
- [ ] Every existing module placed in a layer
- [ ] Can state the one rule: **imports point downward only**

## The `text` subpackage

- [ ] `src/setu/text/{__init__,clean,split}.py` created
- [ ] Cleaning functions moved to `clean.py`; splitting functions to `split.py`
- [ ] `text/__init__.py` re-exports the public surface
- [ ] `__all__` written and matches what is re-exported
- [ ] Can explain what re-exporting buys you when you reorganise later

## Top-level `__init__.py`

- [ ] `src/setu/__init__.py` has a docstring and `__version__` and **nothing else**
- [ ] Can explain why a fat top-level `__init__.py` is a problem by Day 155

## Migration (in order, checking after each step)

- [ ] 1. `text/` package created
- [ ] 2. `textutils.py` made a temporary shim
- [ ] 3. Every import in `src/` and `tests/` updated to `from setu.text import ...`
- [ ] 4. **`textutils.py` deleted** and removed from `LAYERS`
- [ ] 5. Full suite green

## Tests that must be able to fail

- [ ] `test_no_upward_imports` — green ← **today's real assessment**
- [ ] **Added `from setu.loaders import BaseLoader` to `papers.py`, watched it go red, removed it** ← do not skip
- [ ] `test_every_module_imports_cleanly_on_its_own` — green
- [ ] **Added `KEYS = load_keys()` at module level in `papers.py`, watched the subprocess test go red, removed it** ← do not skip
- [ ] `test_importing_setu_is_cheap` — green
- [ ] `test_text_package_reexports_everything_in_all` — green
- [ ] `test_no_wildcard_imports` — green (red during step 2, green after step 4)
- [ ] `test_no_sys_path_manipulation` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are the four steps of an import?
- [ ] Why does a module body run only once per process?
- [ ] Walk through a circular import and say exactly where it fails
- [ ] Why is a local import inside a function a *bad* fix for a circular import?
- [ ] Why must the layering test parse the AST instead of importing the module?
- [ ] Why must the import test run in a **fresh subprocess**?
- [ ] Why does this project use absolute imports rather than relative ones?

## Commit

- [ ] `./m check && ./m done 17` succeeded
