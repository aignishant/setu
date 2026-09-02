# Day 23 — CHECKLIST

**IDs covered:** `NP-06`, `NP-07` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 26, in [`parts/`](parts/)

> `./m done 23` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **Most of today's traps do not raise.** The wrong `axis` on a square array, the wrong `ddof`, a `nan`
> reaching `argmax`, `bincount` without `minlength`, a Python `set` handed to `isin`, and an untranslated
> position from `argpartition` all produce a confident wrong answer with no error text at all. Every box
> below that says "record what it printed" exists because of one of them.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_summary.py -v && ./m depth 23 && ./m check
```

Expected: seventeen tests in `test_summary.py` passing, a green depth report for day 23, then a green
gate.

---

## Setup

- [ ] Confirmed `numpy==2.5.2` is still the pin, with `uv run python scripts/check_pins.py | grep -i numpy`
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Ran `./m scaffold 23` and created `src/setu/summary.py` and `tests/test_summary.py`
- [ ] Loaded `data/steps/month-flat.txt` as `float64` and put the week-one Thursday back to `nan`
- [ ] Can say why that `nan` needs a float dtype and what happens if you try it on an `int64` array
- [ ] Can say in one sentence why Day 22 filled that hole and today reopens it

---

## Section 1 — ufuncs

- [ ] Read [1.1 — one operation, every element](parts/01-ufuncs/1.1-one-operation-every-element.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — `out=` and the temporaries](parts/01-ufuncs/1.2-out-and-the-temporaries.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — dividing by zero warns](parts/01-ufuncs/1.3-divide-by-zero-warns.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `np.where`](parts/01-ufuncs/1.4-np-where-the-vectorised-if.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — `maximum` against `max`](parts/01-ufuncs/1.5-maximum-clip-and-elementwise.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — `isclose` and `allclose`](parts/01-ufuncs/1.6-isclose-and-allclose.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.7 — `reduce`, `accumulate` and `at`](parts/01-ufuncs/1.7-reduce-accumulate-and-at.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `type(np.add).__name__` and counted the ufuncs in the top-level namespace
- [ ] Produced `did not contain a loop with signature matching types` deliberately and read the two
      dtypes at the end of the message
- [ ] Measured a chained expression against the `out=` version and wrote down both the time and the
      number of temporaries
- [ ] Ran `np.add(int32_array, 1)` and `np.add(int32_array, 1.0)` and recorded the two dtypes
- [ ] Divided by zero, read both the warning and the value, then made it raise with `np.errstate`
- [ ] Wrote a `np.where` whose "false" branch computes something invalid, and recorded that it ran anyway
- [ ] Confused `np.max` with `np.maximum` on purpose and recorded the shape of each answer
- [ ] Compared `0.1 + 0.2` against `0.3` with `==` and with `np.isclose`

---

## Section 2 — statistics

- [ ] Read [2.1 — many into one](parts/02-statistics/2.1-a-reduction-turns-many-into-one.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `axis`, the one that disappears](parts/02-statistics/2.2-axis-the-one-that-disappears.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `std`, `var` and `ddof`](parts/02-statistics/2.3-std-var-and-ddof.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `median`, `percentile`, `quantile`](parts/02-statistics/2.4-median-percentile-and-quantile.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — the `nan` family](parts/02-statistics/2.5-the-nan-family.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.6 — float summation and the drift](parts/02-statistics/2.6-float-summation-and-the-drift.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Reduced the month along both axes and said out loud, before running it, what shape each would be
- [ ] Ran the same reduction on a **square** array both ways and recorded that neither raised
- [ ] Printed the ratio of `var(ddof=1)` to `var(ddof=0)` and confirmed it equals `n/(n-1)` exactly
- [ ] Ran `np.array([5.0]).var(ddof=1)`, read **both** warnings, and wrote down which one you would grep
      a log for
- [ ] Computed a variance with the textbook `E[x²] - E[x]²` formula on values near `1e9` and recorded
      that it came out negative
- [ ] Printed all nine `percentile` methods on the same seven values and recorded the spread between them
- [ ] Recorded that two of the nine returned an integer and the rest returned a float
- [ ] Ran `arr == np.nan` on an array containing a `nan` and recorded that it found nothing
- [ ] Ran `argmax` on that array and recorded that it returned the `nan`'s own position
- [ ] Ran `nansum`, `nanmean` and `nanargmax` on an all-`nan` array and recorded the three different
      behaviours
- [ ] Summed a million `float32` values three ways — naive loop, `.sum()`, `math.fsum` — and wrote down
      both errors
- [ ] Added `1.0` to `np.float32(16_777_216.0)` twice and recorded that nothing moved

---

## Section 3 — sorting and searching

- [ ] Read [3.1 — `np.sort` and `.sort()`](parts/03-sorting-and-searching/3.1-sort-and-the-copy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `argsort`, the positions](parts/03-sorting-and-searching/3.2-argsort-the-positions.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — top-k and `argpartition`](parts/03-sorting-and-searching/3.3-top-k-and-argpartition.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — sorting along an axis](parts/03-sorting-and-searching/3.4-sorting-along-an-axis.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — `searchsorted`](parts/03-sorting-and-searching/3.5-searchsorted.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.6 — stability and `kind=`](parts/03-sorting-and-searching/3.6-stability-and-kind.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote `week = week.sort()` on purpose and read the error the **next** line produced
- [ ] Passed `month[0]` to a function that sorts in place and confirmed the month itself changed
- [ ] Used `argsort` to reorder a second array of labels, then broke it by reversing the input instead of
      the positions and recorded the wrong answer
- [ ] Ran `np.argsort` on data containing a `nan` and recorded which value `order[-1]` pointed at
- [ ] Timed `argsort`-then-slice against `argpartition`-then-slice on two million scores and wrote down
      the ratio
- [ ] Confirmed the two agree as **sets** and recorded whether they agreed as arrays on your input size
- [ ] Skipped the translate-back on purpose and recorded which three days it claimed were best
- [ ] Sorted the month with `axis=0`, summed the rows, and compared against the real week totals
- [ ] Tried to index the month with a per-row `argsort` and recorded the shape that came back
- [ ] Ran `searchsorted` on an **unsorted** array and found a value it answered wrongly
- [ ] Binned the month with `searchsorted` against three edges and moved a boundary day by switching
      `side`
- [ ] Found a size at which `kind="quicksort"` and `kind="stable"` disagree, and one at which they do not
- [ ] Timed `quicksort`, `stable` and `heapsort` on two million values and wrote down all three

---

## Section 4 — counting

- [ ] Read [4.1 — `count_nonzero` and the mask](parts/04-counting/4.1-count-nonzero-and-the-mask.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — `np.unique`](parts/04-counting/4.2-unique.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `np.bincount`](parts/04-counting/4.3-bincount.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — `np.histogram`](parts/04-counting/4.4-histogram-and-the-edges.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — `np.isin`](parts/04-counting/4.5-isin-and-membership.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Counted a mask both ways and recorded the type each one returned
- [ ] Handed one of those counts to `json.dumps` and read the `TypeError`
- [ ] Wrote a rate with `//` on purpose and recorded that it printed `0`
- [ ] Combined two conditions with `and` and read the `truth value ... is ambiguous` message
- [ ] Unpacked `np.unique`'s returns in the wrong order and recorded that nothing raised
- [ ] Rebuilt the original array from `values[inverse]` and asserted it matched
- [ ] Called `np.bincount` on values with a large maximum and recorded the size of the result in bytes
- [ ] Called it without `minlength=` on data missing its highest code and recorded the shortened length
- [ ] Used `weights=` to produce a grouped sum and checked it against the same answer via `axis=`
- [ ] Binned `[0., 1., 2., 3.]` against edges `[0, 1, 2, 3]` and explained why the last bin holds two
- [ ] Histogrammed two different datasets with `bins=2` and recorded that the counts matched and the
      edges did not
- [ ] Passed a Python `set` to `np.isin` and recorded that every answer was `False`
- [ ] Compared text against numbers with `np.isin` and recorded that nothing raised
- [ ] Timed `np.isin` against a Python `set` comprehension on two million values

---

## Section 5 — the module

- [ ] Read [5.1 — `src/setu/summary.py`](parts/05-the-module/5.1-the-summary-module.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — `tests/test_summary.py`](parts/05-the-module/5.2-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question

---

## Build

- [ ] `src/setu/summary.py` exists with `Summary`, `top_k`, `summarise` and `hit_rate`, and no
      `TODO(me)` left unanswered
- [ ] `summary` added to `LAYERS` in `src/setu/layout.py`
- [ ] Every `TODO(me)` comment that asked for a written justification has one, in the code, in a full
      sentence
- [ ] `top_k` returns **positions**, not values, and the docstring says so
- [ ] Both translate-backs in `top_k` are marked with a comment naming which array the positions refer to
- [ ] `summarise` states `method=` and translates `sample` into `ddof` in exactly one place
- [ ] Both reductions pass `dtype=ACCUMULATE_IN`, and you can say whether that is a cast or an accumulator
- [ ] Every scalar field of `Summary` is a plain Python number and `best` is not
- [ ] `uv run ruff format src/setu/summary.py tests/test_summary.py` leaves nothing to change
- [ ] `uv run ruff check src/setu/ tests/` is clean

---

## The eval

- [ ] `tests/test_summary.py` exists and every `TODO(me)` is answered
- [ ] The fixture is **not** square and **not** sorted, with a comment saying which two bugs that protects
      against
- [ ] The `month` fixture returns a fresh copy, and you can name the test that would corrupt the others
      without it
- [ ] At least one test computes its expected answer a **different way** rather than pinning a literal
- [ ] The `ddof` test asserts the ratio `sqrt(n/(n-1))`, not a number
- [ ] The no-mutation test passes `equal_nan=True`, and you ran it once without to see it fail
- [ ] The top-k test compares **sets** against `np.argsort`, not arrays
- [ ] `uv run python -m pytest tests/test_summary.py -q` is green
- [ ] **Broke it on purpose (1):** changed `ddof=1 if sample else 0` to `ddof=0`, watched exactly one test
      go red, read the message, put it back
- [ ] **Broke it on purpose (2):** deleted the outer `candidates[...]` from `top_k`'s return, counted how
      many tests went red, and wrote down which one named both the wrong and the right positions
- [ ] Can say why a test asserting `result.mean == 9106.7` would have stayed green through break (2)

---

## Budget

- [ ] Zero model calls made today
- [ ] Zero network requests made today
- [ ] No new package added; `numpy==2.5.2` unchanged in `pyproject.toml` and `uv.lock`

---

## Close the day

- [ ] `./m depth 23` passes with no failures
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include today
- [ ] Answered the three §10 questions out loud without scrolling
- [ ] `./m done 23` — committed. No commit, no day (Principle 1).
