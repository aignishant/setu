# Day 63 — CHECKLIST

**IDs covered:** ST-07, ST-08 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-63/lab/probability.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report including the disease-test count and the prevalence table, then all
stats tests green.

## Setup

- [ ] `./m start 63` and `./m scaffold 63` run
- [ ] `days/day-63/lab/probability.py` created
- [ ] No new packages installed

## ST-07 / ST-08 — the machinery

- [ ] Built a sample space explicitly and computed probabilities by **counting**
- [ ] Used set intersection and union, and confirmed `P(A)+P(B)−P(A∩B)`
- [ ] Can say why the overlap is subtracted
- [ ] Ran `conditioning_shrinks_the_world()`; noted the denominator change from 36 to 18
- [ ] Can define conditioning as a change of sample space
- [ ] Saw one pair where conditioning changed nothing and one where it did
- [ ] Ran `independence_is_a_test_not_an_assumption()`
- [ ] Can state the definition of independence two equivalent ways
- [ ] Can connect the second row to Day 62's confounder

## The base-rate fallacy

- [ ] Ran `the_disease_test_by_counting()` and **followed the counts**, not a formula
- [ ] Recorded: true positives ______ false positives ______ P(sick|positive) ______
- [ ] Can state both conditional probabilities and say which is which
- [ ] Can explain **why** the gap exists, in terms of group sizes
- [ ] Ran `prevalence_drives_everything()` and read the whole column
- [ ] Can name the Day-101 problem this is identical to

## Random variables and expectation

- [ ] Computed `E[X]` and `Var[X]` by hand from a discrete distribution
- [ ] Confirmed `E[X] = 0.75` is a value X can never take
- [ ] Ran the 200,000-draw check and saw the sample mean approach `E[X]`
- [ ] Ran `expectation_is_linear()` and can say which of the four identities always hold
- [ ] Can say why `E[X²] ≠ E[X]²`, and what their difference is
- [ ] Can connect that to Day 61's warning about back-transforming a log

## Joint, marginal, conditional

- [ ] Built a joint table and derived both marginals
- [ ] Derived **both** conditionals and compared 0.75 with 0.60
- [ ] Can say what dividing by rows versus columns actually asks

## Build brief

- [ ] `conditional_probability` — **TODO(me)**: row/col, validates the distribution, does not mutate
- [ ] `are_independent` — **TODO(me)**: outer product comparison, names the worst cell
- [ ] `diagnostic_probabilities` — **TODO(me)**: PPV/NPV **plus per-million counts**
- [ ] `expectation` — **TODO(me)**: variance computed **directly**, validates inputs
- [ ] `law_of_large_numbers` — **TODO(me)**: vectorised, reproducible
- [ ] Can explain why `per_million` counts are returned alongside the ratios

## Tests that must be able to fail

- [ ] `test_row_and_column_conditionals_differ` — green ← **today's real assessment**
- [ ] **Normalised along the wrong axis, watched it go red, fixed it** ← do not skip
- [ ] `test_conditionals_sum_to_one_along_the_conditioning_axis` — green
- [ ] `test_conditional_rejects_a_table_that_is_not_a_distribution` — green, total named
- [ ] `test_conditional_rejects_negative_entries` / `..._does_not_mutate` — green
- [ ] `test_independent_table_is_detected` / `test_dependent_table_is_detected` — green
- [ ] `test_the_famous_disease_result` — green (≈ 0.09, not 0.99)
- [ ] `test_ppv_rises_with_prevalence` — green
- [ ] `test_per_million_counts_reconstruct_the_ratio` — green
- [ ] `test_a_perfect_test_gives_ppv_one` — green
- [ ] `test_zero_prevalence_does_not_divide_by_zero` — green
- [ ] `test_diagnostic_rejects_out_of_range_inputs` — three green cases
- [ ] `test_expectation_matches_a_hand_computation` — green
- [ ] `test_expectation_rejects_probabilities_that_do_not_sum_to_one` — green
- [ ] `test_expectation_rejects_a_length_mismatch` / `..._negative_probabilities` — green
- [ ] `test_variance_is_computed_directly_not_by_subtraction` — green
- [ ] **Computed variance as `E[X²] − E[X]²`, watched it go red on 1e8 values, fixed it** ← do not skip
- [ ] `test_sample_mean_approaches_the_expectation` — green
- [ ] `test_error_shrinks_roughly_as_one_over_root_n` — green
- [ ] `test_law_of_large_numbers_is_reproducible` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Define conditioning without using the word "given"
- [ ] State both conditional probabilities in the disease example and explain the gap
- [ ] What makes the 9% figure arithmetic rather than a trick?
- [ ] Which Day-101 concept is this identical to?
- [ ] How do you test independence rather than assume it?
- [ ] Why is `E[X]` not a prediction?
- [ ] Which expectation identities hold always, which need independence, which never hold?
- [ ] Why is `E[X²] − E[X]²` a numerically bad way to compute variance?

## Commit

- [ ] `./m check && ./m done 63` succeeded
