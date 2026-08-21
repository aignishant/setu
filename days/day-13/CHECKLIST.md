# Day 13 — CHECKLIST

**IDs covered:** PY-14, PY-15 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-13/lab/inheritance.py
uv run python -m pytest tests/test_loaders.py -v
```

Expected: the inheritance report ending with a refused construction, then **twelve green tests**.

## Setup

- [ ] `./m start 13` and `./m scaffold 13` run
- [ ] Files created: `days/day-13/lab/inheritance.py`, `src/setu/loaders.py`, `tests/test_loaders.py`
- [ ] No new packages installed

## PY-14 — inheritance and polymorphism

- [ ] Ran all four demo functions
- [ ] Confirmed `describe()` was inherited without being rewritten
- [ ] Confirmed `cached.reads == 1` after three reads, and can explain why
- [ ] Used `super().__init__()` **first**, before the child's own setup
- [ ] Used `super().read()` inside an override to extend rather than replace
- [ ] Read `CachedSource.__mro__` aloud and can say what it is for
- [ ] Confirmed `isinstance` and `issubclass` results
- [ ] Saw duck typing work with **no shared base class**
- [ ] Can state the "is-a" test for when inheritance is the wrong tool

## PY-15 — encapsulation and abstraction

- [ ] Built an `ABC` with `@abstractmethod`
- [ ] Saw `Forgetful()` refused **at construction** with a `TypeError`
- [ ] Can say why failing at construction beats failing at use
- [ ] Wrote a concrete base method (`load_many`) built on an abstract one

## Build brief

- [ ] `src/setu/loaders.py` created with `UnsupportedFormat` and `BaseLoader`
- [ ] `BaseLoader.load` — **TODO(me)**: reads UTF-8, checks suffix, delegates to `_parse`, normalises
- [ ] `BaseLoader.load_many` — **TODO(me)**, concrete, never overridden
- [ ] `TextLoader._parse` — **TODO(me)**
- [ ] `MarkdownLoader._parse` — **TODO(me)**, no regex
- [ ] `HTMLLoader._parse` — **TODO(me)**, deliberately naive
- [ ] `loader_for` — **TODO(me)**, built from `__subclasses__()`, not a hard-coded dict
- [ ] Noted in your commit message **one HTML input the naive stripper gets wrong**

## Tests that must be able to fail

- [ ] All twelve were red before you implemented the TODOs
- [ ] `test_base_loader_cannot_be_instantiated` — green
- [ ] `test_incomplete_subclass_cannot_be_instantiated` — green
- [ ] **Removed `@abstractmethod`, watched both guards silently pass, put it back** ← do not skip
- [ ] `test_text_loader_normalises_whitespace` — green
- [ ] `test_markdown_strips_syntax` — green
- [ ] `test_html_strips_tags` — green
- [ ] `test_wrong_suffix_is_rejected` — green
- [ ] `test_missing_file_raises` — green
- [ ] `test_load_many_is_inherited_not_overridden` — green
- [ ] `test_load_many_returns_one_result_per_path` — green
- [ ] `test_loader_for_dispatches` — three green cases
- [ ] `test_loader_for_rejects_unknown_suffix` — green
- [ ] `test_a_new_loader_needs_no_registry_edit` — green ← **today's real assessment**
- [ ] **Rewrote `loader_for` as a hard-coded dict, watched that one go red, reverted** ← do not skip

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What problem does polymorphism solve that an `if/elif` chain does not?
- [ ] Why must `super().__init__()` be called, and why first?
- [ ] What is the MRO and when do you need to read it?
- [ ] What is the difference between duck typing and an ABC, and why does this project prefer ABCs?
- [ ] Why is `_parse` abstract while `load` is concrete?
- [ ] Why does `loader_for` build its registry from `__subclasses__()`?
- [ ] Give a case where inheritance is the wrong answer and composition is right

## Commit

- [ ] `./m check && ./m done 13` succeeded
