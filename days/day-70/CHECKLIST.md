# Day 70 — CHECKLIST

**IDs covered:** ST-17 · **Principles served:** 1, 2, 7, 10

## Demo command

```bash
uv run python days/day-70/lab/errors.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the nine-part report including the winner's-curse table, then all stats tests green.

## Setup

- [ ] `./m start 70` and `./m scaffold 70` run
- [ ] `days/day-70/lab/errors.py` created
- [ ] No new packages installed

## ST-17 — the p-value

- [ ] Ran `p_values_are_uniform_under_the_null()` and **read the whole table**
- [ ] Confirmed the fraction below each threshold equals that threshold
- [ ] Can explain why `P(p < 0.05) = 0.05` is by construction
- [ ] Can state what that implies about 100 honest researchers

## Alpha

- [ ] Can say what α actually is, in one sentence
- [ ] Know where 0.05 came from, and that its originator called it a convenience
- [ ] Can name a field that uses a far stricter α, and why
- [ ] Can state the question to ask when choosing α

## The two error types

- [ ] Filled in the 2×2 table from memory
- [ ] Ran `the_two_error_types()`; confirmed the Type I rate landed on α
- [ ] Can say why that is not a coincidence
- [ ] Recorded the power at n=30 for an 8-point effect: ______

## The trade-off

- [ ] Ran `the_trade_off_is_real()` and **read the two middle columns**
- [ ] Can state why no value of α fixes both error types
- [ ] Can say what does

## Power

- [ ] Ran all three tables in `power_depends_on_four_things()`
- [ ] Can name the four inputs to power
- [ ] Can say which one you control, which you cannot, and which is underrated
- [ ] Read `the_convention_and_what_it_costs()`
- [ ] Can state the implicit cost ratio in "80% power at α=0.05"
- [ ] Can give a situation where that ratio is indefensible

## The winner's curse

- [ ] Ran `the_winners_curse()` and **read the inflation column**
- [ ] Recorded power and inflation at n=10: ______ and ______×
- [ ] Can explain **why** the reported effect is inflated
- [ ] Can state why this makes an underpowered result biased rather than weak

## Null results

- [ ] Ran `a_null_result_is_not_no_effect()` with a real 6-point effect
- [ ] Recorded p ______ and power ______
- [ ] Can distinguish "no effect" from "no power" in one sentence
- [ ] Ran `sample_size_planning()`; confirmed n scales with 1/d²
- [ ] Can say why post-hoc power from the observed effect is circular

## Build brief

- [ ] `error_rates` — **TODO(me)**: simulates both error types
- [ ] `power_analysis` — **TODO(me)**: analytic n, **lists its assumptions**
- [ ] `minimum_detectable_effect` — **TODO(me)**: the honest question once n is fixed
- [ ] `winners_curse` — **TODO(me)**: averages only over significant runs
- [ ] `interpret_null_result` — **TODO(me)**: **can never return "no effect"**
- [ ] Can explain why the conclusion vocabulary is constrained

## Tests that must be able to fail

- [ ] `test_the_type_one_rate_lands_on_alpha` — green
- [ ] `test_the_type_one_rate_follows_whatever_alpha_you_choose` — three green cases
- [ ] `test_power_and_type_two_are_complements` — green
- [ ] `test_power_rises_with_n` / `..._with_the_effect` — green
- [ ] `test_power_falls_as_noise_rises` — green
- [ ] `test_tightening_alpha_costs_power` — green (both directions)
- [ ] `test_error_rates_rejects_bad_inputs` — green
- [ ] `test_required_n_scales_with_one_over_d_squared` — green
- [ ] `test_power_analysis_matches_the_textbook_number` — green (≈63)
- [ ] `test_power_analysis_prediction_matches_simulation` — green
- [ ] **Introduced a factor-of-2 slip in the formula, watched both go red, fixed it** ← do not skip
- [ ] `test_power_analysis_lists_its_assumptions` — green
- [ ] `test_power_analysis_rejects_incoherent_requests` — green
- [ ] `test_the_minimum_detectable_effect_shrinks_with_n` — green
- [ ] `test_mdes_round_trips_with_power_analysis` — green
- [ ] `test_underpowered_studies_inflate_the_effect` — green ← **today's real assessment**
- [ ] `test_well_powered_studies_report_honest_effects` — green
- [ ] `test_inflation_falls_as_power_rises` — green
- [ ] **Averaged over ALL runs instead of significant ones, watched inflation vanish, fixed it** ← do not skip
- [ ] `test_winners_curse_handles_zero_significant_runs` — green
- [ ] `test_a_null_result_at_low_power_is_called_underpowered` — green
- [ ] `test_a_null_result_at_high_power_is_evidence_of_no_meaningful_effect` — green
- [ ] `test_it_never_concludes_no_effect` — green (four sample sizes)
- [ ] `test_a_significant_p_short_circuits` — green
- [ ] `test_interpret_requires_a_smallest_effect_of_interest` — green
- [ ] `test_p_values_are_uniform_under_the_null` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Fill in the 2×2 error table and say which cell you choose
- [ ] Why is P(p < 0.05) exactly 0.05 under a true null?
- [ ] Why can no choice of α reduce both error types?
- [ ] Name the four inputs to power and which lever is underrated
- [ ] What cost ratio does "80% power at α=0.05" implicitly assume?
- [ ] Explain the winner's curse and why it makes results biased, not weak
- [ ] Why is post-hoc power circular?
- [ ] Distinguish "no effect" from "no power" and say how you would tell them apart

## Commit

- [ ] `./m check && ./m done 70` succeeded
