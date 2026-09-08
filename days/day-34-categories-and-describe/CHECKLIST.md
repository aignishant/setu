# Day 34 — Definition of done

`PD-13` categorical dtype · `PD-14` descriptive statistics and built-in plotting.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints a measured saving, a refusal, an
ordered sort and a report that includes the text columns:

```bash
uv run python -c "
import numpy as np
import pandas as pd
from setu.audit import SIZE_DTYPE, AuditError, audit, categorise

rng = np.random.default_rng(34)
ITEMS = ['milk', 'bread', 'eggs', 'rice']
AISLES = {'milk': 'dairy', 'bread': 'bakery', 'eggs': 'dairy', 'rice': 'dry goods'}
item = rng.choice(ITEMS, 240_000)
shop = pd.DataFrame({
    'item': pd.Series(item, dtype='str'),
    'aisle': pd.Series([AISLES[i] for i in item], dtype='str'),
    'size': pd.Series(rng.choice(['small', 'medium', 'large'], 240_000), dtype='str'),
    'price': np.round(rng.normal(2.0, 0.5, 240_000), 2),
    'need': rng.integers(1, 4, 240_000),
})
shop.loc[shop.index[:300], 'price'] = np.nan

before = int(shop.memory_usage(deep=True).sum())
typed = categorise(shop, ['item', 'aisle', 'size'], {'size': SIZE_DTYPE})
after = int(typed.memory_usage(deep=True).sum())
print('bytes  :', before, '->', after, '  ratio', round(before / after, 1), 'x')
print('sorted :', list(typed['size'].sort_values().unique()))

nearly = pd.DataFrame({'reference': pd.Series([f'r{i}' for i in range(50_000)], dtype='str')})
try:
    categorise(nearly, ['reference'], {})
except AuditError as e:
    print('refused:', str(e).splitlines()[0])

findings = audit(typed)
print('columns in the report:', sorted(findings['column'].unique()))
print('failed checks        :', int((~findings['passed']).sum()))
"
```

The byte count must go **down**, the sizes must come out `small, medium, large` rather than
alphabetically, the nearly-unique column must be **refused**, and every column of the frame must
appear in the report — including the text ones. If any of those fails, sections 2, 3 or 5 have not
landed.

---

## Setup

- [ ] Ran `./m scaffold 34` and created `src/setu/audit.py` and `tests/test_audit.py`
- [ ] `uv add matplotlib==3.11.1` and the pin is in `pyproject.toml` and `uv.lock`
- [ ] Confirmed `pandas.__version__` is `3.0.5`, `numpy.__version__` is `2.5.2`,
      `matplotlib.__version__` is `3.11.1`
- [ ] If any has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and recorded **my own** text-to-category ratio
- [ ] Saw a `describe()` whose `min` on a quantity column was `-1`
- [ ] Can say why the ratio on my machine is not the ratio on this page

## Section 1 — the repeated word

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say what `deep=True` adds, and for which dtypes it adds nothing

## Section 2 — the `category` dtype

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Can draw the two arrays on paper for the flat's four-row envelope
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Checked the arithmetic: codes' bytes plus categories' bytes matches `memory_usage(deep=True)`
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Found, on my own machine, the ratio of distinct values to rows at which the conversion stops
      paying
- [ ] **2.4** read · ran its check-yourself · answered its question out loud
- [ ] Can name three operations that still work on a category and one that raises

## Section 3 — order

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw `sort_values()` put `large` before `medium`
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Watched a value outside `categories` become blank, with **no** error
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Saw the real error from comparing an **unordered** category with `<`

## Section 4 — the traps

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw the real error from assigning a label that is not in the list
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say when an empty category is a bug and when it is the finding
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] Measured the memory before and after one of the reverting operations
- [ ] **4.4** read · ran its check-yourself · answered its question out loud
- [ ] Watched a `concat` of two categorical columns come back as `object`

## Section 5 — `describe`

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] Confirmed for myself what `std` divides by, rather than taking it on trust
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Made a tie in `top` and saw what it does about it
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] Ran `describe()` on a mixed frame and counted the columns it silently dropped

## Section 6 — the quality report

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Wrote the assertion that turns the `max` finding into a test
- [ ] **6.3** read · ran its check-yourself · answered its question out loud
- [ ] Saw the mean move while the median did not, on my own corrupted frame
- [ ] **6.4** read · ran its check-yourself · answered its question out loud
- [ ] Can say why a constant column is worse than a missing one
- [ ] **6.5** read · ran its check-yourself · answered its question out loud
- [ ] Wrote a chart to `lab/` through the `Agg` backend, with no window opening

## Section 7 — the module

- [ ] **7.1** read · ran its check-yourself · answered its question out loud
- [ ] **7.2** read · ran its check-yourself · answered its question out loud

## Build brief

- [ ] `src/setu/audit.py` exists with `ITEMS`, `AISLES`, `SIZES`, `SIZE_DTYPE`,
      `MAX_MISSING_SHARE` and `MAX_CATEGORY_RATIO` at module level
- [ ] `AuditError` subclasses `ValueError`; no fifth exception family was invented
- [ ] `categorise` returns a new frame, asserts the resulting dtype, and refuses a bad ratio
- [ ] `audit` returns a **frame of findings** with `column`, `check`, `value`, `passed` — it does not
      print
- [ ] `TODO(me)`: fixed `audit` so no column can be missing from its own report, and said so in the
      docstring
- [ ] `TODO(me)`: added `memory_report` with the comment on why the ratio beats the total
- [ ] `TODO(me)`: added `constant_columns` with the comment on `std == 0` against `nunique == 1`
- [ ] `lab/the_column_that_did_nothing.py` runs and prints `describe(include="all")` beside the
      findings
- [ ] `TODO(me)`: added the per-column memory before and after, and named the column carrying the
      saving
- [ ] `TODO(me)`: ran the corruption before and after categorising and recorded both orders

## Tests

- [ ] `tests/test_audit.py` has four **fixtures**: clean, corrupted, unused-category, mismatched
      categories
- [ ] There is a test asserting each fixture has the property it exists for
- [ ] The text-only test asserts the fixture **has** no numeric column before calling `audit`
- [ ] There is a test that a nearly-unique column is refused for conversion
- [ ] `pytest.raises` is used with `match=` on a fragment rather than a whole sentence
- [ ] The memory test asserts a **ratio**, not an absolute byte count
- [ ] **Break it (1):** dropped the dtype assertion in `categorise` and watched **one** test go red
- [ ] **Break it (2):** used `astype("category")` instead of `SIZE_DTYPE` and watched a **different**
      one go red
- [ ] **Break it (3):** removed the ratio guard and watched the refusal test go red
- [ ] **Break it (4):** changed `MAX_MISSING_SHARE` from `0.01` to `0.9` and watched the suite stay
      **green**
- [ ] Can explain what (4) proves about the difference between a bug and a policy change
- [ ] `TODO(me)`: wrote the tests for the fixed `audit`
- [ ] `TODO(me)`: added the categorise-twice property test with its comment
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-34-categories-and-describe/ src/setu/audit.py tests/test_audit.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 34` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero model calls, zero API keys, zero network at run time.** One pinned install:
      `matplotlib==3.11.1`. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 34` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-13` and `PD-14` and quotes **my own** memory ratio from `2.2` and
      the distinct-value ratio at which the saving stopped from `2.3`
