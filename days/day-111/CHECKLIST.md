# Day 111 — CHECKLIST

**IDs covered:** ML-22 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-111/lab/gbm.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the eight-part report ending with what boosting cannot do, then all ensemble tests green.

## Setup

- [ ] `./m start 111` and `./m scaffold 111` run
- [ ] `days/day-111/lab/gbm.py` created
- [ ] No new packages installed

## ML-22 — the classifier

- [ ] Ran `the_classifier_is_the_same_loop()` and matched sklearn
- [ ] Can state the only difference from Day 110's regressor
- [ ] Recorded the score range after 200 rounds: ______
- [ ] Can say what space the trees live in
- [ ] Can say where the probability appears

## The initial prediction

- [ ] Ran `the_initial_prediction_matters()` on 3%-positive data
- [ ] Recorded loss after 5 rounds from log-odds ______ vs from zero ______
- [ ] Can say what starting at 0 actually means in probability terms
- [ ] Can say where this detail usually gets forgotten

## Leaf values

- [ ] Ran `leaf_values_are_log_odds()`
- [ ] Confirmed `sigmoid(decision_function)` equals `predict_proba`
- [ ] Can say what a leaf value of +0.4 means, precisely
- [ ] Can name the day that established the log-odds reading

## Calibration

- [ ] Ran `is_it_calibrated()` on three configurations
- [ ] Recorded max calibration gap for the well-stopped ______ and overfitted ______ model
- [ ] Can say why boosting *should* calibrate
- [ ] Can say what overfitting does to the probabilities, and in which direction
- [ ] Can name what breaks downstream if you skip the check

## The histogram trick

- [ ] Ran `the_histogram_trick()` on 60,000 rows
- [ ] Recorded exact ______ s vs histogram ______ s
- [ ] Can explain the binning in one sentence
- [ ] Can say what binning costs and what it gains besides speed
- [ ] Can say what this has to do with Days 112–113

## Missing values

- [ ] Ran `missing_values_natively()`
- [ ] Confirmed `GradientBoostingClassifier` raised on NaN
- [ ] Can say what the histogram version does with NaN, and per what
- [ ] Can say why that is better than imputation when missingness is informative
- [ ] Can state the risk it introduces to your pipeline

## Quantile loss

- [ ] Fitted three quantile models and built a band
- [ ] Recorded empirical coverage: ______ (target 0.90)
- [ ] Recorded band width where |x| < 1 ______ and |x| ≥ 1 ______
- [ ] Can say what a mean-predicting model cannot tell you
- [ ] Can name the failure mode of independently fitted quantiles

## What remains impossible

- [ ] Ran `what_boosting_still_cannot_do()`
- [ ] Confirmed predictions were flat beyond the training range
- [ ] Can say why the sequential mechanism changes nothing about it

## Build brief

- [ ] `initial_score` — **TODO(me)**: mean / median / **base-rate log-odds**
- [ ] `boosted_scores_to_proba` — **TODO(me)**: reuses Day 99's sigmoid
- [ ] `check_boosting_calibration` — **TODO(me)**: reports **direction**, reuses Day 101
- [ ] `binning_summary` — **TODO(me)**: unaffected features, resolution lost
- [ ] `quantile_band` — **TODO(me)**: counts crossings rather than hiding them
- [ ] `band_coverage` — **TODO(me)**: width by tercile, positive shortfall
- [ ] Can explain why the log-loss initial score is not zero

## Tests that must be able to fail

- [ ] `test_the_squared_loss_starts_at_the_mean` — green
- [ ] `test_the_absolute_loss_starts_at_the_median` — green
- [ ] `test_the_log_loss_starts_at_the_base_rate_log_odds` — green ← **today's real assessment**
- [ ] `test_the_log_start_recovers_the_base_rate` — green
- [ ] **Started at 0 and watched the first rounds climb to the base rate** ← do not skip
- [ ] `test_a_single_class_target_does_not_produce_infinity` — green
- [ ] `test_the_log_start_rejects_a_non_binary_target` — green
- [ ] `test_initial_score_rejects_an_empty_target` — green
- [ ] `test_the_docstring_warns_about_imbalanced_starts` — green
- [ ] `test_scores_are_log_odds_not_probabilities` — green
- [ ] `test_the_conversion_reuses_day_99s_sigmoid` — green
- [ ] `test_the_conversion_docstring_says_log_odds` — green
- [ ] `test_extreme_scores_do_not_overflow` — green
- [ ] `test_a_well_stopped_booster_is_calibrated` — green
- [ ] `test_an_overfitted_booster_becomes_over_confident` — green
- [ ] **Reported only the gap without the direction, watched it go red** ← do not skip
- [ ] `test_the_calibration_warning_mentions_cost_based_thresholds` — green
- [ ] `test_calibration_reuses_day_101` — green
- [ ] `test_calibration_rejects_impossible_probabilities` — green
- [ ] `test_binning_leaves_low_cardinality_features_alone` — green
- [ ] `test_binning_reports_lost_resolution` — green
- [ ] `test_the_binning_note_mentions_regularisation` — green
- [ ] `test_binning_rejects_too_few_bins` — green
- [ ] `test_the_histogram_implementation_is_faster` — green
- [ ] `test_the_band_covers_the_truth_about_as_often_as_claimed` — green
- [ ] `test_the_band_widens_where_the_noise_widens` — green
- [ ] `test_quantile_crossings_are_counted_not_hidden` — green
- [ ] `test_a_clean_band_reports_no_crossings` — green
- [ ] `test_the_band_needs_the_requested_quantiles` — green
- [ ] `test_coverage_reports_width_by_tercile` — green
- [ ] `test_under_coverage_is_reported_as_a_positive_shortfall` — green
- [ ] `test_coverage_rejects_a_length_mismatch` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What changes between the boosting regressor and classifier?
- [ ] What space do the trees live in, and where does the probability come from?
- [ ] Why must the classifier start at the base-rate log-odds?
- [ ] What does a leaf value of 0.4 mean?
- [ ] When is a booster calibrated, and when does it stop being?
- [ ] What breaks downstream if the probabilities are over-confident?
- [ ] Explain the histogram trick and its two effects
- [ ] How do you get a prediction interval from a boosted model, and what can go wrong?

## Commit

- [ ] `./m check && ./m done 111` succeeded
