# Day 19 — CHECKLIST · PHASE 2 GATE

**IDs covered:** `PY-23`, `PY-24` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 10, 11, 14, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 26, in [`parts/`](parts/)

> `./m done 19` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **This is the phase gate.** The twelve criteria in the last section are the point of the day; everything
> above them is what makes them demonstrable.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_models.py tests/test_fetcher.py -v && ./m check
```

Expected: eight tests in `test_models.py` and six in `test_fetcher.py` passing, then a green gate.

---

## Setup

- [ ] `uv add pydantic==2.13.5` and `uv add httpx==0.28.1`, both with `==`
- [ ] Confirmed `uv.lock` changed and committed it (Principle 4)
- [ ] Logged the `2.13.4 → 2.13.5` patch drift in `docs/CHANGELOG_PLAN_DS.md`
- [ ] Created `src/setu/models.py`, `src/setu/fetcher.py` and both test files
- [ ] Ran `uv run python -c "from setu.errors import RateLimited, SetuError; print('errors ok')"` first
- [ ] Ran the twelve-fact setup block and can say what each of the twelve lines proved
- [ ] Can say why lines 3 and 4 are "the whole of the morning"
- [ ] Can say why lines 8 and 9 are "the whole of the afternoon"
- [ ] Read `uv run ruff rule B006` and `uv run ruff rule RUF006` from the installed linter

---

## Section 1 — type hints

- [ ] Read [1.1 — a hint is a note](parts/01-type-hints/1.1-a-hint-is-a-note.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the vocabulary](parts/01-type-hints/1.2-the-vocabulary.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `X | None`](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — the type checker](parts/01-type-hints/1.4-the-type-checker.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Passed a string to a function annotated `int` and watched it work
- [ ] Printed `__annotations__` and `inspect.signature` for one function
- [ ] Wrote an annotation naming an undefined class and read the `NameError`
- [ ] Wrote one signature using `Iterable`, `Mapping`, `Any`, `| None` and a `tuple[...]` return
- [ ] Confirmed `Optional[int] == (int | None)`
- [ ] Passed a generator to a parameter annotated `list` and saw it work at run time
- [ ] Wrote `-> dict` on a function with `return None` and ran a checker over it
- [ ] Compared `if not value:` with `if value is None:` on an empty set
- [ ] Wrote the guard clause and confirmed the checker then accepted the subscript
- [ ] Ran `mypy` with and without `--strict` on the same file and counted the findings
- [ ] Silenced one finding with `# type: ignore[code]` and one with a bare `# type: ignore`

---

## Section 2 — dataclasses

- [ ] Read [2.1 — what `@dataclass` writes](parts/02-dataclasses/2.1-what-dataclass-writes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `default_factory`](parts/02-dataclasses/2.2-default-factory.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `frozen`, `slots`, `kw_only`](parts/02-dataclasses/2.3-frozen-slots-kw-only.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `__post_init__`](parts/02-dataclasses/2.4-post-init.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — not a validator](parts/02-dataclasses/2.5-not-a-validator.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Listed the methods `@dataclass` added to a class with `vars()`
- [ ] Left the colon off a field and found it missing from `fields()` and the signature
- [ ] Put a default before a non-default and read the `TypeError`
- [ ] Tried to put a dataclass instance in a `set`
- [ ] Wrote `tags: list[str] = []` and read the refusal
- [ ] Used `field(default_factory=list)` and confirmed two instances have separate lists
- [ ] Wrote `default_factory=list()` and read the `TypeError`
- [ ] Made a factory return a module-level list and watched it be shared anyway
- [ ] Used `field(repr=False)` on a credential and confirmed it is absent from the `repr`
- [ ] Confirmed `compare=False` affects `__eq__` and **not** the `repr`
- [ ] Put a frozen dataclass in a set, then tried to assign to a field
- [ ] Appended to a list inside a `frozen=True` dataclass and then tried to hash it
- [ ] Measured `sys.getsizeof` for a plain and a slotted instance
- [ ] Misspelt an attribute on a slotted instance and read the `AttributeError`
- [ ] Confirmed `slots=True` under an unslotted parent gives no typo protection
- [ ] Used `kw_only=True` and read the positional `TypeError`
- [ ] Wrote validation and a computed field in `__post_init__` with `field(init=False)`
- [ ] Swapped the validation and the computation and read the `ZeroDivisionError`
- [ ] Wrote a subclass `__post_init__` without `super()` and watched the parent check vanish
- [ ] Built a dataclass from a dictionary of strings and watched the arithmetic go wrong

---

## Section 3 — Pydantic v2

- [ ] Read [3.1 — the model that refuses](parts/03-pydantic/3.1-the-model-that-refuses.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — `ValidationError`](parts/03-pydantic/3.2-validationerror.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — coercion and `strict`](parts/03-pydantic/3.3-coercion-and-strict.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — `model_dump` and the boundary](parts/03-pydantic/3.4-model-dump-and-the-boundary.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.5 — `TriageResult`](parts/03-pydantic/3.5-triage-result.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built the same record as a dataclass and as a `BaseModel` and fed both a string
- [ ] Read a three-problem `ValidationError` and counted the entries
- [ ] Printed `loc`, `type`, `msg` and `input` for one entry
- [ ] Found a nested `loc` of `('to', 'postcode')` from a nested model
- [ ] Joined a `loc` tuple for display and compared it with `str(loc)`
- [ ] Confirmed `500.0` is accepted for an `int` and `500.5` is not
- [ ] Read the whole set of values a `bool` field accepts
- [ ] Confirmed a number is **not** coerced to a `str`
- [ ] Turned on `strict=True` and watched it reject an environment variable
- [ ] Handed `model_dump()` to `json.dumps` with a `datetime` field
- [ ] Compared `model_dump()`, `model_dump(mode="json")` and `model_dump_json()`
- [ ] Asserted a round trip: `model_validate_json(model_dump_json()) == original`
- [ ] Kept a secret out of a dump with `Field(exclude=True)` **and** with `SecretStr`
- [ ] Called `model_json_schema()` and found every constraint in it
- [ ] Sent a model an invented label, a confidence of 95, an empty reason and a renamed field

---

## Section 4 — concurrency

- [ ] Read [4.1 — waiting is not working](parts/04-concurrency/4.1-waiting-is-not-working.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the GIL](parts/04-concurrency/4.2-the-gil.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — threads](parts/04-concurrency/4.3-threads.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — processes](parts/04-concurrency/4.4-processes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — `asyncio`](parts/04-concurrency/4.5-asyncio-one-thread.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.6 — `async def`, `await`](parts/04-concurrency/4.6-async-await.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.7 — `asyncio.gather`](parts/04-concurrency/4.7-gather-and-twenty-fetches.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.8 — timeouts and `TaskGroup`](parts/04-concurrency/4.8-timeouts-and-taskgroup.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.9 — choosing](parts/04-concurrency/4.9-choosing.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Timed eight sleeps and eight loops with and without a thread pool
- [ ] Confirmed the arithmetic version got **slower** with threads
- [ ] Measured `process_time / perf_counter` for a waiting and a working function
- [ ] Compared a Python loop with `hashlib` under four threads and explained the difference
- [ ] Printed `sys.getswitchinterval()` and then lowered it and watched threads slow down
- [ ] Ran the eight-thread ledger with a gap and lost thousands of updates
- [ ] Ran the naive `COUNT += 1` version and watched it come out **right**
- [ ] Added a lock and confirmed the count is exact
- [ ] Held a lock across a `sleep` and watched the pool serialise
- [ ] Started and joined in one loop and measured the sequential time
- [ ] Raised in a raw `threading.Thread` and checked the exit code
- [ ] Ran the same arithmetic in threads and in processes and compared
- [ ] Sent a large list to a process pool and watched it be slower than threads
- [ ] Confirmed a module-level list in the parent is invisible to the workers
- [ ] Passed a lambda to a process pool and read the pickling error
- [ ] Removed the `if __name__ == "__main__":` guard and read what happened
- [ ] Ran `asyncio.gather` over three sleeps and confirmed the elapsed time is the longest one
- [ ] Confirmed `gather` returns results in **argument** order
- [ ] Put `time.sleep` in a coroutine and watched ten tasks take ten times as long
- [ ] Called `asyncio.run` inside a running loop and read the `RuntimeError`
- [ ] Called an `async def` without `await` and checked its type and its truthiness
- [ ] Wrote `await` at module level and read the `SyntaxError`
- [ ] Used `with` where `async with` was needed
- [ ] Ran the twenty-fetch benchmark against the local server and recorded the speed-up
- [ ] Compared one shared `AsyncClient` with one per request
- [ ] Ran `gather` without `return_exceptions` and lost the good results
- [ ] Awaited a coroutine twice and read the `RuntimeError`
- [ ] Timed out a slow coroutine with `asyncio.timeout` and with `wait_for`
- [ ] Watched a `TaskGroup` cancel its siblings, and `gather` not
- [ ] Caught a `TaskGroup` failure with `except ValueError:` and read the tree
- [ ] Swallowed a `CancelledError` with a bare `except:` and watched the task ignore it
- [ ] Confirmed a CPU-bound coroutine cannot be timed out
- [ ] Compared cleanup with and without a `finally` on a cancelled task
- [ ] Replaced a Python loop with `sum()` and measured the difference

---

## Build

- [ ] `src/setu/models.py` defines `Label` as a `StrEnum` with wire-format values
- [ ] `TriageResult` is `frozen=True` and `extra="forbid"`, with a comment saying what each protects
- [ ] `confidence` has an inclusive 0..1 bound, and the choice of `ge`/`le` is explained
- [ ] `reason` has **both** a `min_length` and a `max_length`
- [ ] `tags` uses `default_factory`
- [ ] `schema_for_prompt()` returns `model_json_schema()` and names the three jobs in a comment
- [ ] `src/setu/fetcher.py`'s `Budget` records requests, failures and the peak in flight
- [ ] `Budget.start` has a comment saying why no lock is needed
- [ ] `fetch_all` takes `get` as its **first** argument, injected
- [ ] `limit` and `timeout` are keyword-only
- [ ] The semaphore is created **inside** `fetch_all`
- [ ] `asyncio.timeout` is **inside** the semaphore
- [ ] `budget.finish(ok)` is in a `finally`
- [ ] `gather` is called with `return_exceptions=True`
- [ ] `fetch_all` catches **nothing** and does **not** retry, and the docstring says why
- [ ] **Wrote down, in two sentences, what `limit` defaults to and why** (plan Part 2.1)
- [ ] Added `models` and `fetcher` to `LAYERS` in `src/setu/layout.py`, and `tests/test_layout.py` passes
- [ ] Reproduced all ten traps in `notebooks/day-19-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)
- [ ] Wrote the Phase 2 decision record in `docs/adr/` (Principle 10)

---

## Tests

- [ ] Both test files exist and every test failed before any implementation
- [ ] Every test runs offline and the suite makes **zero** requests
- [ ] `test_a_good_reply_parses` asserts the label equals both `Label.BUG` and `"bug"`
- [ ] `test_an_invented_label_is_rejected` asserts the **code**, not the message
- [ ] `test_a_confidence_of_95_is_rejected` passes
- [ ] `test_an_empty_reason_is_rejected` passes
- [ ] `test_a_renamed_field_is_rejected` passes
- [ ] `test_the_result_cannot_be_edited` passes
- [ ] `test_every_constraint_reaches_the_schema` passes
- [ ] `test_it_round_trips` passes
- [ ] `test_the_fetcher_returns_one_result_per_url` uses reversed durations to prove **argument** order
- [ ] `test_the_fetcher_never_exceeds_its_limit` asserts on the **counter**, not the clock
- [ ] `test_a_failure_comes_back_as_a_value` asserts `retry_after` survived
- [ ] `test_a_slow_url_times_out_and_the_others_survive` passes
- [ ] `test_the_budget_is_accurate_after_failures` passes
- [ ] `test_the_fetcher_makes_no_real_requests` passes
- [ ] **Break it, watch it go red, fix it** — `label: str` → the invented-label and schema tests go red
- [ ] **Break it, watch it go red, fix it** — drop `ge`/`le` → only the confidence test goes red
- [ ] **Break it, watch it go red, fix it** — drop `min_length` → only the empty-reason test goes red
- [ ] **Break it, watch it go red, fix it** — `extra="ignore"` → only the renamed-field test goes red
- [ ] **Break it, watch it go red, fix it** — drop `frozen=True` → only the edit test goes red
- [ ] **Break it, watch it go red, fix it** — timeout **outside** the semaphore → the limit test still
      passes, and under load every queued task times out before starting
- [ ] **Break it, watch it go red, fix it** — remove the `finally` → only the budget test goes red
- [ ] **Break it, watch it go red, fix it** — drop `return_exceptions=True` → two tests go red
- [ ] **Break it, watch it go red, fix it** — replace `gather` with a loop of awaits → only the limit test
      can see it
- [ ] **Break it and watch every test stay GREEN** — remove the semaphore, **and** delete
      `test_the_fetcher_never_exceeds_its_limit`. Every remaining test passes, and the first real run
      fires two hundred requests at a provider that allows tens per minute. Restore the test, watch it go
      red, and say what it was protecting (Principle 5).

---

## THE PHASE 2 GATE

> The twelve criteria from [5.1](parts/05-the-gate/5.1-the-gate-as-a-list.md). Each one is demonstrated by
> a test that has been made to go red at least once. **A criterion that cannot be demonstrated is a gap in
> the day that owns it** — go back to that day rather than writing something quickly here (Principle 1).

- [ ] 1 — `Paper` constructs, validates, and refuses bad input ([Day 12](../day-12-classes/parts/03-the-paper-object/3.2-validation-in-init.md))
- [ ] 2 — A base class with at least two subclasses, used **without** `isinstance` ([Day 13](../day-13-inheritance-and-abstraction/parts/04-abstraction/4.2-the-loader-family.md))
- [ ] 3 — `__repr__`, `__eq__` and `__hash__` behave: two equal papers dedupe in a `set` ([Day 15](../day-15-constructors-and-dunders/parts/03-the-dunders/3.4-hash-and-the-broken-set.md))
- [ ] 4 — An alternative constructor round-trips ([Day 15](../day-15-constructors-and-dunders/parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md))
- [ ] 5 — One project base exception; every type is a subclass of it ([Day 18](../day-18-exceptions/parts/03-your-own/3.1-one-base-class-per-project.md))
- [ ] 6 — `RateLimited` carries `retry_after` **and** survives a pickle round trip ([Day 18](../day-18-exceptions/parts/03-your-own/3.2-an-exception-that-carries-data.md))
- [ ] 7 — A boundary that leaks no dependency's exception, for both a bad file and a missing one ([Day 18](../day-18-exceptions/parts/03-your-own/3.4-translate-at-the-boundary.md))
- [ ] 8 — The fetcher's recorded peak equals its limit ([5.2](parts/05-the-gate/5.2-the-async-fetcher.md))
- [ ] 9 — A slow URL times out and the others survive ([4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md))
- [ ] 10 — Failures come back as values, not as a raise ([4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md))
- [ ] 11 — The run reports what it spent (Principle 5)
- [ ] 12 — Every one of the above has a test, and each has been broken on purpose once (Principle 7)

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today — the benchmark used `127.0.0.1`, the tests used a fake `get`
- [ ] **2** new packages, both pinned with `==`, both in `uv.lock`
- [ ] **0** secrets in any `repr`, message or dump
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-19-typing-dataclasses-and-concurrency/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 19` reports no failures
- [ ] `./m tracker` regenerated, and `docs/TRACKER.md` shows Phase 2 at 8/8
- [ ] `./m done 19`
