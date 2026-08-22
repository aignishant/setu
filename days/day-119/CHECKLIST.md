# Day 119 — CHECKLIST

**IDs covered:** NLP-05 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-119/lab/pos.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the nine-part report ending with what POS tags are for, then all nlp tests green.

## Setup

- [ ] `./m start 119` and `./m scaffold 119` run
- [ ] `days/day-119/lab/pos.py` created
- [ ] NLTK `treebank` and tagger data downloaded
- [ ] No new packages installed

## NLP-05 — sequence labelling

- [ ] Ran `context_decides_the_tag()` on the ambiguous pairs
- [ ] Can say what is structurally different from every model since Day 91
- [ ] Can name what this idea leads to in Phase 16

## The baseline

- [ ] Built the most-frequent-tag tagger **from scratch**
- [ ] Recorded its accuracy: ______
- [ ] Recorded the unseen-word rate: ______
- [ ] Can say what a tagger reporting 93% has actually added
- [ ] Can name the day whose rule this is

## Ambiguity

- [ ] Ran `ambiguity_report`-style analysis
- [ ] Recorded type ambiguity ______ and **token** ambiguity ______
- [ ] Can explain why the two differ so much
- [ ] Can say why that gap is the reason context matters

## Tagsets

- [ ] Ran `tagsets_are_not_universal()`
- [ ] Can say roughly how many tags Penn and Universal have
- [ ] Can name three Penn tags that Universal collapses into one
- [ ] Know which spaCy attribute gives which
- [ ] Can say what happens when the two are mixed

## The tag Day 118 needed

- [ ] Ran `the_tag_day_118_needed()` and **compared the last two columns**
- [ ] Recorded the lemma of `were` with and without a tag
- [ ] Can write the Penn→WordNet mapping from memory
- [ ] Can say what the fallback does, and that it is a guess
- [ ] Ran `spacy_does_it_in_one_pass()`; can say why it needs no mapping
- [ ] Can say what `is_stop` silently adopts

## Taggers as models

- [ ] Ran `taggers_disagree_and_cost_differently()`
- [ ] Recorded agreement between NLTK and spaCy: ______
- [ ] Can say whether the disagreements are random or systematic
- [ ] Ran `a_tagger_is_a_model_with_a_training_distribution()` on five domains
- [ ] Can say what happens to tagging when text is lowercased
- [ ] Can say what unknown words get tagged as
- [ ] Can state why the noun rate is a degradation signal **without labels**
- [ ] Read `what_pos_tags_are_actually_for()`; can give four uses
- [ ] Can say why tagger errors matter more than the accuracy suggests

## Build brief

- [ ] `penn_to_wordnet` — **TODO(me)**: reports `was_guessed`
- [ ] `tag_and_lemmatise` — **TODO(me)**: records guessed positions, warns above 10%
- [ ] `most_frequent_tag_baseline` — **TODO(me)**: statement calls itself a baseline
- [ ] `ambiguity_report` — **TODO(me)**: ranks by frequency, explains the type/token gap
- [ ] `tagset_of` — **TODO(me)**: names an unrecognised tag
- [ ] `assert_consistent_tagset` — **TODO(me)**: message explains the silent failure
- [ ] `tagger_domain_check` — **TODO(me)**: needs **no labels**, actionable recommendation
- [ ] Can explain why the domain check must not require labels

## Tests that must be able to fail

- [ ] `test_the_mapping_uses_the_first_letter` — green
- [ ] `test_a_mapped_tag_is_not_marked_as_guessed` — green
- [ ] `test_an_unmappable_tag_falls_back_and_says_so` — green
- [ ] `test_the_mapping_covers_the_documented_letters` — green
- [ ] `test_an_empty_tag_raises` — green
- [ ] `test_tagging_fixes_what_day_118_could_not` — green ← **today's real assessment**
- [ ] `test_the_no_tag_default_would_have_failed` — green
- [ ] **Dropped the tag and watched `were` stay `were`** ← do not skip
- [ ] `test_guessed_positions_are_recorded` — green
- [ ] `test_many_guessed_tags_are_warned_about` — green
- [ ] `test_tagging_an_empty_list_raises` — green
- [ ] `test_the_baseline_is_around_ninety_percent` — green
- [ ] `test_the_baseline_statement_calls_itself_a_baseline` — green
- [ ] `test_the_baseline_reports_its_unseen_rate` — green
- [ ] `test_the_baseline_needs_training_data` — green
- [ ] `test_token_ambiguity_far_exceeds_type_ambiguity` — green
- [ ] `test_the_ambiguity_note_explains_the_gap` — green
- [ ] `test_the_most_ambiguous_are_ranked_by_frequency` — green
- [ ] `test_ambiguity_needs_a_corpus` — green
- [ ] `test_penn_and_universal_tags_are_distinguished` — green
- [ ] `test_an_unrecognised_tag_is_named` — green
- [ ] `test_a_mixed_tag_sequence_is_refused` — green
- [ ] **Filtered for 'VERB' against Penn tags and watched it silently return nothing** ← do not skip
- [ ] `test_a_consistent_penn_sequence_passes` — green
- [ ] `test_a_consistent_universal_sequence_passes` — green
- [ ] `test_in_domain_text_passes_the_domain_check` — green
- [ ] `test_a_high_noun_rate_signals_degradation` — green
- [ ] `test_an_all_lowercase_corpus_is_flagged` — green
- [ ] `test_the_recommendation_is_actionable` — green
- [ ] `test_the_domain_check_needs_no_labels` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is POS tagging structurally different from Phase 12's models?
- [ ] What accuracy does a context-free baseline reach, and why does that matter?
- [ ] Why does token ambiguity exceed type ambiguity?
- [ ] Name the two tagsets and what happens when you mix them
- [ ] Write the Penn→WordNet mapping and say what the fallback assumes
- [ ] What does lowercasing do to a tagger, and why?
- [ ] How can you detect tagger degradation with no labelled data?
- [ ] Why do tagger errors matter more than the accuracy number suggests?

## Commit

- [ ] `./m check && ./m done 119` succeeded
