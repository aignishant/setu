# Day 8 — CHECKLIST

**IDs covered:** PY-07, PY-08 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-08/lab/containers.py
uv run python -m pytest tests/test_collections.py -v
```

Expected: the container report ending with a measured speed ratio, then all tests green.

## Setup

- [ ] `./m start 8` and `./m scaffold 8` run
- [ ] Files created: `days/day-08/lab/containers.py`, `src/setu/collections.py`, `tests/test_collections.py`
- [ ] No new packages installed

## PY-07 — lists and tuples

- [ ] Used `append`, `extend`, `insert`, `pop`, `remove` and can say how each differs
- [ ] Know what `papers.append(["a","b"])` does versus `extend`
- [ ] Used `[::-1]` and `[::2]` slices
- [ ] Confirmed `sorted()` returns new while `.sort()` returns `None`
- [ ] Saw `TypeError` when assigning into a tuple
- [ ] Confirmed `(1,)` is a tuple and `(1)` is an int
- [ ] Can state the rule for choosing a tuple over a list

## PY-08 — sets and dicts

- [ ] Used `|`, `&`, `-`, `^` on sets and know which is which
- [ ] Noted that set operations are how precision and recall are computed on Day 169
- [ ] Confirmed sets do not preserve order
- [ ] Saw `TypeError: unhashable type` when putting a list in a set
- [ ] Used `.get()` with and without a default; know when `[]` is the right choice instead
- [ ] Used `setdefault` at least once
- [ ] Saw a `.keys()` **view** change length after adding a key
- [ ] Used `|` to merge dicts and confirmed the right-hand side wins

## The measurement

- [ ] Ran `measure()` and recorded the actual ratio on **your** machine: ______×
- [ ] Used `time.perf_counter()` and know why not `time.time()`

## Build brief

- [ ] `unique` — **TODO(me) implemented**, O(n), order-preserving, non-mutating
- [ ] `counts` — **TODO(me) implemented without importing `Counter`**
- [ ] `chunked` — **TODO(me) implemented**, raises `ValueError` on `size < 1`
- [ ] Noted that `chunked` is Day 164's document chunker minus the overlap

## Tests that must be able to fail

- [ ] All were red before you implemented the TODOs
- [ ] `test_unique_preserves_first_seen_order` — green
- [ ] `test_unique_does_not_mutate_input` — green
- [ ] `test_unique_is_not_quadratic` — green ← **today's real assessment**
- [ ] **Rewrote `unique` with `if x not in result` on a list, watched the timing test go red, fixed it** ← do not skip
- [ ] `test_counts` and `test_counts_of_empty_is_empty` — green
- [ ] `test_chunked` — four green cases including the empty list and the ragged final chunk
- [ ] `test_chunked_rejects_zero_size` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is list membership O(n) and set membership O(1)?
- [ ] What is the price you pay for O(1) membership, and which earlier day explains it?
- [ ] Why can a tuple be a dict key but a list cannot?
- [ ] When do you want `d[key]` to raise rather than `d.get(key)` to return `None`?
- [ ] What is a view object, and what happens if you mutate the dict while iterating one?
- [ ] Which side wins in `a | b` for dicts, and what pattern does that enable?
- [ ] Give the four-way rule: when do you reach for list / tuple / set / dict?

## Commit

- [ ] `./m check && ./m done 8` succeeded
