---
day: 29
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 29 — Iteration vs vectorisation; sorting and ranking"
ids: ["PD-05", "PD-06"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 20
generated: "2026-09-03"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 29 — Iteration vs vectorisation; sorting and ranking

**Phase 4 · Pandas 3.0 · Module 4** · `PD-05` iteration and why you should not · `PD-06` sorting,
ranking and `nlargest`, with the plan's named example: **`iterrows` against vectorised, timed on one
million rows.**

> **Yesterday:** getting things out of a frame — `loc` and `iloc`, masks, and the alignment that
> happens whenever two labelled objects meet.
> **Today:** two questions that both come down to *do not make pandas do it one row at a time*. First,
> why walking a frame one row at a time is thousands of times slower than describing the operation
> once — measured, not asserted. Then the two ways of putting rows in order, and the thing neither of
> them tells you: what happens when two rows are equal.
> **Tomorrow:** missing data as a subject in its own right, and why the imputer belongs inside the
> pipeline rather than before it.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody wants to know what the shopping came to.

They do what anybody would do with a piece of paper. Start at the top. Milk, two of them at one
fifteen, that is two thirty. Write it down. Bread, one at one forty. Keep a running total. Four lines,
a few seconds, completely correct.

Then the shop sends three years of history — a million lines — and the same habit takes half a minute
to produce the same kind of answer. The habit was never wrong; it just does not scale, and the reason
is worth understanding rather than memorising.

A frame is not stored as rows. It is stored as **columns**: each one a single block of memory holding
values of one type, laid out end to end. A row cuts across all of those blocks, so it does not exist
until somebody builds it — and a loop builds one, uses it, and throws it away, a million times. The
arithmetic was never the expensive part.

Say it once instead — *multiply these by those, then add all of that up* — and the work happens in
compiled code that walks the blocks. Same eight hundred thousand multiplications. About eleven
milliseconds instead of thirty-three seconds.

The second half of the day is a different kind of not-thinking-per-row, and it is about order.

Three people in the flat do exactly the same number of washing-ups. Somebody sorts the chart and takes
the top row to find the winner. It works. Then somebody rebuilds the chart from the same records,
entered in a different order, and it names a different winner.

Nothing was wrong with either sort. When two rows are equal, the sort has no instruction, so something
else decides — the algorithm, and the order the rows happened to arrive in. Neither of those is in
your code, and neither is in the data.

So the day has one shape running through both halves: **stop asking pandas to make a decision per row,
and stop letting it make a decision you did not write down.** The first is a speed problem with a
measurement attached. The second is a correctness problem that produces a plausible answer every time
and a different one on Tuesday.

---

## §2 The map

Six sections. The first three are `PD-05` — the loop, its replacement, and the measurement that
settles the argument. The next two are `PD-06` — putting rows in order, and numbering them. The last
is where both meet the project's code.

| Section | What it means |
|---|---|
| **1.x** | **The loop** — four ways to walk a frame, and what each one costs you |
| **2.x** | **Vectorised** — describing the operation once instead |
| **3.x** | **The measurement** — the plan's named example, and what a ratio does not tell you |
| **4.x** | **Sorting** — putting rows in order, and the ties nobody specifies |
| **5.x** | **Ranking** — the position as a number, and the top few without a sort |
| **6.x** | **The module** — the rules written down, and a test that could not fail |

### Section 1 — the loop

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [Reading the list one line at a time](parts/01-the-loop/1.1-reading-the-list-one-line-at-a-time.md) | Why is a row expensive? | `foundation` |
| 1.2 | [`iterrows` and the row that lost its dtype](parts/01-the-loop/1.2-iterrows-and-the-row-that-lost-its-dtype.md) | Why did my integers become floats? | `working` |
| 1.3 | [`itertuples` and what it costs](parts/01-the-loop/1.3-itertuples-and-what-it-costs.md) | The faster loop, and its one catch | `working` |
| 1.4 | [The loop that changed nothing](parts/01-the-loop/1.4-the-loop-that-changed-nothing.md) | Why did my write disappear? | `working` |
| 1.5 | [`apply` is a loop wearing a hat](parts/01-the-loop/1.5-apply-is-a-loop-wearing-a-hat.md) | Is `apply` vectorised? | `working` |

### Section 2 — vectorised

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [One operation, every row](parts/02-vectorised/2.1-one-operation-every-row.md) | What replaces the loop? | `foundation` |
| 2.2 | [The three ways to write a condition](parts/02-vectorised/2.2-the-three-ways-to-write-a-condition.md) | How do you vectorise an `if`? | `working` |
| 2.3 | [When there is no vectorised form](parts/02-vectorised/2.3-when-there-is-no-vectorised-form.md) | When does the loop genuinely stay? | `production` |

### Section 3 — the measurement

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [What a million rows is for](parts/03-the-measurement/3.1-what-a-million-rows-is-for.md) | Why does the size change the conclusion? | `working` |
| 3.2 | [The four ways, timed](parts/03-the-measurement/3.2-the-four-ways-timed.md) | The plan's named example | `working` |
| 3.3 | [The number, and where it stops mattering](parts/03-the-measurement/3.3-the-number-and-where-it-stops-mattering.md) | Is it worth fixing? | `production` |

### Section 4 — sorting

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [`sort_values` — the order you asked for](parts/04-sorting/4.1-sort-values-the-order-you-asked-for.md) | How do you put rows in order? | `foundation` |
| 4.2 | [The tie that broke the report](parts/04-sorting/4.2-the-tie-that-broke-the-report.md) | Who decides when two rows are equal? | `working` |
| 4.3 | [`na_position` and the rows that went to the end](parts/04-sorting/4.3-na-position-and-the-rows-that-went-to-the-end.md) | Where do the blanks go? | `working` |
| 4.4 | [`sort_index` and the cost of order](parts/04-sorting/4.4-sort-index-and-the-cost-of-order.md) | When is a sorted index required? | `production` |

### Section 5 — ranking

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`rank` — the position in the order](parts/05-ranking/5.1-rank-the-position-in-the-order.md) | Order as a number, not as an arrangement | `foundation` |
| 5.2 | [The five ways to rank a tie](parts/05-ranking/5.2-the-five-ways-to-rank-a-tie.md) | What number do equal rows get? | `working` |
| 5.3 | [`nlargest` — sorting you do not pay for](parts/05-ranking/5.3-nlargest-sorting-you-do-not-pay-for.md) | The top few, without ordering the rest | `production` |

### Section 6 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`src/setu/order.py`](parts/06-the-module/6.1-the-order-module.md) | Where does each rule live? | `production` |
| 6.2 | [The test that could not fail](parts/06-the-module/6.2-the-test-that-can-go-red.md) | How do you test determinism? | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-29-iteration-and-order/lab
touch src/setu/order.py tests/test_order.py
uv run python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

Expected: `3.0.5 2.5.2`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5 pyarrow==25.0.1`.

Confirm the two things this day's timings assume about your machine:

```bash
uv run python -c "
import time
import pandas as pd
shop = pd.DataFrame({'need': list(range(2000)), 'price': [1.0] * 2000})

def best(fn, reps):
    t = []
    for _ in range(reps):
        s = time.perf_counter()
        fn()
        t.append(time.perf_counter() - s)
    return min(t) * 1000

loop = best(lambda: sum(r['need'] * r['price'] for _, r in shop.iterrows()), 3)
vec = best(lambda: float((shop['need'] * shop['price']).sum()), 20)
print(f'loop       {loop:7.1f} ms')
print(f'vectorised {vec:7.2f} ms')
print(f'ratio      {loop / vec:7.0f}x')
"
```

Expected: a ratio in the **hundreds** at two thousand rows. The exact number will differ from this
day's — every timing here was measured on one laptop under whatever else it was doing
([3.1](parts/03-the-measurement/3.1-what-a-million-rows-is-for.md)). **The ratios are the finding; the
absolute milliseconds are not.**

One warning about section 3: the benchmark in
[3.2](parts/03-the-measurement/3.2-the-four-ways-timed.md) takes about a minute to run, most of it in
the `iterrows` case. That is not a flaw in the script.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/order.py`** — [6.1](parts/06-the-module/6.1-the-order-module.md) walks through the whole
module.

- `SHOP_ORDER` and `SHOP_DIRECTION` — the sort keys and their directions, as parallel constants.
- `OrderError(ValueError)` — for an ordering that did not do what it promised. Import Day 28's
  `SelectionError` rather than defining a fourth exception.
- `line_totals(shop)` — one vectorised expression, and a docstring saying so
  ([2.1](parts/02-vectorised/2.1-one-operation-every-row.md)).
- `in_shop_order(shop)` — a **total** sort: the index name appended as the final key, `kind="stable"`
  stated ([4.2](parts/04-sorting/4.2-the-tie-that-broke-the-report.md)).
- `with_rank(shop)` — `method="min"`, `ascending=False`, blanks refused rather than filled
  ([5.2](parts/05-ranking/5.2-the-five-ways-to-rank-a-tie.md)).
- `top_n(shop, n)` — `nlargest` with `keep="all"` used as a **detector**, raising when more rows tie
  than were asked for ([5.3](parts/05-ranking/5.3-nlargest-sorting-you-do-not-pay-for.md)).
- `is_ordered(shop)` — **as given, this sorts in order to answer, which makes it more expensive than
  the sort it exists to avoid.** [6.1](parts/06-the-module/6.1-the-order-module.md) measures the
  shortfall.
- `TODO(me)`: fix `is_ordered` so it is genuinely cheap — one pass, no sorted copy. The production
  section of [6.1](parts/06-the-module/6.1-the-order-module.md) starts a `pd.factorize` approach and
  deliberately leaves the comparison wrong; working out why an elementwise `<=` is not a
  lexicographic comparison is the exercise. Measure it against `in_shop_order` and record both numbers
  in a comment.
- `TODO(me)`: `in_shop_order` appends `shop.index.name` as the tie-breaker, and that is `None` on a
  frame whose index is unnamed — at which point the sort silently stops being total. Add the check,
  and write one sentence saying what it protects.
- `TODO(me)`: add `spend_by_aisle(shop)` returning the total spend per aisle, **without a loop over
  aisles**. Section 2 gives you enough; Day 31's `groupby` would be the idiomatic answer and is not
  available yet, so solve it with what you have and note in a comment what you would write on Day 31.

**`tests/test_order.py`** — [6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) walks through
the whole file.

- The four kinds of assertion: what each function returns, what it does **not** do, what it refuses,
  and that it is **deterministic** under a reshuffled input.
- The determinism test's fixture must **contain a real tie**, and must assert that it does — this is
  the part's whole lesson.
- One test for the **empty frame** across every public function.
- `TODO(me)`: write the tests for your `spend_by_aisle` — at least one asserting the caller's frame is
  untouched, and at least one on an aisle that appears once.
- `TODO(me)`: add a determinism test for `with_rank` as well, and think about what "the same result"
  means when the function does not reorder anything.
- `TODO(me)`: break the module a **second** way of your own — not the tie-breaker deletion and not the
  rank method. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say which
  test should have caught it and why it did not.

**`lab/million.py`** — the plan's named example, made runnable. A script, because its job is to be run
and waited for.

- Build the million-row frame from the day's seed, and print its row count and memory.
- Time all six ways from [3.2](parts/03-the-measurement/3.2-the-four-ways-timed.md), printing the
  **total each one produced** alongside its time.
- `TODO(me)`: add an assertion that every total is identical, so a version that is fast and wrong
  cannot pass unnoticed.
- `TODO(me)`: run it twice on the same machine and record both sets of numbers in a comment at the
  top. Say which comparisons moved between runs and which did not, and what that means for the ones
  you would quote ([3.1](parts/03-the-measurement/3.1-what-a-million-rows-is-for.md)).

---

## §5 The eval that must be able to fail

`tests/test_order.py` is RED until `src/setu/order.py` exists. Write these two first, because they are
the two that carry the day:

```python
def test_shop_order_is_the_same_whatever_the_input_order(shop: pd.DataFrame) -> None:
    """The sort is total, so a reshuffled input gives an identical result."""
    tied = shop.assign(
        aisle=pd.Series(["07", "07", "07", "11"], index=shop.index, dtype="str"),
        price=[1.15, 1.15, 1.15, 2.05],
    )
    assert tied.duplicated(od.SHOP_ORDER).any(), "the fixture must contain a real tie"
    pd.testing.assert_frame_equal(od.in_shop_order(tied), od.in_shop_order(tied.iloc[::-1]))


def test_rank_shares_the_best_rank_on_a_tie(shop: pd.DataFrame) -> None:
    tied = shop.assign(price=[5.0, 5.0, 3.0, 5.0])
    assert od.with_rank(tied)["rank"].tolist() == [1, 1, 4, 1]
```

**The assertion on the fixture is the point of the first one.** Without it the test passes whether or
not the tie-breaker is there, because a sort with no ties is total whatever key you give it — and that
is not a hypothetical. It is what happened when this suite was first written
([6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md)).

**The mutations to watch.** Two, and they behave differently:

1. In `with_rank`, change `method="min"` to `method="average"`. **One test goes red**, with
   `assert [2, 2, 4, 2] == [1, 1, 4, 1]`.
2. In `in_shop_order`, delete `shop.index.name` from the key list. **One test goes red** — but only
   because the fixture ties. Simplify the fixture back and the same mutation passes twelve out of
   twelve.

And one that **no correctness test can catch**: replace `line_totals`' expression with a loop over
`itertuples`. The answers are identical, the suite stays green, and the function is hundreds of times
slower ([3.2](parts/03-the-measurement/3.2-the-four-ways-timed.md)). The defences are a docstring for
the reviewer and a separate ratio-based performance test
([Day 25, 5.2](../day-25-copy-view-and-the-gate/parts/05-the-gate/5.2-the-performance-test-in-ci.md)).

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed.

The only cost today is patience: the benchmark in
[3.2](parts/03-the-measurement/3.2-the-four-ways-timed.md) builds a million-row frame — about 28 MB in
memory — and the `iterrows` case takes around half a minute on its own. Nothing is written to disk and
nothing is downloaded.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **`for row in frame:`** yields the **column names**, not the rows. Iterating a Series yields its
  values ([1.1](parts/01-the-loop/1.1-reading-the-list-one-line-at-a-time.md)).
- **`iterrows` changes your types.** An `int64` column comes back as `float64`, or as `object` if the
  frame has a text column in it — and which you get depends on the *other* columns
  ([1.2](parts/01-the-loop/1.2-iterrows-and-the-row-that-lost-its-dtype.md)).
- **Writing to the row `iterrows` gives you does nothing**, and unlike chained assignment it does not
  even warn ([1.4](parts/01-the-loop/1.4-the-loop-that-changed-nothing.md)).
- **`itertuples` renames any column that is not a valid identifier** to `_1`, `_2` — positionally, so
  the names shift when a column is added ([1.3](parts/01-the-loop/1.3-itertuples-and-what-it-costs.md)).
- **`apply(axis=1)` is a loop**, and a slower one than `itertuples`
  ([1.5](parts/01-the-loop/1.5-apply-is-a-loop-wearing-a-hat.md)). On an empty frame it calls your
  function once anyway.
- **`*` on a text column is repetition**, so `item * need` succeeds and produces nonsense
  ([2.1](parts/02-vectorised/2.1-one-operation-every-row.md)).
- **A narrow integer dtype overflows silently.** `int8 * 100` wraps rather than promoting
  ([2.1](parts/02-vectorised/2.1-one-operation-every-row.md)).
- **`np.where` returns an array with no index**, so wrap it before assigning or comparing
  ([2.2](parts/02-vectorised/2.2-the-three-ways-to-write-a-condition.md)).
- **`np.select` with no `default=` uses `0`** — which raises among string choices and scores an
  unmatched row zero among numeric ones
  ([2.2](parts/02-vectorised/2.2-the-three-ways-to-write-a-condition.md)).
- **`sort_values` returns a new frame.** A bare call is a line that does nothing
  ([4.1](parts/04-sorting/4.1-sort-values-the-order-you-asked-for.md)).
- **A sort with ties is not deterministic**, because the algorithm and the arrival order decide
  ([4.2](parts/04-sorting/4.2-the-tie-that-broke-the-report.md)).
- **Blanks sort last regardless of `ascending`**, so `.tail(1)` after a sort is a blank row rather than
  the maximum ([4.3](parts/04-sorting/4.3-na-position-and-the-rows-that-went-to-the-end.md)).
- **`rank`'s default is `average`**, so a joint-first row shows as rank 2
  ([5.2](parts/05-ranking/5.2-the-five-ways-to-rank-a-tie.md)). And a rank column is **not** a
  permutation of 1..n.
- **`nlargest(n, ..., keep="all")` can return more than `n` rows**
  ([5.3](parts/05-ranking/5.3-nlargest-sorting-you-do-not-pay-for.md)).
- **A benchmark on a fixture-sized frame proves nothing** about production, because the ratio itself
  grows with the size ([3.1](parts/03-the-measurement/3.1-what-a-million-rows-is-for.md)).

**The pattern behind the day.** Section 1's failures are about **speed**, and they are honest — the
code is correct and slow. Sections 4 and 5's are about **determinism**, and they are the dangerous
kind: a plausible answer that changes when nothing changed. Both come from letting pandas decide
something per row that you should have decided once.

---

## §8 Verify before you code

Fetched on the day of writing. Read the argument lists rather than trusting any lesson, this one
included.

- **Iteration** — <https://pandas.pydata.org/docs/user_guide/basics.html#iteration> — the user guide's
  own warning that iterating is slow and should usually be avoided, with the three methods and what
  each yields.
- **`DataFrame.itertuples`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html> — read the note about
  column names that are not valid Python identifiers being renamed positionally.
- **`DataFrame.sort_values`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html> — check `kind`
  (default `quicksort`, which is **not** stable) and `na_position` (default `last`).
- **`Series.rank`** — <https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html> — the five
  `method` values and what each does to a tie, plus `pct` and `na_option`.
- **`DataFrame.nlargest`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html> — confirm for yourself
  that `keep="all"` can return more rows than `n`, and note the argument order.

---

## §9 Say it in an interview

> A pandas frame is stored by column — contiguous blocks of one dtype — so a row does not exist until
> something builds it. That is why looping is slow: every turn constructs a Python object out of
> values fetched from each block and then discards it, and the arithmetic inside the loop is not the
> cost. On a million rows `iterrows` takes about thirty seconds and the equivalent expression takes
> about five milliseconds. The loops are not all alike either — `apply(axis=1)` is *slower* than
> `itertuples`, and a plain `zip` of two columns beats both, because it builds no per-row object at
> all. What does not help is calling `to_numpy()` first to "avoid pandas overhead": two columns from
> one frame share an index object, so the alignment check is skipped anyway and you have given up the
> protection for a rounding error.
>
> The honest limit is a true sequential dependency — where a row needs the *answer* computed for the
> previous row rather than its value. A running balance with a floor is the example. If it only needs
> the previous row's value, that is `shift` or `diff` and no loop is required.
>
> The second half is ordering, and the thing people miss is that a sort with ties does not define an
> order. Within a tie the result is decided by the algorithm — pandas defaults to quicksort, which is
> not stable — and by the order the rows happened to arrive in, which is a property of the data rather
> than of the code. So any sort whose output matters needs a key that cannot tie, and a check that it
> cannot. Ranking is the safer tool when ties are the point, because it makes you name a `method`
> instead of quietly picking one — and if you only want the extremes, `nlargest` is both faster than
> sorting and better behaved, because it cannot return a row whose value is missing.

---

## §10 Done when

Every box in [CHECKLIST.md](CHECKLIST.md) is ticked, `./m depth 29` passes, and `./m check` is green.

Not when a number of sittings have passed. A part is finished when you can answer its *Check yourself*
question out loud without scrolling up, and the day is finished when you can state the one-question
test for whether something needs a loop, and explain — without looking — why a sort that ran correctly
can still name a different winner tomorrow.
