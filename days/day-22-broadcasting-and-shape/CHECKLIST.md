# Day 22 — CHECKLIST

**IDs covered:** `NP-04`, `NP-05` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 22, in [`parts/`](parts/)

> `./m done 22` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **Two of today's traps do not raise.** A per-row statistic without `keepdims=True` and a `.T` on more
> than two axes both produce arrays of the right shape and the wrong contents. Every box below that
> says "on a non-square array" exists because of them.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_shape.py -v && ./m depth 22 && ./m check
```

Expected: fifteen tests in `test_shape.py` passing, a green depth report for day 22, then a green
gate.

---

## Setup

- [ ] Confirmed `numpy==2.5.2` is still the pin, with `uv run python scripts/check_pins.py | grep -i numpy`
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Created `data/steps/month-flat.txt` with twenty-eight lines, one number each
- [ ] Ran `./m scaffold 22` and created `src/setu/shape.py` and `tests/test_shape.py`
- [ ] Can say why Thursday of week one is `9000` today and was a hole on Days 20 and 21

---

## Section 1 — broadcasting

- [ ] Read [1.1 — one number against twenty-eight](parts/01-broadcasting/1.1-adding-one-number-to-every-day.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the rule in three lines](parts/01-broadcasting/1.2-the-rule-in-three-lines.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — a row against a table](parts/01-broadcasting/1.3-a-row-against-a-table.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — keepdims and the column](parts/01-broadcasting/1.4-keepdims-and-the-column.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — a stride of zero](parts/01-broadcasting/1.5-no-data-is-copied.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — reading the error](parts/01-broadcasting/1.6-reading-the-broadcast-error.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.7 — the broadcast that ate the memory](parts/01-broadcasting/1.7-the-broadcast-that-ate-the-memory.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Timed a comprehension over a million values against the vectorised version, and wrote down what
      the ratio was measured **against**
- [ ] Measured the in-place form against the allocating one and recorded both times and the temporaries
- [ ] Applied the three-step rule on paper to five pairs of shapes before running `np.broadcast_shapes`
- [ ] Mean-centred 60 000 rows and timed it against the row-by-row loop
- [ ] Confirmed the column means of the centred array are zero and the row means are not
- [ ] Produced the `(4,7) (4,)` error deliberately and fixed it two ways — `keepdims` and `np.newaxis`
- [ ] Ran the `keepdims` comparison on a **square** array and recorded that neither version raised
- [ ] Printed the strides of a `np.broadcast_to` result and found the zero
- [ ] Confirmed a broadcast array is read-only, and read the `ValueError`
- [ ] Compared `nbytes` with the real allocation using `tracemalloc`
- [ ] Produced all six shape error messages and can say which word identifies each operation
- [ ] Computed the memory of an `(n, n)` result for n = 1 000, 20 000 and 200 000 **before** running
      anything
- [ ] Triggered a real `_ArrayMemoryError` and read the shape and size in the message
- [ ] Reduced a pairwise computation in blocks and confirmed the answer matched

---

## Section 2 — reshape

- [ ] Read [2.1 — same block, new shape](parts/02-reshape/2.1-same-block-new-shape.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `-1` and the division](parts/02-reshape/2.2-minus-one.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — the `order` argument](parts/02-reshape/2.3-the-order-argument.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `ravel` and `flatten`](parts/02-reshape/2.4-ravel-and-flatten.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — when reshape must copy](parts/02-reshape/2.5-when-reshape-must-copy.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed the strides before and after a reshape and can say where the 56 came from
- [ ] Wrote through a reshaped array and confirmed the original changed
- [ ] Listed every shape twenty-eight values can take and confirmed all of them are views
- [ ] Produced both `-1` errors: two unknowns, and a total that does not divide
- [ ] Wrote a reshape that survives the data doubling in size, and one that does not
- [ ] Printed a `(3, 4)` array in C order and in F order and can say where each value went
- [ ] Round-tripped a buffer through the wrong `order` and looked at the scrambled result
- [ ] Confirmed `ravel` and `flatten` give identical values and differ in `shares_memory`
- [ ] Timed `ravel` on a contiguous array against `ravel` on a transposed one
- [ ] Built the six-row contiguity table and confirmed the flag predicts every answer
- [ ] Used `np.reshape(..., copy=False)` and read the refusal
- [ ] Saw the `DeprecationWarning` for `arr.shape = ...` with `-W always`, and can say why it is hidden
      by default

---

## Section 3 — transpose

- [ ] Read [3.1 — `.T`, the axes swapped](parts/03-transpose/3.1-t-the-axes-swapped.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `transpose`, `swapaxes`, `moveaxis`](parts/03-transpose/3.2-transpose-and-swapaxes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — contiguity](parts/03-transpose/3.3-contiguity-and-the-speed-you-lose.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed `month.T` swaps the strides and allocates nothing
- [ ] Confirmed `.T` on a one-dimensional array changes nothing, and found the right way to make a
      column
- [ ] Wrote through a transpose and watched the original change
- [ ] Predicted the shapes of five rearrangements of a `(2, 3, 4)` cube before running them
- [ ] Converted an image between channels-first and channels-last and back, and confirmed the round
      trip is exact
- [ ] Confirmed `.T` on that image gives a different array from `moveaxis`, with no error
- [ ] Built the five-operation contiguity table and can say which two rows contradict the folklore
- [ ] Confirmed `np.ascontiguousarray` on a C-contiguous array returns the **same object**

---

## Section 4 — joining and splitting

- [ ] Read [4.1 — `concatenate`](parts/04-joining-and-splitting/4.1-concatenate.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — `stack` against `concatenate`](parts/04-joining-and-splitting/4.2-stack-versus-concatenate.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `split` and the uneven piece](parts/04-joining-and-splitting/4.3-split-and-the-uneven-last-piece.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — `np.newaxis` and `expand_dims`](parts/04-joining-and-splitting/4.4-newaxis-and-expand-dims.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — growing an array in a loop](parts/04-joining-and-splitting/4.5-growing-an-array-in-a-loop.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed `concatenate` never returns a view, and that the result is the size of both inputs
- [ ] Produced the "must match exactly" error and can say why nothing was broadcast
- [ ] Concatenated an integer array with a text array and looked at the dtype
- [ ] Produced the same fourteen numbers as `(14,)` and as `(2, 7)`, and said which question each
      answers
- [ ] Confirmed `vstack` behaves differently for one-dimensional and two-dimensional input
- [ ] Split an array and confirmed every piece is a view
- [ ] Produced the "does not result in an equal division" error and fixed it with `array_split`
- [ ] Converted a list of sizes into cut points and confirmed the pieces came out the intended lengths
- [ ] Kept one piece of a split array and measured what `base.nbytes` says is still alive
- [ ] Made a `(7,)` array into a row and into a column, and confirmed both are views
- [ ] Ran a bare `.squeeze()` on a batch of one and on a batch of ten, and recorded the difference
- [ ] Timed the growing loop against one join at 100, 200, 400 and 800 chunks and watched the **ratio**
      grow
- [ ] Measured the peak memory of the growing loop against the one-shot join

---

## Section 5 — the module

- [ ] Read [5.1 — mean-centring the month](parts/05-the-module/5.1-mean-centring-the-month.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — the test that can go red](parts/05-the-module/5.2-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question

---

## Build

- [ ] `src/setu/shape.py` exists and every `TODO(me)` is resolved by your own code
- [ ] `DAYS_PER_WEEK` is named once and used everywhere the 7 appears
- [ ] `as_weeks` checks the shape and the divisibility, and its message says how many are left over
- [ ] `as_weeks` returns a view, and the docstring says so
- [ ] `centre_within_week` uses `keepdims=True`, with the version without it in a comment and a note
      on what each does to a `(4, 7)` and a `(7, 7)` array
- [ ] `DayProfile.fit` computes means along the axis that gives one per **day**, using `nanmean`
- [ ] `DayProfile.fit` refuses fewer than two weeks
- [ ] `DayProfile.apply` checks against the learned width and returns a new array
- [ ] The `fit`/`apply` split is written down as the reason the leak cannot be expressed
- [ ] `stack_months` makes exactly one `np.concatenate` call, outside any loop
- [ ] `stack_months` returns `(0, 7)` for an empty list rather than raising
- [ ] Added `shape` to `LAYERS` in `src/setu/layout.py`
- [ ] `uv run ruff check src/setu/shape.py` and `uv run ruff format --check src/setu/shape.py` are both
      clean

---

## Tests

- [ ] `tests/test_shape.py` exists and every `TODO(me)` is resolved by your own assertions
- [ ] The fixture is **not square**, and you can say what a square one would fail to catch
- [ ] The fixture returns a fresh copy per test
- [ ] The view promise is asserted with `np.shares_memory` **and** by writing through it
- [ ] Row centring is asserted with `np.testing.assert_allclose` and an `atol=`
- [ ] There is a test with both halves: something that must be zero and something that must not
- [ ] The leakage test asserts that fitting on three weeks differs from fitting on four
- [ ] Every `pytest.raises` has a `match=`, and the one with brackets uses a raw string
- [ ] Tried that pattern **without** the raw string and recorded what pytest said
- [ ] All fifteen tests pass
- [ ] **Broke it on purpose:** changed `keepdims=True` to a mean along `axis=0`
- [ ] Confirmed exactly two tests went red and read `assert_allclose`'s printed arrays
- [ ] Put it back and confirmed fifteen green again
- [ ] **Broke it a second time:** changed the fixture to `(7, 7)` and re-broke `keepdims`
- [ ] Counted how many tests still passed with the square fixture, and wrote the number down
- [ ] Ran the whole suite offline with no network available

---

## Budget

- [ ] Model calls this day: **0** — confirmed, not assumed (Principle 5)
- [ ] Network requests: **0** — nothing new was installed
- [ ] No API key was read, and `.env` was not touched
- [ ] The whole test suite runs with the network off

---

## Close

- [ ] `./m depth 22` passes with no failures
- [ ] `./m check` is green — ruff, format, lesson blocks, offline pytest, depth
- [ ] `./m tracker` regenerated `docs/TRACKER.md` and `days/INDEX.md`, and both are committed
- [ ] Can answer the three questions in the hub's §10 out loud, without notes
- [ ] Can give the interview paragraph from §9 in your own words
- [ ] Committed with `./m done 22`
