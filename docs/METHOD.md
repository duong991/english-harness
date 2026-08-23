# Learning Method

## Purpose

The goal is independent English performance in real contexts, not a better AI-assisted artifact. The harness makes a learner's goals, evidence, recurring patterns, and next useful action legible to an AI coach.

## System model

```text
goal discovery and context
  → quick placement
  → skill profile + learning path
  → material and comprehensible input
  → closed-source retrieval and performance
  → self-noticing, bounded feedback, learner retry
  → delayed recall or changed-context transfer
  → updated learner state
```

The system is a routing guide, not a fixed course. `docs/LEARNING_PATH.md` describes what a learner with a given practical profile is likely to need; `learner/PROGRESS.md` records this learner's current evidence and next action.

## Placement and assessment

`start` first discovers what English should enable for this learner and the real situations that matter. Quick placement then answers, “Where should we start?” It is low-stakes, can be spread across sessions, and keeps a raw sample for each of listening, reading, speaking, and writing. It may use provisional practical ranges such as “roughly A2”; it never claims certification.

Assessment answers, “How has this learner performed under stated conditions?” It is controlled and unaided, and happens only when the learner explicitly asks for it. A quick placement is not an exam.

## Learning loops

### Retrieval and performance

1. Choose one concrete, meaningful task just above the learner's current independent ability.
2. Ask for an unaided attempt, then ask what the learner noticed: uncertainty, missing language, weak organization, or unclear meaning.
3. Give at most two or three high-value corrections. Prioritize meaning, comprehensibility, organization, then language form. Quote the learner's own words and give a hint or useful chunk rather than a replacement answer.
4. Require a learner-authored retry.
5. Briefly compare the attempt and retry. Record only evidence that is useful later.

### Acquisition of genuinely new language

1. Use a small, relevant input: a short audio, text, dialogue, or set of three to eight useful chunks.
2. Make meaning, pronunciation or sound, collocation, and register clear enough to understand the input. Do not overload the learner with explanation.
3. Close or remove the source. Ask the learner to recognise, retrieve, say, or write the new language in a related situation.
4. Treat only the closed-source use as learner evidence. Plan a later recall or transfer when it would improve retention.

## What counts as evidence

Raw placement samples, attempts, learner retries, later unaided recall, and transfer to a new context are evidence. An AI rewrite, model example, explained input, or corrected version produced by the agent is not independent learner evidence.

Use scores only when they clarify a decision. Keep the conditions in plain language and do not present them as CEFR certification or a validated universal metric.

## Feedback boundaries

- Never provide corrective feedback on performance before an attempt and self-noticing.
- Do not withhold a small, comprehensible introduction when the target language is genuinely new. Follow it with closed-source retrieval or use.
- Do not rewrite an answer in normal practice.
- Correct the smallest set of issues that will materially improve the next attempt.
- Teach useful chunks in the task's context, not isolated grammar lectures.
- Mark factual, high-stakes, or uncertain claims for verification rather than treating AI judgment as final.

## Skill balance and material

Keep distinct practical evidence for listening, reading, speaking, and writing. Over a useful learning period, touch all four; do not divide time equally by default. The learner's goal, current profile, and bottlenecks determine the priority skill and material.

Choose material that is interesting, lawful to use, and manageable enough to finish. If unfamiliar language blocks nearly every sentence, reduce length or complexity and build the needed chunks first. Listening material needs an accessible, reliable transcript for intensive work; do not pretend written text measures listening.

## Retention and transfer

Use reviews as visible prompts, not a mandatory algorithm. A useful review asks the learner to retrieve a capability unaided after time has passed. A useful transfer retains the capability but changes scenario, topic, audience, or wording. Do not reveal the old answer before the new attempt.

## Privacy

Keep sensitive audio, transcripts, customer material, credentials, and unredacted employer information out of ordinary repository files. Sanitize any real work example before using it with an agent.
