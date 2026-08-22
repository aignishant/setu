# Day 124 — CHECKLIST · **PHASE 14 GATE**

**IDs covered:** NLP-12 · **Principles served:** 1, 7, 8, 10, 15
**Artifact:** a baseline card that governs Phases 15–19

## Demo command

```bash
uv run python days/day-124/lab/classify.py
uv run python -m pytest tests/test_nlp.py -v
uv run python -m pytest -q
```

Expected: the ten-part report ending with the written baseline file, then the whole suite green.

## Setup

- [ ] `./m start 124` and `./m scaffold 124` run
- [ ] Files created: `days/day-124/lab/classify.py`, `reports/day124_baseline_card.md`
- [ ] **`SOURCE.md` row added** — source, licence, dates, how the labels were produced

## The leak check — do this first

- [ ] Ran `the_structural_leak_first()` **before any modelling**
- [ ] Recorded F1 with metadata ______ and without ______
- [ ] Can say what the headers contained
- [ ] Can state Day 87's provenance question in text form
- [ ] Can name three other corpora shapes with the same problem

## The baseline before the baseline

- [ ] Ran `the_baseline_baseline()`
- [ ] Recorded majority-class accuracy ______ and macro F1 ______
- [ ] Can say why the two differ
- [ ] Can say which is the honest choice, and when

## No leaks

- [ ] Ran `the_pipeline_prevents_the_leak()`
- [ ] Recorded feature counts fitted both ways
- [ ] Can say what the Pipeline guarantees inside cross-validation
- [ ] Can say why the manual version produces no error

## Tuning

- [ ] Ran `tune_the_baseline_properly()` over ≥ 20 configurations
- [ ] Recorded best CV macro-F1 ______ and the spread ______ – ______
- [ ] Can say why an untuned baseline is unfair, and name the day
- [ ] Can say why `best_score_` is optimistic
- [ ] Ran `compare_the_linear_models()` across five models
- [ ] Recorded which were within one CV sd of the best
- [ ] Can say what `LinearSVC` lacks, and what to do about it
- [ ] Can say what `ComplementNB` is designed for

## The final evaluation

- [ ] Followed Day 106's four-step order
- [ ] Recorded CV ______ test ______ optimism ______ baseline ______
- [ ] **Read the per-class column**
- [ ] Can say what a good macro-F1 can hide

## Cost

- [ ] Ran `what_this_costs_to_run()`
- [ ] Recorded fit time ______ model size ______ ms/doc ______ GPU ______
- [ ] Can say why this column matters for every later phase
- [ ] Ran `what_the_model_learned()`
- [ ] Read the top features **critically** for leak signals
- [ ] Can say why no SHAP is needed here

## Limitations

- [ ] Read `where_this_baseline_fails()`; can name **all six**
- [ ] Can say why naming them is honest rather than defensive
- [ ] Wrote `reports/day124_baseline.json` including the **search budget**

## Build brief

- [ ] `structural_leak_screen` — **TODO(me)**: human questions, non-definite verdict
- [ ] `majority_baseline` — **TODO(me)**: reports the accuracy/macro-F1 gap
- [ ] `build_text_pipeline` — **TODO(me)**: vectoriser inside, honest about probabilities
- [ ] `tune_baseline` — **TODO(me)**: reports `score_spread`, warns on a small budget
- [ ] `baseline_card` — **TODO(me)**: refuses < 10 configurations and < 4 limitations
- [ ] `compare_against_baseline` — **TODO(me)**: recommends the baseline within noise
- [ ] Can explain why the cost ratio must be surfaced rather than buried

## Tests that must be able to fail

- [ ] `test_a_planted_structural_leak_is_found` — green
- [ ] `test_a_clean_corpus_raises_no_suspicion` — green
- [ ] `test_the_leak_screen_asks_human_questions` — green
- [ ] `test_the_leak_verdict_is_not_definite` — green
- [ ] `test_the_screen_rejects_a_length_mismatch` — green
- [ ] `test_accuracy_and_macro_f1_disagree_on_imbalanced_data` — green
- [ ] `test_macro_f1_is_recommended_when_the_gap_is_large` — green
- [ ] `test_a_balanced_corpus_shows_a_small_gap` — green
- [ ] `test_the_baseline_statement_calls_itself_a_baseline` — green
- [ ] `test_majority_baseline_needs_a_test_set` — green
- [ ] `test_the_vectoriser_lives_inside_the_pipeline` — green
- [ ] `test_the_pipeline_refits_the_vectoriser_per_fold` — green
- [ ] **Vectorised before splitting and watched no error appear** ← do not skip
- [ ] `test_linear_svc_provides_no_probabilities` — green
- [ ] `test_requesting_probabilities_wraps_the_model` — green
- [ ] `test_logistic_regression_provides_probabilities_directly` — green
- [ ] `test_an_unknown_model_lists_the_known_ones` — green
- [ ] `test_tuning_moves_the_score_substantially` — green ← **today's real assessment**
- [ ] **Used `TfidfVectorizer()` defaults and compared the spread** ← do not skip
- [ ] `test_the_search_space_covers_the_parameters_that_matter` — green
- [ ] `test_a_small_search_budget_is_warned_about` — green
- [ ] `test_the_tuning_docstring_says_the_cv_score_is_optimistic` — green
- [ ] `test_tuning_needs_two_classes` — green
- [ ] `test_the_card_records_the_baseline_beside_the_score` — green
- [ ] `test_the_card_records_the_search_budget` — green
- [ ] `test_a_barely_tuned_baseline_is_refused` — green
- [ ] `test_too_few_limitations_are_refused` — green
- [ ] `test_a_missing_cost_key_is_named` — green
- [ ] `test_the_card_reports_the_optimism` — green
- [ ] `test_a_gain_within_noise_recommends_the_baseline` — green
- [ ] **Recommended the higher score regardless of noise, watched it go red** ← do not skip
- [ ] `test_a_real_gain_is_recognised` — green
- [ ] `test_the_cost_ratio_is_visible` — green
- [ ] `test_a_missing_card_raises` — green
- [ ] `test_the_baseline_file_exists_and_is_complete` — green
- [ ] `test_the_baseline_beats_the_majority_class` — green
- [ ] `test_the_baseline_card_report_is_complete` — green
- [ ] `test_the_card_names_the_leak_check` — green
- [ ] `test_phase_14_nlp_module_is_complete` — green (49 functions)
- [ ] `test_the_classifier_script_runs_end_to_end` — green

## The baseline card (gate artifact)

- [ ] **Corpus** — source, licence, dates, how labels were produced
- [ ] **Leak check** — what the screen found, what you removed and why
- [ ] **Split** — stratified, seeded; grouped if documents share an author or thread
- [ ] **Metric** — macro F1 with the majority baseline beside it
- [ ] **Search budget** — how many configurations, over what space
- [ ] **Result** — CV, test, optimism, **and per-class scores**
- [ ] **Cost** — fit time, model size, ms/document, GPU required
- [ ] **What the model learned** — top features, read for leak signals
- [ ] **Limitations** — at least four, specific
- [ ] **What would beat this** — named mechanisms, as the bridge into Phase 15

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why check for a structural leak before anything else?
- [ ] Why is accuracy the wrong metric here, and what replaces it?
- [ ] What does the Pipeline guarantee that manual vectorising does not?
- [ ] Name three ways a baseline can be built dishonestly
- [ ] Why must the search budget be recorded?
- [ ] What does "beating the baseline" require besides a higher score?
- [ ] Give four limitations of this baseline
- [ ] What would a later model have to do to genuinely win?

## PHASE 14 GATE

- [ ] `classify.py` runs in one command and exits 0
- [ ] Leak screen ran **first**; findings recorded
- [ ] Vectoriser **inside** the Pipeline, refitting per fold
- [ ] Baseline tuned over ≥ 20 configurations; spread reported
- [ ] Macro F1 with baseline; accuracy explicitly rejected if imbalanced
- [ ] Per-class scores reported
- [ ] Test set scored **once**; optimism stated
- [ ] Cost profile recorded in full
- [ ] Baseline card complete, four limitations, "what would beat this"
- [ ] `reports/day124_baseline.json` written for Phase 15
- [ ] `test_phase_14_nlp_module_is_complete` green (49 functions)
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 124` succeeded and `./m status` shows Phases 0–14 complete
