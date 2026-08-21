# Day 35 — CHECKLIST · **PHASE 4 GATE**

**IDs covered:** PD-15 · **Principles served:** 1, 7, 10, 13 · **Artifact:** ADR-002

## Demo command

```bash
uv run python days/day-35/lab/benchmark.py
uv run python -m pytest tests/test_frames.py -v
uv run python -m pytest -q
```

Expected: six benchmark sections with real timings and a printed query plan, then all frame tests
green, then the **whole** suite green.

## Setup

- [ ] `./m start 35` and `./m scaffold 35` run
- [ ] `uv add "polars==<pin>" "duckdb==<pin>"` — both exact-pinned
- [ ] Versions from **your** Day-1 verify run; drift logged
- [ ] Files created: `days/day-35/lab/benchmark.py`, `docs/adr/ADR-002-dataframe-engine.md`
- [ ] Fixture built into gitignored `data/processed/`

## PD-15 — the benchmark

- [ ] Ran all six sections
- [ ] Ran each timing **three times** and recorded the median, not the first run
- [ ] Confirmed the three engines returned the **same row count** before trusting any number
- [ ] Recorded: full read — pandas ____s · polars ____s · duckdb ____s
- [ ] Recorded: two-column read — pandas ____s · polars ____s · duckdb ____s
- [ ] Recorded: groupby — pandas ____s · polars ____s · duckdb ____s
- [ ] Recorded: string work — pandas ____s · polars ____s
- [ ] **Printed `plan.explain()` and found the pushed-down projection and predicate**
- [ ] Can explain why laziness wins by *avoiding work*, not by running faster
- [ ] Queried a pandas frame from DuckDB **by variable name**
- [ ] Aggregated the file with DuckDB without loading it
- [ ] Can state the one capability that is possible/impossible rather than fast/slow

## ADR-002 — the artifact (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** states Setu's realistic data sizes, not hypothetical ones
- [ ] **Four options** considered, including the mixed stack
- [ ] **Your measured table** included, with the machine and row count stated
- [ ] The `explain()` output quoted or summarised
- [ ] **Decision** in one sentence
- [ ] **Consequences** honestly names what a mixed stack costs
- [ ] **A threshold** given as a number: below ______ rows, do not switch
- [ ] **What would change our minds** is specific and falsifiable
- [ ] Written from **your** numbers, not from §4's suggested answer
- [ ] Cold-read a day later, reviewer hat on, and signed

## Build brief

- [ ] `engine_note` — **TODO(me)**: returns ADR-002's decision sentence
- [ ] `to_arrow` — **TODO(me)**: returns a pyarrow Table, refuses `object` columns

## Tests that must be able to fail

- [ ] `test_engine_note_is_a_real_sentence` — green
- [ ] `test_to_arrow_round_trips` — green
- [ ] `test_to_arrow_refuses_object_columns` — green
- [ ] `test_adr_002_exists_and_has_numbers` — green ← **the gate test**
- [ ] **Removed the measured numbers from the ADR, watched it go red, put them back** ← do not skip
- [ ] `test_all_three_engines_are_pinned` — green
- [ ] `test_phase_4_frames_module_is_complete` — green (all 25 functions)

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is each of the three tools actually betting on?
- [ ] What is the difference between `read_parquet` and `scan_parquet`, and why does it matter?
- [ ] Explain predicate and projection pushdown using the plan you printed
- [ ] Which of the three differences is possible-vs-impossible rather than fast-vs-slow?
- [ ] Why is Arrow the reason a mixed stack is practical?
- [ ] Why must a benchmark assert the results agree before reporting timings?
- [ ] What is your threshold, and why is stating it the most important line in the ADR?
- [ ] What does a mixed stack cost that a single-engine stack does not?

## PHASE 4 GATE

- [ ] ADR-002 written with real numbers and cold-read
- [ ] pandas, polars and duckdb all exact-pinned in `pyproject.toml`
- [ ] `test_phase_4_frames_module_is_complete` green
- [ ] Produced one clean dataset end to end: `read_table` → `safe_merge` → `assert_quality` → `write_table`
- [ ] `test_no_chained_assignment_anywhere_in_src` **still green** after ten days of edits
- [ ] `test_no_imputation_anywhere_in_src` still green (Day 30's rule)
- [ ] Layering test still green (`frames` is layer 2)
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 35` succeeded and `./m status` shows Phases 0–4 complete
