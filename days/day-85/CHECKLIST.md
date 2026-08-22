# Day 85 — CHECKLIST

**IDs covered:** EDA-03 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-85/lab/exploring.py
uv run python -m pytest tests/test_eda.py -v
```

Expected: the eight-part report ending with the honest inventory, then all eda tests green.

## Setup

- [ ] `./m start 85` and `./m scaffold 85` run
- [ ] `days/day-85/lab/exploring.py` created
- [ ] No new packages installed
- [ ] Confirmed every function looks at the **training split only**

## The discipline

- [ ] Can state why EDA has a p-hacking problem by construction
- [ ] Can state the resolution in one sentence
- [ ] Can say what makes uncorrected looking legitimate here
- [ ] Can name the two earlier days that make it work

## EDA-03 — univariate

- [ ] Ran `one_variable_at_a_time()`; reused Days 59, 60 and 61 rather than recomputing
- [ ] Read the mean-median gap and the skew column **together**
- [ ] Identified which variable needs a median in every summary
- [ ] Ran `the_domain_question()` and found the impossible values
- [ ] Can state the difference between an impossible value and an outlier
- [ ] Can say why the responses differ

## Bivariate

- [ ] Filled in the four-cell type-pair table from memory
- [ ] Ran numeric~numeric; checked the Pearson–Spearman gap and the leverage
- [ ] Ran numeric~categorical; reported **median and IQR**, and eta²
- [ ] Can say why eta² matters more than p at n=3,000
- [ ] Ran categorical~categorical; read Cramér's V and the largest residual
- [ ] Can say what the residual adds that χ² does not

## The leak check

- [ ] Ran `the_leak_check()` and found the planted leak
- [ ] Can explain how `citations_per_page` is built
- [ ] Can state where the fix comes from (the definition, not the number)
- [ ] Can name the Day-39 tool this is a per-feature version of

## Simpson's paradox

- [ ] Ran `simpsons_paradox()` and **read both blocks**
- [ ] Recorded the overall rates and the within-department rates
- [ ] Can explain the mechanism in one sentence
- [ ] Can name the two earlier days this combines

## The inventory

- [ ] Ran `what_exploration_produces()`
- [ ] Can list the three categories it produces
- [ ] Can say what it explicitly does **not** produce
- [ ] Noted the comparison count

## Build brief

- [ ] `univariate` — **TODO(me)**: level-aware, reuses Phase 8, separates bugs from outliers
- [ ] `bivariate` — **TODO(me)**: dispatches on the **type pair**, always reports an effect size
- [ ] `screen_features` — **TODO(me)**: ranks by effect size, counts comparisons, no correction
- [ ] `check_subgroup_stability` — **TODO(me)**: detects reversal and weakening, names the confounder
- [ ] `exploration_report` — **TODO(me)**: hypotheses, problems, drops — never "findings"
- [ ] Can explain why screening deliberately does **not** correct its p-values

## Tests that must be able to fail

- [ ] `test_univariate_reuses_the_phase_8_helpers` — green
- [ ] `test_univariate_respects_the_level` — green
- [ ] `test_a_domain_violation_is_a_bug_not_an_outlier` — green
- [ ] `test_an_extreme_value_is_flagged_as_an_outlier_not_a_bug` — green
- [ ] **Merged the two flag categories, watched both go red, separated them again** ← do not skip
- [ ] `test_univariate_reports_missingness` — green
- [ ] `test_univariate_names_existing_columns_when_missing` — green
- [ ] `test_bivariate_dispatches_on_the_type_pair` — green (three pairs)
- [ ] `test_ordinal_forces_a_rank_method` — green
- [ ] `test_bivariate_always_reports_an_effect_size` — green
- [ ] `test_significant_but_negligible_is_warned_about` — green
- [ ] `test_bivariate_reports_rows_used` — green
- [ ] `test_screening_ranks_by_effect_size_not_p_value` — green
- [ ] **Sorted by p-value instead, watched it go red, fixed it** ← do not skip
- [ ] `test_screening_finds_the_planted_leak` — green (and does not flag `noise`)
- [ ] `test_screening_counts_its_comparisons` — green
- [ ] `test_screening_calls_itself_exploratory` — green
- [ ] `test_screening_does_not_correct_its_p_values` — green
- [ ] `test_simpsons_paradox_is_detected` — green
- [ ] `test_a_stable_relationship_is_not_flagged` — green
- [ ] **Made the stability check always warn, watched the stable case go red, fixed it** ← do not skip
- [ ] `test_small_groups_are_skipped` / `test_too_few_groups_raises` — green
- [ ] `test_the_report_never_calls_anything_a_finding` — green ← **today's real assessment**
- [ ] `test_the_report_separates_problems_from_hypotheses` — green
- [ ] `test_the_report_lists_leaks_with_reasons` — green
- [ ] `test_the_report_discloses_the_comparison_count` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is EDA a multiple-comparisons problem, and what makes it legitimate anyway?
- [ ] Give the four-cell type-pair table and one method for each
- [ ] Why rank by effect size rather than p-value?
- [ ] How do you tell an impossible value from an outlier, and why does it matter?
- [ ] Explain Simpson's paradox with the admissions example
- [ ] What does a bivariate number actually describe?
- [ ] What are the three things exploration produces?
- [ ] Why is "finding" a banned word in the report?

## Commit

- [ ] `./m check && ./m done 85` succeeded
