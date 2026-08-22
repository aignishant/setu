# Day 116 — CHECKLIST · **PHASE 13 GATE**

**IDs covered:** ML-29, ML-30 · **Principles served:** 1, 7, 8, 10, 15
**Artifacts:** a tracked experiment + a project report

## Demo command

```bash
uv run python days/day-116/lab/train.py
uv run python -m pytest tests/test_ensembles.py tests/test_clustering.py -v
uv run python -m pytest -q
```

Expected: the eight-part report ending with the production risks, then the whole suite green.

## Setup

- [ ] `./m start 116` and `./m scaffold 116` run
- [ ] `uv add "mlflow==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-116/lab/train.py`, `reports/day116_project_report.md`
- [ ] `mlruns/` added to `.gitignore`
- [ ] **`SOURCE.md` row added**, including how the attacks were generated

## ML-29 — tracking

- [ ] Ran `tracking_a_run()` and got a run ID
- [ ] Can name the **four** things every run must log
- [ ] Confirmed the **git SHA and dirty flag** are recorded
- [ ] Can say why params without the code reproduce nothing
- [ ] Can say how a dirty-tree run should be treated
- [ ] Read `what_to_log_and_what_not_to()`; can give three things never to log

## ML-30 — the split

- [ ] Ran `the_random_split_lies()` across three splits
- [ ] Recorded PR-AUC: random ______ grouped ______ temporal ______
- [ ] Recorded accuracy for all three
- [ ] Can say why the accuracy column is nearly useless
- [ ] Can explain **why** the random split is optimistic on this data
- [ ] Ran `the_split_that_matches_deployment()`
- [ ] Recorded rows in each test slice: known-host-later ______ unseen-host ______
- [ ] Can say why those slices must be reported separately

## The metric

- [ ] Recorded the constant predictor's accuracy: ______
- [ ] Recorded the PR-AUC baseline: ______
- [ ] Can say why ROC-AUC is misleadingly high here
- [ ] Stated `cost_fn` ______ and `cost_fp` ______ with reasons
- [ ] Computed the cost-optimal threshold: ______
- [ ] Can say what that threshold assumes about the probabilities

## The alert budget

- [ ] Ran `alert_budget_is_the_real_constraint()` at four budgets
- [ ] Recorded recall at 50 alerts/day ______ and 1,000/day ______
- [ ] Can say why the cost formula alone is insufficient
- [ ] Can state what makes a recall figure an operational claim

## The pipeline

- [ ] `train.py` runs in **one command** and exits 0
- [ ] Three temporal slices: train / validation / test
- [ ] Early stopping used the **validation** slice
- [ ] The reported number came from the **test** slice
- [ ] Baseline and lift logged **beside** the score
- [ ] `reports/day116_metrics.json` written with the git state

## Production risks

- [ ] Read `what_would_make_this_fail_in_production()`
- [ ] Can name all five
- [ ] Can explain alert fatigue and why it makes real recall zero
- [ ] Checked the host-signature features with SHAP (Day 114)

## Tests that must be able to fail

- [ ] `test_the_data_is_severely_imbalanced` — green
- [ ] `test_a_constant_predictor_scores_above_ninety_eight_percent` — green
- [ ] `test_the_random_split_is_optimistic` — green ← **today's real assessment**
- [ ] **Used a random split and watched PR-AUC inflate** ← do not skip
- [ ] `test_accuracy_hides_the_difference_the_random_split_makes` — green
- [ ] `test_no_host_straddles_the_grouped_split` — green
- [ ] `test_the_temporal_split_never_trains_on_the_future` — green
- [ ] `test_roc_auc_is_misleadingly_high_on_this_data` — green
- [ ] `test_the_pr_auc_baseline_is_the_positive_rate` — green
- [ ] `test_the_cost_optimal_threshold_is_far_from_a_half` — green
- [ ] `test_a_tighter_alert_budget_lowers_recall` — green
- [ ] `test_the_git_sha_is_recorded` — green
- [ ] `test_the_metrics_file_records_the_baseline_beside_the_score` — green
- [ ] `test_the_metrics_file_records_the_code_version` — green
- [ ] `test_mlruns_is_gitignored` — green
- [ ] `test_the_project_report_exists_and_is_complete` — green
- [ ] `test_the_report_names_both_split_constraints` — green
- [ ] `test_the_report_refuses_to_lead_with_accuracy` — green
- [ ] `test_the_report_states_recall_at_an_alert_budget` — green
- [ ] `test_phase_13_modules_are_complete` — green (47 functions)
- [ ] `test_the_training_script_runs_end_to_end` — green

## The project report (gate artifact)

- [ ] **The decision** — what someone does differently
- [ ] **The data** — source, licence, dates, how the attacks were generated
- [ ] **The split, and why** — grouped **and** temporal, slices reported separately
- [ ] **The metric, and why** — PR-AUC with baseline; accuracy explicitly rejected
- [ ] **The threshold** — from stated costs **and** the alert budget
- [ ] Recall quoted **at** an achievable alert volume
- [ ] **Calibration** checked before the cost threshold was used
- [ ] **What the model keys on** — SHAP, host-signature features checked
- [ ] **Limitations** — at least four, specific
- [ ] **What would make this fail in production** — the five risks
- [ ] **Reproduction** — MLflow run ID, git SHA, the command

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name the three structural problems in intrusion data and the day each was covered
- [ ] Why is a random split optimistic here, specifically?
- [ ] Why would a team reporting accuracy never notice?
- [ ] Why is ROC-AUC misleading on rare positives?
- [ ] Derive the cost-optimal threshold and say what it assumes
- [ ] Why does the alert budget matter more than the cost ratio sometimes?
- [ ] What four things must every tracked run log?
- [ ] Name three risks that do not appear in the test score

## PHASE 13 GATE

- [ ] `train.py` runs in one command and exits 0
- [ ] Every run logs params, metrics **with baseline**, artifacts, git SHA **and dirty flag**
- [ ] `mlruns/` gitignored
- [ ] Split is grouped **and** temporal; both guards pass
- [ ] Unseen-host and known-host-later slices reported separately
- [ ] PR-AUC with baseline; accuracy explicitly rejected
- [ ] Threshold from stated costs, checked against an alert budget
- [ ] Calibration verified before using the cost threshold
- [ ] SHAP run; host-signature features checked for leakage
- [ ] Project report complete, with four limitations and the failure section
- [ ] **ADR-008** (Day 114) written and cold-read
- [ ] `test_phase_13_modules_are_complete` green (47 functions)
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 116` succeeded and `./m status` shows Phases 0–13 complete
