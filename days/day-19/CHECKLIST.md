# Day 19 — CHECKLIST · **PHASE 2 GATE**

**IDs covered:** PY-23, PY-24 · **Principles served:** 1, 4, 5, 7

## Demo command

```bash
uv run python days/day-19/lab/typing_demo.py
uv run python days/day-19/lab/concurrency.py
uv run python -m pytest -q
```

Expected: the typing report, the four measured concurrency comparisons, then the **whole** suite green.

## Setup

- [ ] `./m start 19` and `./m scaffold 19` run
- [ ] `uv add "pydantic==<your pin>"` — appears in `pyproject.toml` and `uv.lock`
- [ ] Version pinned from **your** Day-1 verify run; any drift logged
- [ ] Files created: both lab files, `src/setu/schema.py`, `tests/test_schema.py`

## PY-23 — typing and dataclasses

- [ ] Confirmed `double("ab")` returns `"abab"` with **no error**
- [ ] Read `__annotations__` on a real function
- [ ] Compared a hand-written class with `@dataclass`
- [ ] Used `field(default_factory=list)` and confirmed instances do not share it
- [ ] Tried `tags: list[str] = []` in a dataclass and saw Python **refuse it**
- [ ] Used `frozen=True`, `slots=True`, `order=True` and can say what each buys
- [ ] Used a `TypedDict` and know it has **no** runtime validation

## PY-23 — Pydantic v2

- [ ] Built a model with `Field(min_length=...)`, `Field(ge=..., le=...)`, and `Literal`
- [ ] Saw `year="2017"` **coerced** to `int`
- [ ] Wrote a `@field_validator` with `@classmethod` **underneath** it
- [ ] Saw `exc.errors()` report **every** failure at once
- [ ] Used `model_dump`, `model_dump_json`, `model_validate` — the **v2** names
- [ ] Printed `model_json_schema()` and know which later day consumes it
- [ ] Checked `pydantic.VERSION` before trusting any online example

## PY-24 — concurrency

- [ ] Ran all four comparisons
- [ ] Recorded **your** numbers in `days/day-19/lab/RESULTS.md`:
  - sequential I/O ______s · threaded I/O ______s
  - sequential CPU ______s · threaded CPU ______s · process CPU ______s
  - asyncio gather ______s · await-in-a-loop ______s
- [ ] Confirmed threads help I/O and **do not** help CPU
- [ ] Confirmed processes help CPU, and can name the two costs
- [ ] Saw `await` in a loop run **sequentially**
- [ ] Can state the one-sentence rule without hesitating

## Build brief

- [ ] `src/setu/schema.py` created, layer 1
- [ ] `Paper` — **TODO(me)**: frozen, `extra="forbid"`, all constraints, title validator, `age`, `__str__`
- [ ] Did **not** hand-write `__init__`, `__eq__` or `__repr__`
- [ ] `Chunk` — **TODO(me)**, with a `model_validator` for the span
- [ ] `SearchResult` — **TODO(me)**, nested `Chunk`, bounded score
- [ ] `paper_json_schema()` — **TODO(me)**
- [ ] `papers.py` keeps only non-validation behaviour; `Paper` now lives in `schema.py`
- [ ] Layering test still green after the move

## Tests that must be able to fail

- [ ] `test_title_is_normalised` — green
- [ ] `test_year_is_coerced_from_a_string` — green
- [ ] `test_invalid_input_is_rejected` — five green cases
- [ ] `test_a_typo_is_rejected_not_ignored` — green ← **today's real assessment**
- [ ] **Removed `extra="forbid"`, read what the test says, restored it** ← do not skip
- [ ] `test_all_errors_are_reported_at_once` — green
- [ ] `test_model_is_frozen_and_hashable` — green
- [ ] `test_authors_default_is_not_shared` — green
- [ ] `test_round_trip_through_json` — green
- [ ] `test_json_schema_has_the_fields_an_llm_needs` — green
- [ ] `test_chunk_rejects_a_backwards_span` — green
- [ ] `test_nested_models_validate_recursively` — green
- [ ] `test_score_is_bounded` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are annotations actually for, given nothing enforces them?
- [ ] What does `@dataclass` generate, and which two earlier days did you write by hand first?
- [ ] Why does Pydantic default to *ignoring* unknown keys, and why do you override that?
- [ ] Name three v1 method names and their v2 replacements
- [ ] Why does the JSON schema matter on Day 175, Day 210 and Day 217?
- [ ] Why do threads not speed up arithmetic?
- [ ] Why is `for x in xs: await f(x)` sequential, and what makes it concurrent?

## PHASE 2 GATE

- [ ] `Paper` is a frozen, `extra="forbid"` Pydantic model with a working JSON schema
- [ ] The exception hierarchy lives in `errors.py` and every module uses it
- [ ] `src/setu/ARCHITECTURE.md` written; `test_no_upward_imports` green
- [ ] Every module imports cleanly in a **fresh subprocess**
- [ ] File writes go through `atomic_write`
- [ ] Concurrency numbers recorded from your own machine
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 19` succeeded and `./m status` shows Phases 0–2 complete
