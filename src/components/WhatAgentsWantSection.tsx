import Section from "./Section";

export default function WhatAgentsWantSection() {
  return (
    <Section id="what-agents-want" title="What agents want">
      <p>
        Despite surface differences in documentation, frontier models converge
        on the same core preferences. Here&apos;s the synthesis:
      </p>

      <div className="space-y-6 mt-6">
        <div>
          <h3 className="font-semibold text-lg mb-2">
            Use XML-like tags for structure
          </h3>
          <p>
            Wrap distinct sections of your prompt in descriptive tags. Tags
            create clear boundaries that help models parse complex prompts
            reliably.
          </p>
        </div>

        <div>
          <h3 className="font-semibold text-lg mb-2">
            Choose descriptive tag names
          </h3>
          <p>
            There are no canonical &quot;best&quot; tag names. Use names that
            describe the content: <code>&lt;context&gt;</code>,{" "}
            <code>&lt;instructions&gt;</code>, <code>&lt;example&gt;</code>,{" "}
            <code>&lt;data&gt;</code>. Be consistent within a prompt.
          </p>
        </div>

        <div>
          <h3 className="font-semibold text-lg mb-2">
            Keep Markdown inside tags
          </h3>
          <p>
            Content within tags can use full Markdown formatting—lists,
            headers, code blocks. The tags provide semantic structure; Markdown
            handles formatting.
          </p>
        </div>

        <div>
          <h3 className="font-semibold text-lg mb-2">Nest tags when needed</h3>
          <p>
            For hierarchical content, nest tags naturally. A{" "}
            <code>&lt;examples&gt;</code> section might contain multiple{" "}
            <code>&lt;example&gt;</code> tags. Maintain consistent indentation
            for readability.
          </p>
        </div>

        <div>
          <h3 className="font-semibold text-lg mb-2">No attributes on tags</h3>
          <p>
            Unlike HTML or XML, prompt tags don&apos;t use attributes. Write{" "}
            <code>&lt;example&gt;</code>, not{" "}
            <code>&lt;example type=&quot;good&quot;&gt;</code>. If you need
            metadata, include it as content or use nested tags.
          </p>
        </div>
      </div>

      <p className="mt-8 text-sm opacity-70">
        Sources:{" "}
        <a
          href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags"
          target="_blank"
          rel="noopener noreferrer"
          className="underline"
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
