# Day 48 — CHECKLIST

**IDs covered:** DB-08 · **Principles served:** 1, 5, 7, 9

## Demo command

```bash
uv run python days/day-48/lab/documents.py
uv run python -m pytest tests/test_mongo.py -q
SETU_LIVE=1 uv run python -m pytest tests/test_mongo.py -v
```

Expected: the seven-part document walkthrough ending with the when-to-use-which lists, then all
mongo tests green.

## Setup

- [ ] `./m start 48` and `./m scaffold 48` run
- [ ] `uv add "pymongo==<your pin>"` — exact-pinned, drift logged
- [ ] `MONGODB_URI` present in `.env` from Day 3
- [ ] Files created: `days/day-48/lab/documents.py`, `src/setu/mongo.py`, `tests/test_mongo.py`

## DB-08 — documents

- [ ] Connected and pinged; recorded the latency: ______ ms
- [ ] Know that a `ServerSelectionTimeoutError` is almost always the **IP access list**
- [ ] Set `serverSelectionTimeoutMS` explicitly; know what the default is
- [ ] Ran `lazy_creation()` and saw the **first write** create the collection
- [ ] Can say why lazy creation makes a typo'd name dangerous
- [ ] Inspected an `ObjectId` and its `generation_time`
- [ ] Can explain why sorting by `_id` is roughly chronological
- [ ] Supplied your own `_id`; can say why the natural key is the right choice
- [ ] Stored and read back a document with nested objects and arrays of objects
- [ ] Can say what that document would cost in Postgres

## The cost of no schema

- [ ] Ran `the_cost_of_no_schema()` and **read the output carefully**
- [ ] Confirmed all three bad documents were accepted without complaint
- [ ] Confirmed the typo'd document is invisible to a query on `year`
- [ ] Confirmed `"2019"` does not match `2019`
- [ ] Ran the `$type` aggregation and saw what was actually stored
- [ ] Can state where the schema went, in one sentence

## BSON

- [ ] Ran `bson_is_not_json()`
- [ ] Can name three types BSON preserves that JSON cannot
- [ ] Know that `json.dumps` fails on `ObjectId` and `datetime`
- [ ] Know which later day depends on converting at the boundary

## The decision

- [ ] Read both `when_to_use_which()` lists **out loud**
- [ ] Can state Setu's split and the reason it is by **shape**, not preference
- [ ] Named which Setu collections go where

## Build brief

- [ ] `client` — **TODO(me)**: context manager, timeouts, `MongoUnavailable` chained
- [ ] `collection` — **TODO(me)**: allowlisted, lists what is allowed on failure
- [ ] `insert_document` — **TODO(me)**: **refuses a plain dict**, validates, names duplicate `_id`
- [ ] `find_documents` — **TODO(me)**: mandatory bounded limit, JSON-safe output
- [ ] `healthcheck` — **TODO(me)**: never raises, same shape as `db.healthcheck`
- [ ] Can defend refusing a dict rather than accepting one for convenience

## Tests that must be able to fail

- [ ] `test_mongo_unavailable_is_transient` — green
- [ ] `test_collection_allowlist_rejects_a_typo` — green
- [ ] `test_missing_uri_raises_config_error` — green
- [ ] `test_client_converts_a_timeout_to_mongo_unavailable` — green, with `__cause__` chained
- [ ] **Dropped the `from exc`, watched the cause assertion go red, restored it** ← do not skip
- [ ] `test_find_rejects_an_unbounded_limit` — four green cases
- [ ] `test_insert_refuses_a_plain_dict` — green ← **today's real assessment**
- [ ] **Made `insert_document` accept a dict, watched it go red, reverted** ← do not skip
- [ ] `test_healthcheck_never_raises` — green
- [ ] `test_healthcheck_matches_the_postgres_contract` — green ← a cross-module contract
- [ ] `test_no_raw_mongo_client_in_src` — green
- [ ] **live** `test_ping_and_latency` — green
- [ ] **live** `test_insert_and_find_round_trip` — green, datetime returned as a string
- [ ] **live** `test_results_are_json_serialisable` — green
- [ ] **live** `test_duplicate_id_is_rejected_with_a_useful_message` — green
- [ ] Every live test cleaned up in `finally`; collection left empty

## Budget

- [ ] LLM calls today: **0**
- [ ] Atlas round trips: ~40
- [ ] Confirmed no test documents remain

## Understanding check — answer out loud

- [ ] Map the five SQL terms to their MongoDB equivalents
- [ ] What does "schema-on-read" mean, and where did the schema go?
- [ ] Describe the three documents from `the_cost_of_no_schema` and what each broke
- [ ] Why does a typo'd collection name not raise?
- [ ] Why set `_id` to the natural key?
- [ ] Name three BSON types JSON cannot represent, and one consequence of each
- [ ] Give Setu's Postgres-vs-Mongo split and justify it by shape
- [ ] If you find yourself reaching for `$lookup`, what does that suggest?

## Commit

- [ ] `./m check && ./m done 48` succeeded
