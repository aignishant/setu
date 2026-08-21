# Day 65 — CHECKLIST

**IDs covered:** ST-10, ST-11 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-65/lab/named.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including the dispersion table and the p-value uniformity check, then
all stats tests green.

## Setup

- [ ] `./m start 65` and `./m scaffold 65` run
- [ ] `days/day-65/lab/named.py` created
- [ ] No new packages installed

## ST-10 — Bernoulli and binomial

- [ ] Can state the Bernoulli story in one sentence
- [ ] Read the `p(1−p)` table; can say where variance is maximal
- [ ] Can connect `p = 0.01` to Day 78's imbalanced-classification problem
- [ ] Computed a binomial PMF **by hand** with `math.comb`
- [ ] Can say what the `C(n,k)` factor is actually counting
- [ ] Can state the binomial's **two** assumptions
- [ ] Ran `the_two_assumptions()` and compared the variance columns
- [ ] Can say what overdispersion is a fingerprint of

## ST-11 — Poisson and uniform

- [ ] Ran `poisson_is_a_limit()` and watched the binomial converge
- [ ] Can state the Poisson story, including the word "rare"
- [ ] Ran `the_poisson_signature()`; recorded var/mean for both series
- [ ] Can state the free test in one line
- [ ] Can say which direction a Poisson model errs on overdispersed data, and why that is dangerous
- [ ] Ran `poisson_intervals_scale()`; can say why "λ = 3" alone is meaningless
- [ ] Confirmed `sp.uniform(10, 20)` covers **[10, 30]**, not [10, 20]
- [ ] Know that NumPy's `rng.uniform` disagrees with SciPy's
- [ ] Ran the 3,000-t-test check; recorded the fraction with p < 0.05: ______
- [ ] Can say what distribution a p-value has under a true null, and why that matters on Day 70

## Choosing and checking

- [ ] Read the six-row story table
- [ ] Can say what the middle column is actually claiming
- [ ] Ran `fitting_and_checking()` and saw a successful fit of a wrong model
- [ ] Can describe the overdispersion signature in the observed-vs-expected table

## Build brief

- [ ] `fit_distribution` — **TODO(me)**: fits **and** checks, warns on dispersion
- [ ] Refuses to invent `n_trials` for a binomial
- [ ] `dispersion_ratio` — **TODO(me)**: three verdicts, validates input
- [ ] `goodness_of_fit_table` — **TODO(me)**: shape stable for Day 73
- [ ] `binomial_interval` — **TODO(me)**: Wilson by default, normal available for contrast
- [ ] Can explain why `n_trials` cannot be estimated from counts alone

## Tests that must be able to fail

- [ ] `test_bernoulli_p_is_the_mean` / `..._rejects_non_binary_values` — green
- [ ] `test_binomial_refuses_to_invent_n` — green
- [ ] `test_poisson_lambda_is_the_mean` — green
- [ ] `test_poisson_rejects_negative_counts` / `..._non_integers` — green
- [ ] `test_a_true_poisson_gets_no_dispersion_warning` — green
- [ ] `test_overdispersed_counts_are_flagged` — green ← **today's real assessment**
- [ ] **Removed the dispersion check, watched a wrong model fit silently, restored it** ← do not skip
- [ ] `test_the_dispersion_ratio_is_the_free_test` — green
- [ ] `test_bursty_counts_are_overdispersed` — green
- [ ] `test_underdispersed_counts_are_detected` — green
- [ ] **Made the verdict only ever say poisson-like or overdispersed, watched it go red** ← do not skip
- [ ] `test_dispersion_rejects_a_zero_mean` / `..._negative_counts` — green
- [ ] `test_unknown_distribution_lists_the_known_ones` — green
- [ ] `test_goodness_of_fit_matches_on_real_poisson_data` — green
- [ ] `test_goodness_of_fit_diverges_on_overdispersed_data` — green (excess zeros)
- [ ] `test_goodness_of_fit_is_json_serialisable` — green
- [ ] `test_wilson_interval_contains_the_estimate` — green
- [ ] `test_wilson_stays_inside_zero_and_one` — four green boundary cases
- [ ] `test_the_normal_approximation_fails_where_wilson_does_not` — green
- [ ] **Made Wilson the fallback and normal the default, watched it go red, reverted** ← do not skip
- [ ] `test_the_interval_narrows_with_more_data` — green
- [ ] `test_binomial_interval_rejects_impossible_counts` — three green cases
- [ ] `test_uniform_fit_uses_min_and_max` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Give the generative story for each of the four distributions
- [ ] What are the binomial's two assumptions, and what breaks when each fails?
- [ ] State the Poisson's free self-test in one line
- [ ] Why is understating uncertainty the dangerous direction to be wrong in?
- [ ] Why does "λ = 3" mean nothing on its own?
- [ ] What distribution does a p-value follow under a true null, and what follows from that?
- [ ] Why can `n` not be estimated from binomial counts?
- [ ] Why does the normal proportion interval fail at k = 0?

## Commit

- [ ] `./m check && ./m done 65` succeeded
