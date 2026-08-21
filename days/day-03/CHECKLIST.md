# Day 3 — CHECKLIST · **PHASE 0 GATE**

**IDs covered:** none (Phase-0 infrastructure) · **Principles served:** 5, 9, 13

## Demo command

```bash
uv run python days/day-03/lab/verify_keys.py
uv run python -m pytest -q
```

Expected: three `ok` lines with live rate-limit headers, then all tests green.

## Setup

- [ ] `./m start 3` and `./m scaffold 3` run
- [ ] `uv add "openai==<your pin>"` — appears in `pyproject.toml` and `uv.lock`
- [ ] Files created: `days/day-03/lab/verify_keys.py`, `src/setu/models.py`, `tests/test_models.py`, `docs/RATE_BUDGET_DS.md`
- [ ] `grep -n '^\.env$' .gitignore` printed **SAFE** *before* `.env` was created
- [ ] `cp .env.example .env` done

## Keys (Principle 5)

- [ ] Gemini account created; `GEMINI_API_KEY` in `.env`
- [ ] Groq account created; `GROQ_API_KEY` in `.env`
- [ ] OpenRouter account created; `OPENROUTER_API_KEY` in `.env`
- [ ] **No card on file at any of the three**
- [ ] `git status --porcelain` does **not** mention `.env`
- [ ] `git ls-files | grep '\.env$'` returns nothing (`.env.example` is fine)
- [ ] Read the Gemini training-data warning and wrote the data rule in your own words

## models.py

- [ ] `Provider` dataclass written, frozen
- [ ] `PROVIDERS` filled with all three base URLs
- [ ] `probe_model` for each filled **from the live console** — no `<placeholder>` remains
- [ ] `WORKHORSE`, `FAST_LOOP`, `JUDGE`, `OFFLINE` defined
- [ ] `JUDGE` is on a **different provider** from `WORKHORSE`
- [ ] `key_attr` stores a **name**, not a key — can explain why

## Verification

- [ ] `verify_keys.py` written and run **once**
- [ ] Three `ok` lines printed
- [ ] Rate-limit headers captured from the output
- [ ] Did **not** loop the script

## Rate budget (Principles 5, 9)

- [ ] `docs/RATE_BUDGET_DS.md` created with today's date
- [ ] RPM / RPD / TPM recorded per provider from the **live console**, not from this lesson
- [ ] Data rule written in your own words
- [ ] Ledger row added: `3 requests, day 3, verify_keys.py`

## Databases — provisioned now, used on Day 42

- [ ] Supabase project created; region chosen; URL + anon key + Postgres DSN in `.env`
- [ ] Understood that a free Supabase project **pauses when idle**
- [ ] MongoDB Atlas M0 cluster created; database user added; IP allowlisted
- [ ] `MONGODB_URI` in `.env`
- [ ] Did **not** connect from Python today

## Tests that must be able to fail

- [ ] `test_no_placeholder_model_ids` — was **red** before you filled the console values, now green (×3)
- [ ] `test_every_provider_has_an_https_base_url` — green
- [ ] `test_judge_is_a_different_provider_from_workhorse` — green (swap it temporarily, watch it go red)
- [ ] `test_no_key_material_in_the_module` — green

## Budget

- [ ] LLM calls today: **exactly 3**

## Understanding check — answer out loud

- [ ] Why is a free-tier wall a worse failure mode than a surprising invoice — and what does that change about design?
- [ ] Why does the `openai` library work against Groq and Gemini?
- [ ] What does `with_raw_response` buy you that a normal call does not?
- [ ] Why are the constants named `WORKHORSE` and `JUDGE` rather than `GEMINI` and `OPENROUTER`?
- [ ] Why must an eval judge run on a different provider from the model it grades?
- [ ] Why is the `except` in `verify_keys.py` broad while the one in `config.py` is narrow?
- [ ] What will you never send to a free tier, and why?

## Phase 0 gate

- [ ] Pins frozen with committed evidence (Day 1)
- [ ] `./m check` green (Day 2)
- [ ] CI green on a real push (Day 2)
- [ ] All three providers answering (today)
- [ ] Rate budget recorded (today)
- [ ] Both databases provisioned (today)
- [ ] `./m done 3` succeeded and `./m status` shows Phase 0 complete
