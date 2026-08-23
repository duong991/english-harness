# Agent Workflow

## Read the right context

Before a meaningful session, read `AGENTS.md`, then the learner profile, progress, active vocabulary, recurring errors, and review queue. Read `docs/LEARNING_PATH.md` when selecting level, material, or a skill recipe. Read only the relevant recent session when it helps; do not load every historical session by default.

## Choose the next action

When the learner invokes `$start`, asks for help starting to learn English, or their practical profile is not yet established, use `.agents/skills/start/SKILL.md`. Start by identifying the learner's primary purpose and real situations for English. This is lightweight goal discovery, placement, and first learning—not a formal assessment.

When the learner asks to study:

1. If a useful item in `reviews/QUEUE.md` is due, do that review first.
2. Otherwise use `learner/PROGRESS.md`, `learner/VOCABULARY.md`, and `docs/LEARNING_PATH.md` to choose manageable material and one or more connected skill activities aligned with the learner's priorities.
3. Use a changed-context task when checking retention or transfer. If the learner has no practical evidence yet but asks to practise, begin with a simple familiar task rather than an advanced work scenario.

When the learner asks for a review, use `.agents/skills/review/SKILL.md`. When they ask for a baseline or milestone check, use `.agents/skills/assess/SKILL.md`.

## Conduct a practice session

Use `.agents/skills/study/SKILL.md`. Do not turn a short interaction into unnecessary ceremony. The learner does not operate a state machine; the agent quietly follows the method.

A session may connect skills around one piece of meaningful material: for example, listen or read → identify a few useful chunks → retell or write. Use the applicable recipe in `docs/LEARNING_PATH.md`. For genuinely new language, give concise input first and then require retrieval or use without the source. For a retrieval or performance task, preserve the unaided-attempt → self-noticing → feedback → learner-retry sequence.

A meaningful session usually contains reusable learning evidence: an unaided attempt plus a learner-authored retry, an assessment, or a delayed review. Do not create a session file merely because a conversation happened; a tiny question, vocabulary lookup, explanation, or abandoned exercise does not need a record.

For a meaningful session, create `sessions/YYYY-MM-DD-short-topic.md` using this shape:

```markdown
# Session — Short topic

## Task

## Material and target language

## Attempt

## Self-noticing

## Feedback

## Retry

## What improved

## Skill evidence

## Follow-up
```

Keep the raw attempt as written. The added sections are optional when they do not fit the session. Use `Not completed` only for sections the learner deliberately did not reach; do not invent learner output.

## Update repository truth sparingly

After a meaningful session:

- append the session record;
- update `PROFILE.md` when the learner's goal, primary situations, priorities, or material preferences genuinely changed;
- update `PROGRESS.md` when the primary purpose, skill profile, phase, priority, bottleneck, progress, placement, assessment, or next work genuinely changed;
- update `VOCABULARY.md` only for chunks that are active and have useful source or performance evidence;
- add or revise an item in `ERRORS.md` only for patterns supported by repeated or high-impact evidence;
- add, complete, defer, or remove useful prompts in `reviews/QUEUE.md`.

Do not create duplicate summaries, fake metrics, or administrative records. If no durable update is useful, leave the learner files unchanged.
