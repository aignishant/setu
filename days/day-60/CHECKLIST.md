# Day 60 — CHECKLIST

**IDs covered:** ST-04 · **Principles served:** 1, 2, 4, 7

## Demo command

```bash
uv run python days/day-60/lab/spread.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including the ddof simulation table, then all stats tests green.

## Setup

- [ ] `./m start 60` and `./m scaffold 60` run
- [ ] `days/day-60/lab/spread.py` created
- [ ] No new packages installed

## ST-04 — the measures

- [ ] Ran `a_centre_is_half_a_description()`; confirmed identical means, different spreads
- [ ] Computed variance and sd **by hand** before using a library
- [ ] Confirmed `np.std` and `Series.std` **disagree** by default
- [ ] Can say which defaults to which
- [ ] Confirmed deviations from the mean always sum to zero
- [ ] Can say why squaring beats absolute value, and what it costs

## The ddof demonstration

- [ ] Ran `the_ddof_simulation()` and **read the whole table**
- [ ] Confirmed `ddof=0` is too small at **every** n
- [ ] Recorded the n=2 result: ddof=0 gave ______ against a true ______
- [ ] Ran `why_n_minus_one_intuitively()` and saw x̄ minimise the sum of squares
- [ ] Can explain the correction without reciting a formula
- [ ] Can explain degrees of freedom with the three-values-known-mean example
- [ ] Know that this is a property of the **average over many samples**

## Robustness and units

- [ ] Ran `robust_spread()`; recorded sd inflation vs IQR and MAD
- [ ] Know what the 1.4826 constant does
- [ ] Ran `units_and_comparability()` and computed a CV
- [ ] Can name the **two** situations where a CV is meaningless
- [ ] Ran `range_uses_two_values()` and saw the range grow with n while the sd stabilised

## Build brief

- [ ] `dispersion` — **TODO(me)**: level-aware, raises for nominal, no CV for interval
- [ ] `mad` — **TODO(me)**: scaled and unscaled
- [ ] `coefficient_of_variation` — **TODO(me)**: refuses interval, near-zero and negative means
- [ ] `ddof_bias_demo` — **TODO(me)**: vectorised, returns the analytic expectation too
- [ ] `compare_spread` — **TODO(me)**: inflation ratios for all three
- [ ] Can explain why `dispersion` raises for nominal rather than returning `None`

## Tests that must be able to fail

- [ ] `test_std_matches_a_hand_computation` — green
- [ ] `test_ddof_zero_gives_the_other_answer` — green
- [ ] `test_ddof_must_be_zero_or_one` — three green cases
- [ ] `test_nominal_has_no_dispersion` — green, message mentions ordering
- [ ] `test_ordinal_gets_iqr_but_no_std` — green
- [ ] `test_interval_gets_std_but_no_cv` — green
- [ ] `test_ratio_gets_everything` — green
- [ ] `test_dispersion_all_missing_does_not_raise` — green
- [ ] `test_ddof_zero_is_biased_low` — green
- [ ] `test_ddof_one_is_unbiased` — green
- [ ] `test_the_bias_shrinks_with_n` — four green cases ← **today's real assessment**
- [ ] **Changed the simulation to a Python loop and re-ran; confirmed the same answer far slower** ← do not skip
- [ ] `test_at_n_two_ddof_zero_halves_the_variance` — green
- [ ] `test_ddof_demo_is_reproducible` / `..._rejects_n_below_two` — green
- [ ] `test_mad_is_scaled_to_estimate_sigma` — green (lands near 15)
- [ ] **Dropped the 1.4826 constant, watched it go red, restored it** ← do not skip
- [ ] `test_unscaled_mad_is_smaller` — green
- [ ] `test_mad_is_robust_where_std_is_not` — green
- [ ] `test_mad_rejects_a_tiny_sample` — green
- [ ] `test_cv_is_unitless_and_scale_invariant` — green
- [ ] `test_cv_is_refused_for_interval` — green
- [ ] `test_cv_refuses_a_near_zero_mean` / `..._negative_mean` — green
- [ ] `test_compare_spread_shows_std_inflating_most` — green
- [ ] `test_compare_spread_is_json_serialisable` — green
- [ ] `test_project_default_ddof_is_one` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is a centre alone an inadequate summary?
- [ ] Explain, without a formula, why sample variance divides by n−1
- [ ] What is x̄ the minimiser of, and why does that cause the bias?
- [ ] What is the expected shortfall of ddof=0, and what is it at n=2?
- [ ] Explain degrees of freedom concretely
- [ ] Why squared deviations rather than absolute ones?
- [ ] Why is the range not a summary?
- [ ] Name the two situations where a CV is meaningless

## Commit

- [ ] `./m check && ./m done 60` succeeded
