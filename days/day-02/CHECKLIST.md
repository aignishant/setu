# Day 2 — CHECKLIST

**IDs covered:** none (Phase-0 infrastructure) · **Principles served:** 1, 5, 7

## Demo command

```bash
uv run ruff check . && uv run ruff format --check .
uv run python -m pytest -q
```

Expected: ruff clean, then **4 passed, 1 skipped**.

## Setup

- [ ] `./m start 2` and `./m scaffold 2` run
- [ ] Files created: `tests/conftest.py`, `tests/fixtures/`, `src/setu/config.py`, `tests/test_config.py`, `.github/workflows/check.yml`
- [ ] No new packages installed today

## Ruff

- [ ] `[tool.ruff.lint] select = ["E", "F", "I", "UP", "B", "SIM"]` added to `pyproject.toml`
- [ ] `line-length` and `target-version` set
- [ ] `extend-exclude` covers `notebooks` and `days/*/lab`
- [ ] `uv run ruff check .` passes
- [ ] `uv run ruff format .` run once, then `--check` passes
- [ ] Can say **out loud** what each of the six rule families is for
- [ ] Wrote the `bucket=[]` function into `days/day-02/lab/badcode.py`, ran `ruff check days/`, saw **B006**, deleted the file

## Test strategy

- [ ] `tests/conftest.py` written with `pytest_collection_modifyitems`
- [ ] Live tests are skipped unless `SETU_LIVE=1`
- [ ] `fixtures_dir` fixture written
- [ ] `_no_accidental_network` autouse fixture written and understood
- [ ] `markers` and `--strict-markers` confirmed present in `pyproject.toml`
- [ ] Typo'd a marker (`@pytest.mark.liev`) once, saw the strict-marker **error**, fixed it

## config.py

- [ ] `MissingKey`, `_require`, `Keys`, `load_keys` written
- [ ] `Keys` is `@dataclass(frozen=True)`
- [ ] `load_dotenv(override=False)` — and can explain why not `True`
- [ ] `.strip()` present on the value

## Tests that must be able to fail

- [ ] `test_missing_key_fails_loudly` — green
- [ ] `test_blank_key_is_treated_as_missing` — green
- [ ] `test_whitespace_is_stripped` — green
- [ ] **Deleted `.strip()` from `_require`, watched it go red, restored it** ← do not skip
- [ ] `test_error_message_names_the_variable` — green
- [ ] `test_this_one_is_skipped_by_default` — reported as **skipped**, never as failed
- [ ] `uv run python -m pytest -q -m live --collect-only` lists exactly the live tests

## CI

- [ ] `.github/workflows/check.yml` written
- [ ] `timeout-minutes` set
- [ ] `uv sync --locked` used — understood why `--locked` failing is a feature
- [ ] `ruff format --check` (never plain `format`) in CI
- [ ] `-m "not live"` present — **no test in CI can spend a quota**
- [ ] No `env:` block and no secrets referenced anywhere in the workflow
- [ ] Pushed once and watched the workflow go green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What exactly goes wrong around Day 150 if live and offline tests share one default run?
- [ ] Why does the socket guard fail the test rather than skip it?
- [ ] What does `--strict-markers` protect you from?
- [ ] Why must `load_dotenv` use `override=False`?
- [ ] Why is `Keys` frozen?
- [ ] Why does CI use `uv sync --locked` rather than plain `uv sync`?
- [ ] Why does the live-marked test contain an unconditional failure?

## Commit

- [ ] `./m check && ./m done 2` succeeded
