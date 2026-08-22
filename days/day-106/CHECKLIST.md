# Day 106 — CHECKLIST · **PHASE 12 GATE**

**IDs covered:** ML-17 · **Principles served:** 1, 7, 8, 10, 15 · **Artifacts:** model card + ADR-007

## Demo command

```bash
uv run python days/day-106/lab/search.py
uv run python -m pytest tests/test_models.py -v
uv run python -m pytest -q
```

Expected: the eight-part report ending with what search cannot fix, then the whole suite green.

## Setup

- [ ] `./m start 106` and `./m scaffold 106` run
- [ ] `uv add "optuna==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-106/lab/search.py`, `reports/day106_model_card.md`,
      `docs/adr/ADR-007-model-choice.md`

## ML-17 — grid vs random

- [ ] Ran `why_random_beats_grid()`
- [ ] Can state the geometric argument in one sentence
- [ ] Can say what condition it depends on, and whether it usually holds
- [ ] Can say when grid search **is** the right choice
- [ ] Ran `the_three_strategies()` and compared fits, time and best score
- [ ] Confirmed the scaler was **inside** the pipeline
- [ ] Can say what happens if it is not

## Bayesian search

- [ ] Ran `bayesian_search()` with Optuna
- [ ] Compared the first five and last five trial scores
- [ ] Can say when Bayesian search is worth it
- [ ] Can say when it is not

## The optimism

- [ ] Ran `the_winners_curse_again()` across 40 configurations
- [ ] Recorded mean ______ best ______ sd ______ — best was ______ sd above the mean
- [ ] Can say what you actually found
- [ ] Ran `measuring_the_optimism()` at three budgets
- [ ] Confirmed optimism **grew** with `n_iter`
- [ ] Can say what more search buys, and what it costs

## Comparing families

- [ ] Ran `compare_the_families()` on at least four candidates
- [ ] Listed everything within one CV sd of the best
- [ ] Can state the one-standard-error rule
- [ ] Can say why you must state that the choice was made on simplicity

## The final evaluation

- [ ] Ran `the_final_evaluation()` and followed the four-step order
- [ ] Recorded CV ______ test ______ optimism ______ baseline ______
- [ ] Can recite the order from memory
- [ ] Can say what happens if you go back for another model afterwards
- [ ] Read `what_the_search_cannot_fix()`; can name all five and their days

## Build brief

- [ ] `search_space` — **TODO(me)**: log scales, notes name what matters
- [ ] `random_search` — **TODO(me)**: fresh model each time, reports `expected_optimism`
- [ ] `compare_models` — **TODO(me)**: one-standard-error rule, ordering gives simplicity
- [ ] `final_evaluation` — **TODO(me)**: reuses Day 100, statement carries the baseline
- [ ] `assert_test_set_untouched` — **TODO(me)**
- [ ] `model_card` — **TODO(me)**: refuses empty limitations or `not_for`
- [ ] Can explain why `C` and `gamma` must be sampled on a log scale

## Tests that must be able to fail

- [ ] `test_regularisation_parameters_are_log_scaled` — green
- [ ] **Sampled C uniformly, watched 99% of draws land above 1** ← do not skip
- [ ] `test_the_space_names_which_parameters_matter` — green
- [ ] `test_an_unknown_model_lists_the_known_ones` — green
- [ ] `test_random_search_returns_every_configuration` — green
- [ ] `test_a_fresh_model_is_built_per_configuration` — green
- [ ] `test_the_best_score_carries_an_optimism_estimate` — green
- [ ] `test_a_suspiciously_good_winner_is_flagged` — green
- [ ] `test_a_boundary_optimum_is_flagged` — green
- [ ] `test_random_search_rejects_a_tiny_budget` — green
- [ ] `test_random_search_is_reproducible` — green
- [ ] `test_the_simplest_model_wins_a_near_tie` — green ← **today's real assessment**
- [ ] `test_a_clearly_better_model_is_recommended_despite_complexity` — green
- [ ] **Made the rule always pick the simplest, watched the forest test go red** ← do not skip
- [ ] `test_the_reason_says_when_models_were_indistinguishable` — green
- [ ] `test_compare_needs_at_least_two_candidates` — green
- [ ] `test_the_final_evaluation_reports_optimism` — green
- [ ] `test_the_final_evaluation_reuses_day_100s_confusion` — green
- [ ] `test_the_statement_includes_the_baseline` — green
- [ ] `test_a_second_look_at_the_test_set_is_refused` — green
- [ ] `test_the_model_card_requires_stated_limitations` — green
- [ ] `test_the_model_card_requires_a_not_for_section` — green
- [ ] `test_the_model_card_requires_a_baseline` — green
- [ ] `test_the_model_card_states_why_the_threshold` — green
- [ ] `test_the_card_reports_the_baseline_beside_the_metric` — green
- [ ] `test_phase_12_models_module_is_complete` — green (61 functions)
- [ ] `test_the_model_card_file_exists_and_is_complete` — green
- [ ] `test_adr_007_justifies_the_choice` — green
- [ ] `test_adr_007_names_the_models_rejected` — green
- [ ] `test_adr_007_admits_the_simplest_model_might_win` — green

## The model card (gate artifact)

- [ ] `reports/day106_model_card.md` written
- [ ] **What it predicts** — and what a prediction is used for
- [ ] **Training data** — source, dates, split, known collection biases
- [ ] **How it was chosen** — families, budget, CV scores, one-SE rule if applied
- [ ] **Performance** — test metric **and** baseline, plus the CV optimism
- [ ] **Threshold** — the number, and why, from the cost of each error
- [ ] **Calibration** — whether it is, and whether that matters here
- [ ] **Limitations** — at least three, specific
- [ ] **Not for** — where it must not be used, and why

## ADR-007 (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** — task, metric, and what the baseline achieves
- [ ] **Options** — every family from Days 99–105, with score **and** cost
- [ ] **Decision** — one model, one sentence
- [ ] **Why not the others** — including any rejected on simplicity
- [ ] **Consequences** — retraining, calibration, monitoring
- [ ] **What would change our minds**
- [ ] Cold-read a day later and signed

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give the geometric argument for random over grid search
- [ ] Why must `C` and `gamma` be sampled on a log scale?
- [ ] What have you actually found when you report the best of 40 CV scores?
- [ ] Why does optimism grow with the search budget?
- [ ] Recite the tune → refit → test order, and say why each step is where it is
- [ ] What happens if you look at the test set a second time?
- [ ] State the one-standard-error rule and why it is not a bias toward simplicity
- [ ] Name three things hyperparameter search cannot fix

## PHASE 12 GATE

- [ ] `search.py` runs end to end
- [ ] Every search ran inside a pipeline, scaler **within** it
- [ ] The test set was scored **once**
- [ ] The CV estimate's optimism is reported as a number
- [ ] Families compared with the one-SE rule, and its result stated
- [ ] Model card complete, including a **not for** section
- [ ] ADR-007 written, naming at least three rejected families, cold-read
- [ ] `test_phase_12_models_module_is_complete` green (61 functions)
- [ ] Every Day 97 split guard and Day 100 metric test still green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 106` succeeded and `./m status` shows Phases 0–12 complete
