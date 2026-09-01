# Day 15 — CHECKLIST

**IDs covered:** `PY-17`, `PY-18` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 16, in [`parts/`](parts/)

> `./m done 15` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_paper_api.py -v && ./m check
```

Expected: fifteen tests plus the three parametrised repr rows passing, then a green gate.

---

## Setup

- [ ] Created `tests/test_paper_api.py` and `src/setu/book.py`
- [ ] Ran `uv run python -c "from setu.decorators import retry, timed; print('ok')"` **before** writing anything
- [ ] Ran `uv run python -c "from setu.paper import Paper; print('ok')"` and read the existing `Paper`
- [ ] Ran the seven-fact setup block in the hub's §3 and can say what each of the seven lines proved
- [ ] Read `uv run ruff rule PLW1641` and `uv run ruff rule B019` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — three kinds of method

- [ ] Read [1.1 — the method that receives the class](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the second door in](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `staticmethod`](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `cls` and inheritance](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Called a classmethod on the class **and** on an instance and got the same answer
- [ ] Printed `Contact.describe.__self__` and confirmed it is the class
- [ ] Named a classmethod's first parameter `self` and read `type object 'X' has no attribute`
- [ ] Deleted `@classmethod` and read `missing 1 required positional argument: 'cls'`
- [ ] Called an ordinary method on the class and read `missing 1 required positional argument: 'self'`
- [ ] Built the same object through `__init__` and through a `from_*` classmethod
- [ ] Confirmed the classmethod's whitespace was cleaned by `__init__` and not by itself
- [ ] Removed the `return` from an alternative constructor and read the `AttributeError` on `None`
- [ ] Used `cls.__new__(cls)` and built an object `__init__` would have refused
- [ ] Wrote the "clever `__init__`" with three optional parameters and produced two nonsense objects
- [ ] Compared `type(Contact.__dict__['normalise'])` with `type(Contact.normalise)`
- [ ] Read `NameError: name 'self' is not defined` from a staticmethod
- [ ] Confirmed a missing `@staticmethod` works on the class and fails on an instance
- [ ] Watched a staticmethod naming its own class ignore a subclass's override
- [ ] Called an inherited `from_*` on a subclass with `cls` and with a hard-coded name, and compared the types
- [ ] Read `AttributeError: 'Contact' object has no attribute 'badge'` and traced it back to the constructor

---

## Section 2 — `property`

- [ ] Read [2.1 — a property is worked out](parts/02-property/2.1-a-property-is-worked-out.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — the setter](parts/02-property/2.2-the-setter-and-validation.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — the property that did real work](parts/02-property/2.3-the-property-that-did-real-work.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `cached_property`](parts/02-property/2.4-cached-property-and-the-stale-cache.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `vars(obj)` and confirmed the property is **not** in it
- [ ] Changed a stored field and watched the derived value follow
- [ ] Put brackets on a property and read `'int' object is not callable`
- [ ] Assigned to a getter-only property and read `has no setter`
- [ ] Read a method as an attribute, put it in an `if`, and watched the branch always pass
- [ ] Named a property the same as the attribute `__init__` assigns, and read the failure **inside `__init__`**
- [ ] Wrote a setter, assigned a bad value, and confirmed the **old value survived**
- [ ] Confirmed the same message comes from a constructor and from an assignment
- [ ] Wrote `self.number` instead of `self._number` in a setter and read the `RecursionError`
- [ ] Wrote to the underscore name from outside and skipped the setter entirely
- [ ] Counted the reads of an expensive property in three lines of ordinary-looking code
- [ ] Measured the same three lines with the value read once into a name
- [ ] Made a property raise on a missing field and watched it kill a loop from inside an f-string
- [ ] Put a side effect in a property and watched two reads disagree
- [ ] Compared `property` and `cached_property` on the same body, twice each
- [ ] Found the cached value in `vars(obj)` and cleared it with `del`
- [ ] Changed the input in place and read the stale cached answer
- [ ] Put a `cached_property` on a `__slots__` class and read the `TypeError`
- [ ] Assigned to a `cached_property` and confirmed it silently accepted the value

---

## Section 3 — the dunders

- [ ] Read [3.1 — what a dunder is](parts/03-the-dunders/3.1-what-a-dunder-method-is.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `__repr__` and `__str__`](parts/03-the-dunders/3.2-repr-and-str.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — `__eq__`](parts/03-the-dunders/3.3-eq-and-the-duplicate.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — `__hash__`](parts/03-the-dunders/3.4-hash-and-the-broken-set.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — `__len__` and `__bool__`](parts/03-the-dunders/3.5-len-and-bool.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed `len(x)` and `x.__len__()` print the same marker
- [ ] Read `object of type 'X' has no len()` and named the missing dunder
- [ ] Set `__len__` on an **instance** and confirmed `len()` still fails
- [ ] Gave a dunder the wrong number of parameters and read the message blaming your class
- [ ] Returned a string from `__len__` and read `cannot be interpreted as an integer`
- [ ] Printed the same object with `print(x)` and with `print([x])` on a class that has both dunders
- [ ] Wrote only `__str__` and confirmed a **list** of the objects is still useless
- [ ] Made `__repr__` raise on one object and watched the whole list become unprintable
- [ ] Hard-coded a class name in `__repr__` and watched a subclass lie about itself
- [ ] Ran a deduplicator over two identical objects and got two back
- [ ] Read an `AssertionError` whose two sides are character-for-character identical
- [ ] Returned `False` from `__eq__` and produced an asymmetric comparison
- [ ] Changed an equality field and watched an object leave a list it was in
- [ ] Printed `SomeClass.__hash__` after defining `__eq__` and saw `None`
- [ ] Hashed **more** fields than equality compares and put two equal objects in one set
- [ ] Mutated a hashed field and watched `a in s` be `False` while `s` shows the object
- [ ] Overrode `__eq__` in a subclass and lost `__hash__` again
- [ ] Ran `hash('Mum')` in two processes and got two numbers
- [ ] Added `__len__` and watched `if not x:` change meaning on an empty object
- [ ] Returned an `int` from `__bool__` and read `should return bool, returned int`
- [ ] Watched `x or default` replace a real empty object with the default

---

## Section 4 — the `Paper` API

- [ ] Read [4.1 — ordering](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the container protocol](parts/04-the-paper-api/4.2-the-container-protocol.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — which dunders, and when to stop](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Called `sorted` on objects with no ordering and read the message naming `<`
- [ ] Confirmed `<` and `>` work from `__lt__` alone, and `>=` does not
- [ ] Removed `@functools.total_ordering` and found which comparison broke
- [ ] Sorted `(score, object)` tuples with a tie and read the `TypeError`
- [ ] Built a class where `a == b` and `a < b` are both true, and saw no error
- [ ] Ran `for x in c: assert x in c` on a container whose `__iter__` and `__contains__` disagree
- [ ] Stored one iterator in `__iter__` and watched the second loop return nothing
- [ ] Iterated a class with only `__getitem__` and confirmed it has no `__iter__`
- [ ] Made `__len__` and `__iter__` disagree and compared `len(x)` with `len(list(x))`
- [ ] Wrote an `__add__` on a domain object and asked somebody to guess what it does
- [ ] Used `__getattr__` as a catch-all and turned two typos into `None`

---

## Build

- [ ] `src/setu/paper.py` has `from_arxiv_id` and `from_row`, both returning `cls(...)`
- [ ] Both classmethods are annotated `-> Self`
- [ ] `normalise_title` reuses Day 7's `clean_title` rather than duplicating it
- [ ] `title` and `year` are **read-only** properties
- [ ] `age` is a property and satisfies all four of part 2.3's clauses
- [ ] `slug` is a `cached_property`, and the docstring says why that is safe here
- [ ] `__repr__` uses `type(self).__name__`, `!r`, and no long field
- [ ] `__eq__` returns `NotImplemented` for a non-`Paper`
- [ ] `__eq__`'s docstring states what makes two papers the same, in two sentences
- [ ] `__hash__` hashes **exactly** the fields `__eq__` compares
- [ ] Wrote down whether `Paper` gets a `__lt__`, and why, in one sentence
- [ ] `src/setu/book.py` states its "what is an item" decision **before** the methods
- [ ] `PaperBook.__init__` copies its input
- [ ] `PaperBook.__iter__` builds a fresh iterator on every call
- [ ] `PaperBook.__repr__` shows the count, not the papers
- [ ] Reproduced all seven traps in `notebooks/day-15-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)

---

## Tests

- [ ] `tests/test_paper_api.py` exists and every test failed before any implementation
- [ ] `test_both_doors_produce_the_same_type` passes
- [ ] `test_an_alternative_constructor_still_validates` passes
- [ ] `test_a_subclass_gets_itself_back` asserts on the **subclass**, not on a field
- [ ] `test_the_title_cannot_be_reassigned` asserts on the message
- [ ] `test_the_year_is_validated_on_construction` asserts the value is in the message
- [ ] `test_repr_names_the_class_and_omits_long_fields` asserts **both** content and length
- [ ] `test_a_subclass_repr_names_the_subclass` passes
- [ ] `test_two_papers_from_two_sources_are_one_paper` matches the docstring you wrote
- [ ] `test_a_paper_is_not_equal_to_a_string` asserts `is False` and that nothing raised
- [ ] `test_equal_papers_hash_equal` is written as an **equivalence**, not two assertions
- [ ] `test_a_set_of_duplicates_holds_one` passes
- [ ] `test_the_slug_is_stable_across_two_spellings` passes
- [ ] `test_the_book_len_matches_what_it_yields` passes
- [ ] `test_everything_in_the_book_is_in_the_book` passes
- [ ] `test_the_book_can_be_iterated_twice` passes
- [ ] `test_the_book_reprs_at_every_size` passes for **0**, 1 and 5
- [ ] **Break it, watch it go red, fix it** — `from_row` sets attributes directly → only the validation test goes red
- [ ] **Break it, watch it go red, fix it** — `from_arxiv_id` returns `Paper(...)` → only the subclass test goes red
- [ ] **Break it, watch it go red, fix it** — give `title` a setter → the read-only test goes red, hashing stays green
- [ ] **Break it, watch it go red, fix it** — put a long field in `__repr__` → the length assertion goes red, the content one stays green
- [ ] **Break it, watch it go red, fix it** — delete `__hash__` → the set test **and** the book tests go red
- [ ] **Break it, watch it go red, fix it** — hash the title as well → the invariant test goes red while every equality test stays green
- [ ] **Break it, watch it go red, fix it** — store one iterator in `PaperBook` → only the twice-iterated test goes red
- [ ] **Break it and watch every test stay GREEN** — make `__iter__` yield papers and `__contains__` test id strings,
      and delete `test_everything_in_the_book_is_in_the_book`. Everything passes and the container contradicts
      itself. Restore the test, watch it go red, and say what it was protecting.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today — including inside `from_arxiv_id`
- [ ] **0** files opened from disk by any test
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-15-constructors-and-dunders/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 15` reports no failures
- [ ] `./m done 15`
