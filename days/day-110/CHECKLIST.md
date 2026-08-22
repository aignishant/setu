# Day 110 — CHECKLIST

**IDs covered:** ML-21 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-110/lab/boosting.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the nine-part report ending with when to boost, then all ensemble tests green.

## Setup

- [ ] `./m start 110` and `./m scaffold 110` run
- [ ] `days/day-110/lab/boosting.py` created
- [ ] No new packages installed

## ML-21 — gradient boosting from scratch

- [ ] Wrote the loop in ~20 lines and matched sklearn
- [ ] Can describe the algorithm in one sentence
- [ ] Can say what round 0 predicts, and why
- [ ] Ran `residuals_are_the_gradient()` and confirmed the identity numerically
- [ ] Can explain "gradient descent in **function space**"
- [ ] Can give the residual for all three losses

## The learning rate

- [ ] Ran `the_learning_rate_matters()` at four values
- [ ] Recorded rounds-to-best for η=1.0 ______ and η=0.02 ______
- [ ] Can say what large η does after its optimum
- [ ] Can state how η and `n_estimators` trade

## The difference from bagging

- [ ] Ran `boosting_overfits_and_bagging_does_not()`
- [ ] Confirmed boosting's test error **rose** and bagging's flattened
- [ ] Can say why `n_estimators` is a capacity parameter for one and not the other
- [ ] Can name what this makes mandatory on Day 112

## Weak base models

- [ ] Ran `base_models_must_be_weak()` across six depths
- [ ] Recorded the best depth: ______
- [ ] Can explain what a deep tree does to the sequence
- [ ] Can state the rule, and say it is the **opposite** of Day 108's
- [ ] Can say what depth controls besides capacity

## AdaBoost

- [ ] Wrote AdaBoost from scratch and matched sklearn
- [ ] Can write the α formula from memory
- [ ] Can say what α is when weighted error is 0.5
- [ ] Can explain the weight update `exp(−α·y·prediction)`
- [ ] Ran `adaboost_is_gradient_boosting()`
- [ ] Can state Friedman's result in one sentence
- [ ] Can say why AdaBoost is sensitive to label noise

## Practical

- [ ] Read `sequential_means_no_parallelism()`
- [ ] Can say what XGBoost parallelises, since it cannot parallelise across trees
- [ ] Read `when_to_boost_and_when_not_to()`; can give four situations
- [ ] Can state the honest closing note about Random Forest defaults

## Build brief

- [ ] `negative_gradient` — **TODO(me)**: three losses, docstring names function space
- [ ] `fit_gradient_boosting` — **TODO(me)**: staged history, validation, depth warning
- [ ] Warning names Day 108's opposite rule
- [ ] `staged_predictions` — **TODO(me)**: a generator
- [ ] `overfitting_curve` — **TODO(me)**: recommendation names a **number**
- [ ] `fit_adaboost` — **TODO(me)**: stops at α ≤ 0, warns on weight concentration
- [ ] `boosting_defaults` — **TODO(me)**: depth = interaction order, reasons throughout
- [ ] Can explain why the initial prediction depends on the loss

## Tests that must be able to fail

- [ ] `test_the_squared_error_residual_is_the_negative_gradient` — green
- [ ] `test_absolute_error_uses_only_the_sign` — green
- [ ] `test_log_loss_gradient_is_y_minus_sigmoid` — green
- [ ] `test_log_loss_rejects_a_non_binary_target` — green
- [ ] `test_an_unknown_loss_lists_the_known_ones` — green
- [ ] `test_the_gradient_docstring_names_function_space` — green
- [ ] `test_boosting_matches_sklearn` — green
- [ ] `test_the_training_loss_decreases` — green
- [ ] `test_the_history_has_one_entry_per_round` — green
- [ ] `test_staged_predictions_yields_every_round` — green
- [ ] `test_a_smaller_learning_rate_needs_more_rounds` — green
- [ ] `test_boosting_overfits_with_too_many_rounds` — green ← **today's real assessment**
- [ ] **Assumed more rounds were harmless (Day 108's habit), watched it go red** ← do not skip
- [ ] `test_the_recommendation_names_a_concrete_round_count` — green
- [ ] `test_training_past_the_optimum_is_warned_about` — green
- [ ] `test_a_deep_base_model_is_warned_about` — green
- [ ] **Boosted depth-12 trees and watched the sequence collapse into one tree** ← do not skip
- [ ] `test_shallow_base_models_are_not_warned_about` — green
- [ ] `test_the_initial_prediction_matches_the_loss` — green
- [ ] `test_boosting_rejects_a_bad_learning_rate` — green
- [ ] `test_adaboost_matches_sklearn` — green
- [ ] `test_a_stump_at_chance_gets_zero_weight` — green
- [ ] `test_a_better_stump_gets_more_say` — green
- [ ] `test_weights_stay_normalised` — green
- [ ] `test_label_noise_concentrates_the_weights` — green
- [ ] `test_clean_labels_do_not_concentrate` — green
- [ ] `test_adaboost_rejects_zero_one_labels` — green
- [ ] `test_depth_matches_the_interaction_order` — green
- [ ] `test_the_default_depth_is_shallow` — green
- [ ] `test_a_small_learning_rate_comes_with_more_rounds` — green
- [ ] `test_noisy_labels_avoid_exponential_loss` — green
- [ ] `test_every_boosting_default_has_a_reason` — green
- [ ] `test_an_impossible_interaction_order_is_refused` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Which error term does boosting attack, and how does that differ from bagging?
- [ ] Why is fitting residuals the same as gradient descent?
- [ ] Give the "residual" for squared, absolute and log loss
- [ ] Why must boosting's base models be weak?
- [ ] What does depth control besides capacity?
- [ ] Why does boosting overfit when bagging does not?
- [ ] How do η and `n_estimators` trade against each other?
- [ ] Why is AdaBoost sensitive to label noise?

## Commit

- [ ] `./m check && ./m done 110` succeeded
