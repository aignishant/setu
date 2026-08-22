# Day 99 — CHECKLIST

**IDs covered:** ML-10 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-99/lab/logistic.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the nine-part report ending with the threshold table, then all model tests green.

## Setup

- [ ] `./m start 99` and `./m scaffold 99` run
- [ ] `days/day-99/lab/logistic.py` created
- [ ] No new packages installed

## ML-10 — why not linear

- [ ] Ran `why_not_linear_regression()`; recorded the prediction range
- [ ] Can give **both** objections to linear regression on a binary target

## The sigmoid

- [ ] Read the σ(z) table; confirmed σ(0) = 0.5 and σ(z) + σ(−z) = 1
- [ ] Can say why it never reaches 0 or 1, and why that matters
- [ ] Verified the derivative identity numerically
- [ ] Ran `numerically_stable_sigmoid()` and saw the naive form overflow
- [ ] Can write the stable branch for z < 0

## Log loss

- [ ] Read the cost table and compared log loss with squared error
- [ ] Can say what happens as p → 0 for each
- [ ] Can say why unbounded punishment produces **calibrated** outputs
- [ ] Can say why clipping is necessary

## The gradient

- [ ] Derived it and checked it **numerically**
- [ ] Can write `∇L = Xᵀ(σ(Xβ) − y)/n` from memory
- [ ] Can say why it is identical in form to linear regression's
- [ ] Can say what cancels, and why that pairing is standard

## Fitting

- [ ] Fitted by gradient descent and matched sklearn
- [ ] Passed `penalty=None` — and can say what happens if you forget

## Log-odds

- [ ] Ran `coefficients_are_log_odds()` and read the baseline table
- [ ] Can state the correct interpretation of β in one sentence
- [ ] Can say why there is no single "effect on probability"

## Separation

- [ ] Ran `separable_data_diverges()` and watched |β| grow
- [ ] Can say why no finite optimum exists
- [ ] Can name **both** things perfect separation means

## The threshold

- [ ] Ran `the_threshold_is_a_separate_decision()` and read the recall column
- [ ] Can say what `predict()` silently does
- [ ] Can say why 0.5 is rarely right on imbalanced data
- [ ] Can name the two days that decide the threshold properly

## Build brief

- [ ] `sigmoid` — **TODO(me)**: stable branches, symmetric
- [ ] `log_loss` — **TODO(me)**: clipped, validates target and probabilities
- [ ] `fit_logistic` — **TODO(me)**: reuses Day 95, intercept unpenalised, warns on separation
- [ ] `predict_proba` — **TODO(me)**: probabilities only
- [ ] `odds_ratio` — **TODO(me)**: interpretation says **odds**, never percentage points
- [ ] `probability_change` — **TODO(me)**: requires a baseline
- [ ] `detect_separation` — **TODO(me)**: warns about **both** problems
- [ ] **There is deliberately no `predict()`** — can explain why

## Tests that must be able to fail

- [ ] `test_the_sigmoid_is_stable_at_extremes` — green
- [ ] **Used the naive form, watched z=−800 overflow, branched it** ← do not skip
- [ ] `test_the_sigmoid_is_symmetric` / `..._a_half_at_zero` / `..._matches_scipy` — green
- [ ] `test_log_loss_matches_sklearn` — green
- [ ] `test_log_loss_punishes_confident_wrongness_without_limit` — green
- [ ] `test_a_perfect_prediction_costs_almost_nothing` — green
- [ ] `test_clipping_prevents_an_infinite_loss` — green
- [ ] `test_log_loss_rejects_a_non_binary_target` / `..._probabilities` / `..._length` — green
- [ ] `test_it_matches_sklearn_when_both_are_unregularised` — green
- [ ] **Forgot `penalty=None` and watched a correct implementation look wrong** ← do not skip
- [ ] `test_it_recovers_the_generating_coefficients` — green
- [ ] `test_the_gradient_is_correct` — green
- [ ] `test_the_loss_decreases` — green
- [ ] `test_probabilities_stay_inside_the_unit_interval` — green
- [ ] `test_there_is_no_predict_method` — green
- [ ] `test_a_non_binary_target_is_refused` / `test_a_single_class_is_refused` — green
- [ ] `test_unscaled_features_are_refused_with_day_95s_reason` — green
- [ ] `test_the_intercept_is_not_penalised` — green
- [ ] `test_separable_data_is_detected` — green
- [ ] `test_the_separation_warning_mentions_both_problems` — green
- [ ] **Warned only about convergence, watched the leak assertion go red** ← do not skip
- [ ] `test_non_separable_data_is_not_flagged` — green
- [ ] `test_an_unpenalised_fit_on_separable_data_warns` — green
- [ ] `test_regularisation_bounds_the_coefficients_on_separable_data` — green
- [ ] `test_odds_ratios_are_exponentiated_coefficients` — green
- [ ] `test_the_interpretation_says_odds_not_probability` — green ← **today's real assessment**
- [ ] **Wrote "increases the probability by", watched it go red, fixed the wording** ← do not skip
- [ ] `test_the_same_coefficient_moves_probability_differently_by_baseline` — green
- [ ] `test_probability_change_is_consistent_with_the_odds_ratio` — green
- [ ] `test_probability_change_refuses_a_degenerate_baseline` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give both reasons linear regression fails on a binary target
- [ ] Why does log loss produce calibrated probabilities and squared error not?
- [ ] Write the gradient and say why it looks like linear regression's
- [ ] What does a logistic coefficient actually mean?
- [ ] Why can you not state a coefficient's effect on probability as one number?
- [ ] Why do coefficients diverge on separable data?
- [ ] What does perfect separation usually mean on real data?
- [ ] Why does this module deliberately have no `predict()`?

## Commit

- [ ] `./m check && ./m done 99` succeeded
