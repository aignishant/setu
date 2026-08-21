# Day 67 — CHECKLIST

**IDs covered:** ST-14 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-67/lab/clt.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the seven-part report including the convergence table and the Cauchy failure, then all
stats tests green.

## Setup

- [ ] `./m start 67` and `./m scaffold 67` run
- [ ] `days/day-67/lab/clt.py` created
- [ ] No new packages installed

## ST-14 — watching it happen

- [ ] Can state the theorem in one sentence, being precise about **what** becomes normal
- [ ] Ran `watch_it_happen()` and **read all three named columns**
- [ ] Confirmed the mean of x̄ sits on μ at every n
- [ ] Confirmed the sd of x̄ tracks σ/√n
- [ ] Confirmed the skew of x̄ marches toward zero
- [ ] Recorded the population skew ______ and the skew of means at n=100 ______

## The √n rule

- [ ] Ran `the_root_n_rule()` and confirmed 4× data halves the standard error
- [ ] Can say what going from n=1,000 to n=2,000 actually buys
- [ ] Can state why this governs "should we collect more data?"

## Speed depends on shape

- [ ] Ran `shape_decides_the_speed()` and **read the whole table**
- [ ] Confirmed the lognormal is still skewed at n=100
- [ ] Confirmed the **bimodal** population converges fast
- [ ] Can say what actually determines the speed
- [ ] Can explain why "n > 30" is folklore

## Where it fails

- [ ] Ran `where_it_fails()` and confirmed the Cauchy IQR **does not shrink**
- [ ] Can state the condition the CLT requires
- [ ] Can name a real-world analogue
- [ ] Ran `it_is_only_about_the_mean()`
- [ ] Confirmed the maximum and variance do **not** converge
- [ ] Can say what "CLT, therefore normal" gets wrong when applied to a maximum

## The payoff

- [ ] Ran `the_practical_payoff()`; recorded coverage at n=200: ______
- [ ] Recorded coverage at n=5: ______ and n=20: ______
- [ ] Can say which direction the small-n failure errs in, and why that is dangerous
- [ ] Ran `sums_too()` and can connect it to Day 65's binomial

## Build brief

- [ ] `sampling_distribution` — **TODO(me)**: vectorised, five statistics, reproducible
- [ ] `clt_convergence` — **TODO(me)**: tracks predicted SE and skew ratio, reports `converged_at`
- [ ] `required_n` — **TODO(me)**: the root-n rule inverted
- [ ] `clt_applies` — **TODO(me)**: conservative, checks for infinite variance, returns reasons
- [ ] `coverage_check` — **TODO(me)**: measures what actually matters
- [ ] Can explain why `clt_applies` is deliberately stricter than the folklore

## Tests that must be able to fail

- [ ] `test_the_sampling_distribution_is_centred_on_mu` — green
- [ ] `test_the_standard_error_follows_root_n` — green (claim 2)
- [ ] `test_the_shape_converges` — green (claim 3)
- [ ] `test_sampling_distribution_is_vectorised` — green under 5 s
- [ ] **Wrote it as a Python loop over trials, watched the timing test go red, vectorised it** ← do not skip
- [ ] `test_sampling_distribution_is_reproducible` — green
- [ ] `test_unknown_statistic_raises` / `test_too_few_trials_raises` — green
- [ ] `test_convergence_report_tracks_the_predicted_se` — green
- [ ] `test_convergence_report_shows_skew_shrinking` — green
- [ ] `test_symmetric_populations_converge_faster_than_skewed_ones` — green ← **today's real assessment**
- [ ] `test_a_bimodal_population_still_converges_fast` — green
- [ ] **Judged convergence by how normal the population looked, watched the bimodal test go red** ← do not skip
- [ ] `test_convergence_rejects_a_tiny_population` — green
- [ ] `test_required_n_inverts_the_root_n_rule` — green
- [ ] `test_halving_the_target_quadruples_n` — green
- [ ] `test_required_n_rejects_impossible_targets` — green
- [ ] `test_clt_refuses_small_n_regardless_of_shape` — green
- [ ] `test_clt_refuses_heavy_skew_at_moderate_n` — green
- [ ] `test_clt_accepts_symmetric_data_at_moderate_n` — green
- [ ] `test_clt_accepts_skewed_data_at_large_n` — green
- [ ] `test_clt_refuses_infinite_variance_data` — green
- [ ] **Used only skew and n, watched the Cauchy test go red, added the variance-growth check** ← do not skip
- [ ] `test_coverage_is_close_to_nominal_at_large_n` — green
- [ ] `test_coverage_falls_short_at_small_n_on_skewed_data` — green
- [ ] `test_coverage_is_fine_at_small_n_on_symmetric_data` — green
- [ ] `test_the_clt_says_nothing_about_the_maximum` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the theorem, being precise about what becomes normal
- [ ] Give all three claims, not just the shape one
- [ ] Why does halving your uncertainty cost four times the data?
- [ ] What determines how fast convergence happens?
- [ ] Why does a bimodal population converge faster than a lognormal one?
- [ ] Name the condition the CLT requires, and a distribution that lacks it
- [ ] What does the CLT say about a sample maximum?
- [ ] Why is falling short of nominal coverage the dangerous direction?

## Commit

- [ ] `./m check && ./m done 67` succeeded
