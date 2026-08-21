# Day 56 — CHECKLIST

**IDs covered:** APP-07 · **Principles served:** 1, 5, 7

## Demo command

```bash
uv run streamlit run days/day-56/lab/streaming.py
uv run python -m pytest tests/test_app.py -v
```

Expected: a seven-section page with a working chat box, then all app tests green.

## Setup

- [ ] `./m start 56` and `./m scaffold 56` run
- [ ] `days/day-56/lab/streaming.py` created
- [ ] No new packages installed

## APP-07 — blocking vs streaming

- [ ] Ran the blocking version and sat through the whole wait
- [ ] Ran the streaming version and compared how it **feels** at identical duration
- [ ] Confirmed `st.write_stream` also **returns** the joined text
- [ ] Streamed token by token
- [ ] Can say what changes on Day 197, and what does not

## Progress

- [ ] Used `st.status` with `state="complete"` and `state="error"`
- [ ] Ran the failing version several times and saw the error state
- [ ] Used `st.progress` and can say when each is appropriate
- [ ] Can say why faking a percentage is a small lie

## Abandonment

- [ ] Started a stream and clicked another widget mid-run
- [ ] Confirmed the `finally` counter still incremented
- [ ] Can explain what Streamlit does to a suspended generator
- [ ] Can name the earlier day that established this rule

## Async

- [ ] Ran the eight-wait comparison; recorded sequential ______ s vs gathered ______ s
- [ ] Can state why top-level `await` is impossible here
- [ ] Can state why `asyncio.run` still blocks the rerun
- [ ] Can say when async is worth it and when it is not
- [ ] Know why `asyncio.run` in a loop is wasteful

## Chat

- [ ] Built the chat loop with `st.chat_message` and `st.chat_input`
- [ ] Used the walrus operator on `st.chat_input`
- [ ] Confirmed history is **replayed** from `session_state` and only the new reply streams
- [ ] Can name the later day that builds on this shape

## Build brief

- [ ] `step_stream` — **TODO(me)**: lazy, `try/finally`, `on_error` modes, validates input
- [ ] `throttle` — **TODO(me)**: lazy, batches, always yields the remainder
- [ ] `collect_stream` — **TODO(me)**: time cap, partial result in the exception
- [ ] `chat_history_to_messages` — **TODO(me)**: validates roles, alternation, names the index
- [ ] `render_stream` — **TODO(me)**: thin, status states
- [ ] Can explain why the partial result belongs in the exception

## Tests that must be able to fail

- [ ] `test_step_stream_yields_one_line_per_step` — green
- [ ] `test_step_stream_is_lazy` — green
- [ ] `test_step_stream_cleans_up_when_abandoned` — green ← **today's real assessment**
- [ ] **Removed the `try/finally`, watched the cleanup test go red, restored it** ← do not skip
- [ ] `test_step_stream_source_has_a_finally` — green
- [ ] `test_step_stream_raises_by_default` — green
- [ ] `test_step_stream_can_continue_past_a_failure` — green
- [ ] `test_step_stream_rejects_a_bad_error_mode` / `..._empty_steps` — green
- [ ] `test_throttle_batches_small_chunks` — green, content unchanged
- [ ] `test_throttle_yields_the_remainder` — green
- [ ] **Dropped the short remainder, watched it go red, fixed it** ← do not skip
- [ ] `test_throttle_is_lazy_on_an_infinite_stream` — green (did **not** hang)
- [ ] `test_throttle_rejects_a_bad_size` — green
- [ ] `test_collect_stream_joins` — green
- [ ] `test_collect_stream_enforces_a_time_cap` — green
- [ ] `test_collect_stream_includes_the_partial_result` — green
- [ ] `test_history_requires_alternating_roles` — green
- [ ] `test_history_must_start_with_the_user` — green
- [ ] `test_history_accepts_a_valid_conversation` — green
- [ ] `test_history_names_the_bad_index` — green
- [ ] `test_history_does_not_mutate_the_input` — green
- [ ] `test_stream_functions_are_pure` — green
- [ ] `test_no_asyncio_run_in_a_loop` — green
- [ ] `test_no_top_level_await_in_the_app` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is a generator the right tool here rather than a thread?
- [ ] What does `st.write_stream` return, and what do you do with it?
- [ ] What happens to a suspended generator when Streamlit cancels a script?
- [ ] Why must a generator holding a connection use `try/finally`?
- [ ] Why can you not `await` at the top level of a Streamlit script?
- [ ] When does async pay for itself here, and when does it not?
- [ ] When do you use `st.status` rather than `st.progress`?
- [ ] Describe the replay-then-stream shape of a chat UI

## Commit

- [ ] `./m check && ./m done 56` succeeded
