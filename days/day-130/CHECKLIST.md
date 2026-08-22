# Day 130 — CHECKLIST

**IDs covered:** DL-08 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-130/lab/losses.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with the baseline table, then all nn tests green.

## Setup

- [ ] `./m start 130` and `./m scaffold 130` run
- [ ] `days/day-130/lab/losses.py` created
- [ ] No new packages — NumPy only

## The two families

- [ ] Ran `the_two_families()`
- [ ] Can name the head each loss belongs to, without looking
- [ ] Can say what MSE estimates and what MAE estimates
- [ ] Can say what breaks with a linear head and cross-entropy

## MSE vs MAE

- [ ] Ran `mse_finds_the_mean_mae_finds_the_median()`
- [ ] Recorded argmin MSE ______ and argmin MAE ______ on the outlier data
- [ ] Can say why "robust to outliers" is a **consequence**, not the definition
- [ ] Can state how each gradient scales with the error
- [ ] Can say why MAE's gradient is a problem at exactly 0

## DL-08 — why cross-entropy

- [ ] Ran `why_cross_entropy_for_classification()`
- [ ] Recorded MSE ∂L/∂z at z = −10: ______
- [ ] Recorded BCE ∂L/∂z at z = −10: ______
- [ ] Recorded the ratio: ______
- [ ] Can say why MSE's gradient peaking at z = 0 is backwards

## The cancellation

- [ ] Ran `the_sigma_prime_cancels()`
- [ ] **Derived `∂L/∂z = a − y` on paper** — all four lines
- [ ] Can point at where `σ'(z)` appears and where it divides out
- [ ] Recorded max |numeric − (a − y)|: ______
- [ ] Can say why this means you never compute `σ'(z)` at a cross-entropy head

## The saturation cliff

- [ ] Ran `the_saturation_cliff()`
- [ ] Recorded MSE halve@ at bias −8: ______ and at −12: ______
- [ ] Recorded BCE halve@ across every row: ______ to ______
- [ ] Recorded MSE's accuracy at −12: ______
- [ ] Can state the claim **precisely** (escape time vs saturation), not as "MSE never works"
- [ ] **Ran bias −8 and watched MSE get there anyway, slowly** ← do not skip

## Numerical stability

- [ ] Ran `log_sigmoid_three_ways()`
- [ ] Recorded naive at z = −800: ______
- [ ] Recorded clipped at z = −800: ______ and at −1000: ______
- [ ] Can say why the clipped column is more dangerous than the naive one
- [ ] Can write `log σ(z)` as a `logaddexp` expression from memory
- [ ] Can say what `from_logits=True` actually buys

## Multi-class

- [ ] Ran `softmax_and_categorical_cross_entropy()`
- [ ] Recorded max |numeric − (p − y)/n|: ______
- [ ] Can say why only the true class's probability appears in the loss
- [ ] Can say what the other classes contribute through
- [ ] Can describe the double-softmax bug and why nothing raises

## Baselines

- [ ] Ran `every_loss_needs_its_own_baseline()`
- [ ] Confirmed the BCE baseline equals `H(p)` exactly
- [ ] Can say why (KL divergence)
- [ ] Recorded the MAE baseline from the median ______ vs from the mean ______
- [ ] Recorded the always-predict-0 accuracy on the imbalanced set: ______
- [ ] Can say why an MSE value and a BCE value cannot be compared

## Build brief

- [ ] `loss_and_gradient` — **TODO(me)**: returns `wrt`, cancelled form for logits
- [ ] `bce_with_logits` — **TODO(me)**: exact at |z| = 800, `pos_weight`
- [ ] `categorical_cross_entropy` — **TODO(me)**: refuses a non-distribution row
- [ ] `baseline_loss` — **TODO(me)**: extends Day 128 to all four losses
- [ ] `assert_head_matches_loss` — **TODO(me)**: message names the real reason
- [ ] `class_weights` — **TODO(me)**: note says the loss is no longer comparable
- [ ] `compare_losses` — **TODO(me)**: `None` for "never halved"
- [ ] `assert_loss_is_finite` — **TODO(me)**: names both causes
- [ ] Can explain why `wrt` prevents a real bug

## Tests that must be able to fail

- [ ] `test_mse_is_minimised_by_the_mean` — green
- [ ] `test_mae_is_minimised_by_the_median` — green
- [ ] `test_the_mse_gradient_grows_with_the_error_and_mae_does_not` — green
- [ ] `test_the_mae_gradient_at_zero_is_zero_and_documented` — green
- [ ] `test_the_bce_gradient_is_exactly_prediction_minus_target` — green
- [ ] `test_the_gradient_is_worst_exactly_when_the_model_is_confidently_wrong` — green
- [ ] `test_the_logit_gradient_is_reported_as_logit_space` — green
- [ ] **Multiplied a logit-space gradient by σ'(z) and watched training slow to a crawl** ← do not skip
- [ ] `test_bce_with_logits_is_exact_at_extreme_magnitudes` — green
- [ ] `test_the_clipped_form_would_have_been_wrong` — green
- [ ] **Replaced the fused form with clip-then-log and watched this go red** ← do not skip
- [ ] `test_the_fused_docstring_records_the_silent_failure` — green
- [ ] `test_a_non_finite_logit_raises` — green
- [ ] `test_pos_weight_scales_only_the_positive_term` — green
- [ ] `test_the_categorical_gradient_is_probabilities_minus_target` — green
- [ ] `test_a_target_row_that_is_not_a_distribution_is_refused` — green
- [ ] `test_the_categorical_docstring_warns_about_double_softmax` — green
- [ ] `test_the_bce_baseline_is_the_entropy` — green
- [ ] `test_the_mae_baseline_uses_the_median_not_the_mean` — green
- [ ] `test_the_mse_baseline_is_the_variance` — green
- [ ] `test_the_baseline_docstring_explains_the_entropy_equality` — green
- [ ] `test_a_sigmoid_head_with_mse_is_refused_with_the_reason` — green
- [ ] `test_an_identity_head_with_bce_is_refused` — green
- [ ] `test_every_intended_pairing_is_allowed` — green
- [ ] `test_every_loss_has_a_head` — green
- [ ] `test_balanced_weights_equalise_the_classes` — green
- [ ] `test_the_weight_note_says_the_loss_is_no_longer_comparable` — green
- [ ] `test_a_missing_class_is_named` — green
- [ ] `test_bce_escapes_a_saturated_start_and_mse_does_not` — green ← **today's real assessment**
- [ ] `test_mse_is_slower_not_broken_at_a_mild_start` — green ← **the honesty test**
- [ ] `test_one_loss_is_not_a_comparison` — green
- [ ] `test_a_nan_loss_is_refused_with_its_two_causes` — green
- [ ] `test_a_finite_loss_passes` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Derive `∂L/∂z = a − y` for sigmoid + BCE from first principles
- [ ] Where exactly does `σ'(z)` cancel, and what is it in terms of `a`?
- [ ] Why is MSE's gradient largest at `z = 0` and why is that backwards?
- [ ] State today's claim about MSE precisely enough that it is not an overclaim
- [ ] Why is clipping the sigmoid more dangerous than letting it return `-inf`?
- [ ] Why does the BCE baseline equal the entropy of the labels?
- [ ] Why does MAE's baseline use the median?
- [ ] Why can you not compare an MSE value to a BCE value?

## Commit

- [ ] `./m check && ./m done 130` succeeded
