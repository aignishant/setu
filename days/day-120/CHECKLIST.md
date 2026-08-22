# Day 120 — CHECKLIST

**IDs covered:** NLP-06 · **Principles served:** 1, 7, 8, 9

## Demo command

```bash
uv run python days/day-120/lab/ner.py
uv run python -m pytest tests/test_nlp.py -v
```

Expected: the nine-part report ending with when NER is the wrong tool, then all nlp tests green.

## Setup

- [ ] `./m start 120` and `./m scaffold 120` run
- [ ] `days/day-120/lab/ner.py` created
- [ ] No new packages installed

## NLP-06 — spans, not tokens

- [ ] Ran `what_ner_finds()` and read the character offsets
- [ ] Can say what an entity is, precisely
- [ ] Can explain the three-way `Washington` ambiguity
- [ ] Ran `bio_encoding()`; can define B, I and O
- [ ] Can say what the `B` does for two adjacent same-type entities

## Why token accuracy lies

- [ ] Ran `o_dominates_and_accuracy_lies()`
- [ ] Recorded the O rate: ______
- [ ] Recorded what an all-O model scores: ______
- [ ] Can say how many entities that model extracts
- [ ] Can name the two earlier days whose rules apply here
- [ ] Can say why a token accuracy in an NER write-up is a red flag

## Entity-level evaluation

- [ ] Ran `entity_level_evaluation()` under both schemes
- [ ] Recorded strict F1 ______ and lenient F1 ______
- [ ] Can say what a boundary error costs under strict matching
- [ ] Can state which scheme is "correct"
- [ ] Can say what **is** wrong about reporting one

## Boundaries and case

- [ ] Ran `boundaries_are_the_hard_part()`
- [ ] Can say what kind of error models actually make
- [ ] Can say why flat BIO cannot handle `The New York Times`
- [ ] Ran `case_is_the_strongest_feature()` on four variants
- [ ] Recorded entities found lowercased ______ and uppercased ______
- [ ] Can explain why **ALL-CAPS** hurts too
- [ ] Can name three deployment contexts where this bites

## The baseline

- [ ] Ran `a_gazetteer_baseline()`
- [ ] Can say what a gazetteer's precision and recall look like
- [ ] Can name a situation where it beats a model outright
- [ ] Can name its two failure modes

## Privacy

- [ ] Read `ner_output_is_personal_data()`
- [ ] Can say what NER over customer email actually creates
- [ ] Can give all four questions to answer first
- [ ] Can state Setu's own recorded rule
- [ ] Read `when_ner_is_the_wrong_tool()`; can distinguish NER from linking and relation extraction

## Build brief

- [ ] `bio_to_spans` — **TODO(me)**: records invalid tags, separates adjacent entities
- [ ] `spans_to_bio` — **TODO(me)**: round-trips, refuses overlaps
- [ ] `entity_scores` — **TODO(me)**: both schemes, **statement names the scheme**
- [ ] `token_accuracy_is_misleading` — **TODO(me)**: points at entity metrics
- [ ] `gazetteer_match` — **TODO(me)**: longest-match, word boundaries
- [ ] `case_sensitivity_report` — **TODO(me)**: warning names the deployment risk
- [ ] `assert_ner_target_is_permitted` — **TODO(me)**: Principle 9 gate
- [ ] Can explain why an orphan `I-` tag must be recorded rather than dropped

## Tests that must be able to fail

- [ ] `test_bio_decodes_a_multi_token_entity` — green
- [ ] `test_adjacent_entities_of_the_same_type_stay_separate` — green
- [ ] **Ignored the B and watched two people merge into one** ← do not skip
- [ ] `test_an_orphan_inside_tag_is_recorded_not_dropped` — green
- [ ] `test_a_type_change_mid_entity_starts_a_new_span` — green
- [ ] `test_bio_rejects_a_length_mismatch` / `..._malformed_label` — green
- [ ] `test_bio_round_trips` — green
- [ ] `test_overlapping_spans_are_refused` — green
- [ ] `test_a_span_outside_the_token_range_raises` — green
- [ ] `test_a_boundary_error_costs_twice_under_strict_matching` — green ← **today's real assessment**
- [ ] `test_lenient_matching_accepts_the_same_boundary_error` — green
- [ ] `test_the_two_schemes_give_very_different_scores` — green
- [ ] `test_the_statement_names_the_scheme` — green
- [ ] **Quoted a lenient F1 without naming the scheme, watched it go red** ← do not skip
- [ ] `test_lenient_matching_does_not_double_count_a_gold_span` — green
- [ ] `test_a_wrong_label_is_never_a_match` — green
- [ ] `test_scores_are_broken_down_by_type` — green
- [ ] `test_a_perfect_prediction_scores_one` / `test_an_unknown_scheme_raises` — green
- [ ] `test_predicting_o_everywhere_scores_high_token_accuracy` — green
- [ ] `test_the_warning_points_at_entity_level_metrics` — green
- [ ] `test_the_entity_token_rate_is_reported` — green
- [ ] `test_token_accuracy_needs_labels` — green
- [ ] `test_the_gazetteer_prefers_the_longest_match` — green
- [ ] `test_the_gazetteer_respects_word_boundaries` — green
- [ ] **Dropped word boundaries and watched `Apple` match `Applecart`** ← do not skip
- [ ] `test_the_gazetteer_has_perfect_precision_on_known_names` — green
- [ ] `test_the_gazetteer_has_zero_recall_on_unknown_names` — green
- [ ] `test_an_ambiguous_gazetteer_entry_is_warned_about` — green
- [ ] `test_an_unknown_entity_type_lists_the_known_ones` — green
- [ ] `test_a_case_dependent_extractor_is_flagged` — green
- [ ] `test_the_case_warning_names_the_deployment_risk` — green
- [ ] `test_a_case_insensitive_extractor_is_not_flagged` — green
- [ ] `test_case_report_needs_texts` — green
- [ ] `test_extracting_people_from_user_input_is_refused` — green
- [ ] `test_an_extracted_person_list_needs_a_destination` — green
- [ ] `test_setus_own_rule_passes` — green
- [ ] `test_non_person_extraction_is_unrestricted` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does NER label spans rather than tokens?
- [ ] What does an all-O model score, and what does it extract?
- [ ] What does a boundary error cost under strict matching, and why?
- [ ] What is wrong with quoting an F1 without its scheme?
- [ ] Why does uppercasing hurt NER as much as lowercasing?
- [ ] Name three deployment contexts where NER underperforms its benchmark
- [ ] When does a gazetteer beat a model?
- [ ] What does NER over customer text create, and what must you decide first?

## Commit

- [ ] `./m check && ./m done 120` succeeded
