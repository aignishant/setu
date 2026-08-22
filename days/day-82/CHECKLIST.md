# Day 82 — CHECKLIST

**IDs covered:** FE-07 · **Principles served:** 1, 7, 8, 9

## Demo command

```bash
uv run python days/day-82/lab/construction.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the eight-part report ending with the prediction-time table, then all feature tests green.

## Setup

- [ ] `./m start 82` and `./m scaffold 82` run
- [ ] `days/day-82/lab/construction.py` created
- [ ] No new packages installed

## FE-07 — interactions and polynomials

- [ ] Ran the interaction demo; recorded R² without ______ and with ______
- [ ] Can say what the linear model could not **express** without the product column
- [ ] Can say why trees mostly do not need manual interactions
- [ ] Ran the polynomial demo; confirmed `x³` added nothing
- [ ] Can say why polynomials require scaling, with a number
- [ ] Ran `the_combinatorial_explosion()` and **read the degree-3 column**
- [ ] Can connect it to Day 74 in one sentence

## Binning

- [ ] Compared `cut` and `qcut` on data with two impossible values
- [ ] Can say why uniform bins collapsed and quantile bins did not
- [ ] Can state why bin edges are **fitted parameters**
- [ ] Can say what happens to a test value outside the fitted range, and that it is a decision

## Dates — the trap

- [ ] Built five legitimate date features and one leak
- [ ] Applied the prediction-time test to each, out loud
- [ ] Can state the test in one sentence
- [ ] Noticed the `NaT` pattern and can say why missingness tracked the target
- [ ] Ran `cyclical_features()`; confirmed the two distances become **equal**
- [ ] Can name three other variables that are cyclical

## Ratios and the checklist

- [ ] Built two ratio features
- [ ] Can name the two hazards, including the Day-39 one
- [ ] Read `the_prediction_time_test()` table
- [ ] Can explain the `to_date` vs `total` pair
- [ ] Can name the three words to interrogate in an unfamiliar dataset

## Build brief

- [ ] `prediction_time_check` — **TODO(me)**: over-flags on purpose, asks a question
- [ ] `add_interactions` — **TODO(me)**: explicit pairs only, **no all-pairs option**
- [ ] `add_polynomials` — **TODO(me)**: refuses an explosion, warns on large values
- [ ] `fit_binner` — **TODO(me)**: quantile default, JSON-serialisable edges
- [ ] `apply_binner` — **TODO(me)**: stable labels, counts out-of-range
- [ ] `add_date_features` — **TODO(me)**: **cannot take a second date column**
- [ ] `safe_ratio` — **TODO(me)**: guarded, NaN by default, refuses a sign flip
- [ ] Can explain why making a leak inexpressible beats warning about it

## Tests that must be able to fail

- [ ] `test_suspicious_column_names_are_flagged` — green
- [ ] `test_the_flag_is_a_question_not_a_verdict` — green
- [ ] `test_the_target_itself_is_flagged` — green
- [ ] `test_prediction_check_requires_the_target_to_be_present` — green
- [ ] `test_an_interaction_lets_a_linear_model_fit_what_it_could_not` — green
- [ ] `test_there_is_no_all_pairs_option` — green
- [ ] **Added an `all_pairs=True` convenience, watched it go red, removed it** ← do not skip
- [ ] `test_a_self_pair_is_refused` — green
- [ ] `test_interactions_reject_non_numeric_and_missing_columns` — green
- [ ] `test_interactions_do_not_mutate` — green
- [ ] `test_polynomials_refuse_an_explosion` — green
- [ ] `test_polynomials_warn_on_large_values` — green
- [ ] `test_polynomial_degree_is_bounded` — green
- [ ] `test_quantile_binning_is_the_default` — green
- [ ] `test_quantile_bins_are_robust_to_impossible_values` — green
- [ ] `test_bin_edges_come_from_train_only` — green
- [ ] **Re-binned the test set on its own range, watched it go red, fixed it** ← do not skip
- [ ] `test_out_of_range_values_are_counted` — green
- [ ] `test_bin_labels_are_stable_across_calls` — green
- [ ] `test_the_binner_spec_is_json_serialisable` — green
- [ ] `test_binner_rejects_too_few_distinct_values` — green
- [ ] `test_date_features_are_produced` — green
- [ ] `test_cyclical_hours_make_midnight_adjacent_to_eleven_pm` — green
- [ ] `test_days_since_requires_an_explicit_as_of` — green
- [ ] `test_date_features_cannot_reference_a_second_date` — green ← **today's real assessment**
- [ ] **Added an `end_column=` parameter, watched it go red, removed it** ← do not skip
- [ ] `test_date_features_reject_a_non_datetime_column` — green
- [ ] `test_safe_ratio_guards_zero_denominators` — green
- [ ] `test_safe_ratio_defaults_to_nan_not_a_number` — green
- [ ] `test_safe_ratio_rejects_a_sign_flipping_denominator` — green
- [ ] `test_constructed_features_pass_the_leak_tripwire` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the prediction-time test, and apply it to three column names
- [ ] Why can a linear model not represent an interaction without the product column?
- [ ] Why do polynomials require scaling?
- [ ] How is feature generation a multiple-comparisons problem?
- [ ] Why are quantile bins more robust than uniform ones?
- [ ] Why must bin edges be fitted on train only?
- [ ] Why does integer hour break a distance-based model?
- [ ] Why is `days_since` computed from `now()` a reproducibility bug?

## Commit

- [ ] `./m check && ./m done 82` succeeded
