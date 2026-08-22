# Day 80 — CHECKLIST

**IDs covered:** FE-05 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-80/lab/scaling.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the eight-part report including the three-scaler outlier table, then all feature tests green.

## Setup

- [ ] `./m start 80` and `./m scaffold 80` run
- [ ] `days/day-80/lab/scaling.py` created
- [ ] No new packages installed

## FE-05 — which models care

- [ ] Ran `units_dominate_distance()` and read the printed distance components
- [ ] Can say what the Euclidean distance was actually measuring
- [ ] Ran `which_models_care()` and **read the difference column**
- [ ] Confirmed the forest was unchanged
- [ ] Can state the rule in one sentence
- [ ] Can say why trees are invariant to any monotone transform
- [ ] Ran `regularisation_needs_scaling()`; compared both coefficient vectors
- [ ] Can explain why a large-scale feature escapes the penalty

## The three scalers

- [ ] Ran `the_three_scalers()` and **read the outlier columns**
- [ ] Can rank the three by outlier fragility
- [ ] Can say why min-max is the worst
- [ ] Can name which two statistics each scaler uses

## What scaling does not do

- [ ] Ran `scaling_does_not_change_the_shape()`
- [ ] Confirmed skew and kurtosis were **identical** for all scalers
- [ ] Confirmed only `log1p` changed them
- [ ] Can say what scaling is for, and what a transform is for

## Deployment realities

- [ ] Ran `test_values_escape_the_range()`; recorded how many exceeded 1.0
- [ ] Can say why that is **correct** behaviour
- [ ] Can name all three responses, and what clipping hides
- [ ] Ran `the_leak_now_has_a_guard()`; can name the three earlier days
- [ ] Ran `sparse_data_needs_care()`; can say what centring does to sparsity
- [ ] Know which scaler is sparse-safe, and which later day produces sparse data

## Build brief

- [ ] `needs_scaling` — **TODO(me)**: reason names the mechanism, refuses unknown models
- [ ] `fit_scaler` — **TODO(me)**: robust default, refuses constants, warns on outlier-prone columns
- [ ] `apply_scaler` — **TODO(me)**: applies only, `clip=False`, records out-of-range counts
- [ ] `scaling_drift` — **TODO(me)**: turns a deployment failure into a monitoring signal
- [ ] `assert_shape_unchanged` — **TODO(me)**: catches a transform posing as a scaler
- [ ] Can explain why `robust` is the default and `clip` is off

## Tests that must be able to fail

- [ ] `test_distance_models_need_scaling` — green
- [ ] `test_trees_do_not_need_scaling` — green, reason names the mechanism
- [ ] `test_regularised_linear_models_need_scaling` — green
- [ ] `test_an_unknown_model_raises_rather_than_guessing` — green
- [ ] `test_robust_is_the_default` — green
- [ ] `test_standard_scaling_centres_and_normalises` — green
- [ ] `test_minmax_maps_train_to_zero_one` — green
- [ ] `test_minmax_is_the_most_outlier_fragile` — green ← **today's real assessment**
- [ ] **Made the default `standard`, watched the ordering assertion still hold but the warning tests go red** ← do not skip
- [ ] `test_robust_barely_moves_with_an_outlier` — green
- [ ] `test_scaling_never_changes_the_shape` — four green methods
- [ ] `test_a_log_transform_is_caught_as_shape_changing` — green
- [ ] `test_a_constant_column_is_refused` — green
- [ ] `test_outlier_prone_columns_warn_against_standard` — green
- [ ] `test_robust_on_the_same_column_does_not_warn` — green
- [ ] `test_train_params_are_applied_not_refitted` — green
- [ ] `test_apply_never_fits` — green
- [ ] **Recomputed the mean inside `apply_scaler`, watched it go red, removed it** ← do not skip
- [ ] `test_test_values_may_escape_the_minmax_range` — green
- [ ] `test_clipping_is_off_by_default` — green
- [ ] `test_clipping_still_reports_the_count` — green
- [ ] **Made clipping zero the out-of-range count, watched it go red, kept the evidence** ← do not skip
- [ ] `test_drift_is_detected` / `test_no_drift_on_similar_data` — green
- [ ] `test_sparse_safe_refuses_a_centring_method` — green
- [ ] `test_the_spec_is_json_serialisable` — green
- [ ] `test_apply_rejects_a_missing_column` / `test_apply_does_not_mutate` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the rule for which models need scaling
- [ ] Why are trees invariant, and to what class of transform?
- [ ] Why does unscaled ridge penalise features by their units?
- [ ] Rank the three scalers by outlier fragility and say why
- [ ] What does scaling never change?
- [ ] Why do test values escape the min-max range, and what are your three options?
- [ ] What does clipping hide?
- [ ] Why does centring break a sparse matrix?

## Commit

- [ ] `./m check && ./m done 80` succeeded
