# Review Queue

Keep only useful prompts for unaided delayed recall or changed-context transfer. Every item must point to source evidence. This is the sole source of truth for review due dates, prompts, and acceptance criteria. It is a visible queue, not a notification service or scheduling engine.

A review may target a vocabulary chunk, listening discrimination, reading reasoning, speaking response, or writing capability. Do not reveal the prior answer, target phrasing, or correction notes before the learner attempts it.

## Due

No reviews due.

## Later

### time-suffix-ish
Due: 2026-08-26
Type: delayed recall
Skill: Vocabulary — productive
Source evidence: 2026-08-25 baseline session
Related vocabulary or error item: `learner/VOCABULARY.md#-ish-time-suffix`
Parallel material or exact selection constraint: Time expression
Unaided prompt: Bạn hẹn gặp bạn bè vào khoảng tầm 8 giờ tối. Hãy diễn đạt câu ngắn gọn bằng tiếng Anh có dùng hậu tố nói giờ xấp xỉ vừa học.
Vocabulary retrieval cue, when applicable: Let's meet at 8____.
Target decision: Recall and use `-ish` attached to time.
Contrast if confused, hidden until after the attempt: `-ish` vs `about / around`
Acceptance criteria: Produces `8ish` or `around 8ish`.
After attempt: complete

### have-toast-for-breakfast
Due: 2026-08-26
Type: delayed recall
Skill: Vocabulary — sound & productive
Source evidence: 2026-08-25 baseline session
Related vocabulary or error item: `learner/VOCABULARY.md#have-toast-for-breakfast`
Parallel material or exact selection constraint: Breakfast food
Unaided prompt: Nói câu tiếng Anh: "Tôi thường ăn bánh mì nướng vào buổi sáng". Chú ý phát âm đúng từ bánh mì nướng (không nhầm với răng).
Vocabulary retrieval cue, when applicable: I usually have _____ for breakfast.
Target decision: Retrieve `toast` (/təʊst/).
Contrast if confused, hidden until after the attempt: `toast` /təʊst/ vs `tooth` /tuːθ/
Acceptance criteria: Produces `toast` correctly.
After attempt: complete

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
