# Day 129 — CHECKLIST

**IDs covered:** DL-06, DL-07 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-129/lab/activations.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with clipping-is-a-seatbelt, then all nn tests green.

## Setup

- [ ] `./m start 129` and `./m scaffold 129` run
- [ ] `days/day-129/lab/activations.py` created
- [ ] No new packages — NumPy plus `math.erf`

## DL-06 — the five functions

- [ ] Ran `five_activations_and_their_derivatives()`
- [ ] Recorded max derivative: sigmoid ______ tanh ______ relu ______ gelu ______
- [ ] Can say why the derivative column, not the value column, decides depth
- [ ] Can say which two activations are bounded and why that matters
- [ ] Computed `0.25¹⁵` by hand

## Saturation — the dead zone

- [ ] Ran `where_the_gradient_goes_to_die()`
- [ ] Recorded where sigmoid falls below 1% of peak: |z| > ______
- [ ] Recorded the share of `[-10,10]` that is saturated: ______%
- [ ] Can explain why tanh saturates sooner in `z` yet is still the better choice
- [ ] Can state the difference between *saturation* and *peak* as failures

## GELU

- [ ] Ran `gelu_is_not_monotonic()`
- [ ] Recorded the minimum value ______ at z = ______
- [ ] Recorded the maximum derivative ______ at z = ______
- [ ] Derived `gelu''(z) = φ(z)(2 − z²)` on paper and solved for `z = √2`
- [ ] Can say why "derivatives are at most 1" is false here

## The dying ReLU

- [ ] Ran `the_dying_relu()`
- [ ] Recorded silent units at rate 0.5: ______ and at rate 200: ______
- [ ] Can name the learning rate as the cause
- [ ] Noticed that leaky_relu's silence counts are **almost identical**
- [ ] Ran `a_dead_unit_is_permanently_dead()`
- [ ] Confirmed the ReLU weights are **bit-identical** after 10,000 steps
- [ ] Recorded leaky_relu's drift over the same run: ______
- [ ] Can say why "dead ReLU" is a named problem and "dead tanh" is not

## Zero-centred outputs

- [ ] Ran `zero_centred_matters()`
- [ ] Recorded sign agreement: sigmoid ______% tanh ______%
- [ ] Can derive why all-positive activations constrain the gradient's sign
- [ ] Can say why this argument is separate from the derivative argument

## DL-07 — vanishing, reproduced then fixed

- [ ] Ran `vanishing_reproduced_then_fixed()`
- [ ] Recorded the sigmoid ratio first/last: ______
- [ ] Recorded sigmoid final loss ______ vs baseline ______
- [ ] Confirmed tanh and relu both reach ~0.0066
- [ ] Can say what changed between the failing and passing rows (**only** the activation)
- [ ] **Removed the baseline column and confirmed 0.2481 looks like a normal loss** ← do not skip

## DL-07 — exploding, and the seatbelt

- [ ] Ran `exploding_and_the_seatbelt()`
- [ ] Recorded the first gradient norm at scale 1.5: ______
- [ ] Recorded steps survived without clipping: ______
- [ ] Recorded the clipped run's final loss: ______
- [ ] Can say why clipping is a seatbelt rather than a fix
- [ ] Can say what Day 132 does that clipping does not

## Build brief

- [ ] `apply_activation` — **TODO(me)**: leaky_relu + gelu, exact Φ
- [ ] `activation_derivative` — **TODO(me)**: extends Day 127, gelu exceeds 1
- [ ] `saturation_range` — **TODO(me)**: `inf` for relu, separates the two failures
- [ ] `dead_units` — **TODO(me)**: reports `recoverable`
- [ ] `clip_gradients` — **TODO(me)**: global norm, raises on NaN
- [ ] `gradient_flow_report` — **TODO(me)**: reuses Day 127, names a **concrete** fix
- [ ] `compare_activations` — **TODO(me)**: refuses a single activation
- [ ] `assert_gradients_flow` — **TODO(me)**
- [ ] Can explain why global-norm clipping preserves direction and per-parameter does not

## Tests that must be able to fail

- [ ] `test_the_sigmoid_peak_is_a_quarter_and_tanh_is_one` — green
- [ ] `test_leaky_relu_passes_alpha_not_zero` — green
- [ ] `test_relu_passes_exactly_zero` — green
- [ ] **Changed leaky's negative slope to 0.0 and watched a unit become unrecoverable** ← do not skip
- [ ] `test_the_gelu_derivative_exceeds_one` — green
- [ ] `test_gelu_is_not_monotonic` — green
- [ ] `test_the_gelu_docstring_warns_about_the_approximation` — green
- [ ] `test_every_new_derivative_matches_a_numerical_one` — green
- [ ] `test_alpha_zero_is_refused_because_that_is_relu` — green
- [ ] `test_sigmoid_saturates_past_about_six` — green
- [ ] `test_tanh_saturates_sooner_than_sigmoid` — green
- [ ] `test_the_saturation_note_separates_the_two_failures` — green
- [ ] `test_relu_has_no_saturation_point` — green
- [ ] `test_a_bad_fraction_is_refused` — green
- [ ] `test_silent_units_are_counted` — green
- [ ] `test_a_unit_that_fires_once_is_not_dead` — green
- [ ] `test_relu_units_are_reported_unrecoverable_and_leaky_ones_are_not` — green
- [ ] `test_the_dead_note_says_leaky_goes_silent_just_as_often` — green
- [ ] `test_clipping_preserves_direction` — green
- [ ] **Clipped per parameter instead of globally and watched the direction change** ← do not skip
- [ ] `test_the_norm_is_global_not_per_parameter` — green
- [ ] `test_a_small_gradient_is_left_alone` — green
- [ ] `test_a_nan_gradient_raises_instead_of_being_clipped` — green
- [ ] `test_the_clip_docstring_calls_itself_a_seatbelt` — green
- [ ] `test_a_deep_sigmoid_network_is_reported_as_vanishing` — green
- [ ] `test_the_fix_names_a_concrete_change` — green
- [ ] `test_the_diagnosis_says_it_looks_like_underfitting` — green
- [ ] `test_a_relu_network_at_the_same_depth_does_not_vanish` — green
- [ ] `test_a_flowing_network_is_allowed_to_train` — green
- [ ] `test_a_vanishing_network_is_refused_with_its_fix` — green
- [ ] `test_only_the_activation_changes_and_only_sigmoid_fails` — green ← **today's real assessment**
- [ ] `test_the_failing_row_sits_at_the_baseline` — green
- [ ] `test_one_activation_is_not_a_comparison` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does the derivative, not the function, decide whether depth works?
- [ ] Compute `0.25¹⁵` and say what it means for a 15-layer sigmoid network
- [ ] Where does sigmoid stop learning, and why does the loss not tell you?
- [ ] Why is a dead ReLU different from a saturated sigmoid?
- [ ] What does leaky ReLU actually fix — silence, or permanence?
- [ ] Why does GELU's derivative exceed 1, and where exactly is its peak?
- [ ] Why does an all-positive activation constrain the weight gradient's sign?
- [ ] Why is gradient clipping not a fix for exploding gradients?

## Commit

- [ ] `./m check && ./m done 129` succeeded
