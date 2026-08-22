# Day 127 — CHECKLIST

**IDs covered:** DL-04 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-127/lab/backprop.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with reverse-mode autodiff, then all nn tests green.

## Setup

- [ ] `./m start 127` and `./m scaffold 127` run
- [ ] `days/day-127/lab/backprop.py` created
- [ ] No new packages — still NumPy only

## DL-04 — the chain rule

- [ ] Ran `the_chain_rule_on_one_path()`
- [ ] Derived `∂L/∂w` on paper for the one-weight case
- [ ] Recorded analytic ______ vs numeric ______
- [ ] Can say why the **central** difference is used

## Why backprop is an algorithm

- [ ] Ran `why_the_order_matters()`
- [ ] Can say which terms are shared across weights in a layer
- [ ] Can state the complexity before and after
- [ ] Can say what backprop adds to the chain rule

## The derivation

- [ ] Wrote out all six gradient expressions **on paper**
- [ ] Checked every shape annotation
- [ ] Can say why gradients share their parameters' shapes
- [ ] Can say what determines each transpose

## The check

- [ ] Implemented backprop and ran the numerical check
- [ ] Recorded relative error per parameter (all below 1e-6?)
- [ ] Can say what a passing check establishes
- [ ] Ran `what_a_wrong_gradient_looks_like()` on four planted bugs
- [ ] Confirmed **every one still trains**
- [ ] Can say which bug looks like a learning-rate problem, and why

## Batching

- [ ] Ran `the_batch_dimension()` at three batch sizes
- [ ] Can say what sum vs mean does to the effective learning rate
- [ ] Can say why frameworks average
- [ ] Can state the double-division trap for the bias gradient

## Vanishing gradients

- [ ] Ran `where_gradients_die()` on all three configurations
- [ ] Recorded |δ| at layers 12 and 1 for sigmoid
- [ ] Can compute `0.25¹²` and say what it means
- [ ] Can name the two days that fix this
- [ ] Ran `backprop_is_reverse_mode_autodiff()`
- [ ] Can say when forward mode would be better
- [ ] Can say why a network is the reverse-mode case

## Build brief

- [ ] `activation_derivative` — **TODO(me)**: docstring names the 0.25 peak
- [ ] `dense_backward` — **TODO(me)**: asserts shapes, sums the bias over the batch
- [ ] `backward` — **TODO(me)**: gradients in **forward** order
- [ ] `numerical_gradient` — **TODO(me)**: central difference, restores parameters
- [ ] `gradient_check` — **TODO(me)**: relative error, **diagnoses constant ratios**
- [ ] `gradient_magnitudes` — **TODO(me)**: vanishing/exploding, names the mechanism
- [ ] `assert_gradients_checked` — **TODO(me)**
- [ ] Can explain why a wrong gradient produces no error

## Tests that must be able to fail

- [ ] `test_the_sigmoid_derivative_peaks_at_a_quarter` — green
- [ ] `test_the_derivative_docstring_names_the_quarter` — green
- [ ] `test_relu_derivative_is_a_step` — green
- [ ] `test_tanh_derivative_matches_the_identity` — green
- [ ] `test_every_derivative_matches_a_numerical_one` — green
- [ ] `test_an_unknown_derivative_lists_the_known_ones` — green
- [ ] `test_every_gradient_has_its_parameter_shape` — green
- [ ] `test_the_bias_gradient_sums_over_the_batch` — green
- [ ] **Divided the bias gradient twice and watched the scale silently halve** ← do not skip
- [ ] `test_a_mismatched_upstream_gradient_names_both_shapes` — green
- [ ] `test_the_analytic_gradient_matches_the_numerical_one` — green ← **today's real assessment**
- [ ] `test_a_forgotten_activation_derivative_is_caught` — green
- [ ] **Trained with the broken gradient and watched the loss descend anyway** ← do not skip
- [ ] `test_a_constant_factor_error_is_diagnosed` — green
- [ ] `test_the_verdict_says_a_wrong_gradient_still_trains` — green
- [ ] `test_mismatched_parameter_sets_are_named` — green
- [ ] `test_the_numerical_gradient_uses_a_central_difference` — green
- [ ] `test_parameters_are_restored_exactly_after_perturbation` — green
- [ ] `test_an_out_of_range_epsilon_is_refused` — green
- [ ] `test_the_numerical_docstring_says_it_is_for_checking_only` — green
- [ ] `test_the_backward_sweep_returns_gradients_in_forward_order` — green
- [ ] **Returned them reversed and watched the loss still fall** ← do not skip
- [ ] `test_the_backward_docstring_states_the_complexity` — green
- [ ] `test_an_empty_backward_pass_raises` — green
- [ ] `test_sigmoid_gradients_vanish_with_depth` — green
- [ ] `test_relu_with_good_init_does_not_vanish` — green
- [ ] `test_the_vanishing_note_names_the_mechanism_and_the_fix` — green
- [ ] `test_exploding_gradients_are_detected` — green
- [ ] `test_training_without_a_gradient_check_is_refused` — green
- [ ] `test_a_failed_check_is_refused` / `test_a_passed_check_allows_training` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Derive `∂L/∂w` for a one-weight network from first principles
- [ ] What does backpropagation add to the chain rule?
- [ ] Why does every gradient share its parameter's shape?
- [ ] Name four gradient bugs that still produce a descending loss
- [ ] Why does sum-vs-mean change your effective learning rate?
- [ ] Compute `0.25¹²` and say what it means for a 12-layer sigmoid network
- [ ] When is forward-mode autodiff the better choice?
- [ ] Why is backprop not specific to neural networks?

## Commit

- [ ] `./m check && ./m done 127` succeeded
