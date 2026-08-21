# Day 44 — CHECKLIST

**IDs covered:** DB-04 · **Principles served:** 1, 7, 8, 11

## Demo command

```bash
uv run python days/day-44/lab/constraints.py
uv run python -m pytest tests/test_db.py -v
SETU_LIVE=1 uv run python -m pytest tests/test_db.py -m live -v
```

Expected: six refusals with named constraints, the savepoint recovery, a working upsert — then all
tests green.

## Setup

- [ ] `./m start 44` and `./m scaffold 44` run
- [ ] `sql/003_constraints.sql` written and applied
- [ ] `days/day-44/lab/constraints.py` created
- [ ] No new packages installed

## DB-04 — why the database

- [ ] Can name **four** paths into the data that bypass your Python
- [ ] Can state why a database constraint is the only real guarantee
- [ ] Filled in the natural-vs-surrogate key table from memory
- [ ] Can say which Setu uses where, and why

## The constraints

- [ ] Ran `the_five_constraints()` and saw all six refusals
- [ ] Read `exc.diag.constraint_name` for each
- [ ] Every constraint in your SQL is **explicitly named**
- [ ] Built a **partial** unique index with `WHERE col IS NOT NULL`
- [ ] Confirmed it allows many NULLs and rejects a duplicate value
- [ ] Used `NOT VALID` then `VALIDATE CONSTRAINT`; can say what that avoids on a large table
- [ ] Added a composite unique index on `(paper_id, position)`
- [ ] Can say what that constrains that the primary key does not

## Transactions

- [ ] Ran `transactions_and_partial_failure()`
- [ ] Saw a plain `SELECT` fail with `InFailedSqlTransaction`
- [ ] Used `SAVEPOINT` / `ROLLBACK TO SAVEPOINT` to recover
- [ ] Can explain why a bulk loader needs savepoints

## Upsert

- [ ] Used `ON CONFLICT ... DO UPDATE` with `EXCLUDED`
- [ ] Can say what `EXCLUDED` refers to
- [ ] Connected it to Day 227's re-runnable ingestion

## Costs

- [ ] Read `what_constraints_cost()`
- [ ] Can name what every `UNIQUE` constraint implies
- [ ] Can say what a foreign key without an index on the referencing column costs

## Build brief

- [ ] `CONSTRAINT_MESSAGES` written for every named constraint
- [ ] `friendly_integrity_error` — **TODO(me)**: maps names, never leaks SQL or parameters
- [ ] `upsert` — **TODO(me)**: batched, idempotent, updates only listed columns
- [ ] `insert_many_skipping_bad` — **TODO(me)**: savepoint per row, integrity errors only
- [ ] `assert_no_duplicate_natural_keys` — **TODO(me)**: names offenders, connected to Day 79

## Tests that must be able to fail

- [ ] `test_partial_unique_allows_many_nulls` — green
- [ ] `test_partial_unique_rejects_a_duplicate_value` — green
- [ ] **Used a plain `UNIQUE`, watched one of the pair go red, switched to a partial index** ← do not skip
- [ ] `test_composite_unique_prevents_a_duplicate_position` — green
- [ ] `test_composite_unique_still_allows_a_second_author` — green
- [ ] **Indexed `paper_id` alone, watched the "still allows" test go red, fixed it** ← do not skip
- [ ] `test_constraints_file_names_every_constraint` — green
- [ ] `test_constraint_messages_cover_the_schema` — green ← **today's real assessment**
- [ ] **Added a new named constraint without a message, watched it go red, added one** ← do not skip
- [ ] `test_friendly_error_never_leaks_sql` — green
- [ ] `test_friendly_error_names_an_unmapped_constraint` — green
- [ ] Live: `test_every_constraint_produces_a_useful_message` — three green cases
- [ ] Live: `test_upsert_is_idempotent` — green
- [ ] Live: `test_upsert_updates_only_the_listed_columns` — green
- [ ] **Made the upsert overwrite every column, watched the title assertion go red, fixed it** ← do not skip
- [ ] Live: `test_bad_rows_are_skipped_not_fatal` — green
- [ ] Live: `test_no_duplicate_natural_keys` — green
- [ ] All test rows cleaned up afterwards

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is the database the only layer that guarantees a rule?
- [ ] Why does every constraint need an explicit name?
- [ ] When do you want a partial unique index rather than a plain `UNIQUE`?
- [ ] Why add a constraint `NOT VALID` first on a large table?
- [ ] What happens to a transaction after any error, and how do you recover?
- [ ] What does `EXCLUDED` mean in an upsert?
- [ ] Name two costs of a unique constraint
- [ ] How does a missing unique constraint inflate a test score on Day 79?

## Commit

- [ ] `./m check && ./m done 44` succeeded
