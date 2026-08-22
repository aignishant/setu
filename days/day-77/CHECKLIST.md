# Day 77 — CHECKLIST

**IDs covered:** FE-02 · **Principles served:** 1, 7, 9, 11

## Demo command

```bash
uv run python days/day-77/lab/outliers.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the eight-part report including the masking table, then all feature tests green.

## Setup

- [ ] `./m start 77` and `./m scaffold 77` run
- [ ] `days/day-77/lab/outliers.py` created
- [ ] No new packages installed

## FE-02 — four kinds

- [ ] Can name all four kinds of unusual value and the action each deserves
- [ ] Can say which one causes the most damage when mishandled
- [ ] Can give a real example of the "second population" case

## Detection methods

- [ ] Ran `z_score_masking()` and **read the whole table**
- [ ] Confirmed 10 identical extremes were flagged **zero** times
- [ ] Can define masking in one sentence
- [ ] Confirmed the robust version caught all ten
- [ ] Ran `iqr_on_skewed_data()`; recorded the flag rate on normal ______ and lognormal ______
- [ ] Can say where the 1.5 multiplier comes from
- [ ] Ran `transform_first()`; recorded the before/after flag rates
- [ ] Can state why raising the threshold is the wrong fix
- [ ] Ran `isolation_forest_sees_combinations()`
- [ ] Can explain what a univariate rule structurally cannot see
- [ ] Can say what `contamination` actually does

## Decisions

- [ ] Ran `what_removal_does_to_your_answer()`; recorded all three p-values
- [ ] Can name the Day-74 hack this is
- [ ] Can state the two conditions that make removal legitimate
- [ ] Ran `winsorising_keeps_the_row()`
- [ ] Can say what removal throws away that winsorising does not
- [ ] Ran `the_leakage_rule()`; can say what fitting fences on test does

## Build brief

- [ ] `fit_outlier_rule` — **TODO(me)**: robust default, `log_first`, warns on heavy flagging
- [ ] `apply_outlier_rule` — **TODO(me)**: `flag` default, full audit record, applies only
- [ ] `outlier_diagnosis` — **TODO(me)**: can return **'unclear'**, recommends transform for tails
- [ ] `removal_impact` — **TODO(me)**: warns when the answer moves
- [ ] `assert_rule_was_prespecified` — **TODO(me)**: connects to Day 75's plan
- [ ] Can explain why `flag` is the default action

## Tests that must be able to fail

- [ ] `test_robust_zscore_is_the_default` — green
- [ ] `test_flag_is_the_default_action` — green
- [ ] `test_plain_zscore_masks_repeated_outliers` — green ← **today's real assessment**
- [ ] **Made the default plain z-score, watched the masking assertion go red, reverted** ← do not skip
- [ ] `test_iqr_flags_about_point_seven_percent_of_normal_data` — green
- [ ] `test_iqr_over_flags_skewed_data` — green
- [ ] `test_log_first_fixes_the_over_flagging` — green
- [ ] `test_heavy_flagging_is_warned_about` — green
- [ ] `test_flag_removes_nothing` — green
- [ ] `test_winsorise_caps_but_keeps_the_row` — green
- [ ] `test_remove_is_the_only_action_that_loses_rows` — green
- [ ] `test_the_record_is_a_complete_audit_trail` — green
- [ ] `test_train_bounds_are_applied_not_refitted` — green
- [ ] `test_apply_never_fits` — green
- [ ] **Recomputed percentiles inside `apply`, watched it go red, removed them** ← do not skip
- [ ] `test_isolation_forest_catches_a_combination_univariate_rules_miss` — green
- [ ] `test_diagnosis_recognises_impossible_values` — green
- [ ] `test_diagnosis_recognises_a_heavy_tail` — green (recommends transform, not removal)
- [ ] `test_diagnosis_can_say_unclear` — green
- [ ] `test_removal_that_changes_the_answer_is_warned_about` — green
- [ ] `test_a_harmless_removal_is_not_warned_about` — green
- [ ] `test_the_rule_must_be_prespecified` — green
- [ ] `test_an_unspecified_rule_is_rejected` — green, message names the hack
- [ ] `test_unknown_method_and_action_raise` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name the four kinds of unusual value and the right action for each
- [ ] What is masking, and which method suffers from it?
- [ ] Why do symmetric fences fail on skewed data, and what is the fix?
- [ ] What can an isolation forest see that IQR cannot?
- [ ] What does `contamination` control?
- [ ] What does removal cost that winsorising does not?
- [ ] Why must the outlier rule be fitted on train only?
- [ ] What makes "we removed outliers" legitimate rather than a hack?

## Commit

- [ ] `./m check && ./m done 77` succeeded
