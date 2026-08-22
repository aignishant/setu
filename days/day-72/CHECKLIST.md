# Day 72 — CHECKLIST

**IDs covered:** ST-19 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-72/lab/bayes.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the ten-part report ending with the false-discovery calculation, then all stats tests green.

## Setup

- [ ] `./m start 72` and `./m scaffold 72` run
- [ ] `days/day-72/lab/bayes.py` created
- [ ] No new packages installed

## ST-19 — the theorem

- [ ] Reproduced Day 63's disease answer using the formula
- [ ] Can name all four terms and say what each contributes
- [ ] Can read the theorem as a **sentence**, not a formula
- [ ] Can say what makes it a **loop**

## Odds form

- [ ] Confirmed `P(data)` cancels in the odds form
- [ ] Can state `posterior odds = prior odds × likelihood ratio` from memory
- [ ] Can explain "extraordinary claims require extraordinary evidence" arithmetically
- [ ] Can say what `LR = 1` means — and what it does **not** mean

## Updating

- [ ] Ran `sequential_updating()` and watched belief move
- [ ] Confirmed the belief moves in **both** directions
- [ ] Can say what a p-value cannot do here
- [ ] Ran `order_does_not_matter()` with three orderings
- [ ] Can say why they agree

## The prior

- [ ] Ran `the_prior_matters_then_it_does_not()` and **read the whole table**
- [ ] Recorded the three posteriors at n=0 and at n=500
- [ ] Can state the honest account of the prior objection
- [ ] Used conjugate updating and confirmed it is pure addition
- [ ] Can express a Beta prior's strength in pseudo-observations

## Credible vs confidence

- [ ] Can state what a credible interval says
- [ ] Can state what a confidence interval says (Day 68)
- [ ] Can say which one may make a probability statement about the parameter
- [ ] Can name the price of that

## The punchline

- [ ] Ran `why_significant_findings_are_often_false()` at three base rates
- [ ] Recorded PPV at a 1% base rate: ______
- [ ] Can state the difference between the false-positive rate and the false-discovery rate
- [ ] Can say which earlier day this is arithmetically identical to
- [ ] Read `what_a_bayes_factor_adds()`; can say what it expresses that a p-value cannot
- [ ] Can name its cost

## Build brief

- [ ] `bayes_update` — **TODO(me)**: validates, reports `shift`, does not mutate
- [ ] `sequential_update` — **TODO(me)**: returns history for plotting, order-independent
- [ ] `odds_form` — **TODO(me)**: strength labels, refuses certainty
- [ ] `beta_posterior` — **TODO(me)**: prior strength in observations, credible interval
- [ ] `false_discovery_rate` — **TODO(me)**: **reuses Day 63**, returns counts
- [ ] `describe_credible_interval` — **TODO(me)**: mentions the prior
- [ ] Can explain why `false_discovery_rate` must not reimplement Day 63

## Tests that must be able to fail

- [ ] `test_the_disease_test_reproduced` — green
- [ ] `test_the_posterior_sums_to_one` — green
- [ ] `test_equal_likelihoods_leave_the_prior_unchanged` — green
- [ ] `test_a_prior_that_does_not_sum_to_one_raises` — green, total named
- [ ] `test_mismatched_hypothesis_sets_raise` — green
- [ ] `test_impossible_data_raises_with_a_useful_message` — green
- [ ] `test_bayes_update_does_not_mutate` — green
- [ ] `test_sequential_updating_converges_on_the_truth` — green
- [ ] `test_order_does_not_change_the_posterior` — green
- [ ] `test_batch_equals_one_at_a_time` — green
- [ ] **Averaged instead of multiplying, watched both commutativity tests go red, fixed it** ← do not skip
- [ ] `test_belief_moves_in_both_directions` — green
- [ ] `test_history_is_returned_for_plotting` — green
- [ ] `test_sequential_rejects_no_observations` — green
- [ ] `test_odds_form_matches_the_probability_form` — green
- [ ] `test_a_likelihood_ratio_of_one_is_uninformative_not_no_effect` — green
- [ ] `test_strong_evidence_against_a_strong_prior_still_leaves_doubt` — green
- [ ] `test_certainty_cannot_be_updated` — green
- [ ] `test_odds_form_rejects_a_non_positive_ratio` — green
- [ ] `test_conjugate_update_is_addition` — green
- [ ] `test_prior_strength_is_expressed_in_observations` — green
- [ ] `test_priors_disagree_at_small_n_and_agree_at_large_n` — green
- [ ] `test_the_credible_interval_narrows_with_data` — green
- [ ] `test_beta_posterior_rejects_bad_inputs` — green
- [ ] `test_a_significant_result_can_be_more_likely_false_than_true` — green ← **today's real assessment**
- [ ] `test_a_high_prior_makes_significance_trustworthy` — green
- [ ] `test_lower_alpha_improves_the_discovery_rate` — green
- [ ] `test_the_counts_reconstruct_the_rate` — green
- [ ] `test_false_discovery_reuses_day_63` — green
- [ ] **Reimplemented the calculation inline, watched it go red, reused Day 63** ← do not skip
- [ ] `test_a_credible_interval_may_state_a_probability` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State Bayes' theorem as a sentence about beliefs
- [ ] Why does the odds form make the mechanism clearer?
- [ ] What does `LR = 1` tell you?
- [ ] Why does updating order not matter?
- [ ] When does the prior objection bite, and when does it dissolve?
- [ ] What does a credible interval say that a confidence interval may not?
- [ ] Why is α not the false-discovery rate?
- [ ] Why can a Bayes factor favour the null when a p-value cannot?

## Commit

- [ ] `./m check && ./m done 72` succeeded
