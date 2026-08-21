# Day 68 — CHECKLIST · **PHASE 8 GATE**

**IDs covered:** ST-15 · **Principles served:** 1, 2, 7, 10 · **Artifact:** a coverage report

## Demo command

```bash
uv run python days/day-68/lab/estimation.py
uv run python -m pytest tests/test_stats.py -v
uv run python -m pytest -q
```

Expected: the seven-part report ending with the three-method coverage table, then the whole suite green.

## Setup

- [ ] `./m start 68` and `./m scaffold 68` run
- [ ] `days/day-68/lab/estimation.py` created
- [ ] No new packages installed

## ST-15 — what confidence means

- [ ] Ran `what_confidence_means()`; recorded how many of 20 intervals missed: ______
- [ ] Looked at the misses and confirmed nothing distinguishes them
- [ ] Can state the **wrong** phrasing and say precisely why it is wrong
- [ ] Can state the **right** phrasing
- [ ] Can say where the randomness actually lives

## The construction

- [ ] Built intervals at five confidence levels and read the width column
- [ ] Can say what more confidence costs
- [ ] Ran `z_versus_t()` and recorded the t/z ratio at n=3: ______
- [ ] Can say why t is correct when σ is unknown
- [ ] Recorded coverage using z at n=5: ______ (target 0.95)
- [ ] Can name the Day-71 topic this multiplier becomes

## The bootstrap

- [ ] Wrote the resampling in one line and can explain each argument
- [ ] Confirmed the bootstrap SE agrees with the formula **without using it**
- [ ] Confirmed the bootstrap interval is **asymmetric** on skewed data
- [ ] Can say why symmetry was the problem yesterday
- [ ] Ran `bootstrap_anything()` on five statistics
- [ ] Can name two of them that have no textbook standard-error formula
- [ ] Can state the bootstrap's real advantage in one sentence

## Honest limits

- [ ] Ran `where_the_bootstrap_struggles()` and can describe all three failure modes
- [ ] Can say why a bootstrapped maximum is stuck
- [ ] Can say what plain resampling does to a time series
- [ ] Ran `coverage_is_the_real_test()` and **read the whole table**
- [ ] Can say what happens at n=5 across all three methods

## Build brief

- [ ] `confidence_interval` — **TODO(me)**: `t` by default, warns on z at small n, calls `clt_applies`
- [ ] `bootstrap_ci` — **TODO(me)**: general statistic, vectorised, warns on tiny n and low uniqueness
- [ ] `compare_intervals` — **TODO(me)**: reports asymmetry
- [ ] `interval_coverage` — **TODO(me)**: the gate measurement
- [ ] `describe_interval` — **TODO(me)**: correct English, refuses the probability phrasing
- [ ] Can explain why `t` is the default

## Tests that must be able to fail

- [ ] `test_interval_contains_the_estimate` — green
- [ ] `test_t_is_the_default` — green
- [ ] `test_t_is_wider_than_z_at_small_n` / `test_t_and_z_converge_at_large_n` — green
- [ ] `test_z_at_small_n_carries_a_warning` — green
- [ ] `test_higher_confidence_is_wider` — green
- [ ] `test_interval_narrows_as_root_n` — green
- [ ] `test_confidence_must_be_a_valid_fraction` — four green cases
- [ ] `test_skewed_small_sample_gets_a_clt_warning` — green
- [ ] `test_bootstrap_agrees_with_the_formula_on_normal_data` — green
- [ ] `test_bootstrap_matches_day_25_for_the_mean` — green
- [ ] **Changed a resampling detail and watched the Day-25 agreement break, then fixed it** ← do not skip
- [ ] `test_bootstrap_is_asymmetric_on_skewed_data` — green
- [ ] `test_bootstrap_works_on_a_median` — green
- [ ] `test_bootstrap_works_on_a_percentile_with_no_formula` — green
- [ ] `test_bootstrap_is_reproducible` — green
- [ ] `test_bootstrap_statistic_must_be_vectorised` — green under 5 s
- [ ] `test_bootstrap_warns_on_a_tiny_sample` — green
- [ ] `test_bootstrap_rejects_too_few_values` / `..._resamples` — green
- [ ] `test_a_bootstrapped_maximum_cannot_exceed_the_sample_maximum` — green
- [ ] `test_compare_intervals_reports_asymmetry` — green
- [ ] `test_coverage_is_near_nominal_for_t_at_moderate_n` — green
- [ ] `test_z_under_covers_where_t_does_not` — green
- [ ] `test_all_methods_under_cover_on_skewed_data_at_tiny_n` — green
- [ ] `test_shortfall_is_positive_when_under_covering` — green
- [ ] `test_the_description_does_not_claim_a_probability` — green ← **today's real assessment**
- [ ] **Wrote the sentence the common way, watched it go red, corrected it** ← do not skip
- [ ] `test_the_description_mentions_the_procedure` — green
- [ ] `test_describe_rejects_a_malformed_result` — green
- [ ] `test_phase_8_stats_module_is_complete` — green (42 functions)

## The coverage report (the gate artifact)

- [ ] `reports/day68_coverage.md` written
- [ ] At least four populations tested, including a skewed and a bimodal one
- [ ] At least five sample sizes, including n=5
- [ ] All three methods measured
- [ ] Table shows actual coverage against nominal **and** mean width
- [ ] Finding: where does `z` under-cover, and by how much?
- [ ] Finding: at what n does the bootstrap start beating the parametric interval?
- [ ] Finding: is there a case where nothing works?
- [ ] Recommendation stated as a **followable rule**
- [ ] `clt_applies` thresholds compared with your measurements
- [ ] **Adjusted `clt_applies` if the measurements disagreed with it**
- [ ] The honest paragraph written, and checked against `describe_interval`

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State what a 95% confidence interval means, correctly
- [ ] Why is the common phrasing wrong?
- [ ] Why `t` rather than `z`, and what does the wrong choice cost at n=5?
- [ ] Describe the bootstrap algorithm in one sentence
- [ ] What is the bootstrap's real advantage — and what is it not?
- [ ] Name its three failure modes
- [ ] Why is an asymmetric interval right on skewed data?
- [ ] What happens at n=5 on badly skewed data, whatever method you pick?

## PHASE 8 GATE

- [ ] `reports/day68_coverage.md` written with **your** measurements
- [ ] All three §6 questions answered in your own words
- [ ] The recommendation is a rule someone could follow
- [ ] `clt_applies` adjusted if your data disagreed with it
- [ ] `test_phase_8_stats_module_is_complete` green — 42 functions across 11 days
- [ ] `bootstrap_ci` agrees with Day 25's `bootstrap_mean_ci`
- [ ] Every level-of-measurement guard from Day 58 still green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 68` succeeded and `./m status` shows Phases 0–8 complete
