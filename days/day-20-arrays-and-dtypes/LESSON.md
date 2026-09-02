---
day: 20
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 20 — ndarray, dtypes, and array creation (NumPy 2.x names)"
ids: ["NP-01", "NP-02"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 20
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 20 — `ndarray`, dtypes, and array creation (NumPy 2.x names)

**Phase 3 · NumPy · Module 3 · the first day of a new phase** · `NP-01` the `ndarray`, its dtypes and
its attributes; `NP-02` array creation from data and from ranges. The plan's named examples are
**a Python list of a million floats against an `ndarray` — memory and time, measured** and
**`array`, `zeros`, `arange`, `linspace`, `random.default_rng` (seeded — Principle 4)**. Both are
built today, and the phase gate they feed — **a vectorised stats module beating a loop by ≥50×** on
Day 25 — is only reachable because of what this day establishes.

> **Yesterday:** typing, dataclasses, Pydantic and concurrency closed Phase 2, and the phase gate
> asked for a `Paper` hierarchy, custom exceptions and a tested async fetcher.
> **Today:** a completely different kind of object. Everything so far has been Python objects with
> pointers between them; an array is one block of memory with a description attached, and every
> speed and memory property in the rest of this curriculum comes from that.
> **Tomorrow:** indexing and slicing that same block — and the fact that a slice does not copy,
> which is the most surprising behaviour in the library.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody keeps a note on their phone of how many steps they walk each day. Last week it read 8213,
10442, 6180, then a zero on Thursday because the phone spent the day on the kitchen charger, then
12007, 9631, 7204.

Seven numbers. You could write them on seven sticky notes and drop them in an envelope, or you could
rule a strip of card into seven equal cells and write one number in each.

The envelope is easy. Each note can hold anything — a number, a word, a doodle — and you can add an
eighth whenever you like. To read Friday's number you tip the envelope out and hunt.

The strip of card is stricter. Every cell is the same width, so every cell has to hold the same kind
of thing, and you cannot squeeze an eighth in. In exchange, reading Friday's number is counting four
cells along, the whole strip fits in a corner of the drawer, and if you want to double every number
you can work along the row without stopping to think about what each cell contains.

That is the trade this whole phase rests on. Python's list is the envelope. A NumPy array is the
strip of card. Neither is better in general — but for a million numbers, the strip uses a quarter of
the room and can be read a hundred times faster, and that difference is what makes the rest of data
science possible on an ordinary laptop.

Today is about the strip: what it is made of, what one cell may hold, and the handful of ways to
bring one into being.

---

## §2 The map

**What the section numbers mean today.** This is a `lab` day with two IDs, so the split is one
section per ID plus a synthesis. **1.x and 2.x are `NP-01`** — 1.x is the object itself, its memory
and its measured advantage, and 2.x is what a single cell may hold. **3.x and 4.x are `NP-02`** —
3.x makes arrays from data and from ranges, and 4.x makes them from a seeded generator, which the
plan calls out separately because Principle 4 applies to randomness. **5.x is the synthesis**: the
module where both IDs meet, and its eval.

### Section 1 — the block

| Part | What it answers | Level |
|---|---|---|
| [1.1 A list of boxes](parts/01-the-block/1.1-a-list-of-boxes.md) | What is actually different from a list? | `foundation` |
| [1.2 The six questions](parts/01-the-block/1.2-shape-dtype-and-the-rest.md) | What can an array tell you about itself for free? | `foundation` |
| [1.3 One block, and strides](parts/01-the-block/1.3-one-block-and-strides.md) | How does it find element four without looking? | `working` |
| [1.4 A million numbers, measured](parts/01-the-block/1.4-a-million-floats-measured.md) | How much faster, honestly? | `production` |

### Section 2 — dtypes

| Part | What it answers | Level |
|---|---|---|
| [2.1 A dtype is a promise](parts/02-dtypes/2.1-a-dtype-is-a-promise.md) | What happens when you do not state one? | `foundation` |
| [2.2 The silent wrap](parts/02-dtypes/2.2-integers-and-the-silent-wrap.md) | Why did four times a step count go negative? | `working` |
| [2.3 Floats, `NaN`, precision](parts/02-dtypes/2.3-floats-nan-and-precision.md) | Why is `arr == np.nan` always `False`? | `working` |
| [2.4 `astype` and the copy](parts/02-dtypes/2.4-astype-and-the-copy.md) | Does it round or truncate? | `working` |
| [2.5 NEP 50](parts/02-dtypes/2.5-nep-50-and-the-python-number.md) | What does a plain `2.0` do to a `float32` array? | `production` |
| [2.6 The removed names](parts/02-dtypes/2.6-the-names-that-were-removed.md) | Why does this tutorial's code not run? | `production` |

### Section 3 — creating

| Part | What it answers | Level |
|---|---|---|
| [3.1 `np.array`](parts/03-creating/3.1-np-array-and-what-it-infers.md) | Where do the shape and the dtype come from? | `foundation` |
| [3.2 `zeros`, `ones`, `full`, `empty`](parts/03-creating/3.2-zeros-ones-full-and-empty.md) | Why is `np.empty` not empty? | `working` |
| [3.3 `arange`](parts/03-creating/3.3-arange-and-the-float-step.md) | Why did eleven values come back? | `working` |
| [3.4 `linspace`](parts/03-creating/3.4-linspace.md) | How many points give hundredths from 0 to 1? | `working` |
| [3.5 `_like`, `eye`, `diag`](parts/03-creating/3.5-like-and-the-identity.md) | Why not just type the shape out? | `working` |

### Section 4 — randomness, seeded

| Part | What it answers | Level |
|---|---|---|
| [4.1 `default_rng`](parts/04-random/4.1-default-rng-the-generator.md) | Why two random APIs, and which one? | `working` |
| [4.2 The seed is part of the result](parts/04-random/4.2-the-seed-is-part-of-the-result.md) | When is a reported number not a result? | `production` |
| [4.3 Passing the generator](parts/04-random/4.3-passing-the-generator.md) | Why did all four workers produce the same data? | `production` |

### Section 5 — the module

| Part | What it answers | Level |
|---|---|---|
| [5.1 Typed on purpose](parts/05-the-module/5.1-reading-the-week-typed-on-purpose.md) | Where do the four decisions get made? | `production` |
| [5.2 The test that can go red](parts/05-the-module/5.2-the-test-that-can-go-red.md) | How do you know a test is wired to anything? | `production` |

---

## §3 Setup — run this

```bash
uv add numpy==2.5.2
uv run python -c "import numpy as np; print(np.__version__)"
```

Expect `2.5.2`. Confirm `pyproject.toml` gained the exact pin and that `uv.lock` changed — both are
committed (Principle 4). If the live index has moved past 2.5.2, **stop**: log the drift in
`docs/CHANGELOG_PLAN_DS.md` and regenerate `docs/PINS_DS.md` with
`uv run python scripts/check_pins.py --markdown` before continuing (Principle 14).

```bash
./m scaffold 20
mkdir -p data/steps
printf '8213\n10442\n6180\n-\n12007\n9631\n7204\n' > data/steps/week-01.txt
touch src/setu/steps.py tests/test_steps.py
cat data/steps/week-01.txt
```

Seven lines, with a dash on the fourth. That dash is Thursday, and what you decide it means is most
of today's build.

---

## §4 Build brief

**One new module and one test file.** `src/setu/steps.py` reads a column of daily counts into a
typed array and describes it; `tests/test_steps.py` asserts every decision it makes. Add `steps` to
`LAYERS` in `src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**`src/setu/steps.py`** — [5.1](parts/05-the-module/5.1-reading-the-week-typed-on-purpose.md)
explains every line.

```python
"""Read a column of daily step counts into a typed array, and describe it."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# TODO(me): choose the storage dtype and write the reasoning beside it as a
# comment (part 2.2). State the largest daily count you consider possible, then
# check it against np.iinfo. int16 is tempting and wrong; say why.
STEP_DTYPE = np.dtype(np.int64)
MISSING = "-"


@dataclass(frozen=True, slots=True)
class Summary:
    """What one run of counts looks like, in plain Python types."""

    days: int
    recorded: int
    # TODO(me): total, mean, best, nbytes. Every field is a plain int or float,
    # never np.int64 (part 5.1). Say in a comment what breaks if you leave the
    # NumPy scalars in.


def load_counts(rows: list[str]) -> np.ndarray:
    """Parse one column of daily step counts. A '-' means the day was not recorded."""
    # TODO(me): turn MISSING into np.nan and everything else into text, then
    # build the array with an EXPLICIT dtype (part 2.1). Say in a comment what
    # the array's dtype becomes without the explicit one, and why that is worse
    # than an error.
    # TODO(me): reject a negative count. A dtype constrains the type, never the
    # domain - name the exception class and say why it is that one (Day 18, 2.2).
    raise NotImplementedError


def to_whole(values: np.ndarray, *, fill: int = -1) -> np.ndarray:
    """Narrow to the project dtype, with a visible sentinel where a day is missing."""
    # TODO(me): four steps, in this order, and the order is the point (part 2.4):
    #   1. range-check the real values against np.iinfo(STEP_DTYPE)
    #   2. allocate with np.full and the sentinel, never np.empty (part 3.2)
    #   3. round with np.rint before casting, not after
    #   4. write only the recorded positions
    # Then say in a comment why -1 is a usable sentinel here and would not be
    # for a temperature column.
    raise NotImplementedError


def summarise(values: np.ndarray) -> Summary:
    """Describe a run of counts without letting one missing day poison the answer."""
    # TODO(me): refuse an integer array, and say in the comment what the caller
    # has already lost if they have one (part 2.3).
    # TODO(me): count the recorded days and report that number in the Summary.
    # This is the field that tells a reader whether the mean is over seven days
    # or six.
    # TODO(me): use the nan-aware reductions. Say in a comment which decision
    # you just made on the reader's behalf, and what the other choice would be.
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

**`tests/test_steps.py`** — [5.2](parts/05-the-module/5.2-the-test-that-can-go-red.md) explains
every assertion, and the discipline that makes them worth having.

```python
"""Day 20's eval: every claim the module makes, asserted."""

from __future__ import annotations

import numpy as np
import pytest

from setu.steps import STEP_DTYPE, Summary, load_counts, summarise, to_whole

WEEK = ["8213", "10442", "6180", "-", "12007", "9631", "7204"]


def test_a_missing_day_becomes_nan_not_zero():
    # TODO(me): assert the dtype is float64, that position 3 is nan, and that
    # exactly six of seven are recorded. Use np.isnan, never == np.nan, and say
    # in a comment why (part 2.3).
    raise NotImplementedError


def test_the_naive_mean_is_nan_and_the_nan_mean_is_not():
    # TODO(me): assert values.mean() is nan. This looks like testing NumPy and
    # is really testing that you did not fill the hole in.
    # TODO(me): assert np.nanmean with np.testing.assert_allclose and a stated
    # rtol. Say in a comment why == would fail on somebody else's machine.
    raise NotImplementedError


def test_summary_reports_how_many_days_were_real():
    # TODO(me): assert (days, recorded) as one tuple so a failure shows which
    # half moved. Then total, best, and the mean with a tolerance.
    raise NotImplementedError


def test_summary_returns_plain_python_types():
    # TODO(me): type(x) is int, not isinstance. Say in a comment what isinstance
    # would let through and where that would fail.
    raise NotImplementedError


def test_narrowing_rounds_and_marks_the_hole():
    # TODO(me): pick an input where rint and truncation disagree, and assert
    # the sentinel survived at the missing position.
    raise NotImplementedError


def test_bad_input_is_refused():
    # TODO(me): parametrize three cases - a word, a negative, an empty string -
    # and give every pytest.raises a match=. Say in a comment what a bare
    # pytest.raises(ValueError) would let past (Day 18, 4.4).
    raise NotImplementedError


def test_an_integer_array_is_refused():
    # TODO(me): TypeError, with match=. Say why TypeError and not ValueError.
    raise NotImplementedError


def test_a_value_too_large_for_the_dtype_is_refused():
    # TODO(me): assert on YOUR message, not NumPy's - the check exists so that
    # NumPy's silent wrap never happens (part 2.2).
    raise NotImplementedError


def test_the_array_is_smaller_than_the_list():
    # TODO(me): a SEEDED generator (part 4.2), 100_000 values, and assert a
    # RATIO rather than an exact byte count. Say in a comment why the exact
    # count is the wrong assertion.
    raise NotImplementedError
```

**Then break it on purpose.** Change the `np.nan` in `load_counts` to `0`, run the suite, count how
many tests go red, and read the messages before you put the line back. A test you have never seen
fail is not yet a test (Principle 7).

```bash
uv run python -m pytest -q tests/test_steps.py
./m depth 20
./m check
```

---

## §6 Request budget

| Item | Count | Cost |
|---|---|---|
| Model calls | 0 | £0 |
| Network requests | 1 — `uv add numpy==2.5.2` from PyPI | £0 |
| Live API keys used | none | £0 |
| Data downloaded | none; the seven-line file is written by hand in §3 | £0 |

**Zero model calls today** (Principle 5). Everything on this day runs offline once NumPy is
installed, including every test. Nothing here consumes a free-tier allowance.

---

## §7 Traps

- **`np.zeros(4, 7)` instead of `np.zeros((4, 7))`.** The shape is one argument. The error says
  `Cannot interpret '7' as a data type` and never mentions shape
  ([3.2](parts/03-creating/3.2-zeros-ones-full-and-empty.md)).
- **`arr == np.nan` finds nothing** and returns an all-`False` mask rather than an error, so a
  "drop the missing rows" step silently drops none
  ([2.3](parts/02-dtypes/2.3-floats-nan-and-precision.md)).
- **`arr * 4` on an `int16` array wraps to negative numbers with no warning at all.** Reductions
  promote and elementwise operations do not
  ([2.2](parts/02-dtypes/2.2-integers-and-the-silent-wrap.md)).
- **`astype(np.int64)` truncates.** `7.832` becomes `7`, not `8`, and over a million rows that is a
  systematic downward bias ([2.4](parts/02-dtypes/2.4-astype-and-the-copy.md)).
- **A printed array is not the stored values.** `np.arange(0, 0.7, 0.1)` displays a tidy
  `[0. 0.1 ... 0.6]` and its last element is `0.6000000000000001`, so `== 0.6` is `False`
  ([3.3](parts/03-creating/3.3-arange-and-the-float-step.md)).
- **`np.empty` looks safe** because a fresh process usually hands back zeroed pages. Allocate and
  free something first and the garbage appears ([3.2](parts/03-creating/3.2-zeros-ones-full-and-empty.md)).
- **Half the NumPy code on the internet does not run here.** `np.float_`, `np.NaN`, `np.in1d` and
  about a hundred others were removed in 2.0 ([2.6](parts/02-dtypes/2.6-the-names-that-were-removed.md)).
- **`np.array(x, copy=False)` now raises** rather than meaning "avoid a copy if you can". Use
  `np.asarray(x)` ([3.1](parts/03-creating/3.1-np-array-and-what-it-infers.md)).
- **`len(arr)` gives the first axis, not the element count.** Use `.size`
  ([1.2](parts/01-the-block/1.2-shape-dtype-and-the-rest.md)).
- **Converting a list to an array to do one operation is slower than not bothering.** The conversion
  costs more than the sum it enables ([1.4](parts/01-the-block/1.4-a-million-floats-measured.md)).

---

## §8 Verify before you code

Every one of these was fetched on 2026-09-02 and returned `200`. Read the first three before writing
any code; open the rest when the part points you at them.

- `ndarray`, its attributes and its memory model —
  <https://numpy.org/doc/stable/reference/arrays.ndarray.html>
- Data type objects, and the full list of dtypes —
  <https://numpy.org/doc/stable/reference/arrays.dtypes.html>
- Array creation routines, all of them in one table —
  <https://numpy.org/doc/stable/reference/routines.array-creation.html>
- Scalars, and why `week[0]` is a `np.int64` —
  <https://numpy.org/doc/stable/reference/arrays.scalars.html>
- The `Generator` API, every distribution method —
  <https://numpy.org/doc/stable/reference/random/generator.html>
- The NumPy 2.0 migration guide, including the removed names —
  <https://numpy.org/doc/stable/numpy_2_0_migration_guide.html>
- *NEP 50 — Promotion rules for Python scalars* (2021) —
  <https://numpy.org/neps/nep-0050-scalar-promotion.html>
- *NEP 19 — Random number generator policy* (2018) —
  <https://numpy.org/neps/nep-0019-rng-policy.html>
- `np.arange`, and its own advice to prefer `linspace` for decimal steps —
  <https://numpy.org/doc/stable/reference/generated/numpy.arange.html>

The live pin, checked the same way:

```bash
uv run python scripts/check_pins.py | grep -i numpy
```

---

## §9 Say it in an interview

"A NumPy array is one contiguous block of memory plus a small description — a shape, a dtype, and
one stride per axis saying how many bytes to jump. A Python list of numbers is a row of pointers to
separate integer objects, so it costs about four and a half times the memory for a million values,
and any operation over it pays a bytecode dispatch and an unbox per element. On my machine, summing
a million integers is roughly a hundred times faster as an array than as a hand-written loop, and
about fourteen times faster than the built-in `sum` — I quote both, because which one you compare
against changes the number by an order of magnitude. The price of the block is that every cell is
the same width, which is the dtype, and that is where the interesting failures live: integer
arithmetic wraps silently, a float-to-integer cast truncates rather than rounds, and one string in a
list turns the whole array into text with no warning. So I state the dtype at every boundary and let
bad data fail there. On NumPy 2 specifically, two things changed that break old code: about a
hundred duplicate aliases were removed, and a plain Python number in an expression now adopts the
array's dtype instead of promoting it — so a `float32` pipeline stays `float32` rather than silently
doubling in memory. And anything random gets a `default_rng` generator with a written-down seed,
passed as a parameter rather than created inside, because otherwise parallel workers all produce
identical data and nobody notices."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m depth 20` passes, and `./m check` is
green — which means ruff, the lesson code blocks, the offline tests and the depth contract all
agree. Done is defined by understanding and by green checks, never by elapsed time (Principle 17).

The three questions to answer out loud before you call it finished:

1. Why can an array have only one dtype, and what does that restriction buy?
2. Give three different honest speedup numbers for the same array, and say what each is compared
   against.
3. Why does a function that takes a seed and builds its own generator return the same thing on every
   call?
