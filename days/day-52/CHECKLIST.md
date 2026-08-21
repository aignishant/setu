# Day 52 — CHECKLIST

**IDs covered:** APP-01 · **Principles served:** 1, 6, 7

## Demo command

```bash
uv run streamlit run days/day-52/lab/rerun.py
uv run python -m pytest tests/test_app.py -v
```

Expected: a seven-section page you can click through, then all app tests green.

## Setup

- [ ] `./m start 52` and `./m scaffold 52` run
- [ ] `uv add "streamlit==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-52/lab/rerun.py`, `app/Home.py`, `src/setu/app.py`, `tests/test_app.py`
- [ ] Know how to start and stop the dev server

## APP-01 — the model

- [ ] Can state the one surprising idea in a single sentence
- [ ] Clicked the broken counter **repeatedly** and confirmed it never exceeds 1
- [ ] Can explain exactly why, in terms of which line re-executes
- [ ] Watched the module-scope timestamp change when you moved the slider
- [ ] Confirmed module-level code is **not** run-once
- [ ] Confirmed `st.button` is `True` only on its own rerun
- [ ] Can say why a button is not usable as a mode flag
- [ ] Confirmed a widget **returns a value** rather than firing a handler
- [ ] Sat through the slow computation on several clicks and felt the cost
- [ ] Used `st.empty()` to render out of source order
- [ ] Used `st.stop()` and confirmed nothing below rendered
- [ ] Opened a second tab and confirmed its run counter started at 1

## The three consequences

- [ ] Can name what makes an app slow, and which day fixes it
- [ ] Can name why a variable resets, and which day fixes it
- [ ] Can explain why there is no onChange callback

## The app skeleton

- [ ] `app/Home.py` created and **thin** — wiring only
- [ ] `apply_house_style()` called there and **nowhere else**
- [ ] Can say why calling it per-component would be wrong under the rerun model

## Build brief

- [ ] `summarise_health` — **TODO(me)**: pure, three statuses, never raises, encodes the ADR-004 asymmetry
- [ ] `format_latency` — **TODO(me)**
- [ ] `paginate` — **TODO(me)**: clamps a stale page rather than raising
- [ ] `render_intro` / `render_health` — **TODO(me)**: thin, `st.*` only, `st.stop()` when down
- [ ] Can explain the testable-seam rule in one sentence

## Tests that must be able to fail

- [ ] `test_both_up_is_ok` / `test_one_down_is_degraded` / `test_both_down_is_down` — green
- [ ] `test_postgres_down_is_described_as_worse_than_mongo_down` — green
- [ ] **Returned identical text for both single-failure cases, watched it go red, fixed it** ← do not skip
- [ ] `test_health_lines_include_latency` — green
- [ ] `test_summarise_health_never_raises_on_a_malformed_report` — green (four shapes)
- [ ] `test_summarise_health_is_pure` — green ← **today's real assessment**
- [ ] **Added an `st.error(...)` inside `summarise_health`, watched it go red, moved it to the renderer** ← do not skip
- [ ] `test_format_latency` — four green cases
- [ ] `test_format_latency_rejects_negative` — green
- [ ] `test_paginate_middle_page` / `..._first_and_last` / `..._partial_last_page` — green
- [ ] `test_paginate_clamps_a_stale_page` — green (pages 40, 0 and −5)
- [ ] `test_paginate_empty` — green
- [ ] `test_paginate_rejects_a_bad_page_size` — green
- [ ] `test_app_entry_point_is_thin` — green
- [ ] **Put a `for` loop in `Home.py`, watched it go red, moved it to `setu.app`** ← do not skip
- [ ] `test_style_is_applied_once_at_the_entry_point` — green
- [ ] `test_no_module_level_work_in_the_app_package` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What happens, precisely, when a user clicks a widget?
- [ ] Why does `count = 0; if st.button(): count += 1` never reach 2?
- [ ] When is `st.button` True, and when is it False?
- [ ] Why is there no onChange callback, and what do you get in exchange?
- [ ] What are the two costs of the rerun model, and which day fixes each?
- [ ] What does `st.empty()` buy you, given render order is source order?
- [ ] Do two browser tabs share state? What *is* shared?
- [ ] Why must every decision live outside the Streamlit file?

## Commit

- [ ] `./m check && ./m done 52` succeeded
