# Day 113 — CHECKLIST

**IDs covered:** ML-24 · **Principles served:** 1, 7, 8, 10

## Demo command

```bash
uv run python days/day-113/lab/compare.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the seven-part report ending with the choose-on-other-grounds table, then all ensemble tests
green.

## Setup

- [ ] `./m start 113` and `./m scaffold 113` run
- [ ] `uv add "lightgbm==<pin>" "catboost==<pin>"` — exact-pinned, drift logged
- [ ] `days/day-113/lab/compare.py` created
- [ ] `THREADS` fixed at module level and used by **every** library

## ML-24 — growth strategy

- [ ] Ran `leaf_wise_versus_level_wise()`
- [ ] Can explain level-wise and leaf-wise in one sentence each
- [ ] Can say which parameter controls LightGBM's capacity
- [ ] Can state the most common LightGBM mistake, and why it is worse than it looks
- [ ] Can give the `num_leaves` rule of thumb
- [ ] Ran `leaf_wise_overfits_on_small_data()`
- [ ] Can name the brake to reach for first on small data

## Categories

- [ ] Ran `native_categorical_handling()`
- [ ] Recorded one-hot columns ______ vs native ______
- [ ] Can say what a native categorical split can ask that a one-hot split cannot
- [ ] Know the dtype requirement, and what happens silently without it

## Ordered encoding

- [ ] Ran `catboost_ordered_encoding()` on **pure noise**
- [ ] Recorded naive correlation ______ and ordered correlation ______
- [ ] Can explain the leak in one sentence (Day 81)
- [ ] Can explain how ordering fixes it
- [ ] Can say why several permutations are averaged

## A fair comparison

- [ ] Read `three_ways_a_comparison_goes_wrong()` and can name all **four**
- [ ] Ran `a_fair_comparison()` with three splits and fixed threads
- [ ] Recorded each library's **test** log loss and fit time
- [ ] Recorded the spread across libraries: ______
- [ ] Can say what to compare that spread against
- [ ] Read `picking_on_other_grounds()`; can give three deciding factors that are not accuracy

## Build brief

- [ ] `ordered_target_encoding` — **TODO(me)**: reports **both** correlations
- [ ] `assert_no_target_encoding_leak` — **TODO(me)**: a screen, not a verdict
- [ ] `leaf_capacity` — **TODO(me)**: warns on a naive depth→leaves translation
- [ ] `fair_comparison_spec` — **TODO(me)**: validates **before** you spend compute
- [ ] `compare_libraries` — **TODO(me)**: no winner when within CV noise
- [ ] `library_choice` — **TODO(me)**: note says to revisit only on a measured gap
- [ ] Can explain why the naive correlation belongs in the output

## Tests that must be able to fail

- [ ] `test_naive_target_encoding_leaks_on_pure_noise` — green
- [ ] `test_ordered_encoding_finds_no_signal_where_there_is_none` — green ← **today's real assessment**
- [ ] **Encoded using all rows instead of preceding ones, watched the leak reappear** ← do not skip
- [ ] `test_the_leak_avoided_is_reported` — green
- [ ] `test_ordered_encoding_still_finds_real_signal` — green
- [ ] **Returned the global mean always, watched the real-signal test go red** ← do not skip
- [ ] `test_the_first_appearance_falls_back_to_the_global_mean` — green
- [ ] `test_more_permutations_reduce_the_variance` — green
- [ ] `test_ordered_encoding_rejects_a_length_mismatch` — green
- [ ] `test_a_leaking_encoding_is_refused` — green
- [ ] `test_a_clean_encoding_passes` — green
- [ ] `test_the_leak_screen_says_it_is_a_screen` — green
- [ ] `test_level_wise_capacity_is_two_to_the_depth` — green
- [ ] `test_leaf_wise_capacity_is_num_leaves` — green
- [ ] `test_translating_depth_to_leaves_naively_is_warned_about` — green
- [ ] `test_a_modest_leaf_count_is_not_warned_about` — green
- [ ] `test_the_wrong_parameter_for_the_library_is_refused` — green
- [ ] `test_a_fair_spec_passes` — green
- [ ] `test_reporting_the_validation_split_is_a_violation` — green
- [ ] `test_uncontrolled_threads_are_a_violation` — green
- [ ] `test_a_zero_tuning_budget_is_a_violation` — green
- [ ] `test_an_unknown_library_lists_the_known_ones` — green
- [ ] `test_a_comparison_needs_two_libraries` — green
- [ ] `test_libraries_within_cv_noise_are_indistinguishable` — green
- [ ] `test_an_indistinguishable_comparison_does_not_recommend_the_winner` — green
- [ ] `test_a_real_gap_is_recognised` — green
- [ ] `test_comparison_rejects_a_missing_score` — green
- [ ] `test_small_data_avoids_leaf_wise` — green
- [ ] `test_high_cardinality_categories_favour_catboost` — green
- [ ] `test_an_existing_sklearn_pipeline_avoids_a_new_dependency` — green
- [ ] `test_team_familiarity_counts_when_nothing_else_decides` — green
- [ ] `test_the_note_says_to_revisit_only_on_a_measured_gap` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Contrast level-wise and leaf-wise growth
- [ ] Why is `num_leaves` LightGBM's capacity parameter?
- [ ] What does a native categorical split ask that one-hot cannot?
- [ ] Explain the target-encoding leak and how ordering removes it
- [ ] Name the four ways a boosting comparison goes wrong
- [ ] Why does reporting the validation score differ per library?
- [ ] What do you compare the spread against before naming a winner?
- [ ] Name three non-accuracy grounds for choosing a library

## Commit

- [ ] `./m check && ./m done 113` succeeded
