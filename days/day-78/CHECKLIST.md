# Day 78 — CHECKLIST

**IDs covered:** FE-03 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-78/lab/imbalance.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the nine-part report ending with the recommended order, then all feature tests green.

## Setup

- [ ] `./m start 78` and `./m scaffold 78` run
- [ ] `uv add "imbalanced-learn==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-78/lab/imbalance.py` created

## FE-03 — the metric problem

- [ ] Ran `accuracy_is_meaningless()`; recorded the accuracy of "always no": ______
- [ ] Confirmed it caught **zero** positives
- [ ] Ran `the_metrics_that_work()`; recorded precision, recall, ROC-AUC, PR-AUC
- [ ] Know what the PR-AUC baseline is
- [ ] Can say why ROC-AUC flatters an imbalanced model
- [ ] Ran `precision_is_day_63_again()`
- [ ] Can map all four terms between medical and classifier vocabulary
- [ ] Can say why precision collapses as the positive rate falls

## The threshold

- [ ] Ran `the_threshold_is_yours()` and **read the whole table**
- [ ] Can say what 0.5 actually is
- [ ] Ran `choosing_a_threshold_by_cost()`; recorded the cheapest threshold: ______
- [ ] Can say what "tuning for the business" concretely means
- [ ] Know which dataset a threshold must be tuned on, and why

## Weights and resampling

- [ ] Ran `class_weights_cost_nothing()`
- [ ] Noted that PR-AUC barely moved, and can say why
- [ ] Ran `smote_inside_the_split_only()`; recorded both PR-AUCs and the inflation: ______×
- [ ] Can explain **mechanically** how a synthetic point leaks into test
- [ ] Can say why random oversampling has the same problem
- [ ] Ran `resampling_breaks_calibration()`; recorded both mean predicted probabilities
- [ ] Can say when broken calibration is acceptable and when it is not
- [ ] Read `the_order_to_try_things()` and can recite all four steps **in order**

## Build brief

- [ ] `imbalance_report` — **TODO(me)**: severity grades, baseline accuracy, warns against accuracy
- [ ] `threshold_sweep` — **TODO(me)**: handles zero alarms, validates scores
- [ ] `choose_threshold` — **TODO(me)**: minimises **cost**, not F1
- [ ] `assert_resampling_after_split` — **TODO(me)**: refuses the leaking order
- [ ] `resample` — **TODO(me)**: record with calibration warning, refuses tiny minorities
- [ ] `calibration_check` — **TODO(me)**: detects what resampling broke
- [ ] Can explain why cost beats F1 as an objective

## Tests that must be able to fail

- [ ] `test_severity_is_graded` — four green cases
- [ ] `test_the_majority_baseline_shows_why_accuracy_is_useless` — green
- [ ] `test_the_pr_auc_baseline_is_the_positive_rate` — green
- [ ] `test_severe_imbalance_warns_against_accuracy` — green
- [ ] `test_a_balanced_target_is_not_warned_about` — green
- [ ] `test_imbalance_report_rejects_non_binary` — green
- [ ] `test_lowering_the_threshold_trades_precision_for_recall` — green
- [ ] `test_zero_alarms_gives_precision_zero_not_an_error` — green
- [ ] `test_sweep_rejects_scores_outside_zero_one` / `..._length_mismatch` — green
- [ ] `test_an_expensive_miss_lowers_the_threshold` — green
- [ ] `test_an_expensive_false_alarm_raises_the_threshold` — green
- [ ] **Made `choose_threshold` optimise F1, watched both cost tests go red, fixed it** ← do not skip
- [ ] `test_the_chosen_threshold_beats_the_default_on_cost` — green
- [ ] `test_costs_must_be_positive` — green
- [ ] `test_resampling_before_the_split_is_refused` — green ← **today's real assessment**
- [ ] `test_resampling_after_the_split_is_allowed` — green
- [ ] `test_resample_balances_the_classes` — green
- [ ] `test_the_resample_record_warns_about_calibration` — green
- [ ] `test_resample_refuses_a_tiny_minority` — green
- [ ] `test_class_weight_is_not_a_resampling_strategy` — green
- [ ] `test_a_well_calibrated_model_is_recognised` — green
- [ ] `test_an_over_confident_model_is_caught` — green
- [ ] `test_calibration_bins_are_returned` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is accuracy meaningless at a 2% positive rate?
- [ ] Why does ROC-AUC flatter and PR-AUC not?
- [ ] Map recall, precision and prevalence onto Day 63's vocabulary
- [ ] What is the 0.5 threshold, really?
- [ ] How do you choose a threshold using costs?
- [ ] Explain mechanically how SMOTE before the split leaks
- [ ] What does resampling do to predicted probabilities, and when does that matter?
- [ ] Recite the four-step order and say why SMOTE is last

## Commit

- [ ] `./m check && ./m done 78` succeeded
