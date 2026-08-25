# Day 5 — CHECKLIST

**IDs covered:** `PY-03`, `PY-04` · **Principles served:** 1, 2, 3, 6, 7, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 5` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_conditions.py -v && ./m check
```

Expected: seven passing tests — including the parametrised one that runs six times, once per falsy
value — and a green gate.

---

## Section 1 — operators (`PY-03`)

- [ ] Read [1.1 — an operator is a method call](parts/01-operators/1.1-an-operator-is-a-method-call.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the two divisions](parts/01-operators/1.2-the-two-divisions.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — comparison and chaining](parts/01-operators/1.3-comparison-and-chaining.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `==` is overloadable, `is` is not](parts/01-operators/1.4-equals-is-overloadable-is-is-not.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — bitwise and the mask](parts/01-operators/1.5-bitwise-and-the-mask.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — precedence and associativity](parts/01-operators/1.6-precedence-and-associativity.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Called `int.__add__(1, "two")` directly and saw `NotImplemented` rather than an exception
- [ ] Wrote a class with `__add__` only, watched `1 + obj` raise, added `__radd__`, watched it pass
- [ ] Made `sum()` work on a list of your own objects — and can say which dunder made it possible
- [ ] Printed the four sign combinations of `//` and `%` and confirmed the identity holds on all four
- [ ] Found the negative input where `x // y` and `int(x / y)` disagree
- [ ] Ran `-(-n // k)` and `math.ceil(n / k)` on the same numbers and can say why one is exact
- [ ] Used `week[offset % 7]` with a negative offset and got the day *before*, not an error
- [ ] **Counted the calls:** chained comparison once, the expanded `and` form twice
- [ ] Watched `sorted([3, 1, None])` raise, and fixed it with a key that gives `None` a position
- [ ] Confirmed `"Zebra" < "apple"` is `True` and can say why
- [ ] Sorted a list of tuples and got a two-key sort without writing a comparator
- [ ] Wrote a class whose `__eq__` returns `True` for everything, and confirmed `is None` was immune
- [ ] Built a `MISSING = object()` sentinel and distinguished "omitted" from "passed as `None`"
- [ ] Saw `@dataclass` generate `__eq__`, and used `field(compare=False)` to choose the identity
- [ ] Confirmed `{1,2} & {2,3}` and `5 & 3` use two different functions behind one symbol
- [ ] Wrote a `Mask` class whose `__bool__` raises, and reproduced the "ambiguous" message by hand
- [ ] Saw `2023 == 2023 & True` return `False` and worked out the grouping before being told
- [ ] Used `ast.dump` to settle a grouping question instead of guessing
- [ ] Built the eight-row admin/owner/public truth table and **found the two rows that differ**
- [ ] Confirmed `2 ** 3 ** 2` is `512` and `-2 ** 2` is `-4`

## Section 2 — conditionals (`PY-04`)

- [ ] Read [2.1 — `if`/`elif`/`else` and the indent](parts/02-conditionals/2.1-if-elif-else-and-the-indent.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — truthiness](parts/02-conditionals/2.2-truthiness.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — why `if df:` raises](parts/02-conditionals/2.3-if-df-raises.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `and`/`or` return an operand](parts/02-conditionals/2.4-and-or-return-operands.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — the conditional expression and the guard clause](parts/02-conditionals/2.5-the-conditional-expression.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the `elif` grader against the stacked-`if` grader and saw a 95 come back as a `C`
- [ ] Moved a `return` one level in, watched a function stop checking every row, moved it back
- [ ] Ordered threshold branches loosest-first and confirmed the later branches were unreachable
- [ ] Triggered a `TabError` on purpose, then configured the editor so it cannot happen again
- [ ] Confirmed an instance of your own class with no `__bool__`/`__len__` is truthy
- [ ] Wrote a class where `__bool__` and `__len__` disagree, and confirmed which one wins
- [ ] Printed `bool()` for the whole falsy set, and for `"0"`, `" "`, `[0]`, `nan` and a class object
- [ ] Wrote a `parse_flag` that is not fooled by `"false"`
- [ ] Reproduced the "truth value is ambiguous" error from a `__bool__` you wrote yourself
- [ ] Confirmed `len()` works on that same object, and can say why one question is answerable
- [ ] Saw the identical mistake on a scalar `0.0` produce **no error at all**
- [ ] Printed the *type* of `0 and 5`, `3 and 5`, `"" or None or 0` and `not 0`
- [ ] Watched short-circuiting skip an expensive call, then reversed the operands and watched it run
- [ ] Reversed a `user is not None and user.is_admin` guard and got the `AttributeError` it prevents
- [ ] Rewrote a nine-line assignment as one conditional expression
- [ ] Confirmed only one branch of a conditional expression is evaluated, using a printing function
- [ ] Wrote `sum(rows) / len(rows) if rows else 0.0` on an empty list without a `ZeroDivisionError`
- [ ] Inverted a validation pyramid into guard clauses and confirmed identical results for all inputs
- [ ] Produced an `UnboundLocalError` from a branch that forgot to assign

## Section 3 — where an operator meets a condition

- [ ] Read [3.1 — the `or`-default and the falsy zero](parts/03-the-or-trap/3.1-the-or-default-and-falsy-zero.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `in` is an operator](parts/03-the-or-trap/3.2-in-is-an-operator.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Reproduced the retries incident:** `{"retries": 0}` with `or 3`, and watched it return `3`
- [ ] Confirmed `x or True` can never return `False`, for any input
- [ ] Confirmed `config.get("timeout", 30)` returns `None` when the stored value is `None`
- [ ] Wrote the get-then-`is None` two-step and confirmed it handles all three cases
- [ ] Found one place where `or` as a default is genuinely correct, and can say why
- [ ] Printed a `__contains__` call and confirmed `in` dispatches on the **right** operand
- [ ] Watched the `__iter__` fallback run when there was no `__contains__`
- [ ] Confirmed `1 in {"a": 1}` is `False` and `"ell" in "hello"` is `True`
- [ ] Confirmed `999_999 in range(1_000_000)` is instant
- [ ] **Timed dedup at three sizes with a list and with a set, and watched the RATIO grow**
- [ ] Consumed a generator with one `in` test and got a wrong answer from the second
- [ ] Turned a working `x in a_list` into `TypeError: unhashable type` by switching to a set

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/conditions.py`
- [ ] Implemented `coalesce` — and it is **not** `or`
- [ ] Implemented `config_value` — two questions, in order
- [ ] Implemented `parse_flag` — with the **written comment** deciding what unrecognised input does
- [ ] Implemented `is_faster_membership` — and can defend the reasoning in its comment
- [ ] Implemented `dedup_preserving_order` — with a `seen` that is not a list
- [ ] Reproduced the precedence truth table in `notebooks/day-05-scratch.ipynb`
- [ ] Reproduced the `or`-default incident in the same notebook
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/` (Principle 6)
- [ ] `uv run ruff check src/ tests/` passes, including `E711` and `E712`

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_conditions.py -v` **before** implementing and watched every test fail
- [ ] Implemented the parametrised `test_coalesce_keeps_every_falsy_value` — **both halves**
- [ ] Implemented `test_config_value_distinguishes_missing_key_from_stored_none`
- [ ] Implemented the parametrised `test_parse_flag_is_not_fooled_by_truthiness`
- [ ] Implemented `test_is_faster_membership_names_the_right_containers` — with the generator comment
- [ ] Implemented `test_dedup_preserves_order_and_is_not_quadratic`
- [ ] Implemented `test_chained_comparison_evaluates_the_middle_once`
- [ ] Implemented `test_precedence_of_and_over_or_is_not_what_it_reads_like` — including the row where the two groupings differ
- [ ] **Break it, watch it go red, fix it —** changed `coalesce` to use `or`, saw **six** parametrised failures, read all six. Restored it.
- [ ] **Break it, watch it go red, fix it —** changed `config_value` to a plain `dict.get(key, default)`, saw only the stored-`None` case go red. Restored it.
- [ ] **Break it, watch it go red, fix it —** changed `parse_flag` to `return bool(raw)`, saw three failures for three different reasons. Restored it.
- [ ] **The one that matters most —** changed `dedup_preserving_order`'s `seen` to a list, watched the **order test still pass** and only the ratio assertion go red, and can say why a correctness test cannot see a complexity bug
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] **0** network requests — nothing today left the machine
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] Every step Python takes to evaluate `a + b`, including what happens when the left operand declines
- [ ] Why a class with `__add__` but no `__radd__` breaks `sum()`
- [ ] The identity that defines `%`, and why `-7 % 3` is `2`
- [ ] One concrete bug that `int(x / y)` causes and `x // y` does not
- [ ] What `a < b < c` is equivalent to, and the one thing that equivalence does not preserve
- [ ] Why `sorted([3, 1, None])` raises while `1 == "1"` does not
- [ ] Why `x is None` is trustworthy and `x == None` is not, in terms of which code runs
- [ ] When `None` cannot be used as a default, and what you use instead
- [ ] Why a pandas filter needs `&` — one sentence about `and`, one about overloading
- [ ] Why every operand of a mask needs its own parentheses
- [ ] The four precedence neighbours that cause real bugs, and the bug each one causes
- [ ] Why a fixture full of zeros and ones cannot catch a precedence bug
- [ ] What `elif` does that a second `if` does not, with an input where they disagree
- [ ] Why indentation in Python is grammar, and one class of bug that fact makes impossible
- [ ] The three rules `bool(x)` follows, in order
- [ ] The three questions `if x:` collapses into one, and the safe test for each
- [ ] The four things `if df:` could have meant, and why pandas raises instead of choosing
- [ ] What `a and b` and `a or b` return, in terms of operands rather than booleans
- [ ] Two reasons operand order matters — one about safety, one about cost
- [ ] Why the `else` in a conditional expression cannot be omitted
- [ ] The guard-clause inversion, and two bugs it makes impossible
- [ ] Exactly what `value or default` tests, and the six values in the gap
- [ ] The right default form for a dict, for a parameter, and for JSON with a possible null
- [ ] Why `if item not in seen:` is instant for one container and quadratic for another

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/conditions.py` and `tests/test_conditions.py` staged
- [ ] `notebooks/day-05-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-05-operators-and-conditionals/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 5` passes
- [ ] `./m done 5` ran green and created the commit
