# Day 104 — CHECKLIST

**IDs covered:** ML-15 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-104/lab/svm.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the nine-part report including the kernel-equality check and the scaling wall, then all
model tests green.

## Setup

- [ ] `./m start 104` and `./m scaffold 104` run
- [ ] `days/day-104/lab/svm.py` created
- [ ] No new packages installed

## ML-15 — the margin

- [ ] Ran `many_boundaries_one_margin()`; recorded both margin widths
- [ ] Can say what an SVM optimises that logistic regression does not
- [ ] Ran `only_the_support_vectors_matter()`
- [ ] Confirmed refitting on support vectors alone reproduced the model
- [ ] Confirmed moving 200 non-support points changed nothing
- [ ] Can state the risk that follows from so few points mattering

## C

- [ ] Ran `c_is_the_capacity_dial()` and read all five columns
- [ ] Can say what small C and large C each do to margin, support vectors and variance
- [ ] Can state the relationship between C and Day 98's alpha
- [ ] Can say why confusing them is the classic SVM error

## The kernel trick

- [ ] Ran `the_kernel_trick_exactly()` and confirmed the two Gram matrices agree
- [ ] Can say what the SVM's solution depends on the data *through*
- [ ] Recorded the explicit feature count at degree 10 with p=50: ______
- [ ] Ran `rbf_is_infinite_dimensional()`
- [ ] Can say what the RBF kernel corresponds to, and why you could not build it
- [ ] Read the gamma table; can say what large gamma does to the boundary
- [ ] Can say why C and gamma must be tuned together

## Costs

- [ ] Ran `scaling_is_mandatory_again()`; recorded raw vs scaled accuracy **and** timing
- [ ] Can say why Day 103's argument applies unchanged
- [ ] Ran `it_does_not_scale_to_large_n()`; recorded the time ratios
- [ ] Can say what the kernel matrix costs in memory
- [ ] Can name two concrete alternatives above 50,000 rows
- [ ] Ran `svms_do_not_output_probabilities()`; recorded AUC and Brier for both
- [ ] Can say what `decision_function` actually returns
- [ ] Can say why a sigmoid over it is not calibration
- [ ] Read `when_to_reach_for_an_svm()`; can say why SVMs lost ground after 2012

## Build brief

- [ ] `kernel_matrix` — **TODO(me)**: three kernels, expansion form, clipped before exp
- [ ] `verify_kernel_trick` — **TODO(me)**: demonstrates rather than asserts
- [ ] `fit_svm` — **TODO(me)**: delegates to Day 103's guard, warns at both support extremes
- [ ] `svm_scores` — **TODO(me)**: `is_probability: False`, note names the distance
- [ ] `tune_c_and_gamma` — **TODO(me)**: joint grid, edge-optimum warning
- [ ] `svm_capacity_note` — **TODO(me)**: the C-versus-alpha sentence
- [ ] Can explain why `margin` is `None` for a nonlinear kernel

## Tests that must be able to fail

- [ ] `test_the_linear_kernel_is_the_dot_product` — green
- [ ] `test_the_rbf_kernel_is_one_on_the_diagonal` — green
- [ ] `test_the_rbf_kernel_is_symmetric_and_bounded` — green
- [ ] `test_the_rbf_distance_survives_floating_point` — green
- [ ] **Skipped the clip, watched a tiny negative distance break exp** ← do not skip
- [ ] `test_kernel_matrix_matches_sklearn` — green
- [ ] `test_an_unknown_kernel_lists_the_known_ones` / `..._feature_mismatch` — green
- [ ] `test_the_kernel_equals_the_explicit_expansion` — green ← **today's real assessment**
- [ ] `test_the_explicit_expansion_is_much_larger_than_the_input` — green
- [ ] `test_the_kernel_avoids_a_space_you_could_not_build` — green
- [ ] `test_only_support_vectors_determine_the_boundary` — green
- [ ] `test_refitting_on_support_vectors_alone_reproduces_the_model` — green
- [ ] `test_the_svm_margin_is_wider_than_logistic_regressions` — green
- [ ] `test_a_small_c_widens_the_margin_and_adds_support_vectors` — green
- [ ] `test_c_is_inverted_relative_to_alpha` — green
- [ ] `test_the_margin_is_none_for_a_nonlinear_kernel` — green
- [ ] **Returned a plausible-looking margin for RBF, watched it go red** ← do not skip
- [ ] `test_rbf_separates_what_linear_cannot` — green
- [ ] `test_a_large_gamma_memorises` — green
- [ ] `test_unscaled_features_are_refused_via_day_103s_guard` — green
- [ ] **Reimplemented the scaling check, watched the monkeypatch test go red** ← do not skip
- [ ] `test_scaled_data_passes` — green
- [ ] `test_too_many_rows_is_refused` — green
- [ ] `test_a_high_support_fraction_warns_about_memorisation` — green
- [ ] `test_a_tiny_support_fraction_warns_about_fragility` — green
- [ ] `test_a_non_positive_c_raises` — green
- [ ] `test_scores_are_labelled_as_distances` — green
- [ ] `test_a_sigmoid_of_the_margin_is_not_calibrated` — green
- [ ] `test_c_and_gamma_are_searched_jointly` — green
- [ ] `test_an_edge_optimum_warns_that_the_grid_is_too_narrow` — green
- [ ] `test_tuning_warns_the_best_score_is_optimistic` — green
- [ ] `test_an_empty_grid_raises` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does an SVM optimise, and how does that differ from logistic regression?
- [ ] What are support vectors, and what follows from only they mattering?
- [ ] Which direction does C go, and how does it relate to alpha?
- [ ] Explain the kernel trick — what does the solution depend on the data through?
- [ ] What feature space does the RBF kernel correspond to?
- [ ] What does large gamma do, and what is that in Day 96's vocabulary?
- [ ] Why does an SVM not scale to large n?
- [ ] What does `decision_function` return, and why is a sigmoid of it not a probability?

## Commit

- [ ] `./m check && ./m done 104` succeeded
