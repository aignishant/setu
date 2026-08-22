# Day 112 — CHECKLIST

**IDs covered:** ML-23 · **Principles served:** 1, 7, 8, 15

## Demo command

```bash
uv run python days/day-112/lab/xgb.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the eight-part report ending with the forest comparison, then all ensemble tests green.

## Setup

- [ ] `./m start 112` and `./m scaffold 112` run
- [ ] `uv add "xgboost==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-112/lab/xgb.py` created
- [ ] Checked where `early_stopping_rounds` lives in **your** version

## ML-23 — three splits

- [ ] Built train / validation / test, not train / test
- [ ] Can say what each split is for, in one sentence each
- [ ] Can say what goes wrong with only two

## Early stopping

- [ ] Ran `early_stopping_finds_the_optimum()`
- [ ] Recorded `best_iteration` ______ of 3,000 requested
- [ ] Can say exactly what `early_stopping_rounds=50` means
- [ ] Can say what happens when it is too small, and too large

## The trap

- [ ] Ran `the_validation_set_is_now_used_up()`
- [ ] Recorded validation ______ vs test ______ — optimism ______
- [ ] Can say **why** the validation score is optimistic
- [ ] Can name the day that first identified this
- [ ] Can say what happens if you also tuned depth on that set

## Which knobs matter

- [ ] Ran `five_parameters_matter()` and read both blocks
- [ ] Listed the parameters whose delta exceeded the rest
- [ ] Can name the five (or so) that matter
- [ ] Can say why this matters for Day 106's search budget
- [ ] Ran `depth_and_min_child_weight_do_the_same_job()`
- [ ] Can say how `max_depth` differs from `min_child_weight` and `gamma`
- [ ] Can state the tuning advice given that they interact

## Stochastic sampling

- [ ] Ran `stochastic_sampling_is_bagging_inside_boosting()`
- [ ] Confirmed subsampling helped both score and speed
- [ ] Can give the usual range for both fractions
- [ ] Can name the earlier day this mechanism comes from
- [ ] Can say what it does to reproducibility

## Imbalance

- [ ] Ran `imbalanced_data_needs_a_decision_not_a_parameter()`
- [ ] Recorded PR-AUC with and without `scale_pos_weight`
- [ ] Recorded mean predicted probability both ways, and the true rate
- [ ] Can say what `scale_pos_weight` costs and what it buys
- [ ] Can state the better answer, and name the day it comes from

## Defaults and perspective

- [ ] Read `what_the_defaults_get_wrong()`; can name all three
- [ ] Ran `a_forest_is_still_competitive()`
- [ ] Recorded the difference and the forest's CV sd
- [ ] Can say what to check before claiming XGBoost won

## Build brief

- [ ] `three_way_split` — **TODO(me)**: `val_size` is a fraction of the whole, group-aware
- [ ] `fit_with_early_stopping` — **TODO(me)**: `stopped_early` false when capped
- [ ] Docstring states the validation score is optimistic
- [ ] `honest_early_stopping_score` — **TODO(me)**: reportable **is** the test score
- [ ] `parameter_importance_screen` — **TODO(me)**: admits it misses interactions
- [ ] `assert_imbalance_handled_by_threshold` — **TODO(me)**
- [ ] `boosting_config_report` — **TODO(me)**: clean config produces no warnings
- [ ] Can explain why a capped run is not an early-stopped run

## Tests that must be able to fail

- [ ] `test_the_three_splits_do_not_overlap` — green
- [ ] `test_val_size_is_a_fraction_of_the_whole` — green
- [ ] **Nested two `train_test_split` calls with the same fraction, watched it go red** ← do not skip
- [ ] `test_groups_never_straddle_any_split` — green
- [ ] `test_an_impossible_split_is_refused` — green
- [ ] `test_early_stopping_uses_far_fewer_rounds` — green
- [ ] `test_hitting_the_cap_is_not_early_stopping` — green
- [ ] **Reported a capped run as stopped, watched it go red** ← do not skip
- [ ] `test_a_very_early_stop_is_warned_about` — green
- [ ] `test_the_docstring_says_the_validation_score_is_optimistic` — green
- [ ] `test_early_stopping_rejects_a_bad_patience` — green
- [ ] `test_the_reportable_score_is_the_test_score` — green ← **today's real assessment**
- [ ] **Reported `best_score` as the result, watched the optimism go unnoticed** ← do not skip
- [ ] `test_the_statement_names_the_validation_set_as_the_selector` — green
- [ ] `test_reusing_the_validation_set_as_test_is_refused` — green
- [ ] `test_the_screen_separates_the_parameters_that_matter` — green
- [ ] `test_the_screen_admits_it_misses_interactions` — green
- [ ] `test_the_screen_needs_candidates` — green
- [ ] `test_class_weighting_with_probability_use_is_refused` — green
- [ ] `test_class_weighting_for_ranking_only_is_allowed` — green
- [ ] `test_no_weighting_always_passes` — green
- [ ] `test_a_high_learning_rate_without_early_stopping_is_warned_about` — green
- [ ] `test_a_deep_booster_is_warned_about` — green
- [ ] `test_too_few_rounds_for_a_small_learning_rate_is_warned_about` — green
- [ ] `test_aggressive_subsampling_is_warned_about` — green
- [ ] `test_a_sensible_configuration_is_not_warned_about` — green
- [ ] `test_the_report_names_which_parameters_are_worth_tuning` — green
- [ ] `test_the_report_says_the_rest_can_stay_at_defaults` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does XGBoost add to Day 110's gradient boosting?
- [ ] Why do you need three splits rather than two?
- [ ] Why is the validation score optimistic after early stopping?
- [ ] Name the five parameters that matter, and say why the rest do not
- [ ] How do `max_depth`, `min_child_weight` and `gamma` differ?
- [ ] What does subsampling do, and which earlier day is it borrowed from?
- [ ] Why avoid `scale_pos_weight` when you need probabilities?
- [ ] What must you check before claiming XGBoost beat a Random Forest?

## Commit

- [ ] `./m check && ./m done 112` succeeded
