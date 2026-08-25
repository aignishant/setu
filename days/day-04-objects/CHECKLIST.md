# Day 4 — CHECKLIST

**IDs covered:** `PY-01`, `PY-02` · **Principles served:** 1, 2, 3, 6, 7, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 4` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_objects.py -v && ./m check
```

Expected: six passing tests, including the one that calls a buggy function three times, and a green
gate.

---

## Section 1 — objects and the scalar types (`PY-01`)

- [ ] Read [1.1 — identity, type, value](parts/01-objects/1.1-identity-type-value.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — names are labels](parts/01-objects/1.2-names-are-labels.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — numbers and booleans](parts/01-objects/1.3-numbers-and-bool.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — strings are immutable](parts/01-objects/1.4-strings-are-immutable.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — why `"3" + 3` raises](parts/01-objects/1.5-why-str-plus-int-is-a-typeerror.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `id()`, `type()` and the value of one object, and can name which two never change
- [ ] **Predicted** the `b`/`c` result in 1.1's check-yourself before running it — and was right
- [ ] Watched `y = y + 1` change `id(y)` while `id(x)` stayed the same
- [ ] Watched `b.append(4)` leave both ids identical
- [ ] Wrote `rebind` and `mutate` and confirmed only one of them reached the caller
- [ ] Ran `[[0] * 3] * 3` and can explain the result using the label model
- [ ] Printed `Decimal(0.1)` and saw what a float actually stores
- [ ] Compared floats with `math.isclose` and tightened the tolerance until it failed again
- [ ] Confirmed `nan != nan` and that `math.isnan` is the test
- [ ] Confirmed `bool("false")` is `True`, and wrote a `parse_flag` that is not fooled
- [ ] Timed `+=` string building against `join`, then **doubled the input** and saw the ratio change
- [ ] Saw `title.strip()` with no assignment do nothing
- [ ] Read both `TypeError` messages for `"3" + 3` and `3 + "3"` and can say what the difference tells you
- [ ] Can name a `ValueError` that is not a `TypeError`, and why the distinction matters

## Section 2 — containers and mutability (`PY-02`)

- [ ] Read [2.1 — the four containers](parts/02-containers/2.1-the-four-containers.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — what "in place" means](parts/02-containers/2.2-what-in-place-means.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — aliasing](parts/02-containers/2.3-aliasing-two-names-one-object.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — shallow and deep copy](parts/02-containers/2.4-shallow-and-deep-copy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — hashability](parts/02-containers/2.5-hashability.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built all four containers and answered the three questions for each
- [ ] **Timed list `in` against set `in` at three sizes** and watched the *ratio* grow
- [ ] Confirmed `{}` is an empty dict and `set()` is the empty set
- [ ] Used set difference, intersection and union instead of a loop
- [ ] Saw `items.sort()` return `None` and `sorted(items)` return a list
- [ ] Ran the full paired vocabulary and confirmed every mutating call returned `None`
- [ ] Saw `+=` mutate a list and rebind a tuple, in the same loop
- [ ] Found an alias created **without** `b = a` — inside a list, inside a dict, and via a call
- [ ] Reproduced the shared-default bug and watched output grow across three calls
- [ ] Applied all three defences and confirmed only the unsafe one reached the caller
- [ ] Confirmed `shallow[0] is rows[0]` is `True` and `deep[0] is rows[0]` is `False`
- [ ] Timed alias, shallow copy, deep copy and rebuild on nested data
- [ ] Confirmed `(1, [2])` is unhashable and can explain which part is to blame
- [ ] Built the deliberately-broken mutable-key class and watched an entry become unreachable
- [ ] Used a `frozenset` key and confirmed the lookup ignores order

## Section 3 — where identity and mutability meet

- [ ] Read [3.1 — the mutable default argument](parts/03-identity-trap/3.1-the-mutable-default-argument.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `is` versus `==`](parts/03-identity-trap/3.2-is-versus-equals.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Reproduced the mutable-default bug with my own hands** before reading the fix
- [ ] Printed `func.__defaults__` and confirmed its `id` never changes across calls
- [ ] Wrote the `is None` fix and confirmed three calls give three independent results
- [ ] Wrote the `if not acc:` version and watched it **silently discard** a caller's empty list
- [ ] Saw the same bug in a class attribute, and in a dataclass field
- [ ] Confirmed a `@dataclass` refuses a mutable default with a `ValueError`
- [ ] Saw `256 is int(str(256))` and `257 is int(str(257))` give different answers
- [ ] Saw a run-time-built string not share an object with an identical literal
- [ ] Wrote a class whose `__eq__` returns `True` for everything, and confirmed `is None` was immune
- [ ] Triggered `SyntaxWarning: "is" with a literal` at least once

## Section 4 — the standard underneath

- [ ] Read [*IEEE 754*](papers/01-ieee-754.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built `float-microscope/` from 4.1's demo and read `0.1`'s exact 55-place value out of its own bits
- [ ] Found the rounded final digit in `(0.1).hex()` and can say why that `a` is the whole bug
- [ ] Watched `1e308 * 10` overflow to `inf` **without raising**, then produce `nan` on subtraction
- [ ] Confirmed `0.5` and `0.75` are exact — floats are not randomly wrong
- [ ] Can name the two places money must never be a `float`, and what to use instead

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/objects.py` — the first real code in `src/setu/` (Principle 6)
- [ ] Implemented `shares_object` — one line, using the identity operator
- [ ] Implemented `is_deeply_immutable` — recurses into tuples and frozensets
- [ ] **Wrote the comment deciding whether `hash()` is a valid shortcut**, and why
- [ ] Implemented `independent_copy` — a rebuild, **not** `deepcopy`
- [ ] Implemented `count_shared` — and can say why it cannot use a set
- [ ] Reproduced the mutable-default bug in `notebooks/day-04-scratch.ipynb`
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/`
- [ ] `uv run ruff check src/` passes, including `B006`

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_objects.py -v` **before** implementing and watched all six fail
- [ ] Implemented `test_assignment_aliases_and_rebinding_does_not`
- [ ] Implemented `test_shallow_copy_shares_inner_objects` — asserts **both** halves
- [ ] Implemented `test_mutable_default_accumulates_and_the_fix_does_not` — **three** calls each
- [ ] Implemented `test_deep_immutability_goes_all_the_way_down`
- [ ] Implemented `test_count_shared_finds_the_multiplied_grid` — with the comment explaining the `2`
- [ ] Implemented the parametrised `test_equal_values_need_not_be_the_same_object`
- [ ] **Break it, watch it go red, fix it —** changed `shares_object` to `==`, saw **two** tests go red, and can say why each did. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `independent_copy` return `value.copy()`, saw the copy test go red. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `is_deeply_immutable` return `True` for any tuple. Restored it.
- [ ] **The one that matters most —** reduced the mutable-default test from three calls to one, watched it **pass against the buggy function**, and can say out loud why a single call proves nothing
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] **0** network requests — nothing today left the machine
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] The three properties every object has, and which of them can change
- [ ] Why `y = y + 1` leaves `x` alone but `b.append(4)` does not leave `a` alone — without the word "mutable"
- [ ] The label model, explained to somebody who thinks a variable is a box
- [ ] The one-glance test for whether a line rebinds a name or mutates an object
- [ ] Why `0.1 + 0.2 != 0.3`, using one third in decimal as the analogy
- [ ] The two correct ways to represent money, and why a float is not one
- [ ] Why `+=` on a string cannot append, and two things immutability buys
- [ ] The two typing axes, and where Python sits on each
- [ ] The three questions that distinguish the four containers
- [ ] Why `x in a_list` slows down as the list grows and `x in a_set` does not
- [ ] The signal that an operation mutated rather than returned, and why the library chose it
- [ ] Three ways an alias is created that are not `b = a`
- [ ] Why `records.copy()` is a real copy and still not a backup
- [ ] Why a dictionary is fast, and why that forbids a list as a key
- [ ] Exactly when `[]` in `def f(x, acc=[])` is evaluated, and how many times
- [ ] Why the fix must test `is None` rather than falsiness
- [ ] Why `code is 200` passes every test and fails in production

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/objects.py` and `tests/test_objects.py` staged
- [ ] `notebooks/day-04-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-04-objects/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 4` passes
- [ ] `./m done 4` ran green and created the commit
