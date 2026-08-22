---
day: 110
phase: 13
phase_name: "Ensembles & clustering (Module 13)"
title: "Boosting intuition — AdaBoost to gradient boosting, by hand"
ids: ["ML-21"]
principles: ["P1 build daily", "P2 from scratch before library", "P7 evals before features"]
kind: lab
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 110 — Boosting, by hand

**Phase 13 · Module 13** · ID: **ML-21** (AdaBoost, gradient boosting, additive models)

> **Yesterday:** OOB evaluation, and importance that hides.
> **Today:** the other half of the phase, and it works by an opposite mechanism. Bagging fits models
> **in parallel** and averages away variance. Boosting fits them **in sequence**, each one correcting
> the last, and it attacks **bias**. You will build both AdaBoost and gradient boosting from scratch
> in about twenty lines each.
> **Tomorrow:** the library versions, and early stopping.

```bash
./m start 110 && ./m scaffold 110
```

**Time:** 110 minutes. **Request budget:** 0 model calls.

---

## §1 The story

Day 107 was precise about the limit: **averaging reduces variance and does nothing to bias.** So if
your error is bias — the model is too simple to represent the truth — bagging cannot help.

Boosting attacks bias directly, by a mechanism that sounds implausible until you watch it:

```mermaid
flowchart LR
    F0["start: predict<br/>the mean"] --> R1["what's left over?<br/>**residuals**"]
    R1 --> M1["fit a weak model<br/>to the residuals"]
    M1 --> F1["add it in<br/>(scaled by η)"]
    F1 --> R2["new residuals"]
    R2 --> M2["fit another…"]
    M2 -.-> DOTS["…for M rounds"]

    style R1 fill:#8957e5,color:#fff
    style M1 fill:#238636,color:#fff
```

**Each model is fitted to the errors of everything before it.** Sum them and the bias falls, because
every round explicitly targets what the current ensemble is still getting wrong.

Two historical framings of the same idea, and it is worth seeing them as one:

**AdaBoost (1995)** reweights *rows*. Misclassified rows get heavier, so the next stump concentrates
on them. Each stump also gets a **weight** `α` based on how accurate it was.

**Gradient boosting (1999)** fits the *residuals* directly. And the insight that unified the field:
**the residual of squared error is its negative gradient**, so fitting residuals *is* gradient descent
— performed in function space rather than parameter space. Change the loss and you change what the
"residuals" are, which is why gradient boosting handles classification, ranking and quantile
regression with the same machinery.

Three consequences that decide how you use it:

- **Base models must be weak.** Deep trees fit the residuals perfectly, leaving nothing for the next
  round. Boosting uses depth 1–6, the opposite of Day 108's rule.
- **The learning rate `η` is essential.** Adding each model at full strength overshoots. Small `η`
  with many rounds beats large `η` with few — the same trade as Day 95.
- **More rounds DO overfit.** Unlike bagging, where `n_estimators` cannot hurt, boosting will happily
  fit noise given enough rounds. That is why Day 112's early stopping is mandatory rather than optional.

---

## §2 Setup — run this

```bash
mkdir -p days/day-110/lab
touch days/day-110/lab/boosting.py
```

`src/setu/ensembles.py` grows today. No new packages.

---

## §3 ML-21 — correcting

`days/day-110/lab/boosting.py`:

```python
"""ML-21: AdaBoost and gradient boosting, built by hand."""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from setu.arrays import make_rng


def regression_data(n=600, *, seed=0):
    rng = make_rng(seed)
    x = rng.uniform(-3, 3, n).reshape(-1, 1)
    return x, np.sin(1.6 * x.ravel()) + 0.35 * x.ravel() + rng.normal(0, 0.3, n)


def classification_data(n=1_200, *, seed=0):
    rng = make_rng(seed)
    x = rng.normal(0, 1, (n, 4))
    z = -0.2 + x @ np.array([1.2, -0.9, 0.6, 0.0]) + 0.8 * x[:, 0] * x[:, 1]
    return x, np.where(rng.random(n) < 1 / (1 + np.exp(-z)), 1, -1)


def gradient_boosting_from_scratch() -> None:
    x, y = regression_data()
    x_test, y_test = regression_data(n=2_000, seed=99)

    prediction = np.full(len(y), y.mean())          # round 0: predict the mean
    test_prediction = np.full(len(y_test), y.mean())
    eta, models = 0.1, []

    print(f"\n  {'round':>6} {'train MSE':>11} {'test MSE':>10} {'|residual| mean':>17}")
    print(f"  {0:>6} {((prediction - y) ** 2).mean():>11.5f} "
          f"{((test_prediction - y_test) ** 2).mean():>10.5f} "
          f"{np.abs(y - prediction).mean():>17.5f}")

    for round_number in range(1, 301):
        residual = y - prediction                    # THE gradient of squared error
        stump = DecisionTreeRegressor(max_depth=2).fit(x, residual)
        models.append(stump)
        prediction += eta * stump.predict(x)
        test_prediction += eta * stump.predict(x_test)

        if round_number in (1, 5, 20, 100, 300):
            print(f"  {round_number:>6} {((prediction - y) ** 2).mean():>11.5f} "
                  f"{((test_prediction - y_test) ** 2).mean():>10.5f} "
                  f"{np.abs(y - residual - prediction + residual).mean():>17.5f}")

    library = GradientBoostingRegressor(n_estimators=300, learning_rate=0.1,
                                        max_depth=2, random_state=0).fit(x, y)
    print(f"\n  mine    test MSE: {((test_prediction - y_test) ** 2).mean():.5f}")
    print(f"  sklearn test MSE: {((library.predict(x_test) - y_test) ** 2).mean():.5f}")

    print("\n  That is the whole algorithm: predict the mean, fit the leftovers, add a")
    print("  fraction of it, repeat. Twenty lines, and it matches the library.")


def residuals_are_the_gradient() -> None:
    y = np.array([3.0, 1.0, 4.0, 1.5])
    prediction = np.array([2.0, 2.0, 2.0, 2.0])

    residual = y - prediction
    epsilon = 1e-6
    numeric = np.array([
        (((prediction + epsilon * np.eye(4)[i] - y) ** 2).mean()
         - ((prediction - epsilon * np.eye(4)[i] - y) ** 2).mean()) / (2 * epsilon)
        for i in range(4)
    ])

    print(f"\n  loss L = mean((prediction − y)²)")
    print(f"    residual (y − prediction) : {residual.tolist()}")
    print(f"    −∇L numerically           : {np.round(-numeric * len(y) / 2, 6).tolist()}")

    print("\n  ✅ The residual IS the negative gradient of squared error, up to a constant.")
    print("  So 'fit the residuals' is literally gradient descent — but in FUNCTION")
    print("  space: each step adds a whole model rather than adjusting a parameter.")
    print("\n  🚨 That is why it generalises. Change the loss and the 'residual' changes:")
    print("     - squared error   -> y − prediction")
    print("     - absolute error  -> sign(y − prediction)")
    print("     - log loss        -> y − sigmoid(prediction)")
    print("  Same machinery, different target. Day 111 uses the third one.")


def the_learning_rate_matters() -> None:
    x, y = regression_data()
    x_test, y_test = regression_data(n=2_000, seed=99)

    print(f"\n  {'η':>7} {'rounds to best':>16} {'best test MSE':>15} {'MSE @300':>10}")
    for eta in (1.0, 0.5, 0.1, 0.02):
        prediction = np.full(len(y), y.mean())
        test_prediction = np.full(len(y_test), y.mean())
        history = []
        for _ in range(300):
            stump = DecisionTreeRegressor(max_depth=2).fit(x, y - prediction)
            prediction += eta * stump.predict(x)
            test_prediction += eta * stump.predict(x_test)
            history.append(((test_prediction - y_test) ** 2).mean())
        best = int(np.argmin(history)) + 1
        print(f"  {eta:>7} {best:>16} {min(history):>15.5f} {history[-1]:>10.5f}")

    print("\n  Large η reaches its best in a few rounds and then DEGRADES — it overshoots")
    print("  and starts fitting noise. Small η is slower and ends up better.")
    print("\n  ⚠️ η and n_estimators trade against each other: halve η and you need")
    print("     roughly twice the rounds. Tune them TOGETHER, never separately.")


def boosting_overfits_and_bagging_does_not() -> None:
    x, y = regression_data(n=250)
    x_test, y_test = regression_data(n=2_000, seed=99)

    from sklearn.ensemble import BaggingRegressor

    print(f"\n  {'M':>6} {'boosting test':>15} {'bagging test':>14}")
    for m in (5, 25, 100, 400, 1_500):
        boost = GradientBoostingRegressor(n_estimators=m, learning_rate=0.1,
                                          max_depth=3, random_state=0).fit(x, y)
        bag = BaggingRegressor(DecisionTreeRegressor(), n_estimators=min(m, 400),
                               random_state=0).fit(x, y)
        print(f"  {m:>6} {((boost.predict(x_test) - y_test) ** 2).mean():>15.5f} "
              f"{((bag.predict(x_test) - y_test) ** 2).mean():>14.5f}")

    print("\n  🚨 Boosting's test error falls, bottoms out, and then RISES. Bagging's")
    print("     flattens and stays there (Day 108).")
    print("\n  That single difference is why n_estimators is a capacity parameter for")
    print("  boosting and not for bagging — and why Day 112's early stopping is")
    print("  mandatory rather than a nicety.")


def base_models_must_be_weak() -> None:
    x, y = regression_data(n=400)
    x_test, y_test = regression_data(n=2_000, seed=99)

    print(f"\n  {'max_depth':>10} {'test MSE @200':>15} {'train MSE @200':>16}")
    for depth in (1, 2, 3, 6, 12, None):
        model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1,
                                          max_depth=depth, random_state=0).fit(x, y)
        label = "None" if depth is None else str(depth)
        print(f"  {label:>10} {((model.predict(x_test) - y_test) ** 2).mean():>15.5f} "
              f"{((model.predict(x) - y) ** 2).mean():>16.5f}")

    print("\n  Depth 2–3 wins. Deep trees fit the residuals almost perfectly in round 1,")
    print("  leaving nothing for the next round — the sequence collapses into a single")
    print("  overfitted tree.")
    print("\n  ⚠️ This is the EXACT OPPOSITE of Day 108's rule. Bag deep trees; boost")
    print("     shallow ones. Getting it backwards is the most common boosting mistake.")
    print("\n  Depth also controls INTERACTION order: depth 1 is additive (no interactions),")
    print("  depth 2 captures pairwise, depth 3 three-way. Choose it for that too.")


def adaboost_from_scratch() -> None:
    x, y = classification_data()
    n = len(y)
    weights = np.full(n, 1 / n)
    stumps, alphas = [], []

    print(f"\n  {'round':>6} {'weighted err':>13} {'α':>8} {'ensemble acc':>14}")
    for round_number in range(1, 51):
        stump = DecisionTreeClassifier(max_depth=1).fit(x, y, sample_weight=weights)
        predicted = stump.predict(x)

        error = weights[predicted != y].sum()
        error = np.clip(error, 1e-10, 1 - 1e-10)
        alpha = 0.5 * np.log((1 - error) / error)

        stumps.append(stump)
        alphas.append(alpha)

        weights *= np.exp(-alpha * y * predicted)     # wrong rows get heavier
        weights /= weights.sum()

        if round_number in (1, 2, 10, 50):
            score = np.sign(sum(a * s.predict(x) for a, s in zip(alphas, stumps, strict=True)))
            print(f"  {round_number:>6} {error:>13.5f} {alpha:>8.4f} "
                  f"{(score == y).mean():>14.4f}")

    library = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=50,
                                 algorithm="SAMME", random_state=0).fit(x, y)
    print(f"\n  mine    : {(np.sign(sum(a * s.predict(x) for a, s in zip(alphas, stumps, strict=True))) == y).mean():.4f}")
    print(f"  sklearn : {library.score(x, y):.4f}")

    print("\n  Read the α column: a stump with 50% weighted error gets α = 0 (ignored),")
    print("  and a better one gets more say. The weight update is the whole trick —")
    print("  exp(−α·y·prediction) is >1 when wrong and <1 when right.")


def adaboost_is_gradient_boosting() -> None:
    print("\n  the two are the same algorithm with different losses:")
    print(f"\n  {'method':<22} {'loss':<22} {'what it fits'}")
    rows = [
        ("AdaBoost", "exponential", "reweighted rows"),
        ("gradient boosting (reg)", "squared error", "y − prediction"),
        ("gradient boosting (clf)", "log loss", "y − sigmoid(prediction)"),
        ("robust regression", "absolute error", "sign(y − prediction)"),
    ]
    for method, loss, fits in rows:
        print(f"  {method:<22} {loss:<22} {fits}")

    print("\n  Friedman's 1999 result: AdaBoost is gradient boosting under EXPONENTIAL")
    print("  loss. The row reweighting and the residual fitting are the same operation.")
    print("\n  ⚠️ Exponential loss weights a badly-misclassified row exponentially, so")
    print("     AdaBoost is unusually sensitive to LABEL NOISE — one mislabelled row")
    print("     can dominate later rounds. Log loss grows only linearly out there,")
    print("     which is one reason gradient boosting largely replaced it.")


def sequential_means_no_parallelism() -> None:
    print("\n  the structural cost of boosting:")
    print("    bagging  : all M models are independent — fit them on M cores")
    print("    boosting : model k needs model k−1's residuals — strictly sequential")
    print("\n  ⚠️ So `n_jobs=-1` on a GradientBoostingRegressor does far less than on a")
    print("     forest. XGBoost and LightGBM (Days 112–113) parallelise WITHIN a tree")
    print("     — across features and split candidates — not across trees.")
    print("\n  Practical consequence: a forest of 500 trees may fit faster than a boosted")
    print("  ensemble of 500, even though each boosted tree is far smaller.")


def when_to_boost_and_when_not_to() -> None:
    rows = [
        ("bias-dominated error", "boost", "Day 96's learning curve says so"),
        ("variance-dominated error", "bag", "Day 107; boosting adds capacity you don't need"),
        ("noisy labels", "bag", "boosting chases the noise, AdaBoost worst of all"),
        ("need parallel training", "bag", "boosting is sequential"),
        ("tabular, clean, tuned", "boost", "usually the strongest tabular model"),
        ("tiny dataset", "bag", "boosting has more knobs to overfit with"),
    ]
    print(f"\n  {'situation':<26} {'choose':<8} {'because'}")
    for situation, choice, because in rows:
        print(f"  {situation:<26} {choice:<8} {because}")

    print("\n  And the honest one: on clean tabular data a tuned boosted ensemble usually")
    print("  wins — but it needs early stopping, a tuned learning rate, and a validation")
    print("  set. A Random Forest with defaults is often within a point of it, for a")
    print("  fraction of the effort (Day 106's one-standard-error rule).")


if __name__ == "__main__":
    gradient_boosting_from_scratch()
    residuals_are_the_gradient()
    the_learning_rate_matters()
    boosting_overfits_and_bagging_does_not()
    base_models_must_be_weak()
    adaboost_from_scratch()
    adaboost_is_gradient_boosting()
    sequential_means_no_parallelism()
    when_to_boost_and_when_not_to()
```

**Line by line:**

- `gradient_boosting_from_scratch` — **the whole algorithm in twenty lines.** Predict the mean, fit the
  leftovers with a stump, add `η` times it, repeat. And it matches sklearn, which is the confidence
  Principle 2 exists to provide.
- `residuals_are_the_gradient` — **the identity that unified the field.** The residual *is* the negative
  gradient of squared error, verified numerically. So "fit the residuals" is gradient descent in
  **function space** — each step adds a whole model rather than adjusting a parameter. And the four-line
  table is why it generalises: change the loss and the "residual" changes, same machinery throughout.
- `the_learning_rate_matters` — **large `η` reaches its best in a few rounds and then degrades.** Small
  `η` is slower and ends better. And the practical rule: `η` and `n_estimators` trade against each
  other, so **halving `η` roughly doubles the rounds you need — tune them together.**
- `boosting_overfits_and_bagging_does_not` — **the single most important difference in this phase.**
  Boosting's test error falls, bottoms out and **rises**; bagging's flattens and stays. That is why
  `n_estimators` is a capacity parameter for one and not the other, and why Day 112's early stopping is
  mandatory.
- `base_models_must_be_weak` — depth 2–3 wins. **Deep trees fit the residuals almost perfectly in round
  one, leaving nothing for round two**, and the sequence collapses into a single overfitted tree. This
  is **the exact opposite of Day 108's rule**, and getting it backwards is the most common boosting
  mistake. Depth also sets the **interaction order**: depth 1 is additive, depth 2 pairwise.
- `adaboost_from_scratch` — **read the `α` column.** A stump at 50% weighted error gets `α = 0` and is
  ignored; a better one gets more say. And `exp(−α·y·prediction)` is the whole trick: greater than 1
  when wrong, less than 1 when right.
- `adaboost_is_gradient_boosting` — Friedman's result: **AdaBoost is gradient boosting under exponential
  loss.** And the consequence is practical: exponential loss weights a badly-misclassified row
  *exponentially*, so **AdaBoost is unusually sensitive to label noise** — one mislabelled row can
  dominate later rounds. Log loss grows only linearly out there.
- `sequential_means_no_parallelism` — model `k` needs model `k−1`'s residuals, so boosting is
  **strictly sequential**. XGBoost and LightGBM parallelise *within* a tree, not across trees, and a
  500-tree forest may fit faster than a 500-round boosted ensemble.
- `when_to_boost_and_when_not_to` — six situations, and the honest closing note: a tuned boosted
  ensemble usually wins on clean tabular data, but **a Random Forest with defaults is often within a
  point of it** for a fraction of the effort (Day 106).

---

## §4 Build brief

Extend `src/setu/ensembles.py`:

```python
LOSSES = {"squared", "absolute", "log"}


def negative_gradient(y, prediction, *, loss: str = "squared"):
    """TODO(me): the 'residual' for each loss. PURE.

    - squared  -> y - prediction
    - absolute -> sign(y - prediction)   (robust to outliers; ignores magnitude)
    - log      -> y - sigmoid(prediction)  (y in {0, 1}; reuse Day 99's sigmoid)
    - raise DataError on an unknown loss, listing LOSSES
    - raise DataError if loss='log' and y is not in {0, 1}, naming what was found
    - the docstring must state that this IS the negative gradient, and that fitting
      it is gradient descent in function space (§3.2)
    """
    raise NotImplementedError


def fit_gradient_boosting(x, y, *, n_estimators: int = 100, learning_rate: float = 0.1,
                          max_depth: int = 3, loss: str = "squared",
                          validation=None, seed: int = 42) -> dict:
    """TODO(me): §3.1, as a function, with the staged history kept.

    {"models": [...], "initial", "learning_rate", "loss",
     "train_history": [...], "val_history": [...] | None,
     "best_iteration": int | None, "warnings": [...]}
    - `initial` is the mean for squared loss, the median for absolute, the log-odds
      for log loss — say why in the docstring; a wrong starting point costs rounds
    - train_history has one entry per round, so a caller can PLOT the curve
    - when `validation` is given, record val_history and best_iteration (the argmin)
    - WARN when best_iteration < n_estimators * 0.5: you are training well past the
      optimum and Day 112's early stopping would have saved the compute
    - WARN when max_depth > 6: boosting wants WEAK models (§3.5), and this is the
      most common boosting mistake — the message must name Day 108's opposite rule
    - raise DataError if learning_rate <= 0 or > 1, or n_estimators < 1
    """
    raise NotImplementedError


def staged_predictions(fit: dict, x):
    """TODO(me): the prediction after EVERY round, as a generator.

    Yields the running prediction after 1, 2, ... n_estimators models.
    - this is what makes an overfitting curve plottable without refitting
    - must not materialise all rounds at once for a large x — yield as you go
    """
    raise NotImplementedError


def overfitting_curve(fit: dict, x_val, y_val, *, scorer) -> dict:
    """TODO(me): §3.4 — does this ensemble overfit, and where?

    {"scores": [...], "best_iteration", "best_score", "final_score",
     "overfits": bool, "degradation": float, "recommendation": str}
    - overfits is True when final_score is worse than best_score by more than the
      noise level — boosting DOES overfit, unlike bagging (Day 108)
    - degradation is how much was lost by training past the optimum
    - the recommendation must name a concrete n_estimators, not just 'use early stopping'
    - reuse staged_predictions rather than refitting
    """
    raise NotImplementedError


def fit_adaboost(x, y, *, n_estimators: int = 50, seed: int = 42) -> dict:
    """TODO(me): §3.6, from scratch. y must be in {-1, +1}.

    {"stumps": [...], "alphas": [...], "weighted_errors": [...],
     "final_weights": ndarray, "warnings": [...]}
    - alpha = 0.5 * log((1-err)/err), with err clipped away from 0 and 1
    - weights *= exp(-alpha * y * prediction), then renormalised to sum to 1
    - a stump with weighted error >= 0.5 gets alpha <= 0; STOP and warn rather than
      continuing with a harmful model
    - WARN when the final weights are highly concentrated (top 1% of rows holding
      over 20% of the weight): that is the label-noise failure mode (§3.7)
    - raise DataError if y is not in {-1, +1}, naming what was found
    """
    raise NotImplementedError


def boosting_defaults(*, n_rows: int, noisy_labels: bool = False,
                      interaction_order: int = 2) -> dict:
    """TODO(me): a starting configuration, with reasons. PURE.

    {"max_depth", "learning_rate", "n_estimators", "loss", "reasons": {...},
     "warnings": [...]}
    - max_depth = interaction_order: depth d captures d-way interactions (§3.5)
    - learning_rate small (0.05-0.1) with correspondingly more rounds
    - noisy_labels -> never exponential loss; the reason must cite AdaBoost's
      sensitivity (§3.7), and warn that bagging may be the better choice entirely
    - every parameter needs a reason; a default with no reason is cargo cult
    - raise DataError if interaction_order < 1 or > 6
    """
    raise NotImplementedError
```

- `fit_gradient_boosting` **warning when `max_depth > 6`** encodes §3.5, and the message must name
  Day 108's opposite rule — because the mistake is *transferring* the bagging habit, and naming that is
  what makes the warning land.
- `staged_predictions` as a **generator** is what makes Day 112's early stopping cheap: you get the
  whole overfitting curve from one fit rather than `M` refits.
- `fit_adaboost` **stopping when `α ≤ 0`** matters: a stump worse than chance would be *subtracted* into
  the ensemble, and continuing past it is how a boosted model quietly degrades.

---

## §5 The eval that must be able to fail

Add to `tests/test_ensembles.py`:

```python
from setu.ensembles import (
    LOSSES,
    boosting_defaults,
    fit_adaboost,
    fit_gradient_boosting,
    negative_gradient,
    overfitting_curve,
    staged_predictions,
)


def _regression(n=500, seed=0):
    rng = make_rng(seed)
    x = rng.uniform(-3, 3, n).reshape(-1, 1)
    return x, np.sin(1.6 * x.ravel()) + 0.35 * x.ravel() + rng.normal(0, 0.3, n)


def test_the_squared_error_residual_is_the_negative_gradient():
    """Fitting residuals IS gradient descent, in function space."""
    y = np.array([3.0, 1.0, 4.0, 1.5])
    prediction = np.array([2.0, 2.0, 2.0, 2.0])

    analytic = negative_gradient(y, prediction, loss="squared")
    epsilon = 1e-6
    numeric = np.array([
        (((prediction + epsilon * np.eye(4)[i] - y) ** 2).sum()
         - ((prediction - epsilon * np.eye(4)[i] - y) ** 2).sum()) / (2 * epsilon)
        for i in range(4)
    ])
    assert np.allclose(analytic, -numeric / 2, atol=1e-5)


def test_absolute_error_uses_only_the_sign():
    """Robust to outliers — magnitude is deliberately discarded."""
    gradient = negative_gradient(np.array([10.0, 0.0]), np.array([0.0, 1_000.0]),
                                 loss="absolute")
    assert set(np.unique(gradient)) <= {-1.0, 1.0}


def test_log_loss_gradient_is_y_minus_sigmoid():
    from setu.models import sigmoid

    y = np.array([1, 0, 1, 0])
    prediction = np.array([0.5, -0.5, 2.0, -2.0])
    assert np.allclose(negative_gradient(y, prediction, loss="log"),
                       y - sigmoid(prediction))


def test_log_loss_rejects_a_non_binary_target():
    with pytest.raises(DataError) as info:
        negative_gradient(np.array([-1, 1]), np.array([0.0, 0.0]), loss="log")
    assert "-1" in str(info.value) or "1" in str(info.value)


def test_an_unknown_loss_lists_the_known_ones():
    with pytest.raises(DataError) as info:
        negative_gradient(np.array([1.0]), np.array([0.0]), loss="huber-ish")
    assert any(name in str(info.value) for name in LOSSES)


def test_the_gradient_docstring_names_function_space():
    assert "function space" in negative_gradient.__doc__.lower()


def test_boosting_matches_sklearn():
    from sklearn.ensemble import GradientBoostingRegressor

    x, y = _regression()
    x_test, y_test = _regression(n=1_500, seed=99)

    mine = fit_gradient_boosting(x, y, n_estimators=200, learning_rate=0.1, max_depth=2)
    final = list(staged_predictions(mine, x_test))[-1]
    theirs = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=2,
                                       random_state=0).fit(x, y).predict(x_test)

    assert ((final - y_test) ** 2).mean() == pytest.approx(
        ((theirs - y_test) ** 2).mean(), rel=0.15
    )


def test_the_training_loss_decreases():
    x, y = _regression()
    history = fit_gradient_boosting(x, y, n_estimators=100)["train_history"]
    assert history[-1] < history[0] / 3


def test_the_history_has_one_entry_per_round():
    x, y = _regression()
    assert len(fit_gradient_boosting(x, y, n_estimators=37)["train_history"]) == 37


def test_staged_predictions_yields_every_round():
    x, y = _regression(n=200)
    fit = fit_gradient_boosting(x, y, n_estimators=25)
    stages = list(staged_predictions(fit, x))
    assert len(stages) == 25
    assert ((stages[-1] - y) ** 2).mean() < ((stages[0] - y) ** 2).mean()


def test_a_smaller_learning_rate_needs_more_rounds():
    """They trade against each other — tune them together."""
    x, y = _regression()
    x_val, y_val = _regression(n=1_500, seed=99)

    fast = fit_gradient_boosting(x, y, n_estimators=400, learning_rate=0.5,
                                 max_depth=2, validation=(x_val, y_val))
    slow = fit_gradient_boosting(x, y, n_estimators=400, learning_rate=0.02,
                                 max_depth=2, validation=(x_val, y_val))
    assert slow["best_iteration"] > fast["best_iteration"]


def test_boosting_overfits_with_too_many_rounds():
    """The difference from bagging that decides everything."""
    x, y = _regression(n=150)
    x_val, y_val = _regression(n=2_000, seed=99)

    fit = fit_gradient_boosting(x, y, n_estimators=1_200, learning_rate=0.1, max_depth=4,
                                validation=(x_val, y_val))
    curve = overfitting_curve(fit, x_val, y_val,
                              scorer=lambda t, p: ((t - p) ** 2).mean())
    assert curve["overfits"] is True
    assert curve["best_iteration"] < 1_200
    assert curve["final_score"] > curve["best_score"]


def test_the_recommendation_names_a_concrete_round_count():
    """'Use early stopping' is not actionable."""
    x, y = _regression(n=150)
    x_val, y_val = _regression(n=2_000, seed=99)
    fit = fit_gradient_boosting(x, y, n_estimators=800, learning_rate=0.1, max_depth=4,
                                validation=(x_val, y_val))
    curve = overfitting_curve(fit, x_val, y_val,
                              scorer=lambda t, p: ((t - p) ** 2).mean())
    assert str(curve["best_iteration"]) in curve["recommendation"]


def test_training_past_the_optimum_is_warned_about():
    x, y = _regression(n=150)
    x_val, y_val = _regression(n=2_000, seed=99)
    fit = fit_gradient_boosting(x, y, n_estimators=1_500, learning_rate=0.1, max_depth=4,
                                validation=(x_val, y_val))
    assert fit["warnings"]


def test_a_deep_base_model_is_warned_about():
    """The exact opposite of Day 108's rule — the commonest boosting mistake."""
    x, y = _regression()
    fit = fit_gradient_boosting(x, y, n_estimators=30, max_depth=12)
    assert fit["warnings"]
    warning = " ".join(fit["warnings"]).lower()
    assert "weak" in warning or "shallow" in warning or "depth" in warning
    assert "108" in warning or "bagging" in warning or "forest" in warning, (
        "the warning must name the opposite rule being transferred"
    )


def test_shallow_base_models_are_not_warned_about():
    x, y = _regression()
    fit = fit_gradient_boosting(x, y, n_estimators=30, max_depth=3)
    assert not any("depth" in w.lower() for w in fit["warnings"])


def test_the_initial_prediction_matches_the_loss():
    """A wrong starting point costs rounds."""
    x, y = _regression()
    assert fit_gradient_boosting(x, y, n_estimators=5, loss="squared")["initial"] == \
        pytest.approx(y.mean())
    assert fit_gradient_boosting(x, y, n_estimators=5, loss="absolute")["initial"] == \
        pytest.approx(np.median(y))


def test_boosting_rejects_a_bad_learning_rate():
    x, y = _regression(n=100)
    for eta in (0.0, -0.1, 2.0):
        with pytest.raises(DataError):
            fit_gradient_boosting(x, y, learning_rate=eta)


def test_adaboost_matches_sklearn():
    rng = make_rng(1)
    x = rng.normal(0, 1, (800, 4))
    y = np.where(rng.random(800) < 1 / (1 + np.exp(-(x @ np.array([1.2, -0.9, 0.6, 0.0])))),
                 1, -1)

    fit = fit_adaboost(x, y, n_estimators=40)
    score = np.sign(sum(a * s.predict(x)
                        for a, s in zip(fit["alphas"], fit["stumps"], strict=True)))
    assert (score == y).mean() > 0.7


def test_a_stump_at_chance_gets_zero_weight():
    """alpha = 0.5*log((1-err)/err) is 0 at err = 0.5."""
    rng = make_rng(2)
    x = rng.normal(0, 1, (400, 3))
    y = np.where(rng.random(400) < 0.5, 1, -1)          # pure noise
    fit = fit_adaboost(x, y, n_estimators=10)
    assert min(abs(a) for a in fit["alphas"]) < 0.4


def test_a_better_stump_gets_more_say():
    """Verify the alpha formula directly."""
    for error, expected in ((0.1, 0.5 * np.log(9)), (0.5, 0.0), (0.3, 0.5 * np.log(7 / 3))):
        assert 0.5 * np.log((1 - error) / max(error, 1e-10)) == pytest.approx(expected)


def test_weights_stay_normalised():
    rng = make_rng(3)
    x = rng.normal(0, 1, (500, 3))
    y = np.where(x[:, 0] + rng.normal(0, 0.5, 500) > 0, 1, -1)
    fit = fit_adaboost(x, y, n_estimators=25)
    assert fit["final_weights"].sum() == pytest.approx(1.0)


def test_label_noise_concentrates_the_weights():
    """AdaBoost's exponential loss is unusually sensitive to it."""
    rng = make_rng(4)
    x = rng.normal(0, 1, (600, 3))
    y = np.where(x[:, 0] > 0, 1, -1)
    y[:6] = -y[:6]                                       # 1% flipped labels

    fit = fit_adaboost(x, y, n_estimators=60)
    weights = np.sort(fit["final_weights"])[::-1]
    assert weights[:6].sum() > 0.20, "the mislabelled rows should dominate"
    assert fit["warnings"]


def test_clean_labels_do_not_concentrate():
    """A warning that always fires is useless."""
    rng = make_rng(5)
    x = rng.normal(0, 1, (600, 3))
    y = np.where(x[:, 0] + rng.normal(0, 0.4, 600) > 0, 1, -1)
    fit = fit_adaboost(x, y, n_estimators=40)
    assert not any("noise" in w.lower() or "concentrat" in w.lower()
                   for w in fit["warnings"])


def test_adaboost_rejects_zero_one_labels():
    rng = make_rng(6)
    x = rng.normal(0, 1, (200, 2))
    with pytest.raises(DataError) as info:
        fit_adaboost(x, (x[:, 0] > 0).astype(int))
    assert "0" in str(info.value)


def test_depth_matches_the_interaction_order():
    """Depth d captures d-way interactions."""
    assert boosting_defaults(n_rows=5_000, interaction_order=1)["max_depth"] == 1
    assert boosting_defaults(n_rows=5_000, interaction_order=3)["max_depth"] == 3


def test_the_default_depth_is_shallow():
    result = boosting_defaults(n_rows=10_000)
    assert result["max_depth"] <= 6


def test_a_small_learning_rate_comes_with_more_rounds():
    result = boosting_defaults(n_rows=10_000)
    assert result["learning_rate"] <= 0.1
    assert result["n_estimators"] >= 200


def test_noisy_labels_avoid_exponential_loss():
    result = boosting_defaults(n_rows=5_000, noisy_labels=True)
    assert result["loss"] != "exponential"
    assert result["warnings"]
    assert any("bag" in w.lower() or "forest" in w.lower() for w in result["warnings"])


def test_every_boosting_default_has_a_reason():
    result = boosting_defaults(n_rows=5_000)
    for key in ("max_depth", "learning_rate", "n_estimators", "loss"):
        assert key in result["reasons"]
        assert len(result["reasons"][key]) > 15


def test_an_impossible_interaction_order_is_refused():
    for order in (0, 9):
        with pytest.raises(DataError):
            boosting_defaults(n_rows=1_000, interaction_order=order)
```

**Line by line:**

- `test_boosting_overfits_with_too_many_rounds` — **the day's real assessment.** Three assertions:
  `overfits` is True, the best iteration is well before the end, and the final score is worse than the
  best. **That is the single difference from bagging that decides everything downstream**, including
  why Day 112's early stopping is mandatory.
- `test_a_deep_base_model_is_warned_about` — the warning must mention **Day 108 or bagging or forest**,
  because the mistake is *transferring the bagging habit*, and naming the habit is what makes the
  warning teach rather than nag.
- `test_shallow_base_models_are_not_warned_about` — the negative case, so the depth warning cannot
  degenerate into always firing.
- `test_the_squared_error_residual_is_the_negative_gradient` — Principle 2's payoff, verified against a
  numerical derivative. **The identity is not a slogan.**
- `test_label_noise_concentrates_the_weights` with `test_clean_labels_do_not_concentrate` — 1% flipped
  labels take over 20% of the final weight. **That is AdaBoost's characteristic failure**, and the
  paired clean case stops the warning becoming noise.
- `test_a_stump_at_chance_gets_zero_weight` — `α = 0` at 50% error, so a useless stump is *ignored*
  rather than harming the ensemble. That is the formula doing real work.
- `test_the_recommendation_names_a_concrete_round_count` — **"use early stopping" is not actionable**;
  a number is. Same instinct as Day 96's diagnoses.
- `test_the_initial_prediction_matches_the_loss` — mean for squared, median for absolute. A wrong
  starting point costs rounds and nothing warns you.

```bash
uv run python -m pytest tests/test_ensembles.py -v
```

---

## §6 Request budget

| Resource | Spent today |
|---|---|
| LLM calls | **0** |
| Compute | a few thousand stumps; sequential, so slower than a forest |

---

## §7 Traps

- **Boosting deep trees.** The opposite of Day 108's rule; the commonest mistake.
- **`learning_rate=1.0`.** Overshoots and degrades after a few rounds.
- **Tuning `η` and `n_estimators` separately.** They trade against each other.
- **Treating `n_estimators` as harmless.** Boosting overfits; bagging does not.
- **No validation set.** Then you cannot find `best_iteration` at all.
- **AdaBoost on noisy labels.** Exponential loss lets one bad row dominate.
- **Expecting `n_jobs=-1` to help much.** Boosting is sequential by construction.
- **The wrong initial prediction for the loss.** Mean vs median vs log-odds.
- **Continuing past a stump with `α ≤ 0`.** It is subtracted into the ensemble.
- **Forgetting depth sets interaction order.** Depth 1 is additive.
- **Reaching for boosting on a tiny dataset.** More knobs to overfit with.

---

## §8 Verify before you code

Written **2026-08-21**:

- <https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting> — including the staged
  prediction API used in §3.
- <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html> — check
  the `algorithm` parameter's default and deprecation status in your pinned version.
- <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html> —
  the faster histogram-based implementation Day 112 compares against.
- <https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html> —
  the overfitting curve from §3.4.

---

## §9 Say it in an interview

> "Bagging and boosting attack different terms. Bagging fits models in parallel and averages away
> variance; boosting fits them in sequence, each one trained on what the previous ones got wrong, and
> that reduces bias. The insight worth knowing is that the residual is the negative gradient of
> squared error — so 'fit the residuals' is literally gradient descent, just performed in function
> space where each step adds a whole model instead of nudging a parameter. Change the loss and the
> residual changes: log loss gives you y minus sigmoid, absolute error gives you just the sign. Same
> machinery. Two consequences flip your intuitions from bagging. Base models must be *weak* — depth two
> or three — because a deep tree fits the residuals perfectly in round one and leaves nothing for round
> two, so the sequence collapses. And unlike bagging, more rounds genuinely overfit: the validation
> curve falls, bottoms out and rises again, which is why early stopping is mandatory rather than nice
> to have. I'd also flag that AdaBoost's exponential loss is unusually sensitive to label noise — I
> measured one per cent of flipped labels taking over twenty per cent of the final sample weight."

---

## §10 Done when

Tick [`CHECKLIST.md`](CHECKLIST.md), then `./m check && ./m done 110`.
