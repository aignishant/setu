# Day 51 — CHECKLIST · **PHASE 6 GATE**

**IDs covered:** DB-12 · **Principles served:** 1, 5, 7, 10 · **Artifact:** ADR-004

## Demo command

```bash
uv run python days/day-51/lab/bakeoff.py
uv run python -m pytest tests/test_db.py tests/test_mongo.py -q
SETU_LIVE=1 uv run python -m pytest -v
```

Expected: three timed questions plus storage numbers, ending with `cleaned up both databases`, then
the whole suite green.

## Setup

- [ ] `./m start 51` and `./m scaffold 51` run
- [ ] Files created: `days/day-51/lab/bakeoff.py`, `docs/adr/ADR-004-sql-vs-nosql.md`
- [ ] No new packages installed

## DB-12 — the bake-off

- [ ] Ran each timing **three times** and took the median
- [ ] Confirmed the engines **agree on the row count** before trusting any timing
- [ ] Q1 fetch-one — postgres ______ ms · mongo ______ ms
- [ ] Q2 aggregate — postgres ______ ms · mongo ______ ms · pandas ______ ms
- [ ] Q3 join — postgres ______ ms · mongo ______ ms
- [ ] Storage — postgres ______ MiB · mongo ______ MiB for 20k records
- [ ] Calculated roughly how many documents fit in the 512 MB Atlas tier
- [ ] Can say **why** Q1 favours the document model
- [ ] Can say why pandas winning Q2 is **not** a database result
- [ ] **Read both Q3 implementations**, not just the times
- [ ] Can describe the `$push`-into-an-array shape and why it does not scale
- [ ] `reports/day51_bakeoff.json` written

## The alternative

- [ ] Read `the_jsonb_option()`
- [ ] Can state how Postgres stores, indexes and queries a document
- [ ] Can give the honest counter-arguments **including** the one that cuts against the split

## ADR-004 — the artifact (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** names Setu's real data and both free-tier limits
- [ ] **Four options** considered, including Postgres-only with `jsonb` and Parquet+DuckDB
- [ ] **Your measured table** included, with machine, record count and median-of-three
- [ ] The **structural** Q3 observation recorded, not just the ratio
- [ ] **Decision** in one sentence
- [ ] **Consequences** names the operational cost of two databases
- [ ] **The consistency question answered**: which is the source of truth, and what happens
      when one write succeeds and the other fails
- [ ] **A threshold** given: at what point would you collapse to one?
- [ ] **What would change our minds** is specific and falsifiable
- [ ] Written from **your** numbers, not §4's suggested answer
- [ ] Cold-read a day later, reviewer hat on, and signed

## Build brief

- [ ] `database_report` — **TODO(me)**: both databases, never raises, **reuses** both health checks
- [ ] `assert_source_of_truth` — **TODO(me)**: encodes the ADR's boundary rule, including its asymmetry
- [ ] Did **not** reimplement either health check

## Tests that must be able to fail

- [ ] `test_database_report_never_raises` — green
- [ ] `test_database_report_is_json_serialisable` — green
- [ ] `test_database_report_reuses_both_healthchecks` — green ← an **architecture** test
- [ ] **Reimplemented one health check inline, watched it go red, reverted** ← do not skip
- [ ] `test_adr_004_exists_and_engages_with_the_alternative` — green ← **the gate test**
- [ ] **Deleted the `jsonb` discussion from the ADR, watched it go red, restored it** ← do not skip
- [ ] `test_bakeoff_evidence_file_exists` — green
- [ ] `test_phase_6_db_module_is_complete` — green
- [ ] `test_phase_6_mongo_module_is_complete` — green
- [ ] **live** `test_database_report_reaches_both` — green
- [ ] **live** `test_source_of_truth_passes_on_consistent_data` — green
- [ ] **live** `test_a_paper_without_a_raw_document_is_fine` — green ← the **asymmetry**
- [ ] **Made the check require both sides, watched this go red, fixed it** ← do not skip

## Budget

- [ ] LLM calls today: **0**
- [ ] Postgres round trips: ~200 · Atlas round trips: ~200
- [ ] Confirmed **both** databases are empty of `day51` and `pytest*` test data

## Understanding check — answer out loud

- [ ] Reframe "SQL or NoSQL?" as the question you should actually answer
- [ ] Which engine won which of the three questions, and why?
- [ ] Why is pandas winning Q2 not evidence about databases?
- [ ] Describe the Mongo Q3 implementation and the structural problem with it
- [ ] What does Postgres `jsonb` do, and what is the honest case for using it instead?
- [ ] Which argument for one database cuts against your decision?
- [ ] Name Setu's source of truth, and what happens when the other side's write fails
- [ ] Why does that asymmetry remove the need for a distributed transaction?

## PHASE 6 GATE

- [ ] Bake-off runs clean and writes `reports/day51_bakeoff.json`
- [ ] ADR-004 written with real numbers, the `jsonb` engagement, and the consistency answer
- [ ] ADR-004 cold-read and signed
- [ ] The same question answered in SQL, in an aggregation pipeline, and in pandas — all agreeing
- [ ] `test_phase_6_db_module_is_complete` and `test_phase_6_mongo_module_is_complete` green
- [ ] Every destructive helper still refuses an empty filter (Day 50)
- [ ] No string-formatted SQL anywhere in `src/` (Day 47)
- [ ] Layering test still green (`db` and `mongo` are layer 2)
- [ ] Both free tiers left clean; nothing counting against your quota
- [ ] `./m check` green; CI green on a push (live tests skipped)
- [ ] `./m done 51` succeeded and `./m status` shows Phases 0–6 complete
