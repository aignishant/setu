---
day: 84
phase: 11
phase_name: "EDA (Module 11)"
title: "The EDA loop, and an automated audit(df)"
ids: ["EDA-01", "EDA-02"]
principles: ["P1 build daily", "P7 evals before features", "P9 data has provenance", "P10 interview-ready artifacts"]
kind: lab
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 84 — The EDA loop, and an automated `audit(df)`

**Phase 11 · Module 11 · Exploratory data analysis** · IDs: **EDA-01** (the EDA loop), **EDA-02** (an automated audit)

> **Yesterday:** Phase 10 closed with a leak-proof pipeline.
> **Today:** the discipline that comes *before* it. EDA has a reputation as unstructured poking, and
> that reputation is the problem — unstructured exploration is Day 74's p-hacking with charts. Today
> you build a **loop with a stopping condition** and an `audit(df)` that answers every mechanical
> question in one call, so your attention goes where a machine cannot help.
> **Tomorrow:** univariate and bivariate exploration.

```bash
./m start 84 && ./m scaffold 84
```

**Time:** 110 minutes. **Request budget:** 0 model calls.

---

## §1 The story

"Explore the data" is not a task. It has no completion criterion, which is why EDA either stops too
early (you missed the thing that ruins the model) or never (three days of charts and no decision).

The fix is to treat it as a **loop with a question at the centre**:

```mermaid
flowchart LR
    Q["**a question**<br/>'can this data support<br/>the decision we want<br/>to make?'"] --> A["**audit** — mechanical<br/>shape · types · missing<br/>duplicates · leaks"]
    A --> L["**look** — one variable,<br/>then two, then structure"]
    L --> H["**a hypothesis**<br/>about the data<br/>or the domain"]
    H --> C["**check it**<br/>a chart or a test"]
    C --> D{"decision<br/>reached?"}
    D -->|no| H
    D -->|yes| STOP["**stop**<br/>write it down"]

    style Q fill:#1f6feb,color:#fff
    style STOP fill:#238636,color:#fff
```

Two properties make this different from poking around:

**It starts with a question**, so it can end. "Can this data support a churn model?" is answerable.
"Explore the customer data" is not, and an unanswerable question produces an unbounded exploration.

**The mechanical part is automated.** Row count, dtypes, missingness, duplicates, constant columns,
identifier columns, obvious leaks — a machine does all of that in one call, identically every time,
and never forgets step 7. Your attention is a scarce resource and it should go to the things a
machine cannot see: whether a variable means what its name says, whether the sample resembles the
population, whether a pattern reflects the domain or the collection process.

**And the honesty constraint from Day 74 applies here more than anywhere.** Exploration generates
hypotheses by looking at data. Every one of them is exploratory by construction, and confirming any
of them on the same data is Principle 15. EDA's output is a **list of things to check**, plus
decisions about data quality that do not depend on the target.

Today's `audit(df)` extends Day 34's `quality_report` — which is why that function exists — and
becomes the first call in every notebook and every case study for the rest of the plan.

---

## §2 Setup — run this

```bash
mkdir -p days/day-84/lab
touch days/day-84/lab/eda_loop.py
touch src/setu/eda.py
touch tests/test_eda.py
```

`src/setu/eda.py` is new — layer 3, importing frames, stats, plots and features.

---

## §3 EDA-01 / EDA-02 — the loop and the audit

`days/day-84/lab/eda_loop.py`:

```python
"""EDA-01 / EDA-02: a bounded exploration loop, and the audit that starts it."""

from __future__ import annotations

import numpy as np
import pandas as pd

from setu.arrays import make_rng


def messy_frame(n: int = 3_000) -> pd.DataFrame:
    """A frame with eight planted problems. Find them before reading §3.3."""
    rng = make_rng(0)
    frame = pd.DataFrame({
        "customer_id": [f"c{i:06d}" for i in range(n)],
        "signup_date": pd.to_datetime("2023-01-01") + pd.to_timedelta(
            rng.integers(0, 400, n), unit="D"),
        "plan": rng.choice(["free", "pro", "enterprise"], n, p=[0.7, 0.25, 0.05]),
        "region_code": rng.integers(1, 5, n),
        "monthly_spend": rng.lognormal(3, 1, n).round(2),
        "support_tickets": rng.poisson(rng.gamma(2, 1, n)),
        "satisfaction": rng.integers(1, 6, n).astype(float),
        "api_version": np.full(n, "v2"),
        "churned": rng.random(n) < 0.18,
    })
    frame.loc[frame.sample(400, random_state=1).index, "satisfaction"] = np.nan
    frame.loc[frame.sample(60, random_state=2).index, "monthly_spend"] = -1.0
    frame["days_until_churn"] = np.where(frame["churned"], rng.integers(1, 300, n), np.nan)
    frame["total_lifetime_spend"] = frame["monthly_spend"] * rng.integers(1, 24, n)
    return pd.concat([frame, frame.iloc[:40]], ignore_index=True)


def the_question_comes_first() -> None:
    print("\n  ❌ 'Explore the customer data'")
    print("       no completion criterion — you stop when you get bored or run out of time")
    print("\n  ✅ 'Can this data support a model that predicts churn at signup + 30 days?'")
    print("       answerable, and answerable NO")
    print("\n  The second one tells you what to look at: does churn exist in the data,")
    print("  is it balanced enough, are there features available AT signup + 30 days,")
    print("  and is the sample representative? Four checks, then a decision.")


def the_mechanical_pass(frame: pd.DataFrame) -> None:
    print(f"\n  shape: {frame.shape[0]:,} rows × {frame.shape[1]} columns")
    print(f"  memory: {frame.memory_usage(deep=True).sum() / 1024**2:.1f} MiB")

    print(f"\n  {'column':<22} {'dtype':<16} {'missing':>9} {'unique':>9} {'sample'}")
    for column in frame.columns:
        series = frame[column]
        missing = f"{series.isna().mean():.1%}"
        sample = str(series.dropna().iloc[0])[:18] if series.notna().any() else "—"
        print(f"  {column:<22} {str(series.dtype):<16} {missing:>9} "
              f"{series.nunique():>9} {sample}")

    print(f"\n  duplicate rows: {frame.duplicated().sum()}")
    print(f"  duplicate customer_id: {frame['customer_id'].duplicated().sum()}")


def the_eight_problems(frame: pd.DataFrame) -> None:
    print("\n  what the mechanical pass should have surfaced:")

    print(f"\n  1. DUPLICATE ROWS: {frame.duplicated().sum()} exact copies")
    print("     -> they leak across a train/test split (Day 79)")

    constant = [c for c in frame.columns if frame[c].nunique(dropna=False) <= 1]
    print(f"\n  2. CONSTANT COLUMN: {constant}")
    print("     -> carries no information; Day 83's drop_low_variance removes it")

    identifiers = [c for c in frame.columns
                   if frame[c].nunique() > 0.95 * len(frame) and frame[c].dtype == object]
    print(f"\n  3. IDENTIFIER: {identifiers}")
    print("     -> unique per row; as a feature it can only memorise")

    print(f"\n  4. IMPOSSIBLE VALUES: "
          f"{(frame['monthly_spend'] < 0).sum()} negative monthly_spend")
    print("     -> a sentinel, not a value (Day 34). Ask what -1 meant.")

    print(f"\n  5. LEAK — days_until_churn: {frame['days_until_churn'].isna().mean():.1%} missing")
    print(f"     and missing exactly when churned is False: "
          f"{(frame['days_until_churn'].isna() == ~frame['churned']).mean():.1%} agreement")
    print("     -> Day 82's prediction-time test: it needs the churn date")

    print(f"\n  6. LEAK — total_lifetime_spend: 'lifetime' includes the future")
    print("     -> Day 82's suspect tokens")

    print(f"\n  7. MISLABELLED TYPE: region_code is {frame['region_code'].dtype}")
    print("     -> it is NOMINAL (Day 58). Averaging it or feeding it raw to a linear")
    print("        model asserts region 4 is twice region 2.")

    print(f"\n  8. ORDINAL AS FLOAT: satisfaction is {frame['satisfaction'].dtype}, "
          f"values {sorted(frame['satisfaction'].dropna().unique())}")
    print("     -> a 1-5 rating is ORDINAL. Its mean assumes equal spacing (Day 58).")

    print("\n  Every one of these is mechanical. A machine finds all eight, identically,")
    print("  every time — which is exactly why it should not be your job.")


def what_the_machine_cannot_see(frame: pd.DataFrame) -> None:
    print("\n  what an audit CANNOT tell you, and you must:")
    print("\n    - does 'monthly_spend' mean gross or net? billed or collected?")
    print("    - is 'churned' defined as cancelled, or as lapsed-for-90-days?")
    print("    - the plan mix is 70/25/5 — is that the real population, or did the")
    print("      export filter something?")
    print(f"    - signup dates span {frame['signup_date'].min().date()} to "
          f"{frame['signup_date'].max().date()}. Was anything unusual happening then?")
    print("    - support_tickets is overdispersed (Day 65). Is that bursty users,")
    print("      or a ticketing system that auto-creates duplicates?")
    print("\n  These are DOMAIN questions, and the answers come from a person.")
    print("  Budget your attention for them; automate everything above.")


def the_loop_has_a_stopping_condition(frame: pd.DataFrame) -> None:
    question = "Can this data support a churn model scored at signup + 30 days?"
    print(f"\n  QUESTION: {question}")

    checks = [
        ("does the target exist and vary?",
         f"churned: {frame['churned'].mean():.1%} positive — yes, usable (Day 78)"),
        ("are there enough positive cases?",
         f"{int(frame['churned'].sum()):,} — enough for a model, watch the threshold"),
        ("are features available at signup + 30 days?",
         "NO for days_until_churn and total_lifetime_spend — both must be dropped"),
        ("is the sample representative?",
         "UNKNOWN — needs a domain answer about the export filter"),
    ]
    for check, finding in checks:
        print(f"\n    {check}\n      {finding}")

    print("\n  DECISION: yes, with two columns dropped and one open question.")
    print("\n  That is a stopping condition. Four checks, a decision, and a written")
    print("  record. Not 'I looked at the data for a while'.")


def exploration_generates_hypotheses_not_findings(frame: pd.DataFrame) -> None:
    rates = frame.groupby("plan", observed=True)["churned"].mean()
    print(f"\n  churn rate by plan:\n{(rates * 100).round(1).to_string()}")

    print("\n  Tempting: 'free-plan customers churn more — that is a finding!'")
    print("  It is not. You looked at the data and noticed a pattern, which is")
    print("  exploratory by construction (Day 74).")
    print("\n  You compared 3 groups here, and you will compare dozens by Day 90.")
    print("  Some difference WILL look large. The output of EDA is a LIST OF THINGS")
    print("  TO CHECK, tested on data you have not looked at yet (Principle 15).")


def the_audit_is_the_first_call(frame: pd.DataFrame) -> None:
    print("\n  every notebook, every case study, Days 87-89, starts with:")
    print("\n      from setu.eda import audit")
    print("      report = audit(frame, target='churned')")
    print("\n  because the alternative is remembering fourteen checks, in order,")
    print("  under time pressure, on data you have not seen before.")
    print("  Day 34's quality_report was the first half. Today it grows a target.")


if __name__ == "__main__":
    frame = messy_frame()
    the_question_comes_first()
    the_mechanical_pass(frame)
    the_eight_problems(frame)
    what_the_machine_cannot_see(frame)
    the_loop_has_a_stopping_condition(frame)
    exploration_generates_hypotheses_not_findings(frame)
    the_audit_is_the_first_call(frame)
```

**Line by line:**

- `messy_frame` — **eight planted problems.** Run `the_mechanical_pass` and try to find them all
  before reading §3.3. That exercise is the point: the ones you miss are the ones the audit exists to
  catch.
- `the_question_comes_first` — "explore the customer data" has **no completion criterion**, so you
  stop when you get bored. The specific question tells you exactly what to look at, and it can come
  out **no**, which is what makes it a question rather than a plan.
- `the_eight_problems` — each maps to an earlier day. Duplicates leak across a split (Day 79); the
  constant column is Day 83's `drop_low_variance`; the identifier can only memorise; `-1` spend is a
  Day 34 sentinel; the two leaks are Day 82's prediction-time test and suspect tokens;
  `region_code` as an integer is Day 58's nominal-wearing-integers; `satisfaction` as a float is Day
  58's ordinal mean.
- **The `days_until_churn` tell is worth pausing on.** It is missing exactly when `churned` is False,
  and that agreement rate prints at 100%. **Missingness perfectly correlated with the target** is a
  leak signature you can detect without knowing what the column means.
- `what_the_machine_cannot_see` — **five domain questions**, and none of them has a computational
  answer. Is `monthly_spend` gross or net? Is `churned` cancelled or lapsed? Is the 70/25/5 plan mix
  the real population or an export artefact? **Budget your attention for these; automate everything
  above.**
- `the_loop_has_a_stopping_condition` — four checks, a decision, and one honest **UNKNOWN**. That is a
  stopping condition. Note the decision is *"yes, with two columns dropped and one open question"* —
  not a yes or a no, which is what real answers look like.
- `exploration_generates_hypotheses_not_findings` — the churn-by-plan difference **looks** like a
  finding. It is a pattern you noticed by looking, which makes it exploratory by construction. You
  will compare dozens of groups by Day 90 and **some difference will look large** (Day 74). EDA's
  output is a list of things to check.
- `the_audit_is_the_first_call` — the alternative is remembering fourteen checks, in order, under time
  pressure, on unfamiliar data. **Day 34's `quality_report` was the first half**; today it grows a
  target and becomes the entry point for every case study in Phase 11.

---

## §4 Build brief — `src/setu/eda.py`

```python
"""Exploratory data analysis. Layer 3: imports frames, stats, plots, features."""

from __future__ import annotations

from setu.errors import DataError

SEVERITY = ("blocking", "serious", "worth-checking", "note")


def audit(frame, *, target: str | None = None, as_of_description: str = "prediction time",
          id_threshold: float = 0.95) -> dict:
    """TODO(me): the mechanical pass, in one call. Extends Day 34's quality_report.

    {"shape", "memory_mib", "columns": {...}, "findings": [...], "domain_questions": [...],
     "verdict": str}

    - REUSE quality_report (Day 34) for the per-column statistics; do NOT reimplement
    - each finding is {"severity", "column"|None, "issue", "why_it_matters", "day"}
      where `day` cites the lesson that explains it — a finding a reader cannot act
      on is noise
    - findings must cover, at minimum:
        duplicate rows · duplicate values in an id-like column · constant columns ·
        identifier columns · impossible values (negatives where the name implies a
        count/spend/age) · columns whose MISSINGNESS correlates with the target ·
        suspect-token columns (Day 82's prediction_time_check) · integer columns that
        look nominal · float columns with <= 10 distinct values that look ordinal
    - `domain_questions` is a list of prompts a HUMAN must answer (§3): it must
      include at least one per suspect column, and one about representativeness
    - `verdict` summarises: 'blocking issues found' / 'proceed with N corrections' /
      'no mechanical issues'
    - findings sorted by SEVERITY, blocking first
    - must not mutate the frame (ADR-001); must be JSON-serialisable
    - target=None is allowed: skip only the target-dependent findings, do not raise
    """
    raise NotImplementedError


def missingness_tracks_target(frame, *, target: str, threshold: float = 0.9) -> list:
    """TODO(me): find columns whose MISSINGNESS predicts the target (§3).

    Returns [{"column", "agreement", "direction"}] for columns where
    is-missing agrees with the target (or its negation) above `threshold`.
    - this is a leak signature that works WITHOUT knowing what the column means
    - raise DataError if `target` is absent, or has more than 2 distinct values
    - ignore columns with no missing values at all
    """
    raise NotImplementedError


def eda_question(text: str) -> dict:
    """TODO(me): validate that a question is answerable. PURE.

    {"question", "answerable": bool, "reason", "checks_implied": [...]}
    - answerable=False when the text lacks a decision verb (can/should/does/is) or
      lacks an object — 'explore the data' must fail
    - `checks_implied` is a best-effort list of what the question requires
    - raise DataError on an empty question
    - deliberately crude: it exists to make the framing step EXPLICIT, not to parse
      English. Say so in the docstring.
    """
    raise NotImplementedError


def eda_log(question: str) -> dict:
    """TODO(me): a record of the loop. Returns {"question", "checks": [], "decision": None}.

    - raise DataError if eda_question says the question is not answerable
    """
    raise NotImplementedError


def record_check(log: dict, *, check: str, finding: str,
                 answered: bool = True) -> dict:
    """TODO(me): append a check. Returns a NEW log (ADR-001).

    - `answered=False` records an open question (§3's UNKNOWN), which is a
      legitimate outcome and must survive into the decision
    """
    raise NotImplementedError


def conclude(log: dict, *, decision: str) -> dict:
    """TODO(me): close the loop.

    {"question", "checks", "decision", "open_questions": [...], "hypotheses": [...],
     "warnings": [...]}
    - raise DataError if no checks were recorded — a decision with no evidence
    - `open_questions` are the answered=False checks; they must appear in the output
      rather than being quietly dropped
    - warn if the decision does not mention any open question when some exist
    - EVERY pattern noticed during exploration goes in `hypotheses`, labelled as
      requiring fresh data (Day 74, Principle 15) — never in `decision`
    """
    raise NotImplementedError


def audit_summary(report: dict) -> str:
    """TODO(me): a paragraph a non-specialist can read.

    - lead with the verdict and the blocking count
    - name the blocking issues specifically
    - end with the number of domain questions outstanding
    - must NOT claim the data is 'clean' — say 'no mechanical issues found', which
      is the honest scope of an automated pass
    """
    raise NotImplementedError
```

- `audit` citing the **day** for each finding is the design decision. A report that says "constant
  column" is noise; one that says "constant column — carries no information, see Day 83" is
  actionable by someone who was not there.
- `audit_summary` **refusing the word "clean"** is the same instinct as Day 68's `describe_interval`.
  An automated pass finds mechanical problems; calling the result clean overstates what it checked.
- `conclude` forcing patterns into `hypotheses` rather than `decision` is Principle 15 made
  structural.

---

## §5 The eval that must be able to fail

`tests/test_eda.py`:

```python
import numpy as np
import pandas as pd
import pytest

from setu.arrays import make_rng
from setu.eda import (
    audit,
    audit_summary,
    conclude,
    eda_log,
    eda_question,
    missingness_tracks_target,
    record_check,
)
from setu.errors import DataError


@pytest.fixture
def messy():
    rng = make_rng(0)
    n = 1_000
    frame = pd.DataFrame({
        "customer_id": [f"c{i:05d}" for i in range(n)],
        "region_code": rng.integers(1, 5, n),
        "spend": rng.lognormal(3, 1, n),
        "satisfaction": rng.integers(1, 6, n).astype(float),
        "api_version": np.full(n, "v2"),
        "churned": rng.random(n) < 0.2,
    })
    frame.loc[frame.sample(50, random_state=1).index, "spend"] = -1.0
    frame["days_until_churn"] = np.where(frame["churned"], rng.integers(1, 300, n), np.nan)
    return pd.concat([frame, frame.iloc[:20]], ignore_index=True)


def issues(report):
    return " ".join(f["issue"] for f in report["findings"]).lower()


def test_duplicate_rows_are_found(messy):
    assert "duplicate" in issues(audit(messy, target="churned"))


def test_a_constant_column_is_found(messy):
    report = audit(messy, target="churned")
    assert any(f.get("column") == "api_version" for f in report["findings"])


def test_an_identifier_column_is_found(messy):
    report = audit(messy, target="churned")
    assert any(f.get("column") == "customer_id" for f in report["findings"])


def test_impossible_values_are_found(messy):
    report = audit(messy, target="churned")
    spend_findings = [f for f in report["findings"] if f.get("column") == "spend"]
    assert spend_findings, "50 negative spend values went unreported"


def test_an_integer_column_that_looks_nominal_is_flagged(messy):
    """region_code is int64 and nominal (Day 58)."""
    report = audit(messy, target="churned")
    assert any(f.get("column") == "region_code" for f in report["findings"])


def test_a_float_column_that_looks_ordinal_is_flagged(messy):
    """A 1-5 rating stored as float."""
    report = audit(messy, target="churned")
    assert any(f.get("column") == "satisfaction" for f in report["findings"])


def test_a_suspect_token_column_is_flagged(messy):
    """Day 82's prediction-time test, inside the audit."""
    report = audit(messy, target="churned")
    assert any(f.get("column") == "days_until_churn" for f in report["findings"])


def test_findings_cite_the_day_that_explains_them():
    """A finding a reader cannot act on is noise."""
    frame = pd.DataFrame({"a": [1.0, 1.0, 1.0], "y": [0, 1, 0]})
    report = audit(frame, target="y")
    assert report["findings"]
    for finding in report["findings"]:
        assert finding.get("day"), f"{finding['issue']} cites no lesson"
        assert finding.get("why_it_matters")


def test_findings_are_sorted_by_severity():
    frame = pd.DataFrame({
        "constant": [1.0] * 100,
        "total_spend": np.arange(100.0),
        "y": [0, 1] * 50,
    })
    severities = [f["severity"] for f in audit(frame, target="y")["findings"]]
    from setu.eda import SEVERITY

    order = [SEVERITY.index(s) for s in severities]
    assert order == sorted(order), "blocking issues must come first"


def test_the_audit_reuses_day_34s_quality_report(monkeypatch):
    import setu.frames as frames

    calls = []
    original = frames.quality_report
    monkeypatch.setattr(frames, "quality_report",
                        lambda f, **kw: calls.append(1) or original(f, **kw))
    audit(pd.DataFrame({"a": [1.0, 2.0, 3.0], "y": [0, 1, 0]}), target="y")
    assert calls, "audit reimplemented the per-column statistics"


def test_the_audit_does_not_mutate(messy):
    before = messy.copy()
    audit(messy, target="churned")
    pd.testing.assert_frame_equal(messy, before)


def test_the_audit_is_json_serialisable(messy):
    import json

    json.dumps(audit(messy, target="churned"))


def test_the_audit_works_without_a_target(messy):
    """Target-dependent findings are skipped, not raised."""
    report = audit(messy.drop(columns=["churned"]))
    assert report["findings"]


def test_domain_questions_are_produced(messy):
    """The things a machine cannot answer."""
    report = audit(messy, target="churned")
    assert len(report["domain_questions"]) >= 2
    assert any("represent" in q.lower() or "population" in q.lower()
               for q in report["domain_questions"])


def test_missingness_that_tracks_the_target_is_caught():
    """A leak signature that works without knowing what the column means."""
    rng = make_rng(1)
    n = 500
    churned = rng.random(n) < 0.3
    frame = pd.DataFrame({
        "churned": churned,
        "days_until_churn": np.where(churned, rng.integers(1, 100, n), np.nan),
        "innocent": rng.normal(0, 1, n),
    })
    frame.loc[frame.sample(50, random_state=2).index, "innocent"] = np.nan

    found = {entry["column"] for entry in missingness_tracks_target(frame, target="churned")}
    assert "days_until_churn" in found
    assert "innocent" not in found, "randomly missing data was flagged"


def test_missingness_check_ignores_complete_columns():
    frame = pd.DataFrame({"y": [0, 1] * 50, "full": range(100)})
    assert missingness_tracks_target(frame, target="y") == []


def test_missingness_check_rejects_a_multiclass_target():
    frame = pd.DataFrame({"y": [0, 1, 2] * 30, "x": [np.nan, 1.0, 2.0] * 30})
    with pytest.raises(DataError):
        missingness_tracks_target(frame, target="y")


def test_an_unanswerable_question_is_rejected():
    """'Explore the data' has no completion criterion."""
    assert eda_question("explore the customer data")["answerable"] is False


def test_an_answerable_question_is_accepted():
    result = eda_question("Can this data support a churn model at signup + 30 days?")
    assert result["answerable"] is True
    assert result["checks_implied"]


def test_the_log_refuses_an_unanswerable_question():
    with pytest.raises(DataError):
        eda_log("look at the data")


def test_an_empty_question_raises():
    with pytest.raises(DataError):
        eda_question("   ")


def test_a_decision_with_no_checks_is_refused():
    log = eda_log("Can this data support a churn model?")
    with pytest.raises(DataError):
        conclude(log, decision="yes")


def test_open_questions_survive_into_the_decision():
    """An honest UNKNOWN must not be quietly dropped."""
    log = eda_log("Can this data support a churn model?")
    log = record_check(log, check="target exists?", finding="18% positive")
    log = record_check(log, check="representative?", finding="unknown — ask the exporter",
                       answered=False)
    result = conclude(log, decision="yes, pending the representativeness question")
    assert len(result["open_questions"]) == 1
    assert "representative" in result["open_questions"][0]["check"].lower()


def test_a_decision_ignoring_open_questions_is_warned_about():
    log = eda_log("Can this data support a churn model?")
    log = record_check(log, check="target exists?", finding="yes")
    log = record_check(log, check="representative?", finding="unknown", answered=False)
    result = conclude(log, decision="yes, proceed")
    assert result["warnings"], "an unresolved open question was not raised"


def test_record_check_does_not_mutate():
    log = eda_log("Can this data support a churn model?")
    record_check(log, check="a", finding="b")
    assert log["checks"] == []


def test_patterns_go_in_hypotheses_not_the_decision():
    """Principle 15: you noticed it by looking."""
    log = eda_log("Can this data support a churn model?")
    log = record_check(log, check="churn by plan", finding="free churns more")
    result = conclude(log, decision="yes")
    combined = " ".join(str(h) for h in result["hypotheses"]).lower()
    assert "free" in combined or result["hypotheses"], (
        "an observed pattern was not recorded as a hypothesis"
    )


def test_the_summary_never_claims_the_data_is_clean(messy):
    """An automated pass finds mechanical problems. That is its whole scope."""
    text = audit_summary(audit(messy, target="churned")).lower()
    assert "clean" not in text
    assert "mechanical" in text or "automated" in text


def test_the_summary_names_the_blocking_issues(messy):
    report = audit(messy, target="churned")
    text = audit_summary(report)
    blocking = [f for f in report["findings"] if f["severity"] == "blocking"]
    for finding in blocking:
        if finding.get("column"):
            assert finding["column"] in text, f"{finding['column']} was not named"


def test_the_summary_counts_outstanding_domain_questions(messy):
    report = audit(messy, target="churned")
    text = audit_summary(report)
    assert str(len(report["domain_questions"])) in text
```

**Line by line:**

- `test_findings_cite_the_day_that_explains_them` — **the day's real assessment.** Every finding must
  carry both a `day` and a `why_it_matters`. A report saying "constant column" is noise to anyone who
  was not there; one saying "constant column — carries no information, see Day 83" can be acted on by
  a colleague. This is the difference between an audit and a wall of warnings.
- `test_missingness_that_tracks_the_target_is_caught` — asserts **both** that the leak is found and
  that the innocently-missing column is **not**. A detector that flags every column with missing
  values finds the leak and is useless.
- `test_the_summary_never_claims_the_data_is_clean` — the third time this project has tested English
  (Days 68, 75, now 84), and for the same reason. "Clean" overstates what an automated pass checked;
  "no mechanical issues found" is the honest scope.
- `test_open_questions_survive_into_the_decision` — an honest UNKNOWN is a legitimate outcome and must
  not be quietly dropped. Its companion warns when the decision ignores one.
- `test_findings_are_sorted_by_severity` — a report where a blocking leak appears below a naming
  suggestion is a report nobody reads to the bottom of.
- `test_the_audit_reuses_day_34s_quality_report` — the architecture test, seventh appearance. Two
  implementations of per-column statistics will disagree.
- `test_an_unanswerable_question_is_rejected` — "explore the customer data" must fail, because it has
  no completion criterion. Crude by design, and the docstring says so; the value is making the framing
  step explicit rather than parsing English.
- `test_the_audit_works_without_a_target` — target-dependent findings are **skipped**, not raised.
  EDA often starts before a target is chosen.

```bash
uv run python -m pytest tests/test_eda.py -v
```

---

## §6 Request budget

| Resource | Spent today |
|---|---|
| LLM calls | **0** |

---

## §7 Traps

- **"Explore the data" as a task.** No completion criterion; it ends when you tire.
- **Doing the mechanical checks by hand.** You will forget one, on the day it mattered.
- **Spending attention where a machine could look.** It is a scarce resource.
- **Skipping the domain questions.** They are the only part that needs you.
- **Treating an observed pattern as a finding.** Exploratory by construction (Day 74).
- **Confirming an EDA hypothesis on the same data.** Principle 15.
- **Missing that missingness tracks the target.** A leak signature with no domain knowledge required.
- **An integer column that is really nominal.** Day 58.
- **A 1–5 rating averaged.** Ordinal. Day 58.
- **Duplicate rows left in.** They leak across the split (Day 79).
- **Calling data "clean".** An automated pass checked the mechanical part only.
- **A decision that ignores the open questions.** Record them, or they vanish.

---

## §8 Verify before you code

Written **2026-08-21**:

- <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html> — the crude version of the
  mechanical pass.
- <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html> — `subset` and
  `keep`, which decide what "duplicate" means.
- <https://scikit-learn.org/stable/common_pitfalls.html> — sklearn's own list, several of which the
  audit checks for.

---

## §9 Say it in an interview

> "EDA gets treated as unstructured poking, and that's the problem — unstructured exploration is
> p-hacking with charts. I frame it as a loop with a question at the centre, because a question like
> 'can this data support a churn model scored at signup plus thirty days' is answerable and can come
> out no, whereas 'explore the customer data' has no completion criterion. Then the mechanical half is
> automated: shape, types, missingness, duplicates, constants, identifiers, suspect column names,
> integers that are really categories. A machine does all of that identically every time and never
> forgets step seven, which frees my attention for the things it can't see — whether `churned` means
> cancelled or lapsed, whether the plan mix reflects the real population or an export filter. One
> check I'd highlight is missingness that tracks the target: `days_until_churn` is missing exactly
> when the customer hasn't churned, and that's a leak signature you can detect without knowing what
> the column means. And every finding cites the lesson that explains why it matters, because a report
> that just says 'constant column' is noise to whoever reads it next."

---

## §10 Done when

Tick [`CHECKLIST.md`](CHECKLIST.md), then `./m check && ./m done 84`.
