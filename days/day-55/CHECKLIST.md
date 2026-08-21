# Day 55 — CHECKLIST

**IDs covered:** APP-05, APP-06 · **Principles served:** 1, 5, 7

## Demo command

```bash
uv run streamlit run days/day-55/lab/caching.py
uv run python -m pytest tests/test_app.py -v
```

Expected: a seven-section page with two diverging call counters, then all app tests green.

## Setup

- [ ] `./m start 55` and `./m scaffold 55` run
- [ ] `days/day-55/lab/caching.py` created
- [ ] No new packages installed

## APP-05 — the two caches

- [ ] Moved the slider repeatedly; recorded uncached ______ ms vs cached ______ ms
- [ ] Watched the uncached call counter climb every rerun
- [ ] Watched the cached counter climb **once per distinct argument** then stop
- [ ] Can state what the cache key is
- [ ] Know that a DataFrame argument is hashed **by contents**, and what to do instead
- [ ] Confirmed `cache_data` returns a **different object** each call
- [ ] Mutated your copy and confirmed the cached value was untouched
- [ ] Confirmed `cache_resource` returns the **same** object across reloads
- [ ] Can state which is right for a connection pool, and what goes wrong the other way round

## The bug caching introduces

- [ ] Ran §5 and compared the cached and uncached lists after adding a draft
- [ ] Can state what a cache actually promises
- [ ] Can give one case where staleness is fine and one where it is a correctness bug
- [ ] Used `fn.clear()` and know how it differs from `st.cache_data.clear()`

## What must not be cached

- [ ] Can name all four categories from §6
- [ ] Can explain why the per-user one is a **security** bug rather than a performance one

## APP-06 — rendering

- [ ] Used `st.dataframe` with `column_config` and `hide_index`
- [ ] Know why `st.dataframe` beats `st.table`
- [ ] Compared `st.line_chart` with a `setu.plots` chart via `st.pyplot`
- [ ] Can say when each is appropriate
- [ ] Used `st.metric` with a `delta`; know about `delta_color='inverse'`

## Build brief

- [ ] `CACHE_POLICY` declared, with `approval_queue: None`
- [ ] `cache_ttl` — **TODO(me)**: raises on an undeclared name
- [ ] `assert_cacheable` — **TODO(me)**: the message explains **why**
- [ ] `cache_key_parts` — **TODO(me)**: includes `user`, order-independent, rejects unhashables
- [ ] `format_table` — **TODO(me)**: truncates with a message, config from dtypes, does not mutate
- [ ] `render_dashboard` — **TODO(me)**: thin, uses `setu.plots`, ttls from `cache_ttl`
- [ ] Can explain why caches are declared in a table rather than by typing a decorator

## Tests that must be able to fail

- [ ] `test_declared_ttls_are_returned` — green
- [ ] `test_undeclared_cache_raises` — green
- [ ] `test_approval_queue_is_not_cacheable` — green ← **today's real assessment**
- [ ] **Made the message a bare refusal, watched it go red, added the reason** ← do not skip
- [ ] `test_cacheable_names_pass` — green
- [ ] `test_every_policy_entry_has_a_sane_ttl` — green
- [ ] `test_cache_key_is_order_independent` — green
- [ ] `test_cache_key_includes_the_name` — green
- [ ] `test_cache_key_separates_users` — green
- [ ] **Dropped `user` from the key, watched it go red, restored it** ← do not skip
- [ ] `test_cache_key_without_a_user_differs_from_one_with` — green
- [ ] `test_cache_key_is_hashable` — green
- [ ] `test_cache_key_rejects_an_unhashable_param` — green
- [ ] `test_format_table_truncates_and_says_so` — green
- [ ] `test_format_table_no_message_when_it_fits` — green
- [ ] `test_format_table_does_not_mutate` — green
- [ ] `test_format_table_configures_numeric_columns_by_dtype` — green
- [ ] **Configured columns by name-guessing, watched `title` get a numeric format, fixed it** ← do not skip
- [ ] `test_format_table_is_pure` — green
- [ ] `test_every_cached_function_declares_its_ttl` — green
- [ ] `test_cache_resource_is_only_used_for_connections` — green
- [ ] `test_no_builtin_charts_in_the_app` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the difference between `cache_data` and `cache_resource`, in one sentence?
- [ ] What goes wrong if you swap them?
- [ ] What is a cache actually promising you?
- [ ] Give one thing safe to cache and one where staleness is a correctness bug
- [ ] Why is a per-user cache without the user id a data leak?
- [ ] Why does passing a big DataFrame as a cached argument cost you?
- [ ] When do you use `fn.clear()` rather than clearing everything?
- [ ] Why does the app not use `st.line_chart`?

## Commit

- [ ] `./m check && ./m done 55` succeeded
