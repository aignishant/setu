---
day: 22
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 22 — Broadcasting, and the shape operations that cost nothing"
ids: ["NP-04", "NP-05"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 22
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 22 — Broadcasting, and the shape operations that cost nothing

**Phase 3 · NumPy · Module 3** · `NP-04` broadcasting — the rule that makes "add a vector to a matrix"
legal, with the plan's named example of **mean-centring 60 000 rows with no loop**; `NP-05` array
manipulation — reshape, stack, split and transpose, with the plan's named example of **reshaping a
flat image buffer to `(28, 28)`**, the move you will make again on Day 130.

> **Yesterday:** getting values out of an array, and the fact that most ways of doing so give you a
> view rather than a copy.
> **Today:** making arrays of different shapes work together, and rearranging one array's shape — and
> almost every operation here is a view too, for the same reason.
> **Tomorrow:** the operations that actually compute — universal functions, statistics, sorting and
> the `argsort` top-k that is the retrieval primitive.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody keeps the month of step counts as a grid on squared paper: four rows, one per week, seven
boxes across, one per day.

They want to know which days were unusual. Not "which were big" — that they can see — but unusual for
that day of the week, because Saturdays are always bigger than Wednesdays and comparing them straight
tells you nothing.

So they work out a typical Monday, a typical Tuesday, and so on: seven numbers, written on a strip of
card. Then they lay the strip across the grid and, row by row, subtract. Four rows, one strip, and the
strip is written once and used four times.

Nobody would copy the strip out four times first. It is the same strip; it is simply being read again
for each row.

That is broadcasting, and it is the first half of today. NumPy does exactly what the person with the
card does: it reads the seven numbers four times rather than making four copies of them. The whole
skill is knowing when the shapes will line up, and what happens when they do not.

The second half is even less work. The grid arrived as a text file of twenty-eight numbers in a
column. Turning that column into a grid did not move a single number — somebody cut a window seven
boxes wide and laid it over the list. Turning the grid on its side to see all the Mondays together
moved nothing either. Nearly every way of rearranging an array is a new way of reading the same
memory, and the two places where that stops being true — joining arrays together, and asking for a
layout no stride can describe — are the two places where today's real costs live.

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the split is one group of sections per ID plus a
synthesis. **1.x is `NP-04`**, broadcasting: the rule, what it does not copy, and how it eats memory
when both sides stretch. **2.x, 3.x and 4.x are `NP-05`**, arranged in the order the operations touch
data — 2.x reshapes one array, 3.x reorders its axes, and 4.x joins and splits several. **5.x is the
synthesis**: the module where both IDs meet, and the tests that catch the axis bugs neither ID can
catch alone.

### Section 1 — broadcasting

| Part | What it answers | Level |
|---|---|---|
| [1.1 One number against twenty-eight](parts/01-broadcasting/1.1-adding-one-number-to-every-day.md) | What does `month + 500` do, and what does it cost? | `foundation` |
| [1.2 The rule in three lines](parts/01-broadcasting/1.2-the-rule-in-three-lines.md) | Which shapes work together, and which do not? | `foundation` |
| [1.3 A row against a table](parts/01-broadcasting/1.3-a-row-against-a-table.md) | How do you mean-centre 60 000 rows with no loop? | `working` |
| [1.4 `keepdims` and the column](parts/01-broadcasting/1.4-keepdims-and-the-column.md) | Why does the per-row version refuse? | `working` |
| [1.5 A stride of zero](parts/01-broadcasting/1.5-no-data-is-copied.md) | Is the stretched array really there? | `working` |
| [1.6 Reading the error](parts/01-broadcasting/1.6-reading-the-broadcast-error.md) | Which of the six shape messages is this? | `working` |
| [1.7 The broadcast that ate the memory](parts/01-broadcasting/1.7-the-broadcast-that-ate-the-memory.md) | Why did the process die? | `production` |

### Section 2 — reshape

| Part | What it answers | Level |
|---|---|---|
| [2.1 Same block, new shape](parts/02-reshape/2.1-same-block-new-shape.md) | How much does reshaping move? | `foundation` |
| [2.2 `-1` and the division](parts/02-reshape/2.2-minus-one.md) | Which size do you state, and which do you derive? | `foundation` |
| [2.3 The `order` argument](parts/02-reshape/2.3-the-order-argument.md) | Why did the image come out sideways? | `working` |
| [2.4 `ravel` and `flatten`](parts/02-reshape/2.4-ravel-and-flatten.md) | Two calls, identical values — what differs? | `working` |
| [2.5 When reshape must copy](parts/02-reshape/2.5-when-reshape-must-copy.md) | Where did that full-array copy come from? | `production` |

### Section 3 — transpose

| Part | What it answers | Level |
|---|---|---|
| [3.1 `.T`, the axes swapped](parts/03-transpose/3.1-t-the-axes-swapped.md) | What does a transpose actually change? | `foundation` |
| [3.2 `transpose`, `swapaxes`, `moveaxis`](parts/03-transpose/3.2-transpose-and-swapaxes.md) | Which two axes did you mean? | `working` |
| [3.3 Contiguity](parts/03-transpose/3.3-contiguity-and-the-speed-you-lose.md) | Which operations pay for a transpose? | `production` |

### Section 4 — joining and splitting

| Part | What it answers | Level |
|---|---|---|
| [4.1 `concatenate`](parts/04-joining-and-splitting/4.1-concatenate.md) | Why is this the one operation that always copies? | `working` |
| [4.2 `stack` against `concatenate`](parts/04-joining-and-splitting/4.2-stack-versus-concatenate.md) | A new axis, or a longer one? | `working` |
| [4.3 `split` and the uneven piece](parts/04-joining-and-splitting/4.3-split-and-the-uneven-last-piece.md) | What happens when it does not divide? | `working` |
| [4.4 `np.newaxis` and `expand_dims`](parts/04-joining-and-splitting/4.4-newaxis-and-expand-dims.md) | How do you make a row into a column? | `working` |
| [4.5 Growing an array in a loop](parts/04-joining-and-splitting/4.5-growing-an-array-in-a-loop.md) | Why did the job never finish? | `production` |

### Section 5 — the module

| Part | What it answers | Level |
|---|---|---|
| [5.1 Mean-centring the month](parts/05-the-module/5.1-mean-centring-the-month.md) | Where does the leak get designed out? | `production` |
| [5.2 The test that can go red](parts/05-the-module/5.2-the-test-that-can-go-red.md) | How do you test an axis? | `production` |

---

## §3 Setup — run this

NumPy was pinned on Day 20. Confirm rather than assume:

```bash
uv run python -c "import numpy as np; print(np.__version__)"
uv run python scripts/check_pins.py | grep -i numpy
```

Expect `2.5.2` and no drift. If the live index has moved, **stop**: log it in
`docs/CHANGELOG_PLAN_DS.md` and regenerate `docs/PINS_DS.md` before continuing (Principle 14). No new
package is added today.

```bash
./m scaffold 22
mkdir -p data/steps
printf '8213\n10442\n6180\n9000\n12007\n9631\n7204\n7788\n9120\n11345\n8402\n6733\n14210\n5096\n9004\n8765\n7621\n10188\n9950\n8317\n11002\n6540\n12488\n9873\n7106\n8899\n10540\n9218\n' > data/steps/month-flat.txt
touch src/setu/shape.py tests/test_shape.py
wc -l data/steps/month-flat.txt
```

Twenty-eight lines, one number each, and nothing in the file saying where a week ends. Reading it as
weeks is the first thing the module does, and it costs nothing
([2.1](parts/02-reshape/2.1-same-block-new-shape.md)).

Note that Thursday of week one is `9000` here, where Days 20 and 21 had a hole. **A day that was not
recorded cannot be averaged**, and today is about the arithmetic rather than about missing data, so the
gap is filled before the arithmetic starts. Filling it is Day 21's job
([Day 21, 3.4](../day-21-indexing-and-views/parts/03-boolean-masks/3.4-assigning-through-a-mask.md)).

---

## §4 Build brief

**One new module and one test file.** `src/setu/shape.py` reads the flat file as weeks and centres it
two ways, one of which must not leak. Add `shape` to `LAYERS` in `src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**`src/setu/shape.py`** — [5.1](parts/05-the-module/5.1-mean-centring-the-month.md) explains every
line.

```python
"""Read a flat run of daily counts as weeks, and centre it without leaking."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

DAYS_PER_WEEK = 7


def as_weeks(counts: np.ndarray) -> np.ndarray:
    """Read a flat run of daily counts as (weeks, 7). Returns a VIEW of ``counts``."""
    # TODO(me): shape check first, then the divisibility check. The message must say
    # how many counts are LEFT OVER, not just that it failed - say in a comment what
    # NumPy's own message would have been and why yours is better (part 2.2).
    # TODO(me): reshape with -1 on the axis that varies. Say in a comment which of the
    # two numbers is a fact about weeks and which is a fact about this file.
    # TODO(me): the docstring says VIEW. Prove it to yourself with np.shares_memory
    # before you believe it.
    raise NotImplementedError


def centre_within_week(weeks: np.ndarray) -> np.ndarray:
    """Subtract each week's own mean from its days. Returns a new array."""
    # TODO(me): one line, and it needs keepdims=True (part 1.4). Write the version
    # WITHOUT keepdims in a comment, run it on a (4, 7) array and on a (7, 7) one, and
    # record what each does. That difference is the whole part.
    raise NotImplementedError


@dataclass(frozen=True, slots=True)
class DayProfile:
    """The per-day-of-week means learned from one set of weeks."""

    means: np.ndarray

    @classmethod
    def fit(cls, training_weeks: np.ndarray) -> "DayProfile":
        """Learn one mean per day of the week, from these weeks only."""
        # TODO(me): shape check, then refuse fewer than two weeks - say in a comment
        # what one week would produce and why it looks like it worked.
        # TODO(me): which axis gives one mean per DAY? Write the shape you expect in a
        # comment before you run it (part 1.3).
        # TODO(me): nanmean, not mean. Say what one missing day does to the other choice.
        raise NotImplementedError

    def apply(self, weeks: np.ndarray) -> np.ndarray:
        """Subtract the learned per-day means. The input is never modified."""
        # TODO(me): check the width against the LEARNED width, not against
        # DAYS_PER_WEEK, and say in a comment why that is the better check.
        # TODO(me): one line. Say in a comment why this needs no keepdims and
        # centre_within_week does.
        raise NotImplementedError


def stack_months(months: list[np.ndarray]) -> np.ndarray:
    """Join several (weeks, 7) blocks into one table, with a single allocation."""
    # TODO(me): drop empty blocks, then return the RIGHT SHAPE for the empty case
    # rather than raising (part 4.1). Say in a comment what a caller does with it.
    # TODO(me): check every block before joining any, so the message can name which
    # one is wrong.
    # TODO(me): exactly one np.concatenate, outside any loop. Put the quadratic version
    # in a comment with the word that describes its cost (part 4.5).
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

**`tests/test_shape.py`** — [5.2](parts/05-the-module/5.2-the-test-that-can-go-red.md) explains every
assertion, and why a shape assertion is not enough today.

```python
"""Day 22's eval: every shape promise the module makes, asserted."""

from __future__ import annotations

import numpy as np
import pytest

from setu.shape import (
    DAYS_PER_WEEK,
    DayProfile,
    as_weeks,
    centre_within_week,
    stack_months,
)

# TODO(me): a flat run of 28 float64 values. It must reshape to (4, 7) and NOT to a
# square - say in a comment what a square fixture would fail to catch.
FLAT = np.arange(28, dtype=np.float64) * 100.0


@pytest.fixture
def flat() -> np.ndarray:
    # TODO(me): a fresh copy per test. Name the test below that would corrupt the
    # others without it.
    raise NotImplementedError


def test_as_weeks_is_a_view(flat):
    # TODO(me): assert the shape, assert np.shares_memory, then write through the
    # result and assert the flat array moved. Two ways of asserting one promise.
    raise NotImplementedError


def test_as_weeks_refuses_a_partial_week():
    # TODO(me): pytest.raises with match= on YOUR message.
    raise NotImplementedError


def test_as_weeks_works_for_any_number_of_weeks():
    # TODO(me): 1, 4 and 52 weeks. This is the -1 promise, asserted.
    raise NotImplementedError


def test_centring_within_a_week_zeroes_the_row_means(flat):
    # TODO(me): np.testing.assert_allclose against 0.0 with an atol=, not ==. Say in a
    # comment why the default relative tolerance is useless when the target is zero.
    raise NotImplementedError


def test_centring_within_a_week_leaves_the_input_alone(flat):
    # TODO(me): `before` must be a .copy(). Say what it asserts if you forget.
    raise NotImplementedError


def test_centring_uses_the_row_not_the_column():
    # TODO(me): build a fixture where one row is constant and one varies. Assert the
    # constant row centres to zero AND the varying one does not. Say in a comment what
    # a function that returned all zeros would do to a test with only the first half.
    raise NotImplementedError


def test_profile_learns_one_mean_per_day(flat):
    # TODO(me): the shape assertion that does carry meaning today. Say why this one
    # does and the ones above do not.
    raise NotImplementedError


def test_profile_ignores_the_weeks_it_was_not_fitted_on(flat):
    # TODO(me): fit on three weeks and on four, and assert the means DIFFER. Say in a
    # comment what it would mean if they did not.
    raise NotImplementedError


def test_apply_does_not_change_the_profile_or_the_input(flat):
    # TODO(me): three assertions, one promise. Include np.shares_memory on the result.
    raise NotImplementedError


def test_profile_refuses_one_week():
    # TODO(me): match= on your message.
    raise NotImplementedError


def test_apply_refuses_the_wrong_width(flat):
    # TODO(me): the pattern needs a raw string and escaped brackets. Try it without
    # them first, and record what pytest says.
    raise NotImplementedError


def test_profile_ignores_missing_days():
    # TODO(me): one np.nan in the training weeks, and the means must still be numbers.
    raise NotImplementedError


def test_stack_months_joins_and_keeps_the_width(flat):
    # TODO(me): assert the shape AND that the result shares no memory with the inputs.
    raise NotImplementedError


def test_stack_months_of_nothing_has_the_right_shape():
    # TODO(me): the empty result must be joinable again. Assert that too.
    raise NotImplementedError


def test_stack_months_names_the_bad_block(flat):
    # TODO(me): match= on the block's position, not just on the exception type.
    raise NotImplementedError
```

**Then break it on purpose.** Change `keepdims=True` in `centre_within_week` to a mean along `axis=0`,
run the suite, and read both failures. Put it back, then change the fixture to `(7, 7)` and break it
again — this time count how many tests still pass. A test you have never seen fail is not yet a test
(Principle 7).

```bash
uv run python -m pytest -q tests/test_shape.py
./m depth 22
./m check
```

---

## §6 Request budget

| Item | Count | Cost |
|---|---|---|
| Model calls | 0 | £0 |
| Network requests | 0 — NumPy was installed on Day 20 | £0 |
| Live API keys used | none | £0 |
| Data downloaded | none; the twenty-eight-line file is written by hand in §3 | £0 |

**Zero model calls and zero network today** (Principle 5). Every measurement in the parts runs offline.

---

## §7 Traps

- **`(4, 7)` and `(4,)` will not broadcast**, because shapes are lined up from the **right**, so the 4
  lands under the 7 ([1.2](parts/01-broadcasting/1.2-the-rule-in-three-lines.md)).
- **A per-row statistic needs `keepdims=True`.** Without it the operation raises on a rectangular array
  and silently uses the wrong axis on a square one
  ([1.4](parts/01-broadcasting/1.4-keepdims-and-the-column.md)).
- **`(n, 1)` against `(1, n)` produces `n × n` values.** Twenty thousand becomes 3.2 GB; two hundred
  thousand becomes 320 GB ([1.7](parts/01-broadcasting/1.7-the-broadcast-that-ate-the-memory.md)).
- **`nbytes` on a broadcast array is a claim, not a measurement** — 800 MB reported for a few hundred
  bytes of storage ([1.5](parts/01-broadcasting/1.5-no-data-is-copied.md)).
- **`reshape` returns a view**, so writing to the reshaped array writes to the original
  ([2.1](parts/02-reshape/2.1-same-block-new-shape.md)).
- **`ravel` copies silently after a transpose**, turning a free operation into a full-array copy
  ([2.4](parts/02-reshape/2.4-ravel-and-flatten.md), [2.5](parts/02-reshape/2.5-when-reshape-must-copy.md)).
- **`arr.shape = (...)` is deprecated in NumPy 2.5.** The current way to demand a copy-free reshape is
  `np.reshape(arr, shape, copy=False)` ([2.5](parts/02-reshape/2.5-when-reshape-must-copy.md)).
- **`.T` on a one-dimensional array does nothing at all**, so it is not the way to make a column
  ([3.1](parts/03-transpose/3.1-t-the-axes-swapped.md)).
- **`.T` on three or more axes reverses all of them**, which is almost never what was meant and never
  raises ([3.2](parts/03-transpose/3.2-transpose-and-swapaxes.md)).
- **A transpose costs nothing and makes the next `copy`, `tobytes` or `ravel` cost about five times
  more** ([3.3](parts/03-transpose/3.3-contiguity-and-the-speed-you-lose.md)).
- **`concatenate` never broadcasts** — every axis but the joined one must match exactly
  ([4.1](parts/04-joining-and-splitting/4.1-concatenate.md)).
- **`np.append` is not `list.append`.** It allocates and copies the whole array, every call
  ([4.5](parts/04-joining-and-splitting/4.5-growing-an-array-in-a-loop.md)).
- **Concatenating inside a loop is quadratic.** Four hundred chunks is over a hundred times slower than
  one join ([4.5](parts/04-joining-and-splitting/4.5-growing-an-array-in-a-loop.md)).
- **A bare `.squeeze()` drops the batch axis when the batch is one**, which only happens in production
  ([4.4](parts/04-joining-and-splitting/4.4-newaxis-and-expand-dims.md)).
- **A square test fixture cannot tell `axis=0` from `axis=1`**
  ([5.2](parts/05-the-module/5.2-the-test-that-can-go-red.md)).

---

## §8 Verify before you code

Every one of these was fetched on 2026-09-02 and returned `200`. Read the first two before writing any
code; open the rest when a part points you at them.

- Broadcasting, the rule and its examples —
  <https://numpy.org/doc/stable/user/basics.broadcasting.html>
- Array manipulation routines, all of them in one table —
  <https://numpy.org/doc/stable/reference/routines.array-manipulation.html>
- `np.broadcast_to`, and why the result is read-only —
  <https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html>
- `np.broadcast_shapes`, for checking a rule without allocating —
  <https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html>
- `np.reshape`, including the `copy=` argument —
  <https://numpy.org/doc/stable/reference/generated/numpy.reshape.html>
- `np.ravel`, and its `order=` —
  <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html>
- `np.transpose` — <https://numpy.org/doc/stable/reference/generated/numpy.transpose.html>
- `np.moveaxis` — <https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html>
- `np.concatenate` — <https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html>
- `np.stack` — <https://numpy.org/doc/stable/reference/generated/numpy.stack.html>
- `np.array_split` — <https://numpy.org/doc/stable/reference/generated/numpy.array_split.html>
- `np.expand_dims` — <https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html>
- `np.ascontiguousarray` —
  <https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html>

---

## §9 Say it in an interview

"Broadcasting is one rule: line the two shapes up at the right-hand end, pad the shorter one with 1s
on the left, and every column must be equal or contain a 1, in which case that axis is stretched. It
is what lets you mean-centre sixty thousand rows by writing `X - X.mean(axis=0)` — about sixteen times
faster than a loop that is already vectorised inside, and no loop in the source. The stretching does
not copy: NumPy sets that axis's stride to zero, so the same values are read repeatedly, which is why
a broadcast array is read-only. The two things that bite are the padding direction and the shape of
the result. Because padding is on the left, a per-column statistic broadcasts back for free while a
per-row one needs `keepdims=True`, and on a square array the version without it does not raise — it
silently uses the wrong axis, which is why softmax and row normalisation are always written with
`keepdims`. And when both operands stretch, `(n,1)` against `(1,n)`, the result is n squared, so twenty
thousand values produce a 3.2 GB matrix and two hundred thousand kill the process. On the manipulation
side, reshape, transpose, `moveaxis` and slicing are all views — they rewrite a shape and some strides
and move nothing — so the cost of a transpose is not the transpose, it is that the array is no longer
contiguous and the next `ravel` or `tobytes` silently copies it. The one operation that always
allocates is joining: `concatenate` copies both inputs, so doing it inside a loop copies everything
accumulated so far on each pass and is quadratic. Collect into a list, join once."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m depth 22` passes, and `./m check` is
green. Done is defined by understanding and by green checks, never by elapsed time (Principle 17).

The three questions to answer out loud before you call it finished:

1. State the broadcasting rule in three steps, then say why `(4, 7)` works with `(7,)` and not with
   `(4,)`.
2. Name three shape operations that cost nothing and one that always allocates, and say what makes the
   difference.
3. You transpose an array and the next line gets much slower. What happened, and which two functions
   would let you pay for it deliberately instead?
