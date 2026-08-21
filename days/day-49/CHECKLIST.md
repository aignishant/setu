# Day 49 — CHECKLIST

**IDs covered:** DB-09 · **Principles served:** 1, 5, 7

## Demo command

```bash
uv run python days/day-49/lab/crud.py
uv run python -m pytest tests/test_mongo.py -q
SETU_LIVE=1 uv run python -m pytest tests/test_mongo.py -v
```

Expected: the nine-part CRUD walkthrough ending with `cleaned up.`, then all mongo tests green.

## Setup

- [ ] `./m start 49` and `./m scaffold 49` run
- [ ] `days/day-49/lab/crud.py` created
- [ ] No new packages installed

## DB-09 — the query is a dict

- [ ] Built a filter with `|` and in a loop
- [ ] Can state the composability win, and name the Day 47 section it parallels
- [ ] Can explain why this makes classic SQL injection structurally impossible
- [ ] Can explain the `{"$ne": null}` hole it introduces instead

## Insert

- [ ] Saw `DuplicateKeyError` on a repeated `_id`
- [ ] Can say why the natural key as `_id` makes duplicate ingestion impossible
- [ ] Ran `insert_many(ordered=True)` with a duplicate in the middle and saw later docs **not** inserted
- [ ] Ran it with `ordered=False` and saw it continue
- [ ] Know which you want for ingestion, and why

## Query operators

- [ ] Used a dotted path into a nested object
- [ ] Confirmed `{"cats": "a"}` means **contains**
- [ ] Confirmed `{"cats": ["a"]}` is an exact array match
- [ ] Used `$all`, positional `cats.0`, and `$size`
- [ ] Used `$gte`, `$lte`, `$ne`, `$in`, `$nin`, `$or`, `$and`
- [ ] Used `$exists` and `$type`; can say why these are schema-on-read audit tools
- [ ] Used `$regex`; know why an unanchored pattern cannot use an index

## null vs missing

- [ ] Ran `null_versus_missing()` and read both counts
- [ ] Confirmed `{"field": None}` matches **both** cases
- [ ] Can state why the distinction matters semantically, not just technically

## Projection, sort, cursors

- [ ] Ran `projection_saves_bytes()`; recorded the ratio: ______×
- [ ] Know that `_id` returns unless excluded, and that 1/0 cannot be mixed otherwise
- [ ] Sorted with a **second tiebreak key**; can name the three earlier days with the same rule
- [ ] Ran `skip(2).limit(2)` and can explain why `skip` scales badly
- [ ] Confirmed a cursor is lazy and consumed once (Day 11)

## Build brief

- [ ] `assert_safe_filter` — **TODO(me)**: rejects dict values unless `trusted=True`, explains the attack
- [ ] `find_page` — **TODO(me)**: keyset pagination, deterministic sort, projection, bounded limit
- [ ] `count` — **TODO(me)**: `count_documents`, never the estimate
- [ ] `field_report` — **TODO(me)**: `$type` aggregation, the collection twin of Day 34's `quality_report`
- [ ] Can defend the blunt "no dict values" rule over a cleverer one

## Tests that must be able to fail

- [ ] `test_safe_filter_allows_plain_values` — green
- [ ] `test_safe_filter_rejects_an_operator_value` — green ← **today's real assessment**
- [ ] **Removed the guard, confirmed `{"$ne": None}` would match everything, restored it** ← do not skip
- [ ] `test_safe_filter_rejects_a_nested_operator_value` — green (path reported)
- [ ] `test_safe_filter_allows_trusted_operators` — green
- [ ] `test_find_page_rejects_an_unsafe_filter` — green
- [ ] `test_find_page_enforces_limit_bounds` — three green cases
- [ ] `test_find_page_rejects_an_unknown_collection` — green
- [ ] `test_field_report_rejects_a_bad_sample` — green
- [ ] `test_no_skip_in_src` — green
- [ ] `test_no_estimated_document_count_in_src` — green
- [ ] **live** `test_count_respects_the_filter` — green
- [ ] **live** `test_find_page_paginates_without_skip` — green, pages disjoint
- [ ] **live** `test_find_page_signals_the_last_page` — green
- [ ] **live** `test_find_page_projection_reduces_the_payload` — green
- [ ] **live** `test_find_page_is_deterministic_with_ties` — green
- [ ] **Removed the `_id` tiebreak, ran it several times, saw the order vary, restored it** ← do not skip
- [ ] **live** `test_array_equality_means_contains` — green
- [ ] **live** `test_null_and_missing_are_distinguishable` — green
- [ ] **live** `test_field_report_finds_a_type_inconsistency` — green

## Budget

- [ ] LLM calls today: **0**
- [ ] Atlas round trips: ~60
- [ ] Confirmed **zero** documents left behind

## Understanding check — answer out loud

- [ ] Why does a query being a dict rather than a string change how you build it?
- [ ] Describe the `{"$ne": null}` attack and the fix
- [ ] What does `ordered=True` do on a failure, and when do you want `ordered=False`?
- [ ] Give the four different array queries and what each asks
- [ ] Why does `{"field": None}` not mean "field is missing"?
- [ ] What comes back in a projection unless you say otherwise?
- [ ] Why does every sort need a tiebreak — and which three earlier days said the same?
- [ ] Why is `skip()` the wrong pagination, and what replaces it?

## Commit

- [ ] `./m check && ./m done 49` succeeded
