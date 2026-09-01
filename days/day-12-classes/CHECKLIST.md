# Day 12 — CHECKLIST

**IDs covered:** `PY-13` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 12` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_paper.py -v && ./m check
```

Expected: every test passing, including the shape test that catches a conditional assignment and the
two `authors` tests that catch the two halves of the shared-mutable bug. Then a green gate.

---

## Setup

- [ ] Created `src/setu/paper.py`, `src/setu/dedup.py` and `tests/test_paper.py`
- [ ] Ran `uv run python -c "from setu.textutils import clean_title, title_key; print('ok')"` **before** writing anything
- [ ] Ran the five-fact setup block in the hub's §3 and can say what each of the five lines proved
- [ ] Ran the `__slots__` measurement and **wrote my own two numbers down**
- [ ] Read `uv run ruff rule B006` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — the blank form

- [ ] Read [1.1 — a class is a blank form](parts/01-the-blank-form/1.1-a-class-is-a-blank-form.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — `__init__` and `self`](parts/01-the-blank-form/1.2-init-and-self.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — methods find their object](parts/01-the-blank-form/1.3-methods-find-their-object.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — instance and class attributes](parts/01-the-blank-form/1.4-instance-and-class-attributes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — the shared class attribute](parts/01-the-blank-form/1.5-the-shared-class-attribute.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `type(instance).__name__` and confirmed it is my class, not `object`
- [ ] Confirmed `isinstance(Card, Card)` is `False` and can say why in one sentence
- [ ] Printed an instance with `print()` and read the address, then printed `vars()` instead
- [ ] Changed one instance's attribute and confirmed the other instance and the class were untouched
- [ ] Ran the `__new__`/`__init__` block and confirmed **all three addresses are the same**
- [ ] Called `Card.__init__(obj, ...)` by hand and watched it return `None`
- [ ] Wrote `return self` in `__init__` and read `TypeError: __init__() should return None`
- [ ] Wrote a method without `self` and read `takes 0 positional arguments but 1 was given`
- [ ] Used an attribute in a method that `__init__` never set, and confirmed the class imported fine
- [ ] Printed `card.summary` and `Card.summary` without brackets and read the two different words
- [ ] Confirmed `a.summary.__func__ is b.summary.__func__` is `True`
- [ ] Called a method through the class with the instance supplied by hand
- [ ] Stored a bound method, `del`'d the object, and confirmed the method still worked
- [ ] Read a class attribute through two instances without either owning it
- [ ] Wrote to one instance's copy and confirmed the class and the other instance were unchanged
- [ ] `del`'d the instance attribute and watched the class value reappear
- [ ] **Wrote `self.count += 1` with `count = 0` on the class**, built three, and got `Card.count == 0`
- [ ] Put `tags = []` in a class body and watched one `append` change every instance
- [ ] Printed both instances' `__dict__` and confirmed **neither contains `tags`**
- [ ] Fixed it with `self.tags = list(tags) if tags else []` and confirmed `a.tags is not b.tags`
- [ ] Tried the `clear()` + `extend()` "fix" and watched it fail the same way

---

## Section 2 — attribute lookup

- [ ] Read [2.1 — `__dict__`](parts/02-attribute-lookup/2.1-the-instance-dict.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — setting attributes from outside](parts/02-attribute-lookup/2.2-setting-attributes-from-outside.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `__slots__`](parts/02-attribute-lookup/2.3-slots-and-a-million-objects.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — your object and equality](parts/02-attribute-lookup/2.4-your-object-and-equality.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed an instance `__dict__` and a class `__dict__` side by side
- [ ] Confirmed `vars(obj) is obj.__dict__`
- [ ] Confirmed a method is in the **class's** dictionary and not the instance's
- [ ] Tried `Card.__dict__['x'] = 1` and read `'mappingproxy' object does not support item assignment`
- [ ] Wrote the four-line `look_up` function and watched it report `instance` and `class`
- [ ] Misspelled an attribute on a **write** and confirmed no error, then printed `vars()`
- [ ] Misspelled one on a **read** and read the `Did you mean:` suggestion
- [ ] Confirmed the suggestion points at an earlier typo once one exists
- [ ] Used `getattr(obj, name, default)` and `setattr` with names that came from a list
- [ ] Used `zip(..., strict=True)` when pairing headers with values, and can say what it prevents
- [ ] Shadowed a method with an instance attribute and read `'str' object is not callable`
- [ ] Measured `Plain` against `Slotted` and **wrote both numbers down**
- [ ] Confirmed a slotted instance has no `__dict__` and that `vars()` raises `TypeError`
- [ ] Assigned an undeclared attribute on a slotted object and read the `AttributeError`
- [ ] Triggered `'title' in __slots__ conflicts with class variable`
- [ ] Confirmed `__slots__ = ("title")` is a bare string, not a one-tuple
- [ ] Inherited from a class **without** slots and confirmed `__dict__` came back
- [ ] Built two objects with identical values and confirmed `vars(a) == vars(b)` and `a != b`
- [ ] Put both in a `set()` and got a length of **2**
- [ ] Confirmed `b in [a]` is `False` and `sorted([a, b])` raises
- [ ] Wrote a `same_book(a, b)` function and used it to deduplicate the three cards

---

## Section 3 — the `Paper` object

- [ ] Read [3.1 — designing `Paper`](parts/03-the-paper-object/3.1-designing-paper.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — validation in `__init__`](parts/03-the-paper-object/3.2-validation-in-init.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — a method or a function beside it?](parts/03-the-paper-object/3.3-method-or-function-beside-it.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — when not to write a class](parts/03-the-paper-object/3.4-when-not-to-write-a-class.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Sorted records with a year of `0` and watched the unknown one appear as the oldest
- [ ] Sorted the same records with `None` and read the `TypeError` instead
- [ ] Joined a `None` authors list and read the error a caller would get
- [ ] Ran the six-case `validate` block and read all five failure messages
- [ ] Confirmed `Paper("x", year=True)` is rejected, and watched it slip through without the bool clause
- [ ] Raised from `__init__` and confirmed the name was **never bound**
- [ ] Validated the raw title and stored it, then printed `repr(paper.title)` and saw the spaces
- [ ] Ran the five-row method-or-function decision table, and **added a sixth row of my own**
- [ ] Measured a class against a dict against a tuple for 200 000 records
- [ ] Can say why the class beat the dict, and why that does not settle which to use

---

## Build brief

- [ ] `src/setu/paper.py` created, importing `clean_title` from `setu.textutils` rather than reimplementing it
- [ ] Every field assigned **unconditionally** in `__init__`, including the ones that stay `None`
- [ ] `SOURCES` and `EARLIEST_YEAR` are class attributes, and `SOURCES` is a **tuple**
- [ ] Every field after `title` is keyword-only, behind a bare `*`
- [ ] `authors` is built per instance with `list(authors) if authors else []`
- [ ] Every `raise` carries the offending value with `!r`
- [ ] `citation()` and `is_preprint()` written, each documenting which question made it a method
- [ ] `src/setu/dedup.py` created with `same_paper` and `unique_papers`, and it imports `Paper` one way only
- [ ] The `__slots__` decision written in the class docstring, with the reason
- [ ] Notebook traps reproduced in `notebooks/day-12-scratch.ipynb`, and **the notebook is not committed**

---

## The tests

- [ ] Every test in §5 written and **failing** before any implementation
- [ ] `test_title_is_cleaned_and_stored_cleaned` — expectation written out by hand, not computed
- [ ] `test_empty_title_raises_value_error` — covers `""` **and** `"   "`
- [ ] `test_error_messages_carry_the_offending_value` — uses `pytest.raises(..., match=...)`
- [ ] `test_year_none_is_allowed_and_zero_is_not`
- [ ] `test_year_true_is_rejected`
- [ ] `test_every_field_exists_even_when_absent` — compares `set(vars(a)) == set(vars(b))`
- [ ] `test_authors_defaults_to_a_new_empty_list_each_time`
- [ ] `test_authors_copies_the_callers_list`
- [ ] `test_two_equal_papers_are_not_equal` — with a comment naming the day that changes it
- [ ] `test_same_paper_is_symmetric`
- [ ] `test_unique_papers_keeps_input_order_and_is_lazy`
- [ ] `test_unknown_source_is_rejected` — parametrised over three bad values
- [ ] **Break it, watch it go red, fix it** — `authors = []` on the class body → **two** tests go red
- [ ] **Break it, watch it go red, fix it** — drop the `list(...)` copy → **one** test goes red
- [ ] **Break it, watch it go red, fix it** — `isinstance(year, int)` alone → the bool test goes red
- [ ] **Break it, watch it go red, fix it** — `if doi: self.doi = doi` → the shape test goes red
- [ ] **Break it, watch it go red, fix it** — delete one `!r` → the message test goes red
- [ ] **Break it and watch it stay GREEN** — store the raw title, validate the cleaned one, with a test
      that computes its own expectation. Say why that assertion was worthless before restoring it.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-12-classes/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 12` reports no failures
- [ ] `./m done 12`
