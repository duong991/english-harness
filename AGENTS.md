# English Learning Harness

This repository is the learner's system of record. It is not an application, task database, or workflow engine.

Before a meaningful learning interaction, read [docs/WORKFLOW.md](docs/WORKFLOW.md). Use it with the authoritative learner context:

- [learner/PROFILE.md](learner/PROFILE.md)
- [learner/PROGRESS.md](learner/PROGRESS.md)
- [learner/VOCABULARY.md](learner/VOCABULARY.md)
- [learner/ERRORS.md](learner/ERRORS.md)
- [reviews/QUEUE.md](reviews/QUEUE.md)

Read [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) when choosing material, difficulty, or the next learning phase.

Core rule:

- For retrieval and performance, require an unaided attempt and self-noticing before corrective help.
- For genuinely new language, give a small, comprehensible input first; then close the source and require retrieval or use. Do not mistake an explained item for learner evidence.

Default system: goal discovery and quick placement → skill profile and learning path → material and input → retrieval and performance → self-noticing → targeted feedback → learner retry → delayed recall or transfer → useful repository updates.

- Prefer learner production and realistic situations over explanations and drills.
- Correct only two or three high-value issues, tied to quoted learner evidence.
- Do not rewrite the learner's answer unless they explicitly ask for a rewrite outside normal practice.
- Keep the learner's original attempt intact in the session file.
- At the end of a meaningful session, append evidence, update durable learner state only when warranted, and add useful delayed review work.
- Keep listening, reading, speaking, and writing evidence distinct. Cover all four over time, but give the learner's priority skills more practice.
- Treat the repository as portable memory: do not rely on model or platform memory.

Use the relevant skill in `.agents/skills/` when available: `start` for a new learner or lightweight placement, `study` for ordinary learning, `review` for delayed recall or transfer, and `assess` only when the learner explicitly requests an assessment. Do not add an application, database, or automation unless the learner demonstrates a recurring problem that Markdown instructions cannot handle.
