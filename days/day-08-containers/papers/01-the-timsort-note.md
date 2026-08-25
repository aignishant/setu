---
day: 8
part: "P1"
title: "The note that made sorting adaptive, and the proof that broke it — timsort"
ids: ["PY-07"]
level: production
kind: paper
paper: ["CPython listsort.txt", "doi:10.1007/978-3-319-21690-4_16"]
prerequisites: ["1.5"]
prev: "../parts/03-dedup/3.2-order-preserving-dedup.md"
next: "02-pep-456-and-siphash.md"
---

# The note that made sorting adaptive, and the proof that broke it

## One-line answer

CPython's `list.sort()` is **timsort**, an adaptive stable mergesort whose design is written down not
in a journal but in a plain-text file inside the interpreter's own source tree — and its central
claim, that real data arrives already containing sorted runs worth exploiting, was so widely adopted
that when a formal-verification effort found a bug in the algorithm's bookkeeping fifteen years
later, the same bug was sitting in Java, Android and Python at once.

---

## The citation

Two documents: the design note that defines the algorithm, and the verification paper that found what
was wrong with it.

| Field | The design note | The verification paper |
|---|---|---|
| **Title** | *"listsort.txt"* — the sorting note in CPython's source | *"OpenJDK's java.utils.Collection.sort() Is Broken: The Good, the Bad and the Worst Case"* |
| **Year** | 2002, maintained ever since | 2015 |
| **Identifier** | `CPython listsort.txt` | `doi:10.1007/978-3-319-21690-4_16` (CAV 2015, pages 273–289) |
| **URL** | <https://github.com/python/cpython/blob/main/Objects/listsort.txt> — fetched 2026-08-25 | <https://link.springer.com/chapter/10.1007/978-3-319-21690-4_16> — fetched 2026-08-25 |

**What to actually read.** In the note: the **"Intro"** paragraph, then **"Computing minrun"** and
**"Galloping"** — those three carry the whole design, and the note argues for its constants with
measurements rather than assertion, which is rarer than it should be. In the paper: the description of
the broken invariant and the crashing input. Reading them in that order is the point of this
document — a design, then somebody proving things about it.

**Note on what counts as a primary source.** `listsort.txt` was never peer-reviewed and never
published anywhere but a source tree. It is still the primary source: it is one dated document that
decided how sorting works in several major runtimes, and you can open it. The test in this plan's
Part 11.4 is not "was it refereed" but "is there one dated document that decided this".

---

## The story

Sorting was a solved problem. Quicksort for speed, mergesort when you need stability, heapsort when
you need the worst case bounded — the textbooks had been settled for decades, and there was nothing
obviously left to do.

But look at the lists real programs actually sort. Log lines arriving in near-time order with a few
stragglers. A table already sorted by date, being re-sorted by date and then name. Two sorted files
concatenated. A list that was sorted, had ten items appended, and needs sorting again. Almost none of
it is the uniformly random permutation the textbook analysis assumes — and a classical sort does the
same `n log n` work regardless, because it never looks to see whether the data is already organised.

The insight in the note is embarrassingly simple once stated: **scan the list, notice the stretches
that are already in order, and merge those instead of ignoring them.** A list that arrives sorted
costs `n - 1` comparisons — a single pass that confirms it — instead of `n log n`. Real data is full
of structure, and every previous algorithm threw that structure away on principle.

The second half of the story starts thirteen years later. A group trying to *prove* the algorithm
correct — a routine exercise, on code that had run in every Java and Python program for a decade —
could not close the proof. The invariant the merge bookkeeping was supposed to maintain did not
actually hold. That is where this document stops being a nice design note and starts being a lesson
about what "battle-tested" is worth.

---

## The idea in plain language

A **run** is a stretch of the list that is already in order. Timsort's whole strategy is: find the
runs, make sure none is too short, merge them in a disciplined order.

**Runs are found, not assumed.** Starting at each position, the algorithm walks forward while the
order holds. An *ascending* run is taken as it stands. A **strictly** descending run is reversed in
place — and the word *strictly* is doing real work: reversing a stretch containing equal elements
would swap their relative order and destroy stability, so equal neighbours end a descending run.

**Short runs are extended.** Random data produces runs of length two on average, and merging
thousands of tiny runs is all overhead. So a minimum run length, `minrun`, is chosen — between 32 and
64 — and any natural run shorter than that is extended by binary insertion sort. The note picks the
range by experiment, and says so:

> "When N is a power of 2, testing on random data showed that minrun values of 16, 32, 64 and 128
> worked about equally well."

with 256 losing to data movement and 8 losing to function-call overhead.

**Merging is disciplined by a stack invariant.** Runs are pushed onto a stack, and before pushing the
next one the algorithm merges to keep the run lengths roughly balanced — so a huge run never gets
merged repeatedly against tiny ones. That bookkeeping is the part the verification paper found broken.

**Galloping handles the lopsided case.** When merging, if one side keeps winning, the algorithm stops
comparing element by element and starts searching exponentially — 1, 2, 4, 8 ahead — to find where the
other side's next element belongs. The note argues the threshold, `MIN_GALLOP = 7`, from a comparison
count: galloping to position *i* costs about `2*floor(lg(i))+2` comparisons against a linear scan's
`i+1`, so it only pays from around position 6 onward.

The payoff, in the note's own words, is that on partially ordered data it takes "less than lg(N!)
comparisons needed, and as few as N-1" — below the information-theoretic bound for sorting a *random*
permutation, which is possible only because the data was never random.

---

## Why Setu needs it

- **[1.5](../parts/01-sequences/1.5-sort-sorted-and-key.md) taught `sort`, `sorted`, `key=` and
  stability**, and noted that CPython's sort is timsort with `O(n log n)` worst case and `O(n)` on
  organised data. This document is where that claim comes from, and why stability is not an
  implementation detail you may rely on by accident — it is a designed property that constrains the
  algorithm.
- **[3.1](../parts/03-dedup/3.1-ten-thousand-ids-timed.md) and
  [3.2](../parts/03-dedup/3.2-order-preserving-dedup.md)** both sort or preserve order over data that
  arrives with structure — exactly the case this algorithm was built for.
- **The `key=` argument's cost is decided here**: `key=` is computed once per element (the
  decorate-sort-undecorate pattern is built in), which matters because the comparisons happen on the
  computed keys, and the count of those comparisons is what this document is about.
- **Downstream:** every ranked retrieval result you sort by score, every leaderboard, every
  `sort_values` in the pandas phases sits on an implementation of this design or a close relative of
  it. Knowing that sorting nearly-sorted data is nearly free changes how you build pipelines.

---

## The mechanism

Run detection is the algorithm's first act and its whole thesis. It is about fifteen lines.

```python
def count_run(data: list, lo: int) -> int:
    """Length of the run starting at lo. A strictly descending run is reversed in place."""
    hi = len(data)
    if lo + 1 >= hi:
        return hi - lo
    end = lo + 1
    if data[end] < data[lo]:
        while end + 1 < hi and data[end + 1] < data[end]:
            end += 1
        data[lo : end + 1] = reversed(data[lo : end + 1])
    else:
        while end + 1 < hi and not data[end + 1] < data[end]:
            end += 1
    return end + 1 - lo
```

**Line by line:**

- `if lo + 1 >= hi: return hi - lo` — the last element of the list is a run of one. Without this the
  next line indexes past the end, which is the first thing that breaks when this is written from
  memory.
- `if data[end] < data[lo]:` — one comparison decides which kind of run this is. Everything after
  depends on that single test, which is why it is made once rather than re-derived in the loop.
- `while ... data[end + 1] < data[end]` — the descending branch uses **strict** `<`. Equal
  neighbours end the run. This is the stability rule: the reversal on the next line would otherwise
  swap two equal elements, and after that no amount of care downstream can restore their original
  order.
- `data[lo : end + 1] = reversed(...)` — slice assignment reverses in place, without allocating a new
  list. A descending run is as good as an ascending one *provided* it is reversed here, which is why
  reverse-sorted input is one of the algorithm's best cases rather than one of its worst.
- `not data[end + 1] < data[end]` in the ascending branch — written as the negation of `<` rather
  than as `>=`, because the algorithm is only allowed to use one comparison operator. Python's sort
  calls `__lt__` and nothing else; an object that defines `__lt__` and not `__ge__` must still sort,
  and expressing "non-descending" as `not <` is what guarantees that.
- `return end + 1 - lo` — a length, not an index. The caller advances `lo` by this amount, so an
  off-by-one here silently drops or repeats an element.

---

## The demo

One project, one feature: **detect the natural runs in a list, merge them, and count the comparisons
it took**. No galloping, no `minrun` extension, no merge-stack invariant — just the note's central
claim, made measurable.

```text
run-detector/
├── runsort.py        # natural run detection + merge, counting comparisons
└── test_runsort.py   # the note's claim, asserted
```

`runsort.py`, in full:

```python
"""Timsort's first idea, alone: real data already contains sorted runs, so find them."""


class Counter:
    """Counts comparisons, because the claim being demonstrated is about comparisons."""

    def __init__(self) -> None:
        self.count = 0

    def less(self, a, b) -> bool:
        self.count += 1
        return a < b


def count_run(data: list, lo: int, counter: Counter) -> int:
    """Length of the run starting at lo. A descending run is reversed in place, so it counts too."""
    hi = len(data)
    if lo + 1 >= hi:
        return hi - lo
    end = lo + 1
    if counter.less(data[end], data[lo]):  # strictly descending
        while end + 1 < hi and counter.less(data[end + 1], data[end]):
            end += 1
        data[lo : end + 1] = reversed(data[lo : end + 1])
    else:  # non-descending
        while end + 1 < hi and not counter.less(data[end + 1], data[end]):
            end += 1
    return end + 1 - lo


def merge(left: list, right: list, counter: Counter) -> list:
    out: list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if counter.less(right[j], left[i]):  # strict, so equal elements keep left first
            out.append(right[j])
            j += 1
        else:
            out.append(left[i])
            i += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def runsort(data: list) -> tuple[list, int, int]:
    """Sort by detecting natural runs and merging them. Returns (sorted, runs, comparisons)."""
    counter = Counter()
    working = list(data)
    runs: list[list] = []
    lo = 0
    while lo < len(working):
        length = count_run(working, lo, counter)
        runs.append(working[lo : lo + length])
        lo += length
    run_count = len(runs)
    while len(runs) > 1:
        merged = [
            merge(runs[i], runs[i + 1], counter) if i + 1 < len(runs) else runs[i]
            for i in range(0, len(runs), 2)
        ]
        runs = merged
    return (runs[0] if runs else []), run_count, counter.count
```

**Line by line:** — `count_run` is the mechanism above, with the comparison routed through a counter;
only what is new is walked through here.

- `class Counter` exists because the claim under test is *"fewer comparisons"*, and a wall-clock
  measurement would mix in interpreter overhead, allocation and cache behaviour. Counting the exact
  operation the analysis talks about is what makes the demo evidence rather than anecdote.
- `counter.less(a, b)` is the **only** comparison in the whole file. Every `<` goes through it, so
  the count cannot drift out of step with the work — a counter incremented next to a comparison
  eventually misses one.
- `if counter.less(right[j], left[i])` in `merge` — strict `<` again, and the direction matters: the
  right element is taken only when it is *strictly* smaller, so on a tie the left element goes first.
  That single choice is what makes the merge stable, and reversing the operands would silently break
  stability while still producing sorted output.
- `out.extend(left[i:])` and `out.extend(right[j:])` — after one side is exhausted the other is
  already sorted, so it is copied wholesale with **no** further comparisons. This is where an
  already-sorted input gets its `n - 1` behaviour.
- `working = list(data)` — a copy, so the caller's list is not reordered by the run detection. The
  real `list.sort()` deliberately does the opposite and sorts in place; this demo copies so the test
  can compare against the original.
- The pairwise merge loop halves the number of runs each pass, which is a *balanced* merge rather
  than timsort's stack-invariant merge. That is a simplification and it is the exact place the real
  algorithm keeps its bookkeeping — the bookkeeping the verification paper found broken.
- `return (runs[0] if runs else []), run_count, counter.count` — the run count is returned because it
  is the quantity that explains the comparison count. A demo that reported only the timing would show
  *that* structured data is cheaper without showing *why*.

`test_runsort.py`, in full:

```python
"""The note's claim, asserted: structured data costs fewer comparisons."""

import random

from runsort import runsort


def test_it_actually_sorts():
    random.seed(0)
    data = [random.randrange(1000) for _ in range(500)]
    assert runsort(data)[0] == sorted(data)


def test_a_sorted_list_is_one_run_and_n_minus_one_comparisons():
    data = list(range(1000))
    result, runs, comparisons = runsort(data)
    assert result == data
    assert runs == 1
    assert comparisons == len(data) - 1


def test_a_reversed_list_is_also_one_run():
    data = list(range(1000, 0, -1))
    result, runs, comparisons = runsort(data)
    assert result == sorted(data)
    assert runs == 1
    assert comparisons == len(data) - 1


def test_structure_is_cheaper_than_noise():
    random.seed(0)
    noise = [random.randrange(10_000) for _ in range(2000)]
    two_runs = sorted(noise[:1000]) + sorted(noise[1000:])
    assert runsort(two_runs)[2] < runsort(noise)[2] / 2


def test_the_merge_is_stable():
    data = [("b", 1), ("a", 1), ("c", 0)]
    keyed = [(value, index) for index, (_, value) in enumerate(data)]
    order = [index for _, index in runsort(keyed)[0]]
    assert order == [2, 0, 1]
```

**Line by line:**

- `random.seed(0)` — every random input is seeded, so a failure is reproducible. An unseeded
  benchmark that fails once a week is worse than no benchmark (Principle 4's habit, applied to tests).
- `assert comparisons == len(data) - 1` — an **exact** count, not an upper bound. The note's claim is
  precisely `n - 1` comparisons for an already-sorted list: one per adjacent pair, all inside a single
  run scan. Asserting the exact number means any regression that adds a comparison shows up.
- `test_a_reversed_list_is_also_one_run` uses `range(1000, 0, -1)` — no duplicates. That is
  deliberate: with duplicates the descending run breaks at every equal pair, because of the strictness
  rule above, and the run count would not be 1. The test asserts what the algorithm actually promises.
- `runsort(two_runs)[2] < runsort(noise)[2] / 2` — a *relative* claim, not an absolute number.
  Absolute comparison counts depend on the seed and the list length; the ratio is the property the
  design is claiming, and it survives changes to both.
- `keyed = [(value, index) ...]` in the stability test — pairs of (sort key, original position), so
  after sorting, reading the positions back shows whether equal keys kept their order. Asserting
  `[2, 0, 1]` — `"c"` first, then `"b"` before `"a"` — is stability stated as a fact rather than as a
  hope.

Run it:

```console
$ uv run --with pytest python -m pytest -q
.....                                                                    [100%]
5 passed in 0.05s

$ uv run python -c "
import random
from runsort import runsort
random.seed(0)
n = 2000
noise = [random.randrange(10_000) for _ in range(n)]
cases = {
 'random          ': noise,
 'already sorted  ': sorted(noise),
 'reversed        ': sorted(noise, reverse=True),
 'two sorted halves': sorted(noise[:n//2]) + sorted(noise[n//2:]),
 'sorted + 10 new ': sorted(noise)[:-10] + noise[:10],
}
for name, data in cases.items():
    _, runs, comps = runsort(data)
    print(f'{name}  runs={runs:5d}  comparisons={comps:6d}')"
random            runs=  831  comparisons= 20432
already sorted    runs=    1  comparisons=  1999
reversed          runs=  185  comparisons=  9478
two sorted halves  runs=    2  comparisons=  3995
sorted + 10 new   runs=    5  comparisons=  6717
```

Read the first two lines: the *same 2000 values*, ordered differently, cost 20 432 comparisons or
1 999 — a factor of ten, decided entirely by structure the algorithm bothered to look for.

Then read the third line, which is the interesting one. `reversed` gives **185 runs**, not 1, because
`sorted(noise, reverse=True)` contains duplicates and a descending run must be *strictly* descending
to be safely reversed. Stability costs something, and this line is the price, visible.

**What this demo deliberately leaves out.** `minrun` and the binary insertion that extends short runs
(which is why the random case here produces 831 tiny runs instead of ~60 chunky ones), galloping mode
and `MIN_GALLOP`, in-place merging with a temporary buffer, and the merge-stack invariant — which is
not a detail but *the* thing the verification paper is about, and which is discussed below rather than
implemented.

---

## When it breaks

The everyday failure has nothing to do with runs:

```python
sorted([1, "a"])
```

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

The sort calls `__lt__` and nothing else, so the first comparison between incompatible types ends it.
Note *where* it ends: mid-sort, with the list possibly already partly rearranged if you called
`list.sort()` rather than `sorted()`. A failed in-place sort does not roll back.

The failure that matters historically is the one the verification paper found. The merge stack keeps
an invariant on run lengths; the implementation's check was missing part of its condition, so the
invariant could be violated, so the pre-allocated stack could overflow. In Java this crashed with an
`ArrayIndexOutOfBoundsException` on arrays above roughly 67 million elements. CPython's stack was
generously sized, so it was only breakable above about 2⁴⁹ elements — unreachable in practice, but
**broken in the same way**. The fix landed in CPython 2.7.10, 3.4.4 and 3.5.0, tracked as
`bpo-23515`.

Sit with the shape of that. The code was fifteen years old, had run in essentially every Java and
Python program on earth, was reviewed by very good engineers, and was ported into two other major
runtimes on the strength of that record. It was not found by testing, by fuzzing, or by a crash
report. It was found by someone trying to write down a proof and failing.

**The smallest fix** for the everyday case: sort on a `key=` that produces one type — `key=str` or
`key=lambda x: (isinstance(x, str), x)` — so no comparison ever crosses types. And for the historical
case: keep the interpreter pinned and updated (Principle 4 and Principle 13), because the fix arrived
as a patch release.

---

## What did not survive

**The invariant did not hold, and neither did "battle-tested" as an argument.** The direct casualty is
a way of reasoning: *this code is old and heavily used, therefore it is correct*. Heavy use finds the
bugs that ordinary inputs trigger. It says nothing about the region of the input space no ordinary
input reaches, and that is exactly where this bug lived. Reach for the strongest tool available for
the property you care about — a proof for an invariant, a property test for a broad claim,
`hypothesis` when you cannot prove it — rather than the reassurance of a long deployment history.

**The fix was a patch to the condition, not a redesign.** The paper offered both a corrected version
of the existing check and a cleaner reformulation; the runtimes largely took the minimal patch. The
algorithm still carries bookkeeping that is difficult to reason about, and the follow-up literature —
adaptive Shivers sort and other variants — exists partly because that complexity turned out to be
hard to justify.

**The constants are of their moment.** `MIN_GALLOP = 7` and a `minrun` between 32 and 64 were measured
on early-2000s hardware. The note is unusually honest about this — it shows the measurements — but
cache hierarchies, branch predictors and memory bandwidth have all changed by more than an order of
magnitude, and nothing re-derives those constants for a modern machine.

**The design outgrew the note.** `listsort.txt` describes the algorithm as it was written for CPython
lists. Since then the same design has been ported, tweaked, partially re-derived and formally analysed
in half a dozen places, and CPython itself has added specialised comparison paths for lists that are
all `int`, all `str` or all `float` — a substantial performance change the note does not describe. The
document is the primary source for the *design*, not a current description of any one implementation.

---

## In production

**What a professional does with this.** They stop treating "sort it again" as expensive when the data
is already nearly ordered — re-sorting an almost-sorted list is close to a single pass, which changes
how you design incremental pipelines. They rely on stability *deliberately* — sorting by secondary key
first, then by primary key, to get a multi-key sort without building tuples — and they write a comment
saying so, because a future reader cannot tell an intentional two-pass sort from a redundant one. And
they put the expensive work in `key=` rather than in a comparison function, because `key=` is
evaluated once per element while a comparator is called `O(n log n)` times.

**What changes at scale.** Beyond memory, sorting stops being this algorithm at all: external sorts
merge sorted chunks from disk, and distributed frameworks sort by range-partitioning first — both of
which are *mergesort's* structure, which is why timsort's run-merging model is the right mental
picture for a shuffle. Inside one machine, the win from run detection is largest exactly where data
comes from a database with an `ORDER BY`, from an append-only log, or from a previous sort — which is
most production data.

**The failure that only shows with real data.** A pipeline sorts records by a `key=` returning a
tuple, and one field is occasionally `None`. Every test passes, because test fixtures are complete.
In production, one record with a `None` raises `TypeError: '<' not supported between instances of
'NoneType' and 'str'` — and if the sort was in place, the list is left partially reordered while the
exception propagates.

**The review comment a senior engineer leaves.** On `records.sort(key=lambda r: expensive(r))` —
*"`key=` is fine, that runs once per element; make sure `expensive` is pure, because the order it is
called in is not part of the contract."* On `sorted(rows, key=lambda r: r["score"])` for a mixed
column — *"That raises the moment a `None` appears. Sort on `(r['score'] is None, r['score'])` or
filter first."*

**The interview question.** *"What is the time complexity of Python's `list.sort()`?"* The answer
`O(n log n)` is correct and shallow. The answer that shows you have read the source is: *worst case
`O(n log n)`, but it is adaptive — it detects existing sorted runs, so an already-sorted list costs
`n - 1` comparisons and nearly-sorted data is close to linear; it is also stable, which is a designed
guarantee I can rely on for multi-key sorts.* The follow-up worth being ready for is *"why does
stability constrain the algorithm?"* — because descending runs may only be reversed when they are
strictly descending, which is exactly what the demo's third line shows.

---

## Check yourself

Run this now:

```bash
uv run python -c "
import random, time
random.seed(0)
data = [random.random() for _ in range(200_000)]
for name, d in [('random', data), ('sorted', sorted(data)), ('reversed', sorted(data)[::-1])]:
    copy = d[:]; t = time.perf_counter(); copy.sort(); print(f'{name:9s} {(time.perf_counter()-t)*1000:6.1f} ms')
"
```

The sorted and reversed cases should come in around a tenth of the random case — the note's claim,
reproduced on your own machine with the real implementation.

**Say this out loud, without scrolling up:** *explain why an already-sorted list costs `n - 1`
comparisons, why a descending run has to be strictly descending before it can be reversed, and what
the verification paper found that fifteen years of production traffic did not.*

Next: [PEP 456 and SipHash — the hash that had to become unpredictable](02-pep-456-and-siphash.md)
