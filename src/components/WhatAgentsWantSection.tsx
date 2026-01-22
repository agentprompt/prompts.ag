import React from "react";
import Section from "./Section";

type ContentBlock =
  | { type: "text"; value: string }
  | { type: "code"; value: string };

type GuidelineItem = {
  title: string;
  content: ContentBlock[];
};

type Source = {
  name: string;
  href: string;
  ariaLabel: string;
};

const sources: Source[] = [
  {
    name: "Anthropic",
    href: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags",
    ariaLabel: "Anthropic documentation (opens in new tab)",
  },
  {
    name: "OpenAI",
    href: "https://cookbook.openai.com/examples/gpt4-1_prompting_guide",
    ariaLabel: "OpenAI GPT-4.1 Prompting Guide (opens in new tab)",
  },
  {
    name: "Google",
    href: "https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts",
    ariaLabel: "Google Vertex AI documentation (opens in new tab)",
  },
];

const guidelines: GuidelineItem[] = [
  {
    title: "Use XML-like tags for structure",
    content: [
      {
        type: "text",
        value:
          "Wrap distinct sections of your prompt in descriptive tags. Tags create clear boundaries that help models parse complex prompts reliably.",
      },
    ],
  },
  {
    title: "Choose descriptive tag names",
    content: [
      {
        type: "text",
        value: "There are no canonical \"best\" tag names. Use names that describe the content: ",
      },
      { type: "code", value: "<context>" },
      { type: "text", value: ", " },
      { type: "code", value: "<instructions>" },
      { type: "text", value: ", " },
      { type: "code", value: "<example>" },
      { type: "text", value: ", " },
      { type: "code", value: "<data>" },
      { type: "text", value: ". Be consistent within a prompt." },
    ],
  },
  {
    title: "Keep Markdown inside tags",
    content: [
      {
        type: "text",
        value:
          "Content within tags can use full Markdown formatting—lists, headers, code blocks. The tags provide semantic structure; Markdown handles formatting.",
      },
    ],
  },
  {
    title: "Nest tags when needed",
    content: [
      { type: "text", value: "For hierarchical content, nest tags naturally. A " },
      { type: "code", value: "<examples>" },
      { type: "text", value: " section might contain multiple " },
      { type: "code", value: "<example>" },
      { type: "text", value: " tags. Maintain consistent indentation for readability." },
    ],
  },
  {
    title: "Attributes: labs differ",
    content: [
      {
        type: "text",
        value: "Anthropic recommends no attributes—use nested tags for metadata. OpenAI supports attributes like ",
      },
      { type: "code", value: "<doc id=\"1\" title=\"...\">" },
      { type: "text", value: ". For portability across models, avoid attributes or test both approaches." },
    ],
  },
  {
    title: "Long context: repeat instructions",
    content: [
      {
        type: "text",
        value:
          "For prompts with extensive context, place instructions at both the beginning and end. This helps models maintain focus on your requirements throughout processing.",
      },
    ],
  },
];

function renderContent(content: ContentBlock[]): React.ReactNode {
  return content.map((block, index) => {
    if (block.type === "code") {
      return <code key={index}>{block.value}</code>;
    }
    return <React.Fragment key={index}>{block.value}</React.Fragment>;
  });
}

export default function WhatAgentsWantSection() {
  return (
    <Section id="markdown-in-xml" title="Markdown in XML tags">
      <p>
        Frontier models converge on the same format: Markdown content wrapped in XML-like tags. Here&apos;s what they
        want:
      </p>

      <div className="space-y-5 mt-4">
        {guidelines.map((item) => (
          <div key={item.title}>
            <h3 className="font-semibold text-lg mb-2">{item.title}</h3>
            <p>{renderContent(item.content)}</p>
          </div>
        ))}
      </div>

      <p className="mt-8 text-sm text-[var(--text-muted)]">
        Sources: {sources.map((source, index) => (
          <React.Fragment key={source.name}>
            <a
              href={source.href}
              target="_blank"
              rel="noopener noreferrer"
              className="underline"
              aria-label={source.ariaLabel}
            >
              {source.name}
            </a>
            {index < sources.length - 1 && " · "}
          </React.Fragment>
        ))}
      </p>
    </Section>
  );
}
