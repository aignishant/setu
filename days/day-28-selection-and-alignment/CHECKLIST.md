# Day 28 — Definition of done

`PD-03` indexing and selection · `PD-04` reindexing and alignment.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints three rows and no blanks:

```bash
uv run python -c "
import pandas as pd
from setu import select as sel
mine = pd.Series([2, 1, 6, 1], index=['milk', 'bread', 'eggs', 'rice'], name='need')
theirs = pd.Series([1, 2, 3], index=['milk', 'eggs', 'tea'], name='need')
print('straight add :', (mine + theirs).to_dict())
print('combined     :', sel.combine(mine, theirs).to_dict())
print('dtypes       :', sel.combine(mine, theirs).dtypes.to_dict())
"
```

---

## Setup

- [ ] Ran `./m scaffold 28` and created `src/setu/select.py` and `tests/test_select.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5`; if it has moved, logged it in `docs/CHANGELOG_PLAN_DS.md`
- [ ] Built the frame with `.set_index('item')` and understood why that line makes the day visible
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — label and position

- [ ] **1.1** read · ran its check-yourself · answered its out-loud question
- [ ] Added a row to the top of the frame and watched `loc` hold still while `iloc` moved
- [ ] **1.2** read · ran its check-yourself · answered its out-loud question
- [ ] Saw `loc['eggs']` come back as `dtype: object` and can explain why that is correct
- [ ] Compared `loc['eggs']` against `loc[['eggs']]` and can state the shape rule without brackets
- [ ] **1.3** read · ran its check-yourself · answered its out-loud question
- [ ] **1.4** read · ran its check-yourself · answered its out-loud question
- [ ] Timed `loc[r, c]` against `at[r, c]` on my own machine and got a ratio near 1, not near 100
- [ ] **1.5** read · ran its check-yourself · answered its out-loud question
- [ ] Ran a backwards `loc` slice and got an empty frame with no error
- [ ] Ran `loc['bread':'tea']` on an unsorted index (raises) and on a sorted one (does not)

## Section 2 — masks

- [ ] **2.1** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed a mask is a Series with the frame's labels, not a `True`/`False`
- [ ] Showed that `(x > 1).sum()` and `(x <= 1).sum()` do not add up when a value is missing
- [ ] **2.2** read · ran its check-yourself · answered its out-loud question
- [ ] Filtered with a shuffled mask and got the right rows — then with a reversed **list** and did not
- [ ] Wrote to a filtered frame and confirmed the original was untouched, with no warning
- [ ] **2.3** read · ran its check-yourself · answered its out-loud question
- [ ] Met `The truth value of a Series is ambiguous` from **both** causes and can tell them apart
- [ ] Ran `shop['need'] & 1` and understood why the bracket rule is "always"
- [ ] **2.4** read · ran its check-yourself · answered its out-loud question
- [ ] Ran `isin` with numbers against a text column and got zero rows, silently
- [ ] **2.5** read · ran its check-yourself · answered its out-loud question
- [ ] Saw `sum()` give `0.0` and `mean()` give `nan` on the same empty column
- [ ] Ran the set-difference check that names a value `isin` could not find

## Section 3 — writing

- [ ] **3.1** read · ran its check-yourself · answered its out-loud question
- [ ] Reproduced `ChainedAssignmentError` and noticed it is a **warning**, not an exception
- [ ] Reproduced the filter-then-write case and confirmed it warns about nothing at all
- [ ] **3.2** read · ran its check-yourself · answered its out-loud question
- [ ] Compared `assign(x=lambda f: ...)` against `assign(x=outer_variable)` after a filter
- [ ] Added a column from a differently-indexed Series and watched three holes appear
- [ ] **3.3** read · ran its check-yourself · answered its out-loud question
- [ ] Called `.where(...)` with no assignment and confirmed nothing changed
- [ ] Saw `where` promote `int64` to `float64`, and `other=` prevent it

## Section 4 — alignment

- [ ] **4.1** read · ran its check-yourself · answered its out-loud question
- [ ] Ran the plan's named example: four rows plus three rows giving five, three of them blank
- [ ] Used `add(..., fill_value=0)` and can say what claim about the data that makes
- [ ] **4.2** read · ran its check-yourself · answered its out-loud question
- [ ] Added two same-length, reordered Series both ways and got two different sets of numbers
- [ ] Added two frames and got a 3×3 result with one real value in it
- [ ] Met `Can only compare identically-labeled Series objects` and used `.gt()` instead
- [ ] **4.3** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed `int8 + int8` becomes `float64`, and `Int64 + Int64` does not
- [ ] Watched `2**53 + 1` lose its last digit to the promotion
- [ ] **4.4** read · ran its check-yourself · answered its out-loud question
- [ ] Joined two lists differing only in case and whitespace, and got twice the rows and no values
- [ ] **4.5** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed `to_numpy()` returns a **read-only** view, and `.values` returns different types

## Section 5 — reindexing

- [ ] **5.1** read · ran its check-yourself · answered its out-loud question
- [ ] Watched `reindex` drop two rows and the total fall, with no error
- [ ] Confused `reindex` with `rename` on purpose, to see what each does
- [ ] **5.2** read · ran its check-yourself · answered its out-loud question
- [ ] Compared `fill_value=0`, `ffill` and `bfill` on the same date gap and got three totals
- [ ] Ran `ffill` on an alphabetical index and saw why "ordered" is not the same as "meaningful"
- [ ] **5.3** read · ran its check-yourself · answered its out-loud question
- [ ] Reproduced the cartesian explosion: two duplicates each giving four rows
- [ ] Confirmed `to_dict()` silently hides a duplicated label
- [ ] **5.4** read · ran its check-yourself · answered its out-loud question
- [ ] Ran all four `join=` values and can say which grows, which shrinks and which preserves order
- [ ] Confirmed `align` does **not** refuse duplicates — it multiplies

## Section 6 — the module

- [ ] **6.1** read · ran its check-yourself · answered its out-loud question
- [ ] **6.2** read · ran its check-yourself · answered its out-loud question

## The build

- [ ] `src/setu/select.py` imports Day 26's `SchemaError` rather than defining a third exception
- [ ] `SHELF` is a tuple and is the single source of truth for the reference index
- [ ] `assert_unique_index` names the duplicated labels and the number of extra rows they would cause
- [ ] `rows_for` collects **every** unknown label before raising
- [ ] `dear_items` has no emptiness check, and its docstring says an empty result is valid
- [ ] `flag` uses `assign` with lambdas and cannot mutate its argument
- [ ] `restock` uses a single `.loc` assignment and **confirms the write landed**
- [ ] `onto_shelf` refuses an item the shelf does not know, rather than dropping it
- [ ] `combine` states its `join=`, checks both indexes, and converts back to `int64`
- [ ] There is not one `frame[mask]["col"] = ...` anywhere in the file
- [ ] `TODO(me)`: wrote `cheapest(frame, n)` and documented what it does when `n` is too large
- [ ] `TODO(me)`: decided whether `dear_items` should log an empty result, and wrote the reason down
- [ ] `TODO(me)`: decided about a single entry point for the uniqueness check, with a reason
- [ ] `lab/two_lists.py` prints the plan's example five ways with lengths and dtypes
- [ ] `TODO(me)`: added the reversed-index line and wrote which answer is correct and how I would know

## The tests

- [ ] `tests/test_select.py` asserts what each function returns
- [ ] It asserts what each function **does not do** — the caller's frame is unchanged
- [ ] It asserts what each function refuses, with `match=` on every `pytest.raises`
- [ ] One test asserts an empty result is allowed, and that it keeps its columns and dtypes
- [ ] One test asserts `combine` returns `int64`, and I can say what that proves about blanks
- [ ] `uv run pytest tests/test_select.py -q` is green
- [ ] **Break it:** changed `out.loc[below, 'need']` to `out[below]['need']`, ran the suite, watched it go red
- [ ] Read **both** the `SelectionError` and the `ChainedAssignmentError`, and can say which stopped it
- [ ] Put the `.loc` back and confirmed the suite is green again
- [ ] `TODO(me)`: wrote the tests for `cheapest`, including a no-mutation one
- [ ] `TODO(me)`: added the empty-input sweep across every public function
- [ ] `TODO(me)`: broke the module a **second** way and recorded it in a `# Seen to fail:` block

## The gate

- [ ] `uv run ruff format days/day-28-selection-and-alignment/ src/setu/select.py tests/test_select.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 28` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 28` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-03` and `PD-04` and says which silent failure surprised me most
