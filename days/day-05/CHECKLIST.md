# Day 5 — CHECKLIST

**IDs covered:** PY-03, PY-04 · **Principles served:** 1, 7

## Demo command

```bash
uv run python days/day-05/lab/operators.py
uv run python -m pytest tests/test_textutils.py -q
```

Expected: the operator report, then all tests green (Day 4's plus today's).

## Setup

- [ ] `./m start 5` and `./m scaffold 5` run
- [ ] `days/day-05/lab/operators.py` created
- [ ] No new packages installed

## PY-03 — operators and precedence

- [ ] Ran `identity_vs_equality()` and saw `256 is 256` True but `257 is 257` False
- [ ] Can say **out loud** why that is an implementation detail, not a rule
- [ ] Saw `x == y` True with `x is y` False for two equal lists
- [ ] Confirmed `2 ** 3 ** 2 == 512` and `-2 ** 2 == -4`
- [ ] Confirmed `and` binds tighter than `or`
- [ ] Ran `short_circuit()` and saw that `B` and `D` never printed
- [ ] Can explain why `if user is not None and user.name:` is safe but the reverse order raises

## PY-04 — truthiness

- [ ] Ran `truthiness()`; all assertions passed
- [ ] Wrote the falsy set from memory, then checked it
- [ ] Understood why `"0"` and `"False"` are **truthy**
- [ ] Understood why `[0]` is truthy
- [ ] Read the pandas note and know the three correct alternatives to `if df:`
- [ ] Know why `assert` is not validation in shipped code (`python -O`)

## Build brief

- [ ] `is_blank` — **TODO(me) implemented**, using truthiness rather than `==` chains
- [ ] `first_non_blank` — **TODO(me) implemented**, and it does **not** naively use `or`
- [ ] Both have guard-first, work-last shape

## Tests that must be able to fail

- [ ] `test_is_blank_true` — four green parametrised cases
- [ ] `test_is_blank_false` — four green, including `"0"` and `"False"`
- [ ] `test_first_non_blank_skips_whitespace_only` — green
- [ ] **Rewrote `first_non_blank` as `a or b or c`, watched that test go red, fixed it** ← do not skip
- [ ] `test_first_non_blank_returns_none_when_all_blank` — green
- [ ] Changed `is_blank` to return `1` instead of `True`, watched `is True` catch it, reverted

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What question does `is` answer that `==` does not?
- [ ] What is the only correct use of `is`, and why is `== None` risky?
- [ ] Why is `-2 ** 2` equal to `-4`?
- [ ] What does short-circuiting buy you beyond speed?
- [ ] List the falsy values from memory
- [ ] Why does a DataFrame refuse to answer `if df:` instead of guessing?
- [ ] Why does `assert x is True` catch a bug that `assert x == True` misses?

## Commit

- [ ] `./m check && ./m done 5` succeeded
