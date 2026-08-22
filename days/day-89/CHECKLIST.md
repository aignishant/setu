# Day 89 — CHECKLIST

**IDs covered:** EDA-07 · **Principles served:** 1, 7, 8, 15

## Demo command

```bash
uv run python days/day-89/lab/prices.py
uv run python -m pytest tests/test_eda.py -v
```

Expected: the seven-part report ending with the honest conclusion, then all eda tests green.

## Setup

- [ ] `./m start 89` and `./m scaffold 89` run
- [ ] `uv add "statsmodels==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-89/lab/prices.py` created
- [ ] **`SOURCE.md` row added**, including whether prices are split/dividend adjusted

## The level trap

- [ ] Ran `the_level_trap()`; recorded model R²: ______
- [ ] Recorded the naive baseline R²: ______
- [ ] Recorded the MAE improvement over naive: ______%
- [ ] Read the coefficient and intercept; can say what the model learned
- [ ] Can state what the R² actually measured
- [ ] Ran `model_returns_instead()`; recorded R² ______ and directional accuracy ______
- [ ] Can say why differencing is the first step in any serious workflow

## The shuffle trap

- [ ] Ran `the_shuffle_trap()`; recorded random-split R² ______ vs chronological ______
- [ ] Can say why the random split scoring **better** is alarming
- [ ] Can explain the overlapping-window version in your own words
- [ ] Can name the two earlier days that were protecting against this

## Non-stationarity

- [ ] Ran `non_stationarity()` and read the by-period table
- [ ] Recorded the ADF p-value for price ______ and for return ______
- [ ] Can say what "fitted transforms expire" means concretely
- [ ] Can name the Day-80 objects affected
- [ ] Noted that returns are stationary in the mean but **not** the variance

## Autocorrelation

- [ ] Ran `autocorrelation()` and read all three columns
- [ ] Can say what each column tells you
- [ ] Can state the one real finding available here
- [ ] Can say why risk models exist where return models do not

## What no statistic can detect

- [ ] Read `survivorship_and_adjustment()`
- [ ] Can explain survivorship bias and why backtests on it look excellent
- [ ] Can explain what an unadjusted split looks like in the data
- [ ] Can say where both are answered, and name the Day-87 parallel

## Build brief

- [ ] `naive_baseline` — **TODO(me)**: three kinds, drops the undefined first prediction
- [ ] `beats_baseline` — **TODO(me)**: warns on high R² with low improvement, plain verdict
- [ ] `assert_no_shuffle_split` — **TODO(me)**: names the out-of-order position
- [ ] `stationarity_report` — **TODO(me)**: always tests the difference too, warns about expiry
- [ ] `volatility_structure` — **TODO(me)**: separates direction from magnitude, refuses prices
- [ ] `time_series_checklist` — **TODO(me)**: includes the two provenance questions
- [ ] Can explain why the R²-plus-low-improvement warning names the trap

## Tests that must be able to fail

- [ ] `test_the_naive_baseline_is_hard_to_beat` — green
- [ ] `test_naive_baseline_kinds_differ` — green
- [ ] `test_naive_baseline_rejects_bad_input` — green
- [ ] `test_a_high_r2_with_no_improvement_is_flagged` — green ← **today's real assessment**
- [ ] **Removed the baseline comparison and reported R² alone, watched it go red** ← do not skip
- [ ] `test_the_verdict_is_plain_when_the_model_adds_nothing` — green
- [ ] `test_a_genuinely_better_model_is_recognised` — green
- [ ] **Made the checker always report "no skill", watched it go red, fixed it** ← do not skip
- [ ] `test_beats_baseline_rejects_a_length_mismatch` — green
- [ ] `test_an_out_of_order_index_is_refused` — green
- [ ] `test_an_ordered_index_passes` — green
- [ ] `test_the_out_of_order_position_is_named` — green
- [ ] `test_prices_are_not_stationary` / `test_returns_are_stationary` — green
- [ ] `test_the_difference_is_always_tested_too` — green
- [ ] `test_non_stationarity_warns_that_fitted_transforms_expire` — green
- [ ] `test_stationarity_reports_every_period` — green
- [ ] `test_stationarity_rejects_a_short_series` — green
- [ ] `test_returns_are_directionally_unpredictable` — green
- [ ] `test_volatility_is_predictable_when_it_clusters` — green
- [ ] `test_the_interpretation_separates_direction_from_magnitude` — green
- [ ] `test_passing_prices_instead_of_returns_is_refused` — green
- [ ] `test_the_checklist_finds_duplicate_timestamps` / `..._finds_gaps` — green
- [ ] `test_the_checklist_asks_the_provenance_questions` — green
- [ ] `test_the_checklist_always_requires_a_naive_comparison` — green
- [ ] `test_the_checklist_rejects_a_non_datetime_column` — green

## The honest conclusion

- [ ] Ran `what_to_carry_forward()`
- [ ] Confirmed the conclusion is that direction is close to unpredictable
- [ ] Can say why that is a **successful** case study (Day 75)
- [ ] Can say what the failure would have been

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does predicting price levels give an R² near 1 with no skill?
- [ ] What does the naive baseline tell you that R² cannot?
- [ ] Why does a random split leak, and what does the rolling-window version add?
- [ ] What does non-stationarity do to a fitted scaler?
- [ ] What do the three autocorrelation columns each tell you?
- [ ] Why is volatility predictable when direction is not?
- [ ] Name two data problems no statistic can detect
- [ ] Why is "we found nothing predictive" a success here?

## Commit

- [ ] `./m check && ./m done 89` succeeded
