# Day 57 — CHECKLIST · **PHASE 7 GATE**

**IDs covered:** APP-08 · **Principles served:** 1, 5, 10, 11 · **Artifact:** a live URL + ADR-003

## Demo command

```bash
uv run streamlit run days/day-57/lab/deploy_check.py
uv run python -m pytest tests/test_app.py -v
```

Then: the deployed URL, opened in a **private window**.

## Setup

- [ ] `./m start 57` and `./m scaffold 57` run
- [ ] **`.streamlit/secrets.toml` added to `.gitignore` BEFORE the directory existed**
- [ ] Files created: `days/day-57/lab/deploy_check.py`, `.streamlit/config.toml`,
      `.streamlit/secrets.toml.example`, `docs/adr/ADR-003-app-boundary.md`

## APP-08 — configuration

- [ ] `config.toml` written with `headless`, `maxUploadSize`, telemetry off, theme
- [ ] `maxUploadSize` **matches** `MAX_UPLOAD_MB` from Day 53
- [ ] Can say why the limit must exist in two places
- [ ] `secrets.toml.example` committed with **names only**

## Secrets

- [ ] Ran the presence table; can say why it shows presence and never values
- [ ] Confirmed `git ls-files` contains no `.env` and no `secrets.toml`
- [ ] Know what to do if it ever does (**rotate**, not delete)
- [ ] Can state the three-source precedence for `get_secret`
- [ ] Can say why the Streamlit import in `config.py` must be guarded

## What a stranger can do

- [ ] Read §3 and can state all five posture points
- [ ] Can name the alternative posture and when it becomes the right one
- [ ] Confirmed no destructive helper is importable from `setu.app`

## The network

- [ ] Understood why the Day-3 IP access list stops working
- [ ] **Chose** one of the three Atlas options
- [ ] Can defend the choice, including the caveat if you chose `0.0.0.0/0`
- [ ] Recorded the decision in ADR-003

## Resources

- [ ] Can name all four free-tier constraints from §5
- [ ] Can say why cold start makes the health-panel-first rule matter

## Build brief

- [ ] `get_secret` — **TODO(me)**: three sources in order, guarded import, never leaks the value
- [ ] `running_deployed` — **TODO(me)**: does not raise without Streamlit
- [ ] `check_budget` — **TODO(me)**: pure, refuses the request that *would* exceed
- [ ] `deployment_report` — **TODO(me)**: presence only, never raises
- [ ] `assert_read_only` — **TODO(me)**: names what it found

## ADR-003 — the artifact (Principle 10)

- [ ] Written from `docs/adr/ADR-TEMPLATE.md`
- [ ] **Four options** considered, including a login and the app-as-API-client
- [ ] The three questions answered: **who can reach it · what can it do · whose quota**
- [ ] The Atlas network decision recorded with its reason
- [ ] **Decision** in one sentence
- [ ] **Consequences** says what changes the first time a write path appears
- [ ] **What would change our minds** is specific
- [ ] Cold-read a day later and signed

## Tests that must be able to fail

- [ ] `test_budget_allows_a_request_under_the_cap` — green
- [ ] `test_budget_refuses_over_the_cap` — green
- [ ] `test_budget_refuses_the_request_that_would_exceed` — green
- [ ] **Made the check off by one, watched it go red, fixed it** ← do not skip
- [ ] `test_budget_does_not_mutate_its_input` / `..._rejects_a_zero_cost` / `..._is_pure` — green
- [ ] `test_no_secrets_are_committed` — green ← **the most important test here**
- [ ] `test_secrets_example_has_no_values` — green
- [ ] `test_gitignore_covers_streamlit_secrets` — green
- [ ] `test_config_does_not_hard_import_streamlit` — green
- [ ] **Added a top-level `import streamlit` to config.py, watched the subprocess test go red, guarded it** ← do not skip
- [ ] `test_the_app_is_read_only` — green
- [ ] `test_read_only_check_detects_a_destructive_import` — green ← **today's real assessment**
- [ ] **Made `assert_read_only` a no-op, watched it go red, fixed it** ← do not skip
- [ ] `test_deployment_report_never_leaks_values` — green
- [ ] `test_deployment_report_is_json_serialisable` / `..._never_raises` — green
- [ ] `test_upload_limit_matches_the_platform_config` — green
- [ ] `test_adr_003_answers_the_three_questions` — green
- [ ] `test_phase_7_app_module_is_complete` — green (21 functions)

## Deploy

- [ ] `git status --porcelain` empty
- [ ] Dependencies pinned for the platform (`uv export` if a requirements.txt is needed)
- [ ] Deployed with entry point `app/Home.py`
- [ ] Secrets pasted into the platform UI
- [ ] Atlas decision applied
- [ ] **Opened the URL in a private window** and clicked everything
- [ ] Checked both database dashboards for the load you generated

## Budget

- [ ] LLM calls today: **0**
- [ ] Noted how many database round trips your own clicking cost

## Understanding check — answer out loud

- [ ] Name the three assumptions deployment breaks
- [ ] What is the precedence order for reading a secret, and why that order?
- [ ] Why must the Streamlit import in `config.py` be guarded?
- [ ] Why does your IP allowlist stop working, and what replaces it as a control?
- [ ] What can a stranger with the URL do, and what stops them doing more?
- [ ] When does a public app need a login rather than a budget?
- [ ] Why does a committed secret need rotating rather than deleting?
- [ ] Why must the upload limit exist in two places?

## PHASE 7 GATE

- [ ] A **live URL** you can send someone
- [ ] It renders: health panel, search form, a `setu.plots` chart, a table
- [ ] No secret committed, none rendered
- [ ] Read-only, with an enforced per-session budget
- [ ] Atlas decision made and recorded
- [ ] ADR-003 written and cold-read
- [ ] `test_phase_7_app_module_is_complete` green
- [ ] `app/Home.py` still under the line limit from Day 52
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 57` succeeded and `./m status` shows Phases 0–7 complete
