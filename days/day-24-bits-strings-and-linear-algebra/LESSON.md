---
day: 24
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 24 — Bits, text, and the matrix product every layer is"
ids: ["NP-08", "NP-09"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 24
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 24 — Bits, text, and the matrix product every layer is

**Phase 3 · NumPy · Module 3** · `NP-08` binary and string functions, with the plan's named example of
**`np.packbits` for a compact boolean mask**; `NP-09` matrix operations and linear algebra, with the plan's
named example of **`A @ B` by hand against `np.matmul` — the operation every neural layer is**.

> **Yesterday:** the operations that compute — one instruction applied to every element, many numbers
> collapsed into one, and the top-k that never sorts.
> **Today:** two things NumPy does that are not arithmetic on numbers. Packing yes-or-no answers into the
> bits of one integer, and handling text that a person typed; then the matrix product, which is arithmetic
> on numbers and is the single most important operation in everything after this phase.
> **Tomorrow:** the phase gate — copy against view decided as a policy, and a vectorised stats module that
> beats a loop by fifty times.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Five people share a flat, and there is a chart on the fridge. Eight jobs down the side — bins, hoover,
dishes, bathroom, shopping, recycling, windows, post — and a tick against each job somebody has done this
week.

Forty boxes, each holding a yes or a no. That is the whole of today's data.

The first thing anybody notices about that chart is how little is written on it. Forty ticks and blanks is
almost nothing, and yet writing it out longhand fills a page and copying a year of them fills a notebook.
The obvious response is the one people actually reach for: agree an order for the jobs, once, at the top of
the page — and then each week's row can be written as a single short code instead of eight separate marks.
That is the first section, and the saving is exactly eightfold, because a computer storing a yes-or-no uses
a whole byte where one bit would do.

The second thing anybody notices is that the chart is a mess of spellings. Somebody typed "Bins" with a
capital. Somebody left a space after it. One person had caps lock on. Four people typing the same word four
times produce four different values, and a program counting them finds four different jobs. Nobody did
anything wrong; that is simply what happens when humans type, and the fix is to agree what a name looks
like before counting anything.

The third thing takes longer to notice and is worth more than the other two together. Two people can put
their rows side by side and count the jobs they **both** did — walk along the eight positions together,
tick where both ticked, add up the ticks. One number, and it says something real about the two of them.

Do that for every pair and you have a grid: five rows, five columns, the entry where two people meet
saying how much they overlap. Twenty-five of those little walks, and there is nothing more to it than the
one walk repeated.

That grid is a **matrix product**, and it is the operation the rest of this curriculum is built on. It is
what a neural network layer is. It is what a search engine does to find the documents nearest a question.
It is the same twenty-five walks, done a billion times a second by code somebody spent decades tuning.
Today you write it out by hand first, three loops deep, and then measure exactly what that decades of
tuning bought — which turns out to be about twelve thousand times.

And there is a last question the chart can answer, which nobody would guess it could. If each person also
says how put-upon they felt at the end of the week — one number each — then you have several totals and
you know what went into each of them. That is enough to work backwards to what each individual job is
worth, the same way you could work out the price of milk from three shopping receipts. It is called
solving a system of equations, it is one function call, and it fails in three interesting ways that are the
last third of the day.

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the split is a group of sections per ID plus a module
where they meet. **1.x and 2.x are `NP-08`**: 1.x is the binary half — what a bit is, the four bitwise
ufuncs, shifting, flags and packing — and 2.x is the string half, which is short because NumPy's text
support is limited and knowing where it stops is most of the lesson. **3.x and 4.x are `NP-09`**: 3.x is
the matrix product, built from scratch before the library, and 4.x is what you do with it — solving,
measuring and the three ways a system goes wrong. **5.x is the synthesis**: one module using all four, and
the eval that can go red.

### Section 1 — bits

| Part | What it answers | Level |
|---|---|---|
| [1.1 A number is a row of switches](parts/01-bits/1.1-a-number-is-switches.md) | What is actually in an `int8`? | `foundation` |
| [1.2 The four bitwise ufuncs](parts/01-bits/1.2-the-four-bitwise-ufuncs.md) | What do `&`, `\|`, `^` and `~` do to a row of bits? | `foundation` |
| [1.3 `~` on a bool and on an int](parts/01-bits/1.3-tilde-on-bool-and-int.md) | Why did my filter select every row? | `working` |
| [1.4 `<<` and `>>`](parts/01-bits/1.4-shifts-and-the-bit-that-fell-off.md) | Where did the top bit go? | `working` |
| [1.5 A bitmask](parts/01-bits/1.5-a-bitmask.md) | Eight yes-or-no answers in one integer | `working` |
| [1.6 `packbits` and `unpackbits`](parts/01-bits/1.6-packbits.md) | Forty booleans in five bytes — and what does not survive | `production` |

### Section 2 — strings

| Part | What it answers | Level |
|---|---|---|
| [2.1 `<U8`, text in a fixed-width box](parts/02-strings/2.1-fixed-width-text.md) | Why did "recycling" become "recyclin"? | `foundation` |
| [2.2 `np.strings`](parts/02-strings/2.2-np-strings.md) | How do you lowercase a whole column? | `working` |
| [2.3 Comparison is not a match](parts/02-strings/2.3-comparison-is-not-a-match.md) | The filter returned nothing. Is that real? | `working` |
| [2.4 Where text does not belong](parts/02-strings/2.4-where-text-does-not-belong.md) | A million repeated names — how do you store them? | `production` |

### Section 3 — the matrix product

| Part | What it answers | Level |
|---|---|---|
| [3.1 A dot product is a total](parts/03-matmul/3.1-a-dot-product-is-a-total.md) | One number from two rows — what does it mean? | `foundation` |
| [3.2 `A @ B` by hand](parts/03-matmul/3.2-matmul-by-hand.md) | What is the shape rule, and why is it that? | `foundation` |
| [3.3 `@`, `matmul` and `dot`](parts/03-matmul/3.3-at-matmul-and-dot.md) | Three names — are they the same thing? | `working` |
| [3.4 The measured gap](parts/03-matmul/3.4-the-measured-gap.md) | What did the library buy you? | `working` |
| [3.5 Stacks of matrices](parts/03-matmul/3.5-stacks-of-matrices.md) | A hundred products in one call | `working` |
| [3.6 Every neural layer](parts/03-matmul/3.6-every-neural-layer.md) | What is a layer, arithmetically? | `production` |

### Section 4 — linear algebra

| Part | What it answers | Level |
|---|---|---|
| [4.1 Three trips, three prices](parts/04-linalg/4.1-three-trips-three-prices.md) | Totals known, prices unknown — now what? | `foundation` |
| [4.2 `solve`, and never `inv`](parts/04-linalg/4.2-solve-and-never-inv.md) | The algebra says invert. Why should you not? | `working` |
| [4.3 `np.linalg.norm`](parts/04-linalg/4.3-norm.md) | How do you compare patterns rather than volumes? | `working` |
| [4.4 Singular](parts/04-linalg/4.4-singular-and-the-error.md) | What does that error actually mean? | `working` |
| [4.5 `lstsq`](parts/04-linalg/4.5-lstsq.md) | Four receipts, three prices, no exact answer | `production` |
| [4.6 Conditioning](parts/04-linalg/4.6-conditioning.md) | It solved cleanly. Why is the answer noise? | `production` |

### Section 5 — the module

| Part | What it answers | Level |
|---|---|---|
| [5.1 `src/setu/chores.py`](parts/05-the-module/5.1-the-chores-module.md) | All four sections, wired together | `production` |
| [5.2 `tests/test_chores.py`](parts/05-the-module/5.2-the-test-that-can-go-red.md) | How do you test a wrapper around a library? | `production` |

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
./m scaffold 24
touch src/setu/chores.py tests/test_chores.py
mkdir -p data/chores
```

Today's data is small enough to write by hand, and writing it by hand is the point — five people, eight
jobs, forty ticks:

```bash
uv run python -c "
import numpy as np
did = np.array([
    [1, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0],
], dtype=bool)
np.save('data/chores/week.npy', did)
print('shape', did.shape, 'bytes', did.nbytes, 'packed', np.packbits(did).nbytes)
"
```

Note the two byte counts on that last line: **forty against five**. That eightfold gap is
[1.6](parts/01-bits/1.6-packbits.md)'s whole subject, and seeing it before reading anything is worth more
than the sentence explaining it.

One check on the machine, because [3.4](parts/03-matmul/3.4-the-measured-gap.md) depends on it:

```bash
uv run python -c "import numpy as np; np.show_config()"
```

This prints which linear algebra library NumPy is using. If it names OpenBLAS you will see the numbers that
part reports; a plain reference build is an order of magnitude slower and the ratio there will be smaller.

---

## §4 Build brief

**One new module and one test file.** `src/setu/chores.py` packs the chart, normalises the names, scores
the pairs and prices the chores. Add `chores` to `LAYERS` in `src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**`src/setu/chores.py`** — [5.1](parts/05-the-module/5.1-the-chores-module.md) explains every line.

```python
"""The flat's chore chart: packed into bits, scored with a matrix product, priced with a solve."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntFlag

import numpy as np

CHORE_DTYPE = np.uint8
NAME_WIDTH = 24
NAME_DTYPE = np.dtype(f"<U{NAME_WIDTH}")
BITORDER = "big"
ACCUMULATE_IN = np.float64
MAX_CONDITION = 1e10


class Chore(IntFlag):
    """One bit per chore, counted from the LEAST significant bit."""

    # TODO(me): eight members, written as 1 << n rather than 1, 2, 4, 8. Then write the
    # docstring paragraph this class needs - the one that stops somebody alphabetising
    # it. Say in it what happens to already-stored bytes if the order changes (part 1.5).
    BINS = 1 << 0


CHORE_NAMES = np.array([chore.name.lower() for chore in Chore], dtype=NAME_DTYPE)


def _check_width() -> None:
    """Fail at import if a flag no longer fits its storage dtype."""
    # TODO(me): compare the widest flag against np.iinfo(CHORE_DTYPE).max and raise.
    # Then write in a comment what a ninth flag's VALUE would be, and why a feature
    # built on it would never work and never error (part 1.5).
    raise NotImplementedError


_check_width()


def normalise(values: np.ndarray) -> np.ndarray:
    """Trim and lowercase, so four spellings of one chore become one value."""
    # TODO(me): refuse a non-text dtype, then strip and lower and cast to NAME_DTYPE.
    # Say in a comment why the cast is here and not left to whatever the batch produces
    # (part 2.1).
    raise NotImplementedError


def unknown_names(values: np.ndarray) -> np.ndarray:
    """The normalised names that are not chores. An empty result is the healthy one."""
    # TODO(me): normalise, then np.isin against CHORE_NAMES, then np.unique the misses.
    # Run it ONCE without normalising the vocabulary side and record what comes back
    # (part 2.3).
    raise NotImplementedError


@dataclass(frozen=True, slots=True)
class PackedChart:
    """A chart squeezed to one bit per tick, plus what is needed to unpack it."""

    data: np.ndarray
    shape: tuple[int, ...]
    bitorder: str = BITORDER

    @property
    def saving(self) -> float:
        # TODO(me): one line. Say in a comment what number you expect and when it is
        # NOT that number.
        raise NotImplementedError


def pack(chart: np.ndarray) -> PackedChart:
    """Pack a boolean chart eight ticks to a byte, keeping its shape and bit order."""
    # TODO(me): refuse a non-boolean dtype. The message must say what packbits WOULD
    # have done, not just what you expected (part 1.6).
    # TODO(me): store the shape and the bitorder alongside the bytes. Write in a comment
    # the three arrays that all pack to the same five bytes.
    raise NotImplementedError


def unpack(packed: PackedChart) -> np.ndarray:
    """Restore the chart exactly."""
    # TODO(me): count= is the argument that makes this exact. Run it once WITHOUT on a
    # five-chore chart and write down how many chores came back (part 1.6).
    # TODO(me): reshape, then astype(bool). Say in a comment what indexing with the
    # uint8 version would do instead.
    raise NotImplementedError


def overlap(chart: np.ndarray) -> np.ndarray:
    """How many chores each pair of people both did. (people, people), symmetric."""
    # TODO(me): refuse a BOOLEAN chart, and say in the message why - run it on booleans
    # first and paste what the grid looked like (part 3.1).
    # TODO(me): one @ against the transpose. Use swapaxes(-1, -2), not .T, and say in a
    # comment what .T would do to a stacked chart (part 3.5).
    # TODO(me): assert the output shape against the RULE, computed from the input, not
    # against a literal (part 3.2).
    raise NotImplementedError


def cosine(chart: np.ndarray) -> np.ndarray:
    """Overlap with each person's volume divided out."""
    # TODO(me): norm along the last axis with keepdims. Run it once without keepdims on
    # a SQUARE chart and record that it did not raise (part 4.3).
    # TODO(me): clamp the divisor. Say in a comment who the all-zero row is in a real
    # dataset.
    # TODO(me): clip to [-1, 1] and say in a comment what breaks downstream without it.
    raise NotImplementedError


@dataclass(frozen=True, slots=True)
class Fit:
    """Fitted chore values, and everything needed to judge them."""

    values: np.ndarray
    sum_squared_error: float
    rank: int
    n_chores: int
    condition: float

    @property
    def determined(self) -> bool:
        # TODO(me): one line. Say what a False here means about the answer.
        raise NotImplementedError

    @property
    def digits_left(self) -> float:
        # TODO(me): 16 minus log10 of the condition, guarded for infinity. Say in a
        # comment where the 16 comes from (part 4.6).
        raise NotImplementedError


def chore_values(chart: np.ndarray, scores: np.ndarray) -> Fit:
    """Least-squares fit of how much each chore is worth, from people's total scores."""
    # TODO(me): refuse FEWER rows than columns, and say in the message why an exact
    # arbitrary fit is worse than no fit (part 4.5).
    # TODO(me): lstsq with rcond=None, unpacking all FOUR returns.
    # TODO(me): residuals is EMPTY for an exact fit. Handle it, and put the reason in a
    # comment above the line (part 4.5).
    # TODO(me): compute the condition from the singular values you already have rather
    # than calling np.linalg.cond. Say in a comment what that saves.
    # TODO(me): refuse above MAX_CONDITION, with a message naming the DOMAIN cause
    # (part 4.6).
    raise NotImplementedError
```

---

## §5 The eval that must be able to fail

**`tests/test_chores.py`** — [5.2](parts/05-the-module/5.2-the-test-that-can-go-red.md) explains every
assertion and why the fixture is the design.

```python
"""Day 24's eval: every guard the chores module puts in front of a silent failure."""

from __future__ import annotations

import numpy as np
import pytest

from setu.chores import (
    CHORE_NAMES,
    Chore,
    chore_values,
    cosine,
    normalise,
    overlap,
    pack,
    unknown_names,
    unpack,
)

# TODO(me): five people, eight chores, dtype=bool, NOT square and NOT all the same row
# count. Write the comment above it naming the two bugs each of those choices protects
# against.
DID = np.array([])


@pytest.fixture
def did() -> np.ndarray:
    # TODO(me): a fresh copy per test. Name the test below that would corrupt the others.
    raise NotImplementedError


@pytest.fixture
def counts(did: np.ndarray) -> np.ndarray:
    # TODO(me): build FROM did, not from DID. Say why in a comment.
    raise NotImplementedError


def test_pack_saves_eight_times(did):
    # TODO(me): assert the reported saving AND the raw byte counts. Say in a comment
    # what the second assertion catches that the first does not.
    raise NotImplementedError


def test_pack_round_trips_a_width_that_is_not_a_multiple_of_eight(did):
    # TODO(me): slice to five chores, ASSERT that five is not a multiple of eight, then
    # round trip. Say in a comment why that middle assertion is in a test at all.
    raise NotImplementedError


def test_pack_refuses_counts():
    # TODO(me): pytest.raises with match= on YOUR message, not the exception type.
    raise NotImplementedError


def test_overlap_diagonal_is_each_persons_total(counts):
    # TODO(me): compute the expected answer a DIFFERENT way. No literal numbers.
    raise NotImplementedError


def test_overlap_is_symmetric(counts):
    # TODO(me): one line. Say in a comment which mistake this catches.
    raise NotImplementedError


def test_overlap_refuses_booleans(did):
    # TODO(me): match= on one distinctive word. Say in a comment what the function
    # returns without the guard.
    raise NotImplementedError


def test_overlap_batches(counts):
    # TODO(me): stack two charts, assert the shape AND that entry 0 matches the
    # unstacked answer.
    raise NotImplementedError


def test_cosine_diagonal_is_one(counts):
    raise NotImplementedError


def test_cosine_removes_the_volume_advantage(counts):
    # TODO(me): triple ONE person's row. Assert their raw overlaps triple and their
    # cosine scores do not move. Say in a comment why the diagonal is excluded.
    raise NotImplementedError


def test_cosine_of_an_empty_row_is_not_nan():
    # TODO(me): two assertions - no nan anywhere, AND the empty row scores zero. Say in
    # a comment what a "fix" that filled with ones would do to the second.
    raise NotImplementedError


def test_normalise_collapses_spellings():
    raise NotImplementedError


def test_unknown_names_finds_the_typo():
    raise NotImplementedError


def test_unknown_names_is_empty_for_the_vocabulary():
    # TODO(me): the vocabulary against itself. Say what a non-empty result would mean.
    raise NotImplementedError


def test_chore_values_recovers_the_truth():
    # TODO(me): choose the true values, BUILD the scores from them, add seeded noise,
    # and assert recovery within a tolerance chosen against the noise level. Say in a
    # comment what a zero-noise version would have proved.
    raise NotImplementedError


def test_chore_values_refuses_too_few_people(counts):
    # TODO(me): the day's own fixture is the underdetermined case. match= your message.
    raise NotImplementedError


def test_chore_values_refuses_indistinguishable_chores():
    # TODO(me): make one column a copy of another. Use enough rows that the SHAPE guard
    # does not fire first - say in a comment why the ordering matters.
    raise NotImplementedError


def test_chore_values_reports_a_number_even_for_an_exact_fit():
    # TODO(me): an identity chart fits exactly, so residuals comes back empty. Assert
    # the reported error is a float anyway.
    raise NotImplementedError


def test_the_flags_still_fit_their_dtype():
    raise NotImplementedError
```

**Then break it on purpose, twice.** First delete `count=count` from `unpack`, run the suite, and count how
many tests go red — the answer is one, and knowing which one is the lesson. Put it back. Then delete the
boolean guard from `overlap` and run again: one test fails with `DID NOT RAISE`, and the twenty-one that
pass would all have passed while the function returned a grid of nothing but `True`. A test you have never
seen fail is not yet a test (Principle 7).

```bash
uv run python -m pytest -q tests/test_chores.py
./m depth 24
./m check
```

---

## §6 Request budget

| Item | Count | Cost |
|---|---|---|
| Model calls | 0 | £0 |
| Network requests | 0 — NumPy was installed on Day 20 | £0 |
| Live API keys used | none | £0 |
| Data downloaded | none; the forty-tick chart is written by hand in §3 | £0 |

**Zero model calls and zero network today** (Principle 5). The three timing comparisons — the hand-written
matrix product, the integer-against-float product, and `solve` against `inv` — are the only things on this
day that take noticeable wall-clock, and the first of them takes several seconds by design.

---

## §7 Traps

- **`np.binary_repr(n, width=8)` raises** when `n` needs more than eight bits; `width` is an assertion, not
  padding ([1.1](parts/01-bits/1.1-a-number-is-switches.md)).
- **A boolean array and an integer array of ones and zeros index completely differently** — one selects,
  one looks up positions ([1.1](parts/01-bits/1.1-a-number-is-switches.md)).
- **`&` binds more tightly than `<` and `>`**, so every comparison needs brackets or you get a truth-value
  error from an unrelated cause ([1.2](parts/01-bits/1.2-the-four-bitwise-ufuncs.md)).
- **`~` on an integer array gives `-x - 1`**, so a mask built from `~counts` is all truthy and selects every
  row ([1.3](parts/01-bits/1.3-tilde-on-bool-and-int.md)).
- **`~counts` used as an index returns real values from the wrong rows** on a large array and raises on a
  small one ([1.3](parts/01-bits/1.3-tilde-on-bool-and-int.md)).
- **A left shift silently drops the top bits**, so `200 << 1` in a `uint8` is 144
  ([1.4](parts/01-bits/1.4-shifts-and-the-bit-that-fell-off.md)).
- **`>>` on a signed integer rounds towards negative infinity**, so `-5 >> 1` is `-3` and `int(-5/2)` is
  `-2` ([1.4](parts/01-bits/1.4-shifts-and-the-bit-that-fell-off.md)).
- **`flags & FLAG == 1` is a bug for every flag except the first**, because the test returns the flag's own
  value ([1.5](parts/01-bits/1.5-a-bitmask.md)).
- **`np.uint8(1) << np.uint8(8)` is `0` with no error**, so the ninth flag can be set and tested and does
  nothing ([1.5](parts/01-bits/1.5-a-bitmask.md)).
- **`np.packbits` fills from the most significant bit** while `1 << n` counts from the least — two
  conventions for the same eight positions ([1.6](parts/01-bits/1.6-packbits.md)).
- **`np.unpackbits` without `count=` returns a multiple of eight**, so up to seven phantom `False` values
  come back ([1.6](parts/01-bits/1.6-packbits.md)).
- **The shape and bit order do not survive packing** and must be stored alongside the bytes
  ([1.6](parts/01-bits/1.6-packbits.md)).
- **A text array's width is set by the longest string present when it was built**, and a longer assignment
  later is truncated silently ([2.1](parts/02-strings/2.1-fixed-width-text.md)).
- **A truncated value can still be a valid value** — `"USA"` cut to `"US"` is a different real country
  ([2.1](parts/02-strings/2.1-fixed-width-text.md)).
- **An array has no string methods**; `arr.lower()` raises and `np.strings.lower(arr)` is the call
  ([2.2](parts/02-strings/2.2-np-strings.md)).
- **Some `np.strings` functions are ufuncs and some are not**, so `out=` is available for `add` and not for
  `lower` ([2.2](parts/02-strings/2.2-np-strings.md)).
- **`np.strings.find` returns `-1` for absent**, which is truthy, while position `0` is falsy
  ([2.2](parts/02-strings/2.2-np-strings.md)).
- **Writing a string result back into its source array truncates it**
  ([2.2](parts/02-strings/2.2-np-strings.md)).
- **A text filter that matches nothing is indistinguishable from an empty period** unless you also check
  how many rules matched ([2.3](parts/02-strings/2.3-comparison-is-not-a-match.md)).
- **Normalising one side of a comparison and not the other is worse than normalising neither**
  ([2.3](parts/02-strings/2.3-comparison-is-not-a-match.md)).
- **Two strings can look identical and compare unequal** when an accent is a combining mark
  ([2.3](parts/02-strings/2.3-comparison-is-not-a-match.md)).
- **`object` dtype reports only its pointers in `nbytes`** and will hold a `None` without complaint
  ([2.4](parts/02-strings/2.4-where-text-does-not-belong.md)).
- **Re-deriving a vocabulary per dataset shifts every code above a missing category**
  ([2.4](parts/02-strings/2.4-where-text-does-not-belong.md)).
- **`@` on booleans accumulates in boolean and saturates to `True`**, returning a grid with no information
  and no error ([3.1](parts/03-matmul/3.1-a-dot-product-is-a-total.md)).
- **`*` and `@` both run on square matrices and give different answers of the same shape**
  ([3.2](parts/03-matmul/3.2-matmul-by-hand.md)).
- **`A @ v` and `A @ v[:, None]` differ by a trailing axis** that propagates into every later broadcast
  ([3.2](parts/03-matmul/3.2-matmul-by-hand.md)).
- **`np.dot` on 3-D input crosses every batch entry with every other**, giving batch-squared results with
  no error — and the shapes are indistinguishable at batch size 1
  ([3.3](parts/03-matmul/3.3-at-matmul-and-dot.md)).
- **An integer matrix product does not go to BLAS** and was about thirty times slower in a measurement
  ([3.4](parts/03-matmul/3.4-the-measured-gap.md)).
- **`.T` reverses every axis**, so batched code needs `swapaxes(-1, -2)` — and the bug hides when the batch
  size equals a matrix dimension ([3.5](parts/03-matmul/3.5-stacks-of-matrices.md)).
- **`np.max` is a reduction and `np.maximum` is elementwise**, and confusing them in an activation surfaces
  a layer later ([3.6](parts/03-matmul/3.6-every-neural-layer.md)).
- **Without an activation, stacked layers collapse into a single matrix**
  ([3.6](parts/03-matmul/3.6-every-neural-layer.md)).
- **A transposed `A` solves cleanly and returns plausible wrong numbers**, and only the substitution check
  catches it ([4.1](parts/04-linalg/4.1-three-trips-three-prices.md)).
- **`inv(A) @ b` does about three times the work of `solve(A, b)`** and accumulates more error
  ([4.2](parts/04-linalg/4.2-solve-and-never-inv.md)).
- **Dividing by a norm needs `keepdims=True`**, and on a square array the version without it normalises the
  wrong axis silently ([4.3](parts/04-linalg/4.3-norm.md)).
- **An all-zero row has zero length**, so normalising gives `nan` that spreads through every score
  ([4.3](parts/04-linalg/4.3-norm.md)).
- **A determinant threshold is not a check**, because the determinant scales with the entries
  ([4.4](parts/04-linalg/4.4-singular-and-the-error.md)).
- **`lstsq` returns an empty `residuals` array for an exact fit**, not zero
  ([4.5](parts/04-linalg/4.5-lstsq.md)).
- **The underdetermined case does not raise** — it returns a perfect, arbitrary fit
  ([4.5](parts/04-linalg/4.5-lstsq.md)).
- **An ill-conditioned system solves cleanly and returns noise**, and only `np.linalg.cond` says so
  ([4.6](parts/04-linalg/4.6-conditioning.md)).
- **Forming `AᵀA` squares the condition number**, which is why the textbook regression formula is the wrong
  implementation ([4.6](parts/04-linalg/4.6-conditioning.md)).

---

## §8 Verify before you code

Every one of these was fetched on 2026-09-02 and returned `200`. Read the first three before writing any
code; open the rest when a part points you at them.

- Bitwise operations, all of them in one table —
  <https://numpy.org/doc/stable/reference/routines.bitwise.html>
- String operations, and the note on `numpy.char` being legacy —
  <https://numpy.org/doc/stable/reference/routines.strings.html>
- Linear algebra routines, all of them in one table —
  <https://numpy.org/doc/stable/reference/routines.linalg.html>
- `np.packbits`, including `bitorder=` —
  <https://numpy.org/doc/stable/reference/generated/numpy.packbits.html>
- `np.binary_repr` — <https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html>
- `np.bitwise_count` — <https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html>
- `np.matmul`, including the batching rule —
  <https://numpy.org/doc/stable/reference/generated/numpy.matmul.html>
- `np.linalg.solve` — <https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html>
- `np.linalg.lstsq`, including all four return values —
  <https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html>
- `np.linalg.norm`, including which `ord` values are valid for vectors and for matrices —
  <https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html>
- `np.linalg.cond` — <https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html>
- `np.linalg.matrix_rank` —
  <https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html>

Today needs no separate dated source; every claim here is checkable against the pages above and against the
measurements in the parts. The one convention worth naming rather than citing is **two's complement**, the
way signed integers are represented — top bit set means negative, and the rest counts backwards from zero.
It is why `~x` gives `-x - 1` ([1.3](parts/01-bits/1.3-tilde-on-bool-and-int.md)) and why an `int8` runs
from −128 to 127 rather than −127 to 127. Confirm it for yourself rather than taking it on trust:
`np.binary_repr(-5, width=8)` prints the actual stored bits, and `np.iinfo(np.int8)` prints the limits that
follow from them.

---

## §9 Say it in an interview

"Two things on this day and they look unrelated until you see what they share. The first is that a NumPy
boolean costs a whole byte to store one yes-or-no, so `np.packbits` gives an exact eightfold saving — and
the things that do not survive packing are the shape, the original length and the bit order, so all three
have to travel with the bytes. Without `count=` on the way back you get a multiple of eight, which means up
to seven phantom `False` values that are indistinguishable from real ones. That is a storage decision and
the same reasoning turns up as a bitmask: eight flags in one integer, tested with `flags & FLAG != 0` —
compared against zero, never against one, because the test returns the flag's own value and only the first
flag has the value one. And the bit order is a **storage format**, so reordering an enum silently rewrites
every value already on disk.

The second half is the matrix product, and the thing worth saying is what it is. Entry `(i, j)` of `A @ B`
is row `i` of `A` dotted with column `j` of `B`, so `(n, k)` times `(k, m)` gives `(n, m)` and the shared
dimension vanishes. That is a neural network layer: `maximum(inputs @ weights + bias, 0)`, where the bias
is one number per output broadcast across the batch, and the activation is there because without it two
stacked layers collapse into one matrix. I wrote the triple loop out by hand and measured it against `@` on
300-by-300 matrices — about twelve thousand times, and only a factor of a hundred of that is Python being
slow; the rest is cache-blocked memory access and several multiplications per instruction. The detail most
people miss is that there is no integer BLAS, so an integer matrix product silently takes a fallback path
that was about thirty times slower for me — casting to `float64` first is a real win.

The failures are the interesting part. `@` on booleans accumulates in boolean and saturates, so a whole
overlap grid comes back as `True` with no error. `np.dot` on 3-D input crosses every batch entry with every
other rather than batching, which is indistinguishable from `matmul` at batch size 1 and is batch-times the
memory at 64. And on the linear algebra side, a transposed `A` solves cleanly and returns plausible wrong
prices, so every `solve` gets a substitution check; `lstsq` returns an **empty** residual array for an exact
fit rather than zero; and an ill-conditioned system does not raise at all — it returns an answer whose last
several digits are noise, and the only signal is `np.linalg.cond`. A condition number of ten to the k costs
about k of your sixteen digits, and scaling columns to comparable ranges can recover ten of them, which is a
reason feature scaling matters that has nothing to do with gradient descent."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m depth 24` passes, and `./m check` is green.
Done is defined by understanding and by green checks, never by elapsed time (Principle 17).

The three questions to answer out loud before you call it finished:

1. Name the three things that do not survive `np.packbits`, and say what goes wrong for each one if you
   forget to store it.
2. State the matrix product's shape rule and say why it is that rule rather than an arbitrary convention.
   Then say what a neural network layer is in one line.
3. A system solves without complaint and the answer changes completely when one input moves by a
   ten-thousandth. Say what to measure, what the number means in digits, and the two fixes in order.
