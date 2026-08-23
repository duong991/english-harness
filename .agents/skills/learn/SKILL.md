---
name: learn
description: Run the English Learning Harness through one learner-facing entrypoint. Use when the learner wants to start, learn, practise, review, continue, or explicitly assess English; route internally from goal discovery and adaptive diagnostic to today's lesson, delayed review, weekly review, or controlled assessment.
---

# Learn

Always read `AGENTS.md` and `learner/LEARNING_STATE.md`. Load other context only when it changes today's decision:

- `PROFILE.md` for onboarding, constraints, or material fit;
- `reviews/QUEUE.md` when a review may be due;
- active vocabulary and errors relevant to today's task;
- only the relevant diagnostic or skill section of `docs/LEARNING_PATH.md`;
- the relevant part of `docs/WORKFLOW.md` when recording a session, weekly review, or assessment.

The learner uses one interface. Do not ask them to choose an internal mode.

## Route

1. Run an assessment only when explicitly requested.
2. If the goal contract or time budget is missing, onboard.
3. If the available baseline is insufficient to choose a responsible direction, diagnose adaptively. Environment-limited evidence is unknown, not perpetually missing, and must not block a provisional plan.
4. If a weekly review is due, first run any short due recall that can provide retention evidence within the session budget, then review the week.
5. Otherwise run a due delayed-recall or transfer item.
6. Otherwise run today's smallest goal-aligned lesson.

Honor a learner's specific task request when practical. Explain briefly when a prerequisite or environment limit changes the route.

## Onboard without ceremony

Collect three learner-owned inputs, preferably in one concise prompt:

1. the concrete task English should enable in roughly the next two or three months;
2. the deadline;
3. realistic sessions per week, minutes per session, and preferred schedule.

Do not interview the learner separately for every goal field. Draft the likely context, conditions, acceptance criteria, and comparable evidence from their answer, show the compact contract, and ask for confirmation or correction.

When practical, the first `$learn` run must also include a three-to-five-minute micro-diagnostic or micro-practice that produces learner evidence. Do not end a normal first run after planning alone.

## Diagnose and plan

Collect listening, reading, speaking, and writing evidence separately; infer receptive and productive vocabulary evidence from contextual tasks. Start easy, simplify when needed, and raise only one difficulty dimension when more evidence is useful.

Never substitute written text for listening. Prefer a recording for speaking and label typed speech as a limited proxy. If audio or recording is unavailable, mark the affected evidence `Environment-limited`, plan provisionally from available skills, and name a later opportunity to collect it.

Use the shared labels in `docs/LEARNING_PATH.md`: `A0–A1 Foundation`, `A2 Basic`, `B1 Independent`, `B2 Flexible`, or `C1+ Advanced`, with ranges and confidence when evidence is incomplete.

Once enough available evidence exists:

- identify the goal gap and bottleneck;
- record a realistic cycle direction;
- fill the `Skill plan` with weekly frequency and main method;
- schedule `This week's sessions` against the learner's preferred days and time;
- write the smallest next task.

A level label without a concrete weekly plan and changed next action is not a completed diagnostic.

## Teach and practise

Before starting, state the task, duration, reason, and independent evidence target.

Use relevant, manageable material. For a normal 25–45 minute session, usually introduce no more than five to eight genuinely new chunks, and fewer when the learner is a beginner or retrieval load is already high.

For genuinely new language: give small comprehensible input, check understanding, close the source, then require recognition, retrieval, or use.

For known or practised language: preserve an unaided attempt, ask for self-noticing, give at most two or three high-value corrections tied to learner evidence, and require a learner-authored retry.

One material may connect several skills, but save evidence separately. Never count a model answer, hint, visible-source repetition, or AI rewrite as independent performance.

## Review and close

For delayed review, hide the old answer and correction notes. Use the performance-responsive spacing policy in `docs/LEARNING_PATH.md`, then update only `reviews/QUEUE.md` for timing and prompt. Vocabulary keeps evidence and links to the queue item; it does not duplicate the due date.

For weekly review, use the rubric in `docs/WORKFLOW.md`, then change one important variable and schedule the next week's sessions.

For explicit assessment, read the assessment section of `docs/WORKFLOW.md`, agree on conditions, and remain unaided until submission. Never claim official certification.

For meaningful work, preserve the raw learner attempt in the session format from `docs/WORKFLOW.md` and update durable files only when warranted.

End with the smallest next action: task, expected duration, evidence and acceptance criteria, reason, and a concrete date/time when schedule data is available. If a preferred session was missed, apply the learner's fallback rule rather than silently discarding the plan. Offer a host reminder only after the next time is decided.
