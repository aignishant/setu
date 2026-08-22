# Day 103 — CHECKLIST

**IDs covered:** ML-14 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-103/lab/neighbours.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the nine-part report including the contrast table and the shell measurement, then all model
tests green.

## Setup

- [ ] `./m start 103` and `./m scaffold 103` run
- [ ] `days/day-103/lab/neighbours.py` created
- [ ] No new packages installed

## ML-14 — the algorithm

- [ ] Implemented distance/sort/vote by hand and matched sklearn
- [ ] Can say what `fit` actually does
- [ ] Ran `the_cost_is_at_prediction_time()`; recorded fit vs predict timings
- [ ] Can say why this is called a **lazy** learner
- [ ] Can connect the cost to why Phase 17 uses approximate indexes
- [ ] Can say what a failure to beat KNN tells you

## Scaling — the fourth reason

- [ ] Ran `scale_decides_everything()`
- [ ] Recorded raw accuracy ______ vs scaled ______
- [ ] Can explain why a 1000× sd is a 1,000,000× distance contribution
- [ ] Can state all **four** scaling reasons in this phase, with their days
- [ ] Confirmed the scaler used **train** statistics on both splits

## The curse

- [ ] Ran `the_curse_measured()` and **read the ratio column**
- [ ] Recorded the nearest/farthest ratio at 1 dim ______ and 1000 dims ______
- [ ] Can define "contrast" and say what it goes to
- [ ] Ran `volume_concentrates_in_the_shell()`
- [ ] Confirmed the empirical values matched `0.9^d`
- [ ] Can say why high-dimensional space is "almost entirely surface"
- [ ] Ran `how_much_data_you_would_need()`; recorded the count for 10 dimensions
- [ ] Can say why "more features" is never free

## Consequences

- [ ] Ran `knn_degrades_with_dimension()` with pure noise columns
- [ ] Can say why KNN cannot ignore a useless column
- [ ] Can name two models that can (with their days)
- [ ] Ran `k_is_the_capacity_dial()` and read the gap column
- [ ] Can say what `k=1` training accuracy of 1.0 means
- [ ] Can say why `k` should be odd for binary classification
- [ ] Ran `the_metric_is_a_choice()`; can say when cosine is right and why

## Build brief

- [ ] `knn_predict` — **TODO(me)**: vectorised, three metrics, distance-domination guard
- [ ] `distance_contrast` — **TODO(me)**: verdict **and** an actionable recommendation
- [ ] `choose_k` — **TODO(me)**: odd candidates, exposes train scores, warns of optimism
- [ ] `curse_report` — **TODO(me)**: cites real numbers, names a concrete alternative
- [ ] `assert_scaled_for_distance` — **TODO(me)**: names the **squared** effect
- [ ] Can explain why this guard is not KNN-specific

## Tests that must be able to fail

- [ ] `test_it_matches_sklearn` — green
- [ ] `test_k_one_returns_the_point_itself` — green
- [ ] `test_the_neighbours_are_actually_the_nearest` — green
- [ ] `test_distances_are_returned_sorted` — green
- [ ] `test_prediction_is_vectorised` — green under 5 s
- [ ] `test_unscaled_features_are_refused_with_the_distance_reason` — green
- [ ] **Reused Day 95's or 98's message, watched the distance assertion go red** ← do not skip
- [ ] `test_scaling_rescues_a_hopeless_model` — green
- [ ] `test_an_even_k_warns_about_ties` — green
- [ ] `test_high_dimensional_input_warns_about_the_curse` — green
- [ ] `test_k_larger_than_the_training_set_raises` / `..._unknown_metric_raises` — green
- [ ] `test_contrast_collapses_with_dimension` — green ← **today's real assessment**
- [ ] `test_contrast_is_monotone_in_dimension` — green
- [ ] `test_the_recommendation_is_actionable` — green
- [ ] **Wrote "beware the curse", watched it go red, named a concrete fix** ← do not skip
- [ ] `test_contrast_rejects_a_tiny_input` — green
- [ ] `test_choose_k_prefers_odd_values_for_binary` — green
- [ ] `test_choose_k_exposes_the_k_one_memorisation` — green
- [ ] `test_choose_k_warns_the_score_is_optimistic` — green
- [ ] `test_choose_k_rejects_an_oversized_candidate` — green
- [ ] `test_noise_dimensions_destroy_knn` — green
- [ ] `test_the_curse_report_names_concrete_numbers` — green
- [ ] `test_the_curse_report_suggests_a_named_alternative` — green
- [ ] `test_low_dimensional_data_is_not_flagged` — green
- [ ] **Made the report always warn, watched the low-dimensional case go red** ← do not skip
- [ ] `test_points_per_dimension_is_reported` — green
- [ ] `test_the_scaling_guard_names_the_squared_effect` — green
- [ ] `test_the_scaling_guard_passes_on_scaled_data` — green
- [ ] `test_the_guard_docstring_covers_other_distance_methods` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does KNN's `fit` do, and where does the cost live?
- [ ] Why is unscaled KNN a KNN on one column?
- [ ] Define contrast and say what happens to it as dimensions grow
- [ ] Why is high-dimensional space "almost entirely surface"?
- [ ] Why can KNN not ignore a useless feature?
- [ ] What does `k=1` training accuracy of 1.0 tell you?
- [ ] When is cosine the right metric, and why?
- [ ] Which later phases does the curse affect, and how?

## Commit

- [ ] `./m check && ./m done 103` succeeded
