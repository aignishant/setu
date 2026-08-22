# Day 107 — CHECKLIST

**IDs covered:** ML-18 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-107/lab/averaging.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the eight-part report ending with when not to ensemble, then all ensemble tests green.

## Setup

- [ ] `./m start 107` and `./m scaffold 107` run
- [ ] Files created: `days/day-107/lab/averaging.py`, `src/setu/ensembles.py`,
      `tests/test_ensembles.py`
- [ ] No new packages installed

## ML-18 — the formula

- [ ] Wrote `Var(avg) = ρσ² + (1−ρ)σ²/M` from memory
- [ ] Ran `the_variance_formula()` and **read the last column**
- [ ] Can say what `ρσ²` is and why no number of models beats it
- [ ] Can say what happens at ρ = 1
- [ ] Confirmed the simulated variance matched the prediction

## Correlation

- [ ] Ran `correlation_is_the_whole_game()`
- [ ] Recorded observed variance at ρ = 0 ______ and ρ = 0.9 ______
- [ ] Can name four ways ensembles lower ρ
- [ ] Can say what Random Forest's feature subsampling is for

## Bias vs variance

- [ ] Ran `averaging_fixes_variance_not_bias()` and **read each pair of rows**
- [ ] Confirmed bagging collapsed variance and left bias untouched
- [ ] Can say why bagging a stump is nearly pointless
- [ ] Can state the rule for which base models to bag
- [ ] Can say what boosting attacks instead

## Diminishing returns

- [ ] Ran `diminishing_returns()` from M=1 to M=200
- [ ] Can say roughly where the curve flattens
- [ ] Can say whether more estimators can *hurt* in bagging
- [ ] Can say how boosting differs on that point

## Voting

- [ ] Ran `averaging_probabilities_beats_voting()`
- [ ] Recorded hard ______ vs soft ______ accuracy
- [ ] Can say what hard voting throws away
- [ ] Can name what soft voting assumes, and the day that covers it

## Condorcet

- [ ] Ran `condorcet_needs_independence()` at both correlations
- [ ] Can say why correlated voters stall
- [ ] Recorded what happens with 45%-accurate models at M=51: ______
- [ ] Can state the precondition every base model must meet

## Diversity

- [ ] Ran `diversity_beats_individual_quality()`
- [ ] Recorded ρ for identical ______ and bootstrapped ______ trees
- [ ] Confirmed the individually-worse ensemble averaged better
- [ ] Can state the counter-intuitive rule in one sentence
- [ ] Read `when_not_to_ensemble()`; can give all five conditions

## Build brief

- [ ] `averaged_variance` — **TODO(me)**: reports the floor and what remains reducible
- [ ] `models_needed` — **TODO(me)**: can answer **unreachable**
- [ ] `prediction_correlation` — **TODO(me)**: reports `effective_models`
- [ ] `ensemble_gain` — **TODO(me)**: measured against the **best** member
- [ ] `choose_ensemble_strategy` — **TODO(me)**: reason names the error term
- [ ] `soft_vote` — **TODO(me)**: reports agreement, states the calibration assumption
- [ ] Can explain why gain is measured against the best rather than the mean

## Tests that must be able to fail

- [ ] `test_independent_models_divide_the_variance` — green
- [ ] `test_identical_models_gain_nothing` — green
- [ ] `test_the_floor_is_never_crossed` — green
- [ ] `test_reducible_variance_shrinks_with_more_models` — green
- [ ] `test_the_formula_matches_a_simulation` — green
- [ ] `test_an_impossible_correlation_is_refused` — green
- [ ] `test_a_reachable_target_gives_a_count` — green
- [ ] `test_a_target_below_the_floor_is_unreachable` — green ← **today's real assessment**
- [ ] **Made it return a huge n instead of `reachable: False`, watched it go red** ← do not skip
- [ ] `test_a_target_exactly_at_the_floor_is_unreachable` — green
- [ ] `test_models_needed_rejects_a_non_positive_target` — green
- [ ] `test_identical_predictions_are_flagged` — green
- [ ] `test_diverse_predictions_are_not_flagged` — green
- [ ] `test_effective_models_is_below_the_actual_count_when_correlated` — green
- [ ] `test_effective_models_approaches_the_count_when_independent` — green
- [ ] `test_a_constant_column_is_named` / `..._at_least_two_models` — green
- [ ] `test_gain_is_measured_against_the_best_single_model` — green
- [ ] **Reported only `gain_over_mean`, watched a losing ensemble look successful** ← do not skip
- [ ] `test_a_marginal_gain_is_warned_about` — green
- [ ] `test_a_worthwhile_gain_is_not_warned_about` — green
- [ ] `test_a_member_worse_than_baseline_is_flagged_for_removal` — green
- [ ] `test_ensemble_gain_rejects_an_empty_list` — green
- [ ] `test_variance_dominated_error_gets_bagging_with_deep_models` — green
- [ ] `test_bias_dominated_error_gets_boosting_with_shallow_models` — green
- [ ] `test_noise_dominated_error_gets_no_ensemble` — green
- [ ] `test_the_reason_names_which_error_term_it_attacks` — green
- [ ] `test_an_explanation_requirement_is_warned_about` — green
- [ ] `test_a_tight_latency_budget_is_warned_about` — green
- [ ] `test_an_unknown_error_term_raises` — green
- [ ] `test_soft_voting_keeps_the_confidence_hard_voting_discards` — green
- [ ] `test_soft_voting_reports_agreement` — green
- [ ] `test_weights_must_sum_to_one` — green
- [ ] `test_soft_vote_rejects_probabilities_outside_the_unit_interval` — green
- [ ] `test_the_docstring_names_the_calibration_assumption` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Write the variance formula and explain each term
- [ ] What is the floor, and what is the only way to lower it?
- [ ] Why does bagging a stump achieve almost nothing?
- [ ] Which base models should you bag, and which should you boost?
- [ ] Why does soft voting usually beat hard voting, and what does it assume?
- [ ] When does Condorcet's theorem run in reverse?
- [ ] Why can a *worse* model improve an ensemble?
- [ ] Name three situations where you should not ensemble at all

## Commit

- [ ] `./m check && ./m done 107` succeeded
