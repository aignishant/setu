# Day 94 — CHECKLIST

**IDs covered:** ML-05 · **Principles served:** 1, 2, 7, 10

## Demo command

```bash
uv run python days/day-94/lab/metrics.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report ending with the metric-choice table, then all model tests green.

## Setup

- [ ] `./m start 94` and `./m scaffold 94` run
- [ ] `days/day-94/lab/metrics.py` created
- [ ] No new packages installed

## ML-05 — from scratch

- [ ] Computed all four metrics by hand before using sklearn
- [ ] Can say why MSE is unsuitable for a report
- [ ] Noted the `ddof=0` convention in R² and why implementations can differ

## MAE vs RMSE

- [ ] Ran `what_squaring_does()`; recorded both metrics for both error patterns
- [ ] Can state the question that decides between them
- [ ] Can give a situation favouring each
- [ ] Ran `outliers_choose_the_metric()`; recorded the inflation of each
- [ ] Confirmed **R² went up** with the outlier, and can explain why

## R² is a comparison

- [ ] Ran `r2_is_a_comparison()`
- [ ] Confirmed two models with the same RMSE had very different R²
- [ ] Can say what R² is a property of
- [ ] Can say why comparing it across datasets is meaningless
- [ ] Ran `r2_never_decreases()` and watched the column rise on **pure noise**
- [ ] Can explain why it cannot decrease
- [ ] Confirmed adjusted R² eventually falls

## Baselines

- [ ] Ran `the_baseline_makes_it_readable()` with identical absolute error
- [ ] Recorded the R² range across the three targets
- [ ] Can say what a negative R² means, and why it is useful rather than an error
- [ ] Can say which baseline a time series needs, and why

## MAPE

- [ ] Ran `mape_and_its_trap()`
- [ ] Can name both of its problems
- [ ] Can say when it is safe to use

## Choosing

- [ ] Read the eight-row table
- [ ] Can recall at least five rows
- [ ] Can state the assumption every row makes

## Build brief

- [ ] `regression_metrics` — **TODO(me)**: **always** returns a baseline, no opt-out
- [ ] Warns on high R² with low improvement, and on negative R²
- [ ] `adjusted_r_squared` — **TODO(me)**: not clipped, refuses a vanishing denominator
- [ ] `choose_metric` — **TODO(me)**: baseline always accompanies the recommendation
- [ ] `metric_sensitivity` — **TODO(me)**: signed change for R²
- [ ] `describe_metrics` — **TODO(me)**: units and improvement, no "variance explained"
- [ ] Can explain why there is no way to request a bare metric

## Tests that must be able to fail

- [ ] `test_the_metrics_match_sklearn` — green
- [ ] `test_rmse_is_the_root_of_mse` — green
- [ ] `test_a_baseline_is_always_present` — green ← **today's real assessment**
- [ ] **Added an option to skip the baseline, watched it go red, removed the option** ← do not skip
- [ ] `test_rmse_punishes_one_big_error_more_than_mae` — green (both directions)
- [ ] `test_rmse_is_more_sensitive_to_an_outlier_than_mae` — green
- [ ] `test_r2_can_improve_under_contamination` — green
- [ ] `test_identical_rmse_can_give_very_different_r2` — green
- [ ] `test_a_negative_r2_is_reported_not_clipped` — green
- [ ] **Clipped R² at zero, watched it go red, reverted** ← do not skip
- [ ] `test_a_high_r2_with_no_improvement_is_flagged` — green
- [ ] `test_the_previous_value_baseline_is_available` — green
- [ ] `test_a_length_mismatch_names_both` — green
- [ ] `test_adjusted_r2_requires_n_features` — green
- [ ] `test_r2_never_decreases_when_noise_is_added` — green
- [ ] `test_adjusted_r2_eventually_falls` — green
- [ ] `test_adjusted_r2_matches_the_formula` — green
- [ ] `test_adjusted_r2_is_not_clipped` — green
- [ ] `test_adjusted_r2_refuses_when_the_denominator_vanishes` — green
- [ ] `test_proportional_cost_gives_mae` / `test_disproportionate_cost_gives_rmse` — green
- [ ] `test_outliers_push_toward_mae` — green
- [ ] `test_a_baseline_always_accompanies_the_recommendation` — green
- [ ] `test_a_time_series_gets_the_naive_baseline` — green
- [ ] `test_adjusted_r2_is_additional_never_a_replacement` — green
- [ ] `test_an_unknown_error_cost_is_refused` — green
- [ ] `test_the_description_reports_units_and_improvement` — green
- [ ] `test_the_description_avoids_variance_explained` — green
- [ ] `test_the_description_never_quotes_r2_alone` — green
- [ ] `test_describe_rejects_a_result_without_a_baseline` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What question decides between MAE and RMSE?
- [ ] Why is R² a property of the model **and** the data?
- [ ] Why can R² never decrease when a feature is added?
- [ ] Why can R² rise when your data quality falls?
- [ ] What does a negative R² mean, and why keep it?
- [ ] When is adjusted R² the right comparison, and when is it not enough?
- [ ] Name both problems with MAPE
- [ ] Why does every metric need a baseline, and which one for a time series?

## Commit

- [ ] `./m check && ./m done 94` succeeded
