# Day 91 — CHECKLIST

**IDs covered:** ML-01, ML-02 · **Principles served:** 1, 7, 10

## Demo command

```bash
uv run python days/day-91/lab/framing.py
uv run python -m pytest tests/test_framing.py -v
```

Expected: the eight-part report ending with where this plan sits, then all framing tests green.

## Setup

- [ ] `./m start 91` and `./m scaffold 91` run
- [ ] Files created: `days/day-91/lab/framing.py`, `src/setu/framing.py`, `tests/test_framing.py`

## ML-01 — the terms

- [ ] Can draw the nesting from memory
- [ ] Can give an AI system that contains no learning
- [ ] Can say why data science is **not** in the hierarchy
- [ ] Can say what fraction of this plan so far used no model
- [ ] Can state one thing deep learning is genuinely worse at than boosted trees

## Does this need a model

- [ ] Ran `does_this_need_a_model()` and read all five rows
- [ ] Can state the question that comes **before** "what model should I use?"
- [ ] Can say why an approximation of something countable is worse in every respect

## The label question

- [ ] Can state all four questions from memory
- [ ] Can say which one kills projects, and why
- [ ] Can give the canonical example of a label unavailable at prediction time
- [ ] Can connect question 1 to Day 87 and question 3 to Day 88

## ML-02 — the four types

- [ ] Filled in the four-row table from memory
- [ ] Ran `supervised_and_unsupervised()` on the same data
- [ ] Confirmed the clusters did **not** align with quality
- [ ] Can state unsupervised learning's central difficulty
- [ ] Can say when semi-supervised is worth it, and how it fails silently
- [ ] Can name the three things that make RL harder than supervised learning
- [ ] Can say why this plan solves Day 199's problem with rules rather than RL

## Framing

- [ ] Ran `the_framing_changes_everything()`; read all five framings
- [ ] Can say when the framing decision gets made and how often it is revisited
- [ ] Read `where_this_plan_sits()`
- [ ] Can say what self-supervised learning is, and what bottleneck it dissolves

## Build brief

- [ ] `classify_problem` — **TODO(me)**: `computable_exactly` takes **precedence**
- [ ] Prediction-time failure returns **blocking**, not a warning
- [ ] `choose_task` — **TODO(me)**: ordinal gets its own task, every task has a baseline
- [ ] `assert_label_is_usable` — **TODO(me)**: names every failure, each with a remedy
- [ ] `framing_options` — **TODO(me)**: 'no model' first, options never a recommendation
- [ ] `describe_framing` — **TODO(me)**: avoids "AI", names the baseline
- [ ] Can explain why `framing_options` refuses to recommend

## Tests that must be able to fail

- [ ] `test_an_exactly_computable_question_needs_no_model` — green
- [ ] `test_computable_exactly_beats_everything_else` — green ← **today's real assessment**
- [ ] **Checked labels before computability, watched it go red, reordered** ← do not skip
- [ ] `test_labels_unavailable_at_prediction_time_is_blocking` — green
- [ ] **Made it a warning instead, watched it go red, reverted** ← do not skip
- [ ] `test_supervised_when_labels_exist` — green
- [ ] `test_unsupervised_when_no_labels` — green (with a warning)
- [ ] `test_semi_supervised_when_labels_are_scarce` — green
- [ ] `test_plentiful_labels_are_not_semi_supervised` — green
- [ ] `test_reinforcement_when_there_is_a_reward` — green
- [ ] `test_the_reason_names_the_deciding_input` — green
- [ ] `test_ratio_target_is_regression` — green
- [ ] `test_binary_and_multiclass_are_distinguished` — green
- [ ] `test_an_ordinal_target_gets_its_own_task` — green
- [ ] `test_every_task_comes_with_a_baseline` — four green cases
- [ ] `test_nominal_without_a_class_count_raises` / `test_an_unknown_level_raises` — green
- [ ] `test_a_missing_label_is_refused` — green
- [ ] `test_a_derived_label_is_refused` — green
- [ ] `test_an_unavailable_label_names_the_classic_example` — green
- [ ] `test_too_few_labels_is_refused` — green
- [ ] `test_every_failure_is_reported_not_just_the_first` — green
- [ ] `test_the_messages_say_what_to_do` — green
- [ ] `test_a_usable_label_passes` — green
- [ ] `test_the_no_model_option_comes_first` — green
- [ ] `test_every_option_states_what_it_requires` — green
- [ ] `test_framing_returns_options_not_a_recommendation` — green
- [ ] `test_unlabelled_data_gets_fewer_supervised_options` — green
- [ ] `test_an_empty_description_raises` — green
- [ ] `test_the_description_avoids_the_word_ai` — green
- [ ] `test_the_description_names_the_baseline` — green
- [ ] `test_describe_rejects_a_malformed_result` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Draw the nesting and place data science relative to it
- [ ] What question comes before "what model should I use?"
- [ ] Give the four label questions and say which kills projects
- [ ] What is unsupervised learning's central difficulty?
- [ ] When is semi-supervised worth it, and how does it fail?
- [ ] Name three things that make RL harder
- [ ] Why does this plan not use RL for the agent?
- [ ] Take one dataset and frame it five ways

## Commit

- [ ] `./m check && ./m done 91` succeeded
