# Day 1 — CHECKLIST

**IDs covered:** none (Foundry) · **Principles served:** 4, 7, 13, 14, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 11, in [`parts/`](parts/)

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

- [ ] Read [1.1 — semantic versioning](parts/01-versions/1.1-semantic-versioning.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — version specifiers](parts/01-versions/1.2-version-specifiers.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — the resolution problem](parts/01-versions/1.3-the-resolution-problem.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Watched `sorted(['1.9.0','1.10.0'])` put `1.9.0` last, and `sorted(..., key=Version)` fix it
- [ ] **Predicted all four answers** in 1.2's check-yourself before running it — and was right about `~=3.0` vs `~=3.0.5`
- [ ] Ran `uv tree` and counted the packages nobody declared
- [ ] Forced a resolution conflict on purpose and identified its two premises and conclusion

## Section 2 — reading the truth from the index

- [ ] Read [2.1 — PyPI's JSON API](parts/02-pypi-index/2.1-the-pypi-json-api.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — yanked and pre-release](parts/02-pypi-index/2.2-yanked-and-prerelease.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — the check-pins script](parts/02-pypi-index/2.3-the-check-pins-script.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Fetched a package's metadata with `urllib.request` — with a `User-Agent` **and** a `timeout`
- [ ] Listed the deprecated top-level keys the server still returns, and can say why using them is a bug
- [ ] Printed "newest published" and "newest stable" for a package and understand when they differ
- [ ] Checked the `yanked` flag on a specific release, not just `info.version`
- [ ] Can state PEP 592's rule about which specifiers still install a yanked file
- [ ] Ran a loop where one package 404s and the others still get checked

## Section 3 — freezing it

- [ ] Read [3.1 — the Python-version intersection](parts/03-freezing/3.1-the-python-version-intersection.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — freezing into pyproject and the lock](parts/03-freezing/3.2-freezing-into-pyproject-and-the-lock.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — regenerating pins from evidence](parts/03-freezing/3.3-regenerating-pins-from-evidence.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Computed** the allowed interpreter set by intersecting `requires_python` — did not read it off a table
- [ ] The computed set still contains **3.12**; if it does not, wrote an addendum instead of editing a pin
- [ ] Identified which package supplies the floor and which supplies the ceiling
- [ ] Broke `pyproject.toml` on purpose and watched `uv lock --check` and `uv sync --locked` refuse
- [ ] **Watched `uv sync --frozen` pass on the same broken state** — and can explain why that is not a bug
- [ ] Restored it and confirmed `uv lock --check` exits 0
- [ ] Ran `uv lock --upgrade-package <name>` and looked at how small the diff is

## Section 4 — keeping it frozen

- [ ] Read [4.1 — the three breaking changes](parts/04-drift/4.1-the-three-breaking-changes.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — drift and the amendment protocol](parts/04-drift/4.2-drift-and-the-amendment-protocol.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Found every ⚠️ marker in `docs/PINS_DS.md` and the plan, and can say what each one is warning about
- [ ] Can name the difference between a **loud** and a **silent** breaking change, with an example of each
- [ ] Read this repository's own amendment in `docs/CHANGELOG_PLAN_DS.md` and found its four parts
- [ ] Drafted a drift entry using the template, even though there is nothing to record yet

---

## Build brief — the reps that are yours

- [ ] Created `scripts/check_pins.py` from the skeleton in the hub's §4
- [ ] Implemented `read_pins` — reads **every** dependency group, not just `dev`
- [ ] Implemented `fetch_current` — timeout, `User-Agent`, filters pre-releases, reads `yanked`
- [ ] Implemented `classify` — a **pure** function, no network, most specific condition first
- [ ] Implemented `main` — per-package `try` **inside** the loop, exit 1 on drift
- [ ] Added the cache with an expiry, and confirmed a second run makes no network requests
- [ ] Added `--markdown` and `--json` output modes, with data on stdout and chatter on stderr
- [ ] Added `.pins-cache.json` to `.gitignore`
- [ ] Regenerated the table in `docs/PINS_DS.md` and set `verified:` to today
- [ ] **Left the authored "Python version reasoning" section alone** — generated the fact, kept the judgement

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_pins.py -v` **before** implementing and watched them fail
- [ ] Implemented `test_every_dependency_is_exactly_pinned` — its failure message names the offending spec
- [ ] Implemented `test_python_requirement_is_exact`
- [ ] Implemented `test_classify_detects_a_major_bump` — runs offline
- [ ] Implemented the `@pytest.mark.live` test, and wrote the comment explaining the drift threshold chosen
- [ ] Confirmed the live test is **skipped** by `uv run python -m pytest -m "not live"`
- [ ] **Break it, watch it go red, fix it —** changed a pin to `>=`, saw the pin test go red, restored it
- [ ] **Break it, watch it go red, fix it —** changed `requires-python` to `>=3.12`, saw that test go red, restored it
- [ ] **Break it, watch it go red, fix it —** made `classify` always return `'patch'`, saw that test go red, restored it
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] Network requests were to `pypi.org` only, each with a timeout and a named `User-Agent`
- [ ] A second run of `check_pins.py` used the cache and made **no** requests
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] What a major bump promises, in which direction the promise runs, and who enforces it
- [ ] Why `requests==2.31.0` is right in a service and harmful in a library
- [ ] Why an environment cannot hold two versions of one package, and what that implies for installs
- [ ] The three meanings of "latest", and which one a pin wants
- [ ] PEP 592's rule, and why this project's pinning style is the one it singles out
- [ ] What `--locked` does that `--frozen` does not
- [ ] How you would compute the allowed Python versions from scratch, and why you pick one with room above it
- [ ] Why a silent breaking change costs more than a loud one
- [ ] Which principle is detection and which is response, and why neither works alone

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `pyproject.toml` and `uv.lock` are both staged, in the same commit
- [ ] `.pins-cache.json` does **not** appear in `git status`
- [ ] `uv run python scripts/depth_check.py 1` passes
- [ ] `./m done 1` ran green and created the commit
