# Day 4 — CHECKLIST

**IDs covered:** PY-01, PY-02 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-04/lab/explore_objects.py
uv run python -m pytest tests/test_textutils.py -v
```

Expected: the object/mutability report, then **six green tests**.

## Setup

- [ ] `./m start 4` and `./m scaffold 4` run
- [ ] Files created: `days/day-04/lab/explore_objects.py`, `src/setu/textutils.py`, `tests/test_textutils.py`
- [ ] No new packages installed (standard library only today)

## PY-01 — everything is an object

- [ ] `describe()` written and run; output shows type, id and `repr` for all six values
- [ ] Confirmed `isinstance(True, int)` is `True` and `True + True` is `2`
- [ ] Confirmed `0.1 + 0.2 == 0.3` is `False` — and looked at the actual printed sum
- [ ] Used the `f"{expr=}"` debug form at least once yourself

## PY-02 — mutability

- [ ] `mutability_demo()` written and run
- [ ] Saw `y` change after `x.append(4)` **with your own eyes**
- [ ] Saw `id(s)` change after `s = s.upper()`
- [ ] Ran `t.strip()` with the result discarded and confirmed `t` was unchanged
- [ ] Wrote out the mutable/immutable two-column table from memory, then checked it

## The mutable-default trap

- [ ] Ran `collect_broken("a")` then `collect_broken("b")` and got `['a']` then `['a', 'b']`
- [ ] Ran the fixed `collect` and got `['a']` then `['b']`
- [ ] Can say **out loud** *when* a default argument is evaluated

## Build brief

- [ ] `src/setu/textutils.py` created with the module docstring
- [ ] `normalise_whitespace` read and understood — can explain why `" ".join(text.split())` beats `.replace("  ", " ")`
- [ ] `clean_title` — **TODO(me) implemented by you**
- [ ] `dedupe_preserving_order` — **TODO(me) implemented by you, without mutating the input**
- [ ] Neither function does any I/O or touches a global

## Tests that must be able to fail

- [ ] All six tests were **red** before you implemented the TODOs
- [ ] `test_normalise_collapses_all_whitespace` — green
- [ ] `test_clean_title_strips_trailing_period` — green
- [ ] `test_clean_title_leaves_inner_periods` — green (this one catches a naive `.replace(".", "")`)
- [ ] `test_dedupe_preserves_first_seen_order` — green
- [ ] `test_dedupe_does_not_mutate_its_input` — green ← **today's real assessment**
- [ ] `test_normalise_handles_empty_input` — three green parametrised cases
- [ ] Deliberately broke `dedupe` to mutate the input, watched the mutation test go red, fixed it

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are the three things every Python object has?
- [ ] Why does `y` change when you append to `x`, and what would prevent it?
- [ ] Why does `t.strip()` on its own line accomplish nothing?
- [ ] When is a default argument evaluated, and why does that make `= []` a bug?
- [ ] Why `is None` rather than `== None`?
- [ ] Why is `.copy()` not enough for a list of lists?
- [ ] Name the *same* mutability bug as it will appear in pandas (Day 30) and in LangGraph state (Day 193)

## Commit

```bash
./m check
./m done 4
```

- [ ] `./m done 4` succeeded
