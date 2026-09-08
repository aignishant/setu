---
day: 32
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 32 — Merge, join, concat, pivot, melt"
ids: ["PD-09", "PD-10"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 19
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 32 — Merge, join, concat, pivot, melt

**Phase 4 · Pandas 3.0 · Module 4** · `PD-09` combining tables — `concat`, `merge`, `join` ·
`PD-10` reshaping — `pivot`, `melt`, `stack`, `unstack`.

> **Yesterday:** one question shape — for each value of this column, what is the answer for the rows
> that carry it — and the two shapes its answer can take.
> **Today:** two tables instead of one. How to put them together, the two directions a join can move
> the row count, and why that movement is invisible in the result. Then the same data in two shapes —
> one row per measurement and one row per thing — and the four operations that convert between them.
> **Tomorrow:** text and time — the `.str` and `.dt` accessors, and resampling, which is grouping by a
> key you have to build first.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Two pieces of paper on the kitchen table.

One is the shopping list somebody wrote this morning: milk, bread, eggs, rice, with how many of each.
The other is the list of what things cost, kept by somebody else, which has milk, bread, eggs and tea
on it — tea because it was bought last month, and no rice because rice has never been priced.

Somebody wants one sheet with everything on it. What they do is obvious: take the milk line, find
*milk* on the price sheet, write the price next to it. Then bread. Then eggs.

Then rice, and there is no rice on the price sheet. Keep the line with an empty box, because you still
have to buy rice? Or leave it off, because you cannot cost it? And separately, is the tea on the
combined sheet, given that nobody is buying tea?

Two four-line sheets, three items in common, and **four defensible answers with between three and five
rows.** That is the first half of the day: a join is a decision about the rows that do not match, and
the default is the one that silently deletes them.

The second half is a different shape of trouble. The price sheet gains a second row for milk, because
the price went up in June and somebody sensibly kept both. Now every milk line on the shopping list
pairs with *both* prices, so four rows become six, the quantities are counted twice, and the total
goes up by half. Nothing failed. Nothing warned. **A join is the only common operation whose output
size is not determined by its inputs' sizes**, and the number that would have told you is the row
count, which nobody printed.

Then the third part, which is not about joining at all. The price sheet is a grid: items down the
side, months across the top. Perfectly readable, and useless — you cannot join to a month that is a
column heading rather than a value, you cannot group by it, and adding April means editing every piece
of code that named the months. Turn it on its side, one row per measurement, and all three problems
go away — at the cost of a table nobody can read at a glance.

So the day has one shape running through both halves: **two tables meeting is a decision about rows,
and one table's shape is a decision about who is going to read it.** Store the shape a computer wants,
and turn it into the shape a person wants at the last possible moment.

---

## §2 The map

Six sections. The first three are `PD-09` — putting tables together and checking what happened to the
rows. The next two are `PD-10` — the two directions of reshaping. The last is where both meet the
project's code.

| Section | What it means |
|---|---|
| **1.x** | **Stacking** — `concat`, which matches nothing and just puts one table after another |
| **2.x** | **Merging** — matching on a key, and the four answers to "what about the rows that did not" |
| **3.x** | **The row count** — the two directions it can move, and the checks that see them |
| **4.x** | **Wide to long** — `melt`, and naming both ends of it |
| **5.x** | **Long to wide** — `pivot`, its refusal, and the index-based pair |
| **6.x** | **The module** — the rules written down, and a test that can actually go red |

### Section 1 — stacking

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [Two lists, one under the other](parts/01-stacking/1.1-two-lists-one-under-the-other.md) | What does `concat` do, and what does it not do? | `foundation` |
| 1.2 | [The index that came along](parts/01-stacking/1.2-the-index-that-came-along.md) | Why are there two rows labelled `0`? | `working` |
| 1.3 | [The columns that did not match](parts/01-stacking/1.3-the-columns-that-did-not-match.md) | What happens when the two tables differ? | `working` |
| 1.4 | [Stacking sideways](parts/01-stacking/1.4-stacking-sideways.md) | `axis=1`, and the alignment underneath it | `working` |

### Section 2 — merging

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [The key, and the rows it pairs](parts/02-merging/2.1-the-key-and-the-rows-it-pairs.md) | What `merge` matches on, and what `concat` does not | `foundation` |
| 2.2 | [The four `how`s, on four rows](parts/02-merging/2.2-the-four-hows-on-four-rows.md) | Three, four, four and five rows from the same tables | `working` |
| 2.3 | [When the key has two names](parts/02-merging/2.3-when-the-key-has-two-names.md) | `left_on`, `right_on`, and why to rename instead | `working` |
| 2.4 | [The suffixes, and the column on both sides](parts/02-merging/2.4-the-suffixes-and-the-column-on-both-sides.md) | Why `note_x` is dangerous rather than merely ugly | `production` |

### Section 3 — the row count

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [Count the rows, before and after](parts/03-the-row-count/3.1-count-the-rows-before-and-after.md) | The two numbers you print every time | `working` |
| 3.2 | [The duplicate that multiplied rows](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md) | Two thousand rows in, a million out | `production` |
| 3.3 | [`validate`, and the merge error](parts/03-the-row-count/3.3-validate-and-the-merge-error.md) | One keyword that turns a silent bug into an error | `production` |
| 3.4 | [The join that dropped forty per cent](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md) | 40% of rows, 67% of the revenue, no error | `production` |

### Section 4 — wide to long

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [`melt` — one row per measurement](parts/04-wide-to-long/4.1-melt-one-row-per-measurement.md) | Turning column headings into values | `foundation` |
| 4.2 | [`id_vars`, `value_vars`, and the names you choose](parts/04-wide-to-long/4.2-id-vars-value-vars-and-the-names-you-choose.md) | Naming both ends, and retyping the heading column | `production` |

### Section 5 — long to wide

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`pivot` — one row per thing](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md) | The grid, and when to build it | `working` |
| 5.2 | [The duplicate that makes `pivot` raise](parts/05-long-to-wide/5.2-the-duplicate-that-makes-pivot-raise.md) | Why the refusal beats `pivot_table`'s convenience | `working` |
| 5.3 | [`stack` and `unstack`](parts/05-long-to-wide/5.3-stack-and-unstack.md) | The same two reshapes, through the index | `production` |

### Section 6 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`src/setu/joining.py`](parts/06-the-module/6.1-the-joining-module.md) | Where does each of the day's rules live? | `production` |
| 6.2 | [The test that can go red](parts/06-the-module/6.2-the-test-that-can-go-red.md) | Testing a row count, a match rate and a total | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-32-joining-and-reshaping/lab
touch src/setu/joining.py tests/test_joining.py
uv run python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

Expected: `3.0.5 2.5.2`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5
pyarrow==25.0.1`.

Confirm the two facts the whole day rests on — the four row counts, and the multiplication:

```bash
uv run python -c "
import pandas as pd
wanted = pd.DataFrame({'item': ['milk', 'bread', 'eggs', 'rice'], 'need': [2, 1, 6, 1]})
prices = pd.DataFrame({'item': ['milk', 'bread', 'eggs', 'tea'], 'price': [1.15, 1.40, 0.32, 3.10]})
for how in ('inner', 'left', 'right', 'outer'):
    print(f'{how:6} {len(wanted.merge(prices, on=\"item\", how=how))} rows')
print()
dup = pd.DataFrame({'item': ['milk', 'milk', 'bread'], 'price': [1.15, 1.20, 1.40]})
out = wanted.merge(dup, on='item', how='left')
print('left join against a duplicated lookup:', len(wanted), '->', len(out), 'rows')
print('need total                          :', wanted['need'].sum(), '->', out['need'].sum())
"
```

Expected: `3, 4, 4, 5` for the four `how`s, and then **4 rows becoming 5 with the `need` total rising
from 10 to 12**. That second block is the day's most expensive default — a left join guarantees no row
is lost and guarantees nothing about the row count
([3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md)).

One warning about section 3: the simulation in
[3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md) builds five thousand rows
and the arithmetic block in [3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md)
builds a million-row join. Neither is slow; both are there because the numbers are the argument.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/joining.py`** — [6.1](parts/06-the-module/6.1-the-joining-module.md) walks through the
whole module.

- `RELATIONSHIPS` and `MAX_UNMATCHED` — the day's two policy decisions, as module constants.
- `JoinError(ValueError)` — for a join that did not pair the rows it promised. Import Day 28's
  `SelectionError` and Day 31's `GroupingError` rather than defining a seventh exception.
- `join(detail, lookup, on, relationship, weight, how, max_unmatched)` — `relationship` **required**,
  `validate=` passed through, `indicator=True` always, and the unmatched share measured against a
  weight column as well as a row count
  ([3.3](parts/03-the-row-count/3.3-validate-and-the-merge-error.md),
  [3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md)).
- `stack_frames(frames, ...)` — `concat` with the row counts asserted to add up
  ([1.1](parts/01-stacking/1.1-two-lists-one-under-the-other.md)).
- `to_long(wide, id_vars, value_vars, var_name, value_name, var_order)` — both lists required, the
  columns must partition, the heading column retyped
  ([4.2](parts/04-wide-to-long/4.2-id-vars-value-vars-and-the-names-you-choose.md)).
- `to_grid(long, index, columns, values, column_order, absent)` — duplicates checked first and named,
  no `aggfunc`, the absent-cell meaning required
  ([5.1](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md),
  [5.2](parts/05-long-to-wide/5.2-the-duplicate-that-makes-pivot-raise.md)).
- `enrich(detail, lookup, on)` — **as given, this is a bare left join with no `validate`, no
  indicator and no assertion.** It multiplies rows against a duplicated lookup and is blind to a join
  that matched nothing ([6.1](parts/06-the-module/6.1-the-joining-module.md)).
- `TODO(me)`: fix `enrich`. Make it delegate to `join` with a relationship the caller must supply, and
  state in the docstring what the row count of the result is guaranteed to be.
- `TODO(me)`: add `key_report(left, right, on)` returning, for one key: how many distinct values each
  side has, how many are on both, how many are on one side only, and — if a weight column is given —
  what share of the weight the unmatched keys carry. Say in a comment why the weight share is the
  number worth alerting on.
- `TODO(me)`: `to_grid` refuses duplicates. Add a `guard_size` check that refuses when
  `index cardinality × columns cardinality` exceeds a limit, and answer in a comment why the input's
  row count does not predict that number
  ([5.1](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md)).

**`tests/test_joining.py`** — [6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) walks through
the whole file.

- Four fixtures: a detail frame with a money column, a clean lookup, a **duplicated** lookup and a
  **mismatched** lookup — plus a test asserting each has the property it is for.
- The three assertions that carry the day: the row count, the match rate, and a total.
- `pytest.raises` with `match=` on a fragment, for both the `MergeError` and the `JoinError`.
- `TODO(me)`: write the tests for your fixed `enrich`, including one asserting it refuses a duplicated
  lookup and one asserting the row count is unchanged against a clean one.
- `TODO(me)`: add a round-trip property test — `to_long` then `to_grid` returns the original values —
  and say in a comment why it compares sorted values rather than frames.
- `TODO(me)`: break the module a **second** way of your own — not the `validate` removal and not the
  indicator removal. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say which
  test should have caught it and why it did not.

**`lab/lost_in_the_join.py`** — the day's most expensive failure, made runnable.

- Build the sales-and-stale-lookup simulation from
  [3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md) with the day's seed.
- Print, for coverage of 100%, 90%, 60% and 30%: the unmatched share of rows and the unmatched share
  of revenue.
- `TODO(me)`: add the mean sale for matched and unmatched rows to the output, and say in a comment
  what a large gap between them tells you about the inner join.
- `TODO(me)`: run it once with the lookup keys lower-cased and once with them capitalised, and record
  both results. Say which of the two failures the row count could have caught.

---

## §5 The eval that must be able to fail

`tests/test_joining.py` is RED until `src/setu/joining.py` exists. Write these two first, because they
are the two that carry the day:

```python
def test_a_duplicated_lookup_is_refused(detail, duplicated_lookup) -> None:
    assert duplicated_lookup.duplicated("item").any(), "the fixture must have a duplicate"
    with pytest.raises(pd.errors.MergeError, match=r"not a many-to-one merge"):
        join(detail, duplicated_lookup, on=["item"], relationship="many_to_one")


def test_a_join_that_matches_nothing_is_refused(detail, mismatched_lookup) -> None:
    with pytest.raises(JoinError, match=r"unmatched"):
        join(detail, mismatched_lookup, on=["item"], relationship="many_to_one", weight="paid")
```

**The assertion on the fixture is the point of the first one.** Without a duplicate in the fixture,
the test passes whether or not `validate` is being passed — the same vacuity Day 29 and Day 31 both
found in their own suites
([Day 31, 6.2](../day-31-groupby/parts/06-the-module/6.2-the-test-that-can-go-red.md)).

**The second test is the one nobody writes.** A left join that matches nothing keeps every row, so no
row-count assertion and no shape check can see it
([3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md)). Delete this test and that
bug ships in silence.

**The mutations to watch.** Three, and they behave differently:

1. Remove `validate=relationship` from `join`. **One test goes red** — the duplicated-lookup one — and
   every other test passes, because every other fixture has a unique lookup.
2. Remove `indicator=True` and the unmatched-share check. **A different single test goes red**, and
   the row-count tests do not notice, because the count is unchanged.
3. In `to_long`, drop the `unaccounted` check. **One test goes red** — the one that adds a
   `loaded_at` column — and nothing else does, because no other fixture has a stray column.

And one that **no correctness test can catch**: change `MAX_UNMATCHED` from `0.01` to `0.9`. Every
test stays green, every function still works, and the pipeline will now happily report on a tenth of
the business. The defences are a test asserting the constant's value and a review that treats a policy
change as a policy change.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed.

The largest things the day builds are the five-thousand-row simulation in
[3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md) and the thousand-by-thousand
join in [3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md), which produces a
million rows — a few tens of megabytes, and the point of the exercise. Nothing is written to disk
except the module, the tests and the lab script.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **`merge` with no `on=` joins on every shared column**, so a metadata column added to both tables
  silently becomes part of the key and nothing matches
  ([2.1](parts/02-merging/2.1-the-key-and-the-rows-it-pairs.md)).
- **Matching is exact.** `Milk` is not `milk` and `'bread '` is not `'bread'`, and an inner join
  silently removes every row that differs
  ([2.1](parts/02-merging/2.1-the-key-and-the-rows-it-pairs.md)).
- **A key with different dtypes on the two sides raises** — which is the lucky version; the silent
  version is a leading zero lost at read time
  ([2.1](parts/02-merging/2.1-the-key-and-the-rows-it-pairs.md)).
- **The default `how` is `inner`, which is a filter**, and its criterion is "exists in the lookup"
  ([2.2](parts/02-merging/2.2-the-four-hows-on-four-rows.md)).
- **A blank introduced by a join changes a column's dtype**, so an integer quantity comes back as
  `2.0` ([2.2](parts/02-merging/2.2-the-four-hows-on-four-rows.md)).
- **An outer join sorts the result** and the others do not, so switching `how` reorders every row
  ([2.2](parts/02-merging/2.2-the-four-hows-on-four-rows.md)).
- **`left_on`/`right_on` lists are matched positionally**, so swapping two names joins the wrong
  columns and returns an empty frame with no error
  ([2.3](parts/02-merging/2.3-when-the-key-has-two-names.md)).
- **Overlapping non-key columns become `_x` and `_y`**, which name a position in a call — so swapping
  the merge's arguments silently inverts them
  ([2.4](parts/02-merging/2.4-the-suffixes-and-the-column-on-both-sides.md)).
- **A left join does not guarantee the row count.** A duplicated key on the right multiplies rows and
  copies the left frame's values, inflating every total
  ([3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md)).
- **A key repeated on both sides gives the cross product** — a thousand each is a million rows, and
  the failure is a memory error unrelated to the input size
  ([3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md)).
- **Deduplicating after a join picks rows arbitrarily** and after the damage
  ([3.2](parts/03-the-row-count/3.2-the-duplicate-that-multiplied-rows.md)).
- **`validate` cannot see a join that matched nothing** — uniqueness still holds
  ([3.3](parts/03-the-row-count/3.3-validate-and-the-merge-error.md)).
- **A left join's row count does not move when nothing matches**, so `indicator=True` is the only
  thing that sees it ([3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md)).
- **The rows that fail to match are not a random sample**, so 40% of rows can be 67% of the revenue
  ([3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md)).
- **A left join followed by a group-by loses the same rows one step later**, because `groupby` drops
  blank keys ([3.4](parts/03-the-row-count/3.4-the-join-that-dropped-forty-per-cent.md)).
- **`melt` with only `id_vars` melts everything else**, including a column added upstream, and the
  value column becomes `object` ([4.1](parts/04-wide-to-long/4.1-melt-one-row-per-measurement.md)).
- **The melted heading column is text**, so `feb` sorts before `jan` in every group-by and chart
  ([4.2](parts/04-wide-to-long/4.2-id-vars-value-vars-and-the-names-you-choose.md)).
- **`pd.Categorical` turns values outside `categories` into blanks, silently**
  ([4.2](parts/04-wide-to-long/4.2-id-vars-value-vars-and-the-names-you-choose.md)).
- **`pivot` puts the index column in the index**, so `grid["item"]` raises
  ([5.1](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md)).
- **`pivot` creates cells for combinations that never occurred**, and filling them with zero is a
  claim ([5.1](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md)).
- **A new category is a new row in long form and a new column in wide form**, so a wide file's schema
  is a function of its contents ([5.1](parts/05-long-to-wide/5.1-pivot-one-row-per-thing.md)).
- **`pivot_table` averages duplicates without saying so**, and its default `aggfunc` is `"mean"`
  ([5.2](parts/05-long-to-wide/5.2-the-duplicate-that-makes-pivot-raise.md)).
- **`unstack()` moves whichever level is innermost**, so adding a key to an upstream group-by
  transposes the result ([5.3](parts/05-long-to-wide/5.3-stack-and-unstack.md)).
- **`stack` keeps blanks in pandas 3** and `dropna=` now raises, so an `unstack().stack()` round trip
  comes back longer than it went in ([5.3](parts/05-long-to-wide/5.3-stack-and-unstack.md)).

**The pattern behind the day.** Section 2's failures are about **which rows are paired**; section 3's
are about **how many rows there are**; sections 4 and 5's are about **what shape the table is in**.
Every one of them produces a well-formed table. Three of the twenty-odd raise an error, and the other
seventeen hand you a frame with the right columns, plausible values and no blanks — which is why every
join gets a row count, a match rate and a total, and every reshape gets both ends named.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Merge, join, concatenate and compare** —
  <https://pandas.pydata.org/docs/user_guide/merging.html> — the user guide's own treatment of all
  four, including the diagram of the `how` values and the section on `validate`.
- **`DataFrame.merge`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html> — read the defaults for
  `how`, `on`, `suffixes`, `indicator` and `validate`, and the four strings `validate` accepts.
- **Reshaping and pivot tables** —
  <https://pandas.pydata.org/docs/user_guide/reshaping.html> — the guide's own picture of `pivot`,
  `melt`, `stack` and `unstack` as one family, and the note on what changed in `stack`.
- **`DataFrame.melt`** — <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html> —
  confirm for yourself what `value_vars` defaults to when it is omitted.
- **`DataFrame.pivot`** — <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html> —
  read what it says about duplicate entries, and compare with `pivot_table`'s `aggfunc` default.

---

## §9 Say it in an interview

> Combining two tables comes in two shapes. `concat` stacks them — nothing is matched, rows are put
> after one another and columns line up by name — and `merge` joins them by matching values in a key
> column. The part worth being precise about is what happens to rows that do not match, because that
> is a decision with four answers and the default is the aggressive one: an inner join keeps only keys
> present on both sides, so it acts as a filter whose criterion has nothing to do with your analysis
> and everything to do with how complete somebody else's reference table happens to be.
>
> The thing I actually check every time is the row count, before and after, because a join is the only
> common operation whose output size is not determined by its inputs' sizes. It can shrink, if keys did
> not match. It can grow, if a key is duplicated on the right — and that one is worse, because the left
> frame's values get copied, so every total computed from them inflates. A left join is often described
> as safe because no row is lost, and that is true and it does not guarantee the row *count*. So I pass
> `validate='many_to_one'`, which asserts the lookup's keys are unique and raises before the multiplied
> frame is built, naming the offending key.
>
> `validate` only guards one direction, though. A join where nothing matched passes validation happily,
> because uniqueness still holds, and under a left join the row count does not move either — every row
> survives with nulls. So I also pass `indicator=True` and check the unmatched share, and I measure it
> against a weight column rather than a row count, because the rows that fail to match are almost never
> a random sample. On a simulation where a stale product lookup is missing the newest items, forty per
> cent of rows unmatched is sixty-seven per cent of the revenue, and the mean sale halves. The row
> count understates it by a factor of two.
>
> Reshaping is the other half. Wide is one row per entity with a column per period; long is one row per
> measurement, with the old headings as values in a column. `melt` goes one way and `pivot` the other,
> and `stack` and `unstack` are the same pair for data whose keys are already in the index — which is
> what a two-key group-by hands you. The rule I follow is store long, present wide: long survives a new
> category as a new row rather than a schema change, it is what group-bys, joins and plotting libraries
> all take, and columnar formats compress its repeated identifiers to nothing. Wide is for the last
> step, when a person has to read it — and at that point I name the column order explicitly, because
> otherwise the months come out alphabetically and the chart goes up, down, up.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 32` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
