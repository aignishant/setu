# Day 90 — CHECKLIST · **PHASE 11 GATE**

**IDs covered:** EDA-08 · **Principles served:** 1, 7, 10, 14, 15 · **Artifact:** a report + ADR-006

## Demo command

```bash
uv run python days/day-90/lab/report.py
uv run python -m pytest tests/test_eda.py -v
uv run python -m pytest -q
```

Expected: six steps ending with the comparison-count disclosure, then the whole suite green.

## Setup

- [ ] `./m start 90` and `./m scaffold 90` run
- [ ] Files created: `days/day-90/lab/report.py`, `reports/day90_eda_report.md`,
      `docs/adr/ADR-006-eda-decision.md`

## The rule

- [ ] Can state the test of an EDA report in one sentence
- [ ] Can name all four accumulated obligations, and the day each comes from
- [ ] Can say why "the data does not support this project" is a valuable outcome

## EDA-08 — the report, written in order

**The decision section comes BEFORE opening the data.**

- [ ] **The decision** — one sentence, naming what someone will do differently
- [ ] **What I would need to see** — written before looking, and it **permits stopping**
- [ ] **The data** — source, licence, date, *how it was collected*, and which **split**
- [ ] **What the audit found** — from `audit(df)`, blocking issues first
- [ ] **Univariate** — only variables that bear on the decision
- [ ] **Bivariate** — effect sizes ranked, with subgroup stability for anything relied on
- [ ] **Leakage screen** — and for each, **whether you can explain it**
- [ ] **Comparisons made** — the total, uncorrected
- [ ] **Recommendation** — proceed / proceed with changes / do not proceed
- [ ] **What would change this** — specific and falsifiable
- [ ] **Open questions** — things the data cannot answer

## Building it

- [ ] Script refuses without a stated decision — **verified by blanking the section once**
- [ ] Every number built from the **train** split
- [ ] Every step reused a Phase-11 function; **no new analysis code was needed**
- [ ] Screening ranked by effect size and disclosed its comparison count
- [ ] Suspected leaks surfaced, with the "can you explain it?" question asked
- [ ] Subgroup stability checked for the top features
- [ ] Four figures, each tied to the decision
- [ ] `assert_pack_is_publishable` passed — Day 37 and Day 40 lints still apply
- [ ] `reports/day90_eda.json` written

## Tests that must be able to fail

- [ ] `test_the_report_states_a_decision` — green
- [ ] `test_the_report_has_every_required_section` — green
- [ ] `test_the_success_criteria_were_written_before_looking` — green ← **today's real assessment**
- [ ] **Wrote criteria with no stopping condition, watched it go red, added one** ← do not skip
- [ ] `test_the_report_names_the_split_it_used` — green
- [ ] `test_the_report_records_provenance` — green
- [ ] `test_the_recommendation_is_one_of_three` — green
- [ ] `test_the_json_payload_exists_and_discloses_comparisons` — green
- [ ] `test_the_payload_was_built_from_the_train_split` — green
- [ ] `test_nothing_in_the_payload_is_called_a_finding` — green
- [ ] `test_suspected_leaks_are_surfaced_not_buried` — green
- [ ] `test_the_script_refuses_without_a_stated_decision` — green
- [ ] `test_the_figures_exist_and_passed_the_lints` — green
- [ ] `test_adr_006_records_what_changed` — green
- [ ] `test_adr_006_names_concrete_changes` — green
- [ ] `test_adr_006_lists_what_remains_unconfirmed` — green
- [ ] `test_stopping_is_a_permitted_outcome` — green
- [ ] `test_phase_11_eda_module_is_complete` — green (28 functions)
- [ ] `test_the_report_pipeline_runs_end_to_end` — green

## ADR-006 — the artifact (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** names the decision and what the default would have been
- [ ] **What the data said** — two or three findings that bore on it, with effect sizes and intervals
- [ ] **The decision** in one sentence
- [ ] **What changed** — concrete: features dropped, target framing, split, metric, exclusions
- [ ] **What remains unconfirmed** — named as hypotheses for Phase 12
- [ ] **What would change our minds**
- [ ] Acknowledges that stopping was an available outcome
- [ ] Cold-read a day later and signed

## The human check

- [ ] **Read the report as if you had not written it.** Would you act on it?
- [ ] Is there a single section that could be deleted without loss? Delete it.
- [ ] Does the recommendation follow from the evidence shown, or from what you expected?

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the test of an EDA report?
- [ ] Why does the decision come before the data?
- [ ] Why must the success criteria permit a negative outcome?
- [ ] Why is everything in the report a hypothesis?
- [ ] Why disclose the comparison count?
- [ ] What does an unexplained leak mean for your conclusion?
- [ ] Why rank by effect size rather than p-value?
- [ ] Why is "do not proceed" sometimes the most valuable outcome?

## PHASE 11 GATE

- [ ] Report written with the decision first and falsifiable criteria
- [ ] Assembly script runs end to end and refuses without a decision
- [ ] Every number from the **train** split
- [ ] Comparison count disclosed; nothing called a finding
- [ ] Suspected leaks surfaced with their explanation status
- [ ] Figure pack passes the Phase 5 lints
- [ ] ADR-006 written, naming concrete changes, cold-read
- [ ] `test_phase_11_eda_module_is_complete` green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 90` succeeded and `./m status` shows Phases 0–11 complete
