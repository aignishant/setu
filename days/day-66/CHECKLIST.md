# Day 66 — CHECKLIST

**IDs covered:** ST-12, ST-13 · **Principles served:** 1, 2, 7, 8

## Demo command

```bash
uv run python days/day-66/lab/normal.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including the ratio table and the leakage demonstration, then all
stats tests green.

## Setup

- [ ] `./m start 66` and `./m scaffold 66` run
- [ ] `days/day-66/lab/normal.py` created
- [ ] No new packages installed

## ST-12 — the normal

- [ ] Memorised 68 / 95 / 99.7
- [ ] Recorded the "1 in" figure for 5σ: ______
- [ ] Ran the empirical check on 500,000 draws and confirmed the rule
- [ ] Ran `two_numbers_determine_everything()`
- [ ] Confirmed `P(X > μ+σ)` is identical in every row
- [ ] Can say why that means z carries all the information

## ST-13 — z-scores

- [ ] Converted two different variables to z and compared them
- [ ] Ran `when_the_percentile_lies()` and **read the ratio column**
- [ ] Recorded how much more common `z > 3` was for heavy-tailed data: ______×
- [ ] Can state the separation: what standardising does vs what the percentile assumes

## Checking normality

- [ ] Ran `checking_normality()` and saw the p-values
- [ ] Can say why a normality test is nearly useless at large n
- [ ] Can list the three better tools **in order**
- [ ] Ran `the_qq_plot()` and can say how heavy tails and right skew differ in shape
- [ ] Can say what a Q-Q plot tells you that a p-value cannot

## Scaling

- [ ] Ran `standardise_versus_normalise()` and **looked at the skew column**
- [ ] Can say why scaling does not change the shape
- [ ] Can name what does (and which day)
- [ ] Can state one advantage and one risk of min-max scaling

## The leakage rule

- [ ] Ran `the_leakage_rule()` with a genuinely shifted test set
- [ ] Recorded: correct z-mean ______ vs refitted z-mean ______
- [ ] Can explain in one sentence what refitting erased
- [ ] Can name the earlier day that built the split, and the later day that formalises it
- [ ] Ran `z_for_a_mean_is_different()`
- [ ] Can state what σ/√n is the standard deviation **of**

## Build brief

- [ ] `z_scores` — **TODO(me)**: applies supplied statistics, handles constant and NaN
- [ ] `z_to_percentile` — **TODO(me)**: **warns** when assuming normality; empirical mode
- [ ] `normality_report` — **TODO(me)**: describes the shape, returns **no p-value**, reuses Day 61
- [ ] `standard_error` — **TODO(me)**: sample or explicit parameters, not both
- [ ] `within_sigma` — **TODO(me)**
- [ ] Can explain why `normality_report` deliberately omits a p-value

## Tests that must be able to fail

- [ ] `test_standardising_gives_mean_zero_sd_one` — green
- [ ] `test_standardising_does_not_change_the_shape` — green
- [ ] `test_fitted_flag_distinguishes_the_two_paths` — green
- [ ] `test_supplied_statistics_are_used_not_refitted` — green ← **today's real assessment**
- [ ] **Ignored the supplied mu/sigma and refitted, watched the shift vanish, fixed it** ← do not skip
- [ ] `test_constant_input_gives_zeros_not_inf` — green
- [ ] `test_nan_stays_nan` — green
- [ ] `test_z_scores_does_not_mutate` — green
- [ ] `test_percentile_from_normal_carries_a_warning` — green
- [ ] **Dropped the warning, watched it go red, restored it** ← do not skip
- [ ] `test_empirical_percentile_needs_no_assumption` — green
- [ ] `test_the_two_methods_disagree_on_heavy_tails` — green
- [ ] `test_empirical_method_requires_a_reference` — green
- [ ] `test_normality_report_identifies_a_normal_sample` — green
- [ ] `test_normality_report_identifies_right_skew` / `..._heavy_tails` — green
- [ ] `test_normality_report_returns_no_p_value` — green
- [ ] `test_large_samples_get_a_warning_about_formal_tests` — green
- [ ] `test_normality_report_reuses_day_61_shape` — green
- [ ] `test_standard_error_is_sigma_over_root_n` — green
- [ ] `test_standard_error_from_a_sample` — green
- [ ] `test_standard_error_shrinks_as_root_n` — green
- [ ] `test_standard_error_rejects_ambiguous_arguments` / `..._n_below_two` — green
- [ ] `test_within_sigma_matches_the_empirical_rule_on_normal_data` — three green cases
- [ ] `test_within_sigma_flags_a_heavy_tailed_sample` — green
- [ ] `test_within_sigma_rejects_a_bad_k` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the empirical rule and what 5σ corresponds to
- [ ] What does standardising always do, and what does it never do?
- [ ] When does reading a percentile off a z-score break, and by how much?
- [ ] Why is a normality test the wrong tool at large n?
- [ ] What does the shape of a Q-Q deviation tell you?
- [ ] What exactly does refitting a scaler on the test set erase?
- [ ] What is σ/√n the standard deviation of?
- [ ] Why does heavy-tailed data have *more* mass within 1σ, not less?

## Commit

- [ ] `./m check && ./m done 66` succeeded
