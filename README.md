# English Learning Harness

> **The learner learns English. The harness keeps the goal, evidence, learning direction, and next useful action legible to the AI.**

This is an agent-native, Markdown-first English-learning repository. Open it in Codex, Claude Code, Cursor, or another capable agent and say, for example, “Let’s learn English.” The agent reads the learner state, chooses the right mode and task, runs a learner-first learning loop, and keeps only useful evidence current.

It is deliberately not an English-learning application: no CLI, database, model-provider integration, scheduler, state machine, or analytics layer. The agent is the runtime; the repository is portable memory; Git is optional history.

Vietnamese guide: [GUID.md](GUID.md).

## Start here

1. Open this repository with an AI coding agent.
2. In Codex, invoke `$learn`; elsewhere, ask “Help me learn English.”
3. On the first run, provide three things: the real task English should enable, its deadline, and your realistic weekly time and preferred schedule. The agent drafts the conditions, success criteria, and comparable evidence for confirmation instead of turning onboarding into a long interview.
4. The same run normally includes a short micro-diagnostic or practice. The agent builds an adaptive baseline for listening, reading, speaking, writing, and receptive/productive vocabulary over one or more sessions.
5. Once the available evidence is sufficient, the agent records a cycle direction, a frequency-based skill plan, concrete sessions and exact listening/reading materials for the week, and the smallest next action in [learner/LEARNING_STATE.md](learner/LEARNING_STATE.md).

The learner uses one interface. `$learn` quietly routes to onboarding, diagnostic, today's lesson, a due review, weekly review, or a controlled assessment when explicitly requested.

For listening and reading, the agent selects a specific material or exact excerpt and explains why it fits the goal, level, time, useful language, available evidence, and learner interests. It does not delegate a vague podcast/article search or dump a source list.

## Repository map

```text
AGENTS.md                       agent entrypoint and non-negotiable rules
GUID.md                         Vietnamese learner guide
docs/METHOD.md                  goal-driven learning principles
docs/WORKFLOW.md                state ownership, session records, assessment, and weekly review
docs/LEARNING_PATH.md           adaptive diagnostic and level-aware skill recipes
learner/PROFILE.md              stable context, constraints, and preferences
learner/LEARNING_STATE.md       central goal, baseline, skill/vocabulary cycles, week, materials, and next action
learner/VOCABULARY.md           active chunks, verification, and evidence across skills
learner/ERRORS.md               recurring patterns worth revisiting
sessions/                       raw attempts and meaningful session evidence
reviews/QUEUE.md                delayed recall and changed-context transfer prompts
.agents/skills/learn/SKILL.md   the single learner-facing Codex skill
```

## Learning model

```text
real goal
  → adaptive baseline by skill
  → gap + time budget
  → cycle direction
  → skill plan + this week's sessions
  → exact material selection
  → today's smallest task
  → learn / retrieve / produce
  → self-noticing / feedback / retry
  → delayed recall / transfer
  → update state
  → weekly review and one adjustment
```

Vocabulary and reusable chunks connect listening, reading, speaking, and writing; they are not a separate fifth subject. When vocabulary is a bottleneck, `$learn` runs a goal-linked weekly theme: retrieve due chunks, select and verify a few items from real material, use one-decision cues, require changed-context output, and schedule later transfer.

## Non-negotiable boundaries

- New language may receive a small comprehensible input before closed-source retrieval.
- Known or practised language is attempted unaided before feedback.
- Assisted output is never counted as independent ability.
- Practical estimates remain separate by skill and are not official CEFR certification.
- Audio or recording limits leave the affected skill unknown; they do not block a provisional plan for available skills.
- Playback time, pages, or words consumed do not complete listening or reading; the learner must produce the relevant Evidence Contract.
- Vocabulary cues must force retrieval without revealing the target; important language claims require a learner dictionary, trusted source, or corpus evidence.
- Vocabulary stores knowledge and evidence; `reviews/QUEUE.md` alone stores review timing and prompts.
- Every meaningful session leaves a concrete next action with an expected duration and evidence target.
- Markdown decides what happens next; notification delivery remains the host's responsibility.

Read [docs/WORKFLOW.md](docs/WORKFLOW.md) for recording and review rules, or [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) for diagnostic and skill recipes.
