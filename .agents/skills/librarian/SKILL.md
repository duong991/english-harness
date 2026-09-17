# Librarian Skill

**Description for Main Agent**: Use this skill when the user asks for new learning material (articles, videos, podcasts) or when a learning plan requires selecting specific content. This skill offloads the web search and evaluation to a subagent, keeping the main context clean.

The Librarian is an internal subagent skill dedicated to discovering, evaluating, and cataloging English learning materials. It does not interact directly with the learner.

When the learner needs new material (for reading or listening tasks in `docs/LEARNING_PATH.md`), delegate the search to the Librarian subagent. 

## Inputs to Librarian

Provide a self-contained prompt to the Librarian subagent detailing:
1. Target skill (e.g., listening, reading).
2. Learner's CEFR level (e.g., B1, C2) from `learner/PROFILE.md`.
3. Specific topics of interest from `learner/PROFILE.md` or recent conversation.
4. Time budget (e.g., 5-minute video, 500-word article).
5. Accent preference if applicable.

## Expected Output from Librarian

The Librarian must return exactly one recommended material or a very short, curated list (max 3), including for each:
- Title and Author/Creator.
- Exact URL (use web search/fetch to verify).
- Estimated duration/length.
- CEFR level estimate.
- One-sentence justification of why it fits the learner's specific profile and goal.

## Execution

To use this skill, the main agent calls the `subagent` tool (or `subagent_fork` if context is needed) with `description: "Librarian material search"` and the detailed prompt above. Wait for the result (`run_in_background: false` if needed immediately) before presenting the final task to the learner.