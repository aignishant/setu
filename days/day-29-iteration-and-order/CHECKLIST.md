# Day 29 — Definition of done

`PD-05` iteration and why you should not · `PD-06` sorting, ranking and `nlargest`.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints one total, three ways, and a ratio in the
hundreds:

```bash
uv run python -c "
import time
import numpy as np
import pandas as pd
from setu import order as od
rng = np.random.default_rng(29)
n = 200_000
shop = pd.DataFrame({'need': rng.integers(1, 9, n), 'price': np.round(rng.uniform(0.2, 4.0, n), 2)})

def best(fn, reps):
    t = []
    for _ in range(reps):
        s = time.perf_counter()
        v = fn()
        t.append(time.perf_counter() - s)
    return min(t) * 1000, v

for label, fn, reps in [
    ('itertuples', lambda: sum(r.need * r.price for r in shop.itertuples(index=False)), 2),
    ('zip       ', lambda: sum(a * b for a, b in zip(shop['need'], shop['price'], strict=True)), 3),
    ('vectorised', lambda: float(od.line_totals(shop).sum()), 20),
]:
    ms, value = best(fn, reps)
    print(f'{label} {ms:9.2f} ms   total {float(value):.2f}')
"
```

---

## Setup

- [ ] Ran `./m scaffold 29` and created `src/setu/order.py` and `tests/test_order.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `numpy.__version__` is `2.5.2`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and got a ratio in the **hundreds** at two thousand rows on my own machine
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — the loop

- [ ] **1.1** read · ran its check-yourself · answered its out-loud question
- [ ] Saw that `for x in frame` gives **column names** and `for x in column` gives values
- [ ] Measured the loop against the expression at 2 000 rows and got a three-figure ratio
- [ ] **1.2** read · ran its check-yourself · answered its out-loud question
- [ ] Watched an `int64` column come out of `iterrows` as `float64`, and as `object` once text was added
- [ ] **1.3** read · ran its check-yourself · answered its out-loud question
- [ ] Saw a column called `unit price` renamed to `_1`, and watched that name shift when a column was added
- [ ] **1.4** read · ran its check-yourself · answered its out-loud question
- [ ] Wrote to the row inside `iterrows`, watched the printout say it worked, and the frame say it did not
- [ ] Confirmed `itertuples` **raises** on the same mistake, and can say why that is better
- [ ] **1.5** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed `apply(axis=1)` is slower than `itertuples` on my own machine
- [ ] Ran `apply(axis=1)` on an **empty** frame and counted the calls

## Section 2 — vectorised

- [ ] **2.1** read · ran its check-yourself · answered its out-loud question
- [ ] Multiplied a text column by an integer column and saw the nonsense it produces without erroring
- [ ] Watched an `int8` column **wrap** rather than promote, and can say what 2 × 100 came out as
- [ ] **2.2** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed `np.where` returns an array with **no index**, and wrapped one back into a Series
- [ ] Met `np.select`'s missing `default=` — the `TypeError` with strings, the silent `0` with numbers
- [ ] Found the value `pd.cut` drops when it sits exactly on the lowest bin edge
- [ ] **2.3** read · ran its check-yourself · answered its out-loud question
- [ ] Wrote the running-balance-with-a-floor loop and confirmed `cumsum` gives a different answer
- [ ] Compared `.str` against a list comprehension on a `str` column **and** on an `object` column

## Section 3 — the measurement

- [ ] **3.1** read · ran its check-yourself · answered its out-loud question
- [ ] Ran the size sweep and watched the **ratio itself** grow with the frame
- [ ] Timed a millisecond-scale operation once and then fifty times, and compared the two answers
- [ ] **3.2** read · ran its check-yourself · answered its out-loud question
- [ ] Ran the plan's named example on a million rows **on my own machine** and waited for it
- [ ] Recorded my six numbers next to the day's, and can explain why the absolutes differ
- [ ] Confirmed every one of the six produced the identical total
- [ ] Confirmed `to_numpy()` first buys very little, and can say why
- [ ] **3.3** read · ran its check-yourself · answered its out-loud question
- [ ] Worked out the yearly saving for a nightly job and for a per-request one, from the same ratio
- [ ] Found a step in my own code where the write costs more than the loop

## Section 4 — sorting

- [ ] **4.1** read · ran its check-yourself · answered its out-loud question
- [ ] Called `sort_values` without assigning it and confirmed nothing changed
- [ ] Sorted a numeric column stored as text and saw `'10'` come before `'2'`
- [ ] **4.2** read · ran its check-yourself · answered its out-loud question
- [ ] Sorted the same tied rows from two input orders and got two different winners
- [ ] Added a tie-breaker and confirmed the two now agree
- [ ] Ran `duplicated(keys).any()` and understood what it is asserting
- [ ] **4.3** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed blanks sort last in **both** directions, and that `.iloc[-1]` is therefore not the maximum
- [ ] **4.4** read · ran its check-yourself · answered its out-loud question
- [ ] Timed `is_monotonic_increasing` against a sort and saw the difference
- [ ] Confirmed re-sorting an already-sorted frame is **not** free

## Section 5 — ranking

- [ ] **5.1** read · ran its check-yourself · answered its out-loud question
- [ ] Added a rank column and confirmed the frame's own order was untouched
- [ ] Can say why a rank column comes back as `float64`
- [ ] **5.2** read · ran its check-yourself · answered its out-loud question
- [ ] Ran all five `method=` values on one tie and can say what each gives
- [ ] Confirmed only `dense` has no gaps and only `first` gives every row a distinct number
- [ ] **5.3** read · ran its check-yourself · answered its out-loud question
- [ ] Timed `nlargest(10)` against `sort_values().head(10)` on a million rows
- [ ] Found the case where `sort().tail(2)` returns a blank row and `nlargest(2)` does not
- [ ] Saw `keep='all'` return **three** rows for `n=2`

## Section 6 — the module

- [ ] **6.1** read · ran its check-yourself · answered its out-loud question
- [ ] **6.2** read · ran its check-yourself · answered its out-loud question

## The build

- [ ] `src/setu/order.py` imports Day 28's `SelectionError` rather than defining a fourth exception
- [ ] `line_totals` is one vectorised expression and its docstring says so
- [ ] `in_shop_order` appends the index name as a final key, and states `kind="stable"`
- [ ] `with_rank` states `method="min"` and `ascending=False`, and refuses blanks
- [ ] `top_n` uses `keep="all"` as a detector and **raises** on a boundary tie
- [ ] There is not one `iterrows`, `itertuples` or `apply(axis=1)` anywhere in the module
- [ ] `TODO(me)`: rewrote `is_ordered` so it does not sort, and recorded both timings in a comment
- [ ] `TODO(me)`: added the `index.name is None` check to `in_shop_order`, with its one-sentence reason
- [ ] `TODO(me)`: wrote `spend_by_aisle` without a loop over aisles, and noted the Day 31 version
- [ ] `lab/million.py` runs the plan's named example and prints each version's total beside its time
- [ ] `TODO(me)`: asserted every total is identical, so a fast wrong answer cannot pass
- [ ] `TODO(me)`: ran it twice and recorded which comparisons moved between runs

## The tests

- [ ] `tests/test_order.py` makes all four kinds of assertion — returns, does-not, refuses, deterministic
- [ ] The determinism test's fixture **contains a real tie**, and asserts that it does
- [ ] One test covers the **empty frame** across every public function
- [ ] `uv run pytest tests/test_order.py -q` is green
- [ ] **Break it (1):** changed `method="min"` to `"average"` and watched one test go red
- [ ] **Break it (2):** deleted the tie-breaker from `in_shop_order` and watched one test go red
- [ ] **Break it (3):** removed the tie from the fixture, repeated (2), and watched it go **green**
- [ ] Can explain what (3) proves about the relationship between a test and its fixture
- [ ] Confirmed that replacing `line_totals` with a loop keeps the suite green, and can say what to do
- [ ] `TODO(me)`: wrote the tests for `spend_by_aisle`, including a no-mutation one
- [ ] `TODO(me)`: added a determinism test for `with_rank`
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:` block

## The gate

- [ ] `uv run ruff format days/day-29-iteration-and-order/ src/setu/order.py tests/test_order.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 29` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 29` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-05` and `PD-06` and quotes my own million-row ratio
