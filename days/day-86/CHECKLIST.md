# Day 86 — CHECKLIST

**IDs covered:** EDA-04 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-86/lab/multivariate.py
uv run python -m pytest tests/test_eda.py -v
```

Expected: the eight-part report ending with the when-to-use list, then all eda tests green.

## Setup

- [ ] `./m start 86` and `./m scaffold 86` run
- [ ] `days/day-86/lab/multivariate.py` created
- [ ] No new packages installed

## EDA-04 — from scratch

- [ ] Built PCA from an eigendecomposition **before** using sklearn
- [ ] Used `eigh` rather than `eig`; can say why
- [ ] Confirmed the eigenvalues sum to the number of features
- [ ] Can say why that identity holds
- [ ] Confirmed sklearn's explained ratios match yours

## What it reveals

- [ ] Ran `what_it_reveals()` on six columns from three latent factors
- [ ] Confirmed three components captured nearly everything
- [ ] **Read the loadings column-wise** and named each factor
- [ ] Can say what "we have 6 features but 3 independent things" means operationally

## Standardising

- [ ] Ran `standardising_is_not_optional()`
- [ ] Recorded the dominant column raw: ______ and standardised: ______
- [ ] Can state what unstandardised PCA actually answers

## How many components

- [ ] Ran `choosing_how_many()`; recorded all three rules
- [ ] Can say why "eigenvalue > 1" assumes standardised data
- [ ] Can say what the answer usually is when the purpose is looking

## Multivariate outliers

- [ ] Ran `multivariate_outliers()`
- [ ] Confirmed both values were **univariately unremarkable**
- [ ] Can say why Day 77's per-column z-scores cannot see this
- [ ] Can define "multivariate outlier" in one sentence

## The three problems

- [ ] Ran `pca_ignores_the_target()` and **read the correlation column**
- [ ] Confirmed PC1 dominated the variance and predicted nothing
- [ ] Can say where the signal was, and what rule would have discarded it
- [ ] Ran `pca_is_a_fitted_transform()`
- [ ] Recorded the component angle between the two fits: ______°
- [ ] Can say why this leak is easy to miss
- [ ] Can name all three reasons PCA is a poor modelling default
- [ ] Read `when_pca_is_the_right_feature_step()`; can give one case each way

## Build brief

- [ ] `pca_explore` — **TODO(me)**: labelled loadings, warns by name when unstandardised
- [ ] `scree` — **TODO(me)**: three rules, flags disagreement
- [ ] `redundancy_report` — **TODO(me)**: groups columns, drops carry reasons
- [ ] `multivariate_outliers` — **TODO(me)**: explanations name the columns involved
- [ ] `assert_pca_is_exploratory` — **TODO(me)**: forces a named decision
- [ ] Can explain why the warning names the dominant column rather than being generic

## Tests that must be able to fail

- [ ] `test_pca_matches_the_eigendecomposition` — green
- [ ] `test_three_components_recover_three_latent_factors` — green
- [ ] `test_explained_variance_is_decreasing` — green
- [ ] `test_loadings_are_labelled` — green
- [ ] `test_the_loadings_group_the_latent_factors` — green
- [ ] `test_unstandardised_pca_warns_and_names_the_dominant_column` — green
- [ ] **Made the warning generic, watched it go red, named the column** ← do not skip
- [ ] `test_standardising_changes_which_column_dominates` — green
- [ ] `test_missing_rows_are_dropped_and_counted` — green
- [ ] `test_non_numeric_columns_are_dropped_with_a_note` — green
- [ ] `test_too_few_numeric_columns_raises` / `test_too_many_components_raises` — green
- [ ] `test_scree_reports_every_rule` — green
- [ ] `test_scree_flags_disagreement_between_rules` — green
- [ ] `test_disagreeing_rules_recommend_looking` — green
- [ ] `test_kaiser_finds_the_latent_dimension` — green
- [ ] `test_redundancy_finds_the_effective_dimension` — green
- [ ] `test_redundancy_groups_the_correlated_columns` — green
- [ ] `test_suggested_drops_carry_their_reason` — green
- [ ] `test_independent_columns_are_not_flagged_as_redundant` — green
- [ ] **Made the report always claim redundancy, watched it go red, fixed it** ← do not skip
- [ ] `test_a_multivariate_outlier_is_found` — green
- [ ] `test_outlier_explanations_name_the_columns` — green
- [ ] `test_clean_data_yields_few_outliers` — green
- [ ] `test_outliers_reject_a_bad_quantile` — green
- [ ] `test_pca_can_miss_the_signal_entirely` — green ← **today's real assessment**
- [ ] `test_exploration_context_is_allowed` — green
- [ ] `test_an_unnamed_modelling_context_is_refused` — green
- [ ] `test_pca_is_not_fitted_outside_a_pipeline_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is PCA, in terms of the correlation matrix?
- [ ] Why must you standardise first, and what happens if you do not?
- [ ] What does a loading tell you, and how do you read the table?
- [ ] Define a multivariate outlier and say why per-column checks miss it
- [ ] Give all three reasons PCA is a poor modelling default
- [ ] Why can the top component predict nothing?
- [ ] Why is fitting PCA before the split a leak, and why is it easy to miss?
- [ ] When would dropping a column beat running PCA?

## Commit

- [ ] `./m check && ./m done 86` succeeded
