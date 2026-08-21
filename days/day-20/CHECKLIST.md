# Day 20 — CHECKLIST

**IDs covered:** NP-01, NP-02 · **Principles served:** 1, 4, 7, 13

## Demo command

```bash
uv run python days/day-20/lab/arrays.py
uv run python -m pytest tests/test_arrays.py -v
```

Expected: the nine-part array report (including a measured speed ratio), then all tests green.

## Setup

- [ ] `./m start 20` and `./m scaffold 20` run
- [ ] `uv add "numpy==<your pin>"` — in `pyproject.toml` and `uv.lock`
- [ ] Version pinned from **your** Day-1 verify run; drift logged if any
- [ ] `np.__version__` confirmed to start with `2.`
- [ ] `hasattr(np, "float_")` confirmed **False**
- [ ] Files created: `days/day-20/lab/arrays.py`, `src/setu/arrays.py`, `tests/test_arrays.py`

## NP-01 — anatomy

- [ ] Read `shape`, `ndim`, `size`, `dtype`, `itemsize`, `nbytes`, `.T`
- [ ] Know why a 1-D shape is `(3,)` and not `(3)`
- [ ] Ran `memory_and_speed()` and recorded the ratio on **your** machine: ______×
- [ ] Saw a float in an int list promote the whole array
- [ ] Saw a **string** in a numeric list turn everything into strings
- [ ] Saw `int8` overflow **wrap** with no exception
- [ ] Used `np.errstate` as a context manager
- [ ] Compared `float32` and `float64` precision

## The NumPy 2.x hazard

- [ ] Ran `dead_names()` and saw all seven print `False`
- [ ] Can name the live replacement for `np.NaN`, `np.in1d` and `np.float_`
- [ ] Read the official migration guide linked in §9

## NP-02 — creation

- [ ] Used `np.array` vs `np.asarray` and know which copies
- [ ] Know that `np.array(x, copy=False)` now **raises** in 2.x
- [ ] Used `arange`, `linspace`, `logspace`
- [ ] Know `linspace` **includes** the endpoint while `arange` does not
- [ ] Know why float steps in `arange` are a trap
- [ ] Used `zeros`, `ones`, `full`, `eye`, `zeros_like`
- [ ] Know why `np.empty` must be fully overwritten before reading
- [ ] Used `np.random.default_rng(seed=...)` and confirmed reproducibility
- [ ] Can explain why `np.random.seed()` is discouraged
- [ ] Saw one NaN poison `.sum()`, and used `np.nansum` instead
- [ ] Confirmed `np.nan == np.nan` is `False`

## Build brief

- [ ] `as_float_array` — **TODO(me)**: `asarray`, 1-D only, rejects `inf`, allows `nan` and empty
- [ ] `describe` — **TODO(me)**: nan-aware, `ddof=1`, degenerate case returns `nan`
- [ ] `make_rng` — **TODO(me)**: the single source of randomness
- [ ] `memory_report` — **TODO(me)**: elements, bytes, MiB
- [ ] Can explain why `inf` is rejected but `nan` is not

## Tests that must be able to fail

- [ ] `test_numpy_is_version_2` — green
- [ ] `test_removed_aliases_are_really_gone` — seven green cases
- [ ] `test_as_float_array_does_not_copy_a_correct_array` — green
- [ ] **Used `np.array` instead of `np.asarray`, watched it go red, fixed it** ← do not skip
- [ ] `test_as_float_array_converts_a_list` — green
- [ ] `test_as_float_array_rejects_2d` — green
- [ ] `test_as_float_array_rejects_infinity_but_allows_nan` — green
- [ ] `test_as_float_array_allows_empty` — green
- [ ] `test_describe_ignores_missing_values` — green
- [ ] `test_describe_uses_the_sample_standard_deviation` — green ← **today's sharpest test**
- [ ] **Changed to `ddof=0`, saw it report 2.0 instead of 2.138, reverted** ← do not skip
- [ ] `test_describe_all_missing_does_not_raise` — green
- [ ] `test_rng_is_reproducible` / `test_rng_default_seed_is_stable` / `test_different_seeds_differ` — green
- [ ] `test_memory_report_matches_reality` — green
- [ ] `test_no_legacy_random_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Structurally, what is the difference between a list of floats and a float array?
- [ ] Name the three things that structural difference buys, and the one thing it costs
- [ ] What happens when an `int8` exceeds 127, and why is that dangerous?
- [ ] Why prefer `linspace` over `arange` for floats?
- [ ] Why is `np.nan == np.nan` false, and what do you use instead?
- [ ] Why is `np.random.seed()` a reproducibility hazard rather than a convenience?
- [ ] What is `ddof`, and why did this project pick 1?

## Commit

- [ ] `./m check && ./m done 20` succeeded
