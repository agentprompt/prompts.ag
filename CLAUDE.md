# Agent prompt

A living reference for structured prompt formats, tracking what frontier AI agents want.

## Project Identity

- **Brand name**: Agent prompt (two words, lowercase "prompt")
- **Domain**: prompts.ag
- **GitHub org**: agentprompt
- **Repository**: https://github.com/agentprompt/prompts.ag
- **File extension**: `.ag.md` (transitional), `.ag` (future)

## IMPORTANT RULES

1. **Never use Claude as commit author.** All commits must use the repository owner's git identity (`Simon Heimlicher <simon.github@heimlicher.com>`), not Claude or any AI assistant. This applies to all commits, including initial commits, amendments, and rebases.

## Core Positioning

Modern prompts combine XML-like tags with Markdown content. The challenge isn't the format—it's the uncertainty. Best practices evolve as Anthropic, OpenAI, and Google DeepMind update their guidance.

Agent prompt is a living reference that synthesizes evolving guidance from frontier labs so humans can write prompts with confidence.

**Governing principle**: Agents lead, humans follow. The format evolves with how agents produce and consume prompts. Human authors adapt to agent preferences, not the reverse.

## The Format

`.ag` files contain prompts written for AI agents:

- Pseudo-XML tags for semantic structure (not strict XML)
- Markdown content inside and between tags
- No attributes on tags
- Flexible whitespace—inline or block tags, as author intends

Example:

```ag
You're a financial analyst at AcmeCorp. Generate a Q2 report.

<context>
AcmeCorp is a B2B SaaS company. Our investors value transparency.
</context>

<instructions>
1. Include sections: Revenue Growth, Profit Margins, Cash Flow
2. Highlight strengths and areas for improvement
</instructions>

Use this data:
<data>{{SPREADSHEET_DATA}}</data>
```

## Design Principles

1. **Documentation first, tooling follows.** Clarity about what agents want enables syntax highlighting, validation, formatters. But the reference comes first.
1. **Preserve, don't transform.** Tooling validates and lints—it does not reformat. What the author writes is what the agent receives.
1. **Descriptive, not prescriptive.** The spec documents observed patterns from frontier labs rather than inventing arbitrary conventions.
1. **Living document.** Updated as labs publish new guidance. Versioned against model generations if needed.

## Source Material

Primary reference for Claude/Anthropic:

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags

Key points from Anthropic's guidance:

- No canonical "best" tag names—tag names should make sense for their content
- Be consistent with tag names throughout prompts
- Nest tags for hierarchical content
- Common tags: `<instructions>`, `<example>`, `<context>`, `<data>`, `<formatting>`

## Site Structure

Next.js site (following agentsmd/agents.md pattern):

```
Home
├── The problem (uncertainty, evolving guidance)
├── What agents want (current synthesis)
│   ├── Anthropic / Claude
│   ├── OpenAI / GPT
│   └── Google / Gemini
├── The format (.ag.md)
├── Tooling (roadmap)
└── Contributing
```

## Tech Stack

- Next.js
- TypeScript
- pnpm
- TailwindCSS
- MIT License

## Tooling Roadmap (Future)

1. **Syntax highlighting** — TextMate grammar for VS Code, Sublime, GitHub Linguist
1. **Validation** — dprint plugin (validate structure, don't reformat content)
1. **Language server** — Eventually

## Related Work

- AGENTS.md (https://agents.md) — Repo-level instructions for coding agents
- This project complements AGENTS.md: they define what agents should do, we define how to write prompts for agents

## Context

This project emerged from work on SPX (Spec-Driven Development framework). The `.ag` format addresses a gap in IDE tooling for the XML+Markdown hybrid that LLMs prefer.
