---
day: 16
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 16 — Files, pathlib, buffering, and context managers"
ids: ["PY-19", "PY-20"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P9 data has provenance", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 19
generated: "2026-09-01"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 16 — Files, `pathlib`, buffering, and context managers

**Phase 2 · Advanced Python · Module 2** · `PY-19` file handling, buffering and `pathlib`, `PY-20`
context managers. The plan's named examples are **writing a 50 000-line JSONL without a memory spike**
and **a context manager that guarantees the connection closes on exception**, and by the end of today
both exist in `src/setu/`.

> **Yesterday:** the decorators the language ships with, and the method names Python calls on your
> behalf, so an object of yours behaves like one that came with Python.
> **Today:** where a file actually is, what happens to the bytes between `write` and the disk, and the
> block that cleans up after itself — which turns out to be two more of yesterday's dunder methods.
> **Tomorrow:** modules, packages, imports and `__init__.py` — how the files you have been writing find
> each other.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

You keep a shopping list on the computer. Three lines in it: milk, bread, eggs.

Everything today happens to that one file.

- **Somebody asks where it is** and you say "in Documents, in lists, called shopping". Four pieces, said
  in order. You never say the slashes — those are how it gets written down, and they are written down
  differently on different machines.
- **You send the location to somebody else** and it does not work on their computer, because "the folder
  called lists" means wherever *they* are standing.
- **You add eggs, the battery dies**, and the file comes back saying milk and bread. Not corrupted — just
  smaller, and looking exactly like a file that was saved properly.
- **A café goes on the list** because you are meeting somebody there, and on somebody else's screen it
  says cafÃ©. Nothing was damaged in transit; each machine used a different rule for turning bytes into
  letters.
- **The file grows a character.** Three lines, fourteen letters, and the size says twenty — because a
  line ending is two bytes here and one byte elsewhere.
- **Somebody starts logging every receipt into it** and it is fifty thousand lines. The question is still
  small: how many times did we buy milk?
- **Somebody left it open on the shared computer** and went home, and nobody can edit it until that
  machine is restarted.
- **And the note you handed to the desk downstairs** is not upstairs yet. It is in a tray, and it will be
  up within the hour, and if the building burns down tonight it never arrives.

One thing before any code: **almost nothing today is new machinery.** A file object is an iterator over
its lines, which is Day 11. `with` is `try` / `finally`, and it works through `__enter__` and `__exit__`,
which are Day 15's dunder methods. What is new is the layer underneath — where bytes actually go, and
when.

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the plan's `lab (2 IDs)` split. **1.x**, **2.x** and
**3.x** are `PY-19`, in pipeline order: where the file is, how to read and write it, and what happens to
the bytes on the way. **4.x** is `PY-20` — `with`, what it compiles to, how to write one, and the two
ways one can hide a crash. Section 3 is the day's headline build and section 4 is the rest of it.

### Section 1 — the path

| Part | What it answers | Level |
|---|---|---|
| [1.1 A path is not a string](parts/01-the-path/1.1-a-path-is-not-a-string.md) | Why not just glue strings with a slash? | `foundation` |
| [1.2 Taking a path apart](parts/01-the-path/1.2-taking-a-path-apart.md) | Which of `.name`, `.stem`, `.suffix` has the dot? | `working` |
| [1.3 Relative, absolute, and the working directory](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md) | What decides where a relative path points? | `production` |
| [1.4 `exists()`, `mkdir()`, and the race](parts/01-the-path/1.4-exists-mkdir-and-the-race.md) | Why is checking first worse than just doing it? | `production` |
| [1.5 Globbing](parts/01-the-path/1.5-globbing.md) | Why is `if folder.glob('*.csv'):` always true? | `working` |

### Section 2 — reading and writing

| Part | What it answers | Level |
|---|---|---|
| [2.1 `open()` and the mode string](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md) | At what moment does `w` destroy the file? | `foundation` |
| [2.2 The encoding you must always pass](parts/02-reading-and-writing/2.2-encoding.md) | What does Python use when you leave it off? | `production` |
| [2.3 Newlines, and the file that grew a character](parts/02-reading-and-writing/2.3-newlines.md) | Why do two identical files have different checksums? | `production` |
| [2.4 Reading a big file without holding it](parts/02-reading-and-writing/2.4-reading-a-big-file.md) | What is in memory during `for line in f`? | `working` |
| [2.5 JSONL — one record per line](parts/02-reading-and-writing/2.5-jsonl.md) | What does a truncated file cost in each format? | `production` |

### Section 3 — buffering

| Part | What it answers | Level |
|---|---|---|
| [3.1 The write that had not happened yet](parts/03-buffering/3.1-the-write-that-had-not-happened.md) | Where do the bytes go when you call `write`? | `foundation` |
| [3.2 `flush()`, `os.fsync()`, and what "saved" means](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md) | Which failure does each level survive? | `production` |
| [3.3 Fifty thousand lines without a memory spike](parts/03-buffering/3.3-fifty-thousand-lines.md) | What does building the list first actually cost? | `production` |

### Section 4 — context managers

| Part | What it answers | Level |
|---|---|---|
| [4.1 `with` — the block that cleans up after itself](parts/04-context-managers/4.1-with-the-block-that-cleans-up.md) | What does closing a file do besides releasing it? | `foundation` |
| [4.2 `try` / `finally` is what `with` is](parts/04-context-managers/4.2-try-finally-is-what-with-is.md) | What does `with` add that a `finally` does not? | `working` |
| [4.3 `__enter__` and `__exit__` by hand](parts/04-context-managers/4.3-enter-and-exit-by-hand.md) | What are `__exit__`'s four parameters? | `working` |
| [4.4 The `__exit__` that swallowed the exception](parts/04-context-managers/4.4-the-exit-that-swallowed-the-exception.md) | What does returning `True` from `__exit__` do? | `production` |
| [4.5 `@contextmanager`](parts/04-context-managers/4.5-contextmanager-decorator.md) | Why must the `yield` be inside a `try`? | `production` |
| [4.6 A connection that always closes, and `ExitStack`](parts/04-context-managers/4.6-a-connection-that-always-closes.md) | How do you release a number of things you cannot count in advance? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `pathlib`, `json`, `os`, `contextlib`
and `tracemalloc` from the standard library. Module 2 is still the language; the first new dependency is
Phase 3.

```bash
mkdir -p src/setu tests notebooks data/day-16
touch src/setu/jsonl.py src/setu/paths.py tests/test_jsonl.py tests/test_paths.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-16-scratch.ipynb

# yesterday's Paper must already exist - today's JSONL reader produces them
uv run python -c "from setu.paper import Paper; print('Paper ok')"

# the ten facts the day is built on, before any part names them
uv run python -c "
import contextlib
import locale
import os
from pathlib import Path

p = Path('setup.txt')
print('1 a path is not a string      :', repr(Path('lists') / 'shopping.txt'), '<- part 1.1')
print('2 its pieces                  :', Path('lists/shopping.txt').suffix, Path('lists/shopping.txt').stem, '<- part 1.2')
print('3 relative means from here    :', Path('lists').is_absolute(), '/', Path.cwd().name, '<- part 1.3')

with open(p, 'w', encoding='utf-8') as f:
    f.write('milk\n')
print('4 bytes on disk vs characters :', p.read_bytes(), 'vs', repr(p.read_text(encoding='utf-8')), '<- part 2.3')
print('5 the locale would have used  :', locale.getpreferredencoding(False), '<- part 2.2')

p.unlink(missing_ok=True)
f = open(p, 'w', encoding='utf-8')
f.write('milk\n')
print('6 after write, on disk        :', p.stat().st_size, 'bytes <- part 3.1')
f.close()
print('7 after close, on disk        :', p.stat().st_size, 'bytes <- part 3.1')


class Swallow:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return True


with Swallow():
    raise ValueError('never reaches you')
print('8 an __exit__ returning True  : swallowed the exception <- part 4.4')
print('9 ExitStack exists            :', contextlib.ExitStack.__name__, '<- part 4.6')
print('10 os.fsync exists            :', os.fsync.__name__, '<- part 3.2')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule PLW1514
uv run ruff rule B012
```

Expected from the ten-fact block on this machine, on 2026-09-01. **Lines 1, 4 and 5 differ on
macOS or Linux**, and that is one of the day's subjects:

```
1 a path is not a string      : WindowsPath('lists/shopping.txt') <- part 1.1
2 its pieces                  : .txt shopping <- part 1.2
3 relative means from here    : False / setu <- part 1.3
4 bytes on disk vs characters : b'milk\r\n' vs 'milk\n' <- part 2.3
5 the locale would have used  : cp1252 <- part 2.2
6 after write, on disk        : 0 bytes <- part 3.1
7 after close, on disk        : 6 bytes <- part 3.1
8 an __exit__ returning True  : swallowed the exception <- part 4.4
9 ExitStack exists            : ExitStack <- part 4.6
10 os.fsync exists            : fsync <- part 3.2
```

| What | Where it comes from | Part |
|---|---|---|
| `Path`, `/` as a join, *PEP 428* | standard library | [1.1](parts/01-the-path/1.1-a-path-is-not-a-string.md) |
| `.name`, `.stem`, `.suffix`, `.parent`, `with_suffix` | standard library | [1.2](parts/01-the-path/1.2-taking-a-path-apart.md) |
| `Path.cwd`, `resolve`, `is_relative_to`, `__file__` | standard library | [1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md) |
| `mkdir(parents=, exist_ok=)`, `unlink(missing_ok=)` | standard library | [1.4](parts/01-the-path/1.4-exists-mkdir-and-the-race.md) |
| `glob`, `rglob`, `iterdir` | standard library | [1.5](parts/01-the-path/1.5-globbing.md) |
| `open` modes, text and binary | language | [2.1](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md) |
| encodings, `utf-8-sig`, *PEP 597* | standard library | [2.2](parts/02-reading-and-writing/2.2-encoding.md) |
| universal newlines, `newline=` | standard library | [2.3](parts/02-reading-and-writing/2.3-newlines.md) |
| a file object is an iterator | already met on [Day 11](../day-11-iterators-and-generators/parts/02-generators/2.3-streaming-a-file.md) | [2.4](parts/02-reading-and-writing/2.4-reading-a-big-file.md) |
| `json.dumps`, `json.loads`, JSONL | standard library | [2.5](parts/02-reading-and-writing/2.5-jsonl.md) |
| buffering, `flush`, `os.fsync`, `fileno` | standard library | [3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md), [3.2](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md) |
| `tracemalloc` | standard library | [3.3](parts/03-buffering/3.3-fifty-thousand-lines.md) |
| generators, and why they keep memory flat | already built on [Day 11](../day-11-iterators-and-generators/parts/02-generators/2.1-yield-the-function-that-pauses.md) | [3.3](parts/03-buffering/3.3-fifty-thousand-lines.md) |
| `try` / `finally` | already met on [Day 14](../day-14-decorators/parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md) | [4.2](parts/04-context-managers/4.2-try-finally-is-what-with-is.md) |
| dunder methods are looked up on the type | already met on [Day 15](../day-15-constructors-and-dunders/parts/03-the-dunders/3.1-what-a-dunder-method-is.md) | [4.3](parts/04-context-managers/4.3-enter-and-exit-by-hand.md) |
| `contextlib.contextmanager`, `suppress`, `closing`, `ExitStack` | standard library | [4.5](parts/04-context-managers/4.5-contextmanager-decorator.md), [4.6](parts/04-context-managers/4.6-a-connection-that-always-closes.md) |
| `Paper.from_row` | already built on [Day 15](../day-15-constructors-and-dunders/parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md) | [2.5](parts/02-reading-and-writing/2.5-jsonl.md) |

---

## §4 Build brief

**Two new modules.** `src/setu/paths.py` holds the path rules; `src/setu/jsonl.py` holds the day's
headline build. `src/setu/paper.py` is imported and not changed.

**1. `src/setu/paths.py`** — every path decision in one place, and none of them touching the disk except
where they must.

```python
"""Where this project's files live, decided once."""

from __future__ import annotations

from pathlib import Path

# The repository root, worked out from THIS file rather than from the working
# directory (part 1.3). paths.py is at <root>/src/setu/paths.py, so the root is
# three levels up. If this file moves, this number changes - which is why it is
# written once and never inlined.
ROOT = Path(__file__).resolve().parents[2]


def data_dir(name: str) -> Path:
    """The folder for one dataset, created if it is not there."""
    # TODO(me): ROOT / 'data' / name, then mkdir(parents=True, exist_ok=True)
    # (part 1.4). Say in a comment which failure each of the two flags prevents.
    raise NotImplementedError


def safe_child(base: Path, name: str) -> Path:
    """Join `name` onto `base` and refuse anything that escapes it.

    `name` may come from a filename in an archive, a URL or a user. Part 1.3's
    third failure is what this exists to prevent (Principle 11).
    """
    # TODO(me): join, resolve, then `is_relative_to(base.resolve())`. Raise
    # ValueError naming the offending path if it is outside. Two lines and a
    # raise - and it is the only thing standing between a scraper and someone
    # else's files.
    raise NotImplementedError


def outputs_for(source: Path, suffix: str) -> Path:
    """The output file that belongs to one input file."""
    # TODO(me): same folder, same stem, new suffix - but NOT with_suffix() if
    # the source can have two extensions (part 1.2's second failure). Decide
    # which behaviour you want and say so in the docstring.
    raise NotImplementedError
```

**2. `src/setu/jsonl.py`** — the plan's named example, both directions
([2.5](parts/02-reading-and-writing/2.5-jsonl.md) and
[3.3](parts/03-buffering/3.3-fifty-thousand-lines.md) explain every line).

```python
"""JSONL, written without a memory spike and read without stopping on one bad line."""

from __future__ import annotations

import json
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any


def write_jsonl(path: Path, records: Iterable[dict[str, Any]], *, append: bool = False) -> int:
    """Write one record per line. Returns how many were written.

    Takes an ITERABLE, not a list, so a generator can be handed straight in and
    nothing ever holds the whole dataset (part 3.3).
    """
    # TODO(me): open once, outside the loop, with mode 'a' or 'w', and BOTH
    # encoding='utf-8' and newline='\n' (parts 2.2 and 2.3). Then one
    # json.dumps + '\n' per record. No indent=, ever (part 2.5's first failure).
    #
    # Before appending, check the file ends with a newline and truncate the
    # partial line if it does not - part 2.5's last failure is what happens
    # without that check.
    raise NotImplementedError


def read_jsonl(path: Path, *, on_error: str = "raise") -> Iterator[dict[str, Any]]:
    """Yield one record per line. `on_error` is 'raise' or 'skip'.

    A generator, so the caller's loop holds one record at a time (part 2.4).
    """
    # TODO(me): open with encoding='utf-8', enumerate from 1 so a failure can
    # name the FILE's line number (part 2.5's second failure - json's own
    # message says 'line 1' whatever line it was). json.loads inside a try.
    #
    # 'skip' must not swallow silently: count what was skipped and make the
    # count reachable. Say in the docstring how a caller gets it.
    raise NotImplementedError


def count_records(path: Path) -> int:
    """How many lines, without holding them."""
    # TODO(me): one line, and it must not build a list (part 2.4). Then say in
    # a comment why this is not the same question as 'how many records parse'.
    raise NotImplementedError
```

**3. `src/setu/atomic.py`** — the context manager the plan names.

```python
"""Write a file, or leave the old one alone."""

from __future__ import annotations

import contextlib
import os
from collections.abc import Iterator
from pathlib import Path
from typing import IO


@contextlib.contextmanager
def atomic_write(path: Path, *, encoding: str = "utf-8") -> Iterator[IO[str]]:
    """Yield a handle to a temporary file; rename it onto `path` on success.

    On failure the temporary file is removed and `path` is untouched - which
    is the property part 2.1's second failure shows `open(path, 'w')` does not
    have.
    """
    # TODO(me): a temporary name IN THE SAME FOLDER (a rename across
    # filesystems is not atomic). Then:
    #
    #   try:
    #       yield the handle          <- part 4.5: this MUST be inside a try
    #   except:
    #       remove the temp file, then RE-RAISE (part 4.4 - catching is
    #       suppressing, and this must not suppress)
    #   else:
    #       flush, os.fsync, then Path.replace onto the final name
    #
    # Say in a comment which of parts 3.2's three levels this reaches, and
    # which failure it therefore does and does not survive.
    raise NotImplementedError
```

**4. Reproduce the eight traps in the notebook, then throw the notebook away.** In
`notebooks/day-16-scratch.ipynb`, in this order:

- Build a path by adding strings with no separator and confirm it "exists" nowhere
  ([1.1](parts/01-the-path/1.1-a-path-is-not-a-string.md)).
- Print `Path('data/x.csv').resolve()`, then `os.chdir('..')`, then print it again
  ([1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md)).
- Write `if folder.glob('*.nothing'):` and watch the branch run
  ([1.5](parts/01-the-path/1.5-globbing.md)).
- Open a file `'w'`, raise before writing, and read the empty file back
  ([2.1](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md)).
- Read a UTF-8 file as latin-1 and **count the characters**, not look at them
  ([2.2](parts/02-reading-and-writing/2.2-encoding.md)).
- Write `'milk\nbread\n'` in text mode and read it back with `read_bytes`
  ([2.3](parts/02-reading-and-writing/2.3-newlines.md)).
- Write two lines, check `stat().st_size` before the close, then after
  ([3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md)).
- Write a `@contextmanager` with a bare `yield` and raise inside the block
  ([4.5](parts/04-context-managers/4.5-contextmanager-decorator.md)).

**The notebook is not committed** (Principle 6); the three modules and their tests are.

**5. Decide, in writing, what `read_jsonl(on_error="skip")` does with what it skipped.** Two sentences in
the docstring. Silently dropping records is the option
[2.5](parts/02-reading-and-writing/2.5-jsonl.md)'s *In production* section argues against; any answer
that makes the count reachable can be defended, and an undecided one cannot.

---

## §5 The eval that must be able to fail

Create `tests/test_jsonl.py` and `tests/test_paths.py`. Every one runs offline, writes only to `tmp_path`
([Day 2, 3.2](../day-02-quality-gate/parts/03-pytest/3.2-fixtures-and-tmp-path.md)), and belongs in
`./m check`.

```python
"""Day 16: what a file writer must promise, and what a context manager must not do."""

from __future__ import annotations

import json

import pytest

from setu.atomic import atomic_write
from setu.jsonl import count_records, read_jsonl, write_jsonl
from setu.paths import safe_child

RECORDS = [{"title": "The Kitchen Table", "year": 2019}, {"title": "One Pot", "year": 2024}]


def test_written_bytes_are_the_same_on_every_machine(tmp_path) -> None:
    """Part 2.3: newline='\\n', or the checksum differs between Windows and CI."""
    # TODO(me): write RECORDS, then assert on read_bytes() exactly. NOT on
    # read_text() - that translates and would pass either way, which is the
    # whole point of this test.
    raise NotImplementedError


def test_every_line_is_one_json_object(tmp_path) -> None:
    """Part 2.5: no indent, one record per line."""
    # TODO(me): assert every line parses on its own AND that the count of
    # lines equals the count of records.
    raise NotImplementedError


def test_a_non_ascii_title_round_trips(tmp_path) -> None:
    """Part 2.2: encoding='utf-8' on the write AND on the read."""
    # TODO(me): a title with an accent in it. Assert the read-back title is
    # equal to the original and that len() matches - the length assertion is
    # what catches mojibake, which compares unequal but looks fine.
    raise NotImplementedError


def test_append_adds_without_rewriting(tmp_path) -> None:
    """Part 2.5: the property that makes the format resumable."""
    # TODO(me): write two, append one, assert three records and that the first
    # two are unchanged.
    raise NotImplementedError


def test_append_after_a_partial_line_does_not_corrupt(tmp_path) -> None:
    """Part 2.5's last failure: a killed writer leaves no trailing newline."""
    # TODO(me): write a file ending mid-record, append, then assert EVERY line
    # parses. Without the check in write_jsonl this loses two records instead
    # of one.
    raise NotImplementedError


def test_reading_holds_one_record_at_a_time(tmp_path) -> None:
    """Part 2.4: read_jsonl is a generator."""
    # TODO(me): assert it is not a list - inspect.isgenerator, or assert that
    # next() works before the file has been fully read. Then say in a comment
    # what a caller loses by wrapping it in list().
    raise NotImplementedError


def test_a_bad_line_can_be_skipped_and_is_counted(tmp_path) -> None:
    """The decision you wrote down in §4, made executable."""
    # TODO(me): three lines, one malformed. on_error='skip' yields two AND the
    # skipped count is reachable. If your design does not make it reachable,
    # this test is impossible to write - which is the test telling you
    # something.
    raise NotImplementedError


def test_a_bad_line_raises_by_default(tmp_path) -> None:
    """Silence is opt-in, never the default."""
    # TODO(me): pytest.raises, and assert the message names the FILE's line
    # number. json's own message always says 'line 1' (part 2.5).
    raise NotImplementedError


def test_count_records_does_not_hold_the_file(tmp_path) -> None:
    """Part 2.4: counting is not reading."""
    # TODO(me): 5000 records, assert the count, and use tracemalloc to assert
    # the peak is under, say, 200_000 bytes. A threshold test is unusual and
    # this is the one place it earns its keep.
    raise NotImplementedError


def test_atomic_write_leaves_the_old_file_on_failure(tmp_path) -> None:
    """Part 2.1's second failure, prevented."""
    # TODO(me): write a good file, then raise inside atomic_write, then assert
    # the ORIGINAL contents are intact. Plain open(p, 'w') fails this.
    raise NotImplementedError


def test_atomic_write_leaves_no_temporary_file_behind(tmp_path) -> None:
    """The cleanup half of part 4.5's try/finally."""
    # TODO(me): after a failure, assert list(tmp_path.iterdir()) holds only
    # the original file.
    raise NotImplementedError


def test_atomic_write_does_not_swallow_the_exception(tmp_path) -> None:
    """Part 4.4: catching is suppressing."""
    # TODO(me): pytest.raises around the failing block. A version that catches
    # to clean up and forgets to re-raise passes every other test in this file.
    raise NotImplementedError


@pytest.mark.parametrize("name", ["../escape.txt", "a/../../escape.txt", "/etc/passwd"])
def test_safe_child_refuses_anything_outside_the_base(tmp_path, name) -> None:
    """Part 1.3: joining does not keep you inside."""
    # TODO(me): pytest.raises(ValueError). All three of these are real shapes
    # that arrive in filenames from archives and URLs.
    raise NotImplementedError


def test_safe_child_allows_an_ordinary_name(tmp_path) -> None:
    """A guard that refuses everything is not a guard."""
    # TODO(me): assert safe_child(tmp_path, 'shopping.txt') is inside tmp_path.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_jsonl.py tests/test_paths.py -v
```

Then implement, then **break each one on purpose**:

- Drop `newline="\n"` from `write_jsonl`. **On Windows only the bytes test goes red**, and on Linux
  nothing does — which is the point, and the reason the test asserts bytes rather than text.
- Add `indent=2` to the `json.dumps`. The one-object-per-line test goes red and the round-trip test stays
  green.
- Drop `encoding="utf-8"` from the read. On this machine the non-ASCII test goes red on the **length**
  assertion while the "did it come back" assertion nearly passes.
- Change `"a"` to `"w"` in `write_jsonl(append=True)`. The append test goes red; every other test stays
  green, because they all write once.
- Remove the trailing-newline check before appending. **Only the partial-line test goes red** — the
  ordinary append test cannot see it.
- Make `read_jsonl` build a list and return it. Only the generator test goes red; every value assertion
  in the file still passes.
- Make `on_error="skip"` drop the count. `test_a_bad_line_can_be_skipped_and_is_counted` goes red, and it
  is the only thing standing between you and a pipeline that loses records quietly.
- Move the `yield` in `atomic_write` outside the `try`. **Only the no-temporary-file test goes red** —
  the file is still written correctly on the happy path.
- **Break it and watch every test stay GREEN** — change `atomic_write` to catch the exception, clean up,
  and *not* re-raise, **and** delete `test_atomic_write_does_not_swallow_the_exception`. Everything
  passes, the old file is preserved, no temporary file is left, and every caller now believes a failed
  write succeeded. Restore the test, watch it go red, and say out loud what it was protecting.

That last item is the most important line in this section. A context manager that swallows is invisible
to every test about content, cleanup and correctness — the only test that can see it is the one that
asserts the exception got out.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |
| Disk | a few megabytes in `tmp_path`, deleted by `pytest` |

Today is the first day that writes real files rather than using `io.StringIO`
([Day 13, 4.2](../day-13-inheritance-and-abstraction/parts/04-abstraction/4.2-the-loader-family.md)), so
the budget grows a row. Every test writes into `tmp_path` and nowhere else — a test that writes to a
relative path writes into whatever folder the runner started in
([1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md)), which is somebody's repository.

---

## §7 Traps

- **Gluing path pieces with `+` and no separator makes a valid, wrong filename** —
  [1.1](parts/01-the-path/1.1-a-path-is-not-a-string.md).
- **A Windows path in a string literal is full of escape sequences** —
  [1.1](parts/01-the-path/1.1-a-path-is-not-a-string.md).
- **A `Path` is never equal to a `str`, however identical they look** —
  [1.1](parts/01-the-path/1.1-a-path-is-not-a-string.md).
- **`.suffix` includes the dot, so comparing with `"txt"` is always `False`** —
  [1.2](parts/01-the-path/1.2-taking-a-path-apart.md).
- **`with_suffix` on `corpus.tar.gz` gives `corpus.tar.jsonl`** —
  [1.2](parts/01-the-path/1.2-taking-a-path-apart.md).
- **A folder with a dot in its name has a `.suffix`** —
  [1.2](parts/01-the-path/1.2-taking-a-path-apart.md).
- **`Path` is immutable, so `p.with_suffix(...)` must be assigned** —
  [1.2](parts/01-the-path/1.2-taking-a-path-apart.md).
- **A relative path means "from wherever the process started", not "beside the script"** —
  [1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md).
- **`base / user_name` can escape `base`, and looks fine until it is resolved** —
  [1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md).
- **`resolve()` succeeds on a path that does not exist unless you pass `strict=True`** —
  [1.3](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md).
- **`exists()` is a snapshot, and check-then-act has a gap in the middle** —
  [1.4](parts/01-the-path/1.4-exists-mkdir-and-the-race.md).
- **`mkdir` without `parents=` fails with `FileNotFoundError` about the thing you asked it to create** —
  [1.4](parts/01-the-path/1.4-exists-mkdir-and-the-race.md).
- **`exist_ok=True` still raises when a *file* is in the way** —
  [1.4](parts/01-the-path/1.4-exists-mkdir-and-the-race.md).
- **`unlink` on something already gone raises, and ruins a cleanup block** —
  [1.4](parts/01-the-path/1.4-exists-mkdir-and-the-race.md).
- **`if folder.glob(...)` is always true — a generator has no `__len__`** —
  [1.5](parts/01-the-path/1.5-globbing.md).
- **A single `*` never crosses a folder boundary** —
  [1.5](parts/01-the-path/1.5-globbing.md).
- **A glob's order is undefined, so anything reproducible needs `sorted()`** —
  [1.5](parts/01-the-path/1.5-globbing.md).
- **A glob can only be consumed once** —
  [1.5](parts/01-the-path/1.5-globbing.md).
- **`w` empties the file at the moment it is opened, before anything is written** —
  [2.1](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md).
- **A loop that opens with `w` keeps only the last iteration** —
  [2.1](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md).
- **Binary mode takes no `encoding` and no `str`** —
  [2.1](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md).
- **No `encoding=` means the locale's, which differs between machines** —
  [2.2](parts/02-reading-and-writing/2.2-encoding.md).
- **Mojibake raises nothing and compounds on every round trip** —
  [2.2](parts/02-reading-and-writing/2.2-encoding.md).
- **A BOM becomes an invisible character on the first column name** —
  [2.2](parts/02-reading-and-writing/2.2-encoding.md).
- **Text mode writes `\r\n` on Windows, so two identical files have different checksums** —
  [2.3](parts/02-reading-and-writing/2.3-newlines.md).
- **`csv` without `newline=""` writes `\r\r\n` and a blank row between every row** —
  [2.3](parts/02-reading-and-writing/2.3-newlines.md).
- **`f.readlines()` holds the whole file plus one object per line** —
  [2.4](parts/02-reading-and-writing/2.4-reading-a-big-file.md).
- **A line from a file keeps its `\n`, so `line == "milk"` is `False`** —
  [2.4](parts/02-reading-and-writing/2.4-reading-a-big-file.md).
- **A file object is an iterator, so a second loop over it sees nothing** —
  [2.4](parts/02-reading-and-writing/2.4-reading-a-big-file.md).
- **`indent=` turns a JSONL file into six invalid lines** —
  [2.5](parts/02-reading-and-writing/2.5-jsonl.md).
- **One malformed line kills a whole ingestion run** —
  [2.5](parts/02-reading-and-writing/2.5-jsonl.md).
- **Appending to a file that ends mid-record loses two records instead of one** —
  [2.5](parts/02-reading-and-writing/2.5-jsonl.md).
- **`f.write` touches no disk — the file can be 0 bytes after several writes** —
  [3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md).
- **A process killed without cleanup loses the buffer, cutting mid-record** —
  [3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md).
- **A reader that arrives while a writer holds the file sees a valid, empty file** —
  [3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md).
- **`close()` does not `fsync`, so a clean close is not power-loss durable** —
  [3.2](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md).
- **`fsync` per record is about a thousand times slower** —
  [3.2](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md).
- **A file's size is never evidence that it is finished** —
  [3.2](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md).
- **One `list()` for a count materialises the whole dataset** —
  [3.3](parts/03-buffering/3.3-fifty-thousand-lines.md).
- **An exceeded memory limit in a container is a silent kill, not a `MemoryError`** —
  [3.3](parts/03-buffering/3.3-fifty-thousand-lines.md).
- **A `close()` below an early `return` runs on one code path** —
  [4.1](parts/04-context-managers/4.1-with-the-block-that-cleans-up.md).
- **`Too many open files` names an innocent file** —
  [4.1](parts/04-context-managers/4.1-with-the-block-that-cleans-up.md).
- **A `return` inside `finally` discards the exception** —
  [4.2](parts/04-context-managers/4.2-try-finally-is-what-with-is.md).
- **An exception raised inside cleanup replaces the real one** —
  [4.2](parts/04-context-managers/4.2-try-finally-is-what-with-is.md).
- **`finally` does not run when the process is killed** —
  [4.2](parts/04-context-managers/4.2-try-finally-is-what-with-is.md).
- **`__exit__` takes four parameters, always** —
  [4.3](parts/04-context-managers/4.3-enter-and-exit-by-hand.md).
- **`__exit__` is not called at all if `__enter__` raised** —
  [4.3](parts/04-context-managers/4.3-enter-and-exit-by-hand.md).
- **Cleanup behind an `if exc_type is None` leaks on the failure path** —
  [4.3](parts/04-context-managers/4.3-enter-and-exit-by-hand.md).
- **`return True` from `__exit__` discards the exception silently** —
  [4.4](parts/04-context-managers/4.4-the-exit-that-swallowed-the-exception.md).
- **`suppress(Exception)` eats real bugs along with the one you meant** —
  [4.4](parts/04-context-managers/4.4-the-exit-that-swallowed-the-exception.md).
- **A `yield` not inside a `try` skips cleanup on the failure path** —
  [4.5](parts/04-context-managers/4.5-contextmanager-decorator.md).
- **In a generator-based context manager, catching is suppressing** —
  [4.5](parts/04-context-managers/4.5-contextmanager-decorator.md).
- **A generator-based context manager is single-use** —
  [4.5](parts/04-context-managers/4.5-contextmanager-decorator.md).
- **A `with` inside a loop closes at the end of each iteration** —
  [4.6](parts/04-context-managers/4.6-a-connection-that-always-closes.md).
- **An `ExitStack` with nothing registered exits silently and closes nothing** —
  [4.6](parts/04-context-managers/4.6-a-connection-that-always-closes.md).

---

## §8 Verify before you code

Fetched **2026-09-01**. Today is the language and five standard-library modules, so the library reference
and the PEPs are the authority:

- <https://docs.python.org/3/library/pathlib.html> — `Path`, its attributes, `glob`, `mkdir`, `resolve`
  and `is_relative_to`, with a table mapping every `os.path` function to its `pathlib` equivalent.
- <https://peps.python.org/pep-0428/> — *PEP 428 — The pathlib module* (2012), which states the problems
  with string paths that the module exists to solve.
- <https://docs.python.org/3/library/functions.html#open> — `open`, the full mode table, and the
  `buffering`, `encoding`, `errors` and `newline` parameters, including the sentence about `csv`.
- <https://docs.python.org/3/library/io.html> — the layered picture of raw, buffered and text streams,
  which is where [3.1](parts/03-buffering/3.1-the-write-that-had-not-happened.md)'s buffer lives.
- <https://peps.python.org/pep-0597/> — *PEP 597 — Add optional EncodingWarning* (2019), on why the
  default encoding is a hazard and how to be warned about it.
- <https://docs.python.org/3/library/os.html#os.fsync> — `os.fsync`, and the paragraph admitting it may
  not reach the physical platters on every system.
- <https://docs.python.org/3/reference/compound_stmts.html#the-with-statement> — the language reference's
  translation of `with` into `try` / `finally`.
- <https://docs.python.org/3/library/contextlib.html> — `contextmanager`, `suppress`, `closing`,
  `redirect_stdout` and `ExitStack`.
- <https://jsonlines.org/> — the JSON Lines convention, stated in about a page.

---

## §9 Say it in an interview

> "A path has structure, so I use `pathlib` — `.stem`, `.suffix`, `.parent` instead of string slicing
> with edge cases, and `/` to join, which gets the separator right on every machine. The thing I am
> careful about is that a relative path means 'from wherever the process was started', which is set by
> the shell or the scheduler or the container and has nothing to do with where the source file lives, so
> paths get resolved once at the entry point and passed inward as absolute `Path` objects — and anything
> joined with a name from outside gets `resolve()` and an `is_relative_to` check, because `base / name`
> will happily walk out of `base`. On files, I always pass `encoding='utf-8'`: without it Python uses the
> locale's, which differs between my laptop and the CI runner, and the failure is either a
> `UnicodeDecodeError`, which is the good outcome, or mojibake, which is silent and breaks equality and
> deduplication downstream. And `newline='\n'` on anything another program parses, so the bytes are
> identical everywhere and a content hash means something. The thing people underestimate is buffering:
> `f.write` copies into a buffer in your process and usually touches no disk, so a file can be zero bytes
> after several successful writes, and a process killed without cleanup loses whatever is in the buffer
> — cut at a buffer boundary, not a record boundary, which is why a truncated last record is the normal
> shape of an interrupted write. `close` flushes to the operating system; `fsync` is what survives power
> loss, and it is about a thousand times slower, so it belongs at commit points and nowhere else. For
> writing large files I stream: a generator source, one record per write, no list in between, so peak
> memory does not depend on the input size — and I write to a temporary name and rename, because a rename
> is atomic and `open(path, 'w')` destroys the old file the moment it is called. `with` is `try` /
> `finally` with the cleanup living in the object instead of at every call site, and the two things I
> watch for in a hand-written one are that `__exit__` must not return a true value — that silently
> discards the exception — and that in the `@contextmanager` form the `yield` must be inside a `try`, or
> the cleanup is skipped on exactly the path you wrote it for."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, `src/setu/jsonl.py` writes
50 000 records with a flat memory peak, `src/setu/atomic.py` leaves the old file intact on failure and
lets the exception through, and you have **watched a whole test suite stay green through a context
manager that swallows exceptions** — in §5 — not when a particular amount of time has passed. Then:

```bash
./m done 16
```

Tomorrow is modules, packages and imports: how `src/setu/jsonl.py`, `src/setu/paths.py` and everything
else you have written since Day 10 find each other, and what `__init__.py` is actually for.
