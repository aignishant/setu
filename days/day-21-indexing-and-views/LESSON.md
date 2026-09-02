---
day: 21
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 21 — Indexing, slicing, boolean masks — and the view trap"
ids: ["NP-03"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 23
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 21 — Indexing, slicing, boolean masks — and the view trap

**Phase 3 · NumPy · Module 3** · `NP-03` indexing, slicing, boolean and fancy indexing. The plan's
named example is the one the whole day turns on: **a slice is a view — write to it and the parent
changes.** Everything else today is a consequence of that sentence, including the two things nobody
warns you about: a small view keeps a large array alive, and `tally[positions] += 1` counts each
repeated position once.

> **Yesterday:** the `ndarray` itself — one block of memory, one dtype, and the creation functions
> that bring one into being.
> **Today:** getting things out of that block, and the fact that most ways of doing so do not copy
> anything at all.
> **Tomorrow:** broadcasting and reshaping — how arrays of different shapes are made to line up, and
> which of those operations are also views.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The month of step counts from yesterday is written out as a grid on squared paper: four rows, one per
week, seven boxes across, one per day.

Somebody wants to work on week two. They could copy the seven numbers onto a fresh strip of card, and
then they would have two pieces of paper — the grid, and a strip that happens to hold the same seven
numbers. Changing the strip would leave the grid alone.

Or they could take a sheet of cardboard, cut a window in it seven boxes wide, and lay it over the
second row. Now they are looking at week two. Nothing was copied. There is still one set of numbers
in the world, and the window is a way of looking at part of it.

The window is quicker to make, and it costs almost nothing to carry around. It also has two
properties that catch everybody out. If you write a number through the window, you have written on
the grid — there was never a second copy to write on. And as long as somebody is holding the window,
the whole grid has to be kept, because the window has nothing of its own to show.

NumPy hands you the window by default. Almost every way of taking part of an array gives you a way of
looking at the original rather than a copy of it, and nothing in what you get back says which one you
are holding.

Today is about knowing which one you have, choosing on purpose, and recognising the three bugs that
follow from not knowing: the function that changed its caller's data, the four hundred bytes that
held two hundred megabytes, and the tally that counted six visits as three.

---

## §2 The map

**What the section numbers mean today.** This is a `lab` day with one ID, so the split follows the
`lab` shape from the plan's Part 11.7 — mechanism, then behaviour, then edge case, then failure mode,
then production use. **1.x is the mechanism**: every way of naming positions inside the brackets.
**2.x is the behaviour** that makes NumPy different from every container you have met — the view.
**3.x and 4.x are the two selection styles** that break that rule by copying: by condition, and by
explicit position. **5.x is production**: the leak, the module, and the tests that assert what you
cannot see.

### Section 1 — one element, and a range of them

| Part | What it answers | Level |
|---|---|---|
| [1.1 `arr[3]` and the negative index](parts/01-one-element/1.1-index-and-the-negative-index.md) | What comes back, and why is it not a plain `int`? | `foundation` |
| [1.2 The comma a list cannot do](parts/01-one-element/1.2-the-comma-a-list-cannot-do.md) | How does one index name a position on every axis? | `foundation` |
| [1.3 A slice keeps its axis](parts/01-one-element/1.3-slicing-one-axis.md) | Why does `arr[1]` lose an axis and `arr[1:2]` keep it? | `foundation` |
| [1.4 A whole column](parts/01-one-element/1.4-a-whole-column.md) | How can values 56 bytes apart still be a view? | `working` |
| [1.5 The step and the reverse](parts/01-one-element/1.5-the-step-and-the-reverse.md) | Why does reversing an array cost nothing? | `working` |
| [1.6 `...` and `np.newaxis`](parts/01-one-element/1.6-ellipsis-and-newaxis.md) | How do you write an index that works for any number of axes? | `working` |

### Section 2 — the view trap

| Part | What it answers | Level |
|---|---|---|
| [2.1 A slice does not copy](parts/02-the-view-trap/2.1-a-slice-does-not-copy.md) | Why did the parent array change? | `working` |
| [2.2 `base`, `shares_memory`, flags](parts/02-the-view-trap/2.2-how-to-tell-base-and-shares-memory.md) | How do you tell a view from a copy? | `working` |
| [2.3 `.copy()` and when to pay](parts/02-the-view-trap/2.3-copy-and-when-to-pay.md) | When is a copy worth its cost? | `working` |
| [2.4 The function that changed its input](parts/02-the-view-trap/2.4-the-function-that-changed-its-input.md) | How do you write one that cannot? | `production` |

### Section 3 — boolean masks

| Part | What it answers | Level |
|---|---|---|
| [3.1 A comparison makes an array](parts/03-boolean-masks/3.1-a-comparison-makes-an-array.md) | What does `arr > 5` return, and what does it cost? | `foundation` |
| [3.2 Indexing with a mask](parts/03-boolean-masks/3.2-indexing-with-a-mask.md) | Why is the result flat, and why is it a copy? | `working` |
| [3.3 `&`, `\|`, `~` and why `and` raises](parts/03-boolean-masks/3.3-and-or-not-and-why-and-raises.md) | What is the "truth value is ambiguous" error? | `working` |
| [3.4 Assigning through a mask](parts/03-boolean-masks/3.4-assigning-through-a-mask.md) | Why does the same expression read and write differently? | `working` |
| [3.5 The mask that matched nothing](parts/03-boolean-masks/3.5-the-mask-that-matched-nothing.md) | What is the mean of no values? | `production` |

### Section 4 — fancy indexing

| Part | What it answers | Level |
|---|---|---|
| [4.1 A list of positions](parts/04-fancy-indexing/4.1-a-list-of-positions.md) | How do you select in an order of your own? | `working` |
| [4.2 Two index arrays](parts/04-fancy-indexing/4.2-two-index-arrays.md) | Pairs or a grid? | `working` |
| [4.3 Basic or advanced](parts/04-fancy-indexing/4.3-fancy-indexing-always-copies.md) | Which expressions give a view, and which copy? | `working` |
| [4.4 Repeated positions](parts/04-fancy-indexing/4.4-repeated-positions-and-the-lost-update.md) | Why did six visits count as three? | `production` |
| [4.5 Mixing a slice with a list](parts/04-fancy-indexing/4.5-mixing-a-slice-with-a-list.md) | Where did that axis go? | `production` |

### Section 5 — in anger

| Part | What it answers | Level |
|---|---|---|
| [5.1 The leak a view causes](parts/05-in-anger/5.1-the-leak-a-view-causes.md) | Why is memory growing when nothing is leaking? | `production` |
| [5.2 View or copy, on purpose](parts/05-in-anger/5.2-view-or-copy-on-purpose.md) | How do you put the decision in the interface? | `production` |
| [5.3 The test that can go red](parts/05-in-anger/5.3-the-test-that-can-go-red.md) | How do you assert a promise you cannot see? | `production` |

---

## §3 Setup — run this

NumPy was pinned yesterday. Confirm it rather than assuming it:

```bash
uv run python -c "import numpy as np; print(np.__version__)"
uv run python scripts/check_pins.py | grep -i numpy
```

Expect `2.5.2` and no drift. If the live index has moved, **stop**: log it in
`docs/CHANGELOG_PLAN_DS.md` and regenerate `docs/PINS_DS.md` before continuing (Principle 14). No new
package is added today.

```bash
./m scaffold 21
mkdir -p data/steps
printf '8213 10442 6180 -1 12007 9631 7204\n7788 9120 11345 8402 6733 14210 5096\n9004 8765 7621 10188 9950 8317 11002\n6540 12488 9873 7106 8899 10540 9218\n' > data/steps/month-01.txt
touch src/setu/select.py tests/test_select.py
cat data/steps/month-01.txt
```

Four lines of seven numbers, and a `-1` on the first line where yesterday's file had a dash. That
`-1` is the **sentinel**: the month is an integer array, integers have no `nan`, and `-1` is a step
count that cannot happen. [5.2](parts/05-in-anger/5.2-view-or-copy-on-purpose.md) is where that
choice is argued out, including what it costs.

---

## §4 Build brief

**One new module and one test file.** `src/setu/select.py` decides, for every function, whether the
caller gets a view or a copy, and says so in the name. Add `select` to `LAYERS` in
`src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**`src/setu/select.py`** — [5.2](parts/05-in-anger/5.2-view-or-copy-on-purpose.md) explains every
line.

```python
"""Select days out of a run of step counts, saying view or copy every time."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# TODO(me): choose the sentinel and write the reasoning beside it as a comment
# (part 5.2). State what makes a sentinel safe for THIS column, and name one
# column where the same value would be a real measurement.
MISSING = -1


@dataclass(frozen=True, slots=True)
class Selection:
    """What one filter kept, and what it rejected. Every count is a plain int."""

    values: np.ndarray
    kept: int
    # TODO(me): missing, out_of_range, and a total_seen property computed from
    # the three counts rather than stored. Say in a comment what a stored total
    # could disagree with.


def week(month: np.ndarray, index: int) -> np.ndarray:
    """One week, as a read-only view. Cheap, and must not outlive `month`."""
    # TODO(me): shape check first, with the received shape in the message.
    # TODO(me): return a view that CANNOT be written to. One line of it is
    # subtle - .view() before touching the flags - and part 5.2's second
    # failure shows what happens without it. Say in a comment what the flag
    # protects: the view, the month, or both.
    raise NotImplementedError


def week_copy(month: np.ndarray, index: int) -> np.ndarray:
    """One week, detached. Costs a copy, and is safe to keep and to write to."""
    # TODO(me): two functions rather than one with copy=True. Write the reason
    # in a comment, in one sentence, aimed at the caller.
    raise NotImplementedError


def usable(counts: np.ndarray, *, floor: int = 100, ceiling: int = 60_000) -> np.ndarray:
    """Mark the days that can be used: recorded, and inside the plausible range."""
    # TODO(me): three named conditions, one per line, combined with & (part 3.3).
    # Return the MASK, not the values, and say in a comment what a mask can do
    # that a list of values cannot.
    raise NotImplementedError


def select_usable(counts: np.ndarray, *, floor: int = 100, ceiling: int = 60_000) -> Selection:
    """Gather the usable days, and count what each rule rejected."""
    # TODO(me): count with np.count_nonzero rather than len(counts[mask]), and
    # say in a comment what the second one allocates.
    # TODO(me): the three categories must PARTITION the input - every day
    # counted once, no day counted twice. Write the expression for
    # out_of_range that makes that true, and say why the obvious one is wrong.
    raise NotImplementedError


def fill_missing(counts: np.ndarray, *, out: np.ndarray | None = None) -> np.ndarray:
    """Replace MISSING days with the mean of the usable ones, rounded to whole steps."""
    # TODO(me): guard the empty case BEFORE computing the mean (part 3.5), and
    # say in a comment what the unguarded version writes into an integer array.
    # TODO(me): round before casting, not after (Day 20, 2.4). Say what the
    # other order costs over a million rows.
    # TODO(me): the caller's array is untouched unless they pass out= by name.
    raise NotImplementedError


def tally_visits(positions: np.ndarray, members: int) -> np.ndarray:
    """Count visits per member. Repeats in `positions` are the whole point."""
    # TODO(me): range-check the positions, and say in a comment what
    # np.bincount does with an out-of-range one that minlength cannot fix.
    # TODO(me): counts[positions] += 1 is wrong here (part 4.4). Write the
    # right one, and put the WRONG one in a comment with the number it gives
    # for [0, 0, 0, 3, 3, 6].
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

**`tests/test_select.py`** — [5.3](parts/05-in-anger/5.3-the-test-that-can-go-red.md) explains every
assertion, and the discipline that makes them worth having.

```python
"""Day 21's eval: every promise the selection module makes, asserted."""

from __future__ import annotations

import numpy as np
import pytest

from setu.select import (
    MISSING,
    fill_missing,
    select_usable,
    tally_visits,
    usable,
    week,
    week_copy,
)

MONTH = np.array(
    [
        [8213, 10442, 6180, MISSING, 12007, 9631, 7204],
        [7788, 9120, 11345, 8402, 6733, 14210, 5096],
        [9004, 8765, 7621, 10188, 9950, 8317, 11002],
        [6540, 12488, 9873, 7106, 8899, 10540, 9218],
    ]
)


@pytest.fixture
def month() -> np.ndarray:
    # TODO(me): return a fresh copy per test, and say in a comment which of the
    # tests below would corrupt the others without it.
    raise NotImplementedError


def test_week_is_a_view_and_cannot_be_written_to(month):
    # TODO(me): assert np.shares_memory, assert the writeable flag with `is
    # False`, and assert the ValueError with match=. Say in a comment why the
    # flag and the raise are both worth asserting.
    raise NotImplementedError


def test_week_copy_is_detached(month):
    # TODO(me): shares_memory AND base is None - two different questions
    # (part 4.3). Then write to the copy and assert the month did not move.
    raise NotImplementedError


def test_the_three_categories_cover_every_day(month):
    # TODO(me): assert total_seen == size, then assert the three counts as ONE
    # tuple. Say in a comment why three separate asserts are worse.
    raise NotImplementedError


def test_out_of_range_is_counted_separately():
    # TODO(me): build a four-value array with one below the floor, one fine,
    # one above the ceiling and one missing. Do not reuse the month.
    raise NotImplementedError


def test_fill_missing_leaves_the_caller_alone(month):
    # TODO(me): `before` must be a .copy(). Say in a comment what the test
    # asserts if you forget, and why it can then never fail.
    raise NotImplementedError


def test_fill_missing_with_out_writes_in_place(month):
    # TODO(me): assert `returned is row`, not ==. Say why.
    raise NotImplementedError


def test_fill_missing_refuses_when_nothing_is_usable():
    # TODO(me): pytest.raises with match= on YOUR message, not NumPy's.
    raise NotImplementedError


def test_tally_counts_repeats():
    # TODO(me): assert the SUM equals the number of visits, then the exact
    # counts. Say in a comment which of the two catches part 4.4's bug.
    raise NotImplementedError


def test_tally_refuses_a_position_outside_the_roll():
    # TODO(me): match= on your own message.
    raise NotImplementedError


def test_usable_returns_a_mask_not_values(month):
    # TODO(me): assert the dtype is bool and the shape matches the input.
    raise NotImplementedError
```

**Then break it on purpose.** Delete `view.flags.writeable = False` from `week`, run the suite, read
the failure, and put it back. Then replace `np.bincount` with `counts[positions] += 1` and count how
many tests go red. A test you have never seen fail is not yet a test (Principle 7).

```bash
uv run python -m pytest -q tests/test_select.py
./m depth 21
./m check
```

---

## §6 Request budget

| Item | Count | Cost |
|---|---|---|
| Model calls | 0 | £0 |
| Network requests | 0 — NumPy was installed yesterday | £0 |
| Live API keys used | none | £0 |
| Data downloaded | none; the four-line file is written by hand in §3 | £0 |

**Zero model calls and zero network today** (Principle 5). Everything on this day, including the
memory measurements, runs offline.

---

## §7 Traps

- **A slice is a view, so a helper that "cleans" one week writes into the month.** No error, no
  warning ([2.1](parts/02-the-view-trap/2.1-a-slice-does-not-copy.md)).
- **`arr[mask][0] = 0` changes nothing.** Two pairs of brackets read, one pair writes
  ([3.2](parts/03-boolean-masks/3.2-indexing-with-a-mask.md)).
- **`mask1 and mask2` raises `The truth value of an array with more than one element is ambiguous`** —
  and so do `5000 < week < 11000` and `week > 5000 & week < 11000`, for three different reasons
  ([3.3](parts/03-boolean-masks/3.3-and-or-not-and-why-and-raises.md)).
- **`arr == np.nan` is all `False`.** A "drop the missing days" filter built that way drops none
  ([3.1](parts/03-boolean-masks/3.1-a-comparison-makes-an-array.md)).
- **The mean of an empty selection is `nan` with a warning; the max of one raises.** Same empty array,
  two different behaviours ([3.5](parts/03-boolean-masks/3.5-the-mask-that-matched-nothing.md)).
- **`tally[positions] += 1` counts each repeated position once.** Six visits become three, and the
  result looks like a plausible tally ([4.4](parts/04-fancy-indexing/4.4-repeated-positions-and-the-lost-update.md)).
- **A mask that has been through a file comes back as integers**, and integers in brackets are
  positions, not a condition ([3.2](parts/03-boolean-masks/3.2-indexing-with-a-mask.md)).
- **`month[(1, 2)]` is one element and `month[[1, 2]]` is two rows.** Round brackets against square
  ([4.1](parts/04-fancy-indexing/4.1-a-list-of-positions.md)).
- **Two index arrays separated by a slice put the gathered axis first**, so the result is transposed
  relative to what you expected ([4.5](parts/04-fancy-indexing/4.5-mixing-a-slice-with-a-list.md)).
- **Returning `data[:10]` from a function keeps the whole array alive**, and every observable property
  of those ten values says "small" ([5.1](parts/05-in-anger/5.1-the-leak-a-view-causes.md)).
- **`arr.base is None` is not a copy test.** A mixed expression produces a copy that still has a base;
  `np.shares_memory` is the question that answers the question
  ([4.3](parts/04-fancy-indexing/4.3-fancy-indexing-always-copies.md)).
- **`month[1].flags.writeable = False` protects nothing.** It sets the flag on a temporary view that
  is discarded on the same line ([5.2](parts/05-in-anger/5.2-view-or-copy-on-purpose.md)).

---

## §8 Verify before you code

Every one of these was fetched on 2026-09-02 and returned `200`. Read the first two before writing
any code; open the rest when a part points you at them.

- Indexing on `ndarrays`, basic and advanced, in one page —
  <https://numpy.org/doc/stable/user/basics.indexing.html>
- Copies and views, and the rule that decides which you get —
  <https://numpy.org/doc/stable/user/basics.copies.html>
- Advanced indexing, including the axis-ordering rule for separated index arrays —
  <https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing>
- `np.shares_memory`, and what `max_work` is for —
  <https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html>
- `ndarray.base` — <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html>
- `np.ix_`, the grid helper — <https://numpy.org/doc/stable/reference/generated/numpy.ix_.html>
- `np.take_along_axis` — <https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html>
- `ufunc.at`, the unbuffered update —
  <https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html>
- `np.bincount` — <https://numpy.org/doc/stable/reference/generated/numpy.bincount.html>
- `np.copyto`, and its `where=` —
  <https://numpy.org/doc/stable/reference/generated/numpy.copyto.html>
- `np.flatnonzero` and `np.count_nonzero` —
  <https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html> ·
  <https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html>
- `tracemalloc`, used for the memory measurement in 5.1 —
  <https://docs.python.org/3/library/tracemalloc.html>

---

## §9 Say it in an interview

"NumPy has two families of indexing and the difference decides everything. Basic indexing — whole
numbers, slices, `...`, `newaxis` — returns a view: a new array object pointing at the same memory,
because the selection can be described by a shape and a set of strides. Advanced indexing — a boolean
mask or a list of positions — returns a copy, because arbitrary positions cannot be described by a
stride, so the values have to be gathered. That single rule explains the behaviour people get caught
by. A function that writes to a slice it was handed is writing into the caller's array, so I write
either a function that copies and returns a new array, or one that writes and returns `None`, and the
name says which. `arr[mask][0] = 0` silently does nothing because the read makes a temporary, while
`arr[mask] = 0` writes through. Masks are combined with `&` and `|` and never with `and` and `or`,
which raise, because an array of seven elements has no single truth value. On the memory side, a view
keeps its parent alive, so caching ten values sliced out of a 40 MB array keeps all 40 MB — that is
the growth that looks like a leak and isn't, and the fix is a `.copy()` at the boundary where the
small thing starts outliving the big one. The one that costs people real money is `counts[ids] += 1`
with repeated ids: it is a gather, an add, and a scatter, so every read sees the original value and
each position is only incremented once. `np.add.at` or `np.bincount` is the correct version, and the
test that catches it is asserting that the total equals the number of updates."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m depth 21` passes, and `./m check` is
green. Done is defined by understanding and by green checks, never by elapsed time (Principle 17).

The three questions to answer out loud before you call it finished:

1. Which indexing expressions give a view and which give a copy, and what is the one-sentence reason?
2. Your function is handed `matrix[0]` and writes to it. Name every array that changes, and the two
   ways to stop that happening.
3. A cache of ten-element results is using two hundred megabytes. What is happening, which attribute
   proves it, and what is the fix?
