export default function Hero() {
  return (
    <header className="px-6 py-20 md:py-32">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-bold tracking-tight mb-6">Agent prompt</h1>
        <p className="text-xl md:text-2xl opacity-80 mb-8 max-w-2xl leading-relaxed">
          A living reference for structured prompt formats, tracking what frontier AI agents want.
        </p>
        <div className="flex flex-wrap gap-4">
          <a
            href="#format"
            className="inline-flex items-center px-6 py-3 bg-[var(--foreground)] text-[var(--background)] rounded-lg font-medium hover:opacity-90 transition-opacity"
          >
            See the format
          </a>
          <a
            href="https://github.com/agentprompt/prompts.ag"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-6 py-3 border border-current rounded-lg font-medium hover:opacity-70 transition-opacity"
            aria-label="View on GitHub (opens in new tab)"
          >
            View on GitHub
          </a>
        </div>
      </div>
    </header>
  );
}
