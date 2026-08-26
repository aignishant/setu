---
day: 3
phase: 0
phase_name: "Foundry"
title: "Day 3 — Foundry III: three free keys, two free databases, one rate budget"
ids: []
principles: ["P1 build daily", "P2 from scratch before library", "P4 pin everything", "P5 zero budget", "P7 evals before features", "P9 data has provenance", "P11 blast radius", "P13 weekly freshness check", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: gate
plan: setu
plan_version: "v2.3.0"
parts: 13
generated: "2026-08-24"
status: complete
lab_scaffolded: false
commit: "badea4a"
---

# Day 3 — Foundry III: three free keys, two free databases, one rate budget

**Phase 0 · Foundry · GATE DAY** · No curriculum IDs. This is the day the plan's Phase 0 gate is
satisfied: *repo + pins frozen + `./m check` green + three free keys answering.* The last clause is
today, and the word is **answering**, not obtained.

> **Yesterday:** four gates — lint, format, offline tests, depth — and the same four in CI, where
> nothing may be spent.
> **Today:** five credentials, four model doors, two databases, and one script that proves every one
> of them answers without printing a single secret.
> **Tomorrow:** Phase 1 opens — objects, types and mutability, and the first day of Module 1.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere —
> a day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

There is a version of today that goes badly, and it is worth seeing before the version that goes well.

Someone signs up for three services, copies five credentials into a file, and pastes one of them into
a public commit while tidying up. Nine minutes later somebody else is using it. They delete the line
and commit the deletion, which does nothing at all, because the value is still in the previous commit
and in every clone anybody made.

Elsewhere in the same week, a job that summarises long documents fails after eight calls. Eight. The
allowance is thousands a day. The number in the error is not a request count at all — it is tokens per
minute, and each of those eight calls carried thirty thousand tokens of document. They add a pause
between calls, which is the fix for a completely different problem, and it does not help.

Meanwhile a retry loop somewhere is retrying a *daily* limit every second, for five hours, achieving
nothing but load. And a database connection times out repeatedly, so they regenerate the password
three times before discovering that the password was never the problem: their home IP address changed
overnight and a blocked address does not say "denied", it says nothing at all.

Four failures, four wrong first guesses, and one shared cause. **Every one of them is somebody meeting
a documented, predictable behaviour of a free service and treating it as a mystery**, because nobody
had told them the behaviour existed.

Today tells you. Secrets live in the environment and never in git, because git's whole purpose is to
remember forever and hand out copies — so the only fix for a committed key is revocation, and the
blast radius of a leak was decided when you created the credential, not when you lost it. A provider
has several limits at once, counting different things, and the one that binds you depends on the shape
of your work rather than on the provider's generosity. A correct retry is narrow, exponential,
jittered and bounded, and leaving out the jitter is how two hundred careful clients turn a slow service
into a dead one. A managed free database pauses when idle and blocks unknown addresses silently, so a
wake-and-retry is a feature and a timeout is not a password problem.

And underneath all of it, the habit that makes the rest work: **measure what you actually consumed,
every run, and compare it with what you predicted.** A budget nobody checks goes stale one reasonable
change at a time, and the first anybody hears of it is an allowance running out during unrelated work.

The day ends with one command that opens every door and prints a report you could paste in public.

```mermaid
flowchart LR
    S1["§1 secrets<br/>never in git"] --> S2["§2 four doors<br/>naked calls"]
    S2 --> S3["§3 two databases<br/>pause · allowlist"]
    S3 --> S4["§4 the budget<br/>limits · backoff · receipt"]
    S4 --> S5["§5 the gate<br/>one command, real evidence"]
    style S1 fill:#1f6feb,color:#fff
    style S5 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** This is a `gate` day, so the sections are the *acceptance
criteria of Phase 0*, in the order they must be satisfied: **1.x** the credentials can be held safely,
**2.x** every model door answers, **3.x** both databases answer, **4.x** the consumption is understood
and bounded, **5.x** all of it proved by one command.

### Section 1 — holding a secret

| Part | What it answers | Level |
|---|---|---|
| [1.1 What a secret is, and why it never enters git](parts/01-secrets/1.1-what-a-secret-is.md) | Why is deleting a committed key not a fix? | `foundation` |
| [1.2 `.env`, `python-dotenv`, and `os.environ`](parts/01-secrets/1.2-dotenv-and-os-environ.md) | Why must code read the environment rather than the file? | `working` |
| [1.3 When a key leaks — rotation, history, and blast radius](parts/01-secrets/1.3-when-a-key-leaks.md) | What decides how bad a leak is, and when was that decided? | `production` |

### Section 2 — the four model doors

| Part | What it answers | Level |
|---|---|---|
| [2.1 Gemini — the workhorse door](parts/02-llm-doors/2.1-gemini-the-workhorse.md) | Why write a raw provider call before touching a framework? | `working` |
| [2.2 Groq — the fast door and its token wall](parts/02-llm-doors/2.2-groq-and-the-token-wall.md) | How can a *faster* provider cause a failure a slower one would not? | `working` |
| [2.3 OpenRouter — the second opinion, and a roster that perishes](parts/02-llm-doors/2.3-openrouter-perishable-free.md) | What do you do when the thing you pinned is not yours to pin? | `production` |
| [2.4 Ollama — the door that needs no key](parts/02-llm-doors/2.4-ollama-the-keyless-door.md) | Why is RAM a categorically different ceiling from a rate limit? | `production` |

### Section 3 — the two databases

| Part | What it answers | Level |
|---|---|---|
| [3.1 Supabase — a Postgres that pauses](parts/03-databases/3.1-supabase-a-postgres-that-pauses.md) | Why is a wake-and-retry a feature rather than a workaround? | `working` |
| [3.2 MongoDB Atlas M0 — 512 MB and an allowlist](parts/03-databases/3.2-mongodb-atlas-m0.md) | Why does a blocked address time out instead of being refused? | `working` |

### Section 4 — the rate budget

| Part | What it answers | Level |
|---|---|---|
| [4.1 RPM, RPD, TPM — the three limits](parts/04-rate-budget/4.1-rpm-rpd-tpm.md) | Two people, same tier, same day: why do their 429s need opposite fixes? | `foundation` |
| [4.2 429, and the backoff that is not a busy loop](parts/04-rate-budget/4.2-429-and-real-backoff.md) | Which line does almost every retry loop omit, and what does it cost? | `production` |
| [4.3 The request budget as a receipt](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md) | How does a correct estimate become wrong without anybody being wrong? | `production` |

### Section 5 — the gate

| Part | What it answers | Level |
|---|---|---|
| [5.1 The Phase 0 gate — one command that proves every door](parts/05-the-gate/5.1-the-phase-0-gate.md) | When should a gate stop at the first failure, and when must it not? | `production` |

---

## §3 Setup — run this

Five packages arrive today, each on the day it is first genuinely used, each pinned exactly. The
versions below come from the plan's Part 2 table, read from the index on **2026-08-21** — which makes
them a starting point rather than gospel. Run Day 1's tool afterwards and believe it over this page.

```bash
uv add "google-genai==2.19.0" "groq==1.6.0" "openai==3.3.1" "psycopg[binary]==3.3.4" "pymongo==4.17.0"

# Day 1's tool is the authority on whether those pins are still current, not this lesson.
uv run python scripts/check_pins.py; echo "drift exit: $?"

# the shape is committed; the values never are (part 1.1)
printf '%s\n' \
  '# Copy to .env and fill in. NEVER commit .env.' \
  'GEMINI_API_KEY=' \
  'GROQ_API_KEY=' \
  'OPENROUTER_API_KEY=' \
  'SUPABASE_DB_URL=' \
  'MONGODB_URI=' \
  > .env.example

# create .env EMPTY and confirm git ignores it BEFORE pasting anything into it
touch .env
git check-ignore -q .env && echo "SAFE: git will ignore .env" || echo "STOP: fix .gitignore first"

mkdir -p scripts tests
touch scripts/gate.py tests/test_keys.py
```

| What | Where it comes from | Part |
|---|---|---|
| `python-dotenv` | already pinned, since Day 0 | [1.2](parts/01-secrets/1.2-dotenv-and-os-environ.md) |
| `google-genai` | Gemini's own SDK | [2.1](parts/02-llm-doors/2.1-gemini-the-workhorse.md) |
| `groq` | Groq's own SDK | [2.2](parts/02-llm-doors/2.2-groq-and-the-token-wall.md) |
| `openai` | a client for the chat-completions protocol, **pointed at OpenRouter** | [2.3](parts/02-llm-doors/2.3-openrouter-perishable-free.md) |
| `psycopg[binary]` | Postgres driver — version **3**, not `psycopg2` | [3.1](parts/03-databases/3.1-supabase-a-postgres-that-pauses.md) |
| `pymongo` | MongoDB driver | [3.2](parts/03-databases/3.2-mongodb-atlas-m0.md) |
| Ollama | a **system** binary, not a Python package — optional | [2.4](parts/02-llm-doors/2.4-ollama-the-keyless-door.md) |

Then create the accounts, in this order, because the order avoids the failures:

1. **Gemini** — an API key from the AI Studio console. Free tier only; no billing attached.
2. **Groq** — a key from the console.
3. **OpenRouter** — a key, then **list the free model ids yourself** ([2.3](parts/02-llm-doors/2.3-openrouter-perishable-free.md)); do not take one from a lesson.
4. **Supabase** — a free project, then copy the **database** connection string (not the REST URL).
5. **MongoDB Atlas** — a free M0 cluster, then **a dedicated database user** (not the admin), then **add your current IP to the allowlist**, then copy the string.

Steps 4 and 5's sub-steps are the ones people skip, and skipping either produces a failure that looks
like something else entirely.

---

## §4 Build brief

Three files are yours. The parts contain every technique; assembling them is the rep, and the
`TODO(me)` bodies are deliberately unsolved.

**1. `scripts/gate.py`** — the Phase 0 gate from [5.1](parts/05-the-gate/5.1-the-phase-0-gate.md). It
must check all six doors, gather every failure rather than stopping at the first, print a receipt, and
never emit any part of any credential.

```python
"""Prove every Phase 0 door answers. Prints no secrets, ever.

    uv run python scripts/gate.py

Exit status: 0 when every REQUIRED door answered, 1 otherwise. Optional doors are
reported and never block.
"""

from __future__ import annotations

import sys

from dotenv import load_dotenv

load_dotenv()

# (name, required, env_var or None, probe)
DOORS = [
    ("gemini", True, "GEMINI_API_KEY", None),
    ("groq", True, "GROQ_API_KEY", None),
    ("openrouter", True, "OPENROUTER_API_KEY", None),
    ("supabase", True, "SUPABASE_DB_URL", None),
    ("mongodb", True, "MONGODB_URI", None),
    ("ollama", False, None, None),
]


def probe_gemini() -> str:
    # TODO(me): part 2.1. One minimal call. Return a SHORT, SAFE summary -
    # the model id and the truncated reply, repr'd so an empty answer is visible.
    raise NotImplementedError


def probe_groq() -> str:
    # TODO(me): part 2.2. Note the different call shape and the different
    # place the text lives. Return the model id and the reply.
    raise NotImplementedError


def probe_openrouter() -> str:
    # TODO(me): part 2.3. Use the model id YOU listed from the live catalogue,
    # and record the date you chose it in a comment.
    raise NotImplementedError


def probe_supabase() -> str:
    # TODO(me): part 3.1. SELECT current_user, current_database(). Return the
    # HOSTNAME only - never the connection string. Report current_user: it is
    # the blast radius of the credential you just used.
    raise NotImplementedError


def probe_mongo() -> str:
    # TODO(me): part 3.2. admin.command("ping"), short serverSelectionTimeoutMS
    # so an allowlist failure is fast rather than mysterious. close() in finally.
    raise NotImplementedError


def probe_ollama() -> str:
    # TODO(me): part 2.4. Optional door. localhost, no key. A long timeout -
    # a small model on a laptop is genuinely slow.
    raise NotImplementedError


def run_all() -> list:
    # TODO(me): part 5.1. Run every door through the `timed` helper so ONE
    # exotic failure cannot lose the run. Gather - do not stop at the first
    # failure - and explain in a comment why this is the opposite choice
    # from ./m check's ordering.
    raise NotImplementedError


def report(results: list) -> int:
    # TODO(me): part 5.1. A column per field, a receipt line, and an exit code
    # derived from blocks_the_phase so the code and the report cannot disagree.
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(report(run_all()))
```

**2. Add `gate` to `./m`.** A new branch in the `case` dispatcher from
[Day 0, 3.2](../day-00-setup/parts/03-m-script/3.2-the-case-dispatcher.md), so the gate is one word:

```bash
  gate)
    uv run python scripts/gate.py
    ;;
```

Then answer, in a comment: should `./m check` call `./m gate`? Write down your reasoning. (It should
not — `./m check` runs in CI, and the gate makes live calls. That is
[Day 2, 5.3](../day-02-quality-gate/parts/05-ci/5.3-caching-and-never-spending-a-quota.md), and your
comment should say so.)

**3. `src/setu/config.py`** — the small module every later day imports for credentials, from
[1.2](parts/01-secrets/1.2-dotenv-and-os-environ.md). `require`, `optional`, and a
`which_keys_are_present` that returns booleans keyed by name and can never return a value. This one is
short and it is the first thing you write into `src/setu/` — Principle 6's graduation, on day three.

---

## §5 The eval that must be able to fail

Create `tests/test_keys.py`. The first three run offline and belong in `./m check`; the fourth is
marked `live` and never runs in CI.

```python
"""Day 3: prove the secrets are handled safely and the budget rules are mechanical."""

from __future__ import annotations

import os
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_VARS = (
    "GEMINI_API_KEY",
    "GROQ_API_KEY",
    "OPENROUTER_API_KEY",
    "SUPABASE_DB_URL",
    "MONGODB_URI",
)


def test_env_example_lists_every_variable_with_no_values() -> None:
    """The shape is committed; the values never are. Part 1.1."""
    # TODO(me): read .env.example, assert every name in REQUIRED_VARS appears,
    # and assert NO line has a non-empty value after the '='. A placeholder
    # that is a real key is exactly how these get committed.
    raise NotImplementedError


def test_no_credential_is_tracked_or_was_ever_committed() -> None:
    """Part 1.1: git is the authority, not .gitignore."""
    # TODO(me): assert `git check-ignore .env` succeeds, assert `git ls-files`
    # contains no .env/.pem/.key, and search `git rev-list --all` for a
    # long quoted token. Use subprocess; put the offending path in the message.
    raise NotImplementedError


def test_classify_distinguishes_a_daily_limit_from_a_per_minute_one() -> None:
    """The pure decision function from part 4.2, tested with no network."""
    from gate import classify  # or wherever you put it

    # TODO(me): assert a 429 body mentioning "requests per day" is NOT
    # retryable, that a 429 saying "try again in 3s" IS and returns 3.0,
    # that a 503 is, and that a 401 is not. Most specific condition first.
    raise NotImplementedError


@pytest.mark.live
def test_every_required_door_answers() -> None:
    """The Phase 0 gate, as a test. Skipped by default; never runs in CI."""
    # TODO(me): import run_all from scripts/gate.py, run it, and assert no
    # result has blocks_the_phase set. Put the closed door names in the
    # assertion message. Then write a comment explaining why this test must
    # carry @pytest.mark.live (Day 2, part 3.3).
    raise NotImplementedError
```

Run them and watch all four fail before you write a line:

```bash
uv run python -m pytest tests/test_keys.py -v            # 3 fail, 1 skipped
uv run python -m pytest tests/test_keys.py -v -m live    # the door check
```

Then implement, then **break each one on purpose**:

- Put a fake value after `GEMINI_API_KEY=` in `.env.example` → the first test goes red. Restore it.
- `git add -f .env` (do **not** commit) → the second test goes red. `git restore --staged .env`.
- Make `classify` return `(True, None)` for everything → the third goes red, because a daily limit is
  now retryable. Restore it.
- Rename `GROQ_API_KEY` in `.env` → the `live` test goes red and names `groq`. Restore it.

And the one with no test attached, which is the day's most valuable five minutes: **run the revocation
drill from [1.3](parts/01-secrets/1.3-when-a-key-leaks.md).** Create a second, throwaway key; make it
work; revoke it in the console; run the gate again and **write down the exact error text**. That is
what a revoked key looks like at eleven at night, months from now.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **about 12** — a handful while reading section 2, one per door in the gate, plus the revocation drill. Every one is a few dozen tokens. |
| Network requests | the three provider endpoints, the OpenRouter catalogue, one address lookup, plus package downloads |
| Database connections | one per store; both free tiers, both pinged and closed |
| Free-tier quota | a negligible fraction of one day's allowance on each door — but **count it**, because [4.3](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md) is about the habit, not the number |
| Cost | **$0** (Principle 5) — no card on file, on any of the five services |

**Actual, measured 2026-08-26** — and it disagrees with the estimate, so here is the note
[4.3](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md) asks for:

| Resource | Estimated | Actual | Why |
|---|---|---|---|
| LLM API calls | about 12 | **0** | No provider account exists yet, so no hosted door has been opened. The three model probes are written and their call shapes were checked against the installed SDKs, but nothing has been sent. |
| Network requests | provider endpoints + catalogue + packages | **~40** | 18 to `pypi.org` for the nine pins, 1 to the OpenRouter catalogue (public, no key), the rest package downloads for the five new dependencies. |
| Database connections | one per store | **0** | Same reason: no connection string. |
| Free-tier quota | a negligible fraction | **none** | Nothing was spent because nothing was called. |
| Cost | $0 | **$0** | Principle 5 holds trivially. |

**What this means for the gate.** `./m gate` currently exits **1**, reporting all five required
doors as `ABSENT` — never configured, as distinct from configured-and-broken. That is the honest
state, and it is the state the gate was built to report. Phase 0's last clause — *three free keys
answering* — is **not yet satisfied**. It becomes satisfied the moment five values land in `.env`
and `./m gate` exits 0; nothing else has to change. Until then, the revocation drill in
[1.3](parts/01-secrets/1.3-when-a-key-leaks.md) is also still outstanding, because you cannot
revoke a key you never created.

Write what the day *actually* cost next to this table when you finish. If it disagrees with the
estimate, the estimate is what changes, with a note saying why — that is the whole of
[4.3](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md) in one instruction.

**One hard rule, from [2.1](parts/02-llm-doors/2.1-gemini-the-workhorse.md):** free-tier prompts may be
used to improve a provider's models. **Fixtures and public data only, ever.** No private data through
any hosted door in this project — that is what the local door in
[2.4](parts/02-llm-doors/2.4-ollama-the-keyless-door.md) is for.

---

## §7 Traps

- **Pasting a key into `.env` before confirming git ignores it.** Check first; the check is free and
  the mistake is not — [1.1](parts/01-secrets/1.1-what-a-secret-is.md).
- **"Fixing" a committed key by deleting the line.** It is still in the previous commit and in every
  clone. Revoke — [1.1](parts/01-secrets/1.1-what-a-secret-is.md), [1.3](parts/01-secrets/1.3-when-a-key-leaks.md).
- **Printing the first eight characters of a key to check it loaded.** Print a *hash* prefix, or the
  length — [1.3](parts/01-secrets/1.3-when-a-key-leaks.md).
- **Opening `.env` in code instead of reading `os.environ`.** It works locally and breaks everywhere
  else — [1.2](parts/01-secrets/1.2-dotenv-and-os-environ.md).
- **Giving a secret a default.** That default gets committed and one day it is real —
  [1.2](parts/01-secrets/1.2-dotenv-and-os-environ.md).
- **Believing `"false"` is falsy.** Everything in the environment is a string —
  [1.2](parts/01-secrets/1.2-dotenv-and-os-environ.md).
- **Letting a framework choose the model.** Type it out, every call —
  [2.1](parts/02-llm-doors/2.1-gemini-the-workhorse.md).
- **Assuming the three SDKs share a call shape.** Two of three do, which is why people assume it —
  [2.2](parts/02-llm-doors/2.2-groq-and-the-token-wall.md), [2.3](parts/02-llm-doors/2.3-openrouter-perishable-free.md).
- **Copying a `:free` model id out of a lesson.** List them yourself, and record the date —
  [2.3](parts/02-llm-doors/2.3-openrouter-perishable-free.md).
- **Pacing a loop that is hitting a *token* limit.** Wrong fix for that shape —
  [4.1](parts/04-rate-budget/4.1-rpm-rpd-tpm.md).
- **Making a second key to get more quota.** Limits are usually per organisation —
  [4.1](parts/04-rate-budget/4.1-rpm-rpd-tpm.md).
- **Retrying a daily 429.** Five and a half hours of achieving nothing —
  [4.2](parts/04-rate-budget/4.2-429-and-real-backoff.md).
- **Backoff with no jitter.** Two hundred careful clients returning in unison —
  [4.2](parts/04-rate-budget/4.2-429-and-real-backoff.md).
- **Retrying anything that writes without asking whether it is idempotent** —
  [4.2](parts/04-rate-budget/4.2-429-and-real-backoff.md).
- **Counting successes instead of attempts in a budget.** Retries are requests —
  [4.3](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md).
- **Regenerating a database password when the real problem is an IP allowlist.** A blocked address
  times out; it is not refused — [3.2](parts/03-databases/3.2-mongodb-atlas-m0.md).
- **Using the Atlas admin user for the application.** Blast radius, decided at creation —
  [1.3](parts/01-secrets/1.3-when-a-key-leaks.md), [3.2](parts/03-databases/3.2-mongodb-atlas-m0.md).

---

## §8 Verify before you code

Written **2026-08-24**, against these pages, read live rather than recalled. The call shapes and model
ids in section 2 come from the first three — **re-check them before you rely on them**, because a
model id in a lesson is exactly the kind of fact that decays
([Day 1, 4.2](../day-01-pins/parts/04-drift/4.2-drift-and-the-amendment-protocol.md)):

- <https://ai.google.dev/gemini-api/docs/quickstart> — the client, the Interactions API, the default
  environment variable name.
- <https://ai.google.dev/gemini-api/docs/text-generation> — the current recommended call shape and
  model ids.
- <https://console.groq.com/docs/quickstart> — the client and the chat-completions call.
- <https://openrouter.ai/docs/quickstart> — the `base_url`, and using the chat-completions SDK against
  it.
- <https://ai.google.dev/gemini-api/docs/rate-limits> · <https://console.groq.com/docs/rate-limits> ·
  <https://openrouter.ai/docs/api-reference/limits> — today's numbers, for
  [4.1](parts/04-rate-budget/4.1-rpm-rpd-tpm.md). Write them into your lab notes with today's date.
- <https://www.psycopg.org/psycopg3/docs/> — `psycopg` **3**, not `psycopg2`.
- <https://pymongo.readthedocs.io/> — the client, `serverSelectionTimeoutMS`, and the `+srv` scheme.

**One thing to flag rather than silently absorb** (Principle 14): the plan's Part 2 pins table was read
from the index on 2026-08-21 and lists `google-genai==2.19.0`, while the SDK's current documented entry
point is the Interactions API. If `scripts/check_pins.py` shows drift on any of today's five packages,
that is a **plan amendment** to write in `docs/CHANGELOG_PLAN_DS.md`, not a pin to quietly bump.

---

## §9 Say it in an interview

> "Every credential lives in the environment and never in version control — the ignore rules were
> written before any secret existed, because ignoring a file doesn't help once git is already tracking
> it, and the only real fix for a committed key is revocation, not history rewriting. Each key is
> scoped to one purpose on a free tier with no billing attached, so the blast radius of a leak is a
> spent daily allowance rather than a bill; that's a decision made when the credential is created,
> because you can't shrink it afterwards. On the client side I estimate before I build: measure one
> real call, project requests and tokens per minute, and compare against each published limit —
> because the fix for a request-rate limit is pacing and the fix for a token limit is sending less, and
> both arrive as the same 429. Retries are narrow, exponential, jittered and bounded, and I check
> idempotency before retrying anything that writes. Then every run prints what it actually consumed —
> attempts, not successes, since retries are requests — so when a correct estimate goes stale one
> reasonable change at a time, the drift shows up in week one instead of on the morning the quota runs
> out. And the whole setup is proved by one command that opens every door for real and prints a report
> I could paste in public, because a credential that was pasted but never used isn't a working
> credential."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and `./m gate` exits **0**
with every required door reporting `OK` — not when a particular amount of time has passed. Then:

```bash
./m gate; echo "gate exit: $?"
./m done 3
```

That is Phase 0 complete: repo, pins frozen, `./m check` green, and every door answering. Tomorrow
Phase 1 opens with Module 1 — objects, types, and the mutability trap that has bitten every Python
programmer exactly once.
