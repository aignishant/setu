# Day 98 — CHECKLIST

**IDs covered:** ML-09 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-98/lab/regularise.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the zeros table and the units demonstration, then all model
tests green.

## Setup

- [ ] `./m start 98` and `./m scaffold 98` run
- [ ] `days/day-98/lab/regularise.py` created
- [ ] No new packages installed

## ML-09 — the problem

- [ ] Ran `where_coefficients_go_without_a_penalty()`
- [ ] Recorded fitted coefficient norm ______ vs true ______
- [ ] Recorded train R² ______ vs test R² ______
- [ ] Can name the Day-96 signature this reproduces

## Ridge from scratch

- [ ] Implemented `(XᵀX + αI)⁻¹Xᵀy` by hand and matched sklearn
- [ ] Used `solve`, not `inv`
- [ ] Can say why it is called "ridge"
- [ ] Can say what else the `αI` term fixes (hint: Day 93)

## L1 vs L2 — the mechanism

- [ ] Ran `l1_reaches_zero_and_l2_does_not()` and **read the zeros columns**
- [ ] Confirmed Ridge produced **no** exact zeros at any alpha
- [ ] Can explain the gradient argument for both penalties
- [ ] Can state why everything else about L1 vs L2 follows from it

## Lasso's arbitrary selection

- [ ] Ran `lasso_selects_but_arbitrarily()` across several resamples
- [ ] Confirmed **which** correlated copy survived changed
- [ ] Can say what "Lasso dropped feature 2" actually means
- [ ] Can say what Ridge does with the same three columns
- [ ] Can say what ElasticNet exists for

## Scaling — the third reason

- [ ] Ran `scaling_is_mandatory_for_a_new_reason()`
- [ ] Recorded the penalty share of β₁ in mixed units: ______%
- [ ] Can explain why a 1000× unit change means a 1,000,000× penalty change
- [ ] Can state all **three** distinct reasons to scale, and their days

## The intercept

- [ ] Ran `the_intercept_is_never_penalised()`
- [ ] Recorded the intercept with and without penalty, and `y.mean()`
- [ ] Can say what penalising it drags predictions toward
- [ ] Can say what a from-scratch implementation must do

## Choosing alpha

- [ ] Ran `choosing_alpha()` and confirmed train R² fell **monotonically**
- [ ] Confirmed CV R² peaked in the middle
- [ ] Can explain both halves of that curve using Day 96's vocabulary
- [ ] Can say why the CV score at the chosen alpha is optimistic
- [ ] Read `when_to_use_which()`, including the row about **not** regularising

## Build brief

- [ ] `ridge_closed_form` — **TODO(me)**: intercept excluded, `effective_dof`, uses `solve`
- [ ] `fit_regularised` — **TODO(me)**: scaling guard with a **units-specific** message
- [ ] `regularisation_path` — **TODO(me)**: warns the best score is optimistic
- [ ] `compare_penalties` — **TODO(me)**: reason cites the data, one-standard-error rule
- [ ] `selection_stability` — **TODO(me)**: selection frequency across resamples
- [ ] Can explain why the scaling message must differ from Day 95's

## Tests that must be able to fail

- [ ] `test_the_closed_form_matches_sklearn` — green
- [ ] `test_alpha_zero_is_ordinary_least_squares` — green
- [ ] `test_the_intercept_is_not_shrunk` — green
- [ ] **Included the intercept in the penalty, watched it collapse toward zero** ← do not skip
- [ ] `test_effective_degrees_of_freedom_fall_with_alpha` — green
- [ ] `test_ridge_rejects_a_negative_alpha` — green
- [ ] `test_ridge_never_produces_an_exact_zero` — green
- [ ] `test_lasso_produces_exact_zeros` — green
- [ ] `test_more_alpha_means_fewer_nonzero_for_lasso` — green
- [ ] `test_lasso_keeps_the_informative_features_at_a_sensible_alpha` — green
- [ ] `test_unscaled_features_are_refused_for_a_different_reason` — green
- [ ] **Reused Day 95's message verbatim, watched the units assertion go red** ← do not skip
- [ ] `test_the_scaling_guard_can_be_overridden` — green
- [ ] `test_units_change_which_feature_gets_penalised` — green ← **today's real assessment**
- [ ] `test_correlated_features_trigger_a_lasso_warning` — green
- [ ] `test_ridge_does_not_warn_about_correlation` — green
- [ ] **Made the warning fire for both penalties, watched it go red, narrowed it** ← do not skip
- [ ] `test_an_unknown_penalty_raises` / `test_a_bad_l1_ratio_raises` — green
- [ ] `test_training_score_falls_monotonically_with_alpha` — green
- [ ] `test_the_cv_score_peaks_in_the_middle` — green
- [ ] `test_the_path_warns_that_the_best_score_is_optimistic` — green
- [ ] `test_the_lasso_path_shrinks_the_active_set` — green
- [ ] `test_comparison_gives_a_reason_about_the_data` — green
- [ ] `test_near_ties_prefer_the_simpler_model` — green
- [ ] `test_lasso_selection_is_unstable_among_correlated_features` — green
- [ ] `test_a_genuinely_strong_feature_is_always_selected` — green
- [ ] `test_the_stability_warning_denies_it_is_an_importance_claim` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are you deliberately trading, and against what?
- [ ] Explain via gradients why L1 reaches zero and L2 does not
- [ ] What does a Lasso zero actually tell you about a feature?
- [ ] Why is Lasso's selection unstable among correlated features?
- [ ] Give all three reasons to scale, each with its day
- [ ] Why must the intercept be excluded from the penalty?
- [ ] Why does training R² fall monotonically while CV R² peaks?
- [ ] When should you not regularise at all?

## Commit

- [ ] `./m check && ./m done 98` succeeded
