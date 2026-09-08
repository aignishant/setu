---
day: 31
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 31 — groupby: split–apply–combine, agg and transform"
ids: ["PD-08"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 20
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 31 — `groupby`: split–apply–combine, `agg` and `transform`

**Phase 4 · Pandas 3.0 · Module 4** · `PD-08` split–apply–combine, `agg` and `transform` — with the
plan's named example: **mean citations per year per field, in one expression**, done here as mean
spend per aisle per shop.

> **Yesterday:** the empty box — what a blank is, why it is there, and the three things you can do
> about it, one of which leaks the test set into the training set.
> **Today:** one question shape — *for each distinct value of this column, what is the answer for the
> rows that carry it?* — and the two shapes its answer can take. Plus the four arguments that decide
> which rows are in the answer at all, and a measurement showing that the flexible way of writing it
> is eighty times slower.
> **Tomorrow:** joining and reshaping — putting two tables together, and moving keys between the index
> and the columns, which is the tool today's `unstack` was borrowing in advance.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Four lines on the shopping list, and an aisle written next to each one: milk from dairy, bread from
the bakery, eggs from dairy, rice from the dry goods.

Somebody wants to know what each aisle came to. What they do is what anybody does with a piece of
paper: run a finger down the list, keep a running total per aisle, read the totals out. Two point
three and one ninety-two for dairy. One forty for the bakery. Two oh five for dry.

Three steps happened there and it is worth naming them, because everything today is one of the three.
**Split** — the finger put each line into a pile. **Apply** — each pile got added up. **Combine** —
the answers went into one small table.

Then somebody asks a different question: *which line was the biggest part of its aisle?* Same data,
same piles, same totals — and a completely different piece of paper. This time the answer has one row
per **line**, not one per aisle, because every line needs its own aisle's total written next to it
before you can divide.

That is the day's central distinction, and it survives contact with everything else. One shape is a
report: three aisles, three numbers, small. The other is a column: four lines, four numbers, the same
length as what you started with. The arithmetic is identical. Which one you asked for decides whether
your next line of code works or silently fills a column with blanks.

Then the awkward part, which is about the piles rather than the sums. One line has no aisle written on
it, because somebody typed it in during a phone call. The finger has nowhere to put it, so it does not
go in any pile — and the totals come out to seven sixty-seven for a shop that cost ten seventy-seven,
with nothing on the paper saying so. Three pounds ten is missing and the report is internally
consistent.

And the last part is about cost. On four aisles it does not matter how any of this is written. On a
hundred thousand products the same code takes two seconds instead of twenty-five milliseconds, because
one way describes the operation once and the other way starts a hundred thousand small jobs.

---

## §2 The map

Six sections. The first three are the operation and its two shapes; the fourth is everything that
decides which rows are in the answer; the fifth is the escape hatch and what it costs; the last is
where it meets the project's code.

| Section | What it means |
|---|---|
| **1.x** | **The split** — what a group-by is, and the object that computes nothing |
| **2.x** | **Aggregating** — one row per group, and the four ways to ask for several at once |
| **3.x** | **Transform** — one row per original row, and the calculations only it can do |
| **4.x** | **The keys** — where the key goes, what order, which rows, and the ones that never happened |
| **5.x** | **Filter and apply** — whole groups, arbitrary functions, and the price of both |
| **6.x** | **The module** — the rules written down, and one promise no test can defend |

### Section 1 — the split

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [Four lines, three aisles](parts/01-the-split/1.1-four-lines-three-aisles.md) | What is split–apply–combine? | `foundation` |
| 1.2 | [The object that computed nothing](parts/01-the-split/1.2-the-object-that-computed-nothing.md) | Why does `groupby` return so fast? | `foundation` |
| 1.3 | [What iterating gives you](parts/01-the-split/1.3-what-iterating-gives-you.md) | Looking at the piles, and why not to compute from them | `working` |

### Section 2 — aggregating

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [One number for each group](parts/02-aggregating/2.1-one-number-for-each-group.md) | The reduction, and picking the column first | `foundation` |
| 2.2 | [`size` counts rows, `count` counts values](parts/02-aggregating/2.2-size-counts-rows-count-counts-values.md) | Two kinds of "how many", two shapes | `working` |
| 2.3 | [`agg` — several answers at once](parts/02-aggregating/2.3-agg-several-answers-at-once.md) | Four summaries in one pass, and the two-level header | `working` |
| 2.4 | [Named aggregation](parts/02-aggregating/2.4-named-aggregation.md) | Flat columns, named for what they mean | `production` |

### Section 3 — transform

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [A number for every row](parts/03-transform/3.1-a-number-for-every-row.md) | Putting the group's answer back on the row | `working` |
| 3.2 | [The share of the aisle](parts/03-transform/3.2-the-share-of-the-aisle.md) | Each row's share of its own group, and the check | `working` |
| 3.3 | [`transform` and `agg` — the shape rule](parts/03-transform/3.3-transform-and-agg-the-shape-rule.md) | The one question to ask before every group-by | `production` |

### Section 4 — the keys

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [The key became the index](parts/04-the-keys/4.1-the-key-became-the-index.md) | Why `result["aisle"]` raises | `working` |
| 4.2 | [`sort`, and the order of the groups](parts/04-the-keys/4.2-sort-and-the-order-of-the-groups.md) | Alphabetical, first-seen, or by value | `working` |
| 4.3 | [`dropna`, and the rows that vanished](parts/04-the-keys/4.3-dropna-and-the-rows-that-vanished.md) | The report that does not add up | `production` |
| 4.4 | [Two keys, and the MultiIndex](parts/04-the-keys/4.4-two-keys-and-the-multiindex.md) | Groups by combination, and getting back out | `working` |
| 4.5 | [`observed`, and the aisle nobody visited](parts/04-the-keys/4.5-observed-and-the-aisle-nobody-visited.md) | Three rows of data, sixty thousand rows of report | `production` |

### Section 5 — filter and apply

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`filter` — keeping whole groups](parts/05-filter-and-apply/5.1-filter-keeping-whole-groups.md) | Dropping the one-line aisles | `working` |
| 5.2 | [`apply` — the escape hatch](parts/05-filter-and-apply/5.2-apply-the-escape-hatch.md) | The dearest line in each aisle | `working` |
| 5.3 | [What `apply` costs, measured](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md) | Two times on ten groups, eighty on a hundred thousand | `production` |

### Section 6 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`src/setu/grouping.py`](parts/06-the-module/6.1-the-grouping-module.md) | Where does each of the day's rules live? | `production` |
| 6.2 | [The test that can go red](parts/06-the-module/6.2-the-test-that-can-go-red.md) | Testing a shape, and the promise you cannot test | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-31-groupby/lab
touch src/setu/grouping.py tests/test_grouping.py
uv run python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

Expected: `3.0.5 2.5.2`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5
pyarrow==25.0.1`.

Confirm the two facts the whole day rests on — the two shapes, and the rows that go missing:

```bash
uv run python -c "
import pandas as pd
shop = pd.DataFrame({
    'item':  ['milk', 'bread', 'eggs', 'rice', 'tea'],
    'aisle': ['dairy', 'bakery', 'dairy', 'dry', None],
    'spend': [2.30, 1.40, 1.92, 2.05, 3.10],
})
g = shop.groupby('aisle')['spend']
print('agg       :', g.sum().shape, g.sum().index.name, g.sum().to_dict())
print('transform :', g.transform('sum').shape, g.transform('sum').index.name)
print('rows in   :', len(shop))
print('rows out  :', int(g.size().sum()))
print('total in  :', round(shop['spend'].sum(), 2))
print('total out :', round(g.sum().sum(), 2))
"
```

Expected: an `agg` of shape `(3,)` indexed by `aisle`, a `transform` of shape `(5,)` indexed by
nothing, **four rows out of five**, and `7.67` against `10.77`. **Those last two lines are the day's
most important default** — a row whose key is blank is deleted, silently
([4.3](parts/04-the-keys/4.3-dropna-and-the-rows-that-vanished.md)).

One warning about section 5: the benchmark in
[5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md) builds four frames of half a million
rows and runs several two-second timings. That is not a flaw in the script.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/grouping.py`** — [6.1](parts/06-the-module/6.1-the-grouping-module.md) walks through the
whole module.

- `UNKNOWN`, `MIN_GROUP_ROWS` and `SPEND_SUMMARY` — the day's three policy decisions, as module
  constants. `SPEND_SUMMARY` is a named-aggregation spec
  ([2.4](parts/02-aggregating/2.4-named-aggregation.md)).
- `GroupingError(ValueError)` — for a grouping that did not account for every row or did not return
  the shape it promised. Import Day 28's `SelectionError` and Day 30's `ImputationError` rather than
  defining a sixth exception.
- `summarise(frame, by, spec)` — one row per **group**, keys as columns, `observed=True`,
  `dropna=False`, blank keys filled and logged, and the row count reconciled
  ([4.3](parts/04-the-keys/4.3-dropna-and-the-rows-that-vanished.md)).
- `add_group_stats(frame, value, by)` — one row per **original row**, index asserted, three transforms
  from one `GroupBy` ([3.3](parts/03-transform/3.3-transform-and-agg-the-shape-rule.md)).
- `share_of_group(frame, value, by)` — refuses on an incomplete column, blanks zero-total and
  single-row groups, checks the shares sum to one with a tolerance
  ([3.2](parts/03-transform/3.2-the-share-of-the-aisle.md)).
- `drop_small_groups(frame, by, min_rows)` — `transform("size")` and a mask, **not** `filter`, with the
  dropped rows and groups logged ([5.1](parts/05-filter-and-apply/5.1-filter-keeping-whole-groups.md)).
- `top_rows_per_group(frame, by, order, n)` — `sort_values` then `head`, **not** `apply`
  ([5.2](parts/05-filter-and-apply/5.2-apply-the-escape-hatch.md)).
- `spend_grid(frame, rows, columns)` — **as given, this calls `.fillna(0)` on the pivoted result**,
  which turns "this pair never occurred" into "it occurred and came to nothing"
  ([4.4](parts/04-the-keys/4.4-two-keys-and-the-multiindex.md)).
- `TODO(me)`: fix `spend_grid`. Add an `absent: float | None = None` parameter and make the caller
  decide. Then write one sentence in the docstring saying what each of the two meanings implies for a
  per-column average.
- `TODO(me)`: add `blank_key_report(frame, keys)` returning, per key column, how many rows have a
  blank key and what share of the total value those rows carry. Say in a comment why the *share of
  value* matters more than the count.
- `TODO(me)`: `summarise` reconciles the row count. Add a second reconciliation on a value column, and
  answer in a comment: why must that one use a tolerance rather than `==`?
  ([6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) has the reason.)

**`tests/test_grouping.py`** — [6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) walks
through the whole file.

- A fixture with **uneven groups, a single-row group and a blank key** — plus a test asserting the
  fixture has all three.
- Assertions on the **shape**: the return type, the keys as columns, the plain integer index, and a
  transform's index equal to its input's.
- The reconciliation test: the group sizes sum to the row count.
- `TODO(me)`: add a second fixture whose key is a `category` with two unused categories, and a test
  asserting `summarise` returns one row per **observed** value
  ([4.5](parts/04-the-keys/4.5-observed-and-the-aisle-nobody-visited.md)).
- `TODO(me)`: write the tests for your fixed `spend_grid` — at least one asserting that an unobserved
  pair is blank by default, and one asserting it is zero when the caller asks for zero.
- `TODO(me)`: break the module a **second** way of your own — not the `dropna=False` deletion and not
  the `as_index=False` deletion. Watch what goes red, then record the change and the failure count in
  a `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say
  which test should have caught it and why it did not.

**`lab/group_cost.py`** — the day's measurement, made runnable.

- Build the four frames from [5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md) with
  the day's seed, holding the row count fixed and varying the group count.
- Time the string reduction against the lambda for each, and print the ratio.
- `TODO(me)`: add `transform` to the comparison, both ways, and say in a comment why its ratio is
  larger than `agg`'s.
- `TODO(me)`: run it twice on the same machine and record both sets of numbers at the top. Say which
  column moved between runs and which did not, and what that means for which numbers you would quote
  ([Day 29, 3.1](../day-29-iteration-and-order/parts/03-the-measurement/3.1-what-a-million-rows-is-for.md)).

---

## §5 The eval that must be able to fail

`tests/test_grouping.py` is RED until `src/setu/grouping.py` exists. Write these two first, because
they are the two that carry the day:

```python
def test_every_row_is_accounted_for(shop: pd.DataFrame) -> None:
    """A grouping that loses a row is a grouping that is lying."""
    out = summarise(shop, ["aisle"])
    assert shop["aisle"].isna().any(), "the fixture must have a blank key"
    assert int(out["lines"].sum()) == len(shop)


def test_group_stats_are_aligned_to_the_input(shop: pd.DataFrame) -> None:
    stats = add_group_stats(shop, "spend", ["aisle"])
    assert stats.index.equals(shop.index)
    assert shop.assign(**stats)["spend_group_total"].notna().all()
```

**The assertion on the fixture is the point of the first one.** Without a blank key in the fixture,
`dropna=False` and `dropna=True` give the same answer and the test passes whether or not the module
handles it — which is exactly the fixture failure Day 29 found in its own suite
([Day 29, 6.2](../day-29-iteration-and-order/parts/06-the-module/6.2-the-test-that-can-go-red.md)).

**The index assertion is the point of the second one.** A `transform` rewritten as an `agg` produces a
column of `NaN` when assigned, silently
([3.3](parts/03-transform/3.3-transform-and-agg-the-shape-rule.md)), and no assertion on the *values*
can tell the difference — because there are no values.

**The mutations to watch.** Three, and they behave differently:

1. Delete `dropna=False` from `summarise`. **One test goes red**, with `assert 4 == 5`. Every other
   test passes, because every other test looks at aisles that had a key.
2. Delete `as_index=False`. **The shape tests go red**, because the return becomes a Series and
   `out["aisle"]` raises. This is the loud one.
3. Rewrite `add_group_stats` with `.agg(...)` instead of `.transform(...)`. **The index test goes
   red**; the value tests would have passed, because a column of blanks has no wrong values in it.

And one that **no correctness test can catch**: replace `drop_small_groups`' `transform("size")` with
`filter(lambda b: len(b) >= min_rows)`. The output is identical, the suite stays green, and the
function is eighty times slower at a hundred thousand groups
([5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md)). The defences are a docstring for
the reviewer and a separate benchmark
([Day 25, 5.2](../day-25-copy-view-and-the-gate/parts/05-the-gate/5.2-the-performance-test-in-ci.md)).

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed.

The only cost today is patience: the benchmark in
[5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md) builds four frames of half a million
rows — a few megabytes each — and several of its timings take a second or two. Nothing is written to
disk and nothing is downloaded.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **`groupby` computes nothing.** It returns immediately because it has done no work
  ([1.2](parts/01-the-split/1.2-the-object-that-computed-nothing.md)).
- **Aggregating a frame aggregates every column**, including text ones, where `sum` concatenates and
  `max` picks alphabetically ([2.1](parts/02-aggregating/2.1-one-number-for-each-group.md),
  [2.3](parts/02-aggregating/2.3-agg-several-answers-at-once.md)).
- **`size` and `count` are different questions and different shapes.** `size` is rows and returns a
  Series; `count` is values and returns a frame
  ([2.2](parts/02-aggregating/2.2-size-counts-rows-count-counts-values.md)).
- **A group with no known values sums to `0.00`** and means `NaN`. `min_count=1` fixes the first
  ([2.2](parts/02-aggregating/2.2-size-counts-rows-count-counts-values.md)).
- **`agg` with two reductions on one column gives a two-level column index**, and `result["sum"]`
  raises ([2.3](parts/02-aggregating/2.3-agg-several-answers-at-once.md)).
- **A lambda inside a group-by is one Python call per group** — about eighty times slower than the
  string at a hundred thousand groups
  ([5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md)).
- **Assigning an `agg` result to a column gives all `NaN`**, silently, because the index is the key
  ([3.1](parts/03-transform/3.1-a-number-for-every-row.md)). Worse, it gives a *partly* filled column
  when the frame's index shares labels with the keys.
- **A `transform` whose function returns the wrong shape does not raise** — it returns the original
  values ([3.1](parts/03-transform/3.1-a-number-for-every-row.md)).
- **Shares of a column with blanks in it still sum to one**, and are shares of the known total
  ([3.2](parts/03-transform/3.2-the-share-of-the-aisle.md)).
- **Rounding before a sum-to-one check** turns three thirds into `0.999`
  ([3.2](parts/03-transform/3.2-the-share-of-the-aisle.md)).
- **`result["aisle"]` raises after an aggregation.** The key is the index's *name*, not a column
  ([4.1](parts/04-the-keys/4.1-the-key-became-the-index.md)).
- **`reset_index(drop=True)` throws the key away**, leaving anonymous numbers
  ([4.1](parts/04-the-keys/4.1-the-key-became-the-index.md)).
- **Grouping by a Series with a different index silently returns nothing**
  ([4.1](parts/04-the-keys/4.1-the-key-became-the-index.md)).
- **`sort=False` means first-seen order, not original row order**
  ([4.2](parts/04-the-keys/4.2-sort-and-the-order-of-the-groups.md)).
- **Rows with a blank key are deleted by default**, and the report still adds up internally
  ([4.3](parts/04-the-keys/4.3-dropna-and-the-rows-that-vanished.md)). **SQL's `GROUP BY` keeps them**,
  so the same analysis in two places disagrees.
- **With two keys a row is dropped if either is blank** — the loss multiplies with the number of keys
  ([4.4](parts/04-the-keys/4.4-two-keys-and-the-multiindex.md)).
- **`both["dairy"]` fails on a `MultiIndex` when `dairy` is on the inner level**, while
  `both["main"]` works ([4.4](parts/04-the-keys/4.4-two-keys-and-the-multiindex.md)).
- **`unstack` creates cells for pairs that never occurred**, and filling them with zero is a claim
  ([4.4](parts/04-the-keys/4.4-two-keys-and-the-multiindex.md)).
- **On a categorical key, `observed=False` emits every declared category** — three rows of data can
  become sixty thousand rows of report
  ([4.5](parts/04-the-keys/4.5-observed-and-the-aisle-nobody-visited.md)).
- **`DataFrame.filter` selects columns**; `GroupBy.filter` selects rows by group. Same word, unrelated
  jobs ([5.1](parts/05-filter-and-apply/5.1-filter-keeping-whole-groups.md)).
- **`apply`'s output shape depends on what your function returned**, so it can change with the data
  ([5.2](parts/05-filter-and-apply/5.2-apply-the-escape-hatch.md)).
- **`pd.Series({"n": 2, "total": 4.22})` inside an `apply` makes the count a float**
  ([5.2](parts/05-filter-and-apply/5.2-apply-the-escape-hatch.md)).
- **Two float results of the same calculation compare unequal with `equals`**, differing in the last
  bit ([5.3](parts/05-filter-and-apply/5.3-what-apply-costs-measured.md)).

**The pattern behind the day.** Section 2 and 3's failures are about **shape** — a plausible object of
the wrong kind. Section 4's are about **which rows are in the answer**, and every one of them produces
a report that is internally consistent and quietly short. Section 5's are about **cost**, and they are
the honest kind: the code is correct and slow. Only the third kind announces itself, and only by
taking too long.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Group by: split-apply-combine** — <https://pandas.pydata.org/docs/user_guide/groupby.html> — the
  user guide's own three-step framing, the aggregation/transformation/filtration split, and the
  section on `observed` for categorical keys.
- **`DataFrame.groupby`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html> — read the defaults for
  `sort`, `dropna`, `as_index` and `observed`, and note which of them changed in pandas 3.
- **`DataFrameGroupBy.agg`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.aggregate.html> —
  the three argument forms, and the named-aggregation syntax.
- **`DataFrameGroupBy.transform`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.transform.html> —
  confirm for yourself what it says about the shape the passed function must return.
- **`DataFrameGroupBy.apply`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.apply.html> —
  read what it says about the grouping columns and `include_groups`, which changed in pandas 3.

---

## §9 Say it in an interview

> A group-by answers one shape of question: for each distinct value of some column, what is the answer
> for the rows carrying it. Split into piles, apply a calculation to each, combine the answers. The
> thing worth being precise about is that the combining step has two possible shapes, and choosing
> between them is most of the skill. `agg` gives one row per group, indexed by the key — that is a
> report. `transform` gives one row per original row, indexed like the frame — that is a column. The
> arithmetic is identical. If you assign an `agg` result to a column of the frame it came from, pandas
> aligns the group keys against the row labels, nothing matches, and you get a column of nulls with no
> error at all; that is the single most common group-by bug and it is why "am I asking about the
> groups or about the rows" is the first question.
>
> The arguments matter more than people expect, and I set them explicitly. `dropna` defaults to true,
> so rows whose **key** is missing are deleted before grouping — the group totals then sum to less
> than the column total and nothing in the output says so. SQL's `GROUP BY` keeps nulls as their own
> group, so the same analysis in two places will disagree by a few per cent that nobody can account
> for. With two keys a row goes if either is blank, so the loss grows exactly as the breakdown gets
> more useful. My habit is to fill the key with an explicit label before grouping, and to assert that
> the group sizes add up to the row count. `observed` matters when the key is categorical: with
> `observed=False` you get a row per declared category, empty ones sum to zero — indistinguishable
> from a real zero — and with two categorical keys the number of groups is the product of the category
> lists, which is a genuine way to run out of memory on three rows of data.
>
> On performance, the rule is not the usual one about row counts. A string reduction — `agg("mean")` —
> runs one compiled pass. A lambda is called once per group, so its cost scales with the number of
> **groups**, not rows. On half a million rows with ten groups a lambda is twice as slow; with a
> hundred thousand groups it is about eighty times. `transform` with a lambda is worse again because
> it pays the per-group call and then scatters the result back across every row. So I check
> `nunique()` on the key before writing an `apply`, and for the common cases I write the compiled
> equivalents: `sort_values` plus `head` for top-N per group, and `transform("size")` with a mask
> instead of `filter`.
>
> The thing I would not compromise on is the reconciliation. Every grouping I ship asserts that the
> group sizes sum to the frame's row count, because the failure mode of this whole subject is a report
> that is internally consistent and quietly missing rows — and no assertion on any individual total
> would ever catch it.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 31` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
