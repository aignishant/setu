# Day 1 — CHECKLIST

**IDs covered:** none (Foundry) · **Principles served:** 4, 7, 13, 14, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 1` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python scripts/check_pins.py; echo "drift exit: $?"; grep -n "verified" docs/PINS_DS.md; ./m check
```

Expected: the tool prints a table and exits **0**, `docs/PINS_DS.md` carries **today's** date, and
`./m check` is green.

---

## Section 1 — what a version is

- [x] Read [1.1 — semantic versioning](parts/01-versions/1.1-semantic-versioning.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.2 — version specifiers](parts/01-versions/1.2-version-specifiers.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.3 — the resolution problem](parts/01-versions/1.3-the-resolution-problem.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Watched `sorted(['1.9.0','1.10.0'])` put `1.9.0` last, and `sorted(..., key=Version)` fix it
- [x] **Predicted all four answers** in 1.2's check-yourself before running it — and was right about `~=3.0` vs `~=3.0.5`
- [x] Ran `uv tree` and counted the packages nobody declared
- [x] Forced a resolution conflict on purpose and identified its two premises and conclusion

## Section 2 — reading the truth from the index

- [x] Read [2.1 — PyPI's JSON API](parts/02-pypi-index/2.1-the-pypi-json-api.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.2 — yanked and pre-release](parts/02-pypi-index/2.2-yanked-and-prerelease.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.3 — the check-pins script](parts/02-pypi-index/2.3-the-check-pins-script.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Fetched a package's metadata with `urllib.request` — with a `User-Agent` **and** a `timeout`
- [x] Listed the deprecated top-level keys the server still returns, and can say why using them is a bug
- [x] Printed "newest published" and "newest stable" for a package and understand when they differ
- [x] Checked the `yanked` flag on a specific release, not just `info.version`
- [x] Can state PEP 592's rule about which specifiers still install a yanked file
- [x] Ran a loop where one package 404s and the others still get checked

## Section 3 — freezing it

- [x] Read [3.1 — the Python-version intersection](parts/03-freezing/3.1-the-python-version-intersection.md), ran its check-yourself, answered its out-loud question
- [x] Read [3.2 — freezing into pyproject and the lock](parts/03-freezing/3.2-freezing-into-pyproject-and-the-lock.md), ran its check-yourself, answered its out-loud question
- [x] Read [3.3 — regenerating pins from evidence](parts/03-freezing/3.3-regenerating-pins-from-evidence.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] **Computed** the allowed interpreter set by intersecting `requires_python` — did not read it off a table
- [x] The computed set still contains **3.12**; if it does not, wrote an addendum instead of editing a pin
- [x] Identified which package supplies the floor and which supplies the ceiling
- [x] Broke `pyproject.toml` on purpose and watched `uv lock --check` and `uv sync --locked` refuse
- [x] **Watched `uv sync --frozen` pass on the same broken state** — and can explain why that is not a bug
- [x] Restored it and confirmed `uv lock --check` exits 0
- [x] Ran `uv lock --upgrade-package <name>` and looked at how small the diff is

## Section 4 — keeping it frozen

- [x] Read [4.1 — the three breaking changes](parts/04-drift/4.1-the-three-breaking-changes.md), ran its check-yourself, answered its out-loud question
- [x] Read [4.2 — drift and the amendment protocol](parts/04-drift/4.2-drift-and-the-amendment-protocol.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Found every ⚠️ marker in `docs/PINS_DS.md` and the plan, and can say what each one is warning about
- [x] Can name the difference between a **loud** and a **silent** breaking change, with an example of each
- [x] Read this repository's own amendment in `docs/CHANGELOG_PLAN_DS.md` and found its four parts
- [x] Drafted a drift entry using the template, even though there is nothing to record yet

## The two documents underneath

Sections 1–4 are clauses of two published specifications. Plan v2.3.0 retired the separate paper
document, so both are now cited inside the parts that rest on them, and read at their canonical URLs.

- [x] Read *Semantic Versioning 2.0.0* (2013) at <https://semver.org/spec/v2.0.0.html>, and found the
      clause that says a major bump is the authors' own admission of a break
- [x] Read *PEP 440* (2013) at <https://peps.python.org/pep-0440/>, and found the clause that says
      what `==` means when the released file carries a local version segment

**Proof, not belief:**

- [x] Watched `Version('1.0.0-alpha.1')` become `1.0.0a1` — a string rewritten by a document you had
      not read
- [x] Can state one rule where the two specifications **disagree**, and which one `uv` obeys

---

## Build brief — the reps that are yours

- [x] Created `scripts/check_pins.py` from the skeleton in the hub's §4
- [x] Implemented `read_pins` — reads **every** dependency group, not just `dev`
- [x] Implemented `fetch_current` — timeout, `User-Agent`, filters pre-releases, reads `yanked`
- [x] Implemented `classify` — a **pure** function, no network, most specific condition first
- [x] Implemented `main` — per-package `try` **inside** the loop, exit 1 on drift
- [x] Added the cache with an expiry, and confirmed a second run makes no network requests
- [x] Added `--markdown` and `--json` output modes, with data on stdout and chatter on stderr
- [x] Added `.pins-cache.json` to `.gitignore`
- [x] Regenerated the table in `docs/PINS_DS.md` and set `verified:` to today
- [x] **Left the authored "Python version reasoning" section alone** — generated the fact, kept the judgement

## The eval — it must be able to fail

- [x] Ran `uv run python -m pytest tests/test_pins.py -v` **before** implementing and watched them fail
- [x] Implemented `test_every_dependency_is_exactly_pinned` — its failure message names the offending spec
- [x] Implemented `test_python_requirement_is_exact`
- [x] Implemented `test_classify_detects_a_major_bump` — runs offline
- [x] Implemented the `@pytest.mark.live` test, and wrote the comment explaining the drift threshold chosen
- [x] Confirmed the live test is **skipped** by `uv run python -m pytest -m "not live"`
- [x] **Break it, watch it go red, fix it —** changed a pin to `>=`, saw the pin test go red, restored it
- [x] **Break it, watch it go red, fix it —** changed `requires-python` to `>=3.12`, saw that test go red, restored it
- [x] **Break it, watch it go red, fix it —** made `classify` always return `'patch'`, saw that test go red, restored it
- [x] `./m check` is green

## Budget

- [x] **0** LLM API calls today
- [x] Network requests were to `pypi.org` only, each with a timeout and a named `User-Agent`
- [x] A second run of `check_pins.py` used the cache and made **no** requests
- [x] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [x] What a major bump promises, in which direction the promise runs, and who enforces it
- [x] Why `requests==2.31.0` is right in a service and harmful in a library
- [x] Why an environment cannot hold two versions of one package, and what that implies for installs
- [x] The three meanings of "latest", and which one a pin wants
- [x] PEP 592's rule, and why this project's pinning style is the one it singles out
- [x] What `--locked` does that `--frozen` does not
- [x] How you would compute the allowed Python versions from scratch, and why you pick one with room above it
- [x] Why a silent breaking change costs more than a loud one
- [x] Which principle is detection and which is response, and why neither works alone
- [x] What clause 4 of *Semantic Versioning 2.0.0* says about `0.y.z`, and what that does to every `~=` you write against a young package
- [x] How *PEP 440* defines `~=`, and why `~=2.2` and `~=2.2.1` are different bets

## Commit

- [x] `git status --porcelain` read **before** staging
- [x] `pyproject.toml` and `uv.lock` are both staged, in the same commit
- [x] `.pins-cache.json` does **not** appear in `git status`
- [x] `uv run python scripts/depth_check.py 1` passes
- [x] `./m done 1` ran green and created the commit
