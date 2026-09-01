---
day: 11
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Day 11 — Iterators, generators, `lambda` and `map`"
ids: ["PY-11", "PY-12"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: gate
plan: setu
plan_version: "v2.3.0"
parts: 15
generated: "2026-09-01"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 11 — Iterators, generators, `lambda` and `map`

**Phase 1 · Python foundations · Module 1 · the gate** · `PY-11` iterators and generator functions,
`PY-12` lambda, `map` and functional style. The plan's named examples are *streaming a 2 GB log
line-by-line without loading it* and *where a lambda helps and where it hurts readability*. This is
the last day of Module 1, and Phase 1's deliverable — a ten-function `src/setu/textutils.py`, fully
tested — has to be true when it ends.

> **Yesterday:** how to give a piece of work a name, a signature and a home, and the two scope rules
> that decide what a name means inside it.
> **Today:** the object that hands out one thing at a time, the keyword that builds one for you, the
> smallest function in the language — and the gate that closes Module 1.
> **Tomorrow:** classes, and the `Paper` object the rest of this plan passes around.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

There is a small deli near the station with a paper roll by the door. You tear off a slip, write your
order on it, and drop it in the box. The person behind the counter takes slips out of the box one at
a time and makes them up.

Four slips came out this morning:

```text
milk
  Milk
eggs
Eggs.
```

Everything today is somewhere in that shop.

- **The roll by the door** is a list: go to it as often as you like, and it is still there tomorrow.
- **The box of today's orders** is a reader: it has a position, it only moves forwards, and when it
  is empty it stays empty. Ask an empty box how many there were and it cannot tell you, because the
  answer left one slip at a time.
- **The helper who reads one line, hands it over, and stops mid-sentence** is a generator. They have
  not finished and they have not forgotten where they were. They are simply not moving until somebody
  asks again.
- **The filing cabinet in the back** is a file too large to put on the table. You do not pile a year
  of slips on the floor to count them. You take one, add one to a running total, and drop it in the
  recycling — and the room looks the same at the end as it did at the start.
- **The three people standing in a line**, each doing one small thing and handing the slip along, are
  a pipeline. Nothing accumulates between them, however many slips come through.
- **The card taped to the wall with a title on it** is a named function. **The instruction you say
  out loud for a thirty-second job** is a lambda. Both are instructions; only one of them can be
  looked up afterwards by somebody who was not there, and that difference is the whole judgement.

And one scene that is not about cleverness at all. Somebody works out that you can count the year's
slips one at a time, which is right. Then they are asked for the three most common orders, and the
middle order of the day, and the fifth slip — and none of those can be answered by a method that
throws each slip away. The method was not wrong. It was right for one question and wrong for the next
three, and nobody had said so out loud.

The day ends where the plan says Phase 1 ends: the module is ten functions, every promise in every
docstring has a test that can go red, and the whole thing works on a file it could never hold.

```mermaid
flowchart LR
    S1["§1 iterators<br/>the box, by hand"] --> S2["§2 generators<br/>the helper who pauses"]
    S2 --> S3["§3 lambda and map<br/>small functions, lazy tools"]
    S3 --> S4["§4 the gate<br/>ten functions, fully tested"]
    style S1 fill:#1f6feb,color:#fff
    style S4 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** Two IDs and a gate, so the plan's `lab (2 IDs)` split plus a
gate section: **1.x** is `PY-11`'s foundation — the iterator protocol, built by hand before it is
used; **2.x** is the rest of `PY-11` — generators, which write that protocol for you, and what they
cost; **3.x** is `PY-12` — the smallest function in the language and the lazy tools that take one;
**4.x** is the gate, one document per acceptance criterion.

### Section 1 — iterators

| Part | What it answers | Level |
|---|---|---|
| [1.1 Iterable and iterator — the roll and the slip](parts/01-iterators/1.1-iterable-and-iterator.md) | Why does `iter()` on an iterator give back the same object? | `foundation` |
| [1.2 Building the reader by hand](parts/01-iterators/1.2-writing-next-by-hand.md) | What exactly does a `for` loop require of the object you give it? | `working` |
| [1.3 Exhaustion, and the second loop that saw nothing](parts/01-iterators/1.3-exhaustion.md) | Why did `len(list(box))` destroy the thing it counted? | `working` |
| [1.4 `iter()` with a sentinel](parts/01-iterators/1.4-iter-with-a-sentinel.md) | How do you loop over something that only knows "give me the next one"? | `production` |

### Section 2 — generators

| Part | What it answers | Level |
|---|---|---|
| [2.1 `yield` — the function that pauses](parts/02-generators/2.1-yield-the-function-that-pauses.md) | How much of the body has run when you call a generator function? | `foundation` |
| [2.2 A list against a generator, measured](parts/02-generators/2.2-a-list-against-a-generator.md) | What is the saving worth, in megabytes, on a million items? | `working` |
| [2.3 Streaming a file one line at a time](parts/02-generators/2.3-streaming-a-file.md) | How do you process a file bigger than memory, and what breaks the guarantee? | `production` |
| [2.4 `yield from`, and generators as a pipeline](parts/02-generators/2.4-yield-from-and-the-pipeline.md) | What does `yield from` forward that a manual loop drops? | `production` |
| [2.5 When a generator is the wrong tool](parts/02-generators/2.5-when-a-generator-is-wrong.md) | Which three things does a list do that a generator cannot? | `production` |

### Section 3 — lambda and map

| Part | What it answers | Level |
|---|---|---|
| [3.1 `lambda` — a function with no name](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md) | If a lambda is not faster or more powerful, why does the keyword exist? | `foundation` |
| [3.2 `map`, `filter`, and the iterator you printed by mistake](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md) | How many times has your function run when `map` returns? | `working` |
| [3.3 Where a lambda helps and where it hurts](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md) | Which four things does a lambda give up, and what does it buy? | `production` |
| [3.4 `reduce`, `any`, `all`, and the short circuit](parts/03-lambda-and-map/3.4-reduce-any-and-all.md) | Why is `all([])` `True`, and what does that cost in production? | `production` |

### Section 4 — the gate

| Part | What it answers | Level |
|---|---|---|
| [4.1 Ten functions, fully tested](parts/04-the-gate/4.1-ten-functions-fully-tested.md) | What exactly does "fully tested" mean, if it is not a coverage number? | `production` |
| [4.2 The streaming reader `textutils` needed](parts/04-the-gate/4.2-the-streaming-reader.md) | Why does the reader take an open handle rather than a path? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `itertools`, `functools`,
`operator`, `tracemalloc`, `io` and `sys` from the standard library. Module 1 is the language before
any library, and today is its last day.

```bash
mkdir -p src/setu tests notebooks data

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-11-scratch.ipynb

# yesterday's module must already exist - today ADDS to it, never replaces it
uv run python -c "import setu.textutils as t; print('module at:', t.__file__)"

# the four facts the day is built on, before any part names them
uv run python -c "
slips = ['milk', '  Milk', 'eggs', 'Eggs.']
box = iter(slips)
print('1 reader type :', type(box).__name__, '<- not list (part 1.1)')
print('2 exhaustion  :', len(list(box)), 'then', list(box), '<- part 1.3')
def lazy():
    yield 1
print('3 call a gen   :', type(lazy()).__name__, '<- the body has NOT run (part 2.1)')
print('4 map is lazy  :', map(str.strip, slips), '<- part 3.2')
"

# the measurement the whole of section 2 rests on - run it and read YOUR numbers
uv run python -c "
import tracemalloc
tracemalloc.start()
sum([n * n for n in range(1_000_000)])
print('list peak MB:', round(tracemalloc.get_traced_memory()[1] / 1048576, 3))
tracemalloc.stop()
tracemalloc.start()
sum(n * n for n in range(1_000_000))
print('gen  peak MB:', round(tracemalloc.get_traced_memory()[1] / 1048576, 3))
tracemalloc.stop()
"

# the rule that refuses a named lambda, read from the linter you have installed
uv run ruff rule E731
```

| What | Where it comes from | Part |
|---|---|---|
| `iter`, `next`, `StopIteration` | language, built-ins | [1.1](parts/01-iterators/1.1-iterable-and-iterator.md) |
| `__iter__`, `__next__` | language | [1.2](parts/01-iterators/1.2-writing-next-by-hand.md) |
| `nonlocal` | already met on [Day 10](parts/01-iterators/1.2-writing-next-by-hand.md) | [1.2](parts/01-iterators/1.2-writing-next-by-hand.md) |
| `iter(callable, sentinel)` | built-ins | [1.4](parts/01-iterators/1.4-iter-with-a-sentinel.md) |
| `yield`, `yield from`, `gi_frame`, `close()` | language | [2.1](parts/02-generators/2.1-yield-the-function-that-pauses.md), [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md) |
| `tracemalloc`, `sys.getsizeof` | standard library | [2.2](parts/02-generators/2.2-a-list-against-a-generator.md) |
| `pathlib.Path`, `io.StringIO`, `itertools.cycle` | standard library | [2.3](parts/02-generators/2.3-streaming-a-file.md), [4.2](parts/04-the-gate/4.2-the-streaming-reader.md) |
| `lambda` | language | [3.1](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md) |
| `map`, `filter`, `any`, `all` | built-ins | [3.2](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md), [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md) |
| `operator.itemgetter`, `functools.reduce` | standard library | [3.3](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md), [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md) |
| `casefold`, `strip` | already met on [Day 7](../day-07-strings/parts/02-methods/2.1-normalising-strip-and-case.md) | [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md) |
| order-preserving dedup | already met on [Day 8](../day-08-containers/parts/03-dedup/3.2-order-preserving-dedup.md) | [4.2](parts/04-the-gate/4.2-the-streaming-reader.md) |
| ruff's `E731` and `B023` | already selected on [Day 2](../day-02-quality-gate/parts/01-linting/1.2-choosing-rule-families.md) | [3.1](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md), [3.3](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md) |

---

## §4 Build brief

**One module, finished.** Yesterday wrote seven functions into `src/setu/textutils.py`; today adds
three and brings the file to the ten the plan asks for
([4.1](parts/04-the-gate/4.1-ten-functions-fully-tested.md) has the whole table).

**1. Add three functions to `src/setu/textutils.py`** — do not create a second module, and do not
change the seven that are there except to fix a signature you can defend.

```python
"""Appended to src/setu/textutils.py - the lazy half of the module."""

from collections.abc import Callable, Iterable, Iterator
from typing import TextIO


def iter_titles(handle: TextIO) -> Iterator[str]:
    """Yield each non-empty line of `handle`, cleaned by `clean_title`, one at a time.

    Takes an already-open text handle rather than a Path, so a test can pass
    io.StringIO and never touch a disk (part 4.2). Peak memory does not grow with
    the size of the file.

    Blank and whitespace-only lines are skipped, never yielded as "".
    """
    # TODO(me): a for loop over `handle`, clean_title on each line, skip empties.
    # Part 2.3 has the shape. Decide - and write in a comment - whether you strip
    # the newline yourself or let clean_title's collapse step do it. Those two
    # choices differ on a line that is only "\n", so pick one and test it.
    raise NotImplementedError


def unique_titles(titles: Iterable[str]) -> Iterator[str]:
    """Yield each title the first time its `title_key` is seen, in input order.

    Lazy in and lazy out. Holds one set of keys, so its memory grows with the
    number of DISTINCT titles rather than with the input - that is the honest
    exception to "a generator holds one item" (part 2.5).
    """
    # TODO(me): day 8 part 3.2's dedup, rewritten as a generator. The decision that
    # matters is which value goes in the set and which value you YIELD, and getting
    # those the wrong way round makes "milk" and "  Milk" two different orders.
    raise NotImplementedError


def titles_matching(
    titles: Iterable[str],
    predicate: Callable[[str], bool],
) -> Iterator[str]:
    """Yield the titles for which `predicate` returns True, in input order.

    `predicate` is called once per title, lazily, and NOT AT ALL for titles after
    the caller stops reading.
    """
    # TODO(me): one loop, one if, one yield. Then write the test that proves the
    # last sentence of this docstring, because an untested promise in a docstring
    # is worse than no promise (part 4.1).
    raise NotImplementedError
```

**2. Reproduce the four traps in the notebook, then throw the notebook away.** In
`notebooks/day-11-scratch.ipynb`, in this order:

- Build a reader with `iter()`, call `len(list(...))` on it, then `list(...)` again, and watch the
  second one come back empty ([1.3](parts/01-iterators/1.3-exhaustion.md)).
- Write the `SheetReader` class from [1.2](parts/01-iterators/1.2-writing-next-by-hand.md) with the
  three lines of `__next__` **in the wrong order on purpose**, and count how many of the four slips
  come out.
- Print a `map` object without `list()` around it, then with, and note which one you would have
  written by accident ([3.2](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md)).
- Run `any(...)` over a generator, then `list()` the same generator, and see what is left
  ([3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md)).

**The notebook is not committed** (Principle 6). `src/setu/textutils.py` and its tests are.

**3. Build the big file once, and keep it out of git.** `data/slips_big.txt` from
[2.3](parts/02-generators/2.3-streaming-a-file.md) is a million generated lines. Check that
`data/` is ignored ([Day 0, 2.2](../day-00-setup/parts/02-skeleton/2.2-gitignore-before-secrets-exist.md))
before you build it, because a 6 MB generated file in the history is there forever.

**4. Read your seven existing functions once more with today's question.** For each, ask: *should this
return a container or a reader?* Most of them should stay exactly as they are — `clean_title` returns
one string and `same_title` returns a bool. `clean_titles` is the interesting one, and the answer is
that it stays a list, for a reason [4.1](parts/04-the-gate/4.1-ten-functions-fully-tested.md)'s table
gives. **Write that reason in its docstring** if it is not already there.

---

## §5 The eval that must be able to fail

Add these to `tests/test_textutils.py`. Every one runs offline and belongs in `./m check`.

```python
"""Day 11: prove the three new promises, rather than believing them."""

from __future__ import annotations

import io
import itertools
import tracemalloc

from setu.textutils import iter_titles, titles_matching, unique_titles


def test_iter_titles_skips_blank_and_whitespace_only_lines() -> None:
    """The docstring promises blanks are skipped, never yielded as ''."""
    # TODO(me): a StringIO with a blank line, a spaces-only line and two real
    # titles. Assert the WHOLE list, written out by hand - a length assertion
    # alone would pass for a function that yielded "" twice.
    raise NotImplementedError


def test_iter_titles_yields_cleaned_titles() -> None:
    """It promises clean_title, not str.strip - so assert on a case only clean_title fixes."""
    # TODO(me): include a title with a doubled inner space and a trailing dot.
    # If your assertion passes for a body that only calls .strip(), it is not
    # testing the promise in the docstring.
    raise NotImplementedError


def test_iter_titles_is_a_reader_not_a_list() -> None:
    """Part 1.1: the annotation says Iterator, so assert it behaves like one."""
    # TODO(me): list() it twice and assert the second is empty. Then write a
    # comment saying why that is the CORRECT behaviour and not a bug.
    raise NotImplementedError


def test_iter_titles_peak_memory_does_not_grow_with_the_file() -> None:
    """Part 2.2: a memory promise is a behaviour, so it gets an assertion."""
    # TODO(me): 100_000 lines through io.StringIO, counted with
    # sum(1 for _ in iter_titles(handle)), measured with tracemalloc, asserted
    # under a megabyte. A four-line version of this test proves nothing.
    raise NotImplementedError


def test_unique_titles_keeps_input_order() -> None:
    """An order promise needs three items and the duplicate in the middle."""
    # TODO(me): two items would pass an implementation that returns sorted(set(...)).
    # Three, with the repeat in the middle, would not.
    raise NotImplementedError


def test_unique_titles_compares_by_key_not_by_string() -> None:
    """'milk' and '  Milk' are one order, and title_key is why."""
    # TODO(me): assert which of the two survives - the first, as it was written.
    # That distinction is the whole reason title_key and clean_title are separate.
    raise NotImplementedError


def test_unique_titles_is_lazy_in_its_input() -> None:
    """It must not materialise what it is given."""
    # TODO(me): pass it a generator that appends to a list as it yields. Take one
    # item with next(). Assert the list has ONE entry, not all of them.
    raise NotImplementedError


def test_titles_matching_calls_the_predicate_once_per_title() -> None:
    """The predicate is the caller's, so its call count is the caller's business."""
    # TODO(me): a predicate that records each call. Consume the whole thing.
    # Assert the recorded calls equal the input, in order.
    raise NotImplementedError


def test_titles_matching_stops_calling_when_the_caller_stops() -> None:
    """The laziness claim in the docstring, made executable."""
    # TODO(me): itertools.islice to take two, then assert on the LENGTH of the
    # recorded calls. If it equals the input length, the docstring is lying.
    raise NotImplementedError


def test_pipeline_holds_one_title_at_a_time() -> None:
    """Part 2.4: the three stages compose without collecting anything."""
    # TODO(me): assemble titles_matching(unique_titles(iter_titles(handle)), pred)
    # and assert type(pipeline).__name__ == "generator" BEFORE consuming it.
    # Then consume it and assert the result.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_textutils.py -v
```

Then implement, then **break each one on purpose**:

- Change `iter_titles`'s `yield` to build a list and `return` it → the reader test goes red and the
  memory test goes red. **Two tests for one edit is the sign they are testing different promises.**
- Change `unique_titles` to `yield from set(titles)` → the order test goes red and the key test goes
  red. Restore it, and say out loud why a two-item test would have stayed green.
- Change `titles_matching` to build a list first → **the call-count test stays green and the
  stop-early test goes red.** That pair is the whole difference between "it filters" and "it filters
  lazily".
- Delete the blank-line guard in `iter_titles` → the skip test goes red with a diff containing `''`.
- Make the memory test use four lines instead of a hundred thousand → **every test still passes,
  including the memory one, with the list implementation in place.** Do not restore it until you can
  say what that proves about test data size.

That last item is the most important line in this section. A green suite over a defect is exactly the
failure Principle 7 exists to prevent, and here it is caused by the size of the input rather than by a
missing assertion.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |
| Disk | ~6.5 MB for `data/slips_big.txt`, generated locally and git-ignored |

Module 1 is the language before any library, so the whole day runs offline. `./m check` still runs
`-m "not live"`, so today's tests join the free path only
([Day 2, 5.3](../day-02-quality-gate/parts/05-ci/5.3-caching-and-never-spending-a-quota.md)).

---

## §7 Traps

- **A list is iterable but is not an iterator; `next()` on one raises** —
  [1.1](parts/01-iterators/1.1-iterable-and-iterator.md).
- **`iter()` on an iterator returns the same object, so two names share one position** —
  [1.1](parts/01-iterators/1.1-iterable-and-iterator.md).
- **"not iterable" and "not an iterator" are different errors that read the same** —
  [1.1](parts/01-iterators/1.1-iterable-and-iterator.md).
- **`__next__` without `__iter__` fails with "object is not iterable"** —
  [1.2](parts/01-iterators/1.2-writing-next-by-hand.md).
- **Moving the position before taking the item silently drops the first one** —
  [1.2](parts/01-iterators/1.2-writing-next-by-hand.md).
- **`len(list(reader))` gives the right answer and destroys the data** —
  [1.3](parts/01-iterators/1.3-exhaustion.md).
- **An exhausted reader returns empty forever, with no error** —
  [1.3](parts/01-iterators/1.3-exhaustion.md).
- **A function that validates and then processes eats its own input** —
  [1.3](parts/01-iterators/1.3-exhaustion.md), [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md).
- **A sentinel of the wrong type never matches, and the loop hangs with no error** —
  [1.4](parts/01-iterators/1.4-iter-with-a-sentinel.md).
- **`iter(f.read, "")` reads the whole file as one block and looks correct** —
  [1.4](parts/01-iterators/1.4-iter-with-a-sentinel.md).
- **Calling a generator function runs none of its body, so its argument checks never fire** —
  [2.1](parts/02-generators/2.1-yield-the-function-that-pauses.md).
- **A `yield` anywhere makes the whole function a generator, even on a line that never runs** —
  [2.1](parts/02-generators/2.1-yield-the-function-that-pauses.md).
- **`reset_peak()` does not reset to zero, so a home-made memory benchmark lies** —
  [2.2](parts/02-generators/2.2-a-list-against-a-generator.md).
- **A `list()` or `sorted()` downstream undoes the whole memory saving** —
  [2.2](parts/02-generators/2.2-a-list-against-a-generator.md),
  [2.5](parts/02-generators/2.5-when-a-generator-is-wrong.md).
- **Iterating a file gives lines with their newline still attached** —
  [2.3](parts/02-generators/2.3-streaming-a-file.md).
- **`.readlines()` looks like streaming and holds the whole file** —
  [2.3](parts/02-generators/2.3-streaming-a-file.md).
- **A file with no newlines defeats "one line at a time" entirely** —
  [2.3](parts/02-generators/2.3-streaming-a-file.md).
- **`yield from generator_function` without brackets raises "not iterable"** —
  [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md).
- **A recursive flattener with no base case recurses into single characters** —
  [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md).
- **`StopIteration` raised inside a generator becomes `RuntimeError`** —
  [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md).
- **A suspended generator holds its open file until it is closed or collected** —
  [2.5](parts/02-generators/2.5-when-a-generator-is-wrong.md).
- **A generator cannot be pickled, so it cannot cross a process boundary** —
  [2.5](parts/02-generators/2.5-when-a-generator-is-wrong.md).
- **`f = lambda x: ...` is refused by ruff's `E731`, and it should be** —
  [3.1](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md).
- **Every lambda's `__name__` is `<lambda>`, in every traceback and every profile** —
  [3.1](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md),
  [3.3](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md).
- **Lambdas built in a loop capture the name, not the value** —
  [3.1](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md).
- **Printing a `map` shows an address, because nothing has run** —
  [3.2](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md).
- **`map` truncates silently at the shorter of two sources, and has no `strict=`** —
  [3.2](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md).
- **`filter(None, ...)` keeps a string of spaces, and `filter(str.strip, ...)` does not** —
  [3.2](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md).
- **`key=lambda x: len(x)` is `key=len`, and the wrapper costs a frame per item** —
  [3.3](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md).
- **`reduce` over an empty sequence with no initial value raises** —
  [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md).
- **`reduce` passes the running value first, and addition hides the mistake** —
  [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md).
- **`all([])` is `True`, so an empty import passes every validation** —
  [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md).
- **A short circuit leaves a generator parked mid-stream** —
  [3.4](parts/03-lambda-and-map/3.4-reduce-any-and-all.md).
- **A test whose expected value is computed by the code under test asserts nothing** —
  [4.1](parts/04-the-gate/4.1-ten-functions-fully-tested.md).
- **Ten functions reached by splitting one is a worse module than seven** —
  [4.1](parts/04-the-gate/4.1-ten-functions-fully-tested.md).
- **A generator created inside a `with` and consumed outside it hits a closed file** —
  [4.2](parts/04-the-gate/4.2-the-streaming-reader.md).
- **A memory test over four lines passes for the implementation it was meant to catch** —
  [4.2](parts/04-the-gate/4.2-the-streaming-reader.md).

---

## §8 Verify before you code

Fetched **2026-09-01**. Today is about the language itself, so the language reference and the PEPs are
the authority rather than any library's documentation:

- <https://docs.python.org/3/library/stdtypes.html#iterator-types> — the iterator protocol in the
  standard library's own words, including the sentence that an iterator's `__iter__` must "return the
  iterator object itself" and that once `__next__` raises `StopIteration` "it must continue to do so
  on subsequent calls". That is [1.1](parts/01-iterators/1.1-iterable-and-iterator.md) and
  [1.3](parts/01-iterators/1.3-exhaustion.md).
- <https://docs.python.org/3/library/functions.html#iter> — both forms of `iter`, including the
  sentence that with a sentinel "the first argument must be a callable object" and the block-reader
  example. That is [1.4](parts/01-iterators/1.4-iter-with-a-sentinel.md).
- <https://docs.python.org/3/reference/expressions.html#yield-expressions> — what `yield` and
  `yield from` do to a function, and the generator methods `send`, `throw` and `close`.
- <https://peps.python.org/pep-0255/> — *Simple Generators* (2001), which introduced `yield` so a
  function could hand back values while keeping its local state between resumptions.
- <https://peps.python.org/pep-0479/> — *Change StopIteration handling inside generators* (2014),
  which is why a stray `StopIteration` inside a generator becomes a `RuntimeError`, the default
  everywhere since Python 3.7. That is
  [2.4](parts/02-generators/2.4-yield-from-and-the-pipeline.md)'s first failure.
- <https://docs.python.org/3/howto/functional.html> — the functional-programming HOWTO, whose
  sections on iterators, generators, `lambda`, `map`/`filter` and `functools.reduce` are the
  standard library's own version of section 3, including its recommendation to prefer a `for` loop
  over `reduce`.
- <https://peps.python.org/pep-0008/> — the style guide, for the sentence about never binding a
  lambda to a name with `=`, which is [3.3](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md).
- <https://docs.python.org/3/library/tracemalloc.html> — `start`, `get_traced_memory` and the
  current-versus-peak pair that [2.2](parts/02-generators/2.2-a-list-against-a-generator.md) measures
  with.
- `uv run ruff rule E731` and `uv run ruff rule B023` — the two rules that catch today's headline
  mistakes, read from the linter you have installed rather than from memory.

---

## §9 Say it in an interview

> "The pair I always start with is iterable and iterator, because most confusion in this area is
> people treating one as the other: an iterable can hand you a fresh reader whenever you ask, and an
> iterator *is* that reader — it holds a position, it only moves forwards, and `iter()` on it returns
> itself rather than a new one, which is exactly why a `for` loop works on both and exactly why the
> second loop over a generator is silently empty. A generator function is the easy way to build one:
> the moment there is a `yield` anywhere in the body, calling the function runs none of it and hands
> you a paused object, which is a real gotcha because any argument validation inside it fires at the
> first `next()` rather than at the call — so I split it into a plain wrapper that validates and a
> private generator that streams. The reason I care is memory: a million squares as a list peaks
> around 38 MB and as a generator around a kilobyte, and a file iterated one line at a time has a peak that
> does not grow with the file at all, which is the difference between a job that runs on a small box
> and one that gets killed. But I am equally clear about when not to: a generator gives up length,
> indexing, sorting, reversing, pickling and a second pass, so anything that needs to look back wants
> a list, and I make that a deliberate `list(...)` on a line somebody can point at rather than an
> accident. The two that catch people are `sorted()` on a generator, which silently materialises
> everything, and a suspended generator holding an open file until it is closed. On the functional
> side, `map` and `filter` are lazy too — printing one gives you an object, not your data — and
> `lambda` I use only as an argument, one expression, never named: PEP 8 and ruff's E731 both say
> bind a `def` instead, because the assignment throws away the one thing a lambda has, being an
> expression, and keeps the one cost, which is that every traceback and every profile line says
> `<lambda>`."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, `src/setu/textutils.py`
has ten public functions with a test per promise, and you have **watched the memory test pass over a
four-line input with the wrong implementation in place** — not when a particular amount of time has
passed. Then:

```bash
./m done 11
```

That commit closes Phase 1 and Module 1. Tomorrow starts Phase 2 with classes, and the first object
is `Paper` — the thing the capstone's Reader agent passes around, and the first place these ten
functions get called by something other than a test.
