---
day: 2
phase: 0
phase_name: "Foundry"
title: "Day 2 — Foundry II: the quality machine — ruff, pytest, `./m`, CI"
ids: []
principles: ["P1 build daily", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: lab
plan: setu
plan_version: "v2.1.0"
parts: 14
generated: "2026-08-24"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 2 — Foundry II: the quality machine — ruff, pytest, `./m`, CI

**Phase 0 · Foundry** · No curriculum IDs. This day turns `./m check` from a magic word into four
gates you can defend one at a time, and then puts them on a machine that does not trust you.

> **Yesterday:** every pin verified against the live index, frozen into two files, and recorded in a
> document that regenerates itself.
> **Today:** the four gates — lint, format, offline tests, depth — and the same four running in CI,
> where nobody is watching and nothing may be spent.
> **Tomorrow:** three free keys, two free databases, and a rate budget you can actually name.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere —
> a day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

A project is eight months old. It has a build, and the build is green, and everybody believes the
green means something.

Then a customer reports missing rows. The investigation finds that a filter has been returning
nothing for eleven weeks. There is a test for it, and the test is green, because it asserts that the
result "is not None" — which an empty list satisfies perfectly. Nobody wrote that in bad faith; it
was written at the end of a Friday, it passed the first time it was run, and nobody ever asked
whether it *could* do anything else.

While that is being fixed, three more things come out. A dependency has been installed by hand on one
laptop and never declared, so the build has been silently relying on somebody's machine. The linter
was turned off two years ago by adding a flag that makes it always exit zero, because a wall of four
thousand findings had taught everyone to ignore it. And the nightly integration job has been
collecting zero tests since a directory was renamed — printing "no tests ran" and reporting success.

Four separate failures, one shape. **Every one of them is a gate that was present, looked healthy,
and was not actually checking anything.** A green light nobody has tested is not a safety system; it
is a decoration that discourages you from looking.

Today builds the opposite. Four gates, in an order chosen so the first thing you are told is the
smallest, most specific true thing. A test suite where the first thing you do with a new test is
break it on purpose and watch it go red. A marker that keeps every network call out of the automated
path, so a build that runs sixty times a day cannot quietly drain a daily allowance. And all of it
behind one command, `./m check`, that lives in the repository and runs identically on your laptop and
on a machine created ninety seconds ago that has never met you.

The thread running through the whole day is one question, asked of every tool: **how would I know if
this stopped working?** A linter answers it by being run against broken code. A test answers it by
being watched to fail. A gate answers it by refusing something. A build answers it by starting from
nothing.

```mermaid
flowchart LR
    S1["§1 linting<br/>read without running"] --> S2["§2 formatting<br/>one canonical shape"]
    S2 --> S3["§3 pytest<br/>the test that can go red"]
    S3 --> S4["§4 the gate<br/>four refusals in order"]
    S4 --> S5["§5 CI<br/>a machine that does not trust you"]
    style S1 fill:#1f6feb,color:#fff
    style S5 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** This is a `lab` day with no IDs, so the sections are the
*tools of the quality machine, in the order they run*: **1.x** the linter that reads without running,
**2.x** the formatter that ends the argument, **3.x** the tests that can go red, **4.x** the gate that
chains all of them, **5.x** the fresh machine that runs the gate where nobody is watching.

### Section 1 — the linter: reading code without running it

| Part | What it answers | Level |
|---|---|---|
| [1.1 What a linter is, and the two questions it cannot answer](parts/01-linting/1.1-what-a-linter-is.md) | What can a tool learn from source it never executes — and what can it never learn? | `foundation` |
| [1.2 Rule families, and choosing the six this project runs](parts/01-linting/1.2-choosing-rule-families.md) | Why does turning on every rule make a codebase *less* safe? | `working` |
| [1.3 `--fix`, unsafe fixes, and `noqa` as a debt record](parts/01-linting/1.3-fix-and-noqa-as-debt.md) | When may a machine edit your code, and what does a bare `noqa` cost you in a year? | `production` |

### Section 2 — the formatter: one canonical shape

| Part | What it answers | Level |
|---|---|---|
| [2.1 Why a formatter ends the argument](parts/02-formatting/2.1-why-a-formatter-ends-the-argument.md) | Why is a tool with almost no options better than a configurable one? | `foundation` |
| [2.2 `format --check`, and where each half of the tool belongs](parts/02-formatting/2.2-format-check-and-the-ci-split.md) | Why must a gate never fix what it finds? | `working` |
| [2.3 Python inside Markdown — why this repository's lessons are code](parts/02-formatting/2.3-python-inside-markdown.md) | Which gates reach a code block in a lesson, and which never will? | `production` |

### Section 3 — pytest: the test that can go red

| Part | What it answers | Level |
|---|---|---|
| [3.1 The test that can go red — assertion rewriting and discovery](parts/03-pytest/3.1-the-test-that-can-go-red.md) | How do you know a passing test could ever fail? | `foundation` |
| [3.2 Fixtures, `tmp_path`, and the test that leaves nothing behind](parts/03-pytest/3.2-fixtures-and-tmp-path.md) | Why does a test pass alone and fail in the suite? | `working` |
| [3.3 Markers, `--strict-markers`, and the exit code that means "nothing ran"](parts/03-pytest/3.3-markers-and-exit-code-five.md) | How can a suite report success having run nothing at all? | `production` |

### Section 4 — the gate: four refusals in a fixed order

| Part | What it answers | Level |
|---|---|---|
| [4.1 What `./m check` actually runs, and why the order is not arbitrary](parts/04-the-gate/4.1-what-m-check-actually-runs.md) | Why does lint come before tests for a reason that is *not* speed? | `working` |
| [4.2 The local gate and the remote gate, and why you need both](parts/04-the-gate/4.2-local-gate-versus-remote-gate.md) | Which of your controls are enforcement and which are suggestions? | `production` |

### Section 5 — CI: a machine that does not trust you

| Part | What it answers | Level |
|---|---|---|
| [5.1 What CI actually is — a fresh machine that does not trust you](parts/05-ci/5.1-what-ci-actually-is.md) | What does a green build prove that a green local run does not? | `foundation` |
| [5.2 The workflow file, block by block](parts/05-ci/5.2-the-workflow-file-block-by-block.md) | Why is `@v7` not a pin, and what should a build's token be allowed to do? | `working` |
| [5.3 Caching, and why CI must never spend a quota](parts/05-ci/5.3-caching-and-never-spending-a-quota.md) | What does this run consume, multiplied by how often it runs? | `production` |

---

## §3 Setup — run this

**No new packages today.** `ruff==0.16.4` and `pytest==9.1.1` were pinned into the `dev` group on
[Day 0](../day-00-setup/LESSON.md) and are already in `uv.lock`. Everything else this day uses is the
standard library or a tool you already have. That is deliberate: a day about quality tooling that
began by installing four new things would be teaching the opposite lesson.

```bash
mkdir -p .github/workflows tests
touch .github/workflows/check.yml tests/test_quality_gate.py

# confirm the two tools this day is about are the pinned versions, not something on your PATH
uv run ruff --version
uv run python -m pytest --version

# the gate must be executable IN GIT, or CI fails with "Permission denied" (part 5.2)
git ls-files -s -- m

# and confirm your machine is not hiding anything from a fresh clone (part 5.1)
git status --porcelain --untracked-files=all
uv lock --check && echo "pyproject and uv.lock agree"
```

| What | Where it comes from | Part |
|---|---|---|
| `ruff` | `dev` group, pinned `==0.16.4` | [1.1](parts/01-linting/1.1-what-a-linter-is.md) |
| `pytest` | `dev` group, pinned `==9.1.1` | [3.1](parts/03-pytest/3.1-the-test-that-can-go-red.md) |
| `ast`, `hashlib`, `os`, `re` | standard library | [2.3](parts/02-formatting/2.3-python-inside-markdown.md) |
| `actions/checkout`, `astral-sh/setup-uv` | GitHub Actions, pinned by commit hash | [5.2](parts/05-ci/5.2-the-workflow-file-block-by-block.md) |

If `git ls-files -s -- m` prints `100644` rather than `100755`, fix it now — it is the single most
common reason a first CI run fails:

```bash
git update-index --chmod=+x m
```

---

## §4 Build brief

Three files are yours. The parts contain every technique; assembling them is the rep, and the
`TODO(me)` bodies are deliberately unsolved.

**1. `.github/workflows/check.yml`** — the remote gate. Section 5 gives you every block; your job is
to assemble them into one file that satisfies all six properties below. Do not copy a workflow from
elsewhere — the whole point of [5.2](parts/05-ci/5.2-the-workflow-file-block-by-block.md) is that you
can defend each line.

It must:

- run on pushes to `main` **and** on every pull request, plus a manual trigger
- cancel a superseded run on the same branch (`concurrency`)
- grant the job `contents: read` and nothing more (Principle 11, blast radius)
- carry a `timeout-minutes`
- pin **every** action by commit hash with the version in a trailing comment — a tag is not a pin
- install with `uv sync --locked`, then run `./m check` and nothing else

Two decisions are yours to make and to write down in a comment at the top of the file: whether to run
on pushes to every branch or only `main`, and what timeout is right for a suite that will eventually
train models. Say why, in one line each.

**2. `scripts/check_blocks.py`** — the gap-filler from
[2.3](parts/02-formatting/2.3-python-inside-markdown.md). The format gate reaches inside Markdown but
fails open on a block it cannot parse, and nothing in this repository lints lesson code. This closes
half of that.

```python
"""Parse every Python block in days/ and report the ones that are not Python.

    uv run python scripts/check_blocks.py

Exit status: 0 when every block parses, 1 when any block does not. This proves the blocks are
syntactically Python; it does not run them, and therefore proves nothing about whether they work.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FENCE = chr(96) * 3


def python_blocks(text: str) -> list[str]:
    """Every fenced python/py block in one document, in order."""
    # TODO(me): build the regex from FENCE, non-greedy, with re.M | re.S.
    # Part 2.3 explains why every one of those three details is required --
    # write the version that fails if you drop one, then fix it.
    raise NotImplementedError


def main() -> int:
    # TODO(me): walk days/**/*.md, ast.parse every block, print
    # "<file>: block N: <msg>" for each failure, and return 1 if any failed.
    # Catch SyntaxError specifically -- a bare except would swallow
    # KeyboardInterrupt (E722, part 1.2).
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
```

**3. Add it to the gate.** Once `check_blocks.py` passes on the whole of `days/`, add it to `./m
check` as a fifth gate. Where does it go in the order, and why? [4.1](parts/04-the-gate/4.1-what-m-check-actually-runs.md)
gives you the rule; the placement is your decision to defend.

---

## §5 The eval that must be able to fail

Create `tests/test_quality_gate.py`. All four run offline and belong in `./m check`.

```python
"""Day 2: prove the gate is a gate, and that the budget rule is mechanical."""

from __future__ import annotations

import os
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROVIDER_KEYS = ("GEMINI_API_KEY", "GROQ_API_KEY", "OPENROUTER_API_KEY", "OPENAI_API_KEY")


def test_ruff_config_selects_the_six_families() -> None:
    """Principle 4: the rule set is a pin too. See part 1.2."""
    # TODO(me): read pyproject.toml with tomllib, assert
    # [tool.ruff.lint].select contains E, F, I, UP, B and SIM. Put the
    # missing ones in the assertion message -- a failure that does not say
    # WHICH is a failure you will resent (part 3.1).
    raise NotImplementedError


def test_markers_are_declared_and_strict() -> None:
    """An undeclared marker must be an error, not a new category. Part 3.3."""
    # TODO(me): assert 'live' and 'slow' appear in
    # [tool.pytest.ini_options].markers, AND that addopts contains
    # --strict-markers. Both halves matter -- explain in a comment why
    # declaring the markers without the flag protects nothing.
    raise NotImplementedError


def test_the_gate_refuses_broken_code() -> None:
    """./m check must exit non-zero when the tree is broken. Part 4.1."""
    # TODO(me): write an unparseable .py file into src/setu/, run ./m check
    # with subprocess, assert returncode != 0, and remove the file in a
    # finally: block. If the cleanup is not in finally, one failed run
    # leaves the repo broken -- which is exactly the bug this test is about.
    raise NotImplementedError


def test_ci_holds_no_provider_keys() -> None:
    """Principle 5, as a test rather than as a promise. Part 5.3."""
    # TODO(me): skip unless os.environ.get('CI') == 'true', then assert no
    # name in PROVIDER_KEYS is set. Never print a value -- only the NAME of
    # any key you find.
    raise NotImplementedError
```

Run them and watch all four fail before you write a line:

```bash
uv run python -m pytest tests/test_quality_gate.py -v      # 4 fail
```

Then implement, then **break each one on purpose**:

- Remove `"B"` from `select` in `pyproject.toml` → `test_ruff_config_selects_the_six_families` goes
  red. Restore it.
- Remove `--strict-markers` from `addopts` → `test_markers_are_declared_and_strict` goes red. Restore
  it.
- Comment out the `pytest` line inside `./m check` → `test_the_gate_refuses_broken_code` **still
  passes**, because a parse error is caught by gate one. Work out why that is correct, then break the
  gate in a way that test *does* catch. Restore it.
- Set `CI=true GEMINI_API_KEY=fake` for one run → `test_ci_holds_no_provider_keys` goes red. Confirm
  the failure message names the key and does **not** print `fake`.

And one break with no test attached, which is the point of
[3.1](parts/03-pytest/3.1-the-test-that-can-go-red.md): open
[Day 1's](../day-01-pins/LESSON.md) `tests/test_pins.py`, change one assertion to
`assert result is not None`, and confirm it passes for a function you have deliberately broken.
Restore it. That is the day's most important five seconds.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day, and today's work is what guarantees no build ever will |
| Network requests | dependency downloads only, from the cache after the first `uv sync`; one HTTPS `GET` to `pypi.org` if you run [3.3](parts/03-pytest/3.3-markers-and-exit-code-five.md)'s `live` demo |
| CI minutes | a handful, on the free allowance. `concurrency.cancel-in-progress` and `enable-cache` are the two lines that keep it that way ([5.3](parts/05-ci/5.3-caching-and-never-spending-a-quota.md)) |
| Free-tier quota | none consumed; no provider key exists yet, and after today none ever reaches a runner |
| Cost | **$0** (Principle 5) |

The number to hold on to is not today's zero. It is the multiplier: a build runs on **every push**,
so anything it consumes is consumed dozens of times a day by four people who each thought their change
was small.

---

## §7 Traps

- **Believing `All checks passed!` when nothing was checked.** `ruff check days/` prints it after
  finding no Python files at all — [1.1](parts/01-linting/1.1-what-a-linter-is.md),
  [2.3](parts/02-formatting/2.3-python-inside-markdown.md).
- **Turning on every rule family.** Four thousand findings teach a team to ignore red —
  [1.2](parts/01-linting/1.2-choosing-rule-families.md).
- **Running `--fix --unsafe-fixes` to make a number go down.** The tool told you it was guessing —
  [1.3](parts/01-linting/1.3-fix-and-noqa-as-debt.md).
- **A bare `# noqa`.** It also silences the bug somebody writes on that line next year —
  [1.3](parts/01-linting/1.3-fix-and-noqa-as-debt.md).
- **A gate that edits your files.** Then the commit you deploy is not the commit you tested —
  [2.2](parts/02-formatting/2.2-format-check-and-the-ci-split.md).
- **Assuming the format gate validates your lesson code.** An unparseable block is silently skipped —
  [2.3](parts/02-formatting/2.3-python-inside-markdown.md).
- **A test you have never seen fail.** `assert result is not None` passes forever —
  [3.1](parts/03-pytest/3.1-the-test-that-can-go-red.md).
- **A module-level list shared between tests.** It works until something reorders them —
  [3.2](parts/03-pytest/3.2-fixtures-and-tmp-path.md).
- **Reading `1 passed` without reading `14 deselected`** — [3.3](parts/03-pytest/3.3-markers-and-exit-code-five.md).
- **A job that treats pytest's exit code 5 as success.** "No tests ran" is not a pass —
  [3.3](parts/03-pytest/3.3-markers-and-exit-code-five.md).
- **Fixing the last error in a red gate.** Read the first one; the rest are usually consequences —
  [4.1](parts/04-the-gate/4.1-what-m-check-actually-runs.md).
- **Trusting a pre-commit hook as a policy.** It is per-clone and one flag away from being skipped —
  [4.2](parts/04-the-gate/4.2-local-gate-versus-remote-gate.md).
- **Installing a package on the runner to fix a red build.** That moves the secret instead of removing
  it — [5.1](parts/05-ci/5.1-what-ci-actually-is.md).
- **`uses: some/action@v7`.** A tag can be moved; a commit hash cannot —
  [5.2](parts/05-ci/5.2-the-workflow-file-block-by-block.md).
- **A build whose suite got ten times slower and stayed green.** It has started doing something new —
  [5.3](parts/05-ci/5.3-caching-and-never-spending-a-quota.md).

---

## §8 Verify before you code

Written **2026-08-24**, against these pages, read live rather than recalled. The action versions and
cache flag in [5.2](parts/05-ci/5.2-the-workflow-file-block-by-block.md) come from the first of them —
re-check before you rely on them, which is the habit
[Day 1](../day-01-pins/LESSON.md) built:

- <https://docs.astral.sh/uv/guides/integration/github/> — the recommended workflow shape, the
  commit-pinned action versions, `enable-cache`, and `uv sync --locked`.
- <https://docs.astral.sh/ruff/linter/> — rule families, `select` vs `extend-select` vs `ignore`,
  `--fix`, `--unsafe-fixes`, `noqa`.
- <https://docs.astral.sh/ruff/formatter/> — the formatter's guarantees, `--check`, `--diff`, and
  which file types it reaches into.
- <https://docs.pytest.org/en/stable/reference/exit-codes.html> — the exit codes, including 5.
- <https://docs.pytest.org/en/stable/how-to/mark.html> — markers, `-m` expressions, `--strict-markers`.
- <https://docs.github.com/actions/writing-workflows/workflow-syntax-for-github-actions> — `on`,
  `permissions`, `concurrency`, `timeout-minutes`.
- `uv run ruff rule <CODE>` and `uv run python -m pytest --markers` — the tools describing themselves,
  ahead of any lesson.

---

## §9 Say it in an interview

> "The repository has one gate — a script in version control that runs lint, format-check, the
> offline test suite and a structural check, in that order, and stops at the first failure. The order
> is chosen so the narrowest diagnosis wins: a syntax error reported by the linter is one file and one
> column, and the same error reported by the test suite is forty tracebacks with one cause. CI runs
> that same script and nothing else, so there is exactly one definition of green and it can't drift
> between a laptop and the build server. The build starts from a fresh machine, installs from a
> committed lockfile with `--locked`, and pins every action by commit hash rather than by tag, because
> a tag is a mutable pointer and that code runs with access to the repository. It holds no API keys at
> all: every test that touches a network is marked, and the gate deselects them — so a forgotten
> marker fails loudly and free instead of quietly draining a daily quota sixty times a day. And the
> discipline underneath all of it is that a new test doesn't count until I've broken the code and
> watched it go red, because a test that has only ever passed is a test nobody has verified."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and the workflow has run
green at least once on a real push — not when a particular amount of time has passed. Then:

```bash
./m done 2
```

Tomorrow is Foundry III: three free keys, two free databases, and the rate budget that today's build
is forbidden from spending.
