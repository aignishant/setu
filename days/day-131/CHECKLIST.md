# Day 131 — CHECKLIST

**IDs covered:** DL-09 · **Principles served:** 1, 2, 4, 7

## Demo command

```bash
uv run python days/day-131/lab/optimisers.py
uv run python -m pytest tests/test_optim.py -v
```

Expected: the eight-part report ending with the epsilon table, then all optim tests green.

## Setup

- [ ] `./m start 131` and `./m scaffold 131` run
- [ ] `days/day-131/lab/optimisers.py` created
- [ ] `src/setu/optim.py` created (new module)
- [ ] No new packages — NumPy only

## The zoo

- [ ] Ran `the_update_rule_zoo()`
- [ ] Can write all five update rules from memory
- [ ] Can say how much state each one keeps
- [ ] Computed the optimiser memory for a 7B model in fp32: ______ GB
- [ ] Can say which failure each rule removes

## SGD's speed limit

- [ ] Ran `sgd_has_a_hard_speed_limit()`
- [ ] Recorded f after 200 at η = 0.0199 ______ and at η = 0.021 ______
- [ ] Can derive `η < 2/C` rather than recall it
- [ ] Can say why the limit is set by the steepest direction
- [ ] **Tried η = 0.02 exactly and watched it neither converge nor diverge** ← do not skip

## The ravine

- [ ] Ran `the_ravine()`
- [ ] Recorded steps to 1e-6: adam ______ rmsprop ______ sgd ______
- [ ] Can say why the learning rates in that table are not equal
- [ ] Can say what a shared-η comparison would actually measure

## Momentum

- [ ] Ran `momentum_kills_the_zigzag()`
- [ ] Recorded sign flips: sgd ______ momentum ______ adam ______
- [ ] Can explain why oscillation cancels and consistent motion accumulates
- [ ] Can say how Nesterov differs from plain momentum

## Adaptive methods

- [ ] Ran `adaptive_methods_normalise_each_coordinate()`
- [ ] Confirmed all three RMSProp steps are ~3.162
- [ ] Can say what "adaptive learning rate" actually means
- [ ] Can say why a normalised step is not always good news

## Bias correction

- [ ] Ran `bias_correction_is_not_optional()`
- [ ] Recorded the uncorrected first step ______ and corrected ______
- [ ] Can say which direction the error goes, and why
- [ ] Derived `(1−β₁)/√(1−β₂)` and checked it equals the printed ratio
- [ ] Can say how long the transient lasts at `β₂ = 0.999`

## Adam vs AdamW

- [ ] Ran `adam_plus_l2_is_not_adamw()`
- [ ] Recorded Adam+L2 retained: loud ______ quiet ______
- [ ] Recorded AdamW retained: loud ______ quiet ______
- [ ] Can say why the decay gets scaled under Adam and not under AdamW
- [ ] Can say why an Adam λ cannot be copied into AdamW
- [ ] Read the abstract of the decoupled-weight-decay paper

## Epsilon

- [ ] Ran `epsilon_is_not_just_numerical_hygiene()`
- [ ] Recorded the step at ε = 1e-8 ______ and ε = 1e-2 ______
- [ ] Can say what ε does besides prevent division by zero
- [ ] Can say why Principle 4 covers ε

## Build brief

- [ ] `OptimiserState` — **TODO(me)**: mutable, records the memory cost
- [ ] `make_optimiser` — **TODO(me)**: refuses `adam` + `weight_decay`
- [ ] `step` — **TODO(me)**: non-mutating, bias-corrected, skips bias decay
- [ ] `stability_limit` — **TODO(me)**
- [ ] `effective_step_sizes` — **TODO(me)**
- [ ] `compare_optimisers` — **TODO(me)**: dict of rule → its own rate
- [ ] `assert_bias_corrected` — **TODO(me)**
- [ ] `decay_report` — **TODO(me)**
- [ ] Can explain why `compare_optimisers` takes a dict rather than a list

## Tests that must be able to fail

- [ ] `test_the_stability_limit_is_two_over_the_curvature` — green
- [ ] `test_the_limit_note_names_the_steepest_direction` — green
- [ ] `test_sgd_converges_below_the_limit_and_diverges_above_it` — green
- [ ] `test_a_non_positive_curvature_is_refused` — green
- [ ] `test_adam_reaches_the_target_and_sgd_does_not` — green ← **today's headline**
- [ ] `test_momentum_reduces_the_zigzag` — green
- [ ] `test_one_optimiser_is_not_a_comparison` — green
- [ ] `test_adaptive_rules_normalise_wildly_different_gradients` — green
- [ ] `test_sgd_does_not_normalise` — green
- [ ] `test_the_step_docstring_warns_about_a_tiny_consistent_gradient` — green
- [ ] `test_the_uncorrected_first_step_is_too_large_not_too_small` — green
- [ ] **Removed bias correction and watched the first step triple** ← do not skip
- [ ] `test_a_corrected_constant_gradient_steps_by_exactly_the_learning_rate` — green
- [ ] `test_adam_with_weight_decay_is_refused_and_points_at_adamw` — green
- [ ] `test_adamw_decays_two_parameters_identically` — green
- [ ] **Folded λθ into the gradient instead and watched the two diverge** ← do not skip
- [ ] `test_weight_decay_does_not_touch_the_biases` — green
- [ ] `test_the_decay_report_calls_adam_l2_coupled` — green
- [ ] `test_a_report_with_no_decay_raises` — green
- [ ] `test_the_step_function_does_not_mutate_its_parameters` — green
- [ ] `test_sgd_moves_against_the_gradient` — green
- [ ] `test_the_step_count_advances` — green
- [ ] `test_an_unstepped_adam_state_is_refused` — green
- [ ] `test_the_guard_message_quotes_the_factor` — green
- [ ] `test_every_hyperparameter_is_refused_when_nonsensical` — green
- [ ] `test_an_unknown_rule_lists_the_known_ones` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Write all five update rules from memory
- [ ] Derive SGD's stability limit on a quadratic
- [ ] Why does one learning rate fail on an ill-conditioned surface?
- [ ] What does momentum cancel, and what does it accumulate?
- [ ] What does dividing by `√s` actually normalise away?
- [ ] Is the uncorrected first Adam step too large or too small — and by what factor?
- [ ] Why is Adam + L2 not AdamW?
- [ ] How much memory does Adam add to a 7B-parameter model?

## Commit

- [ ] `./m check && ./m done 131` succeeded
