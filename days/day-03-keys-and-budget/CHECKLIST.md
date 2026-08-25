# Day 3 — CHECKLIST

**IDs covered:** none (Foundry · **GATE DAY**) · **Principles served:** 1, 2, 4, 5, 7, 9, 11, 13, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 3` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, `./m check` green, and `./m gate`
> exiting 0 with every required door `OK`.

## Demo command

```bash
./m gate; echo "gate exit: $?"; ./m check
```

Expected: every required door reports **OK**, a receipt line prints, the gate exits **0**, and
`./m check` is green. **No character of any credential appears anywhere in that output.**

---

## Section 1 — holding a secret

- [x] Read [1.1 — what a secret is](parts/01-secrets/1.1-what-a-secret-is.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.2 — `.env` and `os.environ`](parts/01-secrets/1.2-dotenv-and-os-environ.md), ran its check-yourself, answered its out-loud question
- [x] Read [1.3 — when a key leaks](parts/01-secrets/1.3-when-a-key-leaks.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Ran `git check-ignore -v .env` and read **which rule and line number** protects you
- [x] Confirmed `.env.example` is **not** ignored, and understand the `!` rule that re-includes it
- [x] Created `.env` **empty** and confirmed it was ignored **before** pasting any value into it
- [x] Searched `git rev-list --all` for credential-shaped strings and found none
- [x] Can name a secret that no `.env` rule would ever catch (a connection string in a source file)
- [x] Watched a variable set for one command not exist afterwards, and a child fail to change its parent
- [x] Saw `bool("false")` return `True` and can say what to write instead
- [x] Saw `load_dotenv()` return `False` on a missing file **without raising**, and can say why that matters
- [x] Confirmed a shell-exported variable **beats** the `.env` file, and can say why that precedence is right
- [x] Printed key presence with a **hash** fingerprint and a length — never a prefix of the value
- [x] **Ran the revocation drill:** made a throwaway key, proved it worked, revoked it, and wrote down the exact error text

## Section 2 — the four model doors

- [x] Read [2.1 — Gemini](parts/02-llm-doors/2.1-gemini-the-workhorse.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.2 — Groq](parts/02-llm-doors/2.2-groq-and-the-token-wall.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.3 — OpenRouter](parts/02-llm-doors/2.3-openrouter-perishable-free.md), ran its check-yourself, answered its out-loud question
- [x] Read [2.4 — Ollama](parts/02-llm-doors/2.4-ollama-the-keyless-door.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Made a **raw** Gemini call with no framework, with the model id typed out
- [x] Ran `dir()` over the response object and **found where the token counts live**
- [x] Made a raw Groq call and can name three ways its shape differs from Gemini's
- [x] Measured one call's latency and projected its **tokens per minute** at full speed
- [x] Compared that projection against the provider's published TPM
- [x] **Listed OpenRouter's free model ids from the live catalogue** — did not copy one from the lesson
- [x] Wrote today's date next to the free model id chosen
- [x] Made a call through OpenRouter and can say why the installed package's name does not name its destination
- [x] Can state the rule about which provider an eval judge must run on
- [x] Did the RAM arithmetic for a 3B, 7B and 13B model before pulling anything
- [x] *(optional)* Pulled a small local model and got an answer with **no key anywhere**
- [x] *(optional)* Can name the local failure mode that is worse than an error

## Section 3 — the two databases

- [x] Read [3.1 — Supabase](parts/03-databases/3.1-supabase-a-postgres-that-pauses.md), ran its check-yourself, answered its out-loud question
- [x] Read [3.2 — MongoDB Atlas M0](parts/03-databases/3.2-mongodb-atlas-m0.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Installed `psycopg[binary]` — version **3** — and can say what the `[binary]` extra bought
- [x] Connected to Postgres and read `current_user` — and can state the blast radius of that credential
- [x] Wrote a `describe()` that redacts the password, and used it instead of printing the DSN
- [x] Can name the **one** exception class a wake-retry should catch, and two it must not
- [x] Created a **dedicated** Atlas database user, not the admin one
- [x] Added your current public IP to the allowlist, and **wrote the address down**
- [x] Pinged the cluster and read the storage figure against the 512 MB ceiling
- [x] Can explain why a blocked IP times out rather than being refused, and what that means for diagnosis order
- [x] Can give one question a document store answers better than a relational one, and one it answers worse

## Section 4 — the rate budget

- [x] Read [4.1 — RPM, RPD, TPM](parts/04-rate-budget/4.1-rpm-rpd-tpm.md), ran its check-yourself, answered its out-loud question
- [x] Read [4.2 — 429 and real backoff](parts/04-rate-budget/4.2-429-and-real-backoff.md), ran its check-yourself, answered its out-loud question
- [x] Read [4.3 — the budget as a receipt](parts/04-rate-budget/4.3-the-budget-as-a-receipt.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] **Wrote today's published limits into lab notes**, with today's date and the **scope** of each
- [x] Recorded "not published" where a dimension is not stated, rather than leaving it blank
- [x] Estimated two workload shapes and saw them breach **different** ceilings
- [x] Replaced the estimate's guesses with numbers measured from one real call
- [x] Can name the fix for a request-rate limit and the different fix for a token limit
- [x] Can say what a `400` context-length error means that a `429` does not
- [x] Printed an exponential schedule with and without jitter and compared them
- [x] Can name all four properties of a correct retry, and which one most code omits
- [x] Wrote a `classify` that returns **not retryable** for a daily 429
- [x] Built a receipt that counts **attempts**, not successes
- [x] Saw a run pass on totals and breach on **implied RPM** — and can say why totals alone mislead
- [x] Can state the question to ask before retrying anything that writes

## Section 5 — the gate

- [x] Read [5.1 — the Phase 0 gate](parts/05-the-gate/5.1-the-phase-0-gate.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [x] Can give the general rule that decides between failing fast and gathering, and why this gate gathers
- [x] Can say why `ABSENT` and `FAILED` are separate statuses and demand different actions
- [x] Broke one door on purpose and confirmed the **other five were still checked**
- [x] Confirmed a failing **optional** door does not change the exit code

---

## Build brief — the reps that are yours

- [x] Created `.env.example` with every variable name and **no values**, and committed it
- [x] Created `.env` with all five values, and confirmed it never appears in `git status`
- [x] Added all five packages with exact `==` pins, and committed `pyproject.toml` **and** `uv.lock` together
- [x] Ran `scripts/check_pins.py` afterwards and acted on what it said
- [x] If any of today's five pins drifted, **wrote a plan amendment** rather than quietly bumping it
- [x] Created `src/setu/config.py` with `require`, `optional`, and `which_keys_are_present`
- [x] `which_keys_are_present` returns **booleans keyed by name** and cannot return a value
- [x] Created `scripts/gate.py` from the skeleton in the hub's §4
- [x] Implemented all six probes, each importing its driver **inside** the function
- [x] Every probe returns a short summary containing **no credential**, and the Supabase one reports `current_user`
- [x] Implemented `run_all` — gathers, never stops at the first failure — with a comment on why
- [x] Implemented `report` — columns, a receipt line, exit code derived from `blocks_the_phase`
- [x] Added a `gate)` branch to `./m` and can run it as `./m gate`
- [x] Wrote down whether `./m check` should call `./m gate`, and why not

## The eval — it must be able to fail

- [x] Ran `uv run python -m pytest tests/test_keys.py -v` **before** implementing and watched them fail
- [x] Implemented `test_env_example_lists_every_variable_with_no_values`
- [x] Implemented `test_no_credential_is_tracked_or_was_ever_committed` — asks **git**, not `.gitignore`
- [x] Implemented `test_classify_distinguishes_a_daily_limit_from_a_per_minute_one` — runs offline
- [x] Implemented the `@pytest.mark.live` door test, with the comment explaining why it must be marked
- [x] Confirmed the live test is **skipped** by `uv run python -m pytest -m "not live"`
- [x] **Break it, watch it go red, fix it —** put a fake value in `.env.example`, saw test one go red, restored it
- [x] **Break it, watch it go red, fix it —** `git add -f .env` (uncommitted), saw test two go red, unstaged it
- [x] **Break it, watch it go red, fix it —** made `classify` always retryable, saw test three go red, restored it
- [x] **Break it, watch it go red, fix it —** renamed a key in `.env`, saw the live test name that door, restored it
- [x] `./m check` is green

## Budget

- [x] Counted the LLM calls actually made today and wrote the number next to the hub's §6 table
- [x] If the actual differs from the estimate, **updated §6 with a note saying why**
- [x] No private data was sent through any hosted door — public fixtures only
- [x] **$0** spent; no card on file with any of the five services (Principle 5)
- [x] Confirmed no key was added to CI, and that `./m check` still makes zero provider calls

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [x] Why deleting a committed key changes nothing, and the one action that does
- [x] Why `.gitignore` had to be written on Day 0 rather than today
- [x] Why code reads `os.environ` rather than opening `.env`, using production as the reason
- [x] What decides how bad a leak is, and when that decision was made
- [x] Why you write a raw provider call before adopting a framework
- [x] How a faster provider causes a failure a slower one would not
- [x] Why the 404 on a withdrawn free model is the cheap failure, and what the expensive one is
- [x] Two reasons to run a model locally that are not about money
- [x] Why a `wake_db()` retry is a feature, and the one exception class it catches
- [x] Why a blocked IP times out instead of being refused
- [x] The four rate-limit dimensions, and the two fixes that are not interchangeable
- [x] The four properties of a correct retry, and what happens without jitter
- [x] Why a receipt counts attempts rather than successes
- [x] When a gate should fail fast and when it must gather

## Commit

- [x] `git status --porcelain` read **before** staging
- [x] `.env` does **not** appear anywhere in `git status`
- [x] `.env.example`, `scripts/gate.py`, `src/setu/config.py`, `tests/test_keys.py`, `m`, `pyproject.toml` and `uv.lock` staged together
- [x] `uv run python scripts/depth_check.py 3` passes
- [x] `./m gate` exits **0** with every required door `OK`
- [x] `./m done 3` ran green and created the commit
- [x] **Phase 0 is complete:** repo, pins frozen, `./m check` green, every door answering
