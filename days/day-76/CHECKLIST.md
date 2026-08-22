# Day 76 — CHECKLIST

**IDs covered:** FE-01 · **Principles served:** 1, 7, 8, 9

## Demo command

```bash
uv run python days/day-76/lab/missing.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the seven-part report including the mechanism bias table, then all feature tests green.

## Setup

- [ ] `./m start 76` and `./m scaffold 76` run
- [ ] `uv add "scikit-learn==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-76/lab/missing.py`, `src/setu/features.py`, `tests/test_features.py`

## FE-01 — the three mechanisms

- [ ] Can define MCAR, MAR and MNAR by their **examples**, not their names
- [ ] Ran `the_three_mechanisms()` and **read the bias column**
- [ ] Recorded the bias for each: MCAR ______ MAR ______ MNAR ______
- [ ] Can say why MAR is fixable and MNAR is not

## Testing

- [ ] Ran `you_can_test_for_mcar()` and saw MCAR pass and MAR fail
- [ ] Can state what that test can and **cannot** distinguish
- [ ] Can say why the MAR/MNAR distinction is a provenance judgement (Principle 9)

## What imputation costs

- [ ] Ran `mean_imputation_lies()` and **read all three columns**
- [ ] Recorded sd before ______ and after ______
- [ ] Recorded the correlation before ______ and after ______
- [ ] Can describe the spike mean imputation creates
- [ ] Ran `the_indicator_carries_signal()` on the MNAR case
- [ ] Can say why the indicator is the only honest feature under MNAR

## Strategies

- [ ] Ran `compare_strategies()` on four imputers
- [ ] Recorded which had the lowest RMSE, and can say **why**
- [ ] Can state the limitation shared by every single-value imputation
- [ ] Ran `dropping_is_sometimes_right()`
- [ ] Can say when complete-case analysis is the right call
- [ ] Can compute what `dropna()` costs on 10 columns at 5% missing each

## The leakage rule

- [ ] Ran `the_leakage_rule()` with a genuinely shifted test set
- [ ] Recorded the two resulting means
- [ ] Can name the three earlier days with the same rule
- [ ] Know which day makes it structural

## Build brief

- [ ] `missingness_mechanism_test` — **TODO(me)**: corrects for multiple comparisons, **never claims MNAR**
- [ ] `missingness_impact` — **TODO(me)**: quantifies the sd shrinkage and correlation loss
- [ ] `fit_imputer` — **TODO(me)**: median default, JSON-serialisable spec
- [ ] `apply_imputer` — **TODO(me)**: applies only, indicator before filling, rejects uncovered gaps
- [ ] `imputation_report` — **TODO(me)**: warns above 40% missing
- [ ] Can explain why the verdict vocabulary is constrained

## Tests that must be able to fail

- [ ] `test_mcar_is_recognised_as_plausible` — green
- [ ] `test_mar_is_recognised_as_not_mcar` — green
- [ ] `test_the_verdict_never_claims_mar_or_mnar` — green ← **today's real assessment**
- [ ] **Made the verdict output "MNAR", watched it go red, constrained it** ← do not skip
- [ ] `test_the_mechanism_test_corrects_for_multiple_comparisons` — green
- [ ] `test_mechanism_test_rejects_a_complete_column` — green
- [ ] `test_mean_imputation_shrinks_the_standard_deviation` — green
- [ ] `test_mean_imputation_weakens_correlations` — green
- [ ] `test_impact_does_not_mutate` — green
- [ ] `test_median_is_the_default_strategy` — green
- [ ] `test_the_fitted_spec_is_json_serialisable` — green
- [ ] `test_fit_rejects_an_entirely_missing_column` / `..._unknown_strategy` — green
- [ ] `test_train_values_are_applied_not_refitted` — green
- [ ] `test_apply_never_fits` — green
- [ ] **Recomputed the median inside `apply_imputer`, watched it go red, removed it** ← do not skip
- [ ] `test_the_indicator_is_computed_before_filling` — green
- [ ] **Computed the indicator after filling, saw an all-zero column, fixed the order** ← do not skip
- [ ] `test_the_indicator_can_be_switched_off` — green
- [ ] `test_apply_leaves_no_missing_values` — green
- [ ] `test_apply_rejects_an_uncovered_column_with_gaps` — green
- [ ] `test_apply_rejects_a_missing_spec_column` — green
- [ ] `test_apply_does_not_mutate` — green
- [ ] `test_heavy_missingness_is_warned_about` — green
- [ ] `test_the_report_counts_what_was_filled` — green
- [ ] `test_no_bare_fillna_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give an example of each mechanism, and say what each permits
- [ ] What can you test for, and what can you never test for?
- [ ] What does mean imputation preserve, and what does it destroy?
- [ ] Why is the missingness indicator sometimes the best feature available?
- [ ] What limitation do all single-value imputations share?
- [ ] When is dropping rows the right choice?
- [ ] What goes wrong if the indicator is computed after the fill?
- [ ] Why must the imputer be fitted on train only?

## Commit

- [ ] `./m check && ./m done 76` succeeded
