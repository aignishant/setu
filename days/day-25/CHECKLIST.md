# Day 25 — CHECKLIST · **PHASE 3 GATE**

**IDs covered:** NP-10 · **Principles served:** 1, 7, 8, 10 · **Artifact:** ADR-001

## Demo command

```bash
uv run python days/day-25/lab/copies.py
uv run python -m pytest tests/test_stats.py -v
uv run python -m pytest -q
```

Expected: the six-part copy/view report with two measured ratios, then all stats tests green, then
the **whole** suite green.

## Setup

- [ ] `./m start 25` and `./m scaffold 25` run
- [ ] Files created: `days/day-25/lab/copies.py`, `src/setu/stats.py`, `tests/test_stats.py`, `docs/adr/ADR-001-copy-vs-view.md`
- [ ] No new packages installed

## NP-10 — the full picture

- [ ] Ran `the_full_table()` and **read every one of the fourteen rows**
- [ ] Was surprised by at least one; wrote down which: ______________________
- [ ] Confirmed `astype` copies even with an unchanged dtype
- [ ] Confirmed every arithmetic ufunc allocates a result
- [ ] Saw `reshape` return a view when contiguous and a **copy** after a transpose
- [ ] Compared `b += 100` with `b = b + 100` on a shared array
- [ ] Ran `the_deliberate_in_place_case()`; recorded the ratio: ______×
- [ ] Confirmed a chained view's `.base` points at the **intermediate**, not the original
- [ ] Ran `defensive_copy_costs()`; recorded the per-copy cost: ______ms
- [ ] Can state why `np.shares_memory` beats both `.base` and `OWNDATA`

## ADR-001 — the artifact (Principle 10)

- [ ] Written using `docs/adr/ADR-TEMPLATE.md`
- [ ] **Context** explains the view/copy split and the Day 21 leakage mechanism
- [ ] **At least three options** considered, each with an honest cost
- [ ] **Decision** stated in one sentence a reviewer could repeat back
- [ ] **Consequences** name what gets harder, not only what gets easier
- [ ] **Your measured numbers** from §3 are cited — defensive-copy cost and in-place speedup
- [ ] **What would make us change our minds** is specific and falsifiable
- [ ] Cold-read a day later with your reviewer hat on, and signed

## Build brief

- [ ] `summary` — **TODO(me)**: ten statistics, nan-aware, `ddof=1`, JSON-serialisable
- [ ] `zscores` — **TODO(me)**: NaN stays NaN, zero std gives zeros, does not modify input
- [ ] `iqr_outlier_mask` — **TODO(me)**: NaN is not an outlier, validates factor
- [ ] `correlation_matrix` — **TODO(me)**: standardise + one matmul, **not** `np.corrcoef`
- [ ] `bootstrap_mean_ci` — **TODO(me)**: fully vectorised, reproducible, validates input
- [ ] Can explain how the bootstrap index matrix removes the iteration loop

## Tests that must be able to fail

- [ ] `test_summary_against_hand_computed_values` — green (2.138, not 2.0)
- [ ] `test_summary_ignores_missing` / `test_summary_all_missing_is_nan_not_an_exception` — green
- [ ] `test_summary_is_json_serialisable` — green
- [ ] `test_zscores_are_standardised` — green
- [ ] `test_zscores_keep_nan_as_nan` — green
- [ ] **Made NaN become 0, watched it go red, fixed it** ← do not skip
- [ ] `test_zscores_constant_input_is_zeros_not_inf` — green
- [ ] `test_zscores_does_not_modify_the_input` — green
- [ ] `test_iqr_flags_the_obvious_outlier` — green
- [ ] `test_iqr_does_not_flag_nan` — green
- [ ] `test_iqr_rejects_a_bad_factor` — green
- [ ] `test_correlation_matches_numpy` — green ← **the Principle-2 payoff**
- [ ] `test_correlation_diagonal_is_exactly_one` — green
- [ ] `test_correlation_is_bounded` — green
- [ ] `test_correlation_constant_column_is_zero_not_nan` — green
- [ ] `test_bootstrap_ci_brackets_the_true_mean` — green
- [ ] `test_bootstrap_ci_is_reproducible` — green
- [ ] `test_bootstrap_ci_narrows_with_more_data` — green
- [ ] `test_bootstrap_is_vectorised` — green
- [ ] **Wrote the bootstrap as a Python loop, watched the timing test go red, vectorised it** ← do not skip
- [ ] `test_bootstrap_rejects_too_little_data` — green
- [ ] `test_no_in_place_writes_to_caller_arrays` — green ← **ADR-001, enforced**
- [ ] **Made one function use `-=` on its argument, watched it go red, fixed it** ← do not skip

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Which operations share memory, and which do not?
- [ ] Why is "reshape returns a view" a rule of thumb rather than a guarantee?
- [ ] Why is `.base` unreliable, and what do you use instead?
- [ ] State ADR-001's rule in one sentence
- [ ] Explain the leakage bug it prevents, in terms a non-programmer would follow
- [ ] What does ADR-001 cost, in your measured numbers, and what exception does it grant?
- [ ] Why is turning NaN into 0 during standardisation a silent bug?
- [ ] Why does `np.corrcoef` need `rowvar=False`?

## PHASE 3 GATE

- [ ] `ADR-001` written with real numbers and cold-read
- [ ] `src/setu/stats.py` complete; every function vectorised
- [ ] `correlation_matrix` proven equal to `np.corrcoef`
- [ ] `test_no_in_place_writes_to_caller_arrays` green
- [ ] Every Phase 3 lab runs in **seconds**
- [ ] Layering test still green (`stats` is layer 1, imports only `arrays` and `errors`)
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 25` succeeded and `./m status` shows Phases 0–3 complete
