# Day 54 — CHECKLIST

**IDs covered:** APP-04 · **Principles served:** 1, 7, 12

## Demo command

```bash
uv run streamlit run days/day-54/lab/state.py
uv run python -m pytest tests/test_app.py -v
```

Expected: a seven-section page with a working counter and a draft→review→approve flow, then all app
tests green.

## Setup

- [ ] `./m start 54` and `./m scaffold 54` run
- [ ] `days/day-54/lab/state.py` created
- [ ] No new packages installed

## APP-04 — session state

- [ ] Fixed Day 52's counter; clicked it past 5
- [ ] Can explain in one sentence why the fixed version works
- [ ] Dumped `st.session_state` and found **widget keys you never assigned**
- [ ] Can say what `key=` does to a widget's value

## The ordering trap

- [ ] Ran §3 and saw the "before" line show the **previous** rerun's value
- [ ] Can explain why, in terms of source order rather than a bug
- [ ] Used `on_click=` and confirmed the value was already current
- [ ] Can say exactly when a callback runs relative to the rerun

## Widget keys

- [ ] Assigned to a widget's key programmatically and used `st.rerun()`
- [ ] Know that assigning to a key **and** passing `value=` raises

## The multi-step flow

- [ ] Built compose → review → approve/edit/reject
- [ ] Used `st.rerun()` after **every** stage change
- [ ] Confirmed reject publishes nothing and edit keeps the draft
- [ ] Can name the two later days this is the same shape as
- [ ] Can say what is different about those days (durability, not shape)

## What it is not

- [ ] Opened a second tab and confirmed independent state
- [ ] Can state all four "is not" points from §6

## Build brief

- [ ] `next_stage` — **TODO(me)**: pure, rejects illegal transitions, lists the legal ones
- [ ] `apply_action` — **TODO(me)**: pure, returns a new dict, publishes only via approve
- [ ] `state_summary` — **TODO(me)**
- [ ] `session_keys_to_clear` — **TODO(me)**: never returns a live widget key, deterministic
- [ ] `render_flow` — **TODO(me)**: thin, wired to `apply_action`, reruns after transitions
- [ ] Can explain why the state machine is split into two functions

## Tests that must be able to fail

- [ ] `test_the_happy_path` — green
- [ ] `test_reject_publishes_nothing` — green
- [ ] `test_edit_keeps_the_draft` — green
- [ ] `test_nothing_publishes_without_approve` — green ← **today's real assessment**
- [ ] **Made `reject` append before clearing, watched it go red, fixed it** ← do not skip
- [ ] `test_apply_action_does_not_mutate_its_input` — green
- [ ] `test_published_list_is_not_aliased` — green
- [ ] **Returned the same list object, watched it go red, copied it** ← do not skip
- [ ] `test_propose_requires_a_draft` — green
- [ ] `test_cannot_approve_from_compose` — green, legal actions listed in the message
- [ ] `test_every_legal_transition` — five green cases
- [ ] `test_unknown_stage_raises` / `test_unknown_action_raises` — green
- [ ] `test_every_stage_is_reachable` — green
- [ ] `test_every_stage_can_be_left` — green
- [ ] **Added a stage with no outgoing transitions, watched it go red, removed it** ← do not skip
- [ ] `test_state_summary_mentions_the_counts` — green
- [ ] `test_reset_never_clears_a_live_widget_key` — green
- [ ] `test_reset_is_deterministic` — green
- [ ] `test_flow_functions_are_pure` — green
- [ ] `test_renderer_reruns_after_every_stage_change` — green
- [ ] `test_no_secrets_in_session_state` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does `st.session_state` survive a rerun when a local variable does not?
- [ ] Why does reading a key above the code that sets it give a stale value?
- [ ] When exactly does an `on_click` callback run?
- [ ] What happens if you forget `st.rerun()` after a stage change?
- [ ] Why must a reset not clear a live widget's key?
- [ ] Give all four things `session_state` is not
- [ ] Why is per-session storage the wrong thing for a cache?
- [ ] How is the draft→review→approve flow related to Day 199 and Day 232?

## Commit

- [ ] `./m check && ./m done 54` succeeded
