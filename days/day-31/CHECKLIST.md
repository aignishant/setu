# Day 31 — CHECKLIST

**IDs covered:** PD-08 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-31/lab/grouping.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the seven-part groupby report ending with the two leakage one-liners, then all tests green.

## Setup

- [ ] `./m start 31` and `./m scaffold 31` run
- [ ] `days/day-31/lab/grouping.py` created
- [ ] No new packages installed

## PD-08 — the mechanics

- [ ] Wrote the **by-hand loop first** and confirmed it matches `groupby` (Principle 2)
- [ ] Redrew the split-apply-combine diagram from memory
- [ ] Can state the `agg` / `transform` / `filter` output shapes without hesitating
- [ ] Saw `count` and `size` give different answers on the same group
- [ ] Used **named aggregation** and can say why it beats a list of function names
- [ ] Grouped by two keys and saw the MultiIndex; flattened it with `as_index=False`
- [ ] Confirmed `transform` returns one row per **original** row with the index preserved
- [ ] Used `groupby().rank()` (Day 29's idiom, now fully explained)
- [ ] Used `.filter(lambda g: ...)` and know it returns original rows
- [ ] Ran `the_null_group_default()` and **saw the totals fail to reconcile**
- [ ] Used `sort=False` and can say when it helps
- [ ] Used `observed=True/False` on a categorical key and saw the group count change

## The leakage shape (Principle 8)

- [ ] Ran `the_leakage_shape()` and confirmed the two one-liners give **different** answers
- [ ] Can explain why the leaky version is a leak, in one sentence
- [ ] Know which day does the cross-fitted version properly

## Build brief

- [ ] `group_summary` — **TODO(me)**: named agg, `size` vs `count`, `dropna=False`, `ddof=1`, flat
- [ ] `assert_groups_reconcile` — **TODO(me)**: `np.isclose`, both numbers in the message
- [ ] `within_group_stat` — **TODO(me)**: transform, index asserted, docstring warns about leakage
- [ ] `group_stat_from_reference` — **TODO(me)**: leak-free, returns `(series, n_unseen)`
- [ ] `keep_large_groups` — **TODO(me)**: `transform('size')`, not `.filter(lambda)`
- [ ] Can explain why returning `n_unseen` forces the caller to acknowledge the gap

## Tests that must be able to fail

- [ ] `test_summary_distinguishes_size_from_count` — green
- [ ] `test_summary_keeps_the_null_group` — green
- [ ] **Removed `dropna=False`, watched it go red, restored it** ← do not skip
- [ ] `test_summary_is_a_flat_frame` — green
- [ ] `test_summary_uses_sample_std` — green (2.138, not 2.0)
- [ ] `test_summary_rejects_a_missing_column` — green
- [ ] `test_reconcile_passes_when_nothing_is_lost` — green
- [ ] `test_reconcile_catches_a_dropped_null_group` — green
- [ ] `test_within_group_stat_returns_one_value_per_row` — green
- [ ] **Used `agg` instead of `transform`, watched the row count go wrong, fixed it** ← do not skip
- [ ] `test_within_group_stat_values_are_right` — green
- [ ] `test_within_group_stat_rejects_an_unknown_stat` — green
- [ ] `test_reference_version_uses_only_the_reference_rows` — green ← **today's real assessment**
- [ ] **Computed the statistic over the full frame, watched it return 50 instead of 0, fixed it** ← do not skip
- [ ] `test_reference_version_reports_unseen_groups` — green
- [ ] **Fell back to a global mean for unseen groups, watched it go red, removed the fallback** ← do not skip
- [ ] `test_reference_version_preserves_the_index` — green
- [ ] `test_keep_large_groups` / `..._rejects_zero` — green
- [ ] `test_keep_large_groups_is_fast` — green
- [ ] **Rewrote it with `.filter(lambda)`, watched the timing test go red, reverted** ← do not skip

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Describe split-apply-combine and the three possible output shapes
- [ ] When do you need `transform` rather than `agg`?
- [ ] What is the difference between `count` and `size`, and when does it misreport your n?
- [ ] Which two `groupby` defaults have silently cost people data?
- [ ] How do you check, in one line, that no rows were lost in a groupby?
- [ ] Why is centring a value by its group mean a leak?
- [ ] Why does the leak-free helper return the unseen-group count?

## Commit

- [ ] `./m check && ./m done 31` succeeded
