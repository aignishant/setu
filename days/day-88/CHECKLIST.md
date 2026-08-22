# Day 88 — CHECKLIST

**IDs covered:** EDA-06 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-88/lab/wine.py
uv run python -m pytest tests/test_eda.py -v
```

Expected: the eight-part report ending with the carry-forward inventory, then all eda tests green.

## Setup

- [ ] `./m start 88` and `./m scaffold 88` run
- [ ] `days/day-88/lab/wine.py` created
- [ ] **`SOURCE.md` row added**, including the blind-sensory-assessment collection note
- [ ] Working on the training split only

## EDA-06 — the ordinal question

- [ ] Plotted the quality distribution
- [ ] Can state what a mean of quality assumes
- [ ] Can explain, from the collection process, why the intervals are unequal
- [ ] Can name the Day-58 rule this instantiates

## Three framings

- [ ] Ran `three_framings()`; recorded RMSE ______ accuracy ______ within-one ______
- [ ] Recorded the majority-class baseline for both accuracies
- [ ] Can say what each framing gains and what it costs
- [ ] Can say which one respects order **and** discreteness

## Imbalance

- [ ] Listed the classes under 2% of the data
- [ ] Recorded majority-class accuracy: ______
- [ ] Can say why a well-scoring model may be useless here
- [ ] Can name the day that covers this

## Two datasets

- [ ] Ran `two_datasets_in_one_table()` and read the effect-size column
- [ ] Counted features differing by more than one standard deviation
- [ ] Can state the three options and what each costs
- [ ] Ran `does_the_relationship_survive()` and noted any flagged feature

## Redundancy and domain checks

- [ ] Recorded r between free and total SO₂: ______
- [ ] Can say why they are **mechanically** related, not just correlated
- [ ] Can say why domain knowledge beats PCA here
- [ ] Ran `impossible_values()` and found the cross-column violation type
- [ ] Can say why no per-column audit could find `free ≤ total`

## Build brief

- [ ] `ordinal_target_report` — **TODO(me)**: surfaces `spacing_is_assumed`, names a metric
- [ ] `within_k_accuracy` — **TODO(me)**: baseline always, negative lift visible, k=0 is exact
- [ ] `compare_framings` — **TODO(me)**: each interpretation states its assumption, reuses within_k
- [ ] `subgroup_datasets` — **TODO(me)**: verdict **with options and costs**
- [ ] `cross_column_rules` — **TODO(me)**: example rows, blocking list, names a bad rule
- [ ] Can explain why the spacing assumption is a field rather than a docstring note

## Tests that must be able to fail

- [ ] `test_the_spacing_assumption_is_surfaced` — green ← **today's real assessment**
- [ ] `test_all_three_framings_are_described` — green (each states a cost)
- [ ] **Listed only the advantages of each framing, watched it go red, added the costs** ← do not skip
- [ ] `test_the_recommendation_names_a_metric` — green
- [ ] `test_rare_levels_are_flagged` — green
- [ ] `test_a_continuous_target_is_refused` / `test_too_many_levels_is_refused` — green
- [ ] `test_within_one_is_more_forgiving_than_exact` — green
- [ ] `test_k_zero_is_exact_accuracy` — green
- [ ] `test_the_baseline_is_always_reported` — green
- [ ] `test_a_model_worse_than_the_baseline_is_reported_as_such` — green
- [ ] **Clipped lift at zero, watched the negative case go red, reverted** ← do not skip
- [ ] `test_a_constant_prediction_has_zero_lift` — green
- [ ] `test_within_k_rejects_a_length_mismatch` / `..._negative_k` — green
- [ ] `test_the_three_framings_disagree_on_the_same_predictions` — green
- [ ] `test_each_framing_states_its_spacing_assumption` — green
- [ ] `test_compare_framings_reuses_within_k` — green
- [ ] `test_red_and_white_are_two_datasets` — green
- [ ] `test_a_genuinely_single_dataset_is_not_split` — green
- [ ] **Made the verdict always say "two datasets", watched it go red, fixed it** ← do not skip
- [ ] `test_the_verdict_comes_with_options` — green
- [ ] `test_too_many_groups_is_refused` — green
- [ ] `test_a_cross_column_rule_catches_what_per_column_cannot` — green
- [ ] `test_violations_come_with_example_rows` — green
- [ ] `test_a_widely_violated_rule_is_blocking` — green
- [ ] `test_clean_data_violates_nothing` — green
- [ ] `test_a_malformed_rule_is_named` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is wine quality ordinal rather than numeric, in terms of how it was measured?
- [ ] What does each of the three framings gain and lose?
- [ ] Why must every metric come with a baseline here?
- [ ] Why is a well-scoring model potentially useless on this data?
- [ ] What makes red and white "two datasets stacked"?
- [ ] Why is free/total SO₂ redundancy different from ordinary correlation?
- [ ] Why is domain knowledge a better fix than PCA?
- [ ] Give a cross-column rule and say why no per-column audit finds it

## Commit

- [ ] `./m check && ./m done 88` succeeded
