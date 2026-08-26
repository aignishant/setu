# Day 10 — CHECKLIST

**IDs covered:** `PY-10` · **Principles served:** 1, 2, 3, 4, 6, 7, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 10` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_textutils.py -v && ./m check
```

Expected: twelve passing tests (one parametrised four times), including the positional-call test that
is the only thing proving the bare `*` is still in the signature — and a green gate.

---

## Setup

- [ ] Created `src/setu/textutils.py` and `tests/test_textutils.py`
- [ ] Ran `uv run python -c "import setu; print(setu.__file__)"` and got a path **before** writing anything
- [ ] Ran the three-fact setup block in the hub's §3 and can say what each of the three lines proved
- [ ] Read `uv run ruff rule B006` and `uv run ruff rule B023` from the installed linter
- [ ] Confirmed no new package was added today — Module 1 is the language before any library

---

## Section 1 — the signature

- [ ] Read [1.1 — a function is a named promise](parts/01-the-signature/1.1-a-function-is-a-promise.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — positional and keyword arguments](parts/01-the-signature/1.2-positional-and-keyword.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — default values, and when they are worked out](parts/01-the-signature/1.3-defaults-and-when-they-run.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `*args` and `**kwargs`](parts/01-the-signature/1.4-args-and-kwargs.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — keyword-only and positional-only parameters](parts/01-the-signature/1.5-keyword-only-and-positional-only.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.6 — the signature is the contract](parts/01-the-signature/1.6-the-signature-is-the-contract.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote a function with no `return`, called it, and watched it hand back `None` without raising
- [ ] Stored a function without brackets and read the `TypeError` that named `'function'` as a type
- [ ] Called one function four ways — all positional, all keyword, mixed, and **wrongly ordered** — and confirmed the wrong one raised nothing
- [ ] Triggered `got multiple values for argument` and `positional argument follows keyword argument`, and can say why one is a `TypeError` and the other a `SyntaxError`
- [ ] **Reproduced the mutable default**: called `collect("a")`, `collect("b")`, `collect("c")` and watched the list grow
- [ ] Printed `func.__defaults__` before and after those three calls and watched the default itself change
- [ ] Fixed it with `None` and confirmed a caller's **empty list** survives `is None` and is destroyed by `if not into`
- [ ] Confirmed `@dataclass` raises `ValueError` on a mutable default where a plain `def` does not
- [ ] Printed `type(args).__name__` and `type(kwargs).__name__` and got `tuple` and `dict`
- [ ] Passed a list to a `*args` function **without** spreading it, and read the error that named `sum` rather than the call
- [ ] Watched `**kwargs` swallow a mistyped keyword with no error at all
- [ ] Wrote a forwarding wrapper, forgot the `return` once on purpose, and watched it hand back `None`
- [ ] Added a bare `*` and read `takes 1 positional argument but 2 were given` on a two-parameter function
- [ ] Added a `/` and read `got some positional-only arguments passed as keyword arguments`
- [ ] Printed `inspect.signature` and `__annotations__` on your own function
- [ ] Passed a number into a `raw: str` parameter and watched Python ignore the annotation completely

---

## Section 2 — scope

- [ ] Read [2.1 — LEGB](parts/02-scope/2.1-legb-where-a-name-is-found.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `UnboundLocalError`](parts/02-scope/2.2-unboundlocalerror.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `global` and `nonlocal`](parts/02-scope/2.3-global-and-nonlocal.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — closures and late binding](parts/02-scope/2.4-closures-and-late-binding.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote one name at all four levels and printed what each scope saw
- [ ] Confirmed the module-level value was **unchanged** after both functions ran
- [ ] Shadowed a builtin — `list = [1, 2]` then `list("abc")` — and read `'list' object is not callable`
- [ ] **Printed `func.__code__.co_varnames` before calling the function**, and can say what that proves about when the decision was made
- [ ] Reproduced `UnboundLocalError` with `x += 1` and with an assignment inside an `if` that never ran
- [ ] Reproduced it with `import json` at the bottom of a function that uses `json` at the top
- [ ] Wrote the same counter three ways — parameter, local, `global` — and can say which two are testable
- [ ] Called a `global` counter three times and watched three identical calls give three different answers
- [ ] Triggered `SyntaxError: no binding for nonlocal` and `SyntaxError: name 'x' is used prior to global declaration`
- [ ] Built two independent counters with `make_counter` and confirmed they do not interfere
- [ ] **Built three functions in a loop and watched all three return the last value**
- [ ] Printed `co_freevars` on the broken version (`('i',)`) and the fixed one (`()`)
- [ ] Read `late[0].__closure__[0].cell_contents` and can explain it as the whiteboard
- [ ] Ran `ruff check --select B023` on the broken version and saw it caught

---

## Section 3 — the module

- [ ] Read [3.1 — from notebook to module](parts/03-the-module/3.1-from-notebook-to-module.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — designing `clean_title()`](parts/03-the-module/3.2-designing-clean-title.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — pure functions and the seam](parts/03-the-module/3.3-pure-functions-and-the-seam.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Named all four things a function gains when it graduates out of a notebook
- [ ] Ran the notebook with "restart and run all" and confirmed it still works from a cold start
- [ ] Answered [3.2](parts/03-the-module/3.2-designing-clean-title.md)'s four design questions **in writing** before writing any body
- [ ] Can name the two real records that `strip_bracketed_year=True` would wrongly merge
- [ ] Can say why `clean_title` does not lowercase, and which function does
- [ ] Wrote a pure function and its one-line test with no fixture, no file and no clock
- [ ] Wrote `summarise_years` taking `today` as a parameter, and can say what a default of `date.today()` would freeze

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/textutils.py` from the skeleton in the hub's §4
- [ ] Implemented `clean_title` — four steps, in an order you commented and can defend
- [ ] Implemented `clean_titles` — one comprehension, **no filter**, same length guaranteed
- [ ] Implemented `title_key` — `casefold`, not `lower`
- [ ] Implemented `same_title` — one line, going through `title_key`
- [ ] Implemented `count_titles` — takes text, not a path
- [ ] Implemented `summarise_years` — `today` as a keyword parameter with **no** default
- [ ] Implemented `make_prefixer` — a factory, and built several in a loop to check they are independent
- [ ] Annotated `make_prefixer`'s return type and can say why it matters more there than elsewhere
- [ ] Reviewed `src/setu/text.py` and `src/setu/pipeline.py` against [3.2](parts/03-the-module/3.2-designing-clean-title.md)'s four questions and fixed what failed
- [ ] Ran the Day 7 and Day 9 test suites **before and after** that review and confirmed both stayed green

---

## Tests — every one must be able to go RED

- [ ] Created `tests/test_textutils.py` from the hub's §5
- [ ] Ran the whole file and watched **every** test fail before implementing anything
- [ ] `test_clean_title_collapses_trims_and_drops_one_dot` — expected value written out in full
- [ ] `test_clean_title_keeps_the_year_by_default` — both directions asserted
- [ ] `test_clean_title_options_cannot_be_passed_positionally` — asserts on the **message**
- [ ] `test_clean_titles_preserves_length_and_order` — length asserted **first**, as its own assertion
- [ ] `test_title_key_uses_casefold_not_lower` — the German sharp s
- [ ] `test_same_title_goes_through_the_key` — includes a pair that must **not** match
- [ ] `test_count_titles_ignores_blank_lines` — parametrised four ways, no file opened
- [ ] `test_summarise_years_is_fixed_by_its_arguments` — two fixed dates
- [ ] `test_prefixers_built_in_a_loop_are_independent` — the late-binding guard

**Break it, watch it go red, fix it:**

- [ ] Removed the bare `*` → the positional test **passed**, and can say why a green test was the failure
- [ ] Changed `casefold()` to `lower()` → the sharp-s test went red. Restored it
- [ ] Added a filter inside `clean_titles` → both the length and the value test went red, and can say which one diagnosed it faster. Restored it
- [ ] **Gave `summarise_years` a default of `date.today()` → every test still passed.** Can say what happens to a process running since before midnight, before restoring it

---

## Budget

- [ ] Zero LLM calls today
- [ ] Zero network requests today
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `./m check` is green
- [ ] `notebooks/day-10-scratch.ipynb` is **not** committed (Principle 6)
- [ ] `./m done 10` ran and committed
- [ ] Recorded the completion commit in [`LESSON.md`](LESSON.md)'s frontmatter
