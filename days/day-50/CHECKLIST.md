# Day 50 — CHECKLIST

**IDs covered:** DB-10, DB-11 · **Principles served:** 1, 7, 11, 12

## Demo command

```bash
uv run python days/day-50/lab/writes.py
uv run python -m pytest tests/test_mongo.py -q
SETU_LIVE=1 uv run python -m pytest tests/test_mongo.py -v
```

Expected: the eleven-part walkthrough with two measured ratios, ending with the count-then-delete
cleanup, then all mongo tests green.

## Setup

- [ ] `./m start 50` and `./m scaffold 50` run
- [ ] `days/day-50/lab/writes.py` created
- [ ] No new packages installed

## DB-10 — updates

- [ ] Saw `matched_count` and `modified_count` differ on a repeated update
- [ ] Can say which one to check, and when
- [ ] Used `$set`, `$inc`, `$push`, `$addToSet`, `$unset`
- [ ] Confirmed `$addToSet` did **not** duplicate `"seen"`
- [ ] Ran `the_missing_dollar_set()` and saw `replace_one` destroy the other fields
- [ ] Used an upsert with `$setOnInsert`
- [ ] Confirmed `fetched_at` was **not** overwritten on the second upsert
- [ ] Can say why that makes Day 227's ingestion safely re-runnable

## Blast radius (Principles 11 & 12)

- [ ] Ran `delete_blast_radius()` and read all three counts
- [ ] Confirmed a typo'd **field** matches zero documents
- [ ] Can state which filter shape is actually dangerous, and why
- [ ] Can state the house rule from memory: count first, refuse `{}`, cap the damage

## Indexes

- [ ] Ran `indexes_are_not_subtle()`; recorded the ratio: ______×
- [ ] Found **COLLSCAN** in the plan before, and **IXSCAN** after
- [ ] Recorded the index size: ______ KiB
- [ ] Can name the two costs of an index
- [ ] Ran `compound_index_order_matters()` and confirmed only a **left prefix** is served
- [ ] Can say how to order compound index fields

## DB-11 — the aggregation pipeline

- [ ] Ran the five-stage pipeline
- [ ] Mapped every stage onto its SQL equivalent, including `$match`-after-`$group` = `HAVING`
- [ ] Connected it to Day 31's split–apply–combine
- [ ] Ran `match_first_is_not_optional()`; recorded both timings
- [ ] Can give **two** reasons `$match` goes first
- [ ] Used `$unwind`; can name the Day 32 pandas operation it is
- [ ] Know what `$lookup` is, and what reaching for it repeatedly suggests

## Build brief

- [ ] `update_documents` — **TODO(me)**: refuses `{}`, refuses non-operator updates, counts first, caps
- [ ] `delete_documents` — **TODO(me)**: `dry_run=True` **by default**, refuses `{}`, counts first
- [ ] `ensure_indexes` — **TODO(me)**: declared in `INDEXES`, idempotent, capped at 6
- [ ] `aggregate` — **TODO(me)**: `$match` first required, `$out`/`$merge` rejected, default limit, JSON-safe
- [ ] `explain` — **TODO(me)**: flattened to stage, index, docs examined
- [ ] Can defend `dry_run=True` as the default

## Tests that must be able to fail

- [ ] `test_update_refuses_an_empty_filter` — green
- [ ] `test_delete_refuses_an_empty_filter` — green
- [ ] `test_empty_filter_cannot_be_overridden` — green ← **today's real assessment**
- [ ] **Added an override for `{}` when `max_affected` is large, watched it go red, removed it** ← do not skip
- [ ] `test_update_rejects_a_replacement_document` — green
- [ ] `test_update_accepts_operator_documents` — green
- [ ] `test_aggregate_requires_match_first` — green
- [ ] `test_aggregate_rejects_writing_stages` — two green cases
- [ ] `test_aggregate_rejects_an_unknown_collection` — green
- [ ] `test_index_declaration_is_capped` — green
- [ ] `test_destructive_default_is_conservative` — green
- [ ] `test_delete_dry_run_is_the_default` — green ← an **API-shape** test
- [ ] **Changed the default to `False`, watched it go red, reverted** ← do not skip
- [ ] **live** `test_update_counts_before_it_writes` — green
- [ ] **live** `test_update_refuses_to_exceed_the_cap` — green, both numbers in the message
- [ ] **live** `test_update_wrote_nothing_when_it_refused` — green
- [ ] **Counted after writing instead of before, watched this one go red, fixed the order** ← do not skip
- [ ] **live** `test_delete_dry_run_destroys_nothing` — green
- [ ] **live** `test_delete_actually_deletes_when_asked` — green
- [ ] **live** `test_ensure_indexes_is_idempotent` — green
- [ ] **live** `test_an_index_turns_a_collscan_into_an_ixscan` — green
- [ ] **live** `test_aggregate_matches_a_hand_computed_answer` — green (100 and 100)
- [ ] **live** `test_aggregate_results_are_json_safe` — green
- [ ] **live** `test_aggregate_applies_a_default_limit` — green

## Budget

- [ ] LLM calls today: **0**
- [ ] Atlas round trips: ~300
- [ ] Confirmed the seeded documents and indexes are **gone**

## Understanding check — answer out loud

- [ ] What is the difference between `matched_count` and `modified_count`?
- [ ] What does `replace_one` do that `update_one` with `$set` does not?
- [ ] Why does `$setOnInsert` make a re-runnable ingestion correct?
- [ ] Which filter mistake is dangerous, and which is merely annoying?
- [ ] What do COLLSCAN and IXSCAN mean, and where do you look for them?
- [ ] What are the two costs of an index?
- [ ] State the left-prefix rule
- [ ] Give two reasons `$match` must come first
- [ ] Why should a destructive function default to a dry run?

## Commit

- [ ] `./m check && ./m done 50` succeeded
