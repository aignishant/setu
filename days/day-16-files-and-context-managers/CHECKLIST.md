# Day 16 — CHECKLIST

**IDs covered:** `PY-19`, `PY-20` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 19, in [`parts/`](parts/)

> `./m done 16` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_jsonl.py tests/test_paths.py -v && ./m check
```

Expected: twelve tests in `test_jsonl.py` plus the four parametrised and plain rows in `test_paths.py`
passing, then a green gate.

---

## Setup

- [ ] Created `src/setu/paths.py`, `src/setu/jsonl.py`, `src/setu/atomic.py` and both test files
- [ ] Ran `uv run python -c "from setu.paper import Paper; print('ok')"` **before** writing anything
- [ ] Ran the ten-fact setup block in the hub's §3 and can say what each of the ten lines proved
- [ ] Read `uv run ruff rule PLW1514` and `uv run ruff rule B012` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — the path

- [ ] Read [1.1 — a path is not a string](parts/01-the-path/1.1-a-path-is-not-a-string.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — taking a path apart](parts/01-the-path/1.2-taking-a-path-apart.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — relative, absolute, and the cwd](parts/01-the-path/1.3-relative-absolute-and-the-cwd.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `exists()`, `mkdir()`, and the race](parts/01-the-path/1.4-exists-mkdir-and-the-race.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — globbing](parts/01-the-path/1.5-globbing.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed the same `Path` as `repr` and as `str` and saw two different separators
- [ ] Confirmed a `Path` is **not** equal to the equivalent `str`
- [ ] Built `'lists' + 'shopping.txt'` and confirmed the result exists nowhere
- [ ] Printed `'lists\new\file.txt'` and watched the escape sequences fire
- [ ] Printed `.name`, `.stem`, `.suffix`, `.parent` and `.parts` for one path
- [ ] Did the same for `corpus.tar.gz` and found the two surprises
- [ ] Found a `.suffix` on a **folder** called `v1.2`
- [ ] Called `with_suffix` without assigning the result and confirmed nothing changed
- [ ] Resolved a relative path, changed directory, and resolved it again
- [ ] Ran the same one-line command from two folders and watched `data/` appear and disappear
- [ ] Built `base / '../../secrets.env'` and confirmed `is_relative_to(base)` is `False`
- [ ] Called `resolve(strict=True)` on a missing path and read the error
- [ ] Ran `mkdir(parents=True, exist_ok=True)` twice with no error
- [ ] Removed each flag in turn and read the two different errors
- [ ] Put a **file** where a folder should be and confirmed `exist_ok=True` still raises
- [ ] Called `unlink()` twice and then `unlink(missing_ok=True)` twice
- [ ] Wrote `if folder.glob('*.nothing'):` and watched the branch run
- [ ] Compared `*.txt`, `*/*.txt` and `**/*.txt` on the same tree
- [ ] Consumed a glob twice and got two results and then none

---

## Section 2 — reading and writing

- [ ] Read [2.1 — `open()` and the mode string](parts/02-reading-and-writing/2.1-open-and-the-mode-string.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — encoding](parts/02-reading-and-writing/2.2-encoding.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — newlines](parts/02-reading-and-writing/2.3-newlines.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — reading a big file](parts/02-reading-and-writing/2.4-reading-a-big-file.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — JSONL](parts/02-reading-and-writing/2.5-jsonl.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran `r`, `a`, `w` and `x` on the same file and read the four outcomes
- [ ] Opened `'w'`, raised before writing, and read the **empty** file back
- [ ] Ran a loop that opens `'w'` per iteration and kept only the last batch
- [ ] Wrote a `str` to a binary handle and read the `TypeError`
- [ ] Read one UTF-8 file as `utf-8`, `latin-1` and `ascii` and **counted the characters**
- [ ] Printed `locale.getpreferredencoding(False)` on this machine
- [ ] Round-tripped through the wrong encoding twice and watched the damage double
- [ ] Read a file with a BOM and found the invisible character with `repr`
- [ ] Wrote `'milk\nbread\n'` in text mode and read it back with `read_bytes`
- [ ] Compared the sha256 of two files with identical text and different newlines
- [ ] Wrote a CSV without `newline=''` and found `\r\r\n`
- [ ] Compared `readlines()` and `for line in f` with `tracemalloc`
- [ ] Confirmed a line from a file is `'milk\n'`, not `'milk'`
- [ ] Counted a file then tried to filter it with the same handle, and got zero
- [ ] Wrote a JSONL file and printed its **bytes**
- [ ] Appended one record without reading the first three
- [ ] Chopped bytes off a JSONL and a JSON file and compared what survived
- [ ] Wrote a JSONL with `indent=2` and confirmed **every** line fails to parse
- [ ] Appended to a file ending mid-record and lost two records

---

## Section 3 — buffering

- [ ] Read [3.1 — the write that had not happened](parts/03-buffering/3.1-the-write-that-had-not-happened.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — flush, fsync, and "saved"](parts/03-buffering/3.2-flush-fsync-and-what-saved-means.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — fifty thousand lines](parts/03-buffering/3.3-fifty-thousand-lines.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote twice and read `stat().st_size` as **0 bytes**
- [ ] Watched the size change at `flush()` and again at `close()`
- [ ] Ran a script that writes three lines and calls `os._exit(0)`, then read the empty file
- [ ] Compared `buffering=-1` and `buffering=1` on the same single write
- [ ] Read a file another handle is still writing and got nothing, with no error
- [ ] Printed the size at all three levels and confirmed `fsync` changes nothing visible
- [ ] Timed 2000 lines buffered against 2000 lines with `fsync` per line
- [ ] Timed `fsync` every record against every five hundredth
- [ ] Watched four valid, complete-looking sizes for one growing file
- [ ] Compared peak memory for the list-first and streamed versions of 50 000 records
- [ ] Confirmed the two output files are **byte-identical**
- [ ] Added one `list()` to the streaming version and watched the peak jump
- [ ] Built the whole output with `+=` and compared time **and** memory

---

## Section 4 — context managers

- [ ] Read [4.1 — `with`](parts/04-context-managers/4.1-with-the-block-that-cleans-up.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — `try` / `finally`](parts/04-context-managers/4.2-try-finally-is-what-with-is.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `__enter__` and `__exit__`](parts/04-context-managers/4.3-enter-and-exit-by-hand.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — the `__exit__` that swallowed](parts/04-context-managers/4.4-the-exit-that-swallowed-the-exception.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — `@contextmanager`](parts/04-context-managers/4.5-contextmanager-decorator.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.6 — `ExitStack`](parts/04-context-managers/4.6-a-connection-that-always-closes.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `f.closed` inside and after a `with` block
- [ ] Raised inside a `with` and confirmed the file is still closed
- [ ] Turned on `-W error::ResourceWarning` and produced an unclosed-file warning
- [ ] Put a `close()` below an early `return` and confirmed 0 bytes on disk
- [ ] Opened files in a loop until `Too many open files`, and noted which filename it blamed
- [ ] Read from a file after its `with` block and got `I/O operation on closed file`
- [ ] Wrote the same function with `try` / `finally` and with `with` and compared
- [ ] Confirmed `finally` runs **between** the `return` and the caller
- [ ] Put a `return` inside `finally` and watched it discard an exception
- [ ] Raised inside `finally` and found the original on `__context__`
- [ ] Ran `os._exit(0)` inside a `try` and got **no output at all**
- [ ] Wrote a class with `__enter__` and `__exit__` and printed `exc_type` on both paths
- [ ] Omitted `__exit__` and read the message naming the protocol
- [ ] Gave `__exit__` the wrong number of parameters and noted the block ran first
- [ ] Put the cleanup behind `if exc_type is None` and leaked on the failure path
- [ ] Raised inside `__enter__` and confirmed `__exit__` never ran
- [ ] Returned `True` from `__exit__` and watched the caller carry on
- [ ] Wrote a `@contextmanager` with a bare `yield` and lost the cleanup on failure
- [ ] Wrote two `yield`s and read `generator didn't stop`
- [ ] Reused one generator-based manager and read the second failure
- [ ] Caught the exception at the `yield` and confirmed it was suppressed
- [ ] Opened two connections on one `with` line and read the reverse close order
- [ ] Used `ExitStack` with a run-time number of resources
- [ ] Forgot `enter_context` and watched nothing be closed, with no error

---

## Build

- [ ] `src/setu/paths.py` computes `ROOT` from `__file__`, not from the working directory
- [ ] `data_dir` uses `parents=True, exist_ok=True` and says why in a comment
- [ ] `safe_child` resolves **and** checks `is_relative_to`, and raises naming the path
- [ ] `outputs_for` states in its docstring what it does with two extensions
- [ ] `write_jsonl` takes an `Iterable`, not a `list`
- [ ] `write_jsonl` opens **once**, outside the loop, with `encoding='utf-8'` and `newline='\n'`
- [ ] `write_jsonl` has no `indent=` anywhere
- [ ] `write_jsonl` checks for a trailing newline before appending
- [ ] `read_jsonl` is a generator and yields one record at a time
- [ ] `read_jsonl` reports the **file's** line number on a bad line
- [ ] `read_jsonl`'s docstring says how a caller reaches the skipped count
- [ ] `count_records` builds no list
- [ ] `atomic_write` uses a temporary name **in the same folder**
- [ ] `atomic_write`'s `yield` is inside a `try`
- [ ] `atomic_write` re-raises after cleaning up
- [ ] `atomic_write` flushes and `fsync`s before the rename, and says which level that reaches
- [ ] Reproduced all eight traps in `notebooks/day-16-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)

---

## Tests

- [ ] Both test files exist and every test failed before any implementation
- [ ] Every test writes only into `tmp_path`
- [ ] `test_written_bytes_are_the_same_on_every_machine` asserts on **bytes**, not text
- [ ] `test_every_line_is_one_json_object` passes
- [ ] `test_a_non_ascii_title_round_trips` asserts the **length** as well as the value
- [ ] `test_append_adds_without_rewriting` passes
- [ ] `test_append_after_a_partial_line_does_not_corrupt` passes
- [ ] `test_reading_holds_one_record_at_a_time` passes
- [ ] `test_a_bad_line_can_be_skipped_and_is_counted` passes
- [ ] `test_a_bad_line_raises_by_default` asserts the **file's** line number is in the message
- [ ] `test_count_records_does_not_hold_the_file` asserts a memory threshold
- [ ] `test_atomic_write_leaves_the_old_file_on_failure` passes
- [ ] `test_atomic_write_leaves_no_temporary_file_behind` passes
- [ ] `test_atomic_write_does_not_swallow_the_exception` passes
- [ ] `test_safe_child_refuses_anything_outside_the_base` passes for **all three** shapes
- [ ] `test_safe_child_allows_an_ordinary_name` passes
- [ ] **Break it, watch it go red, fix it** — drop `newline='\n'` → the bytes test goes red **on Windows only**
- [ ] **Break it, watch it go red, fix it** — add `indent=2` → the one-object-per-line test goes red
- [ ] **Break it, watch it go red, fix it** — drop `encoding='utf-8'` on the read → the **length** assertion goes red
- [ ] **Break it, watch it go red, fix it** — `'w'` instead of `'a'` → only the append test goes red
- [ ] **Break it, watch it go red, fix it** — remove the trailing-newline check → only the partial-line test goes red
- [ ] **Break it, watch it go red, fix it** — make `read_jsonl` return a list → only the generator test goes red
- [ ] **Break it, watch it go red, fix it** — drop the skipped count → only its own test goes red
- [ ] **Break it, watch it go red, fix it** — move the `yield` outside the `try` → only the temporary-file test goes red
- [ ] **Break it and watch every test stay GREEN** — make `atomic_write` catch, clean up and not re-raise,
      and delete `test_atomic_write_does_not_swallow_the_exception`. Everything passes and every caller
      believes a failed write succeeded. Restore the test, watch it go red, and say what it was protecting.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] **0** files written outside `tmp_path` by any test
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-16-files-and-context-managers/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 16` reports no failures
- [ ] `./m done 16`
