# Day 20 — CHECKLIST

**IDs covered:** `NP-01`, `NP-02` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 20, in [`parts/`](parts/)

> `./m done 20` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **This is the first day of Phase 3.** Everything here is assumed by Days 21 to 25, and the phase
> gate on Day 25 — a vectorised stats module beating a loop by at least 50× — is only reachable
> because of what today establishes.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_steps.py -v && ./m depth 20 && ./m check
```

Expected: nine tests in `test_steps.py` passing, a green depth report for day 20, then a green gate.

---

## Setup

- [ ] `uv add numpy==2.5.2`, with `==`, never `>=`
- [ ] Confirmed `pyproject.toml` gained the exact pin and that `uv.lock` changed, and committed both
- [ ] Ran `uv run python scripts/check_pins.py | grep -i numpy` and confirmed no drift
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Created `data/steps/week-01.txt` with the seven lines, dash included
- [ ] Ran `./m scaffold 20` and created `src/setu/steps.py` and `tests/test_steps.py`
- [ ] Can say what the dash on line four means, and why it is not a zero

---

## Section 1 — the block

- [ ] Read [1.1 — a list of boxes](parts/01-the-block/1.1-a-list-of-boxes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the six questions](parts/01-the-block/1.2-shape-dtype-and-the-rest.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — one block, and strides](parts/01-the-block/1.3-one-block-and-strides.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — a million numbers, measured](parts/01-the-block/1.4-a-million-floats-measured.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `nbytes` for a seven-element array and the true byte cost of the same seven-element list
- [ ] Watched `arr * 2` double and `list * 2` duplicate, and can say why both are correct
- [ ] Built a ragged list and read the `inhomogeneous shape` error in full
- [ ] Put one string in a list of numbers and confirmed the whole array became `<U21`
- [ ] Printed `len`, `.size` and `.shape` for a `(3, 4)` array and can say why the first is not 12
- [ ] Printed `.strides` for `int64`, `float32` and `int8` arrays and can say why they differ
- [ ] Recovered one element by hand from `tobytes()` using the stride formula
- [ ] Confirmed `grid.T` swaps the strides and is no longer C-contiguous
- [ ] Confirmed `grid.T.ravel().base is None` and `grid.ravel().base is None` disagree
- [ ] Measured the memory ratio for a million integers and wrote the number down
- [ ] Measured three speedups — against a hand loop, against `sum()`, and for an elementwise multiply
- [ ] Ran the same measurement five times and recorded the spread, not one number
- [ ] Timed `np.array(lst).sum()` including the conversion and can say when NumPy is a loss

---

## Section 2 — dtypes

- [ ] Read [2.1 — a dtype is a promise](parts/02-dtypes/2.1-a-dtype-is-a-promise.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — the silent wrap](parts/02-dtypes/2.2-integers-and-the-silent-wrap.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — floats, `NaN`, precision](parts/02-dtypes/2.3-floats-nan-and-precision.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `astype` and the copy](parts/02-dtypes/2.4-astype-and-the-copy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — NEP 50](parts/02-dtypes/2.5-nep-50-and-the-python-number.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.6 — the removed names](parts/02-dtypes/2.6-the-names-that-were-removed.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the six-case inference table and predicted all six dtypes before looking
- [ ] Stated `dtype=np.int64` on text that will not parse and read the `ValueError`
- [ ] Built an `object` array of numbers and can say what performance property was lost
- [ ] Cast decimal data to `int64` and confirmed it truncated rather than rounded
- [ ] Printed `np.iinfo` for four integer widths rather than remembering the limits
- [ ] Multiplied an `int16` step-count array by 4 and counted the negative results
- [ ] Confirmed `small.sum()` is safe and `small * 4` is not, and can say why
- [ ] Subtracted 10 from a `uint8` zero and read the answer out loud
- [ ] Forced `big.sum(dtype=np.int32)` on three billion and watched it go negative
- [ ] Confirmed `np.nan == np.nan` is `False` and that `arr == np.nan` finds nothing
- [ ] Compared `arr.mean()` with `np.nanmean(arr)` on an array with one hole
- [ ] Added `np.float32(16_777_216) + 1` and confirmed nothing changed
- [ ] Confirmed `np.isclose(0.1 + 0.2, 0.3)` and `0.1 + 0.2 == 0.3` disagree
- [ ] Cast an array containing `np.nan` to `int64` and read the sentinel it produced
- [ ] Confirmed `astype(np.int64, copy=False)` returned **the same object**, then wrote to it
- [ ] Tried `casting="safe"` on a narrowing cast and read the `TypeError`
- [ ] Confirmed `(float32_array * 2.0).dtype` is `float32` and can say what NumPy 1 did instead
- [ ] Triggered `OverflowError: Python integer 1000 out of bounds for int8`
- [ ] Confirmed `np.seterr(over="raise")` does **not** catch an integer array overflow
- [ ] Checked twelve removed names with `hasattr` and got twelve `GONE`
- [ ] Read both kinds of removal message and can name the replacement for the unhelpful four
- [ ] Added `NPY` to the ruff `select` list and ran `ruff check --select NPY201 .`

---

## Section 3 — creating

- [ ] Read [3.1 — `np.array`](parts/03-creating/3.1-np-array-and-what-it-infers.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `zeros`, `ones`, `full`, `empty`](parts/03-creating/3.2-zeros-ones-full-and-empty.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — `arange`](parts/03-creating/3.3-arange-and-the-float-step.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — `linspace`](parts/03-creating/3.4-linspace.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — `_like`, `eye`, `diag`](parts/03-creating/3.5-like-and-the-identity.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built 1-D, 2-D and 3-D arrays from nested lists and predicted each shape first
- [ ] Confirmed `np.asarray(existing) is existing` and `np.array(existing) is existing` differ
- [ ] Ran `np.array(x, copy=False)` on a list and read the NumPy 2 `ValueError` in full
- [ ] Built an array with `np.fromiter` from a generator and can say why `dtype=` is compulsory
- [ ] Confirmed `np.array("monday")` gives a zero-dimensional array and that `len()` fails on it
- [ ] Wrote `np.zeros(4, 7)` on purpose and read `Cannot interpret '7' as a data type`
- [ ] Confirmed `np.zeros(7)` is `float64` and can say why that is the default
- [ ] Allocated and freed 800 KB, then printed `np.empty(100_000)[:6]` and saw the debris
- [ ] Ran the `np.empty` demonstration twice and confirmed the values changed
- [ ] Filled four of five slots of an `np.empty` array and read the fifth
- [ ] Compared `arange`'s predicted and actual length for four different decimal stops
- [ ] Printed `repr` of every element of `np.arange(0, 0.7, 0.1)` and found the two that lie
- [ ] Confirmed `np.arange(10, 0)` returns an empty array with no error
- [ ] Confirmed `np.linspace(0, 1, 10)` and `np.linspace(0, 1, 11)` give different gaps
- [ ] Used `retstep=True` and read the step it chose
- [ ] Passed values instead of exponents to `logspace` and looked at what came back
- [ ] Confirmed `np.linspace(0, 1, 4, dtype=np.int64)` collapses three of four values
- [ ] Confirmed `np.zeros_like` inherits the dtype and `np.zeros(shape)` does not
- [ ] Ran `np.full_like(int_array, np.nan)` and read the sentinel plus its `RuntimeWarning`
- [ ] Compared `grid @ eye`, `grid @ ones` and `grid * eye` and can say what each did

---

## Section 4 — randomness, seeded

- [ ] Read [4.1 — `default_rng`](parts/04-random/4.1-default-rng-the-generator.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the seed is part of the result](parts/04-random/4.2-the-seed-is-part-of-the-result.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — passing the generator](parts/04-random/4.3-passing-the-generator.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed two generators with the same seed give the same first draw and then diverge
- [ ] Confirmed the same seed gives **different** numbers in the legacy API and the `Generator` API
- [ ] Called `rng.randint` on a `Generator` and read the `AttributeError`
- [ ] Inserted a stray `np.random.rand(1)` between two seeded draws and watched the results move
- [ ] Called `rng.integers(0, 10)` without `size=` and noticed you got one number, not ten
- [ ] Ran five seeds through the same sampling code and wrote down the spread of the means
- [ ] Compared two identical "treatments" on one seed each and saw a difference appear from nothing
- [ ] Repeated that comparison on twenty shared seeds and confirmed the difference vanished
- [ ] Wrote a function taking a seed and one taking a generator, and can say which repeats itself
- [ ] Built three generators from one seed and confirmed all three produce identical streams
- [ ] Used `parent.spawn(3)` and confirmed the three children differ and the whole set replays
- [ ] Ran a `ProcessPoolExecutor` whose workers each seed themselves, and saw identical output
- [ ] Can say why `seed + i` for worker *i* is better than one seed and still not right

---

## Section 5 — the module

- [ ] Read [5.1 — typed on purpose](parts/05-the-module/5.1-reading-the-week-typed-on-purpose.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — the test that can go red](parts/05-the-module/5.2-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question

---

## Build — `src/setu/steps.py`

- [ ] `STEP_DTYPE` chosen, with the reasoning written beside it as a comment
- [ ] Checked that choice against `np.iinfo` rather than against memory
- [ ] `MISSING` is a named constant, not a repeated string literal
- [ ] `Summary` is `frozen=True, slots=True` and every field is a plain `int` or `float`
- [ ] `load_counts` passes an explicit `dtype=` and can explain what happens without it
- [ ] `load_counts` rejects a negative count, and the message contains the offending value
- [ ] `to_whole` range-checks **before** casting, not after
- [ ] `to_whole` allocates with `np.full` and the sentinel, never with `np.empty`
- [ ] `to_whole` rounds with `np.rint` before the cast, and the comment says why
- [ ] Wrote down why `-1` is a usable sentinel here and would not be for a temperature column
- [ ] `summarise` refuses an integer array with a `TypeError`
- [ ] `summarise` reports `recorded` alongside `days`
- [ ] `summarise` uses the `nan`-aware reductions, and a comment names the decision that makes
- [ ] Added `steps` to `LAYERS` in `src/setu/layout.py`
- [ ] Ran `uv run ruff format days/day-20-arrays-and-dtypes/ src/setu/steps.py`
- [ ] Ran `uv run ruff check src/setu/steps.py` and fixed rather than silenced every finding

---

## Eval — `tests/test_steps.py`

- [ ] Nine tests written, all passing
- [ ] No computed float compared with `==` anywhere in the file
- [ ] Every `pytest.raises` carries a `match=`
- [ ] The bad-input cases are `@pytest.mark.parametrize`d, not a loop inside one test
- [ ] The memory test uses a **seeded** generator and asserts a ratio, not a byte count
- [ ] `type(summary.total) is int`, not `isinstance`, and can say why that matters
- [ ] **Broke it on purpose:** changed the `np.nan` in `load_counts` to `0`
- [ ] Counted how many tests went red and read the messages
- [ ] Confirmed one of the failures names the actual bug rather than a symptom
- [ ] Put the line back and confirmed all nine green again
- [ ] Ran the whole suite offline with no network available

---

## Budget

- [ ] Model calls this day: **0** — confirmed, not assumed (Principle 5)
- [ ] Network requests: **1**, the `uv add` from PyPI
- [ ] No API key was read, and `.env` was not touched
- [ ] The whole test suite runs with the network off

---

## Close

- [ ] `./m depth 20` passes with no failures
- [ ] `./m check` is green — ruff, format, lesson blocks, offline pytest, depth
- [ ] `./m tracker` regenerated `docs/TRACKER.md` and `days/INDEX.md`, and both are committed
- [ ] Can answer the three questions in the hub's §10 out loud, without notes
- [ ] Can give the interview paragraph from §9 in your own words
- [ ] Committed with `./m done 20`
