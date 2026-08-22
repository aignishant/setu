# Day 128 — CHECKLIST

**IDs covered:** DL-05 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-128/lab/training_loop.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with the leakage comparison, then all nn tests green.

## Setup

- [ ] `./m start 128` and `./m scaffold 128` run
- [ ] `days/day-128/lab/training_loop.py` created
- [ ] No new packages — still NumPy only

## The loop itself

- [ ] Ran `the_loop_is_four_lines()`
- [ ] Can name the four lines in order, without looking
- [ ] Can name one fact each framework convenience hides
- [ ] Wrote the loop once without copying it

## DL-05 — learning XOR

- [ ] Ran `learning_xor_at_last()`
- [ ] Recorded the epoch count spent above 0.2499: ______
- [ ] Recorded the first epoch below 0.24: ______
- [ ] Can say what a plateau is and why it is indistinguishable from failure
- [ ] **Re-ran with `epochs=2000` and watched it "fail"** ← do not skip

## One run is not a result

- [ ] Ran `the_same_code_twenty_times()`
- [ ] Recorded 2-2-1 success count: ______ / 20
- [ ] Recorded 2-4-1 success count: ______ / 20
- [ ] Can explain why `0.125` is exactly the loss of a two-row failure
- [ ] Can say why 4 hidden units help when 2 are provably enough

## The headline

- [ ] Ran `a_descending_loss_proves_nothing()`
- [ ] Confirmed the curve is monotonically decreasing
- [ ] Recorded final loss ______ vs baseline ______
- [ ] Can say why a loss curve without a baseline is unreadable
- [ ] Committed to printing the baseline on every run from here on

## Symmetry

- [ ] Ran `symmetry_never_breaks_itself()`
- [ ] Confirmed all hidden units stayed identical
- [ ] Can say why the zero case sits at exactly 0.250000
- [ ] Can say why biases may start at zero when weights may not
- [ ] Can say what Day 132 adds to this

## The silent bug

- [ ] Ran `updating_inside_the_backward_pass()`
- [ ] Recorded the ratio at lr=0.5 ______ and at lr=50 ______
- [ ] Can say why yesterday's gradient check does **not** catch it
- [ ] Can say why a non-mutating update makes the bug unwriteable

## Two curves, and the leak

- [ ] Ran `two_curves_not_one()`
- [ ] Recorded the best validation epoch: ______
- [ ] Confirmed train fell while validation rose
- [ ] Can say why early stopping on the **test** set spends it
- [ ] Ran `where_the_leak_hides()`
- [ ] Recorded the optimism the leak buys: ______%
- [ ] **Named where the leak would have been, in one sentence** ← Principle 8

## Build brief

- [ ] `TrainResult` — **TODO(me)**: frozen, carries its baseline
- [ ] `initialise_network` — **TODO(me)**: refuses `scale <= 0`, seed required
- [ ] `epoch_batches` — **TODO(me)**: covers every row once, keeps the last batch
- [ ] `sgd_update` — **TODO(me)**: returns new layers, does **not** mutate
- [ ] `baseline_loss` — **TODO(me)**
- [ ] `train` — **TODO(me)**: all gradients before any update; validation never updates
- [ ] `diagnose_training` — **TODO(me)**: every verdict names an action
- [ ] `seed_stability` — **TODO(me)**: refuses fewer than 3 seeds
- [ ] `assert_beats_baseline` — **TODO(me)**
- [ ] Can explain why `sgd_update` is pure rather than in-place

## Tests that must be able to fail

- [ ] `test_a_constant_initialisation_is_refused` — green
- [ ] `test_biases_start_at_zero` — green
- [ ] `test_the_same_seed_gives_the_same_network` — green
- [ ] `test_different_seeds_give_different_networks` — green
- [ ] `test_the_init_docstring_points_at_the_scale_question` — green
- [ ] `test_batches_cover_every_row_exactly_once` — green
- [ ] `test_the_last_batch_is_kept_not_dropped` — green
- [ ] **Dropped the last batch and watched the loss look completely normal** ← do not skip
- [ ] `test_the_batch_docstring_names_the_sorted_data_problem` — green
- [ ] `test_shuffling_changes_the_order_but_not_the_contents` — green
- [ ] `test_a_zero_batch_size_is_refused` — green
- [ ] `test_the_update_does_not_mutate_its_input` — green
- [ ] **Made `sgd_update` mutate in place and watched this go red** ← do not skip
- [ ] `test_the_update_moves_against_the_gradient` — green
- [ ] `test_the_update_docstring_explains_why_it_is_pure` — green
- [ ] `test_a_gradient_count_mismatch_names_both` — green
- [ ] `test_the_baseline_is_the_mean_for_mse` — green
- [ ] `test_the_xor_baseline_is_a_quarter` — green
- [ ] `test_the_baseline_docstring_says_a_curve_needs_it` — green
- [ ] `test_the_network_learns_xor` — green
- [ ] `test_training_is_reproducible_from_the_seed_alone` — green
- [ ] `test_the_result_carries_its_baseline` — green
- [ ] `test_the_validation_pass_does_not_update_the_parameters` — green
- [ ] **Updated on the validation pass and watched the training loss improve** ← do not skip
- [ ] `test_early_stopping_without_a_validation_split_is_refused` — green
- [ ] `test_early_stopping_stops_before_the_epoch_cap` — green
- [ ] `test_a_row_count_mismatch_names_both` — green
- [ ] `test_a_tiny_learning_rate_descends_and_still_learns_nothing` — green ← **today's real assessment**
- [ ] `test_a_run_that_never_beats_the_baseline_is_refused` — green
- [ ] `test_a_real_run_passes_the_baseline_guard` — green
- [ ] `test_a_plateau_is_diagnosed_as_train_longer` — green
- [ ] `test_the_plateau_diagnosis_admits_it_cannot_tell` — green
- [ ] `test_overfitting_is_detected_from_two_curves` — green
- [ ] `test_every_diagnosis_names_an_action` — green
- [ ] `test_the_same_configuration_does_not_always_converge` — green
- [ ] `test_a_wider_layer_converges_from_every_seed` — green
- [ ] `test_the_stability_note_says_one_run_reports_the_seed` — green
- [ ] `test_two_seeds_are_not_a_spread` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name the four lines of a training loop, in order
- [ ] Why is a monotonically decreasing loss curve not evidence of learning?
- [ ] Why is a flat loss curve not evidence of failure?
- [ ] What does a single successful run actually tell you?
- [ ] Why does a constant initialisation give a 4-unit layer the capacity of 1?
- [ ] Why does the gradient check miss the update-order bug?
- [ ] What happens to your test score if you early-stop on it?
- [ ] Where would the leak have been today, in one sentence?

## Commit

- [ ] `./m check && ./m done 128` succeeded
