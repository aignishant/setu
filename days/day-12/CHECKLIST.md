# Day 12 — CHECKLIST

**IDs covered:** PY-13 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-12/lab/classes.py
uv run python -m pytest tests/test_papers.py -v
```

Expected: the class-anatomy report, then **twelve green tests**.

## Setup

- [ ] `./m start 12` and `./m scaffold 12` run
- [ ] `days/day-12/lab/classes.py` created
- [ ] Day 10's dict version of `papers.py` kept until the new tests are green
- [ ] No new packages installed

## PY-13 — anatomy

- [ ] Ran all four demo functions
- [ ] Can define class / instance / attribute / method in one sentence each
- [ ] Saw two instances hold separate instance attributes but share the class attribute
- [ ] Ran `Counter.bump(c, 10)` and understood that `self` is just the first argument
- [ ] Ran `the_class_attribute_trap()` and saw `y.tags` change when you touched `x.tags`
- [ ] Can name the **two earlier days** where this same shared-mutable bug appeared
- [ ] Confirmed `_history` is reachable from outside — the underscore is a message, not a lock
- [ ] Set `c.value = -999` and noticed nothing validated it

## Build brief

- [ ] `papers.py` rewritten with `MIN_YEAR`/`MAX_YEAR`, `InvalidPaper`, `Paper`
- [ ] `__init__` — **TODO(me)**: validates, normalises the title via `textutils`, copies authors
- [ ] `summarise` — **TODO(me)**: reuses `truncate`, handles no authors
- [ ] `is_recent` — **TODO(me)**
- [ ] `add_author` — **TODO(me)**: mutates, returns `None`, rejects blank
- [ ] `newest` — **TODO(me)**: ties A–Z, does not mutate the input
- [ ] Understood why the parameter is `paper_id` and not `id`

## Tests that must be able to fail

- [ ] All twelve were red before you implemented the TODOs
- [ ] `test_title_is_normalised_on_construction` — green
- [ ] `test_invalid_construction_raises` — four green cases
- [ ] `test_authors_default_is_not_shared_between_instances` — green
- [ ] **Moved `authors` to a class attribute, watched it go red, reverted** ← do not skip
- [ ] `test_authors_are_copied_from_the_caller` — green
- [ ] `test_authors_accepts_any_iterable` — green (a generator, stored as a list)
- [ ] **Wrote `self.authors = authors or []`, watched the generator test go red, fixed it** ← do not skip
- [ ] `test_add_author_returns_none_and_mutates` — green
- [ ] `test_add_author_rejects_blank` — green
- [ ] `test_summarise_respects_width_and_names_the_first_author` — green
- [ ] `test_summarise_handles_no_authors` — green
- [ ] `test_is_recent_boundary` — three green cases
- [ ] **Changed `>=` to `>`, watched the boundary case go red, reverted** ← do not skip
- [ ] `test_newest_breaks_ties_alphabetically` and `test_newest_does_not_mutate_the_input` — green

## Cleanup

- [ ] Only after everything above is green: deleted Day 10's `make_paper` and module-level `summarise`
- [ ] Re-ran the full suite; still green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the difference between a class attribute and an instance attribute?
- [ ] Why is `c.bump(10)` the same thing as `Counter.bump(c, 10)`?
- [ ] Why must mutable state be created in `__init__`?
- [ ] What does a leading underscore actually enforce?
- [ ] Why does the constructor take an iterable but store a list?
- [ ] Why is all validation in `__init__` and none of it in the methods?
- [ ] When should something stay a function instead of becoming a class?

## Commit

- [ ] `./m check && ./m done 12` succeeded
