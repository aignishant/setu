# Day 32 — CHECKLIST

**IDs covered:** PD-09, PD-10 · **Principles served:** 1, 7, 9

## Demo command

```bash
uv run python days/day-32/lab/combining.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the ten-part report showing both the silent loss and the row explosion, then all tests green.

## Setup

- [ ] `./m start 32` and `./m scaffold 32` run
- [ ] `days/day-32/lab/combining.py` created
- [ ] No new packages installed

## PD-09 — combining

- [ ] Ran `the_silent_loss()` and saw 4 rows become 2 with **no warning**
- [ ] Identified both causes: a case mismatch and a genuine non-match
- [ ] Used `indicator=True` and read the `_merge` value counts
- [ ] Ran `the_row_explosion()` and saw the **output grow** and the sum become wrong
- [ ] Saw `validate="many_to_one"` raise, and can name all four validate options
- [ ] Compared all four join types on the same data
- [ ] Used `left_on` / `right_on` for differently-named keys
- [ ] Named your `suffixes` instead of accepting `_x` / `_y`
- [ ] Ran `dtype_mismatches_match_nothing()` and connected it back to Day 27
- [ ] Can state when to use `concat(axis=1)` versus `merge`
- [ ] Checked `isna().sum().sum()` after a `concat` with mismatched columns

## PD-10 — reshaping

- [ ] Melted wide to long and pivoted back; confirmed the **exact** round-trip
- [ ] Know why `back.columns.name = None` is needed for the comparison
- [ ] Saw `pivot` **raise** on duplicates and can say why that is a feature
- [ ] Used `pivot_table` with `aggfunc` deliberately, not to silence an error
- [ ] Know when `fill_value=0` is right and when it is wrong
- [ ] Used `crosstab` with and without `normalize`
- [ ] Used `stack` / `unstack` and saw the MultiIndex
- [ ] Can name four consumers that want long/tidy data

## Build brief

- [ ] `safe_merge` — **TODO(me)**: `validate` required, indicator internal, returns `(frame, report)`
- [ ] `safe_merge` raises on mismatched key dtypes and on a row explosion
- [ ] `assert_merge_kept_everything` — **TODO(me)**: default tolerance **zero**, count and percentage in the message
- [ ] `to_long` — **TODO(me)**: validates id_vars, keeps missing values
- [ ] `to_wide` — **TODO(me)**: reports how many duplicate pairs
- [ ] Can explain why `validate` has no default

## Tests that must be able to fail

- [ ] `test_merge_reports_the_row_accounting` — green ← **today's real assessment**
- [ ] `test_merge_keeps_every_left_row_by_default` — green
- [ ] **Changed the default to `how='inner'`, watched it go red, reverted** ← do not skip
- [ ] `test_merge_strips_the_indicator_column` — green
- [ ] `test_merge_raises_on_a_row_explosion` — green
- [ ] `test_merge_rejects_mismatched_key_dtypes` — green
- [ ] `test_merge_requires_validate` — green (a `TypeError` from the signature itself)
- [ ] **Gave `validate` a default, watched it go red, removed the default** ← do not skip
- [ ] `test_assert_kept_everything_passes_on_a_full_match` — green
- [ ] `test_assert_kept_everything_fails_by_default` — green
- [ ] `test_assert_kept_everything_allows_an_explicit_tolerance` — green
- [ ] `test_long_wide_round_trip` — green
- [ ] `test_long_keeps_missing_values` — green
- [ ] `test_long_rejects_a_missing_id_var` / `..._no_value_columns` — green
- [ ] `test_wide_reports_how_many_duplicates` — green

## Provenance (Principle 9)

- [ ] Every merge in your lab code printed its before/after row counts
- [ ] Can say, for the day's example, exactly how many rows were lost and why

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is pandas' default join type the dangerous one?
- [ ] Describe the row explosion and why it is worse than the silent loss
- [ ] What does `validate="many_to_one"` actually check?
- [ ] Why do mismatched key dtypes match nothing rather than raising?
- [ ] When is `concat(axis=1)` right and when do you need `merge`?
- [ ] Why does `pivot` refuse duplicates instead of aggregating them?
- [ ] When is `fill_value=0` wrong?
- [ ] Why does `safe_merge` return a report rather than just a frame?

## Commit

- [ ] `./m check && ./m done 32` succeeded
