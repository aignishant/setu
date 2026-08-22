# Day 123 — CHECKLIST

**IDs covered:** NLP-10, NLP-11 · **Principles served:** 1, 2, 7, 9

## Demo command

```bash
uv run python days/day-123/lab/vectors.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the ten-part report ending with document averaging, then all nlp tests green.

## Setup

- [ ] `./m start 123` and `./m scaffold 123` run
- [ ] `uv add "gensim==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-123/lab/vectors.py` created
- [ ] **Pretrained vectors recorded in `PINS_DS.md` as a dataset** — which vectors,
      which corpus, which year (Principle 9)

## The gap

- [ ] Ran `the_gap_yesterday_left()`
- [ ] Recorded TF-IDF similarity for the synonym pair: ______
- [ ] Can say why TF-IDF cannot see synonymy
- [ ] Can name the two earlier days this problem survives from

## NLP-10 — the distributional hypothesis

- [ ] Ran `the_distributional_hypothesis()`
- [ ] Recorded shared contexts for doctor/physician and doctor/mechanic
- [ ] Can state the hypothesis in one sentence
- [ ] Can say what was labelled to make it work

## Count-based embeddings

- [ ] Built co-occurrence + PPMI + SVD **from scratch**
- [ ] Recorded cosine for doctor/physician ______ and doctor/mechanic ______
- [ ] Can say what PPMI does, and which earlier day shares its instinct
- [ ] Can say what happens without PPMI

## NLP-11 — Word2Vec

- [ ] Ran `word2vec_is_a_pretext_task()`
- [ ] Can explain skip-gram and CBOW in one line each
- [ ] Can say what is kept and what is thrown away
- [ ] Can name where the same pattern recurs later in the plan
- [ ] Can say which is the usual default, and why
- [ ] Trained vectors on the toy corpus
- [ ] Confirmed synonyms scored above unrelated words
- [ ] Can say what `workers=1` is for
- [ ] Can say what `min_count` does silently, and when it bites

## Cosine

- [ ] Ran `cosine_not_euclidean()`
- [ ] Recorded cosine and euclidean for `v` vs `4v`
- [ ] Can say what magnitude tracks in an embedding
- [ ] Confirmed cosine equals the dot product after L2 normalisation
- [ ] Can say why Phase 18's vector databases care

## The analogy result

- [ ] Ran `the_analogy_result_is_weaker_than_advertised()`
- [ ] Can say exactly what the standard evaluation excludes
- [ ] Can say what the answer usually is **without** the exclusion
- [ ] Can state the real benchmark accuracy range
- [ ] Can say why this is a convention rather than fraud

## Bias

- [ ] Read `embeddings_inherit_their_corpus()`
- [ ] Can give two published association results
- [ ] Can say whether these are implementation artefacts
- [ ] Can say what debiasing does and does **not** achieve
- [ ] Can state the Principle 9 consequence

## Limits

- [ ] Read `where_static_vectors_break()`
- [ ] Can say what happens to `bank`
- [ ] Can name the OOV fix and the library that provides it
- [ ] Can say which phase resolves the one-vector-per-word limit
- [ ] Ran `document_vectors_by_averaging()`
- [ ] Confirmed the synonym gap closed versus §3.1
- [ ] Can give three weaknesses of averaging

## Build brief

- [ ] `cosine_similarity` — **TODO(me)**: names zero vectors, explains why not euclidean
- [ ] `cooccurrence_matrix` — **TODO(me)**: window does **not** cross documents
- [ ] `ppmi` — **TODO(me)**: no nan or inf, cites the IDF instinct
- [ ] `svd_embeddings` — **TODO(me)**: unit-length rows
- [ ] `train_embeddings` — **TODO(me)**: forces `workers=1`, lists dropped words
- [ ] `analogy` — **TODO(me)**: reports `answer_without_exclusion` **always**
- [ ] `measure_association_bias` — **TODO(me)**: raises on missing words
- [ ] `document_vector` — **TODO(me)**: returns **None** for all-OOV
- [ ] Can explain why the unexcluded analogy answer must be reported

## Tests that must be able to fail

- [ ] `test_cosine_ignores_magnitude` — green
- [ ] `test_euclidean_would_have_disagreed` — green
- [ ] `test_opposite_vectors_score_minus_one` — green
- [ ] `test_a_zero_vector_is_named_not_returned_as_nan` — green
- [ ] `test_a_dimension_mismatch_names_both` — green
- [ ] `test_the_cosine_docstring_explains_why_not_euclidean` — green
- [ ] `test_the_window_does_not_cross_documents` — green
- [ ] **Let the window cross documents and watched invented pairs appear** ← do not skip
- [ ] `test_cooccurrence_is_symmetric` — green
- [ ] `test_a_word_does_not_cooccur_with_itself` — green
- [ ] `test_a_wider_window_finds_more_pairs` — green
- [ ] `test_cooccurrence_rejects_a_zero_window` — green
- [ ] `test_ppmi_downweights_a_ubiquitous_word` — green
- [ ] `test_ppmi_is_never_negative` — green
- [ ] `test_ppmi_produces_no_nan_or_inf` — green
- [ ] `test_the_ppmi_docstring_cites_the_idf_instinct` — green
- [ ] `test_ppmi_rejects_negative_counts` — green
- [ ] `test_count_based_embeddings_find_synonyms` — green
- [ ] `test_normalised_embeddings_have_unit_length` — green
- [ ] `test_too_many_dimensions_are_refused` — green
- [ ] `test_training_is_reproducible` — green
- [ ] **Left `workers` at the default and watched two seeded runs differ** ← do not skip
- [ ] `test_dropped_words_are_listed` — green
- [ ] `test_a_tiny_corpus_is_warned_about` — green
- [ ] `test_trained_vectors_place_synonyms_together` — green
- [ ] `test_training_rejects_an_empty_corpus` — green
- [ ] `test_the_analogy_exclusion_is_visible` — green ← **today's real assessment**
- [ ] `test_without_exclusion_an_input_word_usually_wins` — green
- [ ] **Hid the exclusion inside the implementation, watched the test go red** ← do not skip
- [ ] `test_the_excluded_answer_differs_from_the_unexcluded_one` — green
- [ ] `test_the_analogy_note_is_honest_about_the_convention` — green
- [ ] `test_a_missing_analogy_word_is_named` — green
- [ ] `test_association_bias_is_measurable` — green
- [ ] `test_unbiased_vectors_are_not_flagged` — green
- [ ] `test_the_statement_blames_the_corpus_not_the_algorithm` — green
- [ ] `test_the_statement_does_not_claim_debiasing_solves_it` — green
- [ ] `test_a_missing_bias_word_raises_rather_than_skipping` — green
- [ ] `test_averaging_closes_the_synonym_gap` — green
- [ ] `test_an_all_oov_document_returns_none_not_zeros` — green
- [ ] `test_oov_terms_are_named` — green
- [ ] `test_a_high_oov_rate_is_warned_about` — green
- [ ] `test_weighting_changes_the_document_vector` — green
- [ ] `test_the_docstring_admits_averaging_loses_order` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the distributional hypothesis and say what supervises it
- [ ] Describe the PPMI + SVD route, and why no neural network is needed
- [ ] What does Word2Vec keep, and what does it discard?
- [ ] Why cosine rather than Euclidean for embeddings?
- [ ] What does the standard analogy evaluation exclude, and what happens without it?
- [ ] Are embedding biases a bug? What does debiasing actually achieve?
- [ ] What happens to a word with two senses?
- [ ] Give three weaknesses of averaging word vectors into a document vector

## Commit

- [ ] `./m check && ./m done 123` succeeded
