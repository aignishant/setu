# Day 79 — CHECKLIST

**IDs covered:** FE-04 · **Principles served:** 1, 7, 8, 15

## Demo command

```bash
uv run python days/day-79/lab/splitting.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the eight-part report ending with the seven-step safe order, then all feature tests green.

## Setup

- [ ] `./m start 79` and `./m scaffold 79` run
- [ ] `days/day-79/lab/splitting.py` created
- [ ] No new packages installed

## FE-04 — leakage has no symptom

- [ ] Ran `leakage_has_no_symptom()` on a **random** target
- [ ] Recorded leaky accuracy ______ vs honest ______ vs chance 0.500
- [ ] Can state why nothing errored or warned
- [ ] Can say why this needs a structural guard rather than a reminder

## The three sets

- [ ] Built train/val/test and checked the fractions
- [ ] Caught the `test_size` off-by-one on the second split
- [ ] Can say what each set is **for**, in one phrase each
- [ ] Chose a hyperparameter on validation and looked at test **once**
- [ ] Can say why refitting on train+val afterwards is legitimate

## Stratified

- [ ] Ran `stratify_when_the_class_is_rare()` across five seeds
- [ ] Recorded the range of test positive counts: ______ to ______
- [ ] Can say why that looks like model instability and is not
- [ ] Confirmed `stratify=y` removed the variation

## Grouped — the one people miss

- [ ] Ran `group_leakage_is_the_one_people_miss()`
- [ ] Recorded random-split R² ______ vs grouped R² ______
- [ ] Confirmed **zero** group overlap under the grouped split
- [ ] Can explain what the random-split model actually learned
- [ ] Can name five kinds of data that need a grouped split

## Time

- [ ] Ran `time_makes_random_splitting_invalid()`
- [ ] Can say what a random split does that is not a real task
- [ ] Inspected `TimeSeriesSplit` folds; confirmed train always precedes test
- [ ] Noted the growing training window

## Cross-validation and the test set

- [ ] Compared `StratifiedKFold` and `GroupKFold` fold compositions
- [ ] Know which combination needs `StratifiedGroupKFold`
- [ ] Can say why a CV mean needs its spread reported
- [ ] Ran `the_test_set_is_spent_by_looking()` on a **random** target
- [ ] Recorded the best test accuracy from 60 tries: ______
- [ ] Can name the Day-74 concept this is
- [ ] Read `the_only_safe_order()` and can recite all seven steps

## Build brief

- [ ] `choose_split` — **TODO(me)**: names the deciding evidence, warns about unnoticed groups
- [ ] `split_data` — **TODO(me)**: val fraction of the original, refuses unsorted time, zero group overlap
- [ ] `assert_no_overlap` — **TODO(me)**: index and group, names the offenders
- [ ] `assert_fit_before_apply` — **TODO(me)**: the guard; message says what the leak **does**
- [ ] `split_summary` — **TODO(me)**: warns on tiny test positive counts
- [ ] Can explain why this one guard replaces five earlier reminders

## Tests that must be able to fail

- [ ] `test_a_fitted_step_before_the_split_is_refused` — green ← **today's real assessment**
- [ ] **Made the message a bare refusal, watched it go red, explained the consequence** ← do not skip
- [ ] `test_the_correct_order_passes` — green
- [ ] `test_every_fitted_step_is_caught_before_the_split` — five green cases
- [ ] `test_a_missing_split_is_refused` — green
- [ ] `test_unfitted_steps_before_the_split_are_fine` — green
- [ ] **Made the guard block every pre-split step, watched this go red, narrowed it** ← do not skip
- [ ] `test_the_validation_fraction_is_of_the_original` — green
- [ ] `test_the_three_sets_partition_the_data` — green
- [ ] `test_no_index_appears_in_two_sets` / `test_overlap_is_detected` — green
- [ ] `test_a_grouped_split_shares_no_groups` — green
- [ ] `test_group_overlap_is_detected` — green
- [ ] `test_a_random_split_does_share_groups` — green ← confirms the failure exists
- [ ] `test_stratification_preserves_the_rare_class` — green
- [ ] `test_a_random_split_does_not_preserve_it` — green
- [ ] `test_a_time_split_never_trains_on_the_future` — green
- [ ] `test_an_unsorted_time_column_is_refused` — green
- [ ] `test_a_time_split_ignores_the_seed` — green
- [ ] `test_splits_are_reproducible` — green
- [ ] `test_impossible_fractions_are_refused` — green
- [ ] `test_choose_split_demands_time_when_a_time_column_exists` — green
- [ ] `test_choose_split_detects_a_repeated_group` — green
- [ ] `test_choose_split_warns_about_an_unnoticed_group_column` — green
- [ ] `test_choose_split_stratifies_a_rare_target` — green
- [ ] `test_the_reason_names_the_evidence` — green
- [ ] `test_a_tiny_positive_count_in_test_is_warned_about` — green
- [ ] `test_a_healthy_split_is_not_warned_about` — green
- [ ] `test_the_record_states_how_the_split_was_made` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does leakage need a structural guard rather than discipline?
- [ ] What is each of the three sets for, and what spends the test set?
- [ ] When is stratification necessary, and what goes wrong without it?
- [ ] Describe group leakage and what the model actually learns
- [ ] Why is a random split invalid on time-ordered data?
- [ ] What does an unsorted time column silently produce?
- [ ] Recite the seven-step safe order
- [ ] Which five earlier days does today's guard retire?

## Commit

- [ ] `./m check && ./m done 79` succeeded
