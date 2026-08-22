# Day 117 — CHECKLIST

**IDs covered:** NLP-01, NLP-02 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-117/lab/tokenise.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the nine-part report ending with sentence splitting, then all nlp tests green.

## Setup

- [ ] `./m start 117` and `./m scaffold 117` run
- [ ] `uv add "nltk==<pin>" "spacy==<pin>"` — exact-pinned, drift logged
- [ ] `python -m spacy download en_core_web_sm` run
- [ ] **Model version recorded in `docs/PINS_DS.md`** — a pinned library with an unpinned model
      is not reproducible
- [ ] Files created: `days/day-117/lab/tokenise.py`, `src/setu/nlp.py`, `tests/test_nlp.py`

## NLP-01 — what NLP is

- [ ] Can name the three steps of a classical NLP pipeline
- [ ] Can say which two contain the modelling decisions
- [ ] Can say when those decisions are made, relative to any model existing

## NLP-02 — why `split()` fails

- [ ] Ran `naive_split_fails()` and **read all six failures**
- [ ] Can say what happened to the Japanese sample
- [ ] Can state the general lesson about whitespace splitting

## Normalisation

- [ ] Ran `normalisation_destroys_information()`
- [ ] Can name three distinctions lowercasing destroys
- [ ] Can say what `3.2%` becomes when punctuation is stripped, and why that matters
- [ ] Ran `unicode_is_not_optional()`
- [ ] Confirmed two identical-looking strings compared **unequal**
- [ ] Can say why lowercasing does not fix it
- [ ] Can say why a non-breaking space must not be stripped as "invisible"

## Tokenising

- [ ] Wrote the regex tokeniser and can explain **why URLs must match first**
- [ ] Ran `library_tokenisers_disagree()`
- [ ] Recorded token counts: split ______ nltk ______ spacy ______
- [ ] Can say how NLTK handles `Don't`
- [ ] Can state why there is no "correct" tokenisation

## Vocabulary

- [ ] Ran `tokenisation_decides_the_vocabulary()`
- [ ] Recorded vocabulary size at each stage
- [ ] Can say why a smaller vocabulary is usually good
- [ ] Can name two merges that are decisions rather than cleaning

## Task dependence

- [ ] Read `what_you_must_never_normalise_away()`; can give four task/keep pairs
- [ ] Can say which tasks the default pipeline is worst-case for
- [ ] Ran `sentence_splitting_is_also_hard()`
- [ ] Can say what breaks naive sentence splitting
- [ ] Can name a later phase where sentence boundaries matter

## Build brief

- [ ] `NormaliseSpec` — frozen dataclass of the choices
- [ ] `normalise` — **TODO(me)**: unicode **first**, reports what changed
- [ ] `validate_spec` — **TODO(me)**: distinguishes **blocking** from warning
- [ ] `tokenise` — **TODO(me)**: pattern order, whitespace variant for contrast
- [ ] `vocabulary_impact` — **TODO(me)**: reductions relative to the first spec
- [ ] `tokeniser_agreement` — **TODO(me)**: jaccard, and the no-correct-answer note
- [ ] `assert_normalisation_recorded` — **TODO(me)**: names the unrecorded choices
- [ ] Can explain why blocking and warning are different categories

## Tests that must be able to fail

- [ ] `test_composed_and_decomposed_forms_are_merged` — green
- [ ] `test_unicode_normalisation_runs_before_lowercasing` — green
- [ ] **Lowercased before normalising, watched two forms stay distinct** ← do not skip
- [ ] `test_invisible_characters_are_removed` — green
- [ ] `test_a_non_breaking_space_is_not_treated_as_invisible` — green
- [ ] `test_the_report_names_which_steps_changed_the_string` — green
- [ ] `test_a_step_that_changed_nothing_is_not_reported` — green
- [ ] `test_whitespace_is_collapsed` — green
- [ ] `test_an_unknown_unicode_form_lists_the_valid_ones` — green
- [ ] `test_lowercasing_for_ner_is_blocking` — green ← **today's real assessment**
- [ ] **Made it a warning instead of blocking, watched it go red** ← do not skip
- [ ] `test_case_preserving_ner_is_allowed` — green
- [ ] `test_stripping_punctuation_for_sentiment_warns` — green
- [ ] `test_dropping_emoji_for_sentiment_warns` — green
- [ ] `test_lowercasing_code_is_blocking` — green
- [ ] `test_topic_modelling_tolerates_aggressive_normalisation` — green
- [ ] `test_blocking_and_warning_are_different_categories` — green
- [ ] `test_an_unknown_task_lists_the_known_ones` — green
- [ ] `test_a_url_is_one_token` — green
- [ ] `test_url_matching_beats_the_word_pattern` — green
- [ ] **Put the word pattern first, watched the URL shatter** ← do not skip
- [ ] `test_hashtags_and_mentions_survive` — green
- [ ] `test_numbers_keep_their_separators` — green
- [ ] `test_internal_apostrophes_are_kept` — green
- [ ] `test_hyphenated_words_stay_together` — green
- [ ] `test_whitespace_tokenisation_fails_on_the_same_input` — green
- [ ] `test_whitespace_tokenisation_fails_entirely_on_japanese` — green
- [ ] `test_an_unknown_pattern_raises` — green
- [ ] `test_the_docstring_points_at_a_library` — green
- [ ] `test_each_normalisation_step_shrinks_the_vocabulary` — green
- [ ] `test_reductions_are_relative_to_the_first_spec` — green
- [ ] `test_the_note_says_each_merge_is_a_decision` — green
- [ ] `test_vocabulary_impact_needs_something_to_compare` — green
- [ ] `test_tokenisers_disagree_and_the_gap_is_measured` — green
- [ ] `test_identical_tokenisers_agree_perfectly` — green
- [ ] `test_the_agreement_note_says_there_is_no_correct_answer` — green
- [ ] `test_agreement_needs_two_tokenisers` — green
- [ ] `test_an_unrecorded_non_default_spec_is_refused` — green
- [ ] `test_a_recorded_spec_passes` — green
- [ ] `test_the_documented_default_needs_no_record` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is `split()` not a tokeniser?
- [ ] Name three things lowercasing destroys, and one task where that is fatal
- [ ] Why must unicode normalisation come first?
- [ ] Why must URLs match before the word pattern?
- [ ] Why is there no "correct" tokenisation?
- [ ] What does changing tokeniser do to your downstream features?
- [ ] Give three task/normalisation pairs from the table
- [ ] Why must the normalisation spec be recorded?

## Commit

- [ ] `./m check && ./m done 117` succeeded
