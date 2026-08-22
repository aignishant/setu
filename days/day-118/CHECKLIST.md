# Day 118 — CHECKLIST

**IDs covered:** NLP-03, NLP-04 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-118/lab/normalise_words.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the nine-part report ending with the task table, then all nlp tests green.

## Setup

- [ ] `./m start 118` and `./m scaffold 118` run
- [ ] `days/day-118/lab/normalise_words.py` created
- [ ] NLTK `wordnet` and `stopwords` data downloaded
- [ ] No new packages installed

## NLP-03 — stemming

- [ ] Wrote a Porter subset by hand and compared against NLTK
- [ ] Can say what stemming is, in one sentence, without the word "dictionary"
- [ ] Ran `over_and_under_stemming()`
- [ ] Can define over-stemming with the `univers` example
- [ ] Can define under-stemming with the `ran`/`run` example
- [ ] Can say why better rules cannot fix under-stemming

## Lemmatisation

- [ ] Ran `lemmatisation_needs_the_part_of_speech()`
- [ ] Recorded `saw` as noun ______ and as verb ______
- [ ] Confirmed NLTK's lemmatiser **defaults to noun**
- [ ] Recorded what `lemmatize('was')` returns without a tag: ______
- [ ] Can say why that is the commonest bug in this area
- [ ] Can name the day that supplies the missing tag

## Choosing between them

- [ ] Ran `stemming_versus_lemmatisation()` and recorded both timings
- [ ] Can say when to stem and when to lemmatise
- [ ] Can say when to do **neither**, and why

## NLP-04 — stopwords

- [ ] Ran `stopword_lists_disagree()`
- [ ] Recorded sizes: nltk ______ sklearn ______ spacy ______
- [ ] Recorded the agreement fraction: ______
- [ ] Can say why "we removed stopwords" is not reproducible
- [ ] Know what sklearn's own documentation now warns about

## The negation disaster

- [ ] Ran `the_negation_disaster()`
- [ ] Confirmed the two opposite reviews became **identical**
- [ ] Can list which negations are in sklearn's list
- [ ] Can state the fix — and say why it is not "never remove stopwords"

## When stopwords are the signal

- [ ] Ran `stopwords_are_sometimes_the_signal()`
- [ ] Recorded the function-word rate for both authors
- [ ] Can say why function words fingerprint a writer
- [ ] Can name two tasks where stripping them deletes the feature

## Measuring

- [ ] Read `measure_the_effect_before_deciding()`; can give all four steps
- [ ] Can say why these steps are usually applied
- [ ] Read `what_to_do_by_task()`; can give four task/action pairs
- [ ] Can state what "try neither first" is arguing against

## Build brief

- [ ] `safe_stopwords` — **TODO(me)**: negations removed, `acknowledged` gate, `keep` set
- [ ] Asserts the base list **actually contained** negations
- [ ] `compare_stopword_lists` — **TODO(me)**: names which lists contain negations
- [ ] `stem` — **TODO(me)**: idempotent, points at NLTK
- [ ] `stemming_errors` — **TODO(me)**: **both** error rates
- [ ] `lemmatise` — **TODO(me)**: flags a guessed POS, shows alternatives
- [ ] `measure_step_value` — **TODO(me)**: keeps a step only above CV noise
- [ ] `word_normalisation_advice` — **TODO(me)**: reason names the signal at risk
- [ ] Can explain why the dependency-drift assert is necessary

## Tests that must be able to fail

- [ ] `test_negations_are_removed_from_the_list` — green
- [ ] `test_the_base_list_actually_contained_negations` — green ← dependency-drift guard
- [ ] `test_dropping_negations_requires_acknowledgement` — green
- [ ] `test_an_acknowledged_drop_is_allowed` — green
- [ ] `test_the_intersection_is_smaller_than_any_single_list` — green
- [ ] `test_caller_supplied_words_are_kept` — green
- [ ] `test_an_unknown_source_lists_the_known_ones` — green
- [ ] `test_the_lists_disagree_substantially` — green
- [ ] `test_the_comparison_names_which_lists_contain_negations` — green
- [ ] `test_the_comparison_reports_what_is_unique_to_each` — green
- [ ] `test_stemming_is_idempotent` — green
- [ ] **Reordered the rules and watched idempotence break** ← do not skip
- [ ] `test_stemming_merges_inflections` — green
- [ ] `test_the_stem_docstring_points_at_nltk` — green
- [ ] `test_an_unknown_algorithm_raises` — green
- [ ] `test_over_stemming_is_detected` — green
- [ ] `test_under_stemming_is_detected` — green
- [ ] `test_both_error_rates_are_reported` — green
- [ ] `test_a_clean_vocabulary_has_no_errors` — green
- [ ] `test_stemming_errors_needs_groups` — green
- [ ] `test_a_guessed_pos_is_flagged` — green ← **today's real assessment**
- [ ] **Let it default to noun silently, watched `lemmatize('was')` do nothing** ← do not skip
- [ ] `test_an_explicit_pos_is_not_flagged` — green
- [ ] `test_the_alternatives_show_the_guess_mattered` — green
- [ ] `test_a_word_whose_lemma_is_pos_independent_does_not_warn` — green
- [ ] `test_verbs_are_lemmatised_correctly_with_a_tag` — green
- [ ] `test_an_unknown_pos_lists_the_valid_ones` — green
- [ ] `test_the_negation_disaster_is_reproduced` — green
- [ ] `test_a_safe_list_preserves_the_distinction` — green
- [ ] `test_a_step_that_does_not_help_is_not_kept` — green
- [ ] `test_the_measurement_note_says_these_steps_are_traditional` — green
- [ ] `test_measurement_needs_steps` — green
- [ ] `test_sentiment_never_removes_stopwords` — green
- [ ] `test_authorship_keeps_everything` — green
- [ ] `test_ner_keeps_the_surface_form` — green
- [ ] `test_search_indexing_uses_stemming` — green
- [ ] `test_a_large_corpus_is_told_to_measure_first` — green
- [ ] `test_the_reason_names_the_signal_at_risk` — green
- [ ] `test_an_unknown_task_raises` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Contrast stemming and lemmatisation in one sentence each
- [ ] Define over- and under-stemming with an example of each
- [ ] Why does lemmatisation need a POS tag?
- [ ] What does NLTK's lemmatiser do without one, and why is that dangerous?
- [ ] Why is "we removed stopwords" not a reproducible statement?
- [ ] What happens to "not good" under a standard list?
- [ ] Name a task where stopwords are the signal, and say why
- [ ] What is the honest procedure before adding any of these steps?

## Commit

- [ ] `./m check && ./m done 118` succeeded
