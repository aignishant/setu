# Day 105 — CHECKLIST

**IDs covered:** ML-16 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-105/lab/trees.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the nine-part report ending with what trees cannot do, then all model tests green.

## Setup

- [ ] `./m start 105` and `./m scaffold 105` run
- [ ] `days/day-105/lab/trees.py` created
- [ ] No new packages installed

## ML-16 — impurity

- [ ] Ran `impurity_measures()` and compared Gini with entropy
- [ ] Confirmed impurity is **zero** for a pure node and maximal at an even split
- [ ] Can say what `0·log 0` is, and why the implementation must handle it
- [ ] Can say when the choice between Gini and entropy actually matters

## Choosing a split

- [ ] Ran `choosing_a_split_by_hand()` and matched sklearn's root split
- [ ] Can explain why the gain is **weighted by child size**
- [ ] Can say what happens when no valid split exists

## What trees give you free

- [ ] Ran `no_scaling_required()`
- [ ] Confirmed a monotonic rescaling left the tree **unchanged**
- [ ] Can say why — and name the three earlier days whose scaling rules do not apply here
- [ ] Ran `interactions_come_free()` and saw an interaction found unaided
- [ ] Can say what Day 82 had to do by hand that a tree does structurally

## Overfitting and pruning

- [ ] Ran `it_overfits_completely()`; recorded train accuracy ______ and depth ______
- [ ] Can say why an unlimited tree reaches perfect training accuracy
- [ ] Ran `cost_complexity_pruning()` and read the alpha path
- [ ] Can say what `ccp_alpha` trades
- [ ] Confirmed the pruning choice used **cross-validation**, never test data

## Importance

- [ ] Ran `the_importance_bias()`
- [ ] Confirmed Gini importance was fooled by a **high-cardinality noise column**
- [ ] Confirmed permutation importance was not
- [ ] Can name **both** flaws in Gini importance
- [ ] Can say why permutation importance must be computed on held-out data

## Instability and limits

- [ ] Ran `trees_are_unstable()` across resamples
- [ ] Can say what changes when a single row moves
- [ ] Can say which later day this instability motivates
- [ ] Ran `what_trees_cannot_do()`
- [ ] Can say what an axis-aligned split costs on a diagonal boundary
- [ ] Can say what a tree does outside its training range

## Build brief

- [ ] `impurity` — **TODO(me)**: Gini and entropy, handles the empty and pure cases
- [ ] `best_split` — **TODO(me)**: size-weighted gain, respects `min_samples_leaf`
- [ ] `gini_vs_permutation_importance` — **TODO(me)**: warning names **both** flaws
- [ ] `prune_by_cross_validation` — **TODO(me)**: never touches test data
- [ ] `tree_stability` — **TODO(me)**: note points at ensembles
- [ ] `tree_limitations_report` — **TODO(me)**: diagonal vs axis-aligned
- [ ] Can explain why Gini importance inflates high-cardinality features

## Tests that must be able to fail

- [ ] `test_impurity_is_zero_for_a_pure_node` — green
- [ ] `test_impurity_is_maximal_at_an_even_split` — green
- [ ] `test_impurity_handles_zero_log_zero` — green
- [ ] `test_an_empty_node_has_zero_impurity` — green
- [ ] `test_impurity_rejects_an_unknown_criterion` — green
- [ ] `test_the_split_matches_sklearns_root` — green
- [ ] `test_the_gain_is_weighted_by_child_size` — green
- [ ] **Used an unweighted gain, watched it go red, weighted it** ← do not skip
- [ ] `test_a_perfect_split_has_gain_equal_to_the_parent_impurity` — green
- [ ] `test_no_valid_split_is_a_leaf_condition_not_an_error` — green
- [ ] `test_min_samples_leaf_is_respected` — green
- [ ] `test_split_rejects_a_length_mismatch` — green
- [ ] `test_a_tree_is_invariant_to_monotonic_rescaling` — green
- [ ] `test_a_tree_finds_an_interaction_unaided` — green
- [ ] `test_an_unlimited_tree_memorises` — green
- [ ] `test_pruning_reduces_the_leaf_count` — green
- [ ] `test_pruning_prefers_the_simplest_among_near_ties` — green
- [ ] `test_pruning_never_looks_at_test_data` — green
- [ ] `test_gini_importance_is_fooled_by_a_noise_column` — green ← **today's real assessment**
- [ ] `test_permutation_importance_is_not_fooled` — green
- [ ] **Reported Gini importance as the answer, watched the noise column rank high** ← do not skip
- [ ] `test_the_importance_warning_names_both_flaws` — green
- [ ] `test_importance_requires_a_fitted_tree` — green
- [ ] `test_trees_are_unstable_under_resampling` — green
- [ ] `test_the_stability_note_mentions_ensembles` — green
- [ ] `test_stability_rejects_a_bad_fraction` — green
- [ ] `test_a_diagonal_boundary_penalises_the_tree` — green
- [ ] `test_an_axis_aligned_boundary_does_not_penalise_the_tree` — green
- [ ] `test_the_limitations_docstring_mentions_extrapolation` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Define Gini and entropy, and say when the choice matters
- [ ] Why must split gain be weighted by child size?
- [ ] Why does a tree need no scaling, when KNN and SVM do?
- [ ] What does a tree get for free that Day 82 had to construct?
- [ ] Why does an unlimited tree reach perfect training accuracy?
- [ ] Give both flaws in Gini importance, and the fix for each
- [ ] Why are trees unstable, and what does that motivate?
- [ ] What can a tree not represent, and what does it do outside its training range?

## Commit

- [ ] `./m check && ./m done 105` succeeded
