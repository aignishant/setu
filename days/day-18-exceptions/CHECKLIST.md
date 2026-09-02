# Day 18 — CHECKLIST

**IDs covered:** `PY-22` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 19, in [`parts/`](parts/)

> `./m done 18` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_errors.py tests/test_layout.py -v && ./m check
```

Expected: thirteen tests in `test_errors.py` and yesterday's layout tests passing, then a green gate.

---

## Setup

- [ ] Created `src/setu/errors.py`, `src/setu/manifest.py` and `tests/test_errors.py`
- [ ] Ran `uv run python -m pytest tests/test_layout.py -q` **before** writing anything, and it was green
- [ ] Ran the twelve-fact setup block and can say what each of the twelve lines proved
- [ ] Can say why line 1 had to save the exception as `kept`
- [ ] Read `uv run ruff rule E722` and `uv run ruff rule B012` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — raising and catching

- [ ] Read [1.1 — what raising does](parts/01-raising-and-catching/1.1-what-raising-does.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — `try` / `except` and catching by type](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `else` and `finally`](parts/01-raising-and-catching/1.3-else-and-finally.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — the bare `except`](parts/01-raising-and-catching/1.4-the-bare-except.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — what the object carries](parts/01-raising-and-catching/1.5-the-exception-object.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Read a three-frame traceback bottom-to-top and named what, where, and how it got there
- [ ] Replaced a `raise` with `return None` and found where the error surfaced instead
- [ ] Replaced a `raise` with a `print` and watched the program charge for a 5000g parcel
- [ ] Ran `raise 'a string'` and read `exceptions must derive from BaseException`
- [ ] Wrote three `except` clauses for three types and got three different responses
- [ ] Put `except Exception:` above `except ValueError:` and confirmed the second is dead
- [ ] Used a **tuple** of types in one clause
- [ ] Referred to the `as` name after the block and read the `NameError`
- [ ] Ran a four-clause `try` down both paths and counted which clauses printed
- [ ] Put a `return` in a `finally` and watched an exception vanish
- [ ] Ran `uv run ruff check --select B` on that file and read `B012`
- [ ] Made a `finally` raise and read which error became the headline
- [ ] Caught `sys.exit(3)` with a bare `except:` and checked the exit code was **0**
- [ ] Confirmed `issubclass(SystemExit, Exception)` is `False`
- [ ] Printed `str`, `repr`, `args` and `__traceback__` for one exception
- [ ] Called `add_note` twice and read `__notes__` and the printed traceback
- [ ] Read `__notes__` on an exception with none and got the `AttributeError`
- [ ] Built a traceback string by hand with `traceback.format_exception`

---

## Section 2 — the hierarchy

- [ ] Read [2.1 — catching catches subclasses](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — which built-in to raise](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `raise ... from`](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — re-raising](parts/02-the-hierarchy/2.4-re-raising.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Caught three different `OSError` subclasses with one clause
- [ ] Printed the `__mro__` for `FileNotFoundError`, `KeyError` and `TimeoutError`
- [ ] Confirmed `KeyError` is **not** an `IndexError`
- [ ] Confirmed `UnicodeDecodeError` **is** a `ValueError`
- [ ] Made a custom exception inherit from `ConnectionError` and watched an unrelated retry loop catch it
- [ ] Ran the eight-expression table and matched each mistake to its built-in type
- [ ] Ran `raise NotImplemented` and read why it is a `TypeError`
- [ ] Wrote a `weigh()` that raises `TypeError`, `KeyError` and `ValueError` for three different reasons
- [ ] Raised inside a handler **without** `from` and read *During handling of the above exception*
- [ ] Raised inside a handler **with** `from` and read *the direct cause of*
- [ ] Printed `__cause__`, `__context__` and `__suppress_context__` for all three forms
- [ ] Used `from None` and confirmed `__context__` is still on the object
- [ ] Counted the traceback frames for a bare `raise` and for `raise error`
- [ ] Ran a bare `raise` outside a handler and read the `RuntimeError`
- [ ] Wrote log-and-swallow, watched the caller get `None`, then added `raise`

---

## Section 3 — your own

- [ ] Read [3.1 — one base class per project](parts/03-your-own/3.1-one-base-class-per-project.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — an exception that carries data](parts/03-your-own/3.2-an-exception-that-carries-data.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — the message is an interface](parts/03-your-own/3.3-the-message-is-an-interface.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — translating at the boundary](parts/03-your-own/3.4-translate-at-the-boundary.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Built a three-level family and handled it with two clauses at two levels
- [ ] Confirmed a library's `ValueError` is **not** caught by `except MyBaseError:`
- [ ] Wrote a class that forgot to inherit and read the failure at the `raise`
- [ ] Built `RateLimited` with `provider` and `retry_after` as attributes
- [ ] Pickled it and got `retry_after` back
- [ ] Passed a formatted string to `super().__init__` and watched the pickle fail
- [ ] Made `retry_after` keyword-only and watched the pickle fail differently
- [ ] Removed `__str__` and read what the log line became
- [ ] Wrote a message answering all four questions and one answering none
- [ ] Used `!r` and confirmed `''` and `'   '` are distinguishable
- [ ] Put an API key in a message, read the log line, and deleted the experiment
- [ ] Parsed a delay out of a message with a regex, then reworded the message and watched it break
- [ ] Translated `OSError` and `json.JSONDecodeError` into one type, both `from error`
- [ ] Confirmed the file's line number and `json`'s "line 1" are both correct
- [ ] Caught `Exception` at a boundary and watched a typo be reported as a data problem

---

## Section 4 — in anger

- [ ] Read [4.1 — the `except` that was too wide](parts/04-in-anger/4.1-the-except-that-was-too-wide.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — ask forgiveness or ask permission](parts/04-in-anger/4.2-eafp-and-lbyl.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — `logging.exception`](parts/04-in-anger/4.3-logging-exception.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.4 — `pytest.raises`](parts/04-in-anger/4.4-pytest-raises.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.5 — `ExceptionGroup` and `except*`](parts/04-in-anger/4.5-exception-groups.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.6 — when not to raise](parts/04-in-anger/4.6-when-not-to-raise.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the three-row pipeline with `except Exception` and with `except ValueError` and compared
- [ ] Watched a broad handler make a function's failure path untestable
- [ ] Watched a broad handler in a loop report a dropped connection as bad data
- [ ] Timed look-before against try-it for a present key and a missing key
- [ ] Ran `if exists()` then `unlink()` with the file removed in between
- [ ] Found a check that asks a different question from the operation it guards
- [ ] Compared `print`, `log.error(str)`, `log.error(exc_info=True)` and `log.exception`
- [ ] Called `log.exception` outside a handler and read `NoneType: None`
- [ ] Logged with an f-string and with `%s` and said which one groups in a tracker
- [ ] Wrote a `pytest.raises` that fails, and read `DID NOT RAISE`
- [ ] Put two statements in a `pytest.raises` block and confirmed the second never ran
- [ ] Asserted on `caught.value` attributes rather than on the message
- [ ] Raised an `ExceptionGroup` uncaught and read the tree-shaped traceback
- [ ] Handled one with `except*` and confirmed **every** matching clause ran
- [ ] Tried to catch a group with plain `except ValueError:` and watched it not match
- [ ] Read the `SyntaxError` from mixing `except` and `except*`
- [ ] Read the `SyntaxError` from `return` inside `except*`
- [ ] Compared `str.find` with `str.index` and `dict.get` with `d[k]`
- [ ] Built a sentinel that collides with a real value and watched it lie

---

## Build

- [ ] `src/setu/errors.py` imports **nothing** from `setu` — it is a leaf
- [ ] `SetuError` inherits from `Exception`, not from a built-in, and says why in its docstring
- [ ] `ConfigError` carries the variable **name** and never its value
- [ ] `RateLimited` inherits from `ProviderError`, which inherits from `SetuError`
- [ ] `RateLimited.__init__` passes the **fields** to `super().__init__`
- [ ] `RateLimited` stores `provider` and `retry_after` as attributes
- [ ] `RateLimited.__str__` is computed from the attributes
- [ ] `retry_delay` uses `isinstance`, not `hasattr` and not a regex, and says why in a comment
- [ ] **Wrote down, in two sentences, what `retry_delay` does with an absurd `retry_after`**
- [ ] `ManifestError` carries `path` and an optional `line`
- [ ] `load_manifest` catches `OSError` and `json.JSONDecodeError` and nothing wider
- [ ] Both translations use `from error`
- [ ] `enumerate(..., start=1)`, so the reported line number is the file's
- [ ] Added `errors` (layer 0) and `manifest` to `LAYERS` in `src/setu/layout.py`
- [ ] `tests/test_layout.py` still passes with the two new modules
- [ ] Reproduced all eight traps in `notebooks/day-18-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)

---

## Tests

- [ ] `tests/test_errors.py` exists and every test failed before any implementation
- [ ] Every test runs offline and writes only into `tmp_path`
- [ ] `test_every_error_is_a_setu_error` passes for all four classes
- [ ] `test_rate_limited_is_a_provider_error_but_not_a_connection_error` passes
- [ ] `test_rate_limited_carries_the_delay` asserts **attributes**, not the message
- [ ] `test_rate_limited_survives_a_round_trip` passes
- [ ] `test_str_is_readable_and_names_the_number` passes
- [ ] `test_config_error_never_contains_the_value` passes
- [ ] `test_retry_delay_reads_the_exception` passes
- [ ] `test_retry_delay_does_not_parse_the_message` passes
- [ ] `test_load_manifest_reports_the_files_line_number` asserts the number **2**
- [ ] `test_load_manifest_keeps_the_cause` passes
- [ ] `test_load_manifest_never_leaks_a_json_exception` passes for both inputs
- [ ] `test_a_bug_is_not_translated` passes
- [ ] `test_the_handler_does_not_swallow` passes
- [ ] **Break it, watch it go red, fix it** — `RateLimited(ConnectionError)` → two tests go red
- [ ] **Break it, watch it go red, fix it** — a formatted string in `super().__init__` → only the pickle
      test goes red
- [ ] **Break it, watch it go red, fix it** — delete `__str__` → only the readable-message test goes red
- [ ] **Break it, watch it go red, fix it** — a regex in `retry_delay` → only the message test goes red
- [ ] **Break it, watch it go red, fix it** — drop `from error` → only the cause test goes red
- [ ] **Break it, watch it go red, fix it** — `enumerate` from 0 → the line-number test goes red by one
- [ ] **Break it, watch it go red, fix it** — widen to `except Exception` → only the not-translated test
      goes red
- [ ] **Break it, watch it go red, fix it** — put the value in `ConfigError`'s message → one test goes red
- [ ] **Break it and watch every test stay GREEN** — make `load_manifest` catch `ManifestError` and
      `return []`, **and** delete `test_the_handler_does_not_swallow`. Everything passes and every caller
      believes a malformed manifest was empty. Restore the test, watch it go red, and say what it was
      protecting.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] **0** new packages added today
- [ ] **0** secrets written into any exception message
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-18-exceptions/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 18` reports no failures
- [ ] `./m done 18`
