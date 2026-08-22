# Day 74 — CHECKLIST

**IDs covered:** ST-21 · **Principles served:** 1, 7, 10, 15

## Demo command

```bash
uv run python days/day-74/lab/phacking.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including four manufactured findings and the correction comparison,
then all stats tests green.

## Setup

- [ ] `./m start 74` and `./m scaffold 74` run
- [ ] `days/day-74/lab/phacking.py` created
- [ ] No new packages installed

## ST-21 — the arithmetic

- [ ] Read the FWER table; recorded P(any false positive) at 20 tests: ______
- [ ] Can state why this is compound probability, not a subtle statistical effect
- [ ] Can say what was NOT done wrong in any individual test

## The four hacks — run each one

- [ ] **Hack 1** many outcomes — recorded rate: ______ vs predicted ______
- [ ] **Hack 2** subgroups — recorded overall ______ vs any-subgroup ______
- [ ] Can quote the sentence this most often appears as
- [ ] **Hack 3** optional stopping — recorded the rate at three `max_n` values
- [ ] Can explain why the rate climbs toward 1 with more peeking
- [ ] Can name the two legitimate fixes for A/B tests
- [ ] **Hack 4** flexible analysis — recorded rate: ______
- [ ] Can name two of the five choices that sound entirely defensible
- [ ] Read `the_garden_of_forking_paths()` **twice**
- [ ] Can explain why "I only ran one test" is not by itself a defence

## Corrections

- [ ] Ran `bonferroni_and_bh()` and **read all three rows**
- [ ] Confirmed Bonferroni pinned P(any false positive) at ≈ 0.05
- [ ] Confirmed Bonferroni **missed** real effects
- [ ] Confirmed BH found more true positives at the cost of some false ones
- [ ] Can state what each method controls, in one sentence each
- [ ] Can say when FWER is right and when FDR is
- [ ] Ran `bh_is_a_step_up_procedure()` and traced the threshold table
- [ ] Can explain why BH rejects tests that failed their own threshold

## Honesty

- [ ] Read `what_honesty_looks_like()`
- [ ] Can name all five disclosure practices
- [ ] Can state the last one as a Principle-15 restatement

## Build brief

- [ ] `family_wise_error` — **TODO(me)**
- [ ] `correct_p_values` — **TODO(me)**: BH as a genuine **step-up** procedure, `none` warns
- [ ] `analysis_log` — **TODO(me)**: plan declared **before** any test
- [ ] `record_comparison` — **TODO(me)**: flags unplanned confirmatory tests, does not mutate
- [ ] `honest_summary` — **TODO(me)**: comparison count **in the statement**
- [ ] `optional_stopping_risk` — **TODO(me)**
- [ ] Can explain why naive per-test BH is wrong

## Tests that must be able to fail

- [ ] `test_the_family_wise_arithmetic` / `test_one_test_gives_alpha` — green
- [ ] `test_bonferroni_alpha_is_reported` — green
- [ ] `test_family_wise_rejects_bad_inputs` — green
- [ ] `test_bonferroni_divides_alpha` — green
- [ ] `test_bonferroni_adjusted_values_are_capped_at_one` — green
- [ ] `test_bh_is_a_step_up_procedure` — green ← **today's real assessment**
- [ ] **Implemented BH as a per-test comparison, watched it reject too few, fixed it** ← do not skip
- [ ] `test_bh_rejects_at_least_as_many_as_bonferroni` — green
- [ ] `test_bh_controls_the_false_discovery_rate` — green
- [ ] `test_bonferroni_controls_the_family_wise_rate` — green
- [ ] **Swapped which method was tested against which target, watched both go red** ← do not skip
- [ ] `test_uncorrected_fails_to_control_anything` — green
- [ ] `test_no_correction_carries_a_warning` — green
- [ ] `test_correction_rejects_invalid_p_values` — green
- [ ] `test_optional_stopping_inflates_the_error_rate` — green
- [ ] `test_more_peeking_is_worse` — green
- [ ] `test_a_single_look_is_honest` — green
- [ ] `test_optional_stopping_rejects_bad_inputs` — green
- [ ] `test_the_log_records_every_comparison` — green
- [ ] `test_an_unplanned_confirmatory_test_is_flagged` — green
- [ ] `test_an_unplanned_exploratory_test_is_fine` — green
- [ ] `test_record_does_not_mutate_the_log` — green
- [ ] `test_the_summary_states_how_many_comparisons_were_made` — green
- [ ] `test_the_summary_separates_confirmatory_from_exploratory` — green
- [ ] `test_exploratory_findings_are_flagged_as_needing_fresh_data` — green
- [ ] `test_correction_reduces_the_significant_count` — green
- [ ] `test_a_genuinely_strong_result_survives_correction` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does 20 tests give a 64% false-positive chance?
- [ ] Describe all four hacks and say why none requires a lie
- [ ] Why does optional stopping tend toward certainty?
- [ ] Explain the garden of forking paths
- [ ] What does Bonferroni control? What does BH control?
- [ ] When is each the right choice?
- [ ] Why is BH a step-up procedure, and what breaks without that?
- [ ] Why can exploratory findings not be confirmed on the same data?

## Commit

- [ ] `./m check && ./m done 74` succeeded
