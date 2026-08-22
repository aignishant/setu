# Day 93 — CHECKLIST

**IDs covered:** ML-04 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-93/lab/multiple.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report ending with the goal-dependent advice, then all model tests green.

## Setup

- [ ] `./m start 93` and `./m scaffold 93` run
- [ ] `days/day-93/lab/multiple.py` created
- [ ] No new packages installed

## ML-04 — the normal equations

- [ ] Solved `β = (XᵀX)⁻¹Xᵀy` with `np.linalg.solve`, **not** `inv`
- [ ] Can say why (Day 24)
- [ ] Confirmed sklearn agrees
- [ ] Can say how Day 92 relates to this

## Holding the others constant

- [ ] Ran `holding_the_others_constant()`; recorded β(pages) alone ______ and with references ______
- [ ] Can give both sentences precisely
- [ ] Recorded r(pages, references): ______
- [ ] Can say why the second sentence describes a rare comparison

## Frisch–Waugh

- [ ] Ran `the_frisch_waugh_view()` and confirmed the two slopes are **identical**
- [ ] Can state what a multiple coefficient measures, precisely
- [ ] Recorded the surviving variation: ______%
- [ ] Can say why that percentage is the coefficient's information budget

## Collinearity

- [ ] Ran `collinearity_breaks_stability()` and **read the range column**
- [ ] Recorded the β₁ spread at r=0.99 (true value 3.0): ______ to ______
- [ ] Can state the VIF formula and its two conventional thresholds
- [ ] Ran `collinearity_does_not_break_prediction()`
- [ ] Confirmed the coefficients were wrong and the test R² was fine
- [ ] Can state what collinearity actually damages
- [ ] Ran `perfect_collinearity_is_different()`
- [ ] Confirmed `solve` raises and **sklearn does not**
- [ ] Can say why silent arbitrary coefficients are the worst outcome

## The assumptions

- [ ] Ran `the_assumptions_ranked()` and read all four
- [ ] Can rank them by severity from memory
- [ ] Can say which is severe and **uncheckable**
- [ ] Can say what Durbin–Watson does and does not detect
- [ ] Can say what heteroscedasticity breaks and what it leaves intact
- [ ] Can name the fix for it
- [ ] Can say which assumption people check most and which matters least

## The fix depends on the goal

- [ ] Read `what_to_do_about_collinearity()`
- [ ] Can give the answer for prediction and for interpretation
- [ ] Can say why "just use PCA" is wrong when interpretation is the goal

## Build brief

- [ ] `MultipleFit` — per-feature ranges, condition number, adjusted R²
- [ ] `fit_multiple` — **TODO(me)**: solves, `ddof = n−p−1`, **refuses perfect collinearity**
- [ ] `vif` — **TODO(me)**: reports infinity rather than crashing, thresholds labelled conventions
- [ ] `partial_coefficient` — **TODO(me)**: Frisch–Waugh, reports the information budget
- [ ] `assumption_check` — **TODO(me)**: **ordered by severity**, independence declared uncheckable
- [ ] `collinearity_advice` — **TODO(me)**: goal-dependent, never recommends PCA for interpretation
- [ ] Can explain why refusing perfect collinearity beats sklearn's behaviour

## Tests that must be able to fail

- [ ] `test_the_normal_equations_match_sklearn` — green
- [ ] `test_it_recovers_the_generating_coefficients` — green
- [ ] `test_the_implementation_does_not_invert` — green
- [ ] `test_residual_sd_accounts_for_every_parameter` — green
- [ ] `test_adjusted_r_squared_is_below_r_squared` — green
- [ ] `test_ranges_are_recorded_per_feature` — green
- [ ] `test_perfect_collinearity_is_refused` — green ← **today's real assessment**
- [ ] `test_sklearn_would_have_accepted_it` — green (the contrast that justifies it)
- [ ] **Let it through with lstsq, watched the refusal test go red, added the rank check** ← do not skip
- [ ] `test_too_few_rows_is_refused` / `test_missing_rows_are_dropped` — green
- [ ] `test_vif_is_near_one_for_independent_predictors` — green
- [ ] `test_vif_rises_with_correlation` — green
- [ ] `test_vif_matches_the_analytic_value` — green
- [ ] `test_perfect_collinearity_reports_infinity_rather_than_crashing` — green
- [ ] `test_the_thresholds_are_labelled_as_conventions` — green
- [ ] `test_vif_needs_two_features` — green
- [ ] `test_the_partial_coefficient_equals_the_full_model` — green
- [ ] `test_the_information_budget_is_reported` — green
- [ ] `test_a_heavily_controlled_coefficient_is_warned_about` — green
- [ ] `test_the_interpretation_says_holding_constant` — green
- [ ] `test_the_assumptions_are_ordered_by_severity` — green
- [ ] **Listed them in textbook order, watched it go red, reordered by severity** ← do not skip
- [ ] `test_independence_is_declared_uncheckable` — green
- [ ] `test_the_note_says_normality_matters_least` — green
- [ ] `test_heteroscedasticity_recommends_robust_errors` — green
- [ ] `test_a_curved_relationship_is_flagged_as_a_linearity_violation` — green
- [ ] `test_prediction_goal_does_not_demand_action` — green
- [ ] `test_interpretation_goal_does_not_recommend_pca` — green
- [ ] `test_pca_may_appear_as_an_alternative_with_its_cost` — green
- [ ] `test_no_concerning_vif_means_no_action` / `test_an_unknown_goal_is_refused` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does a multiple regression coefficient mean, precisely?
- [ ] State the Frisch–Waugh identity and what it tells you
- [ ] What are the three effects of collinearity, and which surprises people?
- [ ] Why does the fix depend on your goal?
- [ ] What does sklearn do with perfectly collinear inputs, and why is that bad?
- [ ] Rank the four assumptions by severity and justify the order
- [ ] Which assumption cannot be checked from the data at all?
- [ ] What is the fix for heteroscedasticity, and what is not?

## Commit

- [ ] `./m check && ./m done 93` succeeded
