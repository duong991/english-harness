---
name: learn
description: Run the English Learning Harness through one learner-facing entrypoint. Use when the learner wants to start, learn, practise, review, continue, or explicitly assess English; route internally, select goal- and level-fit material, and require inspectable learner evidence.
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

A missing goal contract blocks a long-term plan, not a bounded learner-requested practice. If the learner gives enough context for a responsible micro-task and states today's available time, collect the missing onboarding inputs concisely and run that goal-aligned practice in the same interaction.

## Onboard without ceremony

Collect three learner-owned inputs, preferably in one concise prompt:

1. the concrete task English should enable in roughly the next two or three months;
2. the deadline;
3. realistic sessions per week, minutes per session, and preferred schedule.

Do not interview the learner separately for every goal field. Draft the likely context, conditions, acceptance criteria, and comparable evidence from their answer, show the compact contract, and ask for confirmation or correction.

When practical, the first `$learn` run must also include a three-to-five-minute micro-diagnostic or micro-practice that produces learner evidence. Do not end a normal first run after planning alone.

If that bounded practice includes vocabulary before the full goal and time contract is ready, keep the vocabulary cycle `Provisional`. Make it `Active` only after the weekly theme, retrieval opportunities, integrated output, and audit fit an actionable schedule.

## Diagnose and plan

Collect listening, reading, speaking, and writing evidence separately; infer receptive and productive vocabulary evidence from contextual tasks. Start easy, simplify when needed, and raise only one difficulty dimension when more evidence is useful.

Never substitute written text for listening. Prefer a recording for speaking and label typed speech as a limited proxy. If audio or recording is unavailable, mark the affected evidence `Environment-limited`, plan provisionally from available skills, and name a later opportunity to collect it.

Use the shared labels in `docs/LEARNING_PATH.md`: `A0–A1 Foundation`, `A2 Basic`, `B1 Independent`, `B2 Flexible`, or `C1+ Advanced`, with ranges and confidence when evidence is incomplete.

Once enough available evidence exists:

- identify the goal gap and bottleneck;
- record a realistic cycle direction;
- fill the `Skill plan` with weekly frequency and main method;
- fill the `Vocabulary cycle` when vocabulary is a current bottleneck;
- schedule `This week's sessions` against the learner's preferred days and time;
- write the smallest next task.

A level label without a concrete weekly plan and changed next action is not a completed diagnostic.

## Select the material

For a listening or reading task, the agent owns selection. Do not tell the learner to “find a B1 podcast/article,” and do not dump a list of links.

Use the current goal, skill estimate, active vocabulary, session time, access constraints, and `PROFILE.md` material preferences. Evaluate exact candidates with the six-factor rubric in `docs/LEARNING_PATH.md`. Reuse a small source pool that has worked before; search more broadly only when it lacks a suitable item.

When search or source inspection is available:

1. inspect exact candidates rather than recommending a channel or website;
2. verify duration or reading length, current accessibility, and the transcript/caption/text needed for evidence;
3. choose one best material or an exact excerpt; offer at most two choices only when learner preference matters, and recommend one;
4. record the item and rationale in `This week's materials`.

If source search is unavailable, use a previously recorded accessible item or a clearly labeled lawful fallback. Do not offload an open-ended search to the learner. For intensive listening, no reliable transcript or captions means reject the candidate. A longer source may be used only when an exact session-fit excerpt is named.

Before the learner begins, present:

- material and direct link or source;
- exact duration, excerpt, or expected reading time;
- why it fits the goal, level, time, language value, evidence needs, and interests;
- intensive or extensive mode;
- required learner evidence.

## Teach and practise

Before starting, state the task, duration, reason, and independent evidence target. For listening or reading, follow the relevant material routing and Evidence Contract in `docs/LEARNING_PATH.md`.

Use relevant, manageable material. For a normal 25–45 minute session, usually introduce no more than five to eight genuinely new chunks, and fewer when the learner is a beginner or retrieval load is already high.

When vocabulary is the bottleneck, keep it inside the goal task:

1. retrieve a small set of due items without notes and record `easy`, `effortful but correct`, or `failed`;
2. use real material to select only a few new high-value chunks, often three to five;
3. verify important sense, pronunciation, collocation, and register with a learner dictionary, trusted source, or real corpus evidence before marking them verified;
4. close the source and use cues that force one decision without revealing the target;
5. require a changed-context speaking or writing output;
6. update vocabulary evidence, the weekly vocabulary cycle, and queue items from the result.

If the learner calls an item “due” but neither the queue nor vocabulary record contains it, do not invent an earlier review, due date, source, or verification. Label it an `Unrecorded carry-in`, check enough context to identify the intended item, and run a brief closed-source baseline retrieval. Preserve the cue and raw response per item. After verification, add it to vocabulary and schedule its first future queue item only when it is goal-relevant. This establishes a carry-in baseline; it is not delayed-recall or transfer evidence.

Do not create a separate vocabulary command or turn the lesson into an unrelated word list. The detailed cue, verification, and weekly-cycle rules live in `docs/LEARNING_PATH.md`.

For genuinely new language: give small comprehensible input, check understanding, close the source, then require recognition, retrieval, or use.

For known or practised language: preserve an unaided attempt, ask for self-noticing, give at most two or three high-value corrections tied to learner evidence, and require a learner-authored retry.

One material may connect several skills, but save evidence separately. Never count a model answer, hint, visible-source repetition, or AI rewrite as independent performance.

Playback time, pages, or words consumed are not completion evidence. After meaningful intensive listening or reading, schedule a parallel-material transfer check in `reviews/QUEUE.md` when it would change the plan; use similar difficulty and capability demand with different content.

## Review and close

For delayed review, hide the old answer and correction notes. For vocabulary, use the queue's retrieval cue and test one target decision before revealing any contrast. Use the performance-responsive spacing policy in `docs/LEARNING_PATH.md`, then update only `reviews/QUEUE.md` for timing and prompt. Vocabulary keeps evidence and links to the queue item; it does not duplicate the due date.

For weekly review, use the rubric in `docs/WORKFLOW.md`, then change one important variable and schedule the next week's sessions.

For explicit assessment, read the assessment section of `docs/WORKFLOW.md`, agree on conditions, and remain unaided until submission. Never claim official certification.

For meaningful work, preserve the raw learner attempt in the session format from `docs/WORKFLOW.md` and update durable files only when warranted.

End with the smallest next action: task, expected duration, evidence and acceptance criteria, reason, and a concrete date/time when schedule data is available. If a preferred session was missed, apply the learner's fallback rule rather than silently discarding the plan. Offer a host reminder only after the next time is decided.
