import React from "react";
import Section from "./Section";

type ContentBlock =
  | { type: "text"; value: string }
  | { type: "code"; value: string };

type GuidelineItem = {
  title: string;
  content: ContentBlock[];
};

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
    title: "No attributes on tags",
    content: [
      { type: "text", value: "Unlike HTML or XML, prompt tags don't use attributes. Write " },
      { type: "code", value: "<example>" },
      { type: "text", value: ", not " },
      { type: "code", value: "<example type=\"good\">" },
      { type: "text", value: ". If you need metadata, include it as content or use nested tags." },
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
    <Section id="what-agents-want" title="What agents want">
      <p>
        Despite surface differences in documentation, frontier models converge on the same core preferences. Here&apos;s
        the synthesis:
      </p>

      <div className="space-y-6 mt-6">
        {guidelines.map((item) => (
          <div key={item.title}>
            <h3 className="font-semibold text-lg mb-2">{item.title}</h3>
            <p>{renderContent(item.content)}</p>
          </div>
        ))}
      </div>

      <p className="mt-8 text-sm opacity-70">
        Sources:{" "}
        <a
          href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags"
          target="_blank"
          rel="noopener noreferrer"
          className="underline"
          aria-label="Anthropic documentation (opens in new tab)"
        >
          Anthropic
        </a>
        {" · "}
        <span className="opacity-50">OpenAI (coming soon)</span>
        {" · "}
        <span className="opacity-50">Google DeepMind (coming soon)</span>
      </p>
    </Section>
  );
}
