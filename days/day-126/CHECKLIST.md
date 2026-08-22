# Day 126 — CHECKLIST

**IDs covered:** DL-03 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-126/lab/forward.py
uv run python -m pytest tests/test_nn.py -v
```

Expected: the eight-part report ending with what the forward pass must keep, then all nn tests green.

## Setup

- [ ] `./m start 126` and `./m scaffold 126` run
- [ ] `days/day-126/lab/forward.py` created
- [ ] No new packages — still NumPy only

## DL-03 — a layer is a matmul

- [ ] Ran `one_layer_is_a_matmul()`
- [ ] Verified one output unit **by hand** against the matmul
- [ ] Can write a layer as an expression from memory
- [ ] Can say why GPUs are relevant to that expression

## Shapes

- [ ] Ran `shapes_are_the_debugging_surface()`
- [ ] Saw the transposed non-square case **raise**
- [ ] Saw the transposed **square** case produce the right shape and wrong numbers
- [ ] Can say why that is the dangerous one
- [ ] Can say what a `(n,1)` bias does

## Why nonlinearities exist

- [ ] Ran `stacking_linear_layers_is_pointless()`
- [ ] Recorded parameters deep ______ vs equivalent single matrix ______
- [ ] Confirmed the outputs matched to machine precision
- [ ] Can state the algebraic reason in one line
- [ ] Can say what the extra parameters are (not "wasted")
- [ ] Confirmed ReLU broke the equivalence

## A full forward pass

- [ ] Ran `a_two_layer_network_forward()` and read the shape table
- [ ] Confirmed each output row summed to 1
- [ ] Can say what `z2 - z2.max(...)` prevents
- [ ] Can name the earlier day with the same instinct

## Batching

- [ ] Ran `batching_is_not_a_loop()`
- [ ] Recorded loop ______ s vs batch ______ s — speedup ______×
- [ ] Can say why BLAS wins
- [ ] Can say what bounds batch size, and which day covers it

## Counting

- [ ] Ran `counting_parameters()` across four architectures
- [ ] Can give the per-layer parameter formula
- [ ] Can say how "wide" and "deep" differ despite similar counts
- [ ] Can name three things the weight-memory figure omits

## Discipline

- [ ] Ran `the_layer_as_a_function()` with assertions
- [ ] Can say where a shape bug surfaces with and without them
- [ ] Read `what_the_forward_pass_must_keep()`
- [ ] Can name **both** things the cache must hold, and what each is for
- [ ] Can say why memory scales with batch size
- [ ] Can say what `torch.no_grad()` will do on Day 135

## Build brief

- [ ] `dense_forward` — **TODO(me)**: returns the cache, refuses a column bias
- [ ] `forward` — **TODO(me)**: names the layer index on a mismatch
- [ ] `softmax` — **TODO(me)**: subtracts the max, docstring explains why
- [ ] `collapse_linear_layers` — **TODO(me)**: **bias composition correct**
- [ ] `assert_shapes` — **TODO(me)**: names the offending layer and both widths
- [ ] `parameter_count` — **TODO(me)**: training estimate, note about activations
- [ ] `batch_speedup` — **TODO(me)**: verifies the results match
- [ ] Can explain why the cache is not optional

## Tests that must be able to fail

- [ ] `test_a_layer_matches_a_hand_computation` — green
- [ ] `test_the_cache_contains_what_backprop_needs` — green
- [ ] `test_the_docstring_says_the_cache_is_not_optional` — green
- [ ] `test_a_shape_mismatch_names_both_shapes` — green
- [ ] `test_a_column_shaped_bias_is_refused` — green
- [ ] **Passed a `(n,1)` bias and watched it broadcast silently** ← do not skip
- [ ] `test_an_unknown_activation_lists_the_known_ones` — green
- [ ] `test_a_network_composes_and_records_its_shapes` — green
- [ ] `test_a_non_composing_network_names_the_layer_index` — green
- [ ] `test_an_empty_network_raises` — green
- [ ] `test_softmax_rows_sum_to_one` — green
- [ ] `test_softmax_survives_large_inputs` — green
- [ ] **Wrote softmax without the max subtraction and watched `nan` appear** ← do not skip
- [ ] `test_softmax_is_shift_invariant` — green
- [ ] `test_the_softmax_docstring_explains_the_trick` — green
- [ ] `test_softmax_rejects_non_finite_input` — green
- [ ] `test_stacked_linear_layers_collapse_to_one` — green ← **today's real assessment**
- [ ] `test_the_collapse_handles_non_zero_biases` — green
- [ ] **Dropped the bias term and watched it pass the zero-bias case only** ← do not skip
- [ ] `test_the_collapse_reports_the_redundant_parameters` — green
- [ ] `test_the_note_calls_them_redundant_not_wasted` — green
- [ ] `test_a_nonlinearity_prevents_the_collapse` — green
- [ ] `test_collapsing_a_nonlinear_network_is_refused` — green
- [ ] `test_shape_checking_catches_a_transposed_square_matrix` — green
- [ ] `test_assert_shapes_names_the_offending_layer` — green
- [ ] `test_assert_shapes_passes_a_valid_architecture` — green
- [ ] `test_parameters_are_counted_per_layer` — green
- [ ] `test_the_training_estimate_exceeds_the_weight_size` — green
- [ ] `test_the_note_says_activations_are_not_included` — green
- [ ] `test_parameter_count_rejects_a_single_layer` — green
- [ ] `test_batching_beats_looping` — green
- [ ] `test_a_speedup_that_changes_the_answer_is_a_bug` — green
- [ ] `test_the_batch_note_mentions_the_memory_bound` — green
- [ ] `test_timing_too_few_rows_is_refused` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Write a layer as an expression and name each shape
- [ ] Why does stacking linear layers achieve nothing?
- [ ] Why is a transposed square matrix worse than a transposed rectangular one?
- [ ] What does subtracting the row max in softmax prevent, and what does it cost?
- [ ] Why is batching faster than looping over rows?
- [ ] What must a forward pass return besides the output, and why?
- [ ] Why does training memory scale with batch size?
- [ ] How do width and depth differ at similar parameter counts?

## Commit

- [ ] `./m check && ./m done 126` succeeded
