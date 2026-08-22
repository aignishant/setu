# Day 114 — CHECKLIST

**IDs covered:** ML-25 · **Principles served:** 1, 7, 8, 10 · **Artifact:** ADR-008

## Demo command

```bash
uv run python days/day-114/lab/explain.py
uv run python -m pytest tests/test_ensembles.py -v
```

Expected: the eight-part report ending with the five parts of a defensible claim, then all ensemble
tests green.

## Setup

- [ ] `./m start 114` and `./m scaffold 114` run
- [ ] `uv add "shap==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-114/lab/explain.py`,
      `docs/adr/ADR-008-what-the-model-keys-on.md`

## ML-25 — the guarantee

- [ ] Ran `the_additivity_guarantee()`
- [ ] Recorded the max reconstruction error: ______
- [ ] Can say what local accuracy means, and why it is exact
- [ ] Can say what space the values sum in, and what breaks under the sigmoid

## Explaining one decision

- [ ] Ran `explaining_one_decision()` on the most confident row
- [ ] Can say what SHAP gives that permutation importance cannot
- [ ] Can say what the contributions are measured **relative to**

## The baseline

- [ ] Ran `the_baseline_is_a_choice()` with three references
- [ ] Recorded three different values for the same feature and row
- [ ] Can state why a bare φ number is incomplete
- [ ] Can write a complete contribution claim in one sentence

## Correlated features

- [ ] Ran `correlated_features_split_the_credit()`
- [ ] Recorded mean |SHAP| for `signal_a` ______ and `copy_of_a` ______
- [ ] Can say what determines how the credit splits
- [ ] Can name the earlier day with the same problem
- [ ] Can state the reading rule for correlated groups

## Debugging

- [ ] Ran `shap_finds_the_leak()` and saw an ID column dominate
- [ ] Recorded the test accuracy that looked fine: ______
- [ ] Can say why this is SHAP's most valuable use
- [ ] Can say what SHAP is doing **correctly** in that case
- [ ] Ran `interactions_are_visible()` and saw φ(a) flip sign with b
- [ ] Can say why a single global importance number misses that

## What it does not tell you

- [ ] Read `what_shap_does_not_tell_you()`; can give all four
- [ ] Can state the intervention caveat precisely
- [ ] Read `a_defensible_explanation()`; can list all five parts

## Build brief

- [ ] `shap_values` — **TODO(me)**: verifies additivity, records the space
- [ ] `explain_row` — **TODO(me)**: `baseline_description` **required**, no causal language
- [ ] `grouped_shap` — **TODO(me)**: sums **raw** φ before taking absolutes
- [ ] `shap_stability` — **TODO(me)**: flags unstable rankings
- [ ] `shap_leak_screen` — **TODO(me)**: asks human questions, verdict is not definite
- [ ] `explanation_claim` — **TODO(me)**: refuses without all four parts
- [ ] Can explain why summing absolutes first is wrong

## Tests that must be able to fail

- [ ] `test_the_contributions_sum_to_the_prediction` — green ← **today's real assessment**
- [ ] `test_a_broken_additivity_guarantee_raises` — green
- [ ] `test_the_values_are_recorded_as_log_odds` — green
- [ ] `test_unknown_columns_are_named` — green
- [ ] `test_a_row_explanation_states_its_baseline` — green
- [ ] `test_an_explanation_without_a_baseline_is_refused` — green
- [ ] **Made `baseline_description` optional, watched the statement become unquotable** ← do not skip
- [ ] `test_the_row_statement_avoids_causal_language` — green
- [ ] `test_the_truncated_contributions_still_reconcile` — green
- [ ] `test_contributions_are_signed` — green
- [ ] `test_correlated_features_split_the_credit` — green
- [ ] `test_grouping_recovers_the_joint_importance` — green
- [ ] `test_grouping_sums_raw_values_not_absolutes` — green
- [ ] **Took absolutes before summing, watched the cancelling pair report 3.0** ← do not skip
- [ ] `test_an_unassigned_column_is_reported` — green
- [ ] `test_credit_splitting_is_warned_about` — green
- [ ] `test_shap_finds_a_planted_leak` — green
- [ ] `test_a_clean_model_has_no_suspected_leak` — green
- [ ] `test_the_leak_screen_asks_human_questions` — green
- [ ] `test_the_leak_verdict_is_not_definite` — green
- [ ] `test_an_unstable_ranking_is_flagged` — green
- [ ] `test_the_stability_warning_denies_it_is_a_finding` — green
- [ ] `test_stability_needs_enough_resamples` — green
- [ ] `test_a_complete_claim_is_defensible` — green
- [ ] `test_a_claim_without_a_baseline_is_not_defensible` — green
- [ ] `test_a_claim_without_grouping_is_not_defensible` — green
- [ ] `test_a_claim_without_stability_is_not_defensible` — green
- [ ] `test_the_claim_names_the_model_and_avoids_causal_language` — green
- [ ] `test_a_claim_with_no_model_is_refused` — green
- [ ] `test_adr_008_exists_and_records_what_the_model_keys_on` — green
- [ ] `test_adr_008_states_the_baseline` — green
- [ ] `test_adr_008_disclaims_causation` — green

## ADR-008 (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** — the model from Day 106's card, and why explanation is needed
- [ ] **What SHAP says** — grouped, stability-checked, with the **baseline stated**
- [ ] **What we checked** — additivity, grouping, stability, leak screen
- [ ] **What we believe and what we do not** — explicitly not causal
- [ ] Screen findings recorded, with the human questions **answered**
- [ ] **Consequences** — what you will monitor, what would trigger a retrain
- [ ] **What would change our minds**
- [ ] Cold-read a day later and signed

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the additivity guarantee, and the space it holds in
- [ ] What can SHAP explain that permutation importance cannot?
- [ ] Why is a φ value meaningless without its baseline?
- [ ] How do correlated features split credit, and what decides the split?
- [ ] Why is SHAP's best use debugging rather than explanation?
- [ ] What does SHAP say about an intervention?
- [ ] Why must correlated groups be summed raw rather than in absolute value?
- [ ] Give the five parts of a defensible explanation claim

## Commit

- [ ] `./m check && ./m done 114` succeeded
