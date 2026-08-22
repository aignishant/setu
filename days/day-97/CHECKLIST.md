# Day 97 — CHECKLIST

**IDs covered:** ML-08 · **Principles served:** 1, 7, 8, 15

## Demo command

```bash
uv run python days/day-97/lab/crossval.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the grouped-leak comparison, then all model tests green.

## Setup

- [ ] `./m start 97` and `./m scaffold 97` run
- [ ] `days/day-97/lab/crossval.py` created
- [ ] No new packages installed

## ML-08 — why not one split

- [ ] Ran `one_split_is_noisy()`; recorded the spread across 20 splits: ______
- [ ] Can say what reporting one of those numbers amounts to
- [ ] Can say what the spread actually represents

## k-fold

- [ ] Ran `k_fold_uses_everything()` at k = 2, 5, 10 and LOO
- [ ] Can state the bias/variance trade-off in the **estimate** as k grows
- [ ] Can say why leave-one-out is not simply "the most thorough"

## Stratification

- [ ] Ran `stratification_matters_when_imbalanced()`
- [ ] Saw a plain `KFold` fold with very few or zero positives
- [ ] Can say what happens to recall or ROC-AUC in that fold
- [ ] Can state the rule for classification
- [ ] Know what sklearn does automatically, and where that does **not** help you

## The grouped leak

- [ ] Ran `the_grouped_leak()`
- [ ] Recorded KFold accuracy ______ vs GroupKFold ______ — inflation ______ pp
- [ ] Can explain what the model actually learned
- [ ] Can say which number predicts production behaviour
- [ ] Can name the two earlier days with the same problem

## Time series

- [ ] Ran `time_series_split()` and read the fold structure
- [ ] Confirmed train always precedes test
- [ ] Noticed the training set **grows** across folds
- [ ] Can say why averaging those folds mixes two effects

## The choice is a claim

- [ ] Read the five-row table and can state each splitter's claim
- [ ] Can state the resolving question in one sentence

## Nested CV

- [ ] Ran `nested_cross_validation()`
- [ ] Recorded flat-CV best ______ vs nested outer mean ______
- [ ] Can say which loop chooses and which measures
- [ ] Can name the two earlier days this bias comes from
- [ ] Ran `what_to_report()`; can say why a t-test across folds is over-confident

## Build brief

- [ ] `choose_splitter` — **TODO(me)**: states the claim, warns on rare classes
- [ ] `cross_validate` — **TODO(me)**: fresh model per fold, returns a distribution
- [ ] `assert_no_group_leak` — **TODO(me)**: names offending groups
- [ ] `assert_temporal_order` — **TODO(me)**: refuses simultaneity too
- [ ] `nested_cross_validate` — **TODO(me)**: records per-fold choices, reports `optimism`
- [ ] `describe_cv` — **TODO(me)**: spread included, no significance claim
- [ ] Can explain why `model_fn` must return a fresh model

## Tests that must be able to fail

- [ ] `test_classification_always_gets_stratified` — green
- [ ] `test_regression_gets_plain_kfold` — green
- [ ] `test_groups_beat_stratification` — green
- [ ] `test_time_order_beats_everything` — green
- [ ] `test_every_choice_states_its_claim` — green
- [ ] `test_a_class_rarer_than_the_fold_count_is_warned_about` — green
- [ ] `test_an_unknown_task_raises` — green
- [ ] `test_cv_returns_a_distribution_not_a_number` — green
- [ ] `test_a_fresh_model_is_used_per_fold` — green
- [ ] **Reused one model instance, watched the id assertion go red, fixed it** ← do not skip
- [ ] `test_disagreeing_folds_are_warned_about` — green
- [ ] `test_missing_groups_are_refused` / `test_too_few_splits_is_refused` — green
- [ ] `test_plain_kfold_leaks_groups_and_group_kfold_does_not` — green ← **today's real assessment**
- [ ] `test_a_group_appearing_on_both_sides_is_caught` — green
- [ ] `test_a_clean_group_split_passes` — green
- [ ] `test_group_kfold_never_leaks_a_group` — green
- [ ] `test_shuffled_kfold_does_leak_a_group` — green
- [ ] **Made the guard never raise, watched this one go red, fixed it** ← do not skip
- [ ] `test_training_after_test_is_refused` — green
- [ ] `test_a_chronological_split_passes` — green
- [ ] `test_simultaneous_rows_are_refused` — green
- [ ] `test_time_series_split_always_passes_the_order_check` — green
- [ ] `test_nested_cv_is_less_optimistic_than_flat_cv` — green
- [ ] `test_nested_cv_records_the_choice_per_outer_fold` — green
- [ ] `test_unstable_tuning_is_surfaced` — green
- [ ] `test_an_empty_grid_is_refused` — green
- [ ] `test_the_description_includes_the_spread` — green
- [ ] `test_the_description_makes_no_significance_claim` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What two problems does CV solve, compared with one split?
- [ ] What claim does each of the five splitters make about your data?
- [ ] What question resolves which one you need?
- [ ] Describe the grouped leak and why the model scores well on it
- [ ] Why must classification CV be stratified even when balanced?
- [ ] What is different about `TimeSeriesSplit`'s folds?
- [ ] Which loop chooses and which measures in nested CV?
- [ ] Why is a t-test across CV folds over-confident?

## Commit

- [ ] `./m check && ./m done 97` succeeded
