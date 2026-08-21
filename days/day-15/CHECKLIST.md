# Day 15 — CHECKLIST

**IDs covered:** PY-17, PY-18 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-15/lab/dunders.py
uv run python -m pytest tests/test_papers.py -v
```

Expected: the method-decorator and dunder report, then the whole `test_papers.py` suite green.

## Setup

- [ ] `./m start 15` and `./m scaffold 15` run
- [ ] `days/day-15/lab/dunders.py` created
- [ ] No new packages installed

## PY-17 — method decorators

- [ ] Built two `@classmethod` alternative constructors
- [ ] Used `cls(...)`, never the class name
- [ ] Ran `cls_is_subclass_safe()` and saw `Kelvinish` come back, not `Temperature`
- [ ] Built a `@staticmethod` and called it without an instance
- [ ] Can say when a `@staticmethod` should really have been a module function
- [ ] Built a `@property` getter and a matching `@x.setter`
- [ ] Confirmed `__init__` assigning to the **public** name runs the setter's validation
- [ ] Built a **read-only** computed property and saw assignment raise `AttributeError`

## PY-18 — dunders

- [ ] Implemented `__repr__` and `__str__`; confirmed a list prints reprs
- [ ] Implemented `__eq__` returning **`NotImplemented`** for unknown types
- [ ] Implemented `__hash__` over the same fields as `__eq__`
- [ ] Confirmed a set of two equal objects has length 1
- [ ] Implemented `__lt__` and used bare `sorted()`
- [ ] Implemented the container protocol (`__len__`, `__getitem__`, `__iter__`, `__contains__`, `__bool__`)
- [ ] Confirmed an empty container is falsy, connecting back to Day 5

## Build brief — Paper

- [ ] `from_row` — **TODO(me)**, uses `cls`, coerces a string year, raises `InvalidPaper`
- [ ] `from_line` — **TODO(me)**, raises on the wrong field count
- [ ] `year` property getter and setter — **TODO(me)**, stores on `_year`
- [ ] `__init__` assigns to `self.year`, not `self._year`
- [ ] `age` — **TODO(me)**, read-only, no setter
- [ ] `is_plausible_year` — **TODO(me)**, `@staticmethod`
- [ ] `__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__`, `__len__` — all **TODO(me)** implemented
- [ ] `newest` simplified to `sorted(papers)[:n]` now that `__lt__` encodes the order

## Tests that must be able to fail

- [ ] `test_from_row_uses_cls_so_subclasses_work` — green
- [ ] **Hard-coded `Paper(...)` in `from_row`, watched it go red, restored `cls`** ← do not skip
- [ ] `test_from_row_coerces_year_from_string` — green
- [ ] `test_from_row_missing_key_raises_invalid_paper` — green (not a bare `KeyError`)
- [ ] `test_from_line_wrong_field_count` — green
- [ ] `test_year_setter_validates_after_construction` — green
- [ ] **Stored before validating, watched the second assertion go red, fixed the order** ← do not skip
- [ ] `test_age_is_read_only` — green
- [ ] `test_is_plausible_year_needs_no_instance` — green
- [ ] `test_repr_is_unambiguous_and_str_is_readable` — green
- [ ] `test_equality_is_by_id_and_hash_agrees` — green
- [ ] **Deleted `__hash__`, saw `TypeError: unhashable type`, restored it** ← do not skip
- [ ] `test_equality_with_another_type_is_false_not_an_error` — green
- [ ] `test_sorting_is_newest_first_then_alphabetical` — green with **no `key=` argument**
- [ ] `test_len_is_the_author_count` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why must a classmethod use `cls` rather than the class name?
- [ ] What does a `@property` let you change later without touching call sites?
- [ ] Why does a property setter store on `_year` rather than `year`?
- [ ] What is the difference between `__repr__` and `__str__`, and which do you write first?
- [ ] Why return `NotImplemented` rather than `False` from `__eq__`?
- [ ] What does Python do to `__hash__` when you define `__eq__`, and why?
- [ ] Which single dunder gives you `sorted`, `min` and `max`?

## Commit

- [ ] `./m check && ./m done 15` succeeded
