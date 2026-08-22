# Day 95 — CHECKLIST

**IDs covered:** ML-06 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-95/lab/descent.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the learning-rate and scaling tables, then all model tests
green.

## Setup

- [ ] `./m start 95` and `./m scaffold 95` run
- [ ] `days/day-95/lab/descent.py` created
- [ ] No new packages installed

## ML-06 — why iterate at all

- [ ] Ran `why_not_just_solve_it()`; recorded closed-form vs one-step timings at p=800
- [ ] Can give **both** reasons gradient descent exists
- [ ] Can say why linear regression is the right place to learn it

## The gradient

- [ ] Derived the gradient by hand
- [ ] Compared it against a **numerical** derivative and confirmed agreement
- [ ] Can say what a gradient check is and why Phase 14 depends on it
- [ ] Can state what a wrong gradient does (hint: not crash)

## Descending

- [ ] Ran `batch_descent()` and watched the loss fall
- [ ] Confirmed GD reached the **closed-form** coefficients
- [ ] Compared true / exact / iterated side by side

## The learning rate

- [ ] Ran `the_learning_rate_is_everything()` and **read the verdict column**
- [ ] Recorded the smallest rate that converged: ______
- [ ] Recorded the smallest rate that diverged: ______
- [ ] Can say what to do first when you see `nan` in a training log

## Scaling

- [ ] Ran `scaling_is_not_optional()` and **read both blocks**
- [ ] Confirmed **no** learning rate worked on the raw features
- [ ] Can describe the loss surface geometrically
- [ ] Can say what Day 80's scaler is actually for

## The three variants

- [ ] Ran `batch_vs_stochastic_vs_mini()` and recorded updates and time for each
- [ ] Can say how many rows batch GD reads to take one step
- [ ] Can say why SGD never quite settles
- [ ] Can say why 32–256 is the usual mini-batch range

## Noise, and stopping

- [ ] Ran `the_noise_is_useful()` with four starting points
- [ ] Confirmed the noiseless version got stuck in the shallower minimum
- [ ] Can say why that makes noise a feature on non-convex surfaces
- [ ] Can say why today's loss is different from Phase 14's
- [ ] Can name all three stopping rules
- [ ] Can say why a capped run must not be reported as fitted

## Build brief

- [ ] `DescentResult` — frozen, carries the evidence it fitted
- [ ] `gradient_descent` — **TODO(me)**: three variants, shuffles per epoch, per-epoch history
- [ ] Refuses unscaled features by default, and **names the ratio**
- [ ] `gradient_check` — **TODO(me)**: **central** difference
- [ ] `diagnose_descent` — **TODO(me)**: every diagnosis actionable
- [ ] `learning_rate_search` — **TODO(me)**: diverged rates reported, not dropped
- [ ] `assert_converged` — **TODO(me)**: cap is not convergence
- [ ] Can explain why `converged` is true only for `stop_reason='tolerance'`

## Tests that must be able to fail

- [ ] `test_it_reaches_the_closed_form_answer` — green
- [ ] `test_it_recovers_the_generating_coefficients` — green
- [ ] `test_the_loss_decreases_monotonically_in_batch_mode` — green
- [ ] `test_the_history_has_one_entry_per_epoch` — green
- [ ] `test_all_three_variants_reach_a_similar_answer` — green
- [ ] `test_stochastic_takes_far_more_updates_per_epoch` — green
- [ ] `test_a_high_learning_rate_diverges_and_says_so` — green
- [ ] `test_a_tiny_learning_rate_hits_the_cap` — green
- [ ] `test_converged_is_true_only_for_tolerance` — green
- [ ] **Set `converged=True` for a capped run, watched it go red, fixed it** ← do not skip
- [ ] `test_unscaled_features_are_refused` — green ← **today's real assessment**
- [ ] **Made the message generic, watched the ratio assertion go red, named the columns** ← do not skip
- [ ] `test_the_scaling_check_can_be_overridden` — green
- [ ] `test_scaled_features_pass_the_check` — green
- [ ] `test_a_non_finite_input_raises` — green
- [ ] `test_a_length_mismatch_names_both` — green
- [ ] `test_a_non_positive_learning_rate_raises` — green
- [ ] `test_descent_is_reproducible` — green
- [ ] `test_the_gradient_check_passes_on_a_correct_derivative` — green
- [ ] `test_the_gradient_check_catches_a_wrong_derivative` — green
- [ ] **Dropped the factor of 2 in a real gradient and watched training converge to the wrong answer** ← do not skip
- [ ] `test_the_gradient_check_uses_a_central_difference` — green
- [ ] `test_gradient_check_rejects_a_bad_epsilon` — green
- [ ] `test_a_diverged_run_is_diagnosed_with_an_action` — green
- [ ] `test_a_capped_run_with_a_falling_loss_suggests_more_epochs` — green
- [ ] `test_a_converged_run_is_reported_as_healthy` — green
- [ ] `test_every_diagnosis_is_actionable` — green
- [ ] `test_the_search_recommends_a_working_rate` — green
- [ ] `test_diverged_rates_are_reported_not_hidden` — green
- [ ] `test_a_search_where_everything_diverges_suggests_scaling` — green
- [ ] `test_assert_converged_accepts_a_converged_run` — green
- [ ] `test_assert_converged_refuses_a_capped_run` — green
- [ ] `test_assert_converged_tells_a_diverged_run_to_lower_the_rate` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give both reasons gradient descent exists despite the closed form
- [ ] What is a gradient check, and what failure does it catch?
- [ ] Why central difference rather than forward?
- [ ] Describe what happens at too small and too large a learning rate
- [ ] Why does unscaled data break gradient descent, geometrically?
- [ ] Compare the three variants by updates, cost and path
- [ ] When is SGD's noise a feature rather than a defect?
- [ ] Why is hitting the iteration cap not convergence?

## Commit

- [ ] `./m check && ./m done 95` succeeded
