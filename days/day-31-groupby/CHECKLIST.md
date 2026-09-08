# Day 31 — Definition of done

`PD-08` split–apply–combine, `agg` and `transform` — with the plan's named example, mean spend per
aisle per shop in one expression.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints a reconciled report, an aligned column
block, and the same five rows accounted for:

```bash
uv run python -c "
import pandas as pd
from setu.grouping import add_group_stats, summarise

shop = pd.DataFrame({
    'item':  ['milk', 'bread', 'eggs', 'rice', 'tea'],
    'aisle': ['dairy', 'bakery', 'dairy', 'dry', None],
    'shop':  ['main', 'main', 'corner', 'main', 'corner'],
    'need':  [2, 1, 6, 1, 1],
    'price': [1.15, 1.40, 0.32, 2.05, 3.10],
})
shop['spend'] = shop['need'] * shop['price']

report = summarise(shop, ['aisle'])
print(report)
print('rows accounted for :', int(report['lines'].sum()), 'of', len(shop))
print('total accounted for:', round(report['total'].sum(), 2), 'of', round(shop['spend'].sum(), 2))
print()
stats = add_group_stats(shop, 'spend', ['aisle'])
print(shop.assign(**stats)[['item', 'aisle', 'spend', 'spend_group_total', 'rows_in_group']])
print()
print(summarise(shop, ['shop', 'aisle']))
"
```

The row count and the total must both reconcile, and the `spend_group_total` column must have no
blanks in it. If either fails, sections 3 and 4 have not landed.

---

## Setup

- [ ] Ran `./m scaffold 31` and created `src/setu/grouping.py` and `tests/test_grouping.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `numpy.__version__` is `2.5.2`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and saw the two shapes: `(3,)` indexed by `aisle`, `(5,)` indexed by nothing
- [ ] Saw **4 rows out of 5** and `7.67` against `10.77`, and can say where the missing £3.10 went
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — the split

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Can name the three steps of split–apply–combine without looking
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] Can say why looping over a `GroupBy` is the clearest way to look and the worst way to compute

## Section 2 — aggregating

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Watched an aggregation concatenate a text column, and can say why narrowing first prevents it
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say which of `size` and `count` `mean()` divides by, and what shape each returns
- [ ] Saw a group with no known values sum to `0.00` and average to `NaN`
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Saw `KeyError: 'sum'` on a two-level column index, and can say why the word is in the printout
- [ ] Measured the string-versus-lambda ratio on my own machine
- [ ] **2.4** read · ran its check-yourself · answered its question out loud
- [ ] Can write a named-aggregation argument from memory: keyword, column, reduction

## Section 3 — transform

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] Watched an `agg` result assigned to a column come out entirely `NaN`
- [ ] Reproduced the *partly* filled version, where the frame's index shares labels with the keys
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Ran the shares-sum-to-one check, and saw it pass on a column that had blanks in it
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Can state the one question that decides between `agg` and `transform`, in one sentence

## Section 4 — the keys

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw `KeyError: 'aisle'` on an aggregation result, and can say what `aisle` is instead
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Pasted two group-bys side by side with different orders and watched the rows misalign
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] **Reconciled a report myself** and found the missing rows
- [ ] Can say what SQL's `GROUP BY` does with a NULL key, and why that matters
- [ ] **4.4** read · ran its check-yourself · answered its question out loud
- [ ] Saw a two-key group-by lose rows to *either* blank key
- [ ] **4.5** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced three rows of data becoming sixty thousand rows of report

## Section 5 — filter and apply

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say why a plain row mask cannot express "keep the groups with at least two rows"
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw an `apply` return three different shapes depending on what the function returned
- [ ] Saw a count come back as a float from a `pd.Series` inside an `apply`
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] **Ran the group-count benchmark on my own machine** and recorded the four ratios
- [ ] Can say which quantity a lambda in a group-by scales with, and which a string reduction does

## Section 6 — the module

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] Can name the three promises the module makes
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Can name the one promise no correctness test can defend, and what to do instead

## Build

- [ ] `src/setu/grouping.py` exists with `UNKNOWN`, `MIN_GROUP_ROWS`, `SPEND_SUMMARY` and
      `GroupingError`
- [ ] `SelectionError` and `ImputationError` are **imported** from Days 28 and 30, not redefined
- [ ] Every `groupby` in the module passes `observed` and `dropna` explicitly
- [ ] `summarise` returns a frame with the keys as columns and reconciles the row count
- [ ] `summarise` refuses a spec with no group size
- [ ] `add_group_stats` asserts its index equals the input's, and computes three columns from one
      `GroupBy`
- [ ] `share_of_group` refuses on an incomplete column and blanks single-row and zero-total groups
- [ ] `drop_small_groups` uses `transform("size")` and a mask, and logs rows **and** groups dropped
- [ ] `top_rows_per_group` uses `sort_values` + `head`, with a stable sort
- [ ] `TODO(me)`: fixed `spend_grid` — added `absent: float | None = None` and documented both
      meanings
- [ ] `TODO(me)`: added `blank_key_report`, and said in a comment why the share of *value* matters
      more than the count
- [ ] `TODO(me)`: added a value reconciliation to `summarise`, and answered why it needs a tolerance
- [ ] `lab/group_cost.py` runs and prints four ratios at four group counts
- [ ] `TODO(me)`: added `transform` to the benchmark and explained why its ratio is larger
- [ ] `TODO(me)`: ran the benchmark twice and recorded both sets of numbers

## Tests

- [ ] `tests/test_grouping.py` uses a **fixture** with uneven groups, a single-row group and a blank
      key
- [ ] There is a test asserting the fixture has all three of those properties
- [ ] The reconciliation test asserts the group sizes sum to the row count
- [ ] The shape tests assert the return type, the keys as columns, and the plain integer index
- [ ] The alignment test asserts `stats.index.equals(frame.index)` **and** that an assignment lands
- [ ] `pytest.raises` is used with `match=`, on a fragment rather than a whole sentence
- [ ] Float comparisons use a tolerance or a rounding, never `==`
- [ ] **Break it (1):** deleted `dropna=False` and watched **one** test go red
- [ ] **Break it (2):** deleted `as_index=False` and watched the shape tests go red
- [ ] **Break it (3):** rewrote `add_group_stats` with `.agg(...)` and watched the index test go red
- [ ] **Break it (4):** replaced `transform("size")` with `filter(...)` and watched the suite stay
      **green**
- [ ] Can explain what (4) proves about what a correctness suite defends
- [ ] `TODO(me)`: added the categorical fixture and the `observed` test
- [ ] `TODO(me)`: wrote the tests for the fixed `spend_grid`
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-31-groupby/ src/setu/grouping.py tests/test_grouping.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 31` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 31` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-08` and quotes my own group-count ratio from `lab/group_cost.py`
