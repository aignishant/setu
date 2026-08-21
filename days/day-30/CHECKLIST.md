# Day 30 — CHECKLIST

**IDs covered:** PD-07 · **Principles served:** 1, 7, 8, 9

## Demo command

```bash
uv run python days/day-30/lab/missing.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the seven-part missing-data report, then all tests green.

## Setup

- [ ] `./m start 30` and `./m scaffold 30` run
- [ ] `days/day-30/lab/missing.py` created
- [ ] No new packages installed

## The rule (Principle 8)

- [ ] Redrew the §1 diagram from memory
- [ ] Can explain, to someone non-technical, why filling before splitting inflates a score
- [ ] Can state the project rule in one sentence
- [ ] Know which day actually does the imputation, and where it lives

## PD-07 — mechanics

- [ ] Saw all three markers (`None`, `np.nan`, `pd.NA`) in one frame
- [ ] Confirmed `isna()` catches all three
- [ ] Confirmed `""` is **not** missing
- [ ] Saw `pd.NA` propagate through a comparison instead of becoming `False`
- [ ] Saw masking with a nullable boolean **raise**, and fixed it with `.fillna(False)` on the mask
- [ ] Can explain why filling a mask is not the same as imputing data
- [ ] Counted missingness per column, as a percentage, per row, and in total
- [ ] Used `df.isna().corr()` and can say what correlated missingness implies
- [ ] Confirmed `.mean()` skips NaN by default
- [ ] Confirmed `.count()` and `len()` differ
- [ ] **Saw `groupby` drop null groups**, and fixed it with `dropna=False`
- [ ] Used `dropna` with `subset=`, `thresh=`, and `axis=1`
- [ ] Can say why `dropna()` is a modelling decision, not a cleanup

## Build brief

- [ ] `missingness_report` — **TODO(me)**: per column, sorted, JSON-serialisable, non-mutating
- [ ] `missingness_pattern` — **TODO(me)**: co-occurring patterns with counts
- [ ] `complete_case_cost` — **TODO(me)**: measures only, never drops
- [ ] `add_missing_indicators` — **TODO(me)**: the one allowed transform, and you can say why
- [ ] `assert_no_missing` — **TODO(me)**: names every offender with its count
- [ ] **No `fillna` / `interpolate` / `ffill` / `bfill` anywhere in `src/setu/`**

## Tests that must be able to fail

- [ ] `test_report_counts_every_marker_type` — green
- [ ] **Used `== np.nan` instead of `isna()`, watched it go red, fixed it** ← do not skip
- [ ] `test_report_includes_complete_columns` — green
- [ ] `test_report_is_sorted_by_missingness` — green
- [ ] `test_report_is_json_serialisable` — green
- [ ] `test_report_does_not_mutate` — green
- [ ] `test_pattern_finds_correlated_missingness` — green
- [ ] `test_pattern_includes_the_complete_case` — green
- [ ] `test_complete_case_cost_measures_without_dropping` — green (all four assertions)
- [ ] `test_complete_case_cost_with_a_subset` / `..._rejects_a_missing_column` — green
- [ ] `test_indicators_are_added_without_mutating` — green
- [ ] `test_indicators_do_not_fill_anything` — green
- [ ] `test_indicators_reject_a_name_collision` — green
- [ ] `test_assert_no_missing_passes_on_clean_columns` — green
- [ ] `test_assert_no_missing_names_every_offender_with_counts` — green
- [ ] `test_no_imputation_anywhere_in_src` — green ← **today's real assessment**
- [ ] **Added a `.fillna(0)` to a src module, watched the guard go red, removed it** ← do not skip

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does imputing before the split invalidate your test score?
- [ ] Name the three missing markers and where each appears
- [ ] What is three-valued logic, and why is `pd.NA > 1` more correct than `False`?
- [ ] Why does masking with a nullable boolean raise?
- [ ] What is `groupby`'s most expensive default, and how do you check for it?
- [ ] What does correlated missingness tell you?
- [ ] Why is a was-missing indicator safe outside a pipeline when a median is not?

## Commit

- [ ] `./m check && ./m done 30` succeeded
