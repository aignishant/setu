# Day 64 — CHECKLIST

**IDs covered:** ST-09 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-64/lab/distributions.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including the density table and the inverse-transform check, then all
stats tests green.

## Setup

- [ ] `./m start 64` and `./m scaffold 64` run
- [ ] `days/day-64/lab/distributions.py` created
- [ ] No new packages installed

## ST-09 — PMF

- [ ] Built a PMF and its CDF as a running total
- [ ] Confirmed the PMF sums to exactly 1
- [ ] Computed a survival probability as `1 − CDF`
- [ ] Can say why a discrete CDF **steps**, and what the step height is

## PDF — the fact people misremember

- [ ] Ran `the_pdf_is_not_a_probability()` and **read the density column**
- [ ] Recorded the density of a uniform on [0, 0.01]: ______
- [ ] Can state what a density actually measures
- [ ] Can say which number is bounded by 1, and which is not
- [ ] Ran `a_point_has_zero_probability()` and watched the interval shrink to zero
- [ ] Can say what `P(X = x) = 0` means, and what it does **not** mean
- [ ] Know when `<` and `≤` are interchangeable and when they are not

## CDF and quantiles

- [ ] Used `cdf`, `sf`, and a difference of two CDFs
- [ ] Compared `1 - cdf(200)` with `sf(200)` and saw the precision loss
- [ ] Can say why that matters specifically in Phase 9
- [ ] Used `ppf` and recovered **±1.96** from it
- [ ] Confirmed `cdf(ppf(p)) == p`
- [ ] Can say what a critical value actually is

## Empirical and practical

- [ ] Compared an empirical CDF with a theoretical one
- [ ] Can say what the ECDF assumes, and why that matters for Day 68
- [ ] Ran `histogram_to_density()`
- [ ] Confirmed `Σ density ≠ 1` but `Σ density × width == 1`
- [ ] Ran `discrete_versus_continuous_cdf()` and saw the binomial CDF jump by the PMF
- [ ] Ran `sampling_from_a_cdf()` and can explain inverse-transform sampling

## Build brief

- [ ] `ecdf` — **TODO(me)**: collapses ties, reaches exactly 1.0, JSON-safe
- [ ] `ecdf_at` — **TODO(me)**: `<=` semantics, vectorised via `searchsorted`
- [ ] `tail_probability` — **TODO(me)**: **must** use `sf` for the upper tail
- [ ] `critical_values` — **TODO(me)**: two-sided and one-sided, validates alpha
- [ ] `is_discrete` — **TODO(me)**
- [ ] `density_check` — **TODO(me)**: raises when the area is not 1
- [ ] Can explain why `tail_probability` mandates `sf`

## Tests that must be able to fail

- [ ] `test_ecdf_reaches_one` — green
- [ ] `test_ecdf_collapses_ties` — green
- [ ] **Emitted one point per observation, watched it go red, collapsed ties** ← do not skip
- [ ] `test_ecdf_is_json_serialisable` — green
- [ ] `test_ecdf_at_uses_less_than_or_equal` — green
- [ ] `test_ecdf_at_outside_the_range` / `..._is_vectorised` — green
- [ ] `test_ecdf_approaches_the_true_cdf` — green
- [ ] `test_upper_tail_uses_sf_not_one_minus_cdf` — green ← **today's real assessment**
- [ ] **Used `1 - cdf` in `tail_probability`, watched it return exactly 0.0, fixed it** ← do not skip
- [ ] `test_lower_tail` / `test_two_sided_doubles_the_smaller_tail` — green
- [ ] `test_two_sided_never_exceeds_one` / `test_unknown_side_raises` — green
- [ ] `test_critical_values_are_the_famous_ones` — green (±1.96 recovered)
- [ ] `test_one_sided_critical_value` — green (1.645)
- [ ] `test_critical_values_round_trip_through_the_cdf` — green
- [ ] `test_alpha_must_be_strictly_between_zero_and_one` — four green cases
- [ ] `test_is_discrete_distinguishes_the_two_kinds` — green
- [ ] `test_discrete_strict_and_non_strict_differ` — green
- [ ] `test_continuous_strict_and_non_strict_agree` — green
- [ ] `test_density_integrates_to_one` — green (area is 1, sum is not)
- [ ] `test_density_peak_matches_the_theoretical_pdf` — green
- [ ] `test_a_pdf_may_exceed_one` — green (density 100, CDF 1)

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the difference between a PMF and a PDF?
- [ ] Why can a density exceed 1, and what is bounded instead?
- [ ] What does `P(X = 120) = 0` mean for a continuous variable?
- [ ] Why is the CDF the function you actually use?
- [ ] Why `sf` rather than `1 - cdf`, and where does it matter?
- [ ] What is ±1.96, precisely?
- [ ] Why do `<` and `≤` differ for a binomial and not for a normal?
- [ ] What does the ECDF assume, and which later day depends on that?

## Commit

- [ ] `./m check && ./m done 64` succeeded
