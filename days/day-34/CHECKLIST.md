# Day 34 — CHECKLIST

**IDs covered:** PD-13, PD-14 · **Principles served:** 1, 7, 9

## Demo command

```bash
uv run python days/day-34/lab/categories.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the ten-part report including a memory table and the break-even rows, then all frame tests green.

## Setup

- [ ] `./m start 34` and `./m scaffold 34` run
- [ ] `days/day-34/lab/categories.py` created
- [ ] No new packages installed

## PD-13 — categoricals

- [ ] Ran `memory_saving()`; recorded the ratio: ______×
- [ ] Confirmed the codes dtype is `int8` for four categories
- [ ] Ran `the_break_even()` and **read all four rows**
- [ ] Can state when a category column is **larger** than a string column
- [ ] Built an **ordered** `CategoricalDtype` and sorted correctly
- [ ] Saw an unordered categorical **refuse** comparison
- [ ] Compared `observed=False` and `observed=True` in a `groupby`
- [ ] Know the pandas 3.0 default, and can say why you state it explicitly anyway
- [ ] Assigned an unknown category and **watched it become NaN silently**
- [ ] Ran `the_train_test_trap()` and can explain why independent code mappings break a model

## PD-14 — describe() as an audit

- [ ] Ran `describe_numeric()` and found all five planted defects **before** reading the hints
- [ ] Listed which describe row reveals each defect
- [ ] Ran `describe_non_numeric()`; can say what `unique == count` and a high `freq` mean
- [ ] Ran `what_describe_misses()` — duplicates, dtypes, memory, skew
- [ ] Know that `.plot.hist()` is for looking, not for reporting

## Build brief

- [ ] `to_categorical` — **TODO(me)**: raises on unknown values, refuses memory-increasing conversions
- [ ] `category_spec` — **TODO(me)**: deterministic, JSON-serialisable, fit on train
- [ ] `quality_report` — **TODO(me)**: full dict + warnings, **reuses `setu.stats.summary`**
- [ ] `assert_quality` — **TODO(me)**: lists every blocking problem
- [ ] Did **not** reimplement the numeric summary
- [ ] Can explain how `to_categorical` turns a silent trap into a loud one

## Tests that must be able to fail

- [ ] `test_to_categorical_converts_and_saves_memory` — green
- [ ] `test_to_categorical_does_not_mutate` — green
- [ ] `test_to_categorical_refuses_a_near_unique_column` — green
- [ ] `test_unknown_category_raises_instead_of_becoming_nan` — green ← **today's real assessment**
- [ ] **Used a plain `astype(CategoricalDtype(...))`, watched `"zzz"` become NaN, added the check** ← do not skip
- [ ] `test_train_spec_applied_to_test_gives_the_same_codes` — green
- [ ] **Converted train and test independently, watched the codes disagree, fixed it** ← do not skip
- [ ] `test_ordered_categorical_sorts_by_declared_order` — green
- [ ] `test_category_spec_is_deterministic_and_serialisable` — green
- [ ] `test_quality_report_finds_missing_values` — green
- [ ] `test_quality_report_flags_a_constant_column` — green
- [ ] `test_quality_report_flags_an_identifier` — green
- [ ] `test_quality_report_counts_duplicate_rows` — green
- [ ] `test_quality_report_finds_negative_sentinels` — green
- [ ] `test_quality_report_is_json_serialisable` — green
- [ ] `test_quality_report_does_not_mutate` — green
- [ ] `test_quality_report_uses_the_shared_summary` — green ← an **architecture** test
- [ ] **Reimplemented the numeric summary inline, watched it go red, switched back to `stats.summary`** ← do not skip
- [ ] `test_assert_quality_lists_every_problem` — green
- [ ] `test_assert_quality_passes_a_clean_frame` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] When does a category column save memory, and when does it cost memory?
- [ ] What happens when you assign a value outside the category set?
- [ ] Why do independently-created categoricals break a train/test workflow?
- [ ] What does `observed=` control, and why state it rather than rely on the default?
- [ ] Name four defects `describe()` reveals, and which row reveals each
- [ ] What can `describe()` *not* see, and why does one of those leak across a split?
- [ ] Why is `unique == count` a reason to exclude a column from a model?
- [ ] Why does `quality_report` call `stats.summary` instead of computing the numbers itself?

## Commit

- [ ] `./m check && ./m done 34` succeeded
