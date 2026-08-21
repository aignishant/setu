# Day 43 — CHECKLIST

**IDs covered:** DB-03 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-43/lab/select.py
uv run python -m pytest tests/test_db.py -v
SETU_LIVE=1 uv run python -m pytest tests/test_db.py -m live -v
```

Expected: the ten-part query report ending with a passing SQL-vs-pandas assertion, then all tests green.

## Setup

- [ ] `./m start 43` and `./m scaffold 43` run
- [ ] `sql/002_seed.sql` written with `ON CONFLICT ... DO NOTHING`
- [ ] Migrations applied; seed data present
- [ ] No new packages installed

## DB-03 — execution order

- [ ] **Redrew the eight-step diagram from memory**
- [ ] Can state the one-line rule about `WHERE` vs `HAVING`
- [ ] Ran `the_alias_error()` and saw the same alias fail in `HAVING` and work in `ORDER BY`
- [ ] Can explain both outcomes using the diagram, without notes

## Clauses

- [ ] Used projection, `DISTINCT`, `count(*)`
- [ ] Can say why `SELECT *` is wrong in application code
- [ ] Used `WHERE` with a parameter, `BETWEEN`, `LIKE` and `ILIKE`
- [ ] Know that `ILIKE` is Postgres-specific
- [ ] Used `GROUP BY` with `count`, `sum`, `avg`, `max`
- [ ] Hit the "must appear in GROUP BY" error at least once and understood why
- [ ] Used `NULLS LAST` and know Postgres's default on `DESC`
- [ ] Compared `count(*)` with `count(col)`; can say what the difference measures
- [ ] Used `ORDER BY` + `LIMIT` together, always
- [ ] Used `OFFSET` and can say why deep pagination is slow

## NULL

- [ ] Ran `null_is_not_a_value()`
- [ ] Confirmed `= NULL` returns **zero** rows
- [ ] Confirmed `<> 'v1'` **excludes** the NULL row
- [ ] Can explain three-valued logic in one sentence
- [ ] Used `coalesce` and connected it to Day 30's `fillna`

## The same question twice

- [ ] Ran `the_same_question_twice()`; the frame assertion passed
- [ ] Mapped each SQL clause to its pandas equivalent out loud
- [ ] Understand why Day 51's ADR depends on this being checked

## Build brief

- [ ] `table_summary` — **TODO(me)**: allowlisted identifiers + `sql.Identifier`, never f-strings
- [ ] `missing_counts` — **TODO(me)**: one query, from `information_schema`
- [ ] `top_n` — **TODO(me)**: mandatory `ORDER BY`, deterministic ties, bounded n
- [ ] `paginate` — **TODO(me)**: a generator, refuses unordered SQL
- [ ] Can explain why placeholders work for values but not identifiers

## Tests that must be able to fail

- [ ] `test_equals_null_matches_nothing` — green ← **today's real assessment**
- [ ] `test_not_equals_excludes_nulls` — green
- [ ] `test_count_star_versus_count_column` — green
- [ ] `test_where_and_having_answer_different_questions` — green
- [ ] `test_alias_is_invisible_to_having` — green
- [ ] `test_alias_is_visible_to_order_by` — green
- [ ] `test_table_summary_rejects_a_bad_identifier` — six green cases
- [ ] **Built the identifier with an f-string, watched the injection case go red, switched to `sql.Identifier`** ← do not skip
- [ ] `test_top_n_rejects_an_absurd_n` — green
- [ ] `test_paginate_refuses_an_unordered_query` — green
- [ ] `test_paginate_is_lazy` — green
- [ ] **Returned a list from `paginate`, watched it go red, made it a generator** ← do not skip
- [ ] `test_no_bare_limit_in_src` — green
- [ ] Live: `test_sql_and_pandas_agree` — green
- [ ] Live: `test_missing_counts_matches_a_manual_check` — green
- [ ] Live: `test_top_n_is_deterministic` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Recite the eight execution steps in order
- [ ] Why can `ORDER BY` see an alias when `HAVING` cannot?
- [ ] Why is `= NULL` always false, and what do you write instead?
- [ ] Why does `<> 'x'` drop your NULL rows?
- [ ] Why must every non-aggregated `SELECT` column appear in `GROUP BY`?
- [ ] What does `count(*) - count(col)` measure?
- [ ] Why is `LIMIT` without `ORDER BY` dangerous rather than merely untidy?
- [ ] Why can't you parameterise a table name, and what do you do instead?

## Commit

- [ ] `./m check && ./m done 43` succeeded
