# Day 92 — CHECKLIST

**IDs covered:** ML-03 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-92/lab/regression.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the ten-part derivation ending with the coefficient's meaning, then all model tests green.

## Setup

- [ ] `./m start 92` and `./m scaffold 92` run
- [ ] Files created: `days/day-92/lab/regression.py`, `src/setu/models.py`, `tests/test_models.py`

## ML-03 — the three ingredients

- [ ] Can name form, loss and minimiser, and what changing each does
- [ ] Ran `why_squared_error()` and read both columns
- [ ] Can say why squared error has a closed form and absolute error does not
- [ ] Can name the cost of that choice

## Deriving it

- [ ] Computed `β₁` and `β₀` **by hand** before touching sklearn
- [ ] Confirmed sklearn agrees to six decimals
- [ ] Confirmed the line passes through (x̄, ȳ)
- [ ] Can say why that identity holds

## The correlation connection

- [ ] Standardised both variables and confirmed `β₁ == r`
- [ ] Can state `β₁ = r × (s_y / s_x)` from memory
- [ ] Can say which Day-62 warnings therefore apply unchanged

## Residuals

- [ ] Confirmed `Σ residual == 0` and `Σ x·residual == 0`
- [ ] Can say **why** both are zero
- [ ] Can state what they are evidence of — and what they are not
- [ ] Used `ddof=2` and can say why

## Predictions

- [ ] Ran `a_prediction_is_not_a_fact()` at three x values
- [ ] Confirmed the interval is **narrowest at x̄**
- [ ] Can say what reporting `ŷ` alone repeats from Day 60
- [ ] Ran `extrapolation_is_a_promise_you_cannot_keep()`
- [ ] Can say what distinguishes an extrapolated prediction in the output (nothing)

## Leverage

- [ ] Ran `outliers_move_the_line()`; recorded the slope change: ______%
- [ ] Compared that point's leverage with a typical one
- [ ] Can state the dangerous **combination**
- [ ] Ran `what_the_coefficient_means()`; can give the honest sentence
- [ ] Can say what centring x does to the intercept's meaning

## Build brief

- [ ] `LinearFit` — records `x_min`, `x_max`, `residual_sd`, `r_squared`
- [ ] `fit_simple_linear` — **TODO(me)**: closed form, `ddof=2`, refuses zero variance
- [ ] `predict` — **TODO(me)**: counts extrapolations **even when warnings are off**
- [ ] `prediction_interval` — **TODO(me)**: uses `t`, widens away from `x̄`
- [ ] `residual_summary` — **TODO(me)**: separates identities from evidence
- [ ] `leverage` — **TODO(me)**: average is exactly 2/n, rule mentions residuals
- [ ] `describe_coefficient` — **TODO(me)**: no causal language, states the range
- [ ] Can explain why the fit records its training range

## Tests that must be able to fail

- [ ] `test_the_closed_form_matches_sklearn` — green
- [ ] `test_it_recovers_the_generating_parameters` — green
- [ ] `test_the_line_passes_through_the_means` — green
- [ ] `test_the_standardised_slope_is_the_correlation` — green
- [ ] `test_a_vertical_line_is_refused` — green
- [ ] `test_too_few_points_is_refused` / `test_a_length_mismatch_names_both` — green
- [ ] `test_missing_pairs_are_dropped` — green
- [ ] `test_the_fit_records_its_training_range` — green
- [ ] `test_extrapolation_is_counted` — green
- [ ] `test_extrapolation_is_counted_even_when_the_warning_is_off` — green
- [ ] **Skipped counting when warnings were off, watched it go red, fixed it** ← do not skip
- [ ] `test_the_warning_says_how_far_beyond` — green
- [ ] `test_predictions_inside_the_range_do_not_warn` — green
- [ ] `test_the_interval_is_narrowest_at_the_mean` — green
- [ ] **Dropped the `(x−x̄)²/Sxx` term, watched only this test go red, restored it** ← do not skip
- [ ] `test_the_interval_uses_t_not_z` — green
- [ ] `test_higher_confidence_is_wider` / `test_the_interval_brackets_the_prediction` — green
- [ ] `test_a_bad_confidence_is_refused` — green
- [ ] `test_the_residual_identities_hold` — green
- [ ] `test_the_identities_hold_for_a_bad_fit_too` — green ← **today's real assessment**
- [ ] `test_the_note_says_the_identities_are_not_evidence` — green
- [ ] `test_average_leverage_is_two_over_n` — green
- [ ] `test_a_far_point_has_high_leverage` — green
- [ ] `test_leverage_does_not_flag_ordinary_points` — green
- [ ] `test_high_leverage_alone_is_not_called_a_problem` — green
- [ ] `test_one_point_can_move_the_slope` — green
- [ ] `test_the_description_avoids_causal_language` — green
- [ ] `test_the_description_states_the_range` — green
- [ ] `test_describe_rejects_an_empty_name` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name the three ingredients of any model
- [ ] Why does squared error give a closed form when absolute error does not?
- [ ] Derive `β₁` and `β₀` from memory
- [ ] Why is the standardised slope equal to `r`?
- [ ] Why do the residuals sum to zero, and what does that prove?
- [ ] Why must a prediction interval widen away from x̄?
- [ ] What makes a single observation dangerous to a fitted line?
- [ ] Give the honest one-sentence reading of a coefficient

## Commit

- [ ] `./m check && ./m done 92` succeeded
