# Day 75 — CHECKLIST · **PHASE 9 GATE**

**IDs covered:** ST-22 · **Principles served:** 1, 7, 10, 14, 15 · **Artifact:** pre-registration + ADR-005

## Demo command

```bash
uv run python days/day-75/lab/analysis.py
uv run python -m pytest tests/test_stats.py -v
uv run python -m pytest -q
```

Expected: eight steps ending with the disclosure statement, then the whole suite green.

## Setup

- [ ] `./m start 75` and `./m scaffold 75` run
- [ ] Files created: `days/day-75/lab/analysis.py`, `reports/day75_preregistration.md`,
      `docs/adr/ADR-005-statistical-standards.md`

## The ordering

- [ ] Can state the four-step ordering from memory
- [ ] Can say why the arrow from step 1 to step 2 is the whole method
- [ ] Can name all six things every claim must report, and the day each comes from

## ST-22 — the pre-registration

**Written and committed BEFORE running anything.**

- [ ] **Question** — one sentence, and answerable **no**
- [ ] **Data** — source, size, what one row is, exclusion rules stated now
- [ ] **Hypothesis** — H₀ and H₁; direction only if committing
- [ ] **Primary outcome** — exactly **one**
- [ ] **Secondary outcomes** — listed exhaustively
- [ ] **Test** — with the level of measurement cited, and `choose_test` consulted
- [ ] **α and correction** — a number, with a reason, and the method across m comparisons
- [ ] **Smallest effect of interest** — the section that does the most work
- [ ] **Power** — required n, or the MDES if n is fixed
- [ ] **Stopping rule** — decided now
- [ ] **What would change our minds**
- [ ] **Committed to git before the results file** ← the timestamp is the claim

## Running it

- [ ] Script refuses to run without the pre-registration — **verified by deleting it once**
- [ ] Assumptions checked **before** the test, in Day 71's severity order
- [ ] Both the parametric and the permutation test run, and agree
- [ ] Effect size and interval reported, phrased via `describe_interval`
- [ ] `interpret_null_result` consulted; MDES recorded
- [ ] Exploratory analyses run, **labelled**, and left uncorrected
- [ ] Comparison count disclosed in the statement
- [ ] `reports/day75_results.json` written

## The honest ending

- [ ] If the primary result was null, it is reported **with its power** — not buried
- [ ] Can say why a pre-registered null is a successful outcome for this gate
- [ ] No exploratory finding was promoted to a conclusion

## Tests that must be able to fail

- [ ] `test_preregistration_exists_and_is_complete` — green
- [ ] `test_the_preregistration_names_one_primary_outcome` — green
- [ ] `test_the_preregistration_states_a_number_for_alpha` — green
- [ ] `test_the_preregistration_was_committed_before_the_results` — green ← **today's real assessment**
- [ ] **Committed the results first on a scratch branch, watched it go red, reordered** ← do not skip
- [ ] `test_results_json_exists_and_records_the_comparison_count` — green
- [ ] `test_the_statement_discloses_the_comparison_count` — green
- [ ] `test_the_statement_is_not_a_probability_claim` — green
- [ ] **Wrote the statement the natural way, watched a banned phrase trip it, fixed it** ← do not skip
- [ ] `test_a_null_result_is_reported_with_its_power` — green
- [ ] `test_adr_005_sets_a_standard_not_a_preference` — green
- [ ] `test_adr_005_names_a_correction_method` — green
- [ ] `test_adr_005_addresses_the_inconvenient_case` — green
- [ ] `test_phase_9_stats_module_is_complete` — green (32 functions)
- [ ] `test_the_full_pipeline_runs_end_to_end` — green

## ADR-005 — the artifact (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** names where statistical claims appear in Setu, including later days
- [ ] **Six rules**, each traceable to the day that demonstrated why
- [ ] α and correction method declared, with reasoning
- [ ] **Consequences** are specific about what this costs
- [ ] **The inconvenient case** answered: what happens when Day 90 finds nothing
- [ ] **What would change our minds**
- [ ] Cold-read a day later and signed

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does writing the plan first make honesty checkable rather than merely claimed?
- [ ] Name the six reporting obligations and the failure each one prevents
- [ ] Why is the smallest effect of interest the section that does the most work?
- [ ] What makes a pre-registered null result a good outcome?
- [ ] Why must exploratory findings be confirmed on fresh data?
- [ ] Why is the comparison count the disclosure?
- [ ] Which phrasings are banned from the report, and why each one?
- [ ] What does ADR-005 commit you to when a result is inconvenient?

## PHASE 9 GATE

- [ ] Pre-registration written, complete, and **committed before** the results
- [ ] `analysis.py` runs end to end and refuses without the pre-registration
- [ ] Statement discloses the comparison count and avoids every banned phrase
- [ ] Null results carry their power or MDES
- [ ] Exploratory work labelled, uncorrected, and not promoted
- [ ] ADR-005 written, addressing the inconvenient case, cold-read
- [ ] `test_phase_9_stats_module_is_complete` green
- [ ] Every Day 74 correction still green; every Day 68 interval phrasing still green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 75` succeeded and `./m status` shows Phases 0–9 complete
