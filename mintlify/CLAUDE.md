# Agent prompt

A living reference for structured prompt formats, tracking what frontier AI agents want.

## Project Identity

- **Brand name**: Agent prompt (two words, lowercase "prompt")
- **Domain**: prompts.ag
- **GitHub org**: agentprompt
- **Repository**: [agentprompt/prompts.ag](https://github.com/agentprompt/prompts.ag)
- **Platform**: Mintlify
- **File extension**: `.ag.md` (transitional), `.ag` (future)

## IMPORTANT RULES

1. **Never use Claude as commit author.** All commits must use the repository owner's git identity (`Simon Heimlicher <simon.github@heimlicher.com>`), not Claude or any AI assistant.

## Core Positioning

Modern prompts combine XML-like tags with Markdown content. The challenge isn't the format—it's the uncertainty. Best practices evolve as Anthropic, OpenAI, and Google update their guidance.

Agent prompt is a living reference that synthesizes evolving guidance from frontier labs so humans can write prompts with confidence.

**Governing principle**: Agents lead, humans follow. The format evolves with how agents produce and consume prompts.

## The Format

`.ag` files contain prompts written for AI agents:

- Pseudo-XML tags for semantic structure (not strict XML)
- Markdown content inside and between tags
- No attributes on tags
- Flexible whitespace—inline or block tags, as author intends

## Design Principles

1. **Documentation first, tooling follows.** Clarity about what agents want enables syntax highlighting, validation, formatters.
2. **Preserve, don't transform.** Tooling validates and lints—it does not reformat. What the author writes is what the agent receives.
3. **Descriptive, not prescriptive.** The spec documents observed patterns from frontier labs rather than inventing arbitrary conventions.
4. **Living document.** Updated as labs publish new guidance.

## Source Material

Primary references:

- Anthropic: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags
- OpenAI: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide/
- Google: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts

## Development

```bash
npm i -g mint
mint dev
```

Preview at http://localhost:3000

## Content Structure

```
docs/
├── docs.json        # Mintlify configuration
├── index.mdx        # Homepage
├── guidelines.mdx   # Markdown in XML tags
├── format.mdx       # The .ag format spec
├── approach.mdx     # Why we don't benchmark
└── tooling.mdx      # Tooling roadmap
```

## Tooling Roadmap (Future)

1. **Syntax highlighting** — TextMate grammar for VS Code, Sublime, GitHub Linguist
2. **Validation** — dprint plugin (validate structure, don't reformat content)
3. **Language server** — LSP support for autocomplete, hover info, and diagnostics

## Related Work

- AGENTS.md (https://agents.md) — Repo-level instructions for coding agents
- This project complements AGENTS.md: they define what agents should do, we define how to write prompts for agents

## Context

This project emerged from work on SPX (Spec-Driven Development framework). The `.ag` format addresses a gap in IDE tooling for the XML+Markdown hybrid that LLMs prefer.
