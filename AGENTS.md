# English Learning Harness

This repository is the learner's portable system of record. It is not an application, database, scheduler, or workflow engine.

Use `.agents/skills/learn/SKILL.md` for every learner-facing interaction. `$learn` is the only public skill.

Authoritative learner context:

- `learner/LEARNING_STATE.md` — active goal, baseline, plan, week, and next action
- `learner/PROFILE.md` — stable context, constraints, and preferences
- `learner/VOCABULARY.md` — knowledge and evidence for active chunks
- `learner/ERRORS.md` — recurring high-impact patterns
- `reviews/QUEUE.md` — the sole source of review timing and prompts

Non-negotiable rules:

- Do not create a long-term plan without an actionable goal contract and realistic time budget. Learning may begin while these are being clarified.
- For new language, give small comprehensible input, close the source, then require retrieval or use. For practised language, require an unaided attempt and self-noticing before bounded feedback and a learner-authored retry.
- Never count explanations, hints, model answers, visible-source repetition, or AI rewrites as independent evidence.
- Keep listening, reading, speaking, writing, and receptive/productive vocabulary evidence distinct. An environment-limited skill remains unknown; it does not block a provisional plan for available skills.
- Prefer a small set of useful chunks from current material. Vocabulary stores what is known; the review queue stores when and how it will be tested.
- Preserve raw attempts. Correct only two or three high-value issues and update durable files only from useful evidence.
- End every meaningful session with a concrete next task, duration, evidence target, reason, and the best available date/time. The host may deliver reminders; the repository does not.
- At weekly review, inspect completion, quality, retention, transfer, errors, and energy; change one important variable.

Keep daily context lean: always read the skill and learning state; load the queue, profile, vocabulary, errors, the relevant part of `docs/LEARNING_PATH.md`, or `docs/WORKFLOW.md` only when the current decision needs them. `docs/METHOD.md` is rationale, not required daily context.
