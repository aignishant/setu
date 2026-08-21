# Day 16 — CHECKLIST

**IDs covered:** PY-19, PY-20 · **Principles served:** 1, 7, 9

## Demo command

```bash
uv run python days/day-16/lab/files.py
uv run python -m pytest tests/test_io.py -v
```

Expected: the paths/encoding/formats/context-manager report, then **twelve green tests**.

## Setup

- [ ] `./m start 16` and `./m scaffold 16` run
- [ ] Files created: `days/day-16/lab/files.py`, `src/setu/io.py`, `tests/test_io.py`
- [ ] No new packages installed

## PY-19 — paths and files

- [ ] Used `/` to join paths and `name` / `stem` / `suffix` / `parent` / `parts`
- [ ] Used `with_suffix` and `resolve`
- [ ] Used `mkdir(parents=True, exist_ok=True)` and `rglob`
- [ ] Ran `encoding_matters()` and saw UTF-8 content read as latin-1 produce **mojibake, not an error**
- [ ] Can say why that silence is what makes encoding bugs survive to production
- [ ] Confirmed `"w"` truncates and `"a"` appends
- [ ] Iterated a file object lazily rather than calling `.read()`
- [ ] Used `line.rstrip()` and know what happens without it
- [ ] Round-tripped **JSONL** with `ensure_ascii=False`
- [ ] Round-tripped **CSV** with `newline=""` — and know what happens without it

## PY-20 — context managers

- [ ] Wrote a class-based context manager with `__enter__` / `__exit__`
- [ ] Confirmed `__enter__`'s return value is what `as` binds
- [ ] Returned `False` from `__exit__` and can explain what `True` would do
- [ ] Wrote the same thing with `@contextlib.contextmanager`
- [ ] Used `try/finally` around the `yield` — and know what breaks without it
- [ ] Used `contextlib.suppress` once, narrowly
- [ ] Confirmed cleanup ran on the exception path

## Build brief

- [ ] `read_jsonl` — **TODO(me)**: lazy, UTF-8, skips blanks, reports the **line number** on bad JSON
- [ ] `write_jsonl` — **TODO(me)**: creates parents, `ensure_ascii=False`, returns a count, **atomic**
- [ ] `atomic_write` — **TODO(me)**: temp file → rename on success, delete on failure, no suppression
- [ ] `read_csv_rows` — **TODO(me)**: streams dicts, `newline=""`
- [ ] Can explain why write-then-rename is safe on a crash

## Tests that must be able to fail

- [ ] All twelve were red before you implemented the TODOs
- [ ] `test_jsonl_round_trip` — green
- [ ] `test_write_jsonl_does_not_escape_non_ascii` — green
- [ ] `test_write_jsonl_creates_parent_directories` — green
- [ ] `test_read_jsonl_skips_blank_lines` — green
- [ ] `test_read_jsonl_reports_the_line_number` — green
- [ ] `test_read_jsonl_is_lazy` — green
- [ ] **Made `read_jsonl` call `f.readlines()`, watched the laziness test go red, fixed it** ← do not skip
- [ ] `test_atomic_write_leaves_no_temp_file` — green
- [ ] `test_atomic_write_preserves_the_original_on_failure` — green ← **today's real assessment**
- [ ] **Wrote directly to `path` with `open(path, "w")`, watched the original get destroyed, fixed it** ← do not skip
- [ ] `test_atomic_write_does_not_suppress_the_exception` — green
- [ ] **Returned `True` from the cleanup, watched the exception vanish, reverted** ← do not skip
- [ ] `test_write_jsonl_is_atomic` — green
- [ ] `test_csv_rows_round_trip` — green
- [ ] `test_utf8_is_explicit_everywhere` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are the three file bugs from §1, and why is each one invisible until it is expensive?
- [ ] Why must `encoding="utf-8"` be explicit at every call site?
- [ ] Why does the `csv` module require `newline=""`?
- [ ] Walk through what `with X as y:` does, on both the success and the exception path
- [ ] What does returning `True` from `__exit__` do, and why is that dangerous?
- [ ] Why does a `@contextmanager` generator need `try/finally`?
- [ ] Why is write-then-rename atomic, and which later day depends on it?

## Commit

- [ ] `./m check && ./m done 16` succeeded
