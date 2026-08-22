# Day 115 — CHECKLIST

**IDs covered:** ML-26, ML-27, ML-28 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-115/lab/clustering.py
uv run python -m pytest tests/test_clustering.py -v
```

Expected: the eight-part report ending with what makes a clustering useful, then all clustering tests
green.

## Setup

- [ ] `./m start 115` and `./m scaffold 115` run
- [ ] Files created: `days/day-115/lab/clustering.py`, `src/setu/clustering.py`,
      `tests/test_clustering.py`
- [ ] No new packages installed

## ML-28 — K-Means from scratch

- [ ] Wrote the assign/move loop and matched sklearn's inertia
- [ ] Can describe the algorithm in one sentence
- [ ] Can say why convergence is guaranteed
- [ ] Can say what it converges **to**

## Local optima

- [ ] Ran `local_optima_are_real()` across 20 seeds
- [ ] Recorded distinct solutions: ______ of 20
- [ ] Recorded best ARI ______ vs worst ______
- [ ] Can say what `n_init` does
- [ ] Can say what `k-means++` does differently from random init

## Scaling

- [ ] Ran `scaling_decides_the_clusters()`
- [ ] Recorded ARI raw ______ vs standardised ______
- [ ] Can say what K-Means clusters on unscaled data
- [ ] Can name all **four** distinct reasons to scale, with their days

## ML-27 — the metric

- [ ] Ran `the_metric_is_an_assumption()`
- [ ] Can say which point cosine calls closest, and why
- [ ] Can say when cosine is right and when it destroys the signal
- [ ] Read the concentration table; recorded the ratio at p=1000: ______
- [ ] Can name the day that established distance concentration

## ML-26 — no structure

- [ ] Ran `k_means_always_returns_k_clusters()` on uniform noise
- [ ] Recorded the silhouette on noise at k=3: ______
- [ ] Compared it against the structured table
- [ ] Can say what distinguishes the two curves
- [ ] Can state what the algorithm cannot tell you

## Choosing k

- [ ] Ran `choosing_k_honestly()`
- [ ] Confirmed inertia fell at every k
- [ ] Can say why "lowest inertia" is never the criterion
- [ ] Can say why the ARI column is unavailable on real data

## Internal metrics

- [ ] Ran `internal_metrics_score_geometry_not_truth()` on concentric rings
- [ ] Recorded silhouette ______ and ARI ______
- [ ] Can say why K-Means split the rings
- [ ] Can state what an internal metric actually measures
- [ ] Read `what_makes_a_clustering_useful()`; can give four criteria and three failures

## Build brief

- [ ] `pairwise_distance` — **TODO(me)**: three metrics, vectorised, names zero-norm rows
- [ ] `choose_metric` — **TODO(me)**: states the **assumption** in words
- [ ] `fit_kmeans` — **TODO(me)**: k-means++, keeps the best restart, reseeds empty clusters
- [ ] Scaling guard with a **clustering-specific** message
- [ ] `k_selection_curve` — **TODO(me)**: elbow and silhouette, flags a flat curve
- [ ] `has_cluster_structure` — **TODO(me)**: `best_k = None` when there is none
- [ ] `cluster_stability` — **TODO(me)**: compares **co-assignment**, not labels
- [ ] `profile_clusters` — **TODO(me)**: warns that a profile without external variables is circular
- [ ] Can explain why an empty cluster must be reseeded

## Tests that must be able to fail

- [ ] `test_euclidean_matches_the_definition` / `test_manhattan_differs_from_euclidean` — green
- [ ] `test_cosine_ignores_magnitude` — green
- [ ] `test_cosine_and_euclidean_disagree_about_which_is_closer` — green
- [ ] `test_a_zero_norm_row_is_named_not_returned_as_nan` — green
- [ ] `test_distances_are_vectorised` — green under 3 s
- [ ] `test_an_unknown_metric_lists_the_known_ones` / `..._mismatched_dimensions` — green
- [ ] `test_text_data_gets_cosine` — green
- [ ] `test_the_assumption_is_stated_in_words` — green
- [ ] `test_high_dimensional_euclidean_is_warned_about` — green
- [ ] `test_low_dimensional_euclidean_is_not_warned_about` — green
- [ ] `test_kmeans_recovers_well_separated_blobs` — green
- [ ] `test_the_inertia_matches_sklearn` — green
- [ ] `test_inertia_falls_every_iteration` — green
- [ ] `test_more_restarts_never_give_a_worse_solution` — green
- [ ] `test_an_unstable_solution_is_warned_about` — green
- [ ] `test_unscaled_data_is_refused_with_a_clustering_specific_reason` — green
- [ ] **Reused Day 98's message, watched the distance assertion go red** ← do not skip
- [ ] `test_the_scaling_guard_can_be_overridden` — green
- [ ] `test_scaling_changes_which_structure_is_found` — green
- [ ] `test_an_empty_cluster_is_reseeded_not_dropped` — green
- [ ] **Dropped an empty cluster, watched it return k−1 groups** ← do not skip
- [ ] `test_kmeans_rejects_an_impossible_k` — green
- [ ] `test_inertia_always_falls_as_k_rises` — green
- [ ] `test_the_docstring_says_inertia_cannot_be_minimised` — green
- [ ] `test_the_silhouette_peaks_at_the_true_k` — green
- [ ] `test_disagreement_between_elbow_and_silhouette_is_reported` — green
- [ ] `test_a_flat_curve_refuses_to_name_a_k` — green
- [ ] `test_uniform_noise_has_no_structure` — green ← **today's real assessment**
- [ ] `test_real_blobs_do_have_structure` — green
- [ ] **Made the detector always report structure, watched the noise test go red** ← do not skip
- [ ] `test_the_statement_says_kmeans_returns_k_regardless` — green
- [ ] `test_structure_detection_needs_enough_references` — green
- [ ] `test_well_separated_clusters_are_stable` — green
- [ ] `test_clusters_in_noise_are_unstable` — green
- [ ] `test_stability_compares_co_assignment_not_labels` — green
- [ ] **Compared label arrays directly, watched a stable clustering report chaos** ← do not skip
- [ ] `test_stability_rejects_a_bad_fraction` — green
- [ ] `test_the_profile_names_what_distinguishes_each_cluster` — green
- [ ] `test_a_tiny_cluster_is_flagged` — green
- [ ] `test_a_profile_without_external_variables_is_called_circular` — green
- [ ] `test_external_differences_are_reported_when_given` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Describe K-Means in one sentence, and say what it converges to
- [ ] Why is one run not a result?
- [ ] What does K-Means cluster on unscaled data?
- [ ] When is cosine right, and when is it wrong?
- [ ] Why can inertia never be used to choose k?
- [ ] What does a silhouette score actually measure?
- [ ] How would you tell whether your data has any cluster structure at all?
- [ ] What is the only non-circular evidence that a clustering means something?

## Commit

- [ ] `./m check && ./m done 115` succeeded
