# Day 9 — CHECKLIST

**IDs covered:** PY-09 · **Principles served:** 1, 3, 7

## Demo command

```bash
uv run python days/day-09/lab/comprehensions.py
uv run python -m pytest -q
```

Expected: the comprehension report, then the whole suite green.

## Setup

- [ ] `./m start 9` and `./m scaffold 9` run
- [ ] `days/day-09/lab/comprehensions.py` created
- [ ] No new packages installed

## PY-09 — the four forms

- [ ] Wrote the loop version and the comprehension version of the same transform
- [ ] Can read a comprehension aloud as a sentence, left to right
- [ ] Used a **list** comprehension `[...]`
- [ ] Used a **set** comprehension `{expr ...}`
- [ ] Used a **dict** comprehension `{k: v ...}` and saw a later key overwrite an earlier one
- [ ] Used a **generator** expression `(...)` and saw it come up empty on second use

## Conditions

- [ ] Used a trailing `if` to **filter**
- [ ] Used a leading `if/else` to **transform**
- [ ] Can state the difference in one sentence without hesitating
- [ ] Combined both in a single comprehension once

## Nesting and memory

- [ ] Flattened a list of lists and confirmed the `for` clauses read outer-first
- [ ] Built a nested list-of-lists with an inner comprehension
- [ ] Compared `sys.getsizeof` for a list comprehension vs a generator expression
- [ ] Ran `sum(...)` over a generator expression without building a list

## Discipline

- [ ] Read the five "use a loop instead" reasons **out loud**
- [ ] Can name at least three from memory

## Build brief

- [ ] `group_by_first_letter` — **TODO(me) implemented**; keys lowercased, values keep original case and order
- [ ] Can explain **why a dict comprehension alone cannot do it**
- [ ] `invert` — **TODO(me) implemented**, collecting duplicate values into lists
- [ ] `clean_all` — **TODO(me) implemented**, reusing `normalise_whitespace` and `is_blank`
- [ ] `clean_all` computes each cleaned value **once** — chose an approach and can defend it

## Tests that must be able to fail

- [ ] All were red before you implemented the TODOs
- [ ] `test_group_by_first_letter` — green (lowercased key, `"Banana"` casing preserved)
- [ ] `test_group_by_first_letter_preserves_input_order` — green
- [ ] **Used a set instead of a list inside the groups, watched the order test go red, fixed it** ← do not skip
- [ ] `test_group_by_first_letter_of_empty` — green
- [ ] `test_invert_collects_duplicate_values` — green
- [ ] **Wrote `invert` as a naive dict comprehension, watched it lose a key, fixed it** ← do not skip
- [ ] `test_clean_all_drops_blanks_and_normalises` — green
- [ ] `test_clean_all_calls_normalise_once_per_item` — green (a double-computing version reports 6)

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Read a two-clause comprehension aloud as an English sentence
- [ ] What is the difference between a trailing `if` and a leading `if/else`?
- [ ] Why does a dict comprehension silently lose data on duplicate keys?
- [ ] Why is a generator expression empty the second time you iterate it?
- [ ] In a flattening comprehension, which `for` clause comes first and why?
- [ ] Name three situations where a loop is the better choice
- [ ] Why can a comprehension never accidentally mutate its source?

## Commit

- [ ] `./m check && ./m done 9` succeeded
