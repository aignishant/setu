# Day 21 — CHECKLIST

**IDs covered:** `NP-03` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 23, in [`parts/`](parts/)

> `./m done 21` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **Today is the day the rest of Phase 3 rests on.** Day 22's reshape and transpose are views for the
> same reason a slice is, and Day 25's phase gate — a vectorised stats module beating a loop by at
> least 50× — is only safe because you can say which operations copy.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_select.py -v && ./m depth 21 && ./m check
```

Expected: eleven tests in `test_select.py` passing, a green depth report for day 21, then a green
gate.

---

## Setup

- [ ] Confirmed `numpy==2.5.2` is still the pin, with `uv run python scripts/check_pins.py | grep -i numpy`
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Created `data/steps/month-01.txt` with four lines of seven numbers, the `-1` included
- [ ] Ran `./m scaffold 21` and created `src/setu/select.py` and `tests/test_select.py`
- [ ] Can say why the missing day is `-1` here and was `np.nan` yesterday, in one sentence

---

## Section 1 — one element, and a range of them

- [ ] Read [1.1 — `arr[3]` and the negative index](parts/01-one-element/1.1-index-and-the-negative-index.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the comma a list cannot do](parts/01-one-element/1.2-the-comma-a-list-cannot-do.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — a slice keeps its axis](parts/01-one-element/1.3-slicing-one-axis.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — a whole column](parts/01-one-element/1.4-a-whole-column.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — the step and the reverse](parts/01-one-element/1.5-the-step-and-the-reverse.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — `...` and `np.newaxis`](parts/01-one-element/1.6-ellipsis-and-newaxis.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `type(week[0])` and confirmed it is a NumPy scalar, not a Python `int`
- [ ] Read the `IndexError` for a position past the end, in full, and noted that it names the axis
- [ ] Confirmed `month[1, 4]` and `month[1][4]` give the same value, and can say which one allocates
- [ ] Printed the shapes of `month[1]`, `month[1:2]` and `month[1:2, :]` and can say why they differ
- [ ] Confirmed a whole column is a view even though its values are 56 bytes apart
- [ ] Printed `.strides` for `month[::2]` and for `month[::-1]` and can say what a negative stride is
- [ ] Used `...` on a three-dimensional array and can say what it stood for
- [ ] Turned a `(7,)` row into a `(7, 1)` column with `np.newaxis` and confirmed it is still a view

---

## Section 2 — the view trap

- [ ] Read [2.1 — a slice does not copy](parts/02-the-view-trap/2.1-a-slice-does-not-copy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `base`, `shares_memory` and the flags](parts/02-the-view-trap/2.2-how-to-tell-base-and-shares-memory.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `.copy()` and when to pay](parts/02-the-view-trap/2.3-copy-and-when-to-pay.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — the function that changed its input](parts/02-the-view-trap/2.4-the-function-that-changed-its-input.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote to a slice, watched the parent change, and can say why no warning was possible
- [ ] Used all three checks on the same array — `base`, `np.shares_memory`, `flags` — and can say what
      each one answers
- [ ] Set `flags.writeable = False` on a view and read the `ValueError` in full
- [ ] Timed a view against a copy of the same thousand rows and wrote both numbers down
- [ ] Named, out loud, the four situations where a `.copy()` is worth paying for
- [ ] Wrote the same function twice — `filled` returning a new array, `fill` returning `None` — and can
      say which one a call site reads as safe
- [ ] Read the `_UFuncOutputCastingError` from `month[0] += 0.5` and can say why plain assignment does
      not raise it

---

## Section 3 — boolean masks

- [ ] Read [3.1 — a comparison makes an array](parts/03-boolean-masks/3.1-a-comparison-makes-an-array.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — indexing with a mask](parts/03-boolean-masks/3.2-indexing-with-a-mask.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — `&`, `|`, `~` and why `and` raises](parts/03-boolean-masks/3.3-and-or-not-and-why-and-raises.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — assigning through a mask](parts/03-boolean-masks/3.4-assigning-through-a-mask.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — the mask that matched nothing](parts/03-boolean-masks/3.5-the-mask-that-matched-nothing.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed a mask's `dtype`, `shape` and `nbytes` and can say why it is one byte per element
- [ ] Confirmed a mask is not a view of the array it came from
- [ ] Measured `mask.sum()` against `np.count_nonzero(mask)` on ten million values and wrote both down
- [ ] Confirmed `month[busy]` is flat and is a copy, and can say why both follow from the same fact
- [ ] Selected whole rows with a one-dimensional mask and can say why the result kept two axes
- [ ] Produced the "truth value ... is ambiguous" error in all three ways: `and`, a chained comparison,
      and missing brackets
- [ ] Confirmed `~` on an integer array does arithmetic rather than logic
- [ ] Wrote through a mask, confirmed the shape did not change, and confirmed `arr[mask][0] = 0` does
      nothing
- [ ] Assigned a float into an integer array through a mask and watched it truncate in silence
- [ ] Ran `sum`, `all`, `any`, `mean` and `max` on an empty selection and recorded all five behaviours
- [ ] Can say why `np.all` of an empty array is `True`, and why that is the wrong default for a check

---

## Section 4 — fancy indexing

- [ ] Read [4.1 — a list of positions](parts/04-fancy-indexing/4.1-a-list-of-positions.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — two index arrays](parts/04-fancy-indexing/4.2-two-index-arrays.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — basic or advanced](parts/04-fancy-indexing/4.3-fancy-indexing-always-copies.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — repeated positions and the lost update](parts/04-fancy-indexing/4.4-repeated-positions-and-the-lost-update.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — mixing a slice with a list](parts/04-fancy-indexing/4.5-mixing-a-slice-with-a-list.md), ran its check-yourself, answered its out-loud question
- [ ] Selected in an order of your own, with a repeat, and confirmed both are legal
- [ ] Indexed a flat array with a `(2, 2)` index array and can say where the result's shape came from
- [ ] Confirmed `month[(1, 2)]` and `month[[1, 2]]` differ, and can say which is which
- [ ] Wrote `month[rows, cols]` for pairs and `month[np.ix_(rows, cols)]` for the grid, and can say
      which rule turns the second into a grid
- [ ] Wrote `probs[np.arange(n), labels]` and can say what it is used for on Day 130
- [ ] Built the basic-versus-advanced table yourself and found the row where `base` and
      `shares_memory` disagree
- [ ] Measured a sorted gather against a shuffled one and wrote the ratio down
- [ ] Ran `tally[walks] += 1` on positions with repeats, confirmed the total is wrong, then fixed it
      with `np.add.at` and with `np.bincount`
- [ ] Predicted all six shapes in 4.5's mechanism before running it, and marked how many you got right

---

## Section 5 — in anger

- [ ] Read [5.1 — the leak a view causes](parts/05-in-anger/5.1-the-leak-a-view-causes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — view or copy, on purpose](parts/05-in-anger/5.2-view-or-copy-on-purpose.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.3 — the test that can go red](parts/05-in-anger/5.3-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question
- [ ] Ran the `tracemalloc` measurement and wrote down both numbers: bytes kept, bytes held
- [ ] Confirmed `del big` does not free an array that a view still points at
- [ ] Wrote the four-line "refusing to cache a view" guard and watched it raise

---

## Build

- [ ] `src/setu/select.py` exists and every `TODO(me)` is resolved by your own code
- [ ] `MISSING` is named once, and the comment says what makes it safe for this column
- [ ] `week` returns a read-only view; `week_copy` returns a detached array; the docstrings say so
- [ ] Confirmed by hand that `month[index].flags.writeable = False` protects nothing, and that your
      `week` does
- [ ] `usable` returns a mask, and the three conditions are named on three lines
- [ ] `select_usable`'s three counts partition the input — checked on data where all three are non-zero
- [ ] `fill_missing` guards the empty case before computing a mean
- [ ] `fill_missing` rounds before casting, and the comment says what truncation would cost
- [ ] `fill_missing` leaves the caller's array alone unless `out=` is passed by name
- [ ] `tally_visits` uses `np.bincount`, range-checks its positions, and carries the wrong version in a
      comment with the number it gives
- [ ] Added `select` to `LAYERS` in `src/setu/layout.py`
- [ ] `uv run ruff check src/setu/select.py` and `uv run ruff format --check src/setu/select.py` are
      both clean

---

## Tests

- [ ] `tests/test_select.py` exists and every `TODO(me)` is resolved by your own assertions
- [ ] The `month` fixture returns a fresh copy, and you can name the test that would corrupt the others
      without it
- [ ] Every `pytest.raises` has a `match=`, and every pattern is from your message, not NumPy's
- [ ] The view promise is asserted with `np.shares_memory`, not by comparing values
- [ ] The "did not touch my array" test uses a real `.copy()` for `before`
- [ ] The `out=` test asserts `is`, not `==`
- [ ] The tally test asserts the sum as well as the exact counts
- [ ] All eleven tests pass
- [ ] **Broke it on purpose:** deleted `view.flags.writeable = False` from `week`
- [ ] Confirmed exactly one test went red, and read the flags block in the failure output
- [ ] Put the line back and confirmed eleven green again
- [ ] **Broke it a second time:** replaced `np.bincount` with `counts[positions] += 1`
- [ ] Counted how many tests went red and can say which assertion did the catching
- [ ] Ran the whole suite offline with no network available

---

## Budget

- [ ] Model calls this day: **0** — confirmed, not assumed (Principle 5)
- [ ] Network requests: **0** — NumPy was installed yesterday and nothing new was added
- [ ] No API key was read, and `.env` was not touched
- [ ] The whole test suite runs with the network off

---

## Close

- [ ] `./m depth 21` passes with no failures
- [ ] `./m check` is green — ruff, format, lesson blocks, offline pytest, depth
- [ ] `./m tracker` regenerated `docs/TRACKER.md` and `days/INDEX.md`, and both are committed
- [ ] Can answer the three questions in the hub's §10 out loud, without notes
- [ ] Can give the interview paragraph from §9 in your own words
- [ ] Committed with `./m done 21`
