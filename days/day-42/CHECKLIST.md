# Day 42 — CHECKLIST

**IDs covered:** DB-01, DB-02 · **Principles served:** 1, 5, 7, 11

## Demo command

```bash
uv run python days/day-42/lab/connect.py
uv run python -m pytest tests/test_db.py -v
SETU_LIVE=1 uv run python -m pytest tests/test_db.py -m live -v
```

Expected: a live connection report, then the offline schema tests green, then the live tests green.

## Setup

- [ ] `./m start 42` and `./m scaffold 42` run
- [ ] `uv add "psycopg[binary]==<pin>" "sqlalchemy==<pin>"` — exact-pinned, drift logged
- [ ] Using **psycopg 3**, not `psycopg2`
- [ ] `POSTGRES_DSN` present and non-empty in `.env`
- [ ] Used the **pooler** connection string if Supabase offered one
- [ ] Files created: lab, `src/setu/db.py`, `tests/test_db.py`, `sql/001_schema.sql`

## DB-01 — schema design

- [ ] Drew the ER diagram yourself before writing the SQL
- [ ] Can explain why `paper_authors` needs to exist
- [ ] Can say why `position` belongs on the junction table and not on either side
- [ ] Can state 1NF, 2NF and 3NF in one sentence each, with an example of breaking each
- [ ] `sql/001_schema.sql` written, every `CREATE TABLE` guarded with `IF NOT EXISTS`
- [ ] Every foreign key has an explicit `ON DELETE`
- [ ] Chose `SET NULL` vs `CASCADE` per relationship and can defend each choice
- [ ] `CHECK` constraints on year range, non-negative citations, blank titles, venue kind
- [ ] `NOT NULL UNIQUE` used together where "exactly one row per name" is meant
- [ ] Composite primary key on `paper_authors`
- [ ] Indexes on the columns you will filter and join on

## DB-02 — connecting

- [ ] Connected with an explicit `connect_timeout`
- [ ] Used **both** nested `with` blocks; can say what each one closes
- [ ] Ran `the_wake_up_problem()` and watched the retry handle a paused project
- [ ] Wrapped `OperationalError` in `TransientError`; left `ProgrammingError` alone
- [ ] Can explain why retrying a syntax error is pointless
- [ ] Used `%s` placeholders with a parameter tuple — **never** an f-string
- [ ] Confirmed the transaction commits on exit and rolls back on exception
- [ ] Used `row_factory=dict_row` and can say what positional tuples break
- [ ] Read `what_not_to_do()` and can name all five

## Build brief

- [ ] `get_pool` — **TODO(me)**: lazy, `min_size=0`, never at import time
- [ ] `connect` — **TODO(me)**: context manager, dict rows, wraps only transient errors
- [ ] `wake` — **TODO(me)**: uses `with_retry`, returns the elapsed seconds
- [ ] `query` — **TODO(me)**: **read-only by name and in fact**, one statement only
- [ ] `execute` — **TODO(me)**: returns the affected row count
- [ ] `query_frame` — **TODO(me)**
- [ ] `apply_migrations` — **TODO(me)**: one transaction, records applied files, all-or-nothing

## Tests that must be able to fail

- [ ] `test_foreign_key_rejects_an_orphan` — green
- [ ] **Removed `PRAGMA foreign_keys = ON`, watched it pass for the wrong reason, restored it** ← do not skip
- [ ] `test_check_constraint_rejects_a_blank_title` / `..._impossible_year` — green
- [ ] `test_composite_key_rejects_a_duplicate_link` — green
- [ ] `test_cascade_removes_the_links_but_set_null_keeps_the_paper` — green
- [ ] **Swapped `SET NULL` and `CASCADE`, watched it go red, fixed it** ← do not skip
- [ ] `test_schema_file_is_idempotent` — green
- [ ] `test_every_foreign_key_states_its_delete_behaviour` — green
- [ ] `test_query_refuses_to_write` — four green cases
- [ ] `test_query_refuses_multiple_statements` — green
- [ ] `test_query_allows_a_cte` — green
- [ ] **Wrote the guard as "must start with SELECT", watched the CTE test go red, fixed it** ← do not skip
- [ ] `test_no_module_level_connection` — green
- [ ] `test_no_fstring_sql_in_src` — green
- [ ] Live: `test_wake_returns_quickly_enough` — green
- [ ] Live: `test_migrations_are_idempotent` — green (second run applies nothing)
- [ ] Live: `test_round_trip_through_postgres` — green
- [ ] The live tests are **skipped** without `SETU_LIVE=1`

## Budget

- [ ] LLM calls today: **0**
- [ ] Pool holds **zero** connections when idle

## Understanding check — answer out loud

- [ ] Why does a many-to-many relationship need a third table?
- [ ] Give a concrete cost of breaking 3NF
- [ ] Why does every foreign key need an explicit `ON DELETE`?
- [ ] Why `NOT NULL` alongside `UNIQUE`?
- [ ] What do the two nested `with` blocks each guarantee?
- [ ] Which errors do you retry, which do you let through, and why?
- [ ] What breaks when a colleague adds a column to a `SELECT` you unpack positionally?
- [ ] Why can most of today's schema tests run with no database at all?

## Commit

- [ ] `./m check && ./m done 42` succeeded
