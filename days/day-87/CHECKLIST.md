# Day 87 — CHECKLIST

**IDs covered:** EDA-05 · **Principles served:** 1, 7, 8, 9

## Demo command

```bash
uv run python days/day-87/lab/reviews.py
uv run python -m pytest tests/test_text_features.py -v
```

Expected: the eight-part report ending with the carry-forward inventory, then all text tests green.

## Setup

- [ ] `./m start 87` and `./m scaffold 87` run
- [ ] Files created: `days/day-87/lab/reviews.py`, `src/setu/text_features.py`,
      `tests/test_text_features.py`
- [ ] **A `SOURCE.md` row added** for the corpus, including *how it was collected*
- [ ] Confirmed you are working on the training split only

## EDA-05 — text breaks the toolkit

- [ ] Can say why a review has no mean
- [ ] Can name the only two things computable without a representation choice
- [ ] Ran `basic_shape()` and **noticed the length gap** before it was explained

## Stopwords

- [ ] Confirmed sklearn's list contains "not", "no", "never"
- [ ] Watched `"not good at all"` become `"good"`
- [ ] Recorded the fraction of reviews containing "not": ______
- [ ] Can state why this is a modelling decision, not cleaning
- [ ] Can name the principled fix

## Representation

- [ ] Ran all six representations and compared feature counts
- [ ] Can say what `min_df=5` gains and what it costs
- [ ] Can say what bigrams buy you here
- [ ] Can state why "every row above is a different dataset"

## Screening

- [ ] Ran `which_words_separate()`
- [ ] Can say how many comparisons that was
- [ ] Can say why leaving them uncorrected is legitimate

## The collection artifact

- [ ] Ran `the_collection_artifact()` and recorded both accuracies
- [ ] Confirmed **length beat sentiment**
- [ ] Read `training_reviews()`'s docstring and can explain why
- [ ] Can say what a model trained on this would do when the scrape changed
- [ ] Can state what Day 85's screen could and **could not** tell you
- [ ] Can say where the explanation actually came from

## Duplicates and carry-forward

- [ ] Compared exact and normalised duplicate counts
- [ ] Can say why near-duplicates are a split problem
- [ ] Can name the split type for shared authors or films
- [ ] Listed hypotheses, decisions **with reasons**, and open questions separately
- [ ] Confirmed nothing was called a finding

## Build brief

- [ ] `TextSpec` — frozen dataclass of the choices
- [ ] `safe_stopwords` — **TODO(me)**: negations removed by default, dangerous path is hard
- [ ] `validate_spec` — **TODO(me)**
- [ ] `text_profile` — **TODO(me)**: no representation choice needed, warns on length gap
- [ ] `top_discriminating_terms` — **TODO(me)**: declares its comparison count
- [ ] `assert_no_length_leak` — **TODO(me)**: a **screen**, asks the provenance question
- [ ] `build_vectorizer` — **TODO(me)**: returns an **unfitted** object
- [ ] Can explain why the length check must not say "drop"

## Tests that must be able to fail

- [ ] `test_negations_are_kept_by_default` — green
- [ ] `test_the_base_list_actually_contained_them` — green ← a **dependency-drift** test
- [ ] `test_dropping_negations_requires_an_explicit_acknowledgement` — green
- [ ] `test_the_spec_validates_ngram_range` / `..._unknown_weighting` — green
- [ ] `test_removing_stopwords_without_negations_is_refused` — green
- [ ] `test_the_spec_is_frozen` — green
- [ ] `test_profile_needs_no_representation_choice` — green
- [ ] `test_profile_finds_near_duplicates` — green
- [ ] `test_near_duplicates_warn_about_split_leakage` — green
- [ ] `test_profile_measures_the_negation_rate` — green
- [ ] `test_profile_rejects_an_empty_corpus` — green
- [ ] `test_the_length_artifact_is_caught` — green ← **today's real assessment**
- [ ] **Made the warning report only the number, watched the provenance assertion go red** ← do not skip
- [ ] `test_a_genuine_length_difference_is_not_treated_as_a_verdict` — green
- [ ] **Made the warning say "drop this feature", watched it go red, softened it to a check** ← do not skip
- [ ] `test_similar_lengths_produce_no_warning` — green
- [ ] `test_assert_no_length_leak_raises_and_asks_why` — green
- [ ] `test_assert_no_length_leak_passes_on_balanced_lengths` — green
- [ ] `test_discriminating_terms_find_the_signal` — green
- [ ] `test_discriminating_terms_declare_their_comparison_count` — green
- [ ] `test_discriminating_terms_call_themselves_hypotheses` — green
- [ ] `test_discriminating_terms_reject_a_multiclass_label` — green
- [ ] `test_the_vectorizer_comes_back_unfitted` — green
- [ ] `test_the_vectorizer_uses_the_safe_stopword_list` — green
- [ ] `test_bigrams_capture_negation` — green
- [ ] `test_unigrams_alone_cannot_distinguish_negation` — green
- [ ] `test_building_from_an_unvalidated_spec_raises` — green
- [ ] `test_source_md_records_the_corpus` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does text require a decision before any statistic is possible?
- [ ] What does removing stopwords do to a sentiment task, and what fixes it?
- [ ] Name three representation choices and what each changes
- [ ] Describe the collection artifact and how a model trained on it fails
- [ ] What can a "predicts too well" screen tell you, and what can it not?
- [ ] Where did the explanation come from?
- [ ] Why must the length check be a screen rather than a verdict?
- [ ] Why deduplicate before splitting, and when do you need a grouped split?

## Commit

- [ ] `./m check && ./m done 87` succeeded
