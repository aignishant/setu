# Day 73 — CHECKLIST

**IDs covered:** ST-20 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-73/lab/chisquare.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report including the expected-count table, then all stats tests green.

## Setup

- [ ] `./m start 73` and `./m scaffold 73` run
- [ ] `days/day-73/lab/chisquare.py` created
- [ ] No new packages installed

## ST-20 — the statistic

- [ ] Computed χ² **by hand** and read the contributions column
- [ ] Can say why dividing by E matters, with an example
- [ ] Can explain `df = categories − 1` in terms of what is forced
- [ ] Ran `the_null_distribution_is_generated_not_assumed()`
- [ ] Confirmed the simulated quantiles match `chi2.ppf`
- [ ] Confirmed `E[χ²] = df`
- [ ] Can connect this to what Day 69 built by shuffling

## Goodness-of-fit

- [ ] Tested a true Poisson and an overdispersed one
- [ ] Recorded both p-values
- [ ] Confirmed `df` loses an extra degree for the estimated λ
- [ ] Can say which direction forgetting that pushes your p-value
- [ ] Can connect this to Day 65's eyeball check

## Independence

- [ ] Built the expected table from the marginals **by hand**
- [ ] Can say why that outer product *is* the definition of independence
- [ ] Can name the Day-63 function this duplicates
- [ ] Confirmed scipy applies **Yates' correction** by default on 2×2
- [ ] Ran `the_residuals_say_where()` and located the largest deviation
- [ ] Can state what a significant χ² does and does not entitle you to say

## The assumption

- [ ] Ran `the_expected_count_rule_measured()` and **read the whole table**
- [ ] Recorded the Type I rate at n=12: ______ and at n=600: ______
- [ ] Can say where the "expected ≥ 5" rule comes from
- [ ] Can name two alternatives when it fails
- [ ] Ran `fisher_when_counts_are_tiny()`; can say what Fisher's test enumerates

## Effect size

- [ ] Ran `significance_is_not_strength()` at three sample sizes
- [ ] Confirmed Cramér's V was **unchanged**
- [ ] Can state V's range and its conventional thresholds
- [ ] Can say why V belongs beside every χ²

## Build brief

- [ ] `chi_square_goodness_of_fit` — **TODO(me)**: `estimated_parameters` in the df, warns on small E
- [ ] `chi_square_independence` — **TODO(me)**: `correction=False` default, V, residuals, safe conclusion
- [ ] `cramers_v` — **TODO(me)**: magnitude labels flagged as conventions
- [ ] `expected_counts` — **TODO(me)**: reuses Day 63's logic
- [ ] `choose_count_test` — **TODO(me)**: names the smallest expected count in the reason
- [ ] Can explain why `correction` defaults to False

## Tests that must be able to fail

- [ ] `test_goodness_of_fit_matches_scipy` — green
- [ ] `test_a_fair_die_is_not_rejected` / `test_a_loaded_die_is_rejected` — green
- [ ] `test_estimated_parameters_reduce_the_degrees_of_freedom` — green ← **today's real assessment**
- [ ] **Ignored `estimated_parameters`, watched the p-value assertion go red, fixed it** ← do not skip
- [ ] `test_too_many_estimated_parameters_raises` — green
- [ ] `test_small_expected_counts_are_warned_about` — green
- [ ] `test_contributions_identify_the_offending_category` — green
- [ ] `test_goodness_of_fit_rejects_mismatched_totals` / `..._negative_counts` — green
- [ ] `test_expected_counts_are_the_outer_product` — green
- [ ] `test_independence_matches_scipy_without_correction` — green
- [ ] `test_correction_defaults_to_false` — green
- [ ] `test_correction_makes_the_test_more_conservative` — green
- [ ] `test_an_independent_table_is_not_rejected` — green
- [ ] `test_the_conclusion_never_names_a_cell` — green
- [ ] **Named the deviating cell in the conclusion, watched it go red, moved it to the residuals** ← do not skip
- [ ] `test_the_residuals_locate_the_deviation` — green
- [ ] `test_cramers_v_is_independent_of_sample_size` — green
- [ ] `test_cramers_v_is_bounded` — green
- [ ] `test_a_perfect_association_gives_v_near_one` — green
- [ ] `test_no_association_gives_v_near_zero` — green
- [ ] `test_significant_but_trivial_is_warned_about` — green
- [ ] `test_independence_rejects_a_degenerate_table` — green
- [ ] `test_choose_recommends_chi_square_with_ample_counts` — green
- [ ] `test_choose_recommends_fisher_for_a_small_two_by_two` — green
- [ ] `test_choose_recommends_permutation_for_a_larger_sparse_table` — green
- [ ] `test_the_expected_count_rule_is_real` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is the squared difference divided by the expected count?
- [ ] Where do the expected counts come from in each of the two uses?
- [ ] Why does an estimated parameter cost a degree of freedom?
- [ ] Which direction does forgetting it push your p-value?
- [ ] Where does the "expected ≥ 5" rule come from, and what did you measure?
- [ ] What does a significant χ² entitle you to say?
- [ ] What do the adjusted residuals add?
- [ ] Why report Cramér's V, and what is it independent of?

## Commit

- [ ] `./m check && ./m done 73` succeeded
