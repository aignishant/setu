---
day: 23
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 23 — Universal functions, statistics, and the argsort top-k"
ids: ["NP-06", "NP-07"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 26
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 23 — Universal functions, statistics, and the `argsort` top-k

**Phase 3 · NumPy · Module 3** · `NP-06` arithmetic and universal functions, with the plan's named
example of **`np.where` as a vectorised `if`**; `NP-07` statistical, sorting, searching and counting
functions, with the plan's named example of **`argsort` to get top-k similar vectors — the retrieval
primitive, 130 days early**.

> **Yesterday:** making arrays of different shapes work together, and rearranging one array's shape —
> almost all of it for free, because almost all of it is a view.
> **Today:** the operations that actually compute. One instruction applied to every element, many numbers
> collapsed into one, and the question "which are the best few" answered without sorting anything.
> **Tomorrow:** bits and matrices — packing booleans into bytes, and the matrix product that every neural
> layer turns out to be.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody has been writing down how many steps they walked, every day, for a month. Four weeks of seven
numbers, on squared paper.

They want three quite different things from it, and it is worth noticing how different.

The first is a change applied to everything. "How far was each day from ten thousand?" That is one
instruction — subtract ten thousand — carried out twenty-eight times, and the answer is still twenty-eight
numbers. Nothing has been summarised; the whole month has simply been rewritten in a different unit.

The second is the opposite. "How did the month go?" Now they want **one** number instead of
twenty-eight, and the moment they pick one they have thrown something away. An average hides the good day
and the bad day. A best day hides everything except the best. There is no summary that keeps everything,
which is why a single number is never enough on its own, and why the honest version of an average comes
with how many days went into it — because one Thursday has no reading at all, and an average over
twenty-seven days labelled as a month is a small lie.

The third is different again, and it is the one that matters most for everything after this phase. "Which
were my three best days?" Not the values — the **days**. And the obvious way to answer it is to put all
twenty-eight in order and look at the end, which works and is far more work than the question needs.
Deciding whether day 14 beat day 22 is not something anybody asked about, and it is most of the effort.
A person doing this by hand would go through the list once keeping the best three so far, and never
compare the discarded days against each other at all.

Those three shapes — one instruction applied to everything, many numbers collapsed into one, and the best
few found without ordering the rest — are the whole day. The third one is the surprising one, and it is
the one you will still be using on Day 155, when the twenty-eight step counts have become two million
similarity scores and the "best three days" have become the three documents to answer a question with.

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the split is a group of sections per ID plus a
synthesis. **1.x is `NP-06`** entire: the ufunc, the object every arithmetic operator really is, and the
arguments and methods it carries that an operator cannot express. **2.x, 3.x and 4.x are `NP-07`**,
arranged by the kind of question asked rather than by function name — 2.x collapses many numbers into one,
3.x puts things in order and finds things in an order, and 4.x counts. **5.x is the synthesis**: the
module where both IDs meet, and the eval that can go red for a reason.

### Section 1 — ufuncs

| Part | What it answers | Level |
|---|---|---|
| [1.1 One operation, every element](parts/01-ufuncs/1.1-one-operation-every-element.md) | What is `+` actually calling? | `foundation` |
| [1.2 `out=` and the temporaries](parts/01-ufuncs/1.2-out-and-the-temporaries.md) | Where did four copies of my array come from? | `working` |
| [1.3 Dividing by zero warns](parts/01-ufuncs/1.3-divide-by-zero-warns.md) | Why did it not raise? | `working` |
| [1.4 `np.where`](parts/01-ufuncs/1.4-np-where-the-vectorised-if.md) | How do you write an `if` with no loop? | `working` |
| [1.5 `maximum` against `max`](parts/01-ufuncs/1.5-maximum-clip-and-elementwise.md) | One letter apart — what changed? | `working` |
| [1.6 `isclose` and `allclose`](parts/01-ufuncs/1.6-isclose-and-allclose.md) | How do you compare floats at all? | `working` |
| [1.7 `reduce`, `accumulate`, `at`](parts/01-ufuncs/1.7-reduce-accumulate-and-at.md) | What else does every ufunc carry? | `production` |

### Section 2 — statistics

| Part | What it answers | Level |
|---|---|---|
| [2.1 Many into one](parts/02-statistics/2.1-a-reduction-turns-many-into-one.md) | What is a reduction, and what does it cost you? | `foundation` |
| [2.2 `axis` — the one that disappears](parts/02-statistics/2.2-axis-the-one-that-disappears.md) | Per week or per weekday? | `foundation` |
| [2.3 `std`, `var` and `ddof`](parts/02-statistics/2.3-std-var-and-ddof.md) | Why does pandas disagree with NumPy? | `working` |
| [2.4 `median`, `percentile`, `quantile`](parts/02-statistics/2.4-median-percentile-and-quantile.md) | Which summary can one bad day not move? | `working` |
| [2.5 The `nan` family](parts/02-statistics/2.5-the-nan-family.md) | One missing day made everything `nan`. Now what? | `working` |
| [2.6 Float summation and the drift](parts/02-statistics/2.6-float-summation-and-the-drift.md) | Why does my total depend on the order? | `production` |

### Section 3 — sorting and searching

| Part | What it answers | Level |
|---|---|---|
| [3.1 `np.sort` and `.sort()`](parts/03-sorting-and-searching/3.1-sort-and-the-copy.md) | Which one rearranged my caller's array? | `foundation` |
| [3.2 `argsort` — the positions](parts/03-sorting-and-searching/3.2-argsort-the-positions.md) | How do labels stay attached to their numbers? | `working` |
| [3.3 Top-k and `argpartition`](parts/03-sorting-and-searching/3.3-top-k-and-argpartition.md) | Ten of a million, without sorting a million? | `working` |
| [3.4 Sorting along an axis](parts/03-sorting-and-searching/3.4-sorting-along-an-axis.md) | Why did my table come apart? | `working` |
| [3.5 `searchsorted`](parts/03-sorting-and-searching/3.5-searchsorted.md) | Where would this value go, in twenty steps? | `working` |
| [3.6 Stability and `kind=`](parts/03-sorting-and-searching/3.6-stability-and-kind.md) | Why did the list reshuffle on unchanged data? | `production` |

### Section 4 — counting

| Part | What it answers | Level |
|---|---|---|
| [4.1 `count_nonzero` and the mask](parts/04-counting/4.1-count-nonzero-and-the-mask.md) | How many days hit the goal? | `foundation` |
| [4.2 `np.unique`](parts/04-counting/4.2-unique.md) | What is in here, and how many of each? | `working` |
| [4.3 `np.bincount`](parts/04-counting/4.3-bincount.md) | Counting with no sort — and the 40 MB surprise | `working` |
| [4.4 `np.histogram`](parts/04-counting/4.4-histogram-and-the-edges.md) | Which bin does a value on the edge go in? | `working` |
| [4.5 `np.isin`](parts/04-counting/4.5-isin-and-membership.md) | Is each of a million values one of these? | `production` |

### Section 5 — the module

| Part | What it answers | Level |
|---|---|---|
| [5.1 `src/setu/summary.py`](parts/05-the-module/5.1-the-summary-module.md) | What should a summary refuse to decide for you? | `production` |
| [5.2 `tests/test_summary.py`](parts/05-the-module/5.2-the-test-that-can-go-red.md) | How do you test a number without pinning it? | `production` |

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
./m scaffold 23
touch src/setu/summary.py tests/test_summary.py
ls data/steps/month-flat.txt
```

The twenty-eight-line file from Day 22 is reused unchanged. **One thing has changed about the data
today**, and it is the subject rather than an inconvenience: the Thursday of week one goes back to being
a hole. Day 22 filled it with `9000` so that the shape arithmetic could be studied without missing values
in the way; today the missing value is half the lesson
([2.5](parts/02-statistics/2.5-the-nan-family.md)). Read the file, convert to `float64`, and put the
`nan` back:

```bash
uv run python -c "
import numpy as np
flat = np.loadtxt('data/steps/month-flat.txt', dtype=np.float64)
month = flat.reshape(-1, 7)
month[0, 3] = np.nan
print(month.shape, 'recorded:', np.count_nonzero(~np.isnan(month)), 'of', month.size)
"
```

An integer array cannot hold a missing day at all, which is why the `dtype=np.float64` is not optional
([Day 20, 2.1](../day-20-arrays-and-dtypes/parts/02-dtypes/2.1-a-dtype-is-a-promise.md)).

---

## §4 Build brief

**One new module and one test file.** `src/setu/summary.py` summarises a run of daily counts and finds
the best few without sorting. Add `summary` to `LAYERS` in `src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**`src/setu/summary.py`** — [5.1](parts/05-the-module/5.1-the-summary-module.md) explains every line.

```python
"""Summarise a run of daily counts, and find the best days without sorting them all."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

ACCUMULATE_IN = np.float64
MIN_DAYS_FOR_SPREAD = 4


@dataclass(frozen=True, slots=True)
class Summary:
    """Every number this module reports, with the evidence behind it."""

    observed: int
    expected: int
    mean: float
    median: float
    std: float
    p25: float
    p75: float
    best: np.ndarray

    @property
    def complete(self) -> bool:
        # TODO(me): one line. Say in a comment why this is a property and not a field,
        # using the word "disagree".
        raise NotImplementedError

    @property
    def iqr(self) -> float:
        # TODO(me): one line. Then say in a comment which of std and iqr you would put
        # on a dashboard that alerts people, and why (part 2.4).
        raise NotImplementedError


def top_k(scores: np.ndarray, k: int) -> np.ndarray:
    """Positions of the ``k`` largest scores, best first."""
    # TODO(me): refuse k < 1, but CLAMP k larger than the array. Write in a comment why
    # those two are treated differently - one is a caller bug and one is not.
    # TODO(me): ravel first. Say in a comment what that costs (part 3.1 will tell you it
    # is nothing, but prove it with np.shares_memory before you believe it).
    # TODO(me): drop the nan scores and KEEP THEIR POSITIONS. Run it once without this
    # step on data containing a nan and record who came top (part 3.2).
    # TODO(me): the empty case must return an array that is still a legal INDEX. Try
    # returning np.array([]) instead and record the error the caller gets.
    # TODO(me): argpartition over everything, then argsort only the k survivors. There
    # are TWO translate-backs in this function - mark both with a comment saying which
    # array the positions refer to before and after (part 3.3).
    raise NotImplementedError


def summarise(counts: np.ndarray, *, k: int = 3, sample: bool = True) -> Summary:
    """Summarise ``counts``, ignoring days that were never recorded."""
    # TODO(me): refuse a non-float dtype. Say in a comment what an integer array being
    # passed here tells you about a step earlier in the pipeline (part 2.5).
    # TODO(me): count the recorded days BEFORE computing anything, and guard on
    # MIN_DAYS_FOR_SPREAD. The message must name both counts.
    # TODO(me): all three quartiles in ONE nanpercentile call. Write the three-call
    # version in a comment and say how many times it partitions the array (part 2.4).
    # TODO(me): state method= even though it is the default, and say in a comment who
    # you are protecting from what.
    # TODO(me): translate `sample` into ddof here, so the caller never types ddof
    # (part 2.3).
    # TODO(me): dtype=ACCUMULATE_IN on the mean and the std. Say in a comment whether
    # that argument is a cast of the input or the accumulator, and what it costs
    # (part 2.6).
    # TODO(me): float() every scalar and NOT the positions. Say why in a comment.
    raise NotImplementedError


def hit_rate(counts: np.ndarray, goal: float) -> tuple[int, int]:
    """How many recorded days reached ``goal``, and how many days were recorded."""
    # TODO(me): a missing day is not a miss. Write the version that gets this wrong in a
    # comment and say what it does to a leaderboard (part 4.1).
    # TODO(me): return BOTH numbers. Say in a comment what a bare count of 8 fails to
    # tell an on-call engineer.
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

**`tests/test_summary.py`** — [5.2](parts/05-the-module/5.2-the-test-that-can-go-red.md) explains every
assertion, and why a test that pins a number proves nothing.

```python
"""Day 23's eval: every promise the summary module makes, asserted."""

from __future__ import annotations

import numpy as np
import pytest

from setu.summary import MIN_DAYS_FOR_SPREAD, Summary, hit_rate, summarise, top_k

# TODO(me): twenty-eight days as float64, NOT square and NOT sorted. Write a comment
# above it naming the two bugs a (7, 7) ascending fixture cannot catch.
MONTH = np.array([])


@pytest.fixture
def month() -> np.ndarray:
    # TODO(me): a fresh copy per test. Name the fixture below that would corrupt every
    # later test without it.
    raise NotImplementedError


@pytest.fixture
def gappy(month: np.ndarray) -> np.ndarray:
    # TODO(me): build this FROM the month fixture, not from MONTH. Say why in a comment.
    raise NotImplementedError


def test_summary_counts_only_recorded_days(gappy):
    # TODO(me): observed, expected, and complete. Use `is False`, not `== False`, and
    # say in a comment what that extra strictness is checking.
    raise NotImplementedError


def test_mean_ignores_the_missing_day_and_divides_by_the_survivors(gappy):
    # TODO(me): compute the expected answer a DIFFERENT WAY inside the test. No literal
    # number anywhere. Say in a comment what a pinned 9106.7 would have failed to catch.
    raise NotImplementedError


def test_ddof_changes_the_answer_by_the_known_ratio(month):
    # TODO(me): the ratio of the two standard deviations is sqrt(n/(n-1)) exactly.
    # Assert the direction first, then the ratio, and say in a comment why the direction
    # assertion earns its line.
    raise NotImplementedError


def test_the_input_is_never_modified(gappy):
    # TODO(me): np.array_equal needs one keyword here or it fails on correct code. Run
    # it without the keyword first and record what happens (part 2.5).
    raise NotImplementedError


def test_median_is_not_the_mean_on_skewed_data():
    # TODO(me): four small values and one enormous one. Assert the median is unmoved AND
    # the mean is dragged. Say in a comment what a test with only the first half proves.
    raise NotImplementedError


def test_every_scalar_field_is_a_plain_python_float(month):
    # TODO(me): `type(x) is float`, not isinstance. Say in a comment why isinstance would
    # pass on np.float64 and what that would let through.
    raise NotImplementedError


def test_summarise_refuses_an_integer_array(month):
    # TODO(me): pytest.raises with match= on YOUR message, not on the exception type.
    raise NotImplementedError


def test_summarise_refuses_too_few_recorded_days():
    # TODO(me): match= on the counts in the message. The pattern needs a raw string -
    # try it without one first and record what pytest says.
    raise NotImplementedError


def test_top_k_agrees_with_a_full_sort(month):
    # TODO(me): compare SETS against np.argsort. Write the array-equality version in a
    # comment and say when it would start failing (part 3.3).
    raise NotImplementedError


def test_top_k_is_ordered_best_first(month):
    # TODO(me): np.diff, and strict <. Say in a comment what non-strict <= would allow.
    raise NotImplementedError


def test_top_k_never_returns_a_missing_day(gappy):
    # TODO(me): ask for ALL of them, not three. Say in a comment why a top-three cannot
    # catch this bug.
    raise NotImplementedError


def test_top_k_clamps_to_what_exists():
    # TODO(me): two values, k of ten.
    raise NotImplementedError


def test_top_k_of_nothing_is_still_an_index():
    # TODO(me): size zero is not enough - INDEX something with the empty result. Say in
    # a comment what dtype makes that work.
    raise NotImplementedError


def test_top_k_refuses_zero(month):
    # TODO(me): match= on your message.
    raise NotImplementedError


def test_hit_rate_reports_both_numbers(gappy):
    # TODO(me): assert both. Say in a comment which of the two is the one that stops a
    # dashboard lying.
    raise NotImplementedError
```

**Then break it on purpose, twice.** First change `ddof=1 if sample else 0` to `ddof=0`, run the suite,
and read the message — one test fails and it compares a number against itself. Put it back. Then delete
the outer `candidates[...]` from `top_k`'s return, run again, and count how many tests catch it and which
one names both the wrong answer and the right one. A test you have never seen fail is not yet a test
(Principle 7).

```bash
uv run python -m pytest -q tests/test_summary.py
./m depth 23
./m check
```

---

## §6 Request budget

| Item | Count | Cost |
|---|---|---|
| Model calls | 0 | £0 |
| Network requests | 0 — NumPy was installed on Day 20 | £0 |
| Live API keys used | none | £0 |
| Data downloaded | none; `data/steps/month-flat.txt` already exists from Day 22 | £0 |

**Zero model calls and zero network today** (Principle 5). Every measurement in the parts runs offline,
and the two timing comparisons — top-k against a sort, and `isin` against a Python loop — are the only
things on this day that take noticeable wall-clock.

---

## §7 Traps

- **`np.max` and `np.maximum` are different operations**, one letter apart: a reduction and an
  elementwise ufunc ([1.5](parts/01-ufuncs/1.5-maximum-clip-and-elementwise.md)).
- **Dividing by zero warns and continues**, giving `inf` or `nan` rather than raising
  ([1.3](parts/01-ufuncs/1.3-divide-by-zero-warns.md)).
- **`np.where` evaluates both branches**, so it cannot be used to guard against an expensive or invalid
  computation ([1.4](parts/01-ufuncs/1.4-np-where-the-vectorised-if.md)).
- **On a square array the wrong `axis` gives the right shape and wrong numbers**, with no error at all
  ([2.2](parts/02-statistics/2.2-axis-the-one-that-disappears.md)).
- **NumPy's `std` defaults to `ddof=0` and pandas' to `ddof=1`**, an eight per cent difference on seven
  values ([2.3](parts/02-statistics/2.3-std-var-and-ddof.md)).
- **`ddof >= n` gives `nan` with a warning, not an error** — which is what per-group statistics on
  single-row groups produce ([2.3](parts/02-statistics/2.3-std-var-and-ddof.md)).
- **One `nan` makes every ordinary reduction `nan`**, and `arr == np.nan` finds nothing
  ([2.5](parts/02-statistics/2.5-the-nan-family.md)).
- **`argmax` returns the position of the `nan`**, which looks like a valid answer
  ([2.5](parts/02-statistics/2.5-the-nan-family.md)).
- **`nansum` of an all-missing array returns `0.0` silently** while `nanmean` returns `nan` and
  `nanargmax` raises ([2.5](parts/02-statistics/2.5-the-nan-family.md)).
- **`a.sum()` on a large `float32` array drifts**, and `dtype=np.float64` is the one-argument fix
  ([2.6](parts/02-statistics/2.6-float-summation-and-the-drift.md)).
- **A `float32` counter stops incrementing at 2²⁴**, permanently and silently
  ([2.6](parts/02-statistics/2.6-float-summation-and-the-drift.md)).
- **`arr.sort()` returns `None`**, so `arr = arr.sort()` throws the array away
  ([3.1](parts/03-sorting-and-searching/3.1-sort-and-the-copy.md)).
- **Sorting a slice in place reorders the parent array**, because a slice is a view
  ([3.1](parts/03-sorting-and-searching/3.1-sort-and-the-copy.md)).
- **There is no `reverse=True`** — descending is `[::-1]` on the **positions**, never on the input
  ([3.2](parts/03-sorting-and-searching/3.2-argsort-the-positions.md)).
- **Positions from a filtered or shortlisted array must be translated back**, or you silently return the
  first `k` items ([3.3](parts/03-sorting-and-searching/3.3-top-k-and-argpartition.md)).
- **`argpartition` only promises the top `k` as a set**, so asserting its whole output against `argsort`
  is a flaky test ([3.3](parts/03-sorting-and-searching/3.3-top-k-and-argpartition.md)).
- **`np.sort(table, axis=0)` shreds the rows** — sorting a table by a column is `argsort` plus a fancy
  index ([3.4](parts/03-sorting-and-searching/3.4-sorting-along-an-axis.md)).
- **A per-row `argsort` cannot index the array directly**; that adds an axis, and
  `np.take_along_axis` is the partner ([3.4](parts/03-sorting-and-searching/3.4-sorting-along-an-axis.md)).
- **`searchsorted` never checks that its array is sorted** and returns a plausible wrong number if it is
  not ([3.5](parts/03-sorting-and-searching/3.5-searchsorted.md)).
- **The default sort is unstable**, and a small fixture hides it because introsort falls back to a stable
  insertion sort ([3.6](parts/03-sorting-and-searching/3.6-stability-and-kind.md)).
- **`np.count_nonzero(arr)` without a comparison counts every non-zero element**, which is almost always
  everything ([4.1](parts/04-counting/4.1-count-nonzero-and-the-mask.md)).
- **A rate written with `//` is always zero** and never warns
  ([4.1](parts/04-counting/4.1-count-nonzero-and-the-mask.md)).
- **`np.unique`'s counts are indexed by position, not by value**
  ([4.2](parts/04-counting/4.2-unique.md)).
- **`np.bincount` allocates `max(value) + 1` slots**, so calling it on identifiers allocates gigabytes
  without warning ([4.3](parts/04-counting/4.3-bincount.md)).
- **`np.bincount` without `minlength=` silently shortens** when the highest code is absent
  ([4.3](parts/04-counting/4.3-bincount.md)).
- **Histogram bins are `[low, high)` except the last**, which is closed at both ends
  ([4.4](parts/04-counting/4.4-histogram-and-the-edges.md)).
- **`bins=<a number>` derives the edges from the data**, so two such histograms are not comparable and
  not summable ([4.4](parts/04-counting/4.4-histogram-and-the-edges.md)).
- **Values outside the outermost histogram edges are dropped silently**
  ([4.4](parts/04-counting/4.4-histogram-and-the-edges.md)).
- **Passing a Python `set` to `np.isin` gives an all-`False` mask with no error**
  ([4.5](parts/04-counting/4.5-isin-and-membership.md)).
- **A dtype mismatch in `np.isin` matches nothing and looks like an empty result**
  ([4.5](parts/04-counting/4.5-isin-and-membership.md)).

---

## §8 Verify before you code

Every one of these was fetched on 2026-09-02 and returned `200`. Read the first two before writing any
code; open the rest when a part points you at them.

- Universal functions, the whole model — <https://numpy.org/doc/stable/reference/ufuncs.html>
- Statistics routines, all of them in one table —
  <https://numpy.org/doc/stable/reference/routines.statistics.html>
- Sorting, searching and counting routines —
  <https://numpy.org/doc/stable/reference/routines.sort.html>
- `np.sum`, including the note on pairwise summation and `dtype=` —
  <https://numpy.org/doc/stable/reference/generated/numpy.sum.html>
- `np.percentile`, including all nine `method=` values —
  <https://numpy.org/doc/stable/reference/generated/numpy.percentile.html>
- `np.nanmean` — <https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html>
- `np.errstate` — <https://numpy.org/doc/stable/reference/generated/numpy.errstate.html>
- `np.sort`, including `kind=` and what each name really selects —
  <https://numpy.org/doc/stable/reference/generated/numpy.sort.html>
- `np.argpartition` — <https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html>
- `np.searchsorted` — <https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html>
- `np.unique` — <https://numpy.org/doc/stable/reference/generated/numpy.unique.html>
- `np.bincount` — <https://numpy.org/doc/stable/reference/generated/numpy.bincount.html>
- `np.histogram` — <https://numpy.org/doc/stable/reference/generated/numpy.histogram.html>
- `np.isin` — <https://numpy.org/doc/stable/reference/generated/numpy.isin.html>

One dated source is cited inside the day. The nine interpolation methods for `percentile` come from
*Sample Quantiles in Statistical Packages* (1996, DOI 10.1080/00031305.1996.10473566,
<https://doi.org/10.1080/00031305.1996.10473566>), which is where the names `hazen`, `weibull` and
`median_unbiased` are defined.

---

## §9 Say it in an interview

"Every arithmetic operator in NumPy is a universal function — `a + b` is `np.add(a, b)` — which matters
because the object form takes arguments the operator cannot: `out=` to write into a buffer you already
own rather than allocating, `where=` to apply the operation only where a mask is true, and methods like
`reduce` and `at`. The compiled loop it picks decides the output dtype, so an `int32` array plus a Python
float silently becomes `float64` and doubles your memory. On the statistics side the three things that
bite are all defaults. `axis` names the axis that disappears, and on a square array the wrong one gives
the right shape and the wrong numbers with no error. `std` defaults to `ddof=0` while pandas and R default
to `ddof=1`, which is an eight per cent difference on seven values and invisible on seven million — so it
matters most for per-group statistics and cross-validation error bars. And one `nan` turns every ordinary
reduction into `nan`, which is deliberate, but `argmax` returns the position **of** the `nan`, which looks
like a real answer. The `nan`-aware family fixes that and is inconsistent at the edges: on an all-missing
input `nansum` gives `0.0` silently, `nanmean` gives `nan` with a warning, and `nanargmax` raises. The
part I would actually lead with is top-k. Getting the ten most similar vectors out of a million scores
does not need a sort: `np.argpartition(scores, -10)[-10:]` places only the boundary element correctly and
leaves both sides unordered, which is one pass rather than `n log n` — I measured about eleven times
faster on two million `float32` scores — and then you sort just those ten to rank them. It returns
positions, so the same call turns similarity scores into document identifiers, which is exactly what a
vector search does. Two things to be careful of: `k` has to be clamped against the array size or it
raises, and the positions from that second sort refer to the shortlist, so they have to be translated back
through the first result — skip that and you silently return the first ten items every time."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m depth 23` passes, and `./m check` is green.
Done is defined by understanding and by green checks, never by elapsed time (Principle 17).

The three questions to answer out loud before you call it finished:

1. Name three things a ufunc gives you that a bare operator cannot, and say what decides the dtype of
   `int32_array + 1.0`.
2. Your service and a colleague's notebook report different standard deviations for the same seven
   numbers. Say why, give the exact ratio between the answers, and say what you would change.
3. Get the ten most similar of a million vectors. Write the two lines, say why neither of them is a sort,
   and name the two places a position has to be translated back.
