# Day 32 — Definition of done

`PD-09` combining tables — `concat`, `merge`, `join` · `PD-10` reshaping — `pivot`, `melt`, `stack`,
`unstack`.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints a guarded join, a refusal, and a round
trip that comes back with the same values:

```bash
uv run python -c "
import pandas as pd
from setu.joining import JoinError, join, to_grid, to_long

MONTHS = ['jan', 'feb', 'mar']

detail = pd.DataFrame({
    'order': [1, 2],
    'item': pd.Series(['milk', 'bread'], dtype='str'),
    'paid': [2.30, 1.40],
})
clean = pd.DataFrame({'item': pd.Series(['milk', 'bread'], dtype='str'), 'price': [1.15, 1.40]})
dupey = pd.DataFrame({'item': pd.Series(['milk', 'milk', 'bread'], dtype='str'), 'price': [1.15, 1.20, 1.40]})

out = join(detail, clean, on=['item'], relationship='many_to_one', weight='paid')
print('rows   :', len(detail), '->', len(out))
print('revenue:', round(detail['paid'].sum(), 2), '->', round(out['paid'].sum(), 2))

try:
    join(detail, dupey, on=['item'], relationship='many_to_one')
except pd.errors.MergeError as e:
    print('refused:', str(e).splitlines()[0])

wide = pd.DataFrame({
    'item': pd.Series(['milk', 'bread'], dtype='str'),
    'jan': [1.15, 1.40], 'feb': [1.15, 1.45], 'mar': [1.20, 1.45],
})
long = to_long(wide, ['item'], MONTHS, 'month', 'price', var_order=MONTHS)
grid = to_grid(long, ['item'], 'month', 'price', column_order=MONTHS)
print('melted :', len(long), 'rows -- expected', len(wide) * len(MONTHS))
print('columns:', list(grid.columns))
print('values kept:', sorted(grid.to_numpy().ravel().round(3)) == sorted(long['price'].round(3)))
"
```

The row count and the revenue must both be unchanged, the duplicated lookup must be refused, and the
grid's columns must be in `MONTHS` order rather than alphabetical. If any of those fails, sections 3
and 4 have not landed.

---

## Setup

- [ ] Ran `./m scaffold 32` and created `src/setu/joining.py` and `tests/test_joining.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `numpy.__version__` is `2.5.2`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and got `3, 4, 4, 5` rows for the four `how`s
- [ ] Saw a **left join** turn 4 rows into 5 and the `need` total rise from 10 to 12
- [ ] Can say why "I used a left join so nothing was lost" is not a safety argument
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — stacking

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say in one word what `concat` matches on, and what `merge` matches on
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] **1.4** read · ran its check-yourself · answered its question out loud

## Section 2 — merging

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Watched a merge with no `on=` join on a metadata column and return an empty frame
- [ ] Saw a capitalised key silently remove two rows out of three
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Can name the four `how`s and say which rows each keeps
- [ ] Saw an integer column become `float64` because a join introduced a blank
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced a composite-key merge returning zero rows because the two lists were in different
      orders
- [ ] **2.4** read · ran its check-yourself · answered its question out loud
- [ ] Swapped a merge's arguments and watched `note_x` change meaning with no error

## Section 3 — the row count

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] **Printed the row count before and after a merge myself**, and a total alongside it
- [ ] Can say why a left join's row count is blind to a join that matched nothing
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced the growth table: 2 × 2, 10 × 10, 100 × 100, 1000 × 1000
- [ ] Can name the four relationship shapes, and say which one almost every real join is
- [ ] Can give the three honest responses to a duplicate on the right
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Saw all four `validate` strings, and read which side each error names
- [ ] Can say what `validate` cannot see, and what to pass in the same call to catch it
- [ ] **3.4** read · ran its check-yourself · answered its question out loud
- [ ] **Measured it myself**: 40% of rows unmatched and 67% of the revenue
- [ ] Compared the mean sale of matched against unmatched rows and saw the gap

## Section 4 — wide to long

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say what happens to a new month in long form and in wide form
- [ ] Watched a column swept into a melt turn the value column into `object`
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw a group-by on a melted month column come out alphabetically
- [ ] Fixed it with an ordered category and saw the order change and the numbers not

## Section 5 — long to wide

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] Can state the store-long-present-wide rule and give the reason
- [ ] Saw a pivot create a cell that did not exist in the long frame
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw `pivot` refuse and `pivot_table` silently average the same duplicate
- [ ] Can say why the refusal is more useful than the convenience
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] Placed all four reshapes in one sentence: `melt`, `pivot`, `stack`, `unstack`
- [ ] Saw an `unstack().stack()` round trip come back **longer** than it went in

## Section 6 — the module

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] Can name the three promises the module makes
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Can name the assertion that catches a join which matched nothing, and why no other one does

## Build

- [ ] `src/setu/joining.py` exists with `RELATIONSHIPS`, `MAX_UNMATCHED` and `JoinError`
- [ ] `SelectionError` and `GroupingError` are **imported** from Days 28 and 31, not redefined
- [ ] `join` takes `relationship` as a **required** argument and passes it to `validate=`
- [ ] `join` passes `indicator=True` and measures the unmatched share against a weight column
- [ ] `join` logs rows in, rows out and both unmatched shares on **every** call
- [ ] `join` guards the empty-frame case so the share is not `nan`
- [ ] `stack_frames` asserts the concatenated row counts add up
- [ ] `to_long` requires both `id_vars` and `value_vars`, and refuses an unaccounted column
- [ ] `to_long` retypes the heading column when `var_order` is given, and refuses values outside it
- [ ] `to_grid` checks for duplicate cells first and names example combinations
- [ ] `to_grid` has **no** `aggfunc`, and takes `column_order` and `absent`
- [ ] `TODO(me)`: fixed `enrich` — delegates to `join`, requires a relationship, states its row-count
      guarantee in the docstring
- [ ] `TODO(me)`: added `key_report`, and said in a comment why the weight share beats the count
- [ ] `TODO(me)`: added the `guard_size` check to `to_grid`, and answered why the row count does not
      predict the grid's size
- [ ] `lab/lost_in_the_join.py` runs and prints unmatched row share and revenue share at four
      coverage levels
- [ ] `TODO(me)`: added the matched/unmatched mean sale to the output with a comment on what the gap
      means
- [ ] `TODO(me)`: ran it with lower-cased and capitalised keys and recorded both results

## Tests

- [ ] `tests/test_joining.py` has four **fixtures**: detail with money, clean, duplicated, mismatched
- [ ] There is a test asserting each fixture has the property it exists for
- [ ] The row-count test asserts the count **and** a total, with `pytest.approx`
- [ ] The duplicated-lookup test asserts the fixture has a duplicate before the `raises` block
- [ ] There is a test that a join matching nothing is refused
- [ ] `pytest.raises` is used with `match=` on a fragment rather than a whole sentence
- [ ] The melt test asserts `len(wide) * len(MONTHS)`, the dtype, and the category order
- [ ] The pivot round-trip test compares **sorted** values, not frames
- [ ] **Break it (1):** removed `validate=` and watched **one** test go red
- [ ] **Break it (2):** removed `indicator=True` and the share check, and watched a **different** one
      go red
- [ ] **Break it (3):** dropped the `unaccounted` check in `to_long` and watched one test go red
- [ ] **Break it (4):** changed `MAX_UNMATCHED` from `0.01` to `0.9` and watched the suite stay
      **green**
- [ ] Can explain what (4) proves about the difference between a bug and a policy change
- [ ] `TODO(me)`: wrote the tests for the fixed `enrich`
- [ ] `TODO(me)`: added the round-trip property test with a comment on why it sorts
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-32-joining-and-reshaping/ src/setu/joining.py tests/test_joining.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 32` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 32` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-09` and `PD-10` and quotes my own unmatched-revenue share from
      `lab/lost_in_the_join.py`
