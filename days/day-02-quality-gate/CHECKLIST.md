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

- [ ] Read [1.1 — what a linter is](parts/01-linting/1.1-what-a-linter-is.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — choosing rule families](parts/01-linting/1.2-choosing-rule-families.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `--fix` and `noqa` as debt](parts/01-linting/1.3-fix-and-noqa-as-debt.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote a file with an unused import, a misspelled variable and a typo, and read all three findings
- [ ] Ran `ruff check days/` and saw `All checks passed!` after it checked **nothing** — and can say why
- [ ] Ran `uv run ruff rule F821` and `uv run ruff linter` instead of searching the internet
- [ ] Ran the same file with `--select F` and with the project's six families, and can name what each extra family added
- [ ] Found `select`, `line-length` and `target-version` in `pyproject.toml` by parsing it, not by eye
- [ ] Watched `--fix` change one line and `--fix --unsafe-fixes` change a second, and read both diffs
- [ ] Used `--diff` to see a fix **without** applying it
- [ ] Can state the difference between a safe fix and an unsafe one, with the `list(rows)` example

## Section 2 — the formatter

- [ ] Read [2.1 — why a formatter ends the argument](parts/02-formatting/2.1-why-a-formatter-ends-the-argument.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `format --check` and the CI split](parts/02-formatting/2.2-format-check-and-the-ci-split.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — Python inside Markdown](parts/02-formatting/2.3-python-inside-markdown.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote a deliberately ugly file and read every decision the formatter made to it
- [ ] **Proved idempotence** — ran the formatter twice and confirmed the second run changed nothing
- [ ] **Proved the AST is unchanged** with `ast.dump`, rather than believing the contract
- [ ] Saw `--check` and `--diff` both exit **1** while leaving the file on disk untouched
- [ ] Wrote a two-gate script and watched `set -e` stop it at the format gate
- [ ] Ran `ruff format --check days/` and `ruff check days/` side by side and can explain both outputs
- [ ] Watched the format gate **pass** on a Markdown file containing a Python block with a missing colon

## Section 3 — pytest

- [ ] Read [3.1 — the test that can go red](parts/03-pytest/3.1-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — fixtures and `tmp_path`](parts/03-pytest/3.2-fixtures-and-tmp-path.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — markers and exit code 5](parts/03-pytest/3.3-markers-and-exit-code-five.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote `test_wishful` and `test_actually_checks`, broke the function, and watched **only one** go red
- [ ] Read a real pytest failure report and identified where assertion rewriting printed both sides
- [ ] Ran `--collect-only` and can say what discovery found and what it ignored
- [ ] Reproduced the shared-module-state failure, then fixed it with a function-scoped fixture
- [ ] Ran `--setup-show` and watched a fixture set up and torn down **once per test**
- [ ] Used `tmp_path` and confirmed the second test's directory was empty
- [ ] Confirmed `monkeypatch.setenv` did **not** leak into the following test
- [ ] Ran `-m "not live"` and read `deselected`, not `skipped` — and can state the difference
- [ ] Made a selection that matched nothing and saw exit code **5**
- [ ] Wrote a misspelled marker and watched `--strict-markers` turn it into a collection error

## Section 4 — the gate

- [ ] Read [4.1 — what `./m check` runs](parts/04-the-gate/4.1-what-m-check-actually-runs.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — local gate vs remote gate](parts/04-the-gate/4.2-local-gate-versus-remote-gate.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Read the `check)` branch of `./m` and can name which part of today explains each line
- [ ] Broke one file two ways and watched **two different gates** refuse it
- [ ] Confirmed the exit code propagates out of `./m check` into an `if`
- [ ] Can give the ordering rule in one sentence, and the reason that is **not** about speed
- [ ] Installed a pre-commit hook, watched it refuse a commit, then watched `--no-verify` skip it
- [ ] Timed the hook's gates against the full gate and can say why the hook holds only the fast ones
- [ ] Removed the hook, or kept it deliberately and wrote down why
- [ ] Can name what a remote gate needs **besides** running on every push before it is unskippable

## Section 5 — CI

- [ ] Read [5.1 — what CI actually is](parts/05-ci/5.1-what-ci-actually-is.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — the workflow file, block by block](parts/05-ci/5.2-the-workflow-file-block-by-block.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.3 — caching and never spending a quota](parts/05-ci/5.3-caching-and-never-spending-a-quota.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Listed untracked **and** ignored files, and confirmed nothing the build needs is in either list
- [ ] Cloned the repo into `/tmp`, ran `uv sync --locked` and `./m check`, and it was green
- [ ] Deleted the temporary clone afterwards
- [ ] Can name the four categories of local accident a fresh machine erases
- [ ] Timed a cold `uv sync` against a warm one and looked at the cache size
- [ ] Hashed `uv.lock`, changed a pin, re-locked, and watched the digest change
- [ ] Counted the `live` and `not live` collections and confirmed they sum to the whole suite
- [ ] Confirmed **0** provider keys are visible, printing names only and never a value

---

## Build brief — the reps that are yours

- [ ] Created `.github/workflows/check.yml` from the blocks in section 5 — not copied from elsewhere
- [ ] It triggers on `push` to `main`, on `pull_request`, and manually
- [ ] It cancels superseded runs on the same branch with `concurrency`
- [ ] It sets `permissions: contents: read` and nothing more (Principle 11)
- [ ] It carries a `timeout-minutes`
- [ ] **Every** action is pinned by commit hash, with the version in a trailing comment
- [ ] It installs with `uv sync --locked` and then runs `./m check` — and nothing else
- [ ] Wrote the two decisions (branch filter, timeout value) as comments at the top, with reasons
- [ ] `git ls-files -s -- m` prints `100755`
- [ ] Pushed, and watched the workflow run **green** on a real push
- [ ] Broke something on a branch on purpose and watched the workflow go **red**, then fixed it
- [ ] Created `scripts/check_blocks.py` from the skeleton in the hub's §4
- [ ] Implemented `python_blocks` — built the fence from `chr(96)`, non-greedy, `re.M | re.S`
- [ ] Implemented `main` — walks `days/`, catches `SyntaxError` specifically, returns 1 on any failure
- [ ] Confirmed it reports **0** unparseable blocks across every day written so far
- [ ] Added it to `./m check` as a fifth gate, and can defend where in the order it sits

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_quality_gate.py -v` **before** implementing and watched all four fail
- [ ] Implemented `test_ruff_config_selects_the_six_families` — its message names the missing families
- [ ] Implemented `test_markers_are_declared_and_strict` — and wrote the comment on why both halves matter
- [ ] Implemented `test_the_gate_refuses_broken_code` — with cleanup in a `finally:` block
- [ ] Implemented `test_ci_holds_no_provider_keys` — prints key **names** only, never a value
- [ ] **Break it, watch it go red, fix it —** removed `"B"` from `select`, saw the config test go red, restored it
- [ ] **Break it, watch it go red, fix it —** removed `--strict-markers`, saw the marker test go red, restored it
- [ ] **Break it, watch it go red, fix it —** ran with `CI=true` and a fake key set, saw the budget test go red, unset it
- [ ] Worked out why commenting out the `pytest` line does **not** make `test_the_gate_refuses_broken_code` fail, and broke the gate in a way that test does catch
- [ ] **The five seconds that matter —** changed an assertion in `tests/test_pins.py` to `assert result is not None`, watched it pass against broken code, and restored it
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] No provider key exists in the build's secrets, and none was added "just to check"
- [ ] `enable-cache` and `concurrency.cancel-in-progress` are both in the workflow
- [ ] A second CI run on an unchanged lockfile restored the cache instead of downloading
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] One bug a linter always catches that a test might miss, and one a test always catches that a linter never can
- [ ] Why enabling every rule family makes a codebase less safe, not more
- [ ] Why `--fix` and `--unsafe-fixes` are two flags, using the `list(rows)` example
- [ ] What property of a formatter makes it safe to run on save, and how you would prove it for one file
- [ ] Why a gate must never fix what it finds, with one developer-facing and one deployment-facing failure
- [ ] Which gates reach a Python block inside a lesson, and which never will
- [ ] The exact experiment that tells you whether a passing test can fail at all
- [ ] Why a test passes alone and fails in the suite, and the two things `tmp_path` guarantees
- [ ] How a suite can report success having collected nothing, and what stops it
- [ ] The gate-ordering rule, and the reason for it that is not about speed
- [ ] Why a pre-commit hook cannot be a team policy
- [ ] What a green build proves about your repository that a green local run does not
- [ ] Why `@v7` is not a pin, and what a build's token should be allowed to do
- [ ] The three independent properties that stop CI spending a quota, and what each alone would miss

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `.github/workflows/check.yml`, `scripts/check_blocks.py`, `tests/test_quality_gate.py` and the updated `m` are all staged together
- [ ] No `.pytest_cache`, `__pycache__` or scratch file appears in `git status`
- [ ] `uv run python scripts/depth_check.py 2` passes
- [ ] `./m done 2` ran green and created the commit
- [ ] The workflow ran green on the pushed commit
