# Day 100 — CHECKLIST

**IDs covered:** ML-11 · **Principles served:** 1, 7, 10

## Demo command

```bash
uv run python days/day-100/lab/confusion.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the cost table and the base-rate collapse, then all model
tests green.

## Setup

- [ ] `./m start 100` and `./m scaffold 100` run
- [ ] `days/day-100/lab/confusion.py` created
- [ ] No new packages installed

## ML-11 — the four boxes

- [ ] Drew the confusion matrix from memory, with the four labels
- [ ] Wrote precision and recall as formulas without looking
- [ ] Can say which box precision ignores, and which recall ignores
- [ ] Can say why that is the reason they trade off

## Accuracy

- [ ] Ran `accuracy_is_usually_the_wrong_default()`
- [ ] Recorded the useless model's accuracy ______ vs the real model's ______
- [ ] Can say what accuracy actually measures on imbalanced data
- [ ] Can state Day 78's rule

## The trade-off

- [ ] Ran `precision_and_recall_trade_off()` across seven thresholds
- [ ] Confirmed nothing about the **model** changed between rows
- [ ] Can say what lowering the threshold does to each metric

## F1 and F-beta

- [ ] Ran `f1_assumes_the_errors_cost_the_same()`
- [ ] Can say what the harmonic mean punishes, with the 0.99/0.01 example
- [ ] Can state the **claim** F1 makes
- [ ] Can say what `beta > 1` and `beta < 1` each favour

## Start from the cost

- [ ] Ran `start_from_the_cost()`; recorded the cheapest threshold: ______
- [ ] Recorded the theoretical optimum: ______
- [ ] Can **derive** `cost_fp/(cost_fp+cost_fn)` from expected cost
- [ ] Can say when 0.5 is the right threshold

## The base rate

- [ ] Ran `precision_depends_on_the_base_rate()` and read both columns
- [ ] Confirmed recall never moved
- [ ] Can name the Day-63 result this is identical to
- [ ] Can state **both** consequences

## Choosing, and multiclass

- [ ] Read `which_metric_when()`; can say what the last row means
- [ ] Ran `multiclass_needs_an_averaging_choice()`
- [ ] Can say what micro, macro and weighted each do
- [ ] Can say which one flatters you when the rare class matters

## Build brief

- [ ] `confusion` — **TODO(me)**: baseline and lift, degenerate cases named, warnings
- [ ] `f_beta` — **TODO(me)**: states its assumption
- [ ] `optimal_threshold` — **TODO(me)**: theoretical **and** empirical, reports cost of 0.5
- [ ] `choose_metric` — **TODO(me)**: known costs beat every proxy
- [ ] `precision_at_base_rate` — **TODO(me)**: **reuses Day 63**
- [ ] `describe_classification` — **TODO(me)**: baseline beside accuracy, base rate with precision
- [ ] Can explain why `at_default` is reported

## Tests that must be able to fail

- [ ] `test_the_four_counts_match_sklearn` — green
- [ ] `test_precision_ignores_false_negatives` — green
- [ ] `test_recall_ignores_false_positives` — green
- [ ] `test_a_useless_model_gets_a_low_lift` — green
- [ ] `test_an_imbalanced_target_warns_about_accuracy` — green
- [ ] `test_a_degenerate_precision_is_zero_not_nan` — green
- [ ] `test_the_degenerate_case_names_which_metric_broke` — green
- [ ] `test_a_perfect_classifier_scores_one` — green
- [ ] `test_confusion_rejects_a_non_binary_target` / `..._length_mismatch` — green
- [ ] `test_f1_punishes_imbalance_between_precision_and_recall` — green
- [ ] `test_f1_matches_sklearn` — green
- [ ] `test_beta_above_one_favours_recall` / `test_beta_below_one_favours_precision` — green
- [ ] `test_f1_states_that_equal_weighting_is_an_assumption` — green
- [ ] `test_f_beta_handles_the_zero_case` / `..._rejects_a_bad_beta` — green
- [ ] `test_the_optimal_threshold_follows_the_cost_ratio` — green ← **today's real assessment**
- [ ] **Searched a grid instead of deriving it, watched the theoretical assertion go red** ← do not skip
- [ ] `test_a_costlier_miss_lowers_the_threshold` — green
- [ ] `test_equal_costs_give_a_threshold_of_a_half` — green
- [ ] `test_the_cost_of_using_the_default_is_reported` — green
- [ ] `test_optimal_threshold_rejects_negative_costs` — green
- [ ] `test_recall_is_unaffected_by_the_base_rate` — green
- [ ] `test_precision_collapses_as_positives_get_rarer` — green
- [ ] `test_it_reuses_day_63s_arithmetic` — green
- [ ] **Reimplemented it inline, watched the monkeypatch test go red, reused Day 63** ← do not skip
- [ ] `test_known_costs_beat_every_proxy_metric` — green
- [ ] `test_accuracy_is_never_chosen_for_imbalanced_data` — green
- [ ] `test_capacity_gives_precision_at_k` — green
- [ ] `test_f1_comes_with_its_assumption_flagged` — green
- [ ] `test_the_reason_cites_the_situation_not_the_definition` — green
- [ ] `test_choose_metric_rejects_an_impossible_rate` — green
- [ ] `test_the_description_reports_the_baseline_beside_accuracy` — green
- [ ] `test_the_description_refuses_to_call_a_no_lift_model_accurate` — green
- [ ] `test_a_precision_claim_requires_a_base_rate` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Draw the four boxes and define precision and recall
- [ ] Which box does each ignore, and why does that matter?
- [ ] Why is accuracy usually the wrong metric?
- [ ] What claim does F1 make, and when is it false?
- [ ] Derive the cost-optimal threshold formula
- [ ] When is 0.5 correct?
- [ ] Why does precision depend on the base rate when recall does not?
- [ ] What are the two consequences of that for deployment?

## Commit

- [ ] `./m check && ./m done 100` succeeded
