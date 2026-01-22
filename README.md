# Agent prompt

A living reference for structured prompt formats, tracking what frontier AI agents want.

**[prompts.ag](https://prompts.ag)**

## What is this?

Modern prompts combine XML-like tags with Markdown content. The challenge isn't the format—it's the uncertainty. Best practices evolve as Anthropic, OpenAI, and Google DeepMind update their guidance.

**Agent prompt** synthesizes evolving guidance from frontier labs so humans can write prompts with confidence.

## Why not validate the format empirically?

We don't benchmark whether XML-tagged prompts outperform pure Markdown. Here's why:

Our goal is **enduring guidance**—advice that remains valid as models improve. The only durable foundation is what frontier labs recommend, which also reflects what they use in training. Empirical validation with today's SOTA models would mean making decisions about the future based on the past.

When Anthropic, OpenAI, or Google update their guidance, we update ours.

## The format

`.ag` files contain prompts written for AI agents:

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

## Principles

1. **Agents lead, humans follow** — The format evolves with how agents produce and consume prompts
2. **Documentation first** — Clarity about what agents want enables tooling
3. **Preserve, don't transform** — What the author writes is what the agent receives
4. **Living document** — Updated as labs publish new guidance

## Development

```bash
pnpm install
pnpm dev
```

## License

MIT
