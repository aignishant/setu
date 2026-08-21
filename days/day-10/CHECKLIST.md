# Day 10 — CHECKLIST

**IDs covered:** PY-10 · **Principles served:** 1, 6, 7

## Demo command

```bash
uv run python days/day-10/lab/functions.py
uv run python -m pytest tests/test_papers.py -v
```

Expected: the parameter report, then **nine green tests**.

## Setup

- [ ] `./m start 10` and `./m scaffold 10` run
- [ ] Files created: `days/day-10/lab/functions.py`, `src/setu/papers.py`, `tests/test_papers.py`
- [ ] No new packages installed

## PY-10 — argument passing

- [ ] Ran `rebind_vs_mutate()` and saw rebinding invisible, mutation visible
- [ ] Redrew the §1 diagram from memory
- [ ] Can state the passing rule in one sentence without saying "by value" or "by reference"
- [ ] Used all six parameter kinds in one signature
- [ ] Saw the `TypeError` from calling a positional-only parameter by keyword
- [ ] Understand what `/` does and when you would want it

## Scope

- [ ] Confirmed reading an enclosing name needs no declaration
- [ ] Uncommented `total += 1` and saw `UnboundLocalError`, then fixed it with `nonlocal`
- [ ] Can explain why assignment makes a name local
- [ ] Know why this project never uses `global`

## Defaults

- [ ] Ran `default_evaluated_once()` and saw the frozen timestamp
- [ ] Can explain why this is the **same mechanism** as the mutable-default bug from Day 4

## Structure

- [ ] Compared `deep` and `flat`; can say why `flat` is the house style
- [ ] Every function you write today has guards first and work last
- [ ] No module in `src/setu/` does work at import time

## Build brief

- [ ] `make_paper` — **TODO(me) implemented** with positional-only id/title/year and keyword-only extras
- [ ] Title normalisation **reuses** `textutils`, not reimplemented
- [ ] Validation raises `InvalidPaper` for blank id, blank title, and out-of-range year
- [ ] `authors` defaults to a **new** list each call
- [ ] `authors` from the caller is **copied**, not aliased
- [ ] `summarise` — **TODO(me) implemented**, reuses `textutils.truncate`, handles no authors
- [ ] `newest` — **TODO(me) implemented**, ties broken A–Z, does not mutate the input

## Tests that must be able to fail

- [ ] All nine were red before you implemented the TODOs
- [ ] `test_make_paper_normalises_the_title` — green
- [ ] `test_make_paper_rejects_bad_input` — four green parametrised cases
- [ ] `test_authors_default_is_not_shared_between_calls` — green
- [ ] **Changed the signature to `authors: list[str] = []`, watched it go red, reverted** ← do not skip
- [ ] `test_authors_are_copied_from_the_caller` — green
- [ ] **Stored the caller's list directly, watched it go red, reverted** ← do not skip
- [ ] `test_extra_positional_args_are_rejected` — green (delete the `*` and confirm it goes red)
- [ ] `test_summarise_does_not_modify_the_paper` — green
- [ ] `test_summarise_respects_width` — green
- [ ] `test_newest_breaks_ties_alphabetically` — green
- [ ] `test_newest_does_not_mutate_the_input` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State Python's argument-passing rule without using "by value" or "by reference"
- [ ] Why does rebinding a parameter not affect the caller, while mutating it does?
- [ ] What do `/` and `*` do in a signature, and why use each?
- [ ] Why does `x += 1` on an enclosing name raise, while reading it does not?
- [ ] Why is `def f(t=time.time())` the same bug as `def f(acc=[])`?
- [ ] Name the two *different* aliasing bugs that the two `authors` tests catch
- [ ] Why must `newest` break ties deterministically?

## Commit

- [ ] `./m check && ./m done 10` succeeded
