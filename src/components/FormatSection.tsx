import Section from "./Section";
import CodeExample from "./CodeExample";

const examplePrompt = `You're a financial analyst at AcmeCorp. Generate a Q2 report.

<context>
AcmeCorp is a B2B SaaS company. Our investors value transparency.
</context>

<instructions>
1. Include sections: Revenue Growth, Profit Margins, Cash Flow
2. Highlight strengths and areas for improvement
</instructions>

Use this data:
<data>{{SPREADSHEET_DATA}}</data>`;

export default function FormatSection() {
  return (
    <Section id="format" title="The format">
      <p>
        <code>.ag</code> files (or <code>.ag.md</code> during the transition)
        contain prompts written for AI agents. The format is simple:
      </p>

      <ul className="list-disc list-inside space-y-2 my-4">
        <li>Pseudo-XML tags for semantic structure (not strict XML)</li>
        <li>Markdown content inside and between tags</li>
        <li>No attributes on tags</li>
        <li>Flexible whitespace—inline or block tags, as author intends</li>
      </ul>

      <div className="my-8">
        <CodeExample code={examplePrompt} filename="quarterly-report.ag" />
      </div>

      <p>
        The format preserves author intent. Tooling validates and lints but
        does not reformat. What you write is what the agent receives.
      </p>
    </Section>
  );
}
