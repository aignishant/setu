# Day 24 — CHECKLIST

**IDs covered:** `NP-08`, `NP-09` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 24, in [`parts/`](parts/)

> `./m done 24` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **Almost every trap today is silent.** `~` on an integer, `@` on booleans, `np.dot` on a batch, a
> truncated string, a normalised comparison against an unnormalised vocabulary, a transposed `solve`, an
> ill-conditioned fit — none of them raises. Every box below that says "record what it printed" exists
> because of one of them.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_chores.py -v && ./m depth 24 && ./m check
```

Expected: twenty tests in `test_chores.py` passing, a green depth report for day 24, then a green gate.

---

## Setup

- [ ] Confirmed `numpy==2.5.2` is still the pin, with `uv run python scripts/check_pins.py | grep -i numpy`
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Ran `./m scaffold 24` and created `src/setu/chores.py` and `tests/test_chores.py`
- [ ] Wrote the forty-tick chart to `data/chores/week.npy` and saw `40` bytes against `5` packed
- [ ] Ran `np.show_config()` and wrote down which linear algebra library NumPy is using

---

## Section 1 — bits

- [ ] Read [1.1 — a number is a row of switches](parts/01-bits/1.1-a-number-is-switches.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the four bitwise ufuncs](parts/01-bits/1.2-the-four-bitwise-ufuncs.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `~` on a bool and on an int](parts/01-bits/1.3-tilde-on-bool-and-int.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `<<` and `>>`](parts/01-bits/1.4-shifts-and-the-bit-that-fell-off.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — a bitmask](parts/01-bits/1.5-a-bitmask.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — `packbits` and `unpackbits`](parts/01-bits/1.6-packbits.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed the bit rows for 0, 1, 5, 13 and 255, and read 13 back as its powers of two out loud
- [ ] Asked for `np.binary_repr(300, width=8)` and read the `Insufficient bit width` error
- [ ] Printed `np.binary_repr(-5)` with and without a width, and can say which one shows the real bits
- [ ] Indexed an array with a boolean mask and with an integer array of the same 1s and 0s, and recorded
      the two different answers
- [ ] Verified `(a & b) | (a ^ b)` equals `a | b` and can explain it one bit position at a time
- [ ] Left the brackets off a chained comparison and read the `truth value ... is ambiguous` error
- [ ] Applied `~` to a boolean array, a `uint8` array and an `int64` array and wrote down all three answers
- [ ] Built a mask with `~counts` on an integer column and recorded how many rows it selected
- [ ] Shifted a `uint8` `200` left by one and recorded that it became 144
- [ ] Compared `-5 >> 1` against `int(-5 / 2)` and can say which one a shift performs
- [ ] Set, cleared, toggled and tested a flag, and recorded that `flags & FLAG` returns the flag's value
- [ ] Set the same flag twice and toggled the same flag twice, and recorded which one returned to the start
- [ ] Tried `np.uint8(1 << 8)` and `np.uint8(1) << np.uint8(8)` and recorded that only one of them raised
- [ ] Packed the chart and confirmed the saving is exactly 8.0
- [ ] Packed a five-chore chart, unpacked it **without** `count=`, and counted the phantom columns
- [ ] Packed an array of counts and recorded what came back

---

## Section 2 — strings

- [ ] Read [2.1 — `<U8`, text in a fixed-width box](parts/02-strings/2.1-fixed-width-text.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `np.strings`](parts/02-strings/2.2-np-strings.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — comparison is not a match](parts/02-strings/2.3-comparison-is-not-a-match.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — where text does not belong](parts/02-strings/2.4-where-text-does-not-belong.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed a text array's `dtype`, `itemsize` and `nbytes` and worked out the bytes per character
- [ ] Assigned a nine-character name into a `<U8` array and recorded what came back and what `==` said
- [ ] Built an array from numbers and one text value and recorded the dtype it chose
- [ ] Called `arr.lower()` and read the `AttributeError`
- [ ] Checked `isinstance(np.strings.lower, np.ufunc)` and `isinstance(np.strings.add, np.ufunc)` and
      recorded that they differ
- [ ] Counted distinct values before and after normalising and wrote down both numbers
- [ ] Wrote a string result back into its source array and recorded the truncation
- [ ] Ran an `isin` filter against an **unnormalised** vocabulary and recorded that it matched nothing
- [ ] Ran the reverse check — how many vocabulary entries matched anything — and can say why it is the more
      useful number
- [ ] Compared a combining-accent string against a precomposed one and recorded the lengths
- [ ] Measured a fixed-width column, an `object` column and integer codes for the same data, and wrote down
      all three sizes and all three comparison times
- [ ] Derived a vocabulary twice from two datasets and recorded that a code changed

---

## Section 3 — the matrix product

- [ ] Read [3.1 — a dot product is a total](parts/03-matmul/3.1-a-dot-product-is-a-total.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `A @ B` by hand](parts/03-matmul/3.2-matmul-by-hand.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — `@`, `matmul` and `dot`](parts/03-matmul/3.3-at-matmul-and-dot.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — the measured gap](parts/03-matmul/3.4-the-measured-gap.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — stacks of matrices](parts/03-matmul/3.5-stacks-of-matrices.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.6 — every neural layer](parts/03-matmul/3.6-every-neural-layer.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Computed a dot product three ways — `np.dot`, `@` and `(a * b).sum()` — and got the same answer
- [ ] Ran `@` on two boolean rows and on a whole boolean chart, and recorded the grid it returned
- [ ] **Wrote `matmul_by_hand` yourself**, three loops deep, before reading past 3.2
- [ ] Checked it against `@` with `np.array_equal` on the integer chart
- [ ] Computed `did @ did.T` and `did.T @ did` and said out loud, before running, what shape each would be
- [ ] Ran `a * b` and `a @ b` on two square matrices and recorded that the shapes matched and the answers
      did not
- [ ] Compared `np.matmul` and `np.dot` on 3-D input and wrote down both shapes and both sizes
- [ ] Timed `matmul_by_hand` against `@` on 300-by-300 floats and wrote down the ratio
- [ ] Timed an `int64` matrix product against the same data as `float64` and wrote down that ratio too
- [ ] Confirmed the hand version and `@` agree with `np.allclose` and **disagree** with `np.array_equal`
- [ ] Applied one matrix across a stack in a single `@` and checked entry 0 against the unstacked answer
- [ ] Ran `.T` on a three-axis array and recorded the shape, then did the same with `swapaxes(-1, -2)`
- [ ] Built one layer — `maximum(x @ w + b, 0)` — and counted how many values the activation zeroed
- [ ] Confirmed `(X @ W1) @ W2` equals `X @ (W1 @ W2)` and can say what that means about depth

---

## Section 4 — linear algebra

- [ ] Read [4.1 — three trips, three prices](parts/04-linalg/4.1-three-trips-three-prices.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — `solve`, and never `inv`](parts/04-linalg/4.2-solve-and-never-inv.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `np.linalg.norm`](parts/04-linalg/4.3-norm.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — singular](parts/04-linalg/4.4-singular-and-the-error.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — `lstsq`](parts/04-linalg/4.5-lstsq.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.6 — conditioning](parts/04-linalg/4.6-conditioning.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Solved the three shopping trips and recovered prices you recognise
- [ ] Solved the **transposed** system, saw plausible prices, and watched the substitution check fail
- [ ] Timed `solve` against `inv` then multiply on a 500-by-500 system and wrote down the ratio
- [ ] Printed the size in bytes of an inverse you did not need
- [ ] Divided by a norm **without** `keepdims` and read the broadcast error
- [ ] Normalised a chart with an all-zero row and recorded where the `nan` appeared
- [ ] Built a raw overlap grid and a cosine grid from the same chart and found a pair whose ranking changed
- [ ] Ran `det`, `matrix_rank` and `cond` on a repeated-row matrix, a nearly-repeated one and a good one,
      and wrote down all nine numbers
- [ ] Computed the determinant of `np.eye(10) * 0.1` and can say why a determinant threshold is useless
- [ ] Fitted four receipts to three prices and read all four of `lstsq`'s return values
- [ ] Ran `lstsq` on a square system and recorded that `residuals` came back **empty**
- [ ] Ran `lstsq` with more unknowns than equations and recorded that it did not raise
- [ ] Nudged one entry of `b` by `1e-4` on the ill-conditioned system and measured how far the answer moved
- [ ] Scaled the columns of a badly-scaled design matrix and wrote down the condition number before and
      after
- [ ] Compared `cond(A)` against `cond(A.T @ A)` and confirmed the squaring

---

## Section 5 — the module

- [ ] Read [5.1 — `src/setu/chores.py`](parts/05-the-module/5.1-the-chores-module.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — `tests/test_chores.py`](parts/05-the-module/5.2-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question

---

## Build

- [ ] `src/setu/chores.py` exists with `Chore`, `normalise`, `unknown_names`, `pack`, `unpack`, `overlap`,
      `cosine` and `chore_values`, and no `TODO(me)` left unanswered
- [ ] `chores` added to `LAYERS` in `src/setu/layout.py`
- [ ] The `Chore` docstring says **STORAGE FORMAT** and explains what reordering does to stored bytes
- [ ] `_check_width()` is called at import, and you can say what a ninth flag's value would be
- [ ] `pack` refuses a non-boolean chart, and the message says what `packbits` would have done
- [ ] `unpack` passes `count=`, and you have run it once without to see the phantom columns
- [ ] `overlap` refuses a boolean chart, and you have seen the all-`True` grid it prevents
- [ ] `overlap` uses `swapaxes(-1, -2)` and never `.T`
- [ ] `cosine` uses `keepdims=True`, clamps the divisor and clips the result, and you can say what each
      prevents
- [ ] `chore_values` handles the empty `residuals` case, and the reason is in a comment above the line
- [ ] `chore_values` computes the condition from `lstsq`'s own singular values rather than calling
      `np.linalg.cond`
- [ ] Every `TODO(me)` that asked for a written justification has one, in the code, in a full sentence
- [ ] `uv run ruff format src/setu/chores.py tests/test_chores.py` leaves nothing to change
- [ ] `uv run ruff check src/setu/ tests/` is clean

---

## The eval

- [ ] `tests/test_chores.py` exists and every `TODO(me)` is answered
- [ ] The fixture is **not** square, and the comment above it says which bug that protects against
- [ ] The row counts are **not** all equal, and the comment says which bug that protects against
- [ ] At least one test uses a width that is not a multiple of eight, and **asserts that property of the
      fixture**
- [ ] Every guard test uses `match=` on the module's own message, not just the exception type
- [ ] The overlap diagonal is checked against a value computed a different way
- [ ] The cosine test scales one row and asserts the raw grid moved and the cosine grid did not
- [ ] The recovery test builds its scores from a known truth and uses a tolerance chosen against the noise
- [ ] `uv run python -m pytest tests/test_chores.py -q` is green
- [ ] **Broke it on purpose (1):** deleted `count=count` from `unpack`, counted how many tests went red,
      read the reshape error, put it back
- [ ] **Broke it on purpose (2):** deleted the boolean guard from `overlap`, watched one test say
      `DID NOT RAISE`, and can say what the other twenty would have let through
- [ ] Can say why a test suite whose fixtures are all eight columns wide does not test `count=` at all

---

## Budget

- [ ] Zero model calls made today
- [ ] Zero network requests made today
- [ ] No new package added; `numpy==2.5.2` unchanged in `pyproject.toml` and `uv.lock`

---

## Close the day

- [ ] `./m depth 24` passes with no failures
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include today
- [ ] Answered the three §10 questions out loud without scrolling
- [ ] `./m done 24` — committed. No commit, no day (Principle 1).
