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

Parallel material or exact selection constraint:

Unaided prompt:

Vocabulary retrieval cue, when applicable:

Target decision:

Contrast if confused, hidden until after the attempt:

Acceptance criteria:

After attempt: complete | defer with reason | replace with a nearer/simpler check
```

Choose the next interval from unaided performance using the policy in `docs/LEARNING_PATH.md`. The weekly review date and latest weekly scores belong in `learner/LEARNING_STATE.md`, not in this queue.

For listening or reading transfer, use different content with similar difficulty and the same capability demand. Replaying or rereading the original may check memory, but it does not establish transfer.

For vocabulary, the cue must provide enough context to force retrieval without showing the target, its first letters, or a near-copy of the source sentence. Test one decision at a time: sense, sound recognition, collocation, register, or productive use. Keep verification and the full knowledge record in the linked vocabulary entry; reveal a contrast only after the learner attempts.

If the learner says an unrecorded vocabulary item is “due,” do not create a retroactive due entry or invent source evidence. Run and record an `Unrecorded carry-in baseline` first, then schedule the first future review from that observed result when the verified item is worth keeping.
