# Day 11 — CHECKLIST · **PHASE 1 GATE**

**IDs covered:** PY-11, PY-12 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-11/lab/lazy.py
uv run python -m pytest -q
```

Expected: the laziness report, then the **whole suite** green — and finishing in seconds, not hanging.

## Setup

- [ ] `./m start 11` and `./m scaffold 11` run
- [ ] Files created: `days/day-11/lab/lazy.py`, `src/setu/streams.py`, `tests/test_streams.py`
- [ ] No new packages installed

## PY-11 — the protocol

- [ ] Called `iter()` and `next()` by hand and saw `StopIteration`
- [ ] Confirmed `iter(list) is not list` but `iter(iterator) is iterator`
- [ ] Can state the difference between **iterable** and **iterator** in one sentence
- [ ] Saw that calling a generator function runs **none** of its body
- [ ] Saw a generator pause at `yield` and resume with locals intact
- [ ] Confirmed a generator is consumed once
- [ ] Compared `sys.getsizeof` for a list vs a generator over 200 000 items
- [ ] Built an **infinite** generator and sliced it with `itertools.islice`
- [ ] Used `itertools.groupby` and know it only groups **consecutive** keys

## PY-12 — lambda and map

- [ ] Used `lambda` as a `sorted` key
- [ ] Used a **tuple key** with a negated field for mixed-direction sorting
- [ ] Compared `map(lambda ...)` with the equivalent comprehension
- [ ] Can say when `map` genuinely wins (an existing named function, no lambda)

## Build brief

- [ ] `read_lines` — **TODO(me)**: lazy, uses `with`, skips blanks and `#` comments
- [ ] `batched` — **TODO(me)**: lazy, no `len()` or slicing, raises on `size < 1`
- [ ] `take` — **TODO(me)**: never consumes more than `n`
- [ ] `sliding` — **TODO(me)**: overlapping windows, lazy
- [ ] Noted that `sliding` is Day 164's chunker with a different unit

## Tests that must be able to fail

- [ ] All ten were red before you implemented the TODOs
- [ ] `test_read_lines_skips_blanks_and_comments` — green
- [ ] `test_read_lines_is_lazy` — green
- [ ] `test_batched_is_lazy_on_infinite_input` — green
- [ ] **Made `batched` call `list(items)` first, watched the test HANG, fixed it** ← do not skip
- [ ] `test_batched_final_batch_is_ragged` — green
- [ ] `test_batched_on_empty_yields_nothing` — green
- [ ] `test_batched_rejects_zero_size` — green
- [ ] `test_take_does_not_over_consume` — green ← the sharpest test here
- [ ] **Made `take` read `n + 1` items, watched it go red, fixed it** ← do not skip
- [ ] `test_take_more_than_available` — green
- [ ] `test_sliding_windows_overlap` and `test_sliding_is_lazy` — green
- [ ] The whole file finishes in **seconds**, not hanging

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What two function calls does a `for` loop actually make?
- [ ] What is the difference between an iterable and an iterator?
- [ ] What exactly happens, step by step, when execution reaches `yield`?
- [ ] Why does calling a generator function run none of its body, and what does that delay?
- [ ] Why does `groupby` need sorted input?
- [ ] Why does testing against an infinite generator *hang* instead of failing, and why is that good?
- [ ] When is `lambda` the right tool, and when did you actually want `def`?

## PHASE 1 GATE

- [ ] `src/setu/` contains: `paths`, `versions`, `config`, `models`, `retry`, `textutils`, `collections`, `papers`, `streams`
- [ ] Every one has a matching test module
- [ ] **No module does any work at import time**
- [ ] Every function that mutates says so in its docstring; none both mutates and returns new
- [ ] `uv run python -m pytest -q` — whole suite green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 11` succeeded and `./m status` shows Phase 1 complete
