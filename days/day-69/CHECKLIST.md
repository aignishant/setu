# Day 69 — CHECKLIST

**IDs covered:** ST-16 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-69/lab/testing.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report ending with the sample-size demonstration, then all stats tests green.

## Setup

- [ ] `./m start 69` and `./m scaffold 69` run
- [ ] `days/day-69/lab/testing.py` created
- [ ] No new packages installed

## ST-16 — the mechanism

- [ ] Ran `any_two_samples_differ()`; recorded the largest chance gap: ______
- [ ] Can state the question a hypothesis test actually answers, in one sentence
- [ ] Can name all five steps from memory
- [ ] Can say which step textbooks obscure, and why it matters

## The permutation test

- [ ] Built a null distribution by shuffling labels
- [ ] Confirmed it centred on zero **without imposing it**
- [ ] Computed the p-value as a **counting operation**
- [ ] Can explain why shuffling is a valid way to represent H₀
- [ ] Ran `when_there_is_no_effect()` and got an unremarkable p
- [ ] Used the phrase "fail to reject", not "accept"

## What p means

- [ ] Can state the definition with the conditioning bar in the right place
- [ ] Can name all three things p is **not**
- [ ] Can say which conditional those three actually describe, and which day covers it

## Choices

- [ ] Ran `one_sided_versus_two()`; recorded both p-values
- [ ] Can say when a one-sided test is legitimate, and what obligation comes with it
- [ ] Ran `the_test_statistic_is_a_choice()` on three statistics
- [ ] Can name one with no textbook formula
- [ ] Can say what goes wrong if you run all three and report the best

## The shortcut

- [ ] Ran `the_named_test_is_a_shortcut()`
- [ ] Confirmed the permutation p and the t-test p agree
- [ ] Confirmed the generated null distribution is approximately normal
- [ ] Can explain **why** the t-test works, in terms of what you just built
- [ ] Can say when the shortcut fails and the permutation test does not

## What a test cannot tell you

- [ ] Ran `what_a_test_cannot_tell_you()` at three sample sizes
- [ ] Confirmed a trivial effect became "highly significant" at large n
- [ ] Can state what p answers and what it does not

## Build brief

- [ ] `permutation_test` — **TODO(me)**: `(count+1)/(resamples+1)`, three alternatives, warnings
- [ ] `null_distribution` — **TODO(me)**: returns the array for plotting
- [ ] `effect_size` — **TODO(me)**: three kinds, magnitude labels flagged as conventions
- [ ] `test_report` — **TODO(me)**: never says "accept", warns on trivial effects and low power
- [ ] `state_result` — **TODO(me)**: correct English, includes the effect size
- [ ] Can explain why a permutation p-value can never be exactly zero

## Tests that must be able to fail

- [ ] `test_a_real_effect_is_detected` / `test_no_effect_gives_an_unremarkable_p` — green
- [ ] `test_the_null_distribution_is_centred_on_zero` — green
- [ ] `test_the_p_value_can_never_be_exactly_zero` — green ← **today's real assessment**
- [ ] **Used `count/resamples`, watched it return 0.0 and go red, fixed it** ← do not skip
- [ ] `test_a_floor_p_value_carries_a_warning` — green
- [ ] `test_the_permutation_p_matches_the_t_test` — green
- [ ] `test_one_sided_is_roughly_half_of_two_sided` — green
- [ ] `test_the_wrong_one_sided_direction_gives_a_large_p` — green
- [ ] `test_unknown_alternative_raises` — green
- [ ] `test_it_works_on_a_statistic_with_no_formula` — green
- [ ] `test_tiny_groups_are_warned_about` — green
- [ ] `test_permutation_is_reproducible` / `test_empty_group_raises` — green
- [ ] `test_null_distribution_is_returned_for_plotting` — green
- [ ] `test_cohens_d_matches_a_hand_computation` — green
- [ ] `test_effect_size_is_independent_of_sample_size` — green
- [ ] `test_magnitude_labels` — green
- [ ] `test_hedges_g_is_smaller_than_d_on_tiny_samples` — green
- [ ] `test_effect_size_rejects_a_zero_pooled_sd` — green
- [ ] `test_report_never_says_accept` — green
- [ ] `test_report_warns_when_significant_but_trivial` — green
- [ ] **Removed that warning, watched it go red, restored it** ← do not skip
- [ ] `test_report_warns_when_null_result_may_be_low_power` — green
- [ ] `test_report_includes_an_interval_on_the_difference` — green
- [ ] `test_the_statement_reports_more_than_a_p_value` — green
- [ ] `test_the_statement_mentions_the_effect_size` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the question a hypothesis test answers
- [ ] Walk through all five steps, naming which is the hard one
- [ ] Why is shuffling labels a valid way to build the null distribution?
- [ ] State what p means, and three things it does not
- [ ] Why can a permutation p-value never be exactly zero?
- [ ] Why does the t-test work — in terms of what you generated today?
- [ ] Why "fail to reject" rather than "accept"?
- [ ] Why must an effect size travel with every p-value?

## Commit

- [ ] `./m check && ./m done 69` succeeded
