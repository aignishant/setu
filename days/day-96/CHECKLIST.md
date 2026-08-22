# Day 96 — CHECKLIST

**IDs covered:** ML-07 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-96/lab/tradeoff.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the seven-part report including the decomposition and learning-curve tables, then all model
tests green.

## Setup

- [ ] `./m start 96` and `./m scaffold 96` run
- [ ] `days/day-96/lab/tradeoff.py` created
- [ ] No new packages installed

## ML-07 — seeing it

- [ ] Ran `see_it_first()` at three degrees
- [ ] Confirmed degree 15 had the **lowest train** and **worst test** error
- [ ] Can say what training error actually measures

## The decomposition

- [ ] Ran `decompose_the_error()` and **read the two middle columns**
- [ ] Confirmed bias falls and variance rises as degree grows
- [ ] Confirmed the three components sum to the measured MSE
- [ ] Can define bias² in terms of the **average** model
- [ ] Can define variance in terms of models disagreeing with **each other**
- [ ] Can write the identity from memory

## The noise floor

- [ ] Ran `the_noise_floor()`; recorded the MSE of a model that knows the truth: ______
- [ ] Can say what a test error near the floor means for your next move
- [ ] Can name a practical way to estimate the floor on a labelling task

## Learning curves

- [ ] Ran `learning_curves()` and **read the shapes, not the numbers**
- [ ] Described the degree-1 shape and its implication
- [ ] Described the degree-15 shape and its implication
- [ ] Filled in the five-row diagnostic table from memory
- [ ] Can say what a **rising** validation curve means

## Capacity

- [ ] Ran `capacity_is_not_only_degree()` with fixed degree and varying alpha
- [ ] Watched the coefficient norm explode without regularisation
- [ ] Can name four things that control capacity, from four different days

## The validation set gets used up

- [ ] Ran `the_validation_set_gets_used_up()`
- [ ] Recorded the selected validation MSE ______ and the true held-out MSE ______
- [ ] Can name the Day-70 concept this is
- [ ] Can say what you need instead

## Build brief

- [ ] `bias_variance_decomposition` — **TODO(me)**: reports `dominant`, refuses too few datasets
- [ ] `learning_curve` — **TODO(me)**: repeats each size, reports sd
- [ ] `diagnose_learning_curve` — **TODO(me)**: `more_data_will_help`, `'suspicious'` for a bug
- [ ] `estimate_noise_floor` — **TODO(me)**: within-group variance, refuses single measurements
- [ ] `assert_not_reporting_validation_as_test` — **TODO(me)**
- [ ] Can explain why `more_data_will_help` is the most valuable field

## Tests that must be able to fail

- [ ] `test_a_simple_model_is_bias_dominated` — green
- [ ] `test_a_complex_model_is_variance_dominated` — green
- [ ] `test_bias_and_variance_move_in_opposite_directions` — green
- [ ] `test_the_decomposition_sums_to_the_total` — green
- [ ] `test_too_few_datasets_is_refused` — green
- [ ] `test_the_gap_closes_as_n_grows_for_a_complex_model` — green
- [ ] `test_the_gap_stays_small_for_a_simple_model` — green
- [ ] `test_the_curve_reports_variability` — green
- [ ] `test_sizes_must_increase` — green
- [ ] `test_underfitting_is_diagnosed_and_more_data_is_refused` — green ← **today's real assessment**
- [ ] **Made `more_data_will_help` always True, watched it go red, fixed it** ← do not skip
- [ ] `test_overfitting_with_a_falling_curve_says_more_data_helps` — green
- [ ] `test_overfitting_with_a_flat_curve_says_reduce_capacity` — green
- [ ] **Ignored whether the curve was still falling, watched one of the pair go red** ← do not skip
- [ ] `test_reaching_the_noise_floor_is_recognised` — green
- [ ] `test_a_rising_validation_curve_is_called_a_bug_not_a_diagnosis` — green
- [ ] `test_every_diagnosis_is_actionable` — green
- [ ] `test_the_noise_floor_is_the_within_group_variance` — green
- [ ] `test_the_noise_floor_needs_repeated_measurements` — green
- [ ] `test_the_noise_floor_needs_enough_groups` — green
- [ ] `test_reporting_a_selection_score_as_a_test_score_is_refused` — green
- [ ] `test_a_genuine_held_out_score_passes` — green
- [ ] `test_the_selected_score_is_optimistic_in_practice` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Write the error decomposition identity and define each term
- [ ] What is bias in terms of the average model? What is variance?
- [ ] Which shapes on a learning curve mean more data will help, and which mean it will not?
- [ ] What does a rising validation curve tell you?
- [ ] What is the noise floor, and how would you estimate it?
- [ ] Name four things that control capacity
- [ ] Why is a validation score biased after model selection?
- [ ] What do you need in order to report an honest test score?

## Commit

- [ ] `./m check && ./m done 96` succeeded
