# Day 121 — CHECKLIST

**IDs covered:** NLP-07, NLP-08 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-121/lab/bow.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the ten-part report ending with the task table, then all nlp tests green.

## Setup

- [ ] `./m start 121` and `./m scaffold 121` run
- [ ] `days/day-121/lab/bow.py` created
- [ ] No new packages installed

## NLP-07 — one-hot and bag of words

- [ ] Ran `one_hot_first()`
- [ ] Can say what distance separates `cat` from `dog` versus `cat` from `the`
- [ ] Can state what one-hot encodes, and what it does not
- [ ] Can name the day that fills that gap
- [ ] Built bag of words from scratch and matched sklearn
- [ ] Can say what decides `|V|`, and which day made those decisions

## Word order

- [ ] Ran `word_order_is_gone()` on all three pairs
- [ ] Confirmed the vectors were **identical**
- [ ] Can say when the information was destroyed, relative to the model
- [ ] Can say why a perfect stopword list does not fix this

## Sparsity

- [ ] Ran `sparsity_is_the_practical_fact()`
- [ ] Recorded dense ______ GB vs sparse ______ MB
- [ ] Can say why `.toarray()` fails only on the full corpus
- [ ] Can name a model family that does **not** accept sparse input

## NLP-08 — n-grams

- [ ] Ran `n_grams_recover_some_order()`
- [ ] Confirmed bigrams separated `not good` from `good`
- [ ] Can say why this beats a stopword list as a fix
- [ ] Ran `the_feature_explosion()` and read the whole grid
- [ ] Recorded the bigram multiplier: ______×
- [ ] Can say what fraction of n-grams appear once
- [ ] Can say what `min_df=2` costs and what it saves

## Counting choices

- [ ] Ran `binary_counts_and_sublinear_scaling()`
- [ ] Can say whether four mentions of "good" are four times as positive
- [ ] Can name a model family that expects binary input
- [ ] Can say which scaling tomorrow's TF-IDF uses

## The leak

- [ ] Ran `the_vocabulary_is_fitted()`
- [ ] Can say what `fit` actually learns
- [ ] Can name the earlier days whose rule this is
- [ ] Can say why people forget it here specifically
- [ ] Ran `out_of_vocabulary_is_silent()`
- [ ] Confirmed an all-OOV document became an **all-zero row**
- [ ] Can say what a model does with that row
- [ ] Can say why the OOV rate is a useful production signal

## Build brief

- [ ] `build_vocabulary` — **TODO(me)**: reports dropped counts, documents the min_df/max_df asymmetry
- [ ] `to_bag_of_words` — **TODO(me)**: **sparse only**, reports OOV and empty rows
- [ ] `order_sensitivity` — **TODO(me)**: finds permutation pairs with identical vectors
- [ ] `ngram_cost` — **TODO(me)**: singleton rate, concrete recommendation
- [ ] `assert_vocabulary_fitted_on_train_only` — **TODO(me)**
- [ ] `oov_monitor` — **TODO(me)**: names the new terms, needs no labels
- [ ] Can explain why `empty_rows` must be surfaced rather than inferred

## Tests that must be able to fail

- [ ] `test_the_vocabulary_is_sorted_and_indexed` — green
- [ ] `test_min_df_is_a_count_and_max_df_is_a_fraction` — green
- [ ] `test_the_dropped_counts_are_reported` — green
- [ ] `test_a_huge_singleton_vocabulary_is_warned_about` — green
- [ ] `test_filters_that_remove_everything_are_named` — green
- [ ] `test_vocabulary_rejects_an_empty_corpus` — green
- [ ] `test_the_matrix_is_sparse` — green
- [ ] **Returned a dense array and watched the type assertion go red** ← do not skip
- [ ] `test_the_docstring_explains_why_sparse` — green
- [ ] `test_counts_match_a_hand_computation` — green
- [ ] `test_binary_mode_discards_repetition` — green
- [ ] `test_sublinear_mode_dampens_repetition` — green
- [ ] `test_an_unknown_mode_raises` — green
- [ ] `test_an_all_oov_document_becomes_an_empty_row` — green
- [ ] `test_a_high_oov_rate_is_warned_about` — green
- [ ] `test_word_order_is_destroyed_under_unigrams` — green ← **today's real assessment**
- [ ] `test_bigrams_recover_the_distinction` — green
- [ ] `test_the_negation_pair_needs_bigrams` — green
- [ ] **Tried to separate "not good" with unigrams and watched it fail** ← do not skip
- [ ] `test_the_note_says_the_information_is_destroyed_early` — green
- [ ] `test_order_sensitivity_needs_two_documents` — green
- [ ] `test_bigrams_multiply_the_feature_count` — green
- [ ] `test_most_ngrams_appear_exactly_once` — green
- [ ] `test_min_df_two_removes_most_of_the_explosion` — green
- [ ] `test_the_recommendation_names_a_concrete_setting` — green
- [ ] `test_the_note_warns_that_min_df_loses_rare_terms` — green
- [ ] `test_fitting_on_all_data_is_refused` — green
- [ ] **Fitted the vectoriser before splitting and watched the guard catch it** ← do not skip
- [ ] `test_fitting_on_train_only_passes` — green
- [ ] `test_fitting_on_train_plus_test_is_refused` — green
- [ ] `test_the_oov_monitor_names_the_new_terms` — green
- [ ] `test_a_stable_corpus_does_not_alert` — green
- [ ] `test_an_empty_document_always_alerts` — green
- [ ] `test_the_monitor_recommendation_is_actionable` — green
- [ ] `test_the_monitor_docstring_says_it_needs_no_labels` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does one-hot encode, and what does it fail to encode?
- [ ] What does bag of words destroy, and when?
- [ ] Why does a perfect stopword list not fix the negation problem?
- [ ] Give the dense-versus-sparse memory figures and say why it matters
- [ ] What do bigrams buy, and what do they cost?
- [ ] Why does `min_df=2` remove most of the explosion almost for free?
- [ ] Why is fitting a vectoriser before splitting a leak?
- [ ] What happens to a document of entirely unseen words?

## Commit

- [ ] `./m check && ./m done 121` succeeded
