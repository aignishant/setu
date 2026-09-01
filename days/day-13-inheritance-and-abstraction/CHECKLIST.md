# Day 13 — CHECKLIST

**IDs covered:** `PY-14`, `PY-15` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 14, in [`parts/`](parts/)

> `./m done 13` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_loaders.py -v && ./m check
```

Expected: the six parametrised tests passing for both loaders, plus the base-refuses test, the
`load_all` failure test and the stranger-class test. Then a green gate.

---

## Setup

- [ ] Created `src/setu/loaders/` with `__init__.py`, `base.py`, `text.py`, `html.py`, and `tests/test_loaders.py`
- [ ] Ran `uv run python -c "from setu.paper import Paper; print('ok')"` **before** writing anything
- [ ] Ran the six-fact setup block in the hub's §3 and can say what each of the six lines proved
- [ ] Read `uv run ruff rule B024` and `uv run ruff rule B027` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — inheritance

- [ ] Read [1.1 — one form that starts from another](parts/01-inheritance/1.1-one-form-that-starts-from-another.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — `super()` and the `__init__` that runs twice](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — the MRO](parts/01-inheritance/1.3-the-mro.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — overriding and the broken promise](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — composition over inheritance](parts/01-inheritance/1.5-composition-over-inheritance.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed a subclass's own `__dict__` and confirmed it defines **one** name while the object can do three things
- [ ] Confirmed `isinstance(child, Parent)` and `issubclass(Child, Parent)` are both `True`
- [ ] Watched one inherited method print three different class names via `type(self).__name__`
- [ ] Subclassed `dict` and confirmed the result has `clear()`, then emptied it from outside
- [ ] Wrote a subclass `__init__` with **no** `super()` and read the `AttributeError`
- [ ] Moved `super().__init__()` to the **last** line and used a parent field above it — same message, different cause
- [ ] Triggered `takes 2 positional arguments but 3 were given` by passing `self` to `super()`
- [ ] Triggered `RuntimeError: super(): __class__ cell not found` outside a class body
- [ ] Used `super().method()` to **extend** a parent's answer rather than replace it
- [ ] Built the `D(B, C)` diamond and printed `__mro__`
- [ ] Confirmed `Source` comes **after** `Scanned`, and can say which rule puts it there
- [ ] Watched `super()` inside the first parent reach the **second parent**, not the grandparent
- [ ] Removed one `super()` call from the chain and watched a step disappear with no error
- [ ] Triggered `Cannot create a consistent method resolution order`
- [ ] Wrote an override with an extra **required** parameter and broke a base-written caller
- [ ] Wrote an override returning `None` and watched the caller's `for` loop raise
- [ ] **Misspelled an overridden method name** and confirmed the base's version ran silently
- [ ] Wrote the parametrised contract test that catches all three
- [ ] Built the same behaviour by inheritance and by composition, and compared `dir()` on each
- [ ] Passed a four-line fake into the composed version and asserted on its call count

---

## Section 2 — polymorphism

- [ ] Read [2.1 — one name, three behaviours](parts/02-polymorphism/2.1-one-name-three-behaviours.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — duck typing and `isinstance`](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — Liskov in plain words](parts/02-polymorphism/2.3-liskov-in-plain-words.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote one loop over three classes with **no `if` and no `isinstance`**
- [ ] Added a fourth class and counted how many existing lines changed — it should be zero
- [ ] Wrote the branch-chain version and confirmed a new kind needs an edit in every copy of the chain
- [ ] Wrote a branch with no `else` and watched the new kind return `None`
- [ ] Passed a class that inherits **nothing** into a function written for the base, and watched it work
- [ ] Added an `isinstance` gate and confirmed it rejects the object that worked
- [ ] Confirmed `type(child) == Base` is `False` while `isinstance(child, Base)` is `True`
- [ ] Wrote a `hasattr` guard, saw it turn a loud failure into an empty result, and removed it
- [ ] Ran `isinstance` against a plain `Protocol` and read the `@runtime_checkable` error
- [ ] Wrote a class whose `read` returns a string and watched a caller iterate it character by character
- [ ] Ran the four-subclass substitution table and can name which rule each failure breaks
- [ ] Watched a subclass's new exception type escape a handler written for the base
- [ ] Wrote a `raise NotImplementedError` in a concrete subclass and can say what it means about the hierarchy

---

## Section 3 — encapsulation

- [ ] Read [3.1 — public, `_protected`, `__private`](parts/03-encapsulation/3.1-public-protected-private.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — name mangling](parts/03-encapsulation/3.2-name-mangling.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — the invariant](parts/03-encapsulation/3.3-the-invariant.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Read **and wrote** a single-underscore attribute from outside the class, with no error
- [ ] Printed `vars()` and found `_ClassName__name` where the source said `__name`
- [ ] Read a mangled attribute from outside using its full name
- [ ] Assigned `obj.__x` from **outside** a class and confirmed a second, differently-named attribute appeared
- [ ] Printed `Method.__code__.co_names` and found the mangled name in the bytecode
- [ ] Set the same `__x` in a base and a child and confirmed **two** attributes exist
- [ ] Confirmed a single-underscore name in the same position gives **one** attribute
- [ ] Watched a child fail to override a parent's `__`-prefixed value, with no error
- [ ] Confirmed a nested class mangles with the **inner** class's name
- [ ] Changed a class's internals and confirmed a caller using only the public surface was unaffected
- [ ] Built the two-field counter, broke its invariant from outside in one line, and printed the mismatch
- [ ] Rewrote it to **derive** the second value, and confirmed the same line could not break it
- [ ] Returned the object's own list from a method and mutated the object through it
- [ ] Added `list(...)` and confirmed the object survived
- [ ] Bypassed a constructor's validation with one assignment afterwards, and can say what Day 15 adds

---

## Section 4 — abstraction

- [ ] Read [4.1 — `abc.ABC` and `@abstractmethod`](parts/04-abstraction/4.1-abc-and-abstractmethod.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the loader family](parts/04-abstraction/4.2-the-loader-family.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `Protocol` versus ABC](parts/04-abstraction/4.3-protocol-versus-abc.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Triggered `Can't instantiate abstract class ... without an implementation for abstract method`
- [ ] Confirmed a subclass that implements nothing is abstract too
- [ ] **Removed `ABC` from the base line** and watched the class instantiate with an inert decorator
- [ ] Put `@abstractmethod` above `@property` and read the `__isabstractmethod__` error at import
- [ ] Misspelled an override under an ABC and watched it fail **at construction**, naming the real method
- [ ] Compared where the failure lands with a placeholder against an abstract method, in a build-then-read batch
- [ ] Used an abstract method **with a body** and called it from a subclass with `super()`
- [ ] Ran the nominal-versus-structural table and can say why `JustHasIt` passes one and not the other
- [ ] Wrote a two-line `Protocol` for `read` and passed both `io.StringIO` and a fake to the same function
- [ ] Confirmed a runtime-checkable `Protocol` says `True` for a class with the right method **name** and the wrong signature
- [ ] Put a method body in a `Protocol` and confirmed a matching class does **not** inherit it

---

## Build brief

- [ ] `src/setu/loaders/base.py` written: `Reader` protocol, `LoaderError`, and an abstract `BaseLoader`
- [ ] The base's class docstring states **returns, raises, promises** for `load()`
- [ ] `BaseLoader` has exactly **one** abstract method
- [ ] `reader` is **held** and named `_reader`, and I can say what that buys in a test
- [ ] `TextLoader` and `HTMLLoader` written, each with `super().__init__(...)` as the **first** line
- [ ] Each loader's extra configuration is a **keyword-only constructor argument with a default**
- [ ] Both `load()` methods return `list[Paper]`, `[]` when empty, and wrap every reader failure in `LoaderError`
- [ ] Every `Paper` produced carries a `source` (Principle 9)
- [ ] `LOADERS` registry written, and adding a format is genuinely **one line**
- [ ] `load_all` written with one `try`, one `except LoaderError`, and **no `isinstance` anywhere**
- [ ] `load_all` collects failures rather than stopping at the first one
- [ ] The `Reader` docstring says whether it is a `Protocol` or an ABC **and why**
- [ ] Read both `load()` methods side by side and moved up only what is genuinely identical
- [ ] Notebook traps reproduced in `notebooks/day-13-scratch.ipynb`, and **the notebook is not committed**

---

## The tests

- [ ] Every test in §5 written and **failing** before any implementation
- [ ] `make()` helper written, and **no test in the file touches a disk or a network**
- [ ] `test_base_loader_cannot_be_instantiated` — asserts on the message, not only the exception type
- [ ] `test_every_loader_returns_a_list_of_papers` — parametrised over `LOADERS.values()`
- [ ] `test_every_loader_returns_an_empty_list_for_empty_input` — uses `== []`, not `not result`
- [ ] `test_every_loader_raises_only_loader_error` — uses a `RaisingReader`
- [ ] `test_every_loader_is_safe_to_call_twice`
- [ ] `test_every_loader_sets_provenance`
- [ ] `test_load_all_keeps_the_good_papers_when_one_loader_fails`
- [ ] `test_a_stranger_class_is_not_a_baseloader_and_still_works`
- [ ] **Break it, watch it go red, fix it** — remove `ABC` → only the base-refuses test goes red
- [ ] **Break it, watch it go red, fix it** — return `None` for empty → **two** tests go red
- [ ] **Break it, watch it go red, fix it** — drop the `except` around the reader → only that loader's row goes red
- [ ] **Break it, watch it go red, fix it** — `super().__init__()` last → every test for that loader goes red
- [ ] **Break it, watch it go red, fix it** — rename `load` to `laod` → fails at **construction**, naming `load`
- [ ] **Break it and watch six stay GREEN** — iterate `self._reader` instead of calling `read()`.
      Only `safe_to_call_twice` goes red. Say why the other six were green before restoring it.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] **0** files opened from disk by any test
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-13-inheritance-and-abstraction/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 13` reports no failures
- [ ] `./m done 13`
