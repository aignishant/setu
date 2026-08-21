# Day 47 — CHECKLIST

**IDs covered:** DB-07 · **Principles served:** 1, 7, 11

## Demo command

```bash
uv run python days/day-47/lab/injection.py
uv run python -m pytest tests/test_db.py -q
SETU_LIVE=1 uv run python -m pytest tests/test_db.py -v
```

Expected: the injection walkthrough ending with a measured plan-caching ratio, then all db tests green.

## Setup

- [ ] `./m start 47` and `./m scaffold 47` run
- [ ] `days/day-47/lab/injection.py` created
- [ ] Confirmed the demo uses **SQLite only** — it never touches your Supabase project
- [ ] No new packages installed

## DB-07 — the demo

- [ ] Ran `the_ordinary_case()` first and confirmed the interpolated query **works**
- [ ] Can say why that is exactly what makes the bug survive code review
- [ ] Ran `the_attack()`; **read the printed query** and identified the injected syntax
- [ ] Ran `the_destructive_one()` and confirmed the table count went to zero
- [ ] Understood that this needed `executescript`, and that `OR '1'='1'` does **not**
- [ ] Ran `parameters_are_not_escaping()` with all three inputs including `O'Brien`
- [ ] Can state why parameterisation is a **different mechanism** from escaping
- [ ] Compared `?` and `:name`; know why named placeholders are preferred
- [ ] Saw `SELECT * FROM ?` raise, and can explain the grammar reason
- [ ] Ran `plan_caching()`; recorded the ratio: ______×

## SQLAlchemy Core

- [ ] Built a `Table` with `Column` objects
- [ ] Used `engine.begin()` for a write; know what `engine.connect()` would have done
- [ ] Printed a compiled `select()` and confirmed the value is a **bind parameter**
- [ ] Built a dynamic filter by chaining `.where()`
- [ ] Confirmed `papers.c['nope']` raises immediately
- [ ] Read the three reasons this project uses Core and not the ORM, **out loud**

## Build brief

- [ ] `quote_identifier` — **TODO(me)**: allowlist first, quote second, rejects embedded quotes
- [ ] `assert_parameterised` — **TODO(me)**: narrow rule, no false positives on `IS NULL` / `LIMIT`
- [ ] `build_select` — **TODO(me)**: returns `(sql, params)`, values never in the SQL
- [ ] `insert_many` — **TODO(me)**: key check, bulk insert, empty list is a no-op
- [ ] Can explain why `build_select` returns SQL instead of executing it

## Tests that must be able to fail

- [ ] `test_quote_identifier_allows_known_tables` — green
- [ ] `test_quote_identifier_rejects_unknown` — green (message lists what is allowed)
- [ ] `test_quote_identifier_rejects_an_embedded_quote` — green ← proves the **second** check fires
- [ ] `test_build_select_never_puts_a_value_in_the_sql` — four green cases ← **today's real assessment**
- [ ] **Interpolated one filter value into the SQL, watched all four go red, fixed it** ← do not skip
- [ ] `test_build_select_binds_every_filter` — green
- [ ] `test_build_select_quotes_the_table` — green
- [ ] `test_build_select_rejects_an_unknown_table` / `..._order_column` — green
- [ ] `test_build_select_rejects_a_bad_limit` / `..._empty_columns` — green
- [ ] `test_assert_parameterised_flags_an_embedded_literal` — green
- [ ] `test_assert_parameterised_flags_a_numeric_literal` — green
- [ ] `test_assert_parameterised_allows_a_parameterised_query` — green
- [ ] `test_assert_parameterised_allows_is_null` — green
- [ ] `test_assert_parameterised_allows_limit` — green
- [ ] `test_assert_parameterised_allows_a_mixed_query` — green
- [ ] **Broadened the rule to flag any literal, watched the three false-positive tests go red, narrowed it** ← do not skip
- [ ] `test_insert_many_rejects_mismatched_keys` — green
- [ ] `test_insert_many_on_empty_does_nothing` — green
- [ ] `test_insert_many_rejects_an_unknown_table` — green
- [ ] **live** `test_hostile_input_matches_nothing_and_harms_nothing` — green, table intact
- [ ] **live** `test_insert_many_round_trips` — green, and cleans up in `finally`

## Budget

- [ ] LLM calls today: **0**
- [ ] Postgres round trips: ~10 (live tests only)

## Understanding check — answer out loud

- [ ] What exactly does the database do differently with a parameter versus an interpolated value?
- [ ] Why is "I escape my inputs" a weaker answer than "I parameterise"?
- [ ] Why does the one-statement rule not make interpolation safe?
- [ ] Why can a table name never be a placeholder?
- [ ] Why is quoting alone insufficient for an identifier?
- [ ] What is the difference between `engine.begin()` and `engine.connect()`?
- [ ] Why does this project use SQLAlchemy Core rather than the ORM? Give all three reasons
- [ ] Why do the false-positive tests for `assert_parameterised` matter as much as the true positives?

## Commit

- [ ] `./m check && ./m done 47` succeeded
