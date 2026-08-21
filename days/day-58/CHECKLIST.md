# Day 58 — CHECKLIST

**IDs covered:** ST-01, ST-02 · **Principles served:** 1, 7, 10

## Demo command

```bash
uv run python days/day-58/lab/levels.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report ending with the dtype demonstration, then all stats tests green.

## Setup

- [ ] `./m start 58` and `./m scaffold 58` run
- [ ] `uv add "scipy==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-58/lab/levels.py` created

## ST-01 — sample and population

- [ ] Can define **statistic** and **parameter** and say which you can observe
- [ ] Ran the sample-size loop; watched the error shrink but **not smoothly**
- [ ] Ran it with a different seed and saw a small sample land closer than a large one once
- [ ] Ran `the_same_sample_twice()` and recorded the difference: ______
- [ ] Can say why "the groups differ" is never the finding
- [ ] Ran `sampling_bias_beats_sample_size()` and confirmed the 100× larger sample was worse
- [ ] Can state what a bigger sample fixes and what it does not
- [ ] Can give the same number as a descriptive claim and an inferential one

## ST-02 — levels of measurement

- [ ] Built the four-level frame and read the dtypes
- [ ] Computed `mean venue_id` and can say why it is meaningless
- [ ] Can say what that number does when it reaches a model as a feature
- [ ] Ran `ordinal_means_are_a_lie()`; confirmed a mean of 1.0 with **no** medium observations
- [ ] Can state the assumption an ordinal mean makes
- [ ] Can name the Day-88 project this affects
- [ ] Can explain why 20 °C is not twice 10 °C
- [ ] Know how to convert `year` (interval) into something ratio-valid
- [ ] Read the permitted-statistics table and can say how the level chooses the test
- [ ] Ran `the_dtype_does_not_tell_you()` and can state what pandas cannot know

## Build brief

- [ ] `PERMITTED` table declared, with reasons beside it
- [ ] `assert_permitted` — **TODO(me)**: refuses with a **reason**
- [ ] `describe_by_level` — **TODO(me)**: omits the mean for nominal/ordinal, reuses `summary`
- [ ] `infer_level` — **TODO(me)**: id columns → nominal; documented as a guess
- [ ] `measurement_schema` — **TODO(me)**: declarations win, guesses reported separately
- [ ] `claim_type` — **TODO(me)**
- [ ] Did **not** reimplement Day 25's `summary`

## Tests that must be able to fail

- [ ] `test_every_level_permits_the_mode` — four green cases
- [ ] `test_mean_is_permitted_for_interval_and_ratio` — green
- [ ] `test_mean_is_refused_for_nominal_and_ordinal` — green ← **today's real assessment**
- [ ] **Made the message a bare refusal, watched it go red, added the reason** ← do not skip
- [ ] `test_median_is_refused_for_nominal` — green
- [ ] `test_ratio_only_statistics_are_refused_for_interval` — green
- [ ] `test_unknown_level_and_statistic_raise` — green
- [ ] `test_permitted_sets_are_nested` — green
- [ ] **Added a statistic to `interval` but not `ratio`, watched it go red, fixed it** ← do not skip
- [ ] `test_describe_omits_the_mean_for_ordinal` — green
- [ ] `test_describe_includes_the_mean_for_ratio` — green
- [ ] `test_describe_uses_sample_std` — green (2.138, not 2.0)
- [ ] `test_describe_reuses_the_shared_summary` — green
- [ ] `test_describe_all_missing_does_not_raise` — green
- [ ] `test_infer_ordered_categorical_is_ordinal` — green
- [ ] `test_infer_unordered_categorical_and_text_are_nominal` — green
- [ ] `test_infer_treats_an_id_column_as_nominal` — green ← the bug this day exists to prevent
- [ ] `test_infer_positive_numeric_is_ratio` / `..._with_negatives_is_interval` — green
- [ ] `test_declared_levels_beat_inferred` — green
- [ ] `test_guessed_columns_are_reported` — green
- [ ] `test_declaring_a_missing_column_raises` — green
- [ ] `test_schema_is_json_serialisable` — green
- [ ] `test_claim_type` — four green cases
- [ ] `test_claim_type_rejects_empty` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the difference between a statistic and a parameter?
- [ ] Give the same number as a descriptive claim and as an inferential one
- [ ] Why does a bigger sample not fix bias?
- [ ] Why is "these two groups differ" never a finding on its own?
- [ ] Name the four levels and one legal and one illegal operation for each
- [ ] What assumption does an ordinal mean make that you cannot justify?
- [ ] Why is a ratio of years meaningless, and what fixes it?
- [ ] Why can pandas not infer the level of measurement?

## Commit

- [ ] `./m check && ./m done 58` succeeded
