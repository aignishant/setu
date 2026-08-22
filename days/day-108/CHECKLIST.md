# Day 108 — CHECKLIST

**IDs covered:** ML-19 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-108/lab/forest.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the eight-part report ending with where forests still lose, then all ensemble tests green.

## Setup

- [ ] `./m start 108` and `./m scaffold 108` run
- [ ] `days/day-108/lab/forest.py` created
- [ ] No new packages installed

## ML-19 — bagging

- [ ] Wrote bagging from scratch in three lines
- [ ] Reused Day 68's bootstrap
- [ ] Confirmed the **average tree** was no better than a single one
- [ ] Can say where the gain actually came from
- [ ] Ran `the_bootstrap_leaves_rows_out()`; recorded the fraction: ______
- [ ] Can say what that fraction converges to, and why it matters tomorrow

## Why bagging alone is not enough

- [ ] Ran `bagged_trees_stay_correlated()` and **read the first two columns together**
- [ ] Recorded ρ for bagging ______ and for `sqrt` ______
- [ ] Confirmed individual trees got worse while the ensemble got better
- [ ] Confirmed `max_features=1` eventually hurt the ensemble too
- [ ] Ran `why_bagging_alone_correlates()`
- [ ] Recorded how often the dominant feature was the first split, both ways
- [ ] Can state the mechanism in one sentence

## Tuning

- [ ] Ran `tuning_max_features()` across five settings
- [ ] Can give the classification and regression defaults
- [ ] Can say when the usual advice **reverses**, and why
- [ ] Ran `more_trees_never_hurt()` from 1 to 1,000
- [ ] Confirmed test accuracy flattened rather than falling
- [ ] Can say what `n_estimators` should be set by
- [ ] Can name the parameters that actually control capacity
- [ ] Ran `depth_should_stay_unlimited()`
- [ ] Can say why pruning inside a forest is doing the averaging's job badly

## What survives the ensemble

- [ ] Ran `where_forests_still_lose()`
- [ ] Recorded logistic ______ vs forest ______ on a diagonal boundary
- [ ] Recorded the forest's extrapolated predictions at x = 6 and 10
- [ ] Can say what a forest can only ever return
- [ ] Can name the day whose limitations these are

## Build brief

- [ ] `bootstrap_indices` — **TODO(me)**: in-bag and out-of-bag, ~1/e
- [ ] `fit_bagged` — **TODO(me)**: fresh model each time, tracks `in_bag_counts`
- [ ] Refuses when any row is in-bag for every model
- [ ] `decorrelation_curve` — **TODO(me)**: confirms `trade_is_visible`
- [ ] `forest_defaults` — **TODO(me)**: a **reason** per parameter, noise reversal
- [ ] `assert_n_estimators_not_tuned` — **TODO(me)**
- [ ] `forest_limitations` — **TODO(me)**: diagonal penalty and extrapolation
- [ ] Can explain why a row with no OOB estimate is an error rather than a skip

## Tests that must be able to fail

- [ ] `test_the_bootstrap_leaves_out_about_a_third` — green
- [ ] `test_in_bag_and_out_of_bag_partition_the_rows` — green
- [ ] `test_the_bootstrap_draws_with_replacement` — green
- [ ] **Sampled without replacement, watched the unique-count assertion go red** ← do not skip
- [ ] `test_bootstrap_is_reproducible` / `..._rejects_a_tiny_n` — green
- [ ] `test_bagging_beats_a_single_model` — green
- [ ] `test_a_fresh_model_is_built_per_estimator` — green
- [ ] `test_in_bag_counts_are_tracked` — green
- [ ] `test_too_few_estimators_leaves_rows_with_no_oob_estimate` — green
- [ ] `test_bagging_rejects_a_single_estimator` — green
- [ ] `test_hiding_features_lowers_the_correlation` — green
- [ ] `test_weaker_trees_make_a_better_ensemble` — green ← **today's real assessment**
- [ ] **Judged max_features by single-tree accuracy, watched it pick the wrong setting** ← do not skip
- [ ] `test_the_trade_is_described_in_words` — green
- [ ] `test_the_curve_needs_something_to_compare` — green
- [ ] `test_classification_defaults_to_sqrt` — green
- [ ] `test_regression_uses_more_features_per_split` — green
- [ ] `test_depth_is_unlimited_by_default` — green
- [ ] `test_every_default_carries_a_reason` — green
- [ ] `test_many_noise_features_reverse_the_usual_advice` — green
- [ ] `test_forest_defaults_rejects_an_unknown_task` — green
- [ ] `test_selecting_a_flattened_n_estimators_is_refused` — green
- [ ] `test_choosing_the_largest_n_estimators_is_fine` — green
- [ ] `test_a_forest_never_extrapolates` — green
- [ ] `test_a_diagonal_boundary_is_detected` — green
- [ ] `test_an_axis_aligned_boundary_is_not_penalised` — green
- [ ] `test_the_notes_credit_the_underlying_tree_limit` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Describe bagging in one sentence, and say what makes the trees differ
- [ ] Why do bagged trees stay correlated when one feature dominates?
- [ ] What does Random Forest do about it, and what does it cost?
- [ ] Why does lowering `max_features` improve the forest while hurting each tree?
- [ ] When does the `sqrt` advice reverse?
- [ ] Why can `n_estimators` not overfit, and what should you tune instead?
- [ ] Why should forest trees stay unpruned?
- [ ] Name two tree limitations that averaging does **not** fix

## Commit

- [ ] `./m check && ./m done 108` succeeded
