# Day 84 — CHECKLIST

**IDs covered:** EDA-01, EDA-02 · **Principles served:** 1, 7, 9, 10

## Demo command

```bash
uv run python days/day-84/lab/eda_loop.py
uv run python -m pytest tests/test_eda.py -v
```

Expected: the seven-part walkthrough ending with the audit's role, then all EDA tests green.

## Setup

- [ ] `./m start 84` and `./m scaffold 84` run
- [ ] Files created: `days/day-84/lab/eda_loop.py`, `src/setu/eda.py`, `tests/test_eda.py`
- [ ] `eda.py` placed at layer 3

## EDA-01 — the loop

- [ ] Can state why "explore the data" is not a task
- [ ] Can give an answerable EDA question, and say why it can end
- [ ] Can name the five stages of the loop
- [ ] Ran `the_loop_has_a_stopping_condition()`
- [ ] Can say what a real decision looks like (not a yes or a no)

## Find the eight problems

- [ ] Ran `the_mechanical_pass()` **first** and tried to spot all eight
- [ ] Recorded how many you found unaided: ______ / 8
- [ ] Then read `the_eight_problems()` and matched each to an earlier day
- [ ] Can explain the `days_until_churn` missingness tell
- [ ] Can say why that signature works **without** knowing the column's meaning

## What a machine cannot see

- [ ] Read all five domain questions
- [ ] Can say who answers them
- [ ] Can state the attention argument in one sentence

## Honesty

- [ ] Ran `exploration_generates_hypotheses_not_findings()`
- [ ] Can say why the churn-by-plan difference is not a finding
- [ ] Can connect it to Day 74 and Principle 15
- [ ] Can state what the output of EDA actually is

## Build brief

- [ ] `audit` — **TODO(me)**: nine finding types, cites the day, reuses Day 34
- [ ] `missingness_tracks_target` — **TODO(me)**: the leak signature
- [ ] `eda_question` — **TODO(me)**: crude by design, documented as such
- [ ] `eda_log` / `record_check` / `conclude` — **TODO(me)**: open questions survive
- [ ] `audit_summary` — **TODO(me)**: never says "clean"
- [ ] Did **not** reimplement `quality_report`
- [ ] Can explain why every finding cites a lesson

## Tests that must be able to fail

- [ ] `test_duplicate_rows_are_found` — green
- [ ] `test_a_constant_column_is_found` — green
- [ ] `test_an_identifier_column_is_found` — green
- [ ] `test_impossible_values_are_found` — green
- [ ] `test_an_integer_column_that_looks_nominal_is_flagged` — green
- [ ] `test_a_float_column_that_looks_ordinal_is_flagged` — green
- [ ] `test_a_suspect_token_column_is_flagged` — green
- [ ] `test_findings_cite_the_day_that_explains_them` — green ← **today's real assessment**
- [ ] **Dropped the `day` field, watched it go red, restored it** ← do not skip
- [ ] `test_findings_are_sorted_by_severity` — green
- [ ] `test_the_audit_reuses_day_34s_quality_report` — green
- [ ] `test_the_audit_does_not_mutate` / `..._is_json_serialisable` — green
- [ ] `test_the_audit_works_without_a_target` — green
- [ ] `test_domain_questions_are_produced` — green
- [ ] `test_missingness_that_tracks_the_target_is_caught` — green
- [ ] **Flagged every column with missing values, watched the `innocent` assertion go red** ← do not skip
- [ ] `test_missingness_check_ignores_complete_columns` — green
- [ ] `test_missingness_check_rejects_a_multiclass_target` — green
- [ ] `test_an_unanswerable_question_is_rejected` — green
- [ ] `test_an_answerable_question_is_accepted` — green
- [ ] `test_the_log_refuses_an_unanswerable_question` — green
- [ ] `test_an_empty_question_raises` — green
- [ ] `test_a_decision_with_no_checks_is_refused` — green
- [ ] `test_open_questions_survive_into_the_decision` — green
- [ ] `test_a_decision_ignoring_open_questions_is_warned_about` — green
- [ ] `test_record_check_does_not_mutate` — green
- [ ] `test_patterns_go_in_hypotheses_not_the_decision` — green
- [ ] `test_the_summary_never_claims_the_data_is_clean` — green
- [ ] `test_the_summary_names_the_blocking_issues` — green
- [ ] `test_the_summary_counts_outstanding_domain_questions` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does an unanswerable question produce an unbounded exploration?
- [ ] Name the eight planted problems and the day each maps to
- [ ] Why is missingness that tracks the target a leak signature?
- [ ] Name three things an audit cannot tell you
- [ ] Why is a pattern noticed during EDA not a finding?
- [ ] What is the actual output of an EDA session?
- [ ] Why must every finding cite a lesson?
- [ ] Why must the summary avoid the word "clean"?

## Commit

- [ ] `./m check && ./m done 84` succeeded
