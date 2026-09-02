---
day: 17
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 17 — Modules, packages, imports and __init__.py"
ids: ["PY-21"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 17
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 17 — Modules, packages, imports and `__init__.py`

**Phase 2 · Advanced Python · Module 2** · `PY-21` modules, packages, imports and `__init__.py`. The
plan's named example is **the `src/setu/` layout the whole plan writes into**, and by the end of today that
layout is a decision you made on purpose, with a test holding it.

> **Yesterday:** where a file actually is, what happens to the bytes between `write` and the disk, and the
> block that cleans up after itself.
> **Today:** how the files you have been writing since Day 10 find each other — what `import` really does,
> where Python looks, what a package is, and what belongs in `__init__.py`.
> **Tomorrow:** exceptions and error types of your own, starting with `src/setu/errors.py` — which is the
> first module today's layering rule will call a leaf.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The flat keeps its recipes on cards.

It started as one sheet stuck to the fridge, and it grew, and now there is a binder. Everything today
happens to that binder.

- **Somebody wrote a note to themselves at the bottom of a card** — "put a pot on now" — and now everybody
  who opens the binder to check how long stock simmers reads it, and some of them do it.
- **One person carries the binder to the counter and reads off it. One copies the number onto a sticky
  note and puts the binder away.** Both get 45. Then somebody corrects the page to 30, and only one of
  them finds out.
- **A rule was added to save walking:** before fetching a card, check whether it is already on the counter.
  It works, and it means a correction made on the shelf is never seen by anybody cooking tonight.
- **A card was photocopied and handed to somebody**, and the copy says "see the card behind this one",
  which means nothing to a person holding one loose sheet.
- **There are three places a recipe might be** — the counter, the binder, the drawer in the hall — and
  everybody looks in the same order without ever having agreed on it. The first one found wins.
- **Somebody put a card marked STOCK on the counter** and it is a stock cube. From then on, everyone who
  asks for stock gets the cube, including the person making risotto, who never asked for stock at all.
- **The binder got dividers**, so a recipe now has an address instead of a position, and opening it at
  "soups" means walking past two front sheets on the way.
- **One front sheet fell out and nobody noticed**, until the housemate's binder went on the same shelf and
  the two "breads" sections silently became one.
- **Two lists on the fridge each begin by telling you to check the other**, and somebody filling in both
  from scratch got stuck in the middle, holding one of them half written.
- **And the last argument is about the front cover** — whether to copy the ten popular recipes onto it, or
  to write only the section names, or to fix the two cards that point at each other in a loop.

One thing before any code: **almost nothing today is new syntax.** You have been typing `import` since Day
0. What is new is what that word does — and it turns out to be Day 12's attribute lookup, Day 14's
decorators, Day 11's caching idea and Day 16's paths, all arriving at once in a mechanism nobody ever
explains.

---

## §2 The map

**What the section numbers mean today.** One ID, so the sections are the plan's `lab (1 ID)` split —
mechanism, then behaviour, then structure, then production use. **1.x** is the module: what an import
actually does to one file. **2.x** is finding it: where Python looks, and the four reasons it does not
find things. **3.x** is the package: folders, `__init__.py`, and what belongs in it. **4.x** is the
project: the layout, the cycle, the launcher, and the surface — the four decisions `src/setu/` needs.

### Section 1 — the module

| Part | What it answers | Level |
|---|---|---|
| [1.1 A module is a file that has already run](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md) | What does `import` actually *do*? | `foundation` |
| [1.2 The four import forms](parts/01-the-module/1.2-the-four-import-forms.md) | Why does a patched value not reach my module? | `working` |
| [1.3 `sys.modules`](parts/01-the-module/1.3-sys-modules.md) | Why is my notebook still running the old code? | `working` |
| [1.4 `__name__`, and the same file under two names](parts/01-the-module/1.4-the-name-that-changes.md) | Why is my module-level list suddenly two lists? | `working` |

### Section 2 — finding it

| Part | What it answers | Level |
|---|---|---|
| [2.1 `sys.path`](parts/02-finding-it/2.1-sys-path.md) | Why does the same file import a sibling one way and not the other? | `working` |
| [2.2 `ModuleNotFoundError`](parts/02-finding-it/2.2-modulenotfounderror.md) | It is installed. Why can it not be found? | `production` |
| [2.3 The file named after a standard-library module](parts/02-finding-it/2.3-shadowing-the-standard-library.md) | Why is the traceback in a file I never opened? | `production` |
| [2.4 `uv run` and the editable install](parts/02-finding-it/2.4-uv-run-and-the-editable-install.md) | Why does `import setu` work at all? | `production` |

### Section 3 — the package

| Part | What it answers | Level |
|---|---|---|
| [3.1 A package is a folder Python will import from](parts/03-the-package/3.1-a-package-is-a-folder.md) | Why does `import xml` not give me `xml.etree`? | `foundation` |
| [3.2 `__init__.py` — the front page](parts/03-the-package/3.2-init-py-is-the-front-page.md) | What is that file actually for? | `working` |
| [3.3 What to put in it, and what it costs](parts/03-the-package/3.3-what-goes-in-init.md) | Who pays for a convenient re-export? | `production` |
| [3.4 The missing `__init__.py`](parts/03-the-package/3.4-the-missing-init.md) | Why did a misspelled folder import successfully? | `production` |
| [3.5 Absolute and relative imports](parts/03-the-package/3.5-absolute-and-relative-imports.md) | What does one dot count from? | `working` |

### Section 4 — the project

| Part | What it answers | Level |
|---|---|---|
| [4.1 The `src/` layout](parts/04-the-project/4.1-the-src-layout.md) | Which bug does one extra folder actually prevent? | `production` |
| [4.2 The circular import](parts/04-the-project/4.2-the-circular-import.md) | What does "partially initialized" mean? | `production` |
| [4.3 `python file.py` versus `python -m`](parts/04-the-project/4.3-script-versus-module.md) | Why does the scheduler fail on a file everything imports? | `production` |
| [4.4 Designing `setu`'s public surface](parts/04-the-project/4.4-designing-the-public-surface.md) | Which of these decisions can a test hold? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `sys`, `importlib` and `ast` from the
standard library. Module 2 is still the language; the first new dependency is Day 19.

```bash
mkdir -p tests notebooks
touch src/setu/layout.py tests/test_layout.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-17-scratch.ipynb

# the package must already be importable, or nothing below means anything
uv run python -c "import setu; print('setu ok:', setu.__file__)"

# the twelve facts the day is built on, before any part names them
uv run python -c "
import sys
from pathlib import Path

import days
import setu

Path('_probe.py').write_text('print(\"   (the file ran)\")\n', encoding='utf-8')
print('1 an import RUNS the file     :', end=' ')
import _probe
print('2 and only once               :', end=' ')
import _probe
print('(nothing was printed)')
print('3 the register knows it       :', '_probe' in sys.modules, '<- part 1.3')
print('4 this program is called      :', __name__, '<- part 1.4')
print('5 Python looks here first     :', sys.path[0] or '(the current directory)', '<- part 2.1')
print('6 with this interpreter       :', Path(sys.executable).parent.parent.name, '<- part 2.2')
print('7 setu is a package           :', hasattr(setu, '__path__'), '<- part 3.1')
print('8 its front page defines      :', [n for n in dir(setu) if not n.startswith('_')], '<- part 3.3')
import setu.config
print('9 after importing a child     :', [n for n in dir(setu) if not n.startswith('_')], '<- part 3.1')
print('10 setu lives under           :', Path(setu.__file__).parent.parent.name, '<- part 4.1')
print('11 days/ has no __init__.py   :', days.__file__, '<- part 3.4')
print('12 one dot inside setu.config :', setu.config.__package__, '<- part 3.5')
Path('_probe.py').unlink()
"

# where the editable install actually lives - one line, one path
cat .venv/Lib/site-packages/_editable_impl_setu.pth
```

Expected from the twelve-fact block, run from the repository root on 2026-09-02. **It must be run from the
root**, because facts 5 and 11 are about the working directory:

```
1 an import RUNS the file     :    (the file ran)
2 and only once               : (nothing was printed)
3 the register knows it       : True <- part 1.3
4 this program is called      : __main__ <- part 1.4
5 Python looks here first     : (the current directory) <- part 2.1
6 with this interpreter       : .venv <- part 2.2
7 setu is a package           : True <- part 3.1
8 its front page defines      : [] <- part 3.3
9 after importing a child     : ['config'] <- part 3.1
10 setu lives under           : src <- part 4.1
11 days/ has no __init__.py   : None <- part 3.4
12 one dot inside setu.config : setu <- part 3.5
```

Line 9 is the one to stare at: `setu` gained an attribute it did not have on line 8, because importing a
child attaches it to its parent ([3.1](parts/03-the-package/3.1-a-package-is-a-folder.md)).

| What | Where it comes from | Part |
|---|---|---|
| what `import` executes, and when | language | [1.1](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md) |
| `import x`, `as`, `from x import y`, `*`, `__all__` | language | [1.2](parts/01-the-module/1.2-the-four-import-forms.md) |
| `sys.modules`, `importlib.reload` | standard library | [1.3](parts/01-the-module/1.3-sys-modules.md) |
| `__name__`, `__main__`, the guard | language | [1.4](parts/01-the-module/1.4-the-name-that-changes.md) |
| `sys.path`, `PYTHONPATH`, `-X importtime` | standard library | [2.1](parts/02-finding-it/2.1-sys-path.md) |
| `ModuleNotFoundError` vs `ImportError`, `sys.executable` | language | [2.2](parts/02-finding-it/2.2-modulenotfounderror.md) |
| first-match-wins, `module.__file__` as a diagnostic | language | [2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md) |
| the `.pth` file, editable installs, *PEP 660* | packaging | [2.4](parts/02-finding-it/2.4-uv-run-and-the-editable-install.md) |
| `uv`, `pyproject.toml`, the lockfile | already met on [Day 0](../day-00-setup/parts/02-skeleton/2.4-uv-init-pyproject-and-the-lockfile.md) | [2.4](parts/02-finding-it/2.4-uv-run-and-the-editable-install.md) |
| `__path__`, subpackages, attachment to the parent | language | [3.1](parts/03-the-package/3.1-a-package-is-a-folder.md) |
| `__init__.py` as the package's module | language | [3.2](parts/03-the-package/3.2-init-py-is-the-front-page.md) |
| re-exporting, `__all__`, module `__getattr__`, *PEP 562* | language | [3.3](parts/03-the-package/3.3-what-goes-in-init.md) |
| namespace packages, *PEP 420* | language | [3.4](parts/03-the-package/3.4-the-missing-init.md) |
| `__package__`, leading dots, *PEP 328* | language | [3.5](parts/03-the-package/3.5-absolute-and-relative-imports.md) |
| dunder methods are looked up on the type | already met on [Day 15](../day-15-constructors-and-dunders/parts/03-the-dunders/3.1-what-a-dunder-method-is.md) | [3.3](parts/03-the-package/3.3-what-goes-in-init.md) |
| the `src` layout | packaging | [4.1](parts/04-the-project/4.1-the-src-layout.md) |
| partially initialized modules | language | [4.2](parts/04-the-project/4.2-the-circular-import.md) |
| `__main__.py`, `-m`, console scripts | language | [4.3](parts/04-the-project/4.3-script-versus-module.md) |
| `ast.parse`, `ast.walk` | already used by [`scripts/check_blocks.py`](../../scripts/check_blocks.py) | [4.4](parts/04-the-project/4.4-designing-the-public-surface.md) |
| closures, and why the walker nests a function | already met on [Day 10](../day-10-functions/parts/02-scope/2.4-closures-and-late-binding.md) | [4.4](parts/04-the-project/4.4-designing-the-public-surface.md) |

---

## §4 Build brief

**One new module and one decision.** `src/setu/layout.py` reads the package's own import graph;
`tests/test_layout.py` holds the rules it finds. Nothing else in `src/setu/` changes today, which is
itself the point — today's deliverable is the shape of the folder, not another feature.

**1. `src/setu/layout.py`** — the package's own import graph, read without running anything
([4.4](parts/04-the-project/4.4-designing-the-public-surface.md) explains every line).

```python
"""Read this package's own import graph, by parsing it rather than importing it."""

from __future__ import annotations

import ast
from pathlib import Path

# This file is src/setu/layout.py, so the package folder is its parent - worked out from
# __file__ and not from the working directory (Day 16, part 1.3). PACKAGE.name is the
# importable name, which differs from the folder path under the src layout (part 4.1).
PACKAGE = Path(__file__).resolve().parent
TOP = PACKAGE.name

# The layers, lowest first. A module may import anything in a layer BELOW its own and
# nothing above it. A module not named here is unclassified, and the test decides what
# that means - which is a decision you have to make and write down.
LAYERS: dict[str, int] = {
    "errors": 0,
    "paths": 0,
    "config": 1,
    "layout": 1,
}


def internal_imports(path: Path) -> set[str]:
    """Every module inside this package that `path` imports, by short name."""
    # TODO(me): ast.parse the source, then ast.walk it - NOT tree.body, or you miss
    # every import inside a function, which is exactly the shape part 4.2 warns about.
    #
    # Two node types: ast.Import (alias.name is the full dotted string) and
    # ast.ImportFrom (node.level is the number of leading dots; node.module can be
    # None for `from . import x`, and that None is what breaks a first draft).
    raise NotImplementedError


def graph() -> dict[str, set[str]]:
    """Module short name -> the modules of ours it imports."""
    # TODO(me): every *.py in PACKAGE except __init__.py. Say in a comment why
    # __init__.py is excluded and whether you think that is right (part 3.3).
    raise NotImplementedError


def find_cycle(edges: dict[str, set[str]]) -> list[str] | None:
    """The first cycle, as the path that closes it, or None."""
    # TODO(me): depth-first, with TWO collections - the route you are on and the
    # nodes you have finished. Using one is the bug that reports a diamond as a
    # cycle, and a checker that cries wolf gets deleted (part 4.4).
    #
    # Return the path, not True. `pantry -> shopping -> pantry` is a message
    # somebody can act on; "there is a cycle" is not.
    raise NotImplementedError


def back_edges(edges: dict[str, set[str]]) -> list[tuple[str, str]]:
    """Imports that go from a lower layer to a higher one."""
    # TODO(me): for each module in LAYERS, every import whose layer is >= its own.
    # Decide what to do about a module that is not in LAYERS at all, and write the
    # decision in the docstring - silently ignoring it is how the rule rots.
    raise NotImplementedError
```

**2. `tests/test_layout.py`** — the rules, made executable. See §5.

**3. Decide, in writing, what `src/setu/__init__.py` is for.** Two or three sentences at the top of the
file as a comment, or in `src/setu/README.md`. The three options and their costs are
[3.3](parts/03-the-package/3.3-what-goes-in-init.md); `src/setu/README.md` already states one answer, and
your job is to agree with it on purpose or to change it on purpose. An undecided front page is the one
that grows.

**4. Reproduce the eight traps in the notebook, then throw the notebook away.** In
`notebooks/day-17-scratch.ipynb`, in this order:

- Put a `print` at the outer level of a file and import it from another
  ([1.1](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md)).
- `from m import VALUE`, then have `m` rebind `VALUE`, and print both
  ([1.2](parts/01-the-module/1.2-the-four-import-forms.md)).
- Edit a module on disk and re-run the `import` cell, and watch nothing change
  ([1.3](parts/01-the-module/1.3-sys-modules.md)).
- Run one file two ways and print `__name__` and `__package__` both times
  ([1.4](parts/01-the-module/1.4-the-name-that-changes.md), [4.3](parts/04-the-project/4.3-script-versus-module.md)).
- Print `sys.path[0]` under `python file.py` and under `python -m`
  ([2.1](parts/02-finding-it/2.1-sys-path.md)).
- Save a file called `random.py` beside your notebook, then `import statistics`
  ([2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md)).
- Make a folder with no `__init__.py`, import it, and print `__file__`
  ([3.4](parts/03-the-package/3.4-the-missing-init.md)).
- Write two modules that import each other and read both error messages
  ([4.2](parts/04-the-project/4.2-the-circular-import.md)).

**The notebook is not committed** (Principle 6); `layout.py` and its tests are.

**5. Do not add anything to `src/setu/` that today's rules would reject.** If a module you want does not
fit a layer, that is information about the module.

---

## §5 The eval that must be able to fail

Create `tests/test_layout.py`. Every test runs offline, reads files without importing them, and belongs in
`./m check`.

```python
"""Day 17: the rules about this package's shape, made executable."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from setu.layout import PACKAGE, back_edges, find_cycle, graph, internal_imports

STDLIB_NAMES = {"json", "types", "email", "logging", "string", "time", "copy", "random", "secrets"}


def test_the_graph_covers_every_module(tmp_path) -> None:
    """A checker that silently skips files is not a checker."""
    # TODO(me): assert the keys of graph() match every *.py in PACKAGE except
    # __init__.py. This is the test that catches a glob typo, which would otherwise
    # make every test below pass vacuously.
    raise NotImplementedError


def test_relative_imports_are_counted(tmp_path) -> None:
    """Part 3.5: `from . import x` has module=None, and that None breaks a first draft."""
    # TODO(me): write a tiny file into tmp_path containing `from . import errors`
    # and assert internal_imports finds `errors`. Without the None guard this test
    # raises AttributeError instead of failing an assertion - which is still red,
    # and is still the test doing its job.
    raise NotImplementedError


def test_imports_inside_functions_are_counted(tmp_path) -> None:
    """Part 4.2: a deferred import is still an edge."""
    # TODO(me): a file with `def f():` and an import in its body. Assert it is
    # found. A walker that only reads tree.body passes every other test in this
    # file and misses exactly the cycles somebody worked around.
    raise NotImplementedError


def test_the_package_has_no_import_cycle() -> None:
    """Part 4.2, as a gate rather than a habit."""
    # TODO(me): assert find_cycle(graph()) is None, and put the returned path in
    # the assertion message so a failure names the cycle.
    raise NotImplementedError


def test_find_cycle_does_not_report_a_diamond() -> None:
    """The false positive that gets checkers deleted."""
    # TODO(me): {'a': {'b', 'c'}, 'b': {'d'}, 'c': {'d'}, 'd': set()} has no cycle.
    # A find_cycle written with one collection instead of two fails this and passes
    # everything else.
    raise NotImplementedError


def test_find_cycle_reports_the_path() -> None:
    """A message somebody can act on."""
    # TODO(me): {'x': {'y'}, 'y': {'x'}} returns a list containing both names, in
    # order, closing on itself.
    raise NotImplementedError


def test_no_module_imports_a_higher_layer() -> None:
    """The layer rule from part 4.4."""
    # TODO(me): assert back_edges(graph()) == [], with the offending pairs in the
    # message. This is the test the day exists for.
    raise NotImplementedError


def test_leaf_modules_import_nothing_of_ours() -> None:
    """A leaf that imports a sibling is a cycle waiting to close."""
    # TODO(me): every module at layer 0 has an empty set in graph(). Say in a
    # comment why this is not the same assertion as the one above.
    raise NotImplementedError


@pytest.mark.parametrize("name", sorted(STDLIB_NAMES))
def test_no_module_shadows_a_standard_library_name(name) -> None:
    """Part 2.3, prevented rather than diagnosed."""
    # TODO(me): assert (PACKAGE / f"{name}.py").exists() is False. Nine cheap
    # assertions that would have saved somebody an evening.
    raise NotImplementedError


def test_every_module_parses() -> None:
    """The cheapest possible smoke test, and it costs nothing."""
    # TODO(me): ast.parse every file in PACKAGE. It runs no code (part 1.1), so it
    # is safe on a module that would open a connection at import.
    raise NotImplementedError


def test_the_front_page_matches_the_decision_you_wrote_down() -> None:
    """Part 3.3: an undecided __init__.py is the one that grows."""
    # TODO(me): assert whatever you decided in §4 item 3. If you chose "empty",
    # assert the file has no import statements. If you chose a re-export, assert
    # __all__ exists and every name in it is importable. A test you cannot write
    # means the decision was not made.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_layout.py -v
```

Then implement, then **break each one on purpose**:

- Change `ast.walk(tree)` to `tree.body`. **Only `test_imports_inside_functions_are_counted` goes red** —
  every other test in the file passes, which is precisely why that test exists.
- Delete the `if node.module:` guard. `test_relative_imports_are_counted` errors with `AttributeError:
  'NoneType' object has no attribute 'split'` rather than failing an assertion. Both are red; say out loud
  which you would rather see and why.
- Remove `stack.pop()` from `find_cycle`. `test_find_cycle_does_not_report_a_diamond` goes red and the
  real-package test stays green, because the package is small.
- Use one collection instead of two in `find_cycle`. Same test, same red.
- Return `True` instead of the path. `test_find_cycle_reports_the_path` goes red and the gate test stays
  green — the difference between a useful failure and a useless one.
- Add `from setu.config import REQUIRED` to a layer-0 module. `test_no_module_imports_a_higher_layer` and
  `test_leaf_modules_import_nothing_of_ours` both go red. Now remove the module from `LAYERS` entirely and
  watch what your `back_edges` does about an unclassified module — that is the decision item 4 asked you to
  write down.
- Create an empty `src/setu/json.py`. One parametrised case goes red, and nothing else notices — including
  the code, until much later ([2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md)).
- **Break it and watch every test stay GREEN** — change `graph()` to glob `*.pyc` instead of `*.py`, **and**
  delete `test_the_graph_covers_every_module`. Every remaining test passes, on an empty graph: there are no
  cycles in nothing, no back edges in nothing, and no leaves that import anything. Restore the test, watch
  it go red, and say out loud what it was protecting.

That last item is the most important line in this section. Every other test in the file asserts something
about a graph; only one asserts that the graph is the graph.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| New packages | **0** — Module 2 is still the language |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |
| Disk | a few kilobytes in `tmp_path`, deleted by `pytest` |

Today's tests **parse** files rather than importing them, so they run no code from `src/setu/`
([1.1](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md)). That is a budget property as
well as a safety one: a check that imports every module in a package pays every module's import-time cost,
and on Day 172 that would mean building provider clients in CI.

---

## §7 Traps

- **`import` runs the file; a `print` at the outer level fires on import** —
  [1.1](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md).
- **A module that reads a file at its outer level fails at the importer's `import` line** —
  [1.1](parts/01-the-module/1.1-a-module-is-a-file-that-has-already-run.md).
- **`from m import x` copies the binding, so a later rebinding in `m` is never seen** —
  [1.2](parts/01-the-module/1.2-the-four-import-forms.md).
- **`monkeypatch` on a module has no effect on code that did `from module import name`** —
  [1.2](parts/01-the-module/1.2-the-four-import-forms.md).
- **Two star imports silently overwrite each other, and the order matters** —
  [1.2](parts/01-the-module/1.2-the-four-import-forms.md).
- **`import *` inside a function is a `SyntaxError`, not a style warning** —
  [1.2](parts/01-the-module/1.2-the-four-import-forms.md).
- **Re-running an `import` cell after editing the file changes nothing** —
  [1.3](parts/01-the-module/1.3-sys-modules.md).
- **`importlib.reload` leaves every existing reference pointing at the old class** —
  [1.3](parts/01-the-module/1.3-sys-modules.md).
- **Module-level state is process-global, so tests pollute each other in file order** —
  [1.3](parts/01-the-module/1.3-sys-modules.md).
- **A file both launched and imported is loaded twice, with two copies of its state** —
  [1.4](parts/01-the-module/1.4-the-name-that-changes.md).
- **Anything under `if __name__ == "__main__":` is invisible to every importer** —
  [1.4](parts/01-the-module/1.4-the-name-that-changes.md).
- **`sys.path[0]` is the script's folder for a file and the working directory for `-m`** —
  [2.1](parts/02-finding-it/2.1-sys-path.md).
- **`sys.path.append` in a module edits a global list for the whole process** —
  [2.1](parts/02-finding-it/2.1-sys-path.md).
- **`PYTHONPATH` fixes it invisibly, and only on your machine** —
  [2.1](parts/02-finding-it/2.1-sys-path.md).
- **The install name is not the import name: `python-dotenv` gives `dotenv`** —
  [2.2](parts/02-finding-it/2.2-modulenotfounderror.md).
- **`ModuleNotFoundError` is usually the wrong interpreter, not a missing package** —
  [2.2](parts/02-finding-it/2.2-modulenotfounderror.md).
- **`import xml` then `xml.etree` raises `AttributeError`, not `ModuleNotFoundError`** —
  [2.2](parts/02-finding-it/2.2-modulenotfounderror.md), [3.1](parts/03-the-package/3.1-a-package-is-a-folder.md).
- **Catching `ModuleNotFoundError` for an optional dependency misses a broken install** —
  [2.2](parts/02-finding-it/2.2-modulenotfounderror.md).
- **A file called `random.py` breaks libraries that have never heard of you** —
  [2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md).
- **A shadow that satisfies the calls being made raises nothing at all** —
  [2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md).
- **Deleting `__pycache__` is not the fix; deleting the `.py` is** —
  [2.3](parts/02-finding-it/2.3-shadowing-the-standard-library.md).
- **A `.pth` file belongs to one environment and means nothing in another** —
  [2.4](parts/02-finding-it/2.4-uv-run-and-the-editable-install.md).
- **`import pkg` does not import `pkg.sub`, and the folder being on disk is not enough** —
  [3.1](parts/03-the-package/3.1-a-package-is-a-folder.md).
- **`import a.b.c` binds `a`, not `c`** —
  [3.1](parts/03-the-package/3.1-a-package-is-a-folder.md).
- **An `__init__.py` that raises makes every module under it unimportable** —
  [3.1](parts/03-the-package/3.1-a-package-is-a-folder.md), [3.2](parts/03-the-package/3.2-init-py-is-the-front-page.md).
- **`__init___.py` with three underscores makes a namespace package and no error** —
  [3.2](parts/03-the-package/3.2-init-py-is-the-front-page.md).
- **A re-export in a front page is loaded by everyone who touches the package** —
  [3.3](parts/03-the-package/3.3-what-goes-in-init.md).
- **An optional dependency in `__init__.py` makes itself mandatory for the whole package** —
  [3.3](parts/03-the-package/3.3-what-goes-in-init.md).
- **A module `__getattr__` with no `raise` makes every misspelling `None`** —
  [3.3](parts/03-the-package/3.3-what-goes-in-init.md).
- **A misspelled folder imports successfully and is empty; `__file__` is `None`** —
  [3.4](parts/03-the-package/3.4-the-missing-init.md).
- **Adding one empty `__init__.py` can remove half a namespace package** —
  [3.4](parts/03-the-package/3.4-the-missing-init.md).
- **Deleting an empty `__init__.py` "because it is empty" changes the package's kind** —
  [3.4](parts/03-the-package/3.4-the-missing-init.md).
- **`import .stock` is a `SyntaxError`; only the `from` form has a relative version** —
  [3.5](parts/03-the-package/3.5-absolute-and-relative-imports.md).
- **Relative imports fail in a file launched directly, because `__package__` is `None`** —
  [3.5](parts/03-the-package/3.5-absolute-and-relative-imports.md), [4.3](parts/04-the-project/4.3-script-versus-module.md).
- **A flat layout lets tests import code the wheel never packaged** —
  [4.1](parts/04-the-project/4.1-the-src-layout.md).
- **`src/` does not stop the repository root being importable — `import days` works right now** —
  [4.1](parts/04-the-project/4.1-the-src-layout.md).
- **An `__init__.py` in `src/` makes the importable name `src.setu`** —
  [4.1](parts/04-the-project/4.1-the-src-layout.md).
- **Which module a cycle blames depends on which one you import first** —
  [4.2](parts/04-the-project/4.2-the-circular-import.md).
- **`import x` survives a cycle only until the first outer-level attribute access** —
  [4.2](parts/04-the-project/4.2-the-circular-import.md).
- **Reordering two lines to fix a cycle is undone by the next formatter run** —
  [4.2](parts/04-the-project/4.2-the-circular-import.md).
- **`-m` takes a dotted module name, never a path with slashes and `.py`** —
  [4.3](parts/04-the-project/4.3-script-versus-module.md).
- **`-m` must be run from the folder that can see the package, not from inside it** —
  [4.3](parts/04-the-project/4.3-script-versus-module.md).
- **A bare `pytest` may belong to a different environment than `python -m pytest`** —
  [4.3](parts/04-the-project/4.3-script-versus-module.md).
- **A cycle checker written with one collection reports a diamond as a cycle** —
  [4.4](parts/04-the-project/4.4-designing-the-public-surface.md).
- **A checker that reads only the top of the file misses every deferred import** —
  [4.4](parts/04-the-project/4.4-designing-the-public-surface.md).
- **`utils.py` has no reason to reject anything, so it collects, and then it cycles** —
  [4.4](parts/04-the-project/4.4-designing-the-public-surface.md).

---

## §8 Verify before you code

Fetched **2026-09-02**. Today is the language and three standard-library modules, so the language
reference, the library reference and the PEPs are the authority:

- <https://docs.python.org/3/reference/import.html> — the import system in full: the module cache,
  searching, loading, `__path__`, namespace packages, relative imports, and the sentence in §5.4 that
  explains every circular-import message you will ever read.
- <https://docs.python.org/3/using/cmdline.html> — what `-m`, `-c` and a script path each prepend to
  `sys.path`, in the project's own words rather than folklore.
- <https://docs.python.org/3/library/sys.html> — `sys.modules`, `sys.path`, `sys.executable`, and the
  warning about modifying `sys.modules` while it is being iterated.
- <https://docs.python.org/3/library/importlib.html> — `import_module`, `reload`, and the paragraph on what
  `reload` does *not* update.
- <https://peps.python.org/pep-0328/> — *PEP 328 — Imports: Multi-Line and Absolute/Relative* (2003), which
  removed implicit relative imports and defined the leading-dot syntax.
- <https://peps.python.org/pep-0420/> — *PEP 420 — Implicit Namespace Packages* (2012), the reason a folder
  with no `__init__.py` still imports.
- <https://peps.python.org/pep-0562/> — *PEP 562 — Module `__getattr__` and `__dir__`* (2017), the
  mechanism behind a lazy front page.
- <https://peps.python.org/pep-0660/> — *PEP 660 — Editable installs for pyproject.toml based builds*
  (2021), which is why `import setu` works with no copy in `site-packages`.
- <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/> — the packaging guide's
  own comparison, including the editable-install difference.
- <https://docs.python.org/3/library/ast.html> — `ast.parse` and `ast.walk`, and the node attributes
  `Import.names`, `ImportFrom.module` and `ImportFrom.level` that today's build reads.

---

## §9 Say it in an interview

> "`import x` is not a lookup, it is an execution: Python checks `sys.modules` first, and on a miss it
> finds the file, creates an empty module object, **puts it in `sys.modules` before running it**, and then
> executes the file top to bottom. So everything at a module's outer level happens at import, once per
> process — which is why I keep modules free of import-time work, because otherwise every test that
> imports anything downstream pays for it and a fixture cannot get in first. That pre-registration is also
> the whole explanation of circular imports: the second module gets a real but half-built object, so
> `from x import name` raises `cannot import name … from partially initialized module` while a plain
> `import x` survives until the first attribute access. I fix those by extracting whatever the two modules
> share into a third module that imports neither, rather than by moving an import into a function, which
> works but hides the design problem. Finding a module is a walk down `sys.path`, first match wins, and
> `sys.path[0]` is set by the launcher — the script's own folder for `python file.py`, the working
> directory for `python -m` — which is why the same file imports its sibling one way and not the other,
> and why a `random.py` in your project replaces the standard library's for every dependency in the
> process. When an import fails, the first thing I print is `sys.executable`, because a second interpreter
> is a more likely cause than a missing package. For layout I use `src/`, so the package is only reachable
> through the install and the tests exercise the packaged artifact — a flat layout will happily import code
> the wheel never included. `__init__.py` I keep empty in an application: whatever it imports is loaded by
> everyone who touches the package, so a convenient re-export is a cost paid process-wide, and if I do want
> short names I use a module-level `__getattr__` so the import is deferred to first use. And I keep the
> import direction one-way with a test that parses the package with `ast` — parsing, not importing, so it
> also catches the deferred imports people use to work around cycles."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, `src/setu/layout.py` reports
the package's real import graph, `tests/test_layout.py` fails when a leaf imports a sibling, and you have
**watched the whole suite stay green on an empty graph** — in §5 — not when a particular amount of time has
passed. Then:

```bash
./m done 17
```

Tomorrow is exceptions and error types of your own. The first file it writes is `src/setu/errors.py`, and
today's layer rule is what says it may import nothing of ours — which is exactly why it is the module
everything else will be allowed to import.
