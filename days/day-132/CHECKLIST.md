# Day 132 — CHECKLIST

**IDs covered:** DL-10 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-132/lab/initialisation.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with the output-bias table, then all nn tests green.

## Setup

- [ ] `./m start 132` and `./m scaffold 132` run
- [ ] `days/day-132/lab/initialisation.py` created
- [ ] No new packages — NumPy only

## The recursion

- [ ] Ran `the_recursion()`
- [ ] **Derived `Var(z) = n_in · Var(w) · Var(x)` on paper**
- [ ] Can say what `k` is and why `k = 1` is the only safe value
- [ ] Recorded the mean over 200 draws ______ vs predicted ______
- [ ] Recorded the single-draw range ______ to ______
- [ ] Can say what "exact in expectation" does **not** guarantee

## Variance with depth

- [ ] Ran `variance_through_twenty_layers()`
- [ ] Recorded layer-20 variance: σ=0.01 ______ σ=1.0 ______ He ______
- [ ] Can say why the failure is not gradual
- [ ] Computed `k^20` by hand for one of the failing rows

## DL-10 — the factor of two

- [ ] Ran `why_relu_needs_a_factor_of_two()`
- [ ] Recorded the **variance** ratio ______ and the **second moment** ratio ______
- [ ] Can say why they differ (nonzero mean after ReLU)
- [ ] Can say which one He's derivation uses
- [ ] **Can explain why quoting 0.342 is wrong even though the conclusion is right**

## Xavier vs He

- [ ] Ran `xavier_is_for_tanh_he_is_for_relu()`
- [ ] Recorded Xavier + relu at layer 20 ______ and Xavier + tanh ______
- [ ] Can say why they are the same derivation, not two brands
- [ ] Ran `xaviers_two_forms()`
- [ ] Confirmed the uniform limit `√(6/(n+m))` has std equal to `√(2/(n+m))`
- [ ] Can say why the constant is 6 and not 2

## Gradients backwards

- [ ] Ran `the_gradient_goes_backwards_too()`
- [ ] Recorded the He ratio ______ and the σ=0.01 ratio ______
- [ ] Can state the backward recursion
- [ ] Can say why forward and backward cannot both be satisfied when fans differ

## The payoff

- [ ] Ran `does_it_actually_train()`
- [ ] Recorded final loss: zeros ______ σ=0.01 ______ σ=1.0 ______ Xavier ______ He ______
- [ ] Can name the **three distinct failure modes** in that table
- [ ] Can say why zeros and σ=0.01 fail for unrelated reasons
- [ ] **Ran σ=1.0 and confirmed it is worse than the baseline** ← do not skip

## Biases

- [ ] Ran `what_the_bias_gets()`
- [ ] Can say why biases start at zero without a symmetry problem
- [ ] Recorded `log(p/(1−p))` for a 1% base rate: ______
- [ ] Can connect the output-bias trick to Day 130's saturated start

## Build brief

- [ ] `initialiser_scale` — **TODO(me)**: shows the `a²/3 = Var(w)` identity
- [ ] `initialise_network` — **TODO(me)**: retires Day 128's `scale` argument
- [ ] `variance_by_depth` — **TODO(me)**: note names a scheme, not a topic
- [ ] `relu_second_moment_ratio` — **TODO(me)**: returns **both** ratios
- [ ] `output_bias_for_base_rate` — **TODO(me)**
- [ ] `compare_initialisations` — **TODO(me)**: distinguishes symmetry from scale
- [ ] `assert_initialisation_is_sane` — **TODO(me)**
- [ ] Can explain why defaulting the scheme from the activation is the point

## Tests that must be able to fail

- [ ] `test_he_is_exactly_twice_xavier_in_variance_at_equal_fans` — green
- [ ] `test_he_uses_fan_in_and_xavier_uses_the_average` — green
- [ ] `test_he_normal_matches_the_derivation` — green
- [ ] `test_the_uniform_limit_has_the_same_variance_as_the_normal_form` — green
- [ ] `test_lecun_is_one_over_fan_in` — green
- [ ] `test_an_unknown_scheme_lists_the_known_ones` — green
- [ ] `test_a_zero_fan_is_refused` — green
- [ ] `test_relu_halves_the_second_moment_not_the_variance` — green
- [ ] **Swapped the second-moment ratio for the variance ratio and watched it go red** ← do not skip
- [ ] `test_the_ratio_note_explains_why_they_differ` — green
- [ ] `test_every_activation_has_a_default_initialiser` — green
- [ ] `test_relu_defaults_to_he_and_tanh_to_xavier` — green
- [ ] `test_he_holds_the_variance_across_twenty_layers` — green
- [ ] `test_a_tiny_initialisation_collapses` — green
- [ ] `test_xavier_with_relu_loses_orders_of_magnitude` — green
- [ ] `test_xavier_with_tanh_is_fine` — green
- [ ] `test_the_variance_verdict_names_a_scheme_not_a_topic` — green
- [ ] `test_a_collapsed_profile_is_refused_before_training` — green
- [ ] `test_a_stable_profile_passes` — green
- [ ] `test_the_output_bias_starts_at_the_base_rate` — green
- [ ] `test_a_single_class_dataset_is_refused` — green
- [ ] `test_the_bias_docstring_connects_to_the_loss` — green
- [ ] `test_he_beats_xavier_and_both_beat_the_baseline` — green ← **today's real assessment**
- [ ] `test_symmetry_and_scale_failures_are_distinguished` — green
- [ ] **Reported both failures as "scale" and watched this go red** ← do not skip
- [ ] `test_one_scheme_is_not_a_comparison` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Derive the variance recursion from scratch
- [ ] Why is there exactly one safe value of `n_in · Var(w)`?
- [ ] Where does He's factor of two come from — and which moment is it about?
- [ ] Why is the variance ratio of ReLU not 0.5?
- [ ] Why does Xavier fail with ReLU but not with tanh?
- [ ] Why can forward and backward not both be satisfied?
- [ ] What are the three distinct failure modes in the training table?
- [ ] What does `log(p/(1−p))` as an output bias buy you?

## Commit

- [ ] `./m check && ./m done 132` succeeded
