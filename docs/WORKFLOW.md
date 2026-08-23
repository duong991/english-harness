# Recording and Review Workflow

Read only the section needed for the current interaction. Runtime routing and teaching behavior live in `.agents/skills/learn/SKILL.md`; pedagogy recipes live in `docs/LEARNING_PATH.md`.

## File ownership

| File | Owns |
| --- | --- |
| `learner/PROFILE.md` | Stable context, access constraints, and preferences |
| `learner/LEARNING_STATE.md` | Goal contract, time budget, baseline, cycle, skill plan, weekly sessions, and next action |
| `learner/VOCABULARY.md` | Active chunks and independent evidence |
| `learner/ERRORS.md` | Recurring or high-impact patterns |
| `reviews/QUEUE.md` | All delayed-review timing, prompts, and acceptance criteria |
| `sessions/` | Raw attempts and meaningful dated evidence |

Do not duplicate review due dates in vocabulary. Do not duplicate the active goal or weekly plan in the profile.

## Complete a plan

A cycle plan is ready only when:

- the goal contract and study capacity are actionable;
- available skill evidence is sufficient to identify a provisional gap;
- environment-limited evidence is labeled and given a later collection opportunity;
- the skill plan names weekly frequency and main method for every relevant area;
- this week's sessions have a duration, focus, evidence target, and schedule or ordered slot;
- the next action is concrete.

Prefer specific frequency such as “speaking 3× this week” over vague priority labels. Use the learner's preferred days, time, timezone, and missed-session fallback. If those are unknown, schedule an ordered session slot and collect calendar preferences without blocking practice.

## Record a meaningful session

Create `sessions/YYYY-MM-DD-short-topic.md` only for reusable evidence: diagnostic output, an unaided attempt and learner retry, delayed review, weekly review, or assessment.

```markdown
# Session — Short topic

## Goal link and task

## Conditions and material

## Input or target language

## Unaided attempt

## Self-noticing

## Feedback

## Learner retry

## Skill evidence

## Follow-up
```

Use only applicable sections. Keep the raw attempt intact and never invent learner output. A lookup, explanation, tiny question, or abandoned exercise does not need a session file.

## Weekly review

If a short due recall can supply retention evidence within today's budget, run it before scoring the week.

Score each dimension from 0 to 2 and cite brief evidence:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Completion | Important work not attempted | Partly completed | Important planned work completed |
| Quality | Meaning often failed | Meaning mostly arrived with limits | Current task criteria met |
| Retention | Little unaided recall | Partial or unstable recall | Useful delayed recall |
| Transfer | No changed-context use | Assisted or partial transfer | Independent transfer |

Also note repeated, improving, and new errors; material fit; and energy or recovery. Change one important variable for the next week, then refresh the skill plan only where that change matters, schedule the next week's sessions, and set the next action.

## Explicit assessment

Assessment runs only when requested. Agree on observable conditions before starting. Do not teach, hint, rewrite, or reveal target language until submission. Preserve raw output and record separate skill performance, confidence, limitations, and the next learning implication. Do not claim official CEFR certification or a validated exam score.

## Finish state updates

After meaningful work:

- append the session record;
- update `PROFILE.md` only when stable context or preferences changed;
- update `LEARNING_STATE.md` when goal, baseline, plan, bottleneck, evidence, weekly schedule, or next action changed;
- update vocabulary and errors only from useful evidence;
- add, complete, defer, replace, or remove queue items as review needs change.

The next action must include task, duration, material when known, evidence and acceptance criteria, reason, and the best available date/time or delay condition. Notification delivery remains outside the repository.
