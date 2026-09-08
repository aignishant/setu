# Day 30 — Definition of done

`PD-07` missing data — `NA`, `fillna`, `dropna`, `interpolate`, and why the median goes in the
pipeline rather than in the dataframe.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints a learned value, two filled halves, and
a filled single row:

```bash
uv run python -c "
import pandas as pd
from setu.missing import MedianImputer, drop_incomplete, profile

shop = pd.DataFrame(
    {
        'item': pd.Series(['milk', 'bread', 'eggs', 'rice'], dtype='str'),
        'need': [2, 1, 6, 1],
        'price': [1.15, 1.40, None, 2.05],
        'paid_by': pd.Series(['ana', None, 'ana', None], dtype='str'),
    }
).set_index('item')

print(profile(shop))
print()

train = pd.DataFrame({'price': [1.0, None, 2.0, 3.0]})
test = pd.DataFrame({'price': [10.0, 11.0, None, 12.0]})
imputer = MedianImputer(['price']).fit(train)
print('learned :', imputer.values_)
print('train   :', imputer.transform(train)['price'].tolist())
print('test    :', imputer.transform(test)['price'].tolist())
print('one row :', imputer.transform(pd.DataFrame({'price': [None]})).to_dict('records'))
"
```

The test half's blank must come out as the **training** median, and the single row must work. If
either fails, section 6 has not landed.

---

## Setup

- [ ] Ran `./m scaffold 30` and created `src/setu/missing.py` and `tests/test_missing.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `numpy.__version__` is `2.5.2`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and saw `NaN == NaN` print `False` and `pd.NA == pd.NA` print `<NA>`
- [ ] Saw the all-blank column sum to `0.0`, and can say why that is the most dangerous line on the
      page
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — what missing means

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say what `sum`, `mean`, `count` and `len` each do with the same blank — four answers
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] **1.4** read · ran its check-yourself · answered its question out loud
- [ ] **1.5** read · ran its check-yourself · answered its question out loud
- [ ] Can name which blank goes with which dtype without looking: `NaN`, `NaT`, `<NA>`

## Section 2 — finding it

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw `ValueError: The truth value of a Series is ambiguous` with my own eyes
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say why the blank *share* is the number to alert on rather than the count
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced the `-999` column: zero missing values, average of `-248.6`

## Section 3 — why it is missing

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] Can name the three reasons in ordinary words, and say which one no arithmetic can fix
- [ ] Ran the three-case simulation and saw case B's per-aisle means survive while case C's did not
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Watched the flag come out all-`False` when the two lines are in the wrong order

## Section 4 — dropping

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Measured it myself: twenty columns at five per cent blank, and about a third of the rows left
- [ ] Watched a bare `df.dropna()` on its own line change nothing
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw `TypeError: You cannot set both the how and thresh arguments at the same time.`
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] Can say, in one sentence each, what dropping a row costs and what dropping a column costs

## Section 5 — filling

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] Measured the spread and the correlation before and after a mean fill, on my own machine
- [ ] Watched `df.fillna(0)` write a zero into a text column
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw a group with no values come out of a group-wise fill still blank, with no error
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced the meter: `ffill` giving weekly usage of `0, 0, 90`
- [ ] Saw one entity's value fill another entity's blank when the frame was interleaved
- [ ] **5.4** read · ran its check-yourself · answered its question out loud
- [ ] Compared `interpolate()` against `interpolate(method="time")` on an uneven index
- [ ] Watched a trailing gap silently become a forward fill and report no blanks remaining

## Section 6 — the leak

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] **Ran the demonstration myself**: changed one held-back row and watched the whole-data fill
      value move while the train-only value did not
- [ ] Can state the rule in one sentence, in the right order
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Ran the single-row test and can say why it settles the design argument
- [ ] **6.3** read · ran its check-yourself · answered its question out loud
- [ ] Saw `RuntimeError: transform called before fit`, and can say what the loose-function version
      would have done instead

## Section 7 — the module

- [ ] **7.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say why `blank_rate_by` returns a table rather than a true-or-false verdict
- [ ] **7.2** read · ran its check-yourself · answered its question out loud

## Build

- [ ] `src/setu/missing.py` exists with `REQUIRED`, `MAX_DROP_SHARE` and `ImputationError`
- [ ] `SelectionError` is **imported** from Day 28's module, not redefined
- [ ] `profile` returns a frame and prints nothing
- [ ] `require_complete` raises with the column counts **and** the first offending row labels
- [ ] `blank_rate_by` returns evidence sorted by spread, and no verdict
- [ ] `drop_incomplete` refuses above `MAX_DROP_SHARE` and logs the two drop counts separately
- [ ] `MedianImputer` has `fit` and `transform`, writes the flag before the fill, and raises when
      unfitted
- [ ] `fill_by_group` has a minimum group size and a global fallback, and logs how many rows took
      each path
- [ ] `TODO(me)`: fixed `carry_forward` — `by`, `order` and `limit` all required, blanks in the
      ordering column refused
- [ ] `TODO(me)`: added `save`/`load` to `MedianImputer`, with a `schema_version` in the payload
- [ ] `TODO(me)`: answered in a comment what breaks if `add_indicator` is not written into the file
- [ ] `TODO(me)`: added `sentinel_report`, and said in its docstring whether it also range-checks
- [ ] `lab/why_it_is_missing.py` runs and prints the three cases with their per-group means
- [ ] `TODO(me)`: added a fourth case with a flat blank rate and a biased answer
- [ ] `TODO(me)`: compared global against group fill on case B and recorded both numbers

## Tests

- [ ] `tests/test_missing.py` uses a **fixture**, not a module-level frame
- [ ] The leak test is written, and asserts on a **copy** of `values_`
- [ ] The flag test asserts `blanks_before == 1` before asserting on the flag's sum
- [ ] `pytest.raises` is used with `match=`, and the dots in the pattern are escaped
- [ ] There is a test that transforms a **single row** and checks the columns match the training
      frame's
- [ ] **Break it (1):** swapped the two lines in `transform` and watched one test go red
- [ ] **Break it (2):** changed `fit` to see the whole dataset and watched **only** the leak test go
      red
- [ ] **Break it (3):** changed `max_loss` from `0.02` to `0.9` and watched the suite stay **green**
- [ ] Can explain what (3) proves about the difference between a bug and a policy change
- [ ] `TODO(me)`: wrote the tests for the fixed `carry_forward` and removed the `xfail` marker
- [ ] `TODO(me)`: added the `save`/`load` round-trip test
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-30-missing-data/ src/setu/missing.py tests/test_missing.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 30` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 30` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-07` and states, in one line, the rule about splitting before
      filling
