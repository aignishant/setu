# Day 24 — CHECKLIST

**IDs covered:** NP-08, NP-09 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-24/lab/linalg.py
uv run python -m pytest tests/test_arrays.py -v
```

Expected: the nine-part report ending with recovered regression coefficients, then all tests green.

## Setup

- [ ] `./m start 24` and `./m scaffold 24` run
- [ ] `days/day-24/lab/linalg.py` created
- [ ] No new packages installed

## NP-08 — bits and strings

- [ ] Used `&`, `|`, `^`, `~` on boolean arrays
- [ ] Ran `packing_saves_memory()` and confirmed the 8× reduction
- [ ] Round-tripped a mask and **noticed the required trim** after `unpackbits`
- [ ] Used `np.binary_repr` and a shift
- [ ] Saw `<U3` truncate a long string **silently** — ran the line and looked at the output
- [ ] Used `np.strings` (not `np.char`, which is the 1.x name)
- [ ] Saw `dtype=object` avoid truncation but give up the performance
- [ ] Can state where text actually belongs in this project

## NP-09 — linear algebra

- [ ] Can state the shape rule `(n,k) @ (k,m) -> (n,m)` from memory
- [ ] Triggered a shape `ValueError` and read which dimension disagreed
- [ ] Compared `a * b` with `a @ b` and can say why confusing them is worse than an error
- [ ] Ran `a_dense_layer_by_hand()` and can point at the matmul, the broadcast bias, and the ReLU
- [ ] Know why ReLU uses `np.maximum` and not `np.max`
- [ ] Used `np.linalg.norm` with `axis` and `keepdims`
- [ ] Computed a cosine by hand, then via `normalised @ normalised.T`
- [ ] Used `np.linalg.solve` and can say why `inv()` is the wrong tool
- [ ] Saw a singular matrix fail `solve`, and connected it to Day 93's multicollinearity
- [ ] Recovered known regression coefficients with `lstsq`

## Build brief

- [ ] `l2_normalise` — **TODO(me)**: `keepdims`, zero rows → zeros not nan, returns new
- [ ] `cosine_similarity_matrix` — **TODO(me)**: one matmul, exact-1.0 diagonal, clipped to [-1, 1]
- [ ] `query_top_k` — **TODO(me)**: reuses Day 23's `top_k`, validates dimensions
- [ ] `pack_mask` / `unpack_mask` — **TODO(me)**, with the padding trimmed
- [ ] Noted that `query_top_k` **is** Day 155's vector search

## Tests that must be able to fail

- [ ] `test_l2_normalise_gives_unit_rows` — green
- [ ] `test_l2_normalise_handles_a_zero_row` — green
- [ ] **Removed the zero-norm guard, saw `nan`, restored it** ← do not skip
- [ ] `test_l2_normalise_does_not_modify_the_input` — green
- [ ] `test_cosine_diagonal_is_exactly_one` — green
- [ ] **Removed the `[-1, 1]` clip, saw `1.0000000000000002`, restored it** ← do not skip
- [ ] `test_cosine_is_bounded_and_symmetric` — green
- [ ] `test_cosine_matches_the_hand_computation` — green
- [ ] `test_cosine_zero_row_is_zero_everywhere` — green
- [ ] `test_query_top_k_finds_the_nearest_rows` — green
- [ ] `test_query_top_k_rejects_a_dimension_mismatch` — green
- [ ] `test_query_top_k_uses_no_python_loop_over_rows` — green ← **today's real assessment**
- [ ] **Wrote it as a loop over rows, watched the timing test go red, switched to a matvec** ← do not skip
- [ ] `test_mask_packing_round_trips` — green
- [ ] `test_mask_packing_handles_non_multiples_of_eight` — seven green cases
- [ ] **Removed the trim from `unpack_mask`, watched sizes 1/7/9/13/65 fail while 8 and 64 passed, fixed it** ← do not skip
- [ ] `test_packing_actually_saves_memory` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the matmul shape rule, and what the inner dimension does
- [ ] What is the difference between `a * b` and `a @ b`, and why is confusing them dangerous?
- [ ] Write a dense layer in one line and name each of its three parts
- [ ] Why `np.maximum` and not `np.max` for ReLU?
- [ ] How does one matmul give every pairwise cosine, and why does that matter for a vector database?
- [ ] Why never `inv()` to solve a system?
- [ ] What breaks if a cosine comes back as `1.0000000000000002`?
- [ ] Why must you trim after `unpackbits`, and which sizes expose the bug?

## Commit

- [ ] `./m check && ./m done 24` succeeded
