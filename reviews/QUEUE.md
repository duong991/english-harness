# Review Queue

Keep only useful prompts for unaided delayed recall or changed-context transfer. Every item must point to source evidence. This is the sole source of truth for review due dates, prompts, and acceptance criteria. It is a visible queue, not a notification service or scheduling engine.

A review may target a vocabulary chunk, listening discrimination, reading reasoning, speaking response, or writing capability. Do not reveal the prior answer, target phrasing, or correction notes before the learner attempts it.

## Due

No reviews due.

## Later

No later reviews scheduled.

## Item format

```markdown
### Short capability name

Due:

Type: delayed recall | changed-context transfer

Skill:

Source evidence:

Related vocabulary or error item:

Unaided prompt:

Acceptance criteria:

After attempt: complete | defer with reason | replace with a nearer/simpler check
```

Choose the next interval from unaided performance using the policy in `docs/LEARNING_PATH.md`. The weekly review date and latest weekly scores belong in `learner/LEARNING_STATE.md`, not in this queue.
