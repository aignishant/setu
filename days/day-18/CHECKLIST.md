# Day 18 — CHECKLIST

**IDs covered:** PY-22 · **Principles served:** 1, 7, 11

## Demo command

```bash
uv run python days/day-18/lab/errors.py
uv run python -m pytest tests/test_errors.py -v
uv run python -m pytest -q
```

Expected: the five-part error report, then all error tests green, then the **whole** suite green
after the rewiring.

## Setup

- [ ] `./m start 18` and `./m scaffold 18` run
- [ ] Files created: `days/day-18/lab/errors.py`, `src/setu/errors.py`, `tests/test_errors.py`
- [ ] No new packages installed

## PY-22 — mechanics

- [ ] Ran `the_four_blocks()`; can say when `else` runs and when `finally` runs
- [ ] Confirmed `finally` runs even when `except` returns
- [ ] Ran `narrow_beats_broad()` and saw the typo surface under a narrow handler and hide under a broad one
- [ ] Used `raise X(...) from exc` and read `__cause__`
- [ ] Saw `__cause__` be `None` without `from`, and know what `__context__` is
- [ ] Ordered `except` clauses subclass-first and know what reversing them does
- [ ] Wrote a custom exception carrying **structured data**, not just a message

## Build brief

- [ ] `src/setu/errors.py` created with `SetuError`, `ConfigError`, `DataError`, `TransientError`
- [ ] `MissingKey`, `InvalidPaper`, `UnsupportedFormat` placed under the right parents
- [ ] `RateLimited` — **TODO(me)**: `provider` + `retry_after`, validated, in the message
- [ ] `RetriesExhausted` — **TODO(me)**: `attempts` attribute, named in the message
- [ ] `errors.py` is layer 0 — it imports **nothing** from `setu`
- [ ] `config.py` re-exports `MissingKey` from `errors`
- [ ] `papers.py` re-exports `InvalidPaper` from `errors`
- [ ] `loaders.py` re-exports `UnsupportedFormat` from `errors`
- [ ] `retry.py` / `decorators.py` use `RetriesExhausted` from `errors`
- [ ] `retry`'s default `exceptions=` filter is now `(TransientError,)`
- [ ] Can defend the decision that `RetriesExhausted` is itself transient

## Tests that must be able to fail

- [ ] `test_hierarchy` — eight green cases
- [ ] `test_setu_error_is_not_too_broad` — green
- [ ] `test_catching_transient_covers_every_retryable_error` — green
- [ ] `test_rate_limited_carries_structured_data` — green
- [ ] `test_rate_limited_rejects_a_negative_delay` — green
- [ ] `test_retries_exhausted_names_the_attempt_count` — green
- [ ] `test_retry_chains_the_original_cause` — green
- [ ] **Removed `from exc` in the retry decorator, watched it go red, restored it** ← do not skip
- [ ] `test_config_still_exposes_missing_key` — green (Day 2's tests still pass)
- [ ] `test_papers_raises_the_shared_invalid_paper` — green, asserting the **parent** class
- [ ] `test_no_bare_excepts_in_src` — green
- [ ] **Added an `except Exception:` to a src module, watched it go red, removed it** ← do not skip
- [ ] Full suite green after all the rewiring

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the two rules from §1
- [ ] Give a concrete example of a broad `except` hiding your own bug
- [ ] When does `else` run, and why put code there instead of in the `try`?
- [ ] What does `from exc` set, and what do you lose without it?
- [ ] Why must `except` clauses be ordered subclass-first?
- [ ] Why does `RateLimited` carry `retry_after` as an attribute rather than only in the message?
- [ ] Why should a test assert `DataError` rather than `InvalidPaper`?
- [ ] Why is a bare `except:` worse than `except Exception:`?

## Commit

- [ ] `./m check && ./m done 18` succeeded
