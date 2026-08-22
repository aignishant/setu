# Day 71 — CHECKLIST

**IDs covered:** ST-18 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-71/lab/ttests.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report including the Student-vs-Welch and correlation tables, then all stats
tests green.

## Setup

- [ ] `./m start 71` and `./m scaffold 71` run
- [ ] `days/day-71/lab/ttests.py` created
- [ ] No new packages installed

## ST-18 — the family

- [ ] Computed a one-sample t **by hand** before using scipy
- [ ] Can name where SE, df and `sf` each came from (three earlier days)
- [ ] Can describe `t` as a ratio, in words
- [ ] Confirmed the paired test is **identical** to a one-sample test on differences
- [ ] Recorded independent p ______ vs paired p ______ on the same data
- [ ] Can say what pairing removed

## Student vs Welch

- [ ] Ran `student_versus_welch()` and **read the whole table**
- [ ] Confirmed Student survives with equal n and breaks with unequal n
- [ ] Recorded Student's worst false-positive rate: ______ (target 0.05)
- [ ] Confirmed Welch's power cost when variances are equal is negligible
- [ ] Know what `scipy.stats.ttest_ind` defaults to, and why that is wrong

## What actually matters

- [ ] Ran `what_the_t_test_assumes()` on four scenarios
- [ ] Confirmed skew and heavy tails **barely move** the error rate
- [ ] Confirmed the outlier row does not
- [ ] Can say which assumption is over-worried about and which is under-worried about
- [ ] Ran `independence_is_the_assumption_that_matters()`
- [ ] Recorded the false-positive rate at r = 0.5: ______
- [ ] Can name three real situations that produce correlated observations
- [ ] Can say why no transformation fixes it

## ANOVA

- [ ] Computed F **by hand** from between- and within-group sums of squares
- [ ] Can describe F as a ratio, in words
- [ ] Can say what F ≈ 1 means
- [ ] Confirmed a significant F cannot identify **which** group differs
- [ ] Ran `anova_versus_pairwise()`; recorded both false-positive rates
- [ ] Can say what the ANOVA exists to avoid
- [ ] Can state the right order of operations

## Rank tests

- [ ] Ran `when_to_use_a_rank_test()` on three scenarios
- [ ] Can say when the t-test wins and when the rank test does
- [ ] Can state what Mann-Whitney's null hypothesis actually is

## Build brief

- [ ] `t_test` — **TODO(me)**: Welch by default, reports assumptions, reuses Days 68 and 69
- [ ] `anova` — **TODO(me)**: eta-squared, conclusion never names a group, points to post-hoc
- [ ] `choose_test` — **TODO(me)**: level-aware, reason names the deciding factor
- [ ] `effective_n` — **TODO(me)**: the design-effect formula
- [ ] `assumption_report` — **TODO(me)**: concerns ordered by **measured** severity
- [ ] Can explain why normality is checked last

## Tests that must be able to fail

- [ ] `test_one_sample_matches_scipy` — green
- [ ] `test_welch_is_the_default` — green
- [ ] `test_paired_equals_one_sample_on_the_differences` — green
- [ ] `test_pairing_beats_independence_on_paired_data` — green
- [ ] `test_paired_rejects_unequal_lengths` — green
- [ ] `test_equal_var_true_warns_when_variances_differ` — green
- [ ] `test_outliers_are_flagged` — green
- [ ] `test_skewed_data_alone_does_not_warn` — green ← **today's real assessment**
- [ ] **Made the checker warn on any non-normality, watched it go red, narrowed it** ← do not skip
- [ ] `test_the_result_carries_an_effect_size_and_an_interval` — green
- [ ] `test_assumptions_are_reported` — green
- [ ] `test_anova_matches_scipy` — green
- [ ] `test_f_is_near_one_when_nothing_differs` — green
- [ ] `test_anova_never_names_a_group` — green
- [ ] **Wrote a conclusion naming the differing group, watched it go red, fixed it** ← do not skip
- [ ] `test_anova_points_at_a_post_hoc_test` — green
- [ ] `test_eta_squared_is_reported_and_bounded` — green
- [ ] `test_anova_warns_on_very_unequal_variances` — green
- [ ] `test_anova_needs_three_groups` — green
- [ ] `test_effective_n_collapses_under_correlation` — green
- [ ] `test_effective_n_equals_n_when_independent` — green
- [ ] `test_effective_n_rejects_impossible_correlations` — green
- [ ] `test_choose_test_defaults_to_welch` — green
- [ ] `test_choose_test_refuses_a_t_test_on_ordinal_data` — green
- [ ] `test_choose_test_sends_nominal_to_chi_square` — green
- [ ] `test_choose_test_picks_a_rank_test_with_outliers` — green
- [ ] `test_choose_test_handles_paired_and_many_groups` — green
- [ ] `test_assumption_report_ranks_outliers_above_normality` — green
- [ ] `test_assumption_report_says_independence_cannot_be_checked` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Describe `t` and `F` each as a ratio, without formulas
- [ ] Why is the paired test the same as a one-sample test?
- [ ] When does Student's t-test break, and why is Welch nearly free?
- [ ] Rank the t-test's assumptions by how much violating them actually costs
- [ ] What does a within-group correlation of 0.5 do to your effective n?
- [ ] What does a significant F entitle you to say — and not say?
- [ ] Why is running all pairwise t-tests worse than an ANOVA?
- [ ] What is Mann-Whitney's null hypothesis?

## Commit

- [ ] `./m check && ./m done 71` succeeded
