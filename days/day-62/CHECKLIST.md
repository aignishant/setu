# Day 62 — CHECKLIST

**IDs covered:** ST-06 · **Principles served:** 1, 2, 7, 10

## Demo command

```bash
uv run python days/day-62/lab/association.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report including the Anscombe table, then all stats tests green.

## Setup

- [ ] `./m start 62` and `./m scaffold 62` run
- [ ] `days/day-62/lab/association.py` created
- [ ] No new packages installed

## ST-06 — from covariance to correlation

- [ ] Computed covariance and `r` **by hand** before using a library
- [ ] Read the products row and can say which pairs contribute positively
- [ ] Ran `units_are_the_problem()`; confirmed covariance changed 25.4× and `r` did not
- [ ] Can state the derivation in one sentence

## Anscombe

- [ ] Ran `anscombe()` and **read the table before the descriptions**
- [ ] Confirmed all seven statistics agree to two decimal places
- [ ] Can describe the shape of each of the four sets
- [ ] Can say which one supports "these variables are linearly related"
- [ ] Ran `what_removing_one_point_does()`
- [ ] Saw set IV's correlation become **undefined** and can explain why
- [ ] Saw set I barely move

## Spearman

- [ ] Ran `spearman_sees_monotonic()`
- [ ] Confirmed the exponential has Spearman ≈ 1.0 but lower Pearson
- [ ] Confirmed the parabola defeats **both**
- [ ] Can state what `r ≈ 0` does and does not mean
- [ ] Ran `spearman_is_robust()`; saw one outlier flip Pearson's **sign**
- [ ] Can say why a rank cannot run away

## r² and causation

- [ ] Read the `r` vs `r²` table; can say what `r = 0.7` really means
- [ ] Ran `correlation_is_not_causation()`
- [ ] Confirmed the association vanished after controlling for the confounder
- [ ] Can explain what a confounder does, using the constructed example

## Build brief

- [ ] `association` — **TODO(me)**: level-aware, returns warnings, drops and counts incomplete pairs
- [ ] `leverage_check` — **TODO(me)**: leave-one-out, names the influential point
- [ ] `anscombe_frames` — **TODO(me)**
- [ ] `association_matrix` — **TODO(me)**: reuses Day 25, lists skipped pairs, caps the work
- [ ] Can explain why warnings travel with the number

## Tests that must be able to fail

- [ ] `test_correlation_matches_scipy` — green
- [ ] `test_correlation_is_scale_invariant` — green
- [ ] `test_r_squared_is_reported` — green
- [ ] `test_anscombe_sets_share_their_statistics` — green ← **today's real assessment**
- [ ] `test_anscombe_has_four_sets_of_eleven_points` — green
- [ ] `test_leverage_finds_anscombe_four_fragile` — green
- [ ] `test_leverage_finds_anscombe_three_fragile` — green
- [ ] `test_leverage_says_anscombe_one_is_stable` — green
- [ ] **Made `leverage_check` always report fragile, watched the set-I test go red, fixed it** ← do not skip
- [ ] `test_leverage_names_the_influential_point` — green (x = 19)
- [ ] `test_leverage_rejects_tiny_samples` — green
- [ ] `test_pearson_and_spearman_diverge_on_a_curve` — green, warning fired
- [ ] **Removed the divergence warning, watched it go red, restored it** ← do not skip
- [ ] `test_spearman_is_robust_to_an_outlier` — green
- [ ] `test_near_zero_r_does_not_mean_independent` — green
- [ ] `test_pearson_is_refused_for_ordinal` — green
- [ ] `test_spearman_is_allowed_for_ordinal` — green
- [ ] `test_nominal_is_refused_for_both` — green
- [ ] `test_small_n_gets_a_warning` — green
- [ ] `test_missing_pairs_are_dropped_and_counted` — green
- [ ] `test_too_few_complete_pairs_raises` / `test_unknown_method_raises` — green
- [ ] `test_matrix_reuses_day_25_correlation` — green
- [ ] `test_matrix_lists_skipped_pairs` — green
- [ ] `test_matrix_refuses_too_many_columns` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Derive correlation from covariance in one sentence
- [ ] Describe all four Anscombe sets and what each would mislead you into
- [ ] Why can you not tell which set you have from the statistics?
- [ ] What does `r ≈ 0` actually rule out?
- [ ] When is Spearman the right choice, and why is it robust?
- [ ] Why report `r²` beside `r`?
- [ ] How does a confounder manufacture a correlation?
- [ ] What does a Pearson–Spearman gap tell you for free?

## Commit

- [ ] `./m check && ./m done 62` succeeded
