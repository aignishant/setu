# Day 59 — CHECKLIST

**IDs covered:** ST-03 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-59/lab/central.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report including the breakdown-point table, then all stats tests green.

## Setup

- [ ] `./m start 59` and `./m scaffold 59` run
- [ ] `days/day-59/lab/central.py` created
- [ ] No new packages installed

## ST-03 — from scratch

- [ ] Computed all three by hand before using numpy or scipy
- [ ] Handled the median's **even** case correctly
- [ ] Can say why a median may be a value that appears nowhere in the data
- [ ] Checked `scipy.stats.mode`'s signature for **your** pinned version

## The demonstration

- [ ] Ran `one_billionaire()`; recorded how far the mean moved: ______
- [ ] …and the median: ______
- [ ] Ran `the_breakdown_point()` and **read the whole table**
- [ ] Can state the breakdown point of each measure
- [ ] Can define robustness in that precise sense

## Which one

- [ ] Ran `which_one_is_the_question()`
- [ ] Confirmed `mean × n == sum` exactly
- [ ] Can state why the median has no totalling property
- [ ] Can give one question that needs the mean **despite** heavy skew

## Mode

- [ ] Used `.mode()` on nominal data
- [ ] Saw pandas return **every** tied mode
- [ ] Can say what `.mode()[0]` silently does
- [ ] Saw the mode be useless on continuous data, and know the two fixes

## Bimodality and other traps

- [ ] Ran `bimodal_is_a_warning()`; counted how many observations were near the "centre"
- [ ] Connected it to Day 37 and Day 39
- [ ] Used `trim_mean`; know you must state the trim fraction
- [ ] Ran the weighted-mean comparison: naive ______ vs weighted ______
- [ ] Can name what averaging averages ignores
- [ ] Can say what `nanmean` assumes about the missing values

## Build brief

- [ ] `central_tendency` — **TODO(me)**: level-aware, calls `assert_permitted`, skew direction
- [ ] `modes` — **TODO(me)**: every tie, empty when all unique, ignores NaN, JSON-safe
- [ ] `weighted_mean` — **TODO(me)**: validates lengths, weights, NaN
- [ ] `robustness_report` — **TODO(me)**: empirical shift plus breakdown points
- [ ] `choose_centre` — **TODO(me)**: purpose-aware, returns a **reason**
- [ ] Can explain why `modes` returns a list rather than a value

## Tests that must be able to fail

- [ ] `test_mean_matches_a_hand_computation` — green
- [ ] `test_median_of_an_even_sample_averages_the_middle_two` — green
- [ ] `test_nominal_gets_a_mode_and_nothing_else` — green
- [ ] `test_ordinal_gets_a_median_but_no_mean` — green
- [ ] `test_skew_direction_is_detected` — three green cases
- [ ] `test_skew_direction_is_absent_for_ordinal` — green
- [ ] `test_trimmed_mean_is_between_mean_and_median` — green
- [ ] `test_trim_must_be_a_valid_fraction` — three green cases
- [ ] `test_all_missing_does_not_raise` — green
- [ ] `test_modes_returns_every_tie` — green ← **today's real assessment**
- [ ] **Returned a single value from `modes`, watched it go red, returned a list** ← do not skip
- [ ] `test_modes_is_empty_when_everything_is_unique` — green
- [ ] `test_modes_ignores_nan` / `..._plain_python_types` / `..._rejects_empty_input` — green
- [ ] `test_weighted_mean_accounts_for_group_size` — green (2.0 vs 2.6)
- [ ] `test_weighted_mean_rejects_a_length_mismatch` — green, both lengths named
- [ ] `test_weighted_mean_rejects_negative_weights` / `..._zero_total_weight` — green
- [ ] `test_weighted_mean_allows_an_empty_group` — green
- [ ] `test_weighted_mean_refuses_nan_with_weight` — green
- [ ] `test_robustness_shows_the_mean_moves_more` — green
- [ ] `test_total_always_recommends_the_mean` — green ← the counter-intuitive one
- [ ] **Made `choose_centre` return the median whenever skewed, watched it go red, fixed it** ← do not skip
- [ ] `test_total_is_illegal_for_ordinal` — green
- [ ] `test_typical_recommends_the_mode_for_nominal` / `..._median_for_ordinal` — green
- [ ] `test_choose_centre_always_gives_a_reason` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Define each measure in one sentence, without formulas
- [ ] What is a breakdown point, and what is each measure's?
- [ ] Give a question that needs the mean even though the data is skewed
- [ ] Why does the median have no totalling property?
- [ ] What does `.mode()[0]` hide?
- [ ] Why is the mode useless on continuous data?
- [ ] What does averaging group means get wrong?
- [ ] What does `nanmean` assume, and what must you report beside it?

## Commit

- [ ] `./m check && ./m done 59` succeeded
