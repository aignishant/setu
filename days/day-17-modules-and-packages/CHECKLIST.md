# Day 17 — CHECKLIST

**IDs covered:** `PY-21` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 17, in [`parts/`](parts/)

> `./m done 17` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_layout.py -v && ./m check
```

Expected: eleven tests in `test_layout.py` (one of them parametrised nine ways) passing, then a green gate.

---

## Setup

- [ ] Created `src/setu/layout.py` and `tests/test_layout.py`
- [ ] Ran `uv run python -c "import setu; print(setu.__file__)"` **before** writing anything
- [ ] Ran the twelve-fact setup block **from the repository root** and can say what each line proved
- [ ] Can say why line 9 differs from line 8 in that block
- [ ] Read `.venv/Lib/site-packages/_editable_impl_setu.pth` and know what its one line does
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — the module

- [ ] Read [1.1 — a module is a file that has already run](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the four import forms](parts/01-the-module/1.2-the-four-import-forms.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `sys.modules`](parts/01-the-module/1.3-sys-modules.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `__name__`, and the same file under two names](parts/01-the-module/1.4-the-name-that-changes.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Put a `print` at the outer level of a module and watched it fire from another file's `import`
- [ ] Imported the same module twice and confirmed it printed once
- [ ] Confirmed `import m` and `import m as n` give the same object with `is`
- [ ] Made a module rebind one of its own names and watched `from m import name` not follow it
- [ ] Ran two star imports with a colliding name and watched the second win, silently
- [ ] Wrote `from m import *` inside a function and read the `SyntaxError`
- [ ] Set `__all__` and watched a public name disappear from `import *`
- [ ] Printed `sys.modules["m"]` and read the file path it names
- [ ] Edited a module on disk, re-imported it, and confirmed the old value survived
- [ ] Called `importlib.reload` and confirmed an object built before it kept the **old** class
- [ ] Ran one file directly and imported it, printing `__name__` both times
- [ ] Made a file import itself and watched its outer level run twice with two copies of a list

---

## Section 2 — finding it

- [ ] Read [2.1 — `sys.path`](parts/02-finding-it/2.1-sys-path.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `ModuleNotFoundError`](parts/02-finding-it/2.2-modulenotfounderror.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — shadowing the standard library](parts/02-finding-it/2.3-shadowing-the-standard-library.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `uv run` and the editable install](parts/02-finding-it/2.4-uv-run-and-the-editable-install.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `sys.path` under `python file.py`, `python -m mod` and `python -c` and compared entry 0
- [ ] Ran one file two ways where only one of them could import a sibling
- [ ] Made it work with `PYTHONPATH` and then said out loud why that is not a fix
- [ ] Printed `sys.executable` under `uv run` and under a bare `python`
- [ ] Ran `import python_dotenv` and `import dotenv` and read the difference
- [ ] Read `ModuleNotFoundError.__mro__` and confirmed it **is an** `ImportError`
- [ ] Ran `import xml` then `xml.etree` and read which exception type came back
- [ ] Saved a `random.py` and watched `import statistics` fail in the standard library
- [ ] Printed `json.__file__` to identify a shadow in one line
- [ ] Deleted the shadowing `.py`, left `__pycache__`, and confirmed the import is fine
- [ ] Read `_editable_impl_setu.pth` and `direct_url.json` in `site-packages`
- [ ] Confirmed there is **no** copy of `setu` in `site-packages`

---

## Section 3 — the package

- [ ] Read [3.1 — a package is a folder](parts/03-the-package/3.1-a-package-is-a-folder.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `__init__.py` is the front page](parts/03-the-package/3.2-init-py-is-the-front-page.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — what goes in it, and what it costs](parts/03-the-package/3.3-what-goes-in-init.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — the missing `__init__.py`](parts/03-the-package/3.4-the-missing-init.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — absolute and relative imports](parts/03-the-package/3.5-absolute-and-relative-imports.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built a package with two subpackages and printed which `__init__.py` files ran, in order
- [ ] Confirmed `import pkg` does **not** give you `pkg.sub`
- [ ] Confirmed `import pkg.sub.mod` binds `pkg` and produces a `NameError` on `mod`
- [ ] Printed `__file__` and `__path__` for a package and for a plain module
- [ ] Listed `sys.modules` after one deep import and counted the entries
- [ ] Made `from pkg import sub` work with an **empty** `pkg/__init__.py`
- [ ] Made an `__init__.py` raise and confirmed nothing under it could be imported
- [ ] Measured `python -X importtime` for an empty front page and a re-exporting one
- [ ] Wrote a module-level `__getattr__` and confirmed nothing below loaded until asked
- [ ] Deleted the `raise` from that `__getattr__` and watched a typo become `None`
- [ ] Made two same-named folders on the path merge into one namespace package
- [ ] Added one empty `__init__.py` and watched half of it disappear
- [ ] Imported a misspelled folder successfully and printed `__file__` as `None`
- [ ] Used all three relative forms — `from . import`, `from .. import`, `from ..x import`
- [ ] Printed `__package__` for a module in a package and for one run directly
- [ ] Read the `SyntaxError` from `import .stock`
- [ ] Read the `ImportError` from too many dots

---

## Section 4 — the project

- [ ] Read [4.1 — the `src/` layout](parts/04-the-project/4.1-the-src-layout.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the circular import](parts/04-the-project/4.2-the-circular-import.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — script versus module](parts/04-the-project/4.3-script-versus-module.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — designing the public surface](parts/04-the-project/4.4-designing-the-public-surface.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built a flat project and a `src` project and confirmed only one imports without an install
- [ ] Confirmed `import days` works in **this** repository, and can say why `src/` does not stop it
- [ ] Put an `__init__.py` in a `src/` folder and watched the importable name become `src.pkg`
- [ ] Built a two-module cycle and read the message **both** ways round
- [ ] Changed the cycle to `import m` plus a use inside a function and watched it work
- [ ] Moved one use to the outer level and read the `AttributeError` variant
- [ ] Fixed it properly by extracting a third module, and confirmed either import order works
- [ ] Wrote a `__main__.py` and ran the package with `python -m`
- [ ] Ran that same file directly and read the relative-import failure
- [ ] Printed `__name__` and `__package__` under `-m` and under a direct launch

---

## Build

- [ ] `src/setu/layout.py` computes `PACKAGE` from `__file__`, not from the working directory
- [ ] `internal_imports` uses `ast.walk`, not `tree.body`, and says why in a comment
- [ ] `internal_imports` handles `ImportFrom` with `module=None`
- [ ] `internal_imports` returns a **set**, and the comment says why
- [ ] `graph()` covers every `*.py` in the package and says why `__init__.py` is excluded
- [ ] `find_cycle` uses two collections and returns the **path**, not `True`
- [ ] `find_cycle` sorts its neighbours so the reported cycle is the same on every run
- [ ] `back_edges` states in its docstring what it does with an unclassified module
- [ ] `LAYERS` names every module currently in `src/setu/`
- [ ] **Wrote down, in two or three sentences, what `src/setu/__init__.py` is for** — and whether that
      agrees with `src/setu/README.md`
- [ ] Reproduced all eight traps in `notebooks/day-17-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)

---

## Tests

- [ ] `tests/test_layout.py` exists and every test failed before any implementation
- [ ] Every test runs offline and imports nothing from `src/setu/` except `layout`
- [ ] `test_the_graph_covers_every_module` passes
- [ ] `test_relative_imports_are_counted` passes
- [ ] `test_imports_inside_functions_are_counted` passes
- [ ] `test_the_package_has_no_import_cycle` passes and names the cycle in its message
- [ ] `test_find_cycle_does_not_report_a_diamond` passes
- [ ] `test_find_cycle_reports_the_path` passes
- [ ] `test_no_module_imports_a_higher_layer` passes
- [ ] `test_leaf_modules_import_nothing_of_ours` passes
- [ ] `test_no_module_shadows_a_standard_library_name` passes for **all nine** names
- [ ] `test_every_module_parses` passes
- [ ] `test_the_front_page_matches_the_decision_you_wrote_down` passes
- [ ] **Break it, watch it go red, fix it** — `tree.body` instead of `ast.walk` → only the
      inside-a-function test goes red
- [ ] **Break it, watch it go red, fix it** — drop the `node.module` guard → the relative-import test
      errors rather than fails
- [ ] **Break it, watch it go red, fix it** — remove `stack.pop()` → only the diamond test goes red
- [ ] **Break it, watch it go red, fix it** — return `True` instead of the path → only the path test goes red
- [ ] **Break it, watch it go red, fix it** — import `setu.config` from a layer-0 module → two tests go red
- [ ] **Break it, watch it go red, fix it** — create an empty `src/setu/json.py` → one parametrised case
      goes red and nothing else notices
- [ ] **Break it and watch every test stay GREEN** — make `graph()` glob `*.pyc`, **and** delete
      `test_the_graph_covers_every_module`. Every remaining test passes on an empty graph. Restore the
      test, watch it go red, and say what it was protecting.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] **0** new packages added today
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-17-modules-and-packages/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 17` reports no failures
- [ ] `./m done 17`
