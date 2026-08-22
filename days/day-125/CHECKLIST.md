# Day 125 — CHECKLIST

**IDs covered:** DL-01, DL-02 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-125/lab/perceptron.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with the phase roadmap, then all nn tests green.

## Setup

- [ ] `./m start 125` and `./m scaffold 125` run
- [ ] Files created: `days/day-125/lab/perceptron.py`, `src/setu/nn.py`, `tests/test_nn.py`
- [ ] **No new packages** — NumPy only until Day 134

## DL-01 — why now

- [ ] Ran `why_deep_learning_now()` and read the timeline
- [ ] Can say what the 1986–2012 gap was waiting on
- [ ] Can name all three, and say which is engineering rather than theory
- [ ] Can state the honest counterweight about tabular data

## DL-02 — the perceptron rule

- [ ] Trained AND by hand; recorded epochs to converge: ______
- [ ] Can write the update rule from memory
- [ ] Can say what happens when a prediction is **correct**
- [ ] Can say why the perceptron stops at a narrow margin

## The guarantee

- [ ] Ran `the_convergence_guarantee()` on AND, OR and XOR
- [ ] Can state Novikoff's theorem in one sentence
- [ ] Can say how it compares to gradient descent's guarantees
- [ ] Recorded what XOR did: ______
- [ ] Can say what happens **without** `max_epochs`

## Why XOR is impossible

- [ ] Ran `why_xor_is_impossible()` and followed all four constraints
- [ ] Can derive the contradiction on paper
- [ ] Can say what kind of statement this is
- [ ] Can give the geometric version in one sentence
- [ ] Can say what it did to the field in 1969

## The fix

- [ ] Ran `one_hidden_layer_solves_it()`
- [ ] Can say what each hidden unit computes
- [ ] **Read the h₀/h₁ column** and found the two coinciding cases
- [ ] Can say what a hidden layer is actually doing, in one sentence
- [ ] Ran `the_step_function_kills_gradients()`
- [ ] Can say what the step derivative is, everywhere
- [ ] Can say why the perceptron rule escapes this, and why that only works for one layer
- [ ] Can say why sigmoid and ReLU exist

## Perspective

- [ ] Ran `a_perceptron_is_almost_logistic_regression()`
- [ ] Can name **both** differences
- [ ] Can say which finds a better margin, and why that matters
- [ ] Read `where_this_phase_is_going()`; can say when the libraries arrive and why then

## Build brief

- [ ] `step` — **TODO(me)**: strictly greater, docstring names the zero gradient
- [ ] `perceptron_predict` — **TODO(me)**: single row and batch alike
- [ ] `train_perceptron` — **TODO(me)**: `errors_per_epoch`, warns it cycles rather than fails
- [ ] `is_linearly_separable` — **TODO(me)**: **decides**, does not train-and-hope
- [ ] `xor_impossibility_proof` — **TODO(me)**: the contradiction as data
- [ ] `hand_built_xor` — **TODO(me)**: returns `hidden_activations`
- [ ] `compare_to_logistic` — **TODO(me)**: names both differences, reports margins
- [ ] Can explain why non-convergence needs its own warning wording

## Tests that must be able to fail

- [ ] `test_step_is_strictly_greater_than_zero` — green
- [ ] `test_the_step_docstring_names_the_zero_gradient` — green
- [ ] `test_prediction_handles_a_single_row_and_a_batch_identically` — green
- [ ] `test_a_shape_mismatch_names_both_shapes` — green
- [ ] `test_the_perceptron_learns_and` / `..._or` — green
- [ ] `test_a_correct_prediction_produces_no_update` — green
- [ ] `test_convergence_is_finite_on_separable_data` — green
- [ ] `test_xor_never_converges` — green ← **today's real assessment**
- [ ] **Ran XOR without `max_epochs` and had to kill the process** ← do not skip
- [ ] `test_the_non_convergence_warning_says_it_does_not_fail` — green
- [ ] `test_the_error_history_shows_the_cycling` — green
- [ ] `test_a_non_binary_target_is_refused` — green
- [ ] `test_zero_epochs_is_refused` — green
- [ ] `test_and_and_or_are_separable` — green
- [ ] `test_xor_is_decided_not_guessed` — green
- [ ] **Used "didn't converge" as the separability answer, watched it go red** ← do not skip
- [ ] `test_the_reason_is_actionable` — green
- [ ] `test_separability_needs_two_classes` — green
- [ ] `test_a_wide_margin_is_reported_as_larger` — green
- [ ] `test_the_proof_derives_a_contradiction` — green
- [ ] `test_the_conclusion_says_no_training_change_helps` — green
- [ ] `test_the_hand_built_network_solves_xor` — green
- [ ] `test_the_two_positive_cases_collapse_to_one_point` — green
- [ ] `test_the_hidden_space_is_linearly_separable` — green
- [ ] `test_the_explanation_names_what_each_unit_computes` — green
- [ ] `test_a_perceptron_finds_a_narrower_margin_than_logistic_regression` — green
- [ ] `test_the_differences_name_both_the_activation_and_the_objective` — green
- [ ] `test_the_note_says_a_larger_margin_generalises_better` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Write the perceptron update rule and say when it does nothing
- [ ] State the convergence guarantee and its condition
- [ ] Derive the XOR contradiction from the four constraints
- [ ] What kind of claim is the XOR result — empirical or proof?
- [ ] What does a hidden layer do, in one sentence?
- [ ] Why can gradient descent not train through a step function?
- [ ] Give both differences between a perceptron and logistic regression
- [ ] What was the 1986–2012 gap waiting on?

## Commit

- [ ] `./m check && ./m done 125` succeeded
