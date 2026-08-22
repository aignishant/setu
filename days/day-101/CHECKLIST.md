# Day 101 — CHECKLIST

**IDs covered:** ML-12 · **Principles served:** 1, 7, 8, 10

## Demo command

```bash
uv run python days/day-101/lab/curves.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the imbalance and calibration tables, then all model tests
green.

## Setup

- [ ] `./m start 101` and `./m scaffold 101` run
- [ ] `days/day-101/lab/curves.py` created
- [ ] No new packages installed

## ML-12 — ROC

- [ ] Ran `the_roc_curve()` and read the TPR/FPR table
- [ ] Confirmed the pairwise simulation matched `roc_auc_score`
- [ ] Can state what AUC **means** in one sentence
- [ ] Can say what AUC never looks at

## Imbalance

- [ ] Ran `imbalance_breaks_roc()` across four positive rates
- [ ] Recorded ROC-AUC at 0.5 ______ and at 0.001 ______
- [ ] Recorded PR-AUC at 0.5 ______ and at 0.001 ______
- [ ] Can explain the difference in terms of **one box**
- [ ] Ran `pr_auc_needs_its_baseline()`
- [ ] Can say what a random model's PR-AUC equals
- [ ] Can say why "PR-AUC = 0.30" is unquotable alone

## Calibration

- [ ] Ran `auc_cannot_see_calibration()` and confirmed **identical** AUC in all rows
- [ ] Can say what the Brier score saw that AUC did not
- [ ] Can connect this to Day 100's cost threshold
- [ ] Ran `a_calibration_curve()` and compared predicted with actual per bin
- [ ] Can say why logistic regression is calibrated by construction
- [ ] Can say why tree ensembles usually are not
- [ ] Ran `fixing_calibration()`; confirmed AUC barely moved and Brier improved
- [ ] Can explain the **three-way** split and why each part is needed

## Thresholds

- [ ] Ran `choosing_a_threshold_properly()`
- [ ] Recorded the best-F1 threshold ______ and the cost-optimal ______
- [ ] Confirmed 0.5 was the most expensive on test
- [ ] Can say why a threshold is a fitted parameter
- [ ] Ran `curves_need_the_positive_class()` and saw the single-class failure
- [ ] Can say where this bites in cross-validation

## Build brief

- [ ] `roc_auc` — **TODO(me)**: pairwise interpretation, **raises** on one class
- [ ] `pr_auc` — **TODO(me)**: baseline and lift, base rate in the interpretation
- [ ] `calibration_report` — **TODO(me)**: ECE, direction, skips sparse bins
- [ ] `assert_calibrated_before_costing` — **TODO(me)**: names the direction
- [ ] `tune_threshold` — **TODO(me)**: delegates to Day 100, warns it is optimistic
- [ ] `evaluate_at_threshold` — **TODO(me)**: reuses Day 100's confusion, keeps 0.5 visible
- [ ] Can explain why a single-class input raises instead of returning nan

## Tests that must be able to fail

- [ ] `test_auc_matches_sklearn` — green
- [ ] `test_auc_is_the_pairwise_ranking_probability` — green
- [ ] `test_the_interpretation_uses_the_pairwise_phrasing` — green
- [ ] `test_a_single_class_raises_rather_than_returning_nan` — green
- [ ] **Returned nan instead, watched a CV mean become nan with no explanation** ← do not skip
- [ ] `test_rare_positives_get_a_pr_auc_recommendation` — green
- [ ] `test_roc_auc_is_stable_across_imbalance_and_pr_auc_is_not` — green
- [ ] `test_a_random_model_scores_the_positive_rate_on_pr` — green
- [ ] `test_pr_auc_reports_lift_not_just_the_score` — green
- [ ] `test_the_pr_interpretation_names_the_base_rate` — green
- [ ] `test_pr_auc_needs_at_least_one_positive` — green
- [ ] `test_auc_cannot_see_a_calibration_failure` — green ← **today's real assessment**
- [ ] `test_a_well_calibrated_model_is_recognised` — green
- [ ] `test_an_overconfident_model_is_named_as_such` — green
- [ ] `test_an_underconfident_model_is_named_as_such` — green
- [ ] **Detected only overconfidence, watched the underconfident case go red** ← do not skip
- [ ] `test_sparse_bins_are_skipped_and_counted` — green
- [ ] `test_the_brier_score_matches_sklearn` — green
- [ ] `test_calibration_needs_at_least_two_bins` — green
- [ ] `test_cost_thresholding_is_refused_on_an_uncalibrated_model` — green
- [ ] `test_cost_thresholding_is_allowed_on_a_calibrated_model` — green
- [ ] `test_calibration_is_monotonic_so_ranking_survives` — green
- [ ] `test_the_cost_objective_delegates_to_day_100` — green
- [ ] `test_tuning_warns_that_the_score_is_optimistic` — green
- [ ] `test_recall_at_precision_requires_the_precision_floor` — green
- [ ] `test_precision_at_k_requires_a_capacity` — green
- [ ] `test_a_costlier_miss_lowers_the_tuned_threshold` — green
- [ ] `test_evaluation_reports_the_positive_rate` — green
- [ ] `test_evaluation_keeps_the_default_visible` — green
- [ ] `test_evaluation_reuses_day_100s_confusion` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does ROC-AUC mean, in pairwise terms?
- [ ] Which single box explains ROC's behaviour on imbalanced data?
- [ ] What is PR-AUC's baseline, and why does that matter for quoting it?
- [ ] Why can AUC not detect a calibration failure?
- [ ] What does calibration have to do with Day 100's cost threshold?
- [ ] Why must calibration use a third split?
- [ ] Why is a tuned threshold a fitted parameter?
- [ ] When is ROC-AUC undefined, and where does that bite?

## Commit

- [ ] `./m check && ./m done 101` succeeded
