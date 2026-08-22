# Day 122 — CHECKLIST

**IDs covered:** NLP-09 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-122/lab/tfidf.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the nine-part report ending with the task table, then all nlp tests green.

## Setup

- [ ] `./m start 122` and `./m scaffold 122` run
- [ ] `days/day-122/lab/tfidf.py` created
- [ ] No new packages installed

## NLP-09 — the problem

- [ ] Ran `why_raw_counts_rank_badly()`
- [ ] Confirmed `the` ranked equal with `quantum`
- [ ] Can say what raw counts measure, and what they do not

## IDF

- [ ] Built IDF from scratch
- [ ] Recorded idf of `the` ______ and `quantum` ______
- [ ] Can say what happens to a term in every document
- [ ] Can say why this beats Day 118's stopword list
- [ ] Can say what `log(N/0)` gives, and why that matters

## TF-IDF

- [ ] Built the full weighting and ranked one document
- [ ] Confirmed `quantum` at the top and `the` at zero
- [ ] Can state the whole idea in five words

## sklearn's three differences

- [ ] Ran `sklearn_differs_in_three_ways()`
- [ ] Can name **all three**
- [ ] Confirmed the smoothed formula matched sklearn's `idf_`
- [ ] Can say what weight a universal term gets under each formula
- [ ] Can say why that difference is behavioural rather than cosmetic

## L2 normalisation

- [ ] Ran `l2_normalisation_is_not_optional()`
- [ ] Recorded the two vector norms with and without it
- [ ] Can say what dominates similarity without normalisation
- [ ] Can say what cosine similarity reduces to with it
- [ ] Can name the day and phase that depend on that

## TF variants

- [ ] Ran `tf_variants_change_the_answer()` across five definitions
- [ ] Can say what `sublinear_tf=True` computes
- [ ] Can say whether it is on by default
- [ ] Can say when it helps, and why (Day 121's point)

## The leak

- [ ] Ran `the_idf_is_fitted_and_leaks()`
- [ ] Recorded the idf of `the` fitted both ways
- [ ] Can name **both** leaks
- [ ] Can say which one is specific to TF-IDF and why it is subtler

## What it cannot do

- [ ] Ran `tfidf_is_a_ranking_not_a_meaning()`
- [ ] Recorded similarity of the two synonymous documents: ______
- [ ] Can say what TF-IDF actually matches
- [ ] Can name the day that fills the gap
- [ ] Read the task table; can give three tasks it suits and two it does not

## Build brief

- [ ] `inverse_document_frequency` — **TODO(me)**: returns the **formula string**
- [ ] `term_frequency` — **TODO(me)**: four variants, guards `log(0)`
- [ ] `fit_tfidf` — **TODO(me)**: reuses Day 121's vocabulary, warns on `norm=None`
- [ ] `transform_tfidf` — **TODO(me)**: uses the **fitted** idf, sparse output
- [ ] `matches_sklearn` — **TODO(me)**: reports `differences_found`, not a boolean
- [ ] `top_terms` — **TODO(me)**: docstring says keywords are corpus-relative
- [ ] `assert_idf_fitted_on_train_only` — **TODO(me)**: names **both** leaks
- [ ] Can explain why the formula string is worth returning

## Tests that must be able to fail

- [ ] `test_a_universal_term_is_annihilated_by_the_textbook_formula` — green
- [ ] `test_the_add_one_adjustment_stops_annihilation` — green
- [ ] `test_a_rare_term_outweighs_a_common_one` — green
- [ ] `test_smoothing_prevents_a_division_by_zero` — green
- [ ] `test_the_unsmoothed_zero_case_explains_why_smoothing_exists` — green
- [ ] `test_the_formula_is_returned_as_a_string` — green
- [ ] `test_a_df_above_n_is_refused` — green
- [ ] `test_relative_tf_divides_by_length` — green
- [ ] `test_sublinear_tf_dampens_repetition` — green
- [ ] `test_sublinear_tf_handles_zero_without_a_log_error` — green
- [ ] **Wrote `1 + log(tf)` unguarded and watched `-inf` appear** ← do not skip
- [ ] `test_binary_tf_discards_the_count` — green
- [ ] `test_an_unknown_tf_variant_lists_the_known_ones` — green
- [ ] `test_negative_counts_are_refused` — green
- [ ] `test_the_from_scratch_version_matches_sklearn` — green ← **today's real assessment**
- [ ] `test_the_three_adjustments_are_named` — green
- [ ] **Built the textbook formula first and watched it disagree** ← do not skip
- [ ] `test_omitting_smoothing_breaks_the_match` — green
- [ ] `test_l2_normalisation_gives_every_document_unit_length` — green
- [ ] `test_without_normalisation_length_dominates` — green
- [ ] `test_normalisation_makes_proportional_documents_identical` — green
- [ ] `test_dropping_the_norm_is_warned_about` — green
- [ ] `test_the_matrix_is_sparse` — green
- [ ] `test_transform_uses_the_fitted_idf_not_a_recomputed_one` — green
- [ ] **Recomputed idf at transform time and watched the guard catch it** ← do not skip
- [ ] `test_the_transform_docstring_names_the_leak` — green
- [ ] `test_an_all_oov_document_is_reported` — green
- [ ] `test_a_fit_without_an_idf_is_refused` — green
- [ ] `test_top_terms_are_the_distinguishing_ones` — green
- [ ] `test_the_docstring_says_keywords_are_corpus_relative` — green
- [ ] `test_top_terms_rejects_an_out_of_range_document` — green
- [ ] `test_tfidf_does_not_capture_synonymy` — green
- [ ] `test_fitting_on_all_data_is_refused` — green
- [ ] `test_the_leak_message_names_both_leaks` — green
- [ ] `test_a_train_only_fit_passes` — green
- [ ] `test_the_idf_weights_differ_when_test_is_included` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give the TF-IDF formula and explain each half
- [ ] Why does IDF downweight stopwords automatically, and why is that better than a list?
- [ ] Name sklearn's three differences from the textbook formula
- [ ] What weight does a universal term get under each, and why does it matter?
- [ ] What does L2 normalisation prevent, and what does it enable?
- [ ] Name both TF-IDF leaks and say which is subtler
- [ ] Why do "movie" and "film" score no higher than "movie" and "automobile"?
- [ ] When is TF-IDF still the right answer?

## Commit

- [ ] `./m check && ./m done 122` succeeded
