# English Learning Harness

> **The learner learns English. The harness only makes the learner, learning method, history, and next useful action legible to the AI.**

This is an agent-native, Markdown-first English-learning repository. Open it in Codex, Claude Code, Cursor, or another capable agent and say, for example, “Let’s practise English.” The agent reads the repository, runs a learner-first practice loop, and keeps the useful learning record current.

It is deliberately not an English-learning application: no CLI, database, model-provider integration, scheduler, state machine, or analytics layer. The agent is the runtime; the repository is memory; Git is optional history.

Vietnamese guide: [GUID.md](GUID.md).

## Start here

1. Read [learner/PROFILE.md](learner/PROFILE.md) and fill in anything you already know; it is fine to leave the goal open.
2. Open this repository with an AI coding agent.
3. In Codex, start with `$start`; elsewhere, ask “Help me start learning English.” You can also ask to practise, review, or assess your progress.
4. `start` first identifies the learner's primary purpose and real situations for English, then runs lightweight, four-skill placement over one or more sessions. It is not a formal exam.
5. The agent follows [AGENTS.md](AGENTS.md), preserves your raw work in `sessions/`, and updates only useful durable state.

## Repository map

```text
AGENTS.md                   agent entrypoint and non-negotiable learning rules
GUID.md                     Vietnamese guide for learners and repository operation
docs/METHOD.md              learning principles
docs/WORKFLOW.md            agent operating workflow and session format
docs/LEARNING_PATH.md       level-aware routing and skill-specific lesson recipes
learner/PROFILE.md          goals, contexts, level, and preferences
learner/PROGRESS.md         current focus, bottleneck, progress, next work
learner/VOCABULARY.md       active chunks and their evidence of use
learner/ERRORS.md           recurring patterns worth revisiting
sessions/                   one human-readable Markdown record per meaningful session
reviews/QUEUE.md            useful delayed recall and transfer work
.agents/skills/             start, study, review, and assess agent behaviours
```

## Principles

- New language can be introduced in small, comprehensible pieces; retrieval and performance remain unaided and preserved.
- Feedback follows learner self-noticing and stays bounded.
- A retry belongs to the learner; AI does not ghostwrite it.
- The learner has a separate practical profile for listening, reading, speaking, and writing; priority skills get more time.
- Later recall and changed-context transfer matter more than a polished first result.
- Markdown files are authoritative. Agent memory is not.

Read [docs/WORKFLOW.md](docs/WORKFLOW.md) for the full interaction contract.
