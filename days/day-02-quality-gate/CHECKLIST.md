# Day 2 — CHECKLIST

**IDs covered:** none (Foundry) · **Principles served:** 1, 4, 5, 6, 7, 11, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 14, in [`parts/`](parts/)

> `./m done 2` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, `./m check` green, and one green
> run of the workflow on a real push.

## Demo command

```bash
./m check; echo "gate exit: $?"; uv run python scripts/check_blocks.py; echo "blocks exit: $?"
```

Expected: the gate prints **OK all green**, the block checker reports **0** unparseable blocks, and
both exit **0**.

---

## Section 1 — the linter

- [x] Read [1.1 — what a linter is](parts/01-linting/1.1-what-a-linter-is.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.2 — choosing rule families](parts/01-linting/1.2-choosing-rule-families.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.3 — `--fix` and `noqa` as debt](parts/01-linting/1.3-fix-and-noqa-as-debt.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Wrote a file with an unused import, a misspelled variable and a typo, and read all three findings
- [x] Ran `ruff check days/` and saw `All checks passed!` after it checked **nothing** — and can say why
- [x] Ran `uv run ruff rule F821` and `uv run ruff linter` instead of searching the internet
- [x] Ran the same file with `--select F` and with the project's six families, and can name what each extra family added
- [x] Found `select`, `line-length` and `target-version` in `pyproject.toml` by parsing it, not by eye
- [x] Watched `--fix` change one line and `--fix --unsafe-fixes` change a second, and read both diffs
- [x] Used `--diff` to see a fix **without** applying it
- [x] Can state the difference between a safe fix and an unsafe one, with the `list(rows)` example

## Section 2 — the formatter

- [x] Read [2.1 — why a formatter ends the argument](parts/02-formatting/2.1-why-a-formatter-ends-the-argument.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.2 — `format --check` and the CI split](parts/02-formatting/2.2-format-check-and-the-ci-split.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.3 — Python inside Markdown](parts/02-formatting/2.3-python-inside-markdown.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Wrote a deliberately ugly file and read every decision the formatter made to it
- [x] **Proved idempotence** — ran the formatter twice and confirmed the second run changed nothing
- [x] **Proved the AST is unchanged** with `ast.dump`, rather than believing the contract
- [x] Saw `--check` and `--diff` both exit **1** while leaving the file on disk untouched
- [x] Wrote a two-gate script and watched `set -e` stop it at the format gate
- [x] Ran `ruff format --check days/` and `ruff check days/` side by side and can explain both outputs
- [x] Watched the format gate **pass** on a Markdown file containing a Python block with a missing colon

## Section 3 — pytest

- [x] Read [3.1 — the test that can go red](parts/03-pytest/3.1-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question
- [x] Read [3.2 — fixtures and `tmp_path`](parts/03-pytest/3.2-fixtures-and-tmp-path.md), ran its check-yourself, answered its out-loud question
- [x] Read [3.3 — markers and exit code 5](parts/03-pytest/3.3-markers-and-exit-code-five.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Wrote `test_wishful` and `test_actually_checks`, broke the function, and watched **only one** go red
- [x] Read a real pytest failure report and identified where assertion rewriting printed both sides
- [x] Ran `--collect-only` and can say what discovery found and what it ignored
- [x] Reproduced the shared-module-state failure, then fixed it with a function-scoped fixture
- [x] Ran `--setup-show` and watched a fixture set up and torn down **once per test**
- [x] Used `tmp_path` and confirmed the second test's directory was empty
- [x] Confirmed `monkeypatch.setenv` did **not** leak into the following test
- [x] Ran `-m "not live"` and read `deselected`, not `skipped` — and can state the difference
- [x] Made a selection that matched nothing and saw exit code **5**
- [x] Wrote a misspelled marker and watched `--strict-markers` turn it into a collection error

## Section 4 — the gate

- [x] Read [4.1 — what `./m check` runs](parts/04-the-gate/4.1-what-m-check-actually-runs.md), ran its check-yourself, answered its out-loud question
- [x] Read [4.2 — local gate vs remote gate](parts/04-the-gate/4.2-local-gate-versus-remote-gate.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Read the `check)` branch of `./m` and can name which part of today explains each line
- [x] Broke one file two ways and watched **two different gates** refuse it
- [x] Confirmed the exit code propagates out of `./m check` into an `if`
- [x] Can give the ordering rule in one sentence, and the reason that is **not** about speed
- [x] Installed a pre-commit hook, watched it refuse a commit, then watched `--no-verify` skip it
- [x] Timed the hook's gates against the full gate and can say why the hook holds only the fast ones
- [x] Removed the hook, or kept it deliberately and wrote down why
- [x] Can name what a remote gate needs **besides** running on every push before it is unskippable

## Section 5 — CI

- [x] Read [5.1 — what CI actually is](parts/05-ci/5.1-what-ci-actually-is.md), ran its check-yourself, answered its out-loud question
- [x] Read [5.2 — the workflow file, block by block](parts/05-ci/5.2-the-workflow-file-block-by-block.md), ran its check-yourself, answered its out-loud question
- [x] Read [5.3 — caching and never spending a quota](parts/05-ci/5.3-caching-and-never-spending-a-quota.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Listed untracked **and** ignored files, and confirmed nothing the build needs is in either list
- [x] Cloned the repo into `/tmp`, ran `uv sync --locked` and `./m check`, and it was green
- [x] Deleted the temporary clone afterwards
- [x] Can name the four categories of local accident a fresh machine erases
- [x] Timed a cold `uv sync` against a warm one and looked at the cache size
- [x] Hashed `uv.lock`, changed a pin, re-locked, and watched the digest change
- [x] Counted the `live` and `not live` collections and confirmed they sum to the whole suite
- [x] Confirmed **0** provider keys are visible, printing names only and never a value

---

## Build brief — the reps that are yours

- [x] Created `.github/workflows/check.yml` from the blocks in section 5 — not copied from elsewhere
- [x] It triggers on `push` to `main`, on `pull_request`, and manually
- [x] It cancels superseded runs on the same branch with `concurrency`
- [x] It sets `permissions: contents: read` and nothing more (Principle 11)
- [x] It carries a `timeout-minutes`
- [x] **Every** action is pinned by commit hash, with the version in a trailing comment
- [x] It installs with `uv sync --locked` and then runs `./m check` — and nothing else
- [x] Wrote the two decisions (branch filter, timeout value) as comments at the top, with reasons
- [x] `git ls-files -s -- m` prints `100755`
- [x] Pushed, and watched the workflow run **green** on a real push
- [x] Broke something on a branch on purpose and watched the workflow go **red**, then fixed it
- [x] Created `scripts/check_blocks.py` from the skeleton in the hub's §4
- [x] Implemented `python_blocks` — built the fence from `chr(96)`, non-greedy, `re.M | re.S`
- [x] Implemented `main` — walks `days/`, catches `SyntaxError` specifically, returns 1 on any failure
- [x] Confirmed it reports **0** unparseable blocks across every day written so far
- [x] Added it to `./m check` as a fifth gate, and can defend where in the order it sits

## The eval — it must be able to fail

- [x] Ran `uv run python -m pytest tests/test_quality_gate.py -v` **before** implementing and watched all four fail
- [x] Implemented `test_ruff_config_selects_the_six_families` — its message names the missing families
- [x] Implemented `test_markers_are_declared_and_strict` — and wrote the comment on why both halves matter
- [x] Implemented `test_the_gate_refuses_broken_code` — with cleanup in a `finally:` block
- [x] Implemented `test_ci_holds_no_provider_keys` — prints key **names** only, never a value
- [x] **Break it, watch it go red, fix it —** removed `"B"` from `select`, saw the config test go red, restored it
- [x] **Break it, watch it go red, fix it —** removed `--strict-markers`, saw the marker test go red, restored it
- [x] **Break it, watch it go red, fix it —** ran with `CI=true` and a fake key set, saw the budget test go red, unset it
- [x] Worked out why commenting out the `pytest` line does **not** make `test_the_gate_refuses_broken_code` fail, and broke the gate in a way that test does catch
- [x] **The five seconds that matter —** changed an assertion in `tests/test_pins.py` to `assert result is not None`, watched it pass against broken code, and restored it
- [x] `./m check` is green

## Budget

- [x] **0** LLM API calls today
- [x] No provider key exists in the build's secrets, and none was added "just to check"
- [x] `enable-cache` and `concurrency.cancel-in-progress` are both in the workflow
- [x] A second CI run on an unchanged lockfile restored the cache instead of downloading
- [x] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [x] One bug a linter always catches that a test might miss, and one a test always catches that a linter never can
- [x] Why enabling every rule family makes a codebase less safe, not more
- [x] Why `--fix` and `--unsafe-fixes` are two flags, using the `list(rows)` example
- [x] What property of a formatter makes it safe to run on save, and how you would prove it for one file
- [x] Why a gate must never fix what it finds, with one developer-facing and one deployment-facing failure
- [x] Which gates reach a Python block inside a lesson, and which never will
- [x] The exact experiment that tells you whether a passing test can fail at all
- [x] Why a test passes alone and fails in the suite, and the two things `tmp_path` guarantees
- [x] How a suite can report success having collected nothing, and what stops it
- [x] The gate-ordering rule, and the reason for it that is not about speed
- [x] Why a pre-commit hook cannot be a team policy
- [x] What a green build proves about your repository that a green local run does not
- [x] Why `@v7` is not a pin, and what a build's token should be allowed to do
- [x] The three independent properties that stop CI spending a quota, and what each alone would miss

## Commit

- [x] `git status --porcelain` read **before** staging
- [x] `.github/workflows/check.yml`, `scripts/check_blocks.py`, `tests/test_quality_gate.py` and the updated `m` are all staged together
- [x] No `.pytest_cache`, `__pycache__` or scratch file appears in `git status`
- [x] `uv run python scripts/depth_check.py 2` passes
- [x] `./m done 2` ran green and created the commit
- [x] The workflow ran green on the pushed commit
