# Day 109 — CHECKLIST

**IDs covered:** ML-20 · **Principles served:** 1, 7, 8, 10

## Demo command

```bash
uv run python days/day-109/lab/oob.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the nine-part report ending with what importance cannot tell you, then all ensemble tests
green.

## Setup

- [ ] `./m start 109` and `./m scaffold 109` run
- [ ] `days/day-109/lab/oob.py` created
- [ ] No new packages installed

## ML-20 — out-of-bag

- [ ] Ran `oob_is_free_validation()`; recorded OOB ______ vs 5-fold CV ______
- [ ] Can explain what an OOB prediction actually is
- [ ] Know what `oob_score=True` requires, and what happens without it
- [ ] Ran `oob_needs_enough_trees()` and read the coverage column
- [ ] Recorded rows with no OOB prediction at M=5: ______
- [ ] Can write `P(in-bag in all M trees)` and evaluate it at M=10
- [ ] Can say why a partially-covered OOB score is misleading

## The caveat that matters

- [ ] Ran `oob_leaks_on_grouped_data()`
- [ ] Recorded OOB ______ vs GroupKFold ______ — inflation ______ pp
- [ ] Can say **why** the bootstrap leaks on grouped data
- [ ] Can state when OOB is valid, in one sentence
- [ ] Can name the day whose limitations OOB inherits

## Gini importance

- [ ] Ran `gini_importance_is_still_fooled()`
- [ ] Confirmed `many_ids` outranked real signal
- [ ] Can give **both** reasons Gini importance fails
- [ ] Can say why high cardinality helps a column cheat

## Permutation importance

- [ ] Ran `permutation_importance_on_held_out_data()`
- [ ] Confirmed `many_ids` fell to ~0
- [ ] Can say which two problems it fixes at once
- [ ] Can state the question it actually asks

## Where permutation breaks

- [ ] Ran `but_permutation_breaks_on_correlated_features()`
- [ ] Recorded individual importance of `signal_a` ______ and `copy_of_a` ______
- [ ] Recorded the **joint** cost of dropping both: ______
- [ ] Can explain the mechanism in one sentence
- [ ] Can explain the **impossible rows** problem separately

## The fix

- [ ] Ran `group_the_correlated_features()`
- [ ] Confirmed the a-group showed its true joint importance
- [ ] Can say why permuting together avoids impossible rows
- [ ] Can state the rule for correlated features
- [ ] Can name the earlier day that finds the clusters

## What importance is not

- [ ] Ran `importance_is_not_a_property_of_a_feature()` across three models
- [ ] Recorded three different values for the same feature
- [ ] Can state the honest sentence form
- [ ] Read `what_importance_cannot_tell_you()`; can give all five

## Build brief

- [ ] `oob_predictions` — **TODO(me)**: nan for uncovered rows, reports `n_models_used`
- [ ] `oob_score` — **TODO(me)**: coverage stated, docstring names the assumption
- [ ] `assert_oob_is_valid` — **TODO(me)**: message explains **why** rows matter
- [ ] `grouped_permutation_importance` — **TODO(me)**: same permutation per group
- [ ] Reports `ungrouped_columns` rather than dropping them
- [ ] `importance_report` — **TODO(me)**: clusters, unstable list, no causal language
- [ ] `compare_importance_methods` — **TODO(me)**: names the inflated features
- [ ] Can explain why features within noise of zero must not be ranked

## Tests that must be able to fail

- [ ] `test_oob_predictions_use_only_unseen_models` — green
- [ ] `test_rows_without_an_estimate_are_nan_not_dropped` — green
- [ ] **Dropped uncovered rows silently, watched the nan assertion go red** ← do not skip
- [ ] `test_low_coverage_is_warned_about` — green
- [ ] `test_the_oob_score_is_close_to_cross_validation` — green
- [ ] `test_few_models_are_warned_about` — green
- [ ] `test_the_oob_docstring_names_the_exchangeability_assumption` — green
- [ ] `test_grouped_data_makes_oob_invalid` — green
- [ ] `test_time_ordered_data_makes_oob_invalid` — green
- [ ] `test_ordinary_data_passes` — green
- [ ] `test_gini_importance_ranks_a_noise_column_highly` — green
- [ ] `test_permutation_importance_does_not` — green
- [ ] `test_correlated_features_hide_from_individual_permutation` — green ← **today's real assessment**
- [ ] **Permuted each group column separately, watched the joint importance vanish** ← do not skip
- [ ] `test_the_hidden_pair_is_warned_about` — green
- [ ] `test_an_unassigned_column_is_reported_not_dropped` — green
- [ ] `test_a_column_in_two_groups_is_named` — green
- [ ] `test_the_report_finds_the_correlated_cluster` — green
- [ ] `test_features_within_noise_of_zero_are_not_ranked` — green
- [ ] `test_the_statement_makes_no_causal_claim` — green
- [ ] `test_the_comparison_names_the_gini_inflated_features` — green
- [ ] `test_the_comparison_explains_the_disagreement` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is an out-of-bag prediction, and why is it nearly free?
- [ ] When is OOB invalid, and why exactly?
- [ ] Give both flaws in Gini importance
- [ ] What two problems does permutation importance fix?
- [ ] How do correlated features hide from it?
- [ ] What are "impossible rows" and why do they matter?
- [ ] What is the fix, and what does it require you to do first?
- [ ] State the honest sentence form for an importance claim

## Commit

- [ ] `./m check && ./m done 109` succeeded
