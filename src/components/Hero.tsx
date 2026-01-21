import CodeExample from "./CodeExample";

const examplePrompt = `You are a financial analyst. Generate a Q2 report.

<context>
AcmeCorp is a B2B SaaS company.
Our investors value transparency.
</context>

<instructions>
1. Revenue Growth, Profit Margins, Cash Flow
2. Highlight strengths and improvements
</instructions>

<data>{{SPREADSHEET_DATA}}</data>`;

export default function Hero() {
  return (
    <header className="px-6 py-12 md:py-20">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div>
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight mb-4">What agents want</h1>
          <p className="text-lg md:text-xl text-[var(--text-secondary)] mb-6 leading-relaxed">
            A living reference for structured prompt formats, synthesizing guidance from frontier labs.
          </p>
          <div className="flex flex-wrap gap-4">
            <a
              href="#markdown-in-xml"
              className="inline-flex items-center px-5 py-2.5 bg-[var(--foreground)] text-[var(--background)] rounded-lg font-medium hover:opacity-90 transition-opacity"
            >
              Learn the format
            </a>
            <a
              href="https://github.com/agentprompt/prompts.ag"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center px-5 py-2.5 border border-current rounded-lg font-medium hover:opacity-70 transition-opacity"
              aria-label="View on GitHub (opens in new tab)"
            >
              View on GitHub
            </a>
          </div>
        </div>

        <CodeExample code={examplePrompt} filename="example.ag" />
      </div>
    </header>
  );
}
