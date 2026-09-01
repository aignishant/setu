# Day 11 — CHECKLIST

**IDs covered:** `PY-11`, `PY-12` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 15, in [`parts/`](parts/)
**Kind:** `gate` — this is Phase 1's acceptance, so the last section is not optional.

> `./m done 11` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_textutils.py -v && ./m check
```

Expected: every test in the file passing — yesterday's plus today's ten — including the memory test
over a hundred thousand lines and the two laziness tests that are the only proof the docstrings are
not lying. Then a green gate.

---

## Setup

- [ ] Ran `uv run python -c "import setu.textutils as t; print(t.__file__)"` and got a path **before** writing anything
- [ ] Ran the four-fact setup block in the hub's §3 and can say what each of the four lines proved
- [ ] Ran the memory block in §3 and **wrote my own two numbers down** — they will not match the page
- [ ] Read `uv run ruff rule E731` and `uv run ruff rule B023` from the installed linter
- [ ] Confirmed `data/` is git-ignored **before** generating `data/slips_big.txt`
- [ ] Confirmed no new package was added today — Module 1 is the language before any library

---

## Section 1 — iterators

- [ ] Read [1.1 — iterable and iterator](parts/01-iterators/1.1-iterable-and-iterator.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — building the reader by hand](parts/01-iterators/1.2-writing-next-by-hand.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — exhaustion](parts/01-iterators/1.3-exhaustion.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `iter()` with a sentinel](parts/01-iterators/1.4-iter-with-a-sentinel.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `type(iter(a_list)).__name__` and got `list_iterator`, not `list`
- [ ] Confirmed `iter(a_list) is iter(a_list)` is `False` and `iter(a_reader) is a_reader` is `True`
- [ ] Took one item through one name and watched the position move for the other name too
- [ ] Called `next()` past the end and read the `StopIteration` traceback that carries **no message**
- [ ] Triggered `'list' object is not an iterator` and `'int' object is not iterable`, and can say which end of the pair each one means
- [ ] Built the closure reader with `nonlocal` and confirmed a second `make_reader(...)` starts again at the top
- [ ] Wrote `SheetReader` with `__iter__` and `__next__`, and looped it with `for`
- [ ] Deleted `__iter__` and read `'SheetReader' object is not iterable` **with `__next__` still present**
- [ ] Returned a list from `__iter__` and read `iter() returned non-iterator of type 'list'`
- [ ] **Put the three lines of `__next__` in the wrong order on purpose** and counted how many of the four slips came out
- [ ] Ran `len(list(box))` then `list(box)` and watched the second come back `[]`
- [ ] Read `object of type 'generator' has no len()` and can say why refusing is better than walking
- [ ] Rewrote a `while True` read-and-break as `iter(callable, sentinel)` and confirmed the sentinel is never yielded
- [ ] Used `iter(handle.read, "")` by mistake, saw one enormous block, and can say what the lambda was for

---

## Section 2 — generators

- [ ] Read [2.1 — `yield`, the function that pauses](parts/02-generators/2.1-yield-the-function-that-pauses.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — a list against a generator](parts/02-generators/2.2-a-list-against-a-generator.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — streaming a file](parts/02-generators/2.3-streaming-a-file.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `yield from` and the pipeline](parts/02-generators/2.4-yield-from-and-the-pipeline.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — when a generator is wrong](parts/02-generators/2.5-when-a-generator-is-wrong.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Called a generator function and confirmed **no line of its body ran** — the `print` before the loop stayed silent
- [ ] Watched `C: woke up after #0` print during the **second** `next()` call, not the first
- [ ] Put `return 1` above a `yield` and watched the function return a generator that yields nothing
- [ ] Put a `raise ValueError` at the top of a generator, called it, and confirmed **nothing raised**
- [ ] Split that generator into a validating wrapper plus a private generator, and confirmed the error now fires at the call
- [ ] Measured a million squares as a list and as a generator, and **wrote both peaks down**
- [ ] Printed `sys.getsizeof` on the list and on the generator, and can say why the generator's number never changes
- [ ] Reproduced the `reset_peak()` mistake and got a "lazy" number that was not lazy
- [ ] Built `data/slips_big.txt` and measured `read_text().splitlines()` against `for line in handle`
- [ ] Iterated a file and read a line back with `repr()`, seeing the `\n` still attached
- [ ] Slipped `.readlines()` into a streaming loop and watched the peak jump by three orders of magnitude
- [ ] Wrote a three-stage pipeline and confirmed `type(pipeline).__name__` is `generator` **before** consuming it
- [ ] Wrote a recursive flattener, left out the `isinstance` base case first, and read the `RecursionError`
- [ ] Triggered `RuntimeError: generator raised StopIteration` and can say which PEP made that happen
- [ ] Printed `gen.gi_frame.f_locals["handle"].closed` on a paused generator and got `False`
- [ ] Called `gen.close()` and confirmed `gen.gi_frame is None`
- [ ] Tried `len`, `[0]`, `[1:3]` and `reversed()` on a generator and read all four messages
- [ ] Ran `sorted(gen)` with `tracemalloc` and watched the memory saving disappear entirely
- [ ] Tried to `pickle.dumps` a generator and read `cannot pickle 'generator' object`

---

## Section 3 — lambda and map

- [ ] Read [3.1 — `lambda`, a function with no name](parts/03-lambda-and-map/3.1-lambda-a-function-with-no-name.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `map` and `filter` are lazy](parts/03-lambda-and-map/3.2-map-and-filter-are-lazy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — where a lambda hurts](parts/03-lambda-and-map/3.3-where-a-lambda-hurts.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — `reduce`, `any`, `all`](parts/03-lambda-and-map/3.4-reduce-any-and-all.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed `type(a_lambda) is type(a_def)` — there is no separate lambda type
- [ ] Printed `(lambda s: s).__name__` and got `<lambda>`
- [ ] Read a traceback with a `<lambda>` frame in it, and can say what that costs in a file with fifteen of them
- [ ] Triggered `SyntaxError: cannot assign to lambda` and read the caret span
- [ ] Built lambdas in a loop, watched them all use the last value, and fixed it with a default argument
- [ ] Ran `ruff check --select E731` on `tidy = lambda s: s.strip()` and read the `help:` line
- [ ] Printed a `map` object without `list()` and got an address
- [ ] Instrumented the mapped function with a `print` and confirmed **not one call** happened at `map(...)` time
- [ ] Walked a `map` twice and got the results and then `[]`
- [ ] Compared `map(str.strip, xs)`, the comprehension, and `map(lambda s: s.strip(), xs)` and can say which to delete
- [ ] Gave `map` two sources of different lengths and watched it truncate with no warning
- [ ] Compared `filter(None, xs)` against `filter(str.strip, xs)` on a whitespace-only string and can say why they differ
- [ ] Replaced a `key=lambda x: len(x)` with `key=len` and a `key=lambda r: r["qty"]` with `operator.itemgetter`
- [ ] Ran `reduce` over an empty sequence with no initial value and read the `TypeError`
- [ ] Named `reduce`'s lambda parameters backwards on a **subtraction** and watched the wrong answer
- [ ] Instrumented `any` and `all` and counted how many items each examined
- [ ] Confirmed `any([]) is False` and `all([]) is True`, and can say why both are correct
- [ ] Ran `any(...)` over a generator, then `list()`'d the same generator, and saw what was left

---

## Section 4 — the gate

- [ ] Read [4.1 — ten functions, fully tested](parts/04-the-gate/4.1-ten-functions-fully-tested.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the streaming reader](parts/04-the-gate/4.2-the-streaming-reader.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the function-count script and watched it report the three missing names **before** writing them
- [ ] Handed a `Path` to a handle-shaped generator and read `'WindowsPath' object is not iterable`
- [ ] Created a generator inside a `with` block, consumed it outside, and read `I/O operation on closed file.`
- [ ] Wrote `wrong_unique` with `yield from set(...)` and confirmed a **two-item** test would have passed it

---

## Build brief

- [ ] `iter_titles(handle)` written, with a comment saying which newline decision I made and why
- [ ] `unique_titles(titles)` written, with the docstring stating that its set grows with distinct titles
- [ ] `titles_matching(titles, predicate)` written, with the laziness sentence in its docstring
- [ ] All three annotated `-> Iterator[str]` and importable from `setu.textutils`
- [ ] `clean_titles`'s docstring now says **why** it returns a list rather than a reader
- [ ] Reread all seven of yesterday's functions and can say, for each, why it returns a container or a value
- [ ] `src/setu/textutils.py` has **ten public functions**, none of them created by splitting one behaviour into four
- [ ] Notebook traps reproduced in `notebooks/day-11-scratch.ipynb`, and **the notebook is not committed**
- [ ] `data/slips_big.txt` generated, and confirmed **not** staged by git

---

## The tests

- [ ] Every test in §5 written and **failing** before any implementation
- [ ] `test_iter_titles_skips_blank_and_whitespace_only_lines` — asserts the whole list, written by hand
- [ ] `test_iter_titles_yields_cleaned_titles` — would fail for a body that only calls `.strip()`
- [ ] `test_iter_titles_is_a_reader_not_a_list` — asserts the second walk is empty, with a comment saying why that is correct
- [ ] `test_iter_titles_peak_memory_does_not_grow_with_the_file` — a hundred thousand lines, asserted under a megabyte
- [ ] `test_unique_titles_keeps_input_order` — three items, duplicate in the middle
- [ ] `test_unique_titles_compares_by_key_not_by_string` — asserts **which** of the pair survives
- [ ] `test_unique_titles_is_lazy_in_its_input` — one `next()`, one recorded call
- [ ] `test_titles_matching_calls_the_predicate_once_per_title`
- [ ] `test_titles_matching_stops_calling_when_the_caller_stops` — `islice` two, assert the call count
- [ ] `test_pipeline_holds_one_title_at_a_time` — asserts `generator` before consuming
- [ ] **Break it, watch it go red, fix it** — `iter_titles` returns a list → the reader test **and** the memory test go red
- [ ] **Break it, watch it go red, fix it** — `unique_titles` becomes `yield from set(...)` → order and key tests go red
- [ ] **Break it, watch it go red, fix it** — `titles_matching` builds a list first → **only** the stop-early test goes red
- [ ] **Break it and watch it stay GREEN** — shrink the memory test to four lines with the list implementation in place, and say what that proves
- [ ] Every docstring promise in the three new functions has an assertion that goes red when it is broken

---

## The Phase 1 gate

- [ ] `src/setu/textutils.py` exists with ten public functions, each with a docstring and annotations
- [ ] `tests/test_textutils.py` passes in full, offline, with no `live` marker
- [ ] The module works on `data/slips_big.txt` — a file it never holds — through `iter_titles`
- [ ] I can say, for every one of the ten, whether it is eager or lazy **and why**
- [ ] `./m check` is green: `ruff check`, `ruff format --check`, `check_blocks.py`, pytest, `depth_check.py`
- [ ] `./m depth 11` reports no failures

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-11-iterators-and-generators/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m done 11` — the commit that closes Phase 1 and Module 1
