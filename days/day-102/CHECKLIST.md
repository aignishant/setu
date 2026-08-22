# Day 102 — CHECKLIST

**IDs covered:** ML-13 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-102/lab/bayes_classifier.py
uv run python -m pytest tests/test_models.py -v
```

Expected: the eight-part report including the correlation and calibration comparisons, then all model
tests green.

## Setup

- [ ] `./m start 102` and `./m scaffold 102` run
- [ ] `days/day-102/lab/bayes_classifier.py` created
- [ ] No new packages installed

## ML-13 — the assumption

- [ ] Ran `why_the_assumption_is_needed()`; recorded combinations at 20 features
- [ ] Can state the naive assumption in one sentence
- [ ] Can say how many parameters it saves
- [ ] Can give a concrete example of the assumption being false

## Counting

- [ ] Computed the likelihood table **by hand** and matched sklearn
- [ ] Can say why training needs no iteration at all
- [ ] Found a word with a likelihood ratio near 1
- [ ] Can say why that makes a stopword list unnecessary

## Logs and smoothing

- [ ] Ran `why_logs_are_mandatory()` and saw the direct product hit **exactly 0.0**
- [ ] Can say what happens to the argmax when every class scores zero
- [ ] Can explain the log-sum-exp trick and why subtracting the max is safe
- [ ] Ran `why_smoothing_is_mandatory()`; recorded the number of zero cells
- [ ] Can say what one unseen word does without smoothing
- [ ] Can describe alpha as a **prior**, and name the Day-72 connection

## Why it survives

- [ ] Ran `the_assumption_is_false()` with duplicated features
- [ ] Recorded AUC and Brier for both cases
- [ ] Can explain why the **argmax** usually survives
- [ ] Ran `rankings_are_good_probabilities_are_not()`
- [ ] Recorded the fraction of predictions above 0.99: ______
- [ ] Can state the day's conclusion in one sentence
- [ ] Can say what to do if you need real probabilities

## The variants

- [ ] Fitted all three and can say what `P(feature|class)` is in each
- [ ] Can say what Bernoulli does that multinomial-on-binary does not
- [ ] Can name Gaussian NB's distributional assumption
- [ ] Can say why `StandardScaler` breaks MultinomialNB
- [ ] Read `when_it_is_the_right_choice()`; can say what a failure to beat it implies

## Build brief

- [ ] `fit_naive_bayes` — **TODO(me)**: three variants, log space, variance floor
- [ ] `predict_log_proba` — **TODO(me)**: log-sum-exp normalisation
- [ ] `naive_bayes_proba` — **TODO(me)**: docstring warns about calibration
- [ ] `evidence_per_feature` — **TODO(me)**: likelihood ratios, uninformative bucket
- [ ] `independence_violation` — **TODO(me)**: **within-class** correlation
- [ ] Can explain why overall correlation is the wrong measurement

## Tests that must be able to fail

- [ ] `test_multinomial_matches_sklearn` — green
- [ ] `test_probabilities_match_sklearn` / `..._sum_to_one` — green
- [ ] `test_log_space_survives_a_long_document` — green
- [ ] `test_the_naive_exponential_would_underflow` — green
- [ ] **Exponentiated without shifting, watched an 800-word document give 0/0** ← do not skip
- [ ] `test_smoothing_prevents_a_zero_likelihood` — green
- [ ] `test_zero_alpha_warns_or_produces_infinities` — green
- [ ] `test_more_smoothing_flattens_the_likelihoods` — green
- [ ] `test_multinomial_rejects_negative_values` — green
- [ ] `test_gaussian_matches_sklearn` — green
- [ ] `test_gaussian_survives_a_constant_feature_within_a_class` — green
- [ ] `test_bernoulli_penalises_absent_features` — green
- [ ] `test_an_unknown_variant_raises` / `test_a_class_with_one_example_raises` — green
- [ ] `test_correlated_features_barely_hurt_the_ranking` — green ← **today's real assessment**
- [ ] `test_correlated_features_ruin_the_probabilities` — green ← **and its pair**
- [ ] `test_the_probabilities_are_overconfident` — green
- [ ] `test_the_proba_docstring_warns_about_calibration` — green
- [ ] `test_uninformative_features_are_identified` — green
- [ ] `test_evidence_ranks_by_the_likelihood_ratio` — green
- [ ] `test_evidence_refuses_multiclass` — green
- [ ] `test_violation_uses_within_class_correlation` — green
- [ ] **Used overall correlation, watched conditionally-independent features flag as severe** ← do not skip
- [ ] `test_duplicated_features_are_flagged_as_severe` — green
- [ ] `test_the_consequence_names_ranking_and_probabilities` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the naive assumption and give an example of it failing
- [ ] Why does the model work despite the assumption being false?
- [ ] What exactly degrades when features are correlated, and what does not?
- [ ] Why is log space mandatory rather than preferred?
- [ ] Explain the log-sum-exp trick
- [ ] What does smoothing prevent, and what is alpha really?
- [ ] Why must the independence check use within-class correlation?
- [ ] When would you not use Naive Bayes?

## Commit

- [ ] `./m check && ./m done 102` succeeded
