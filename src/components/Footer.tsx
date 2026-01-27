export default function Footer() {
  return (
    <footer className="mt-auto px-6 py-12 border-t border-[var(--border)]">
      <div className="max-w-4xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-[var(--text-muted)]">
        <p>
          prompts.ag is open source under the{" "}
          <a
            href="https://github.com/agentprompt/prompts.ag/blob/main/LICENSE"
            target="_blank"
            rel="noopener noreferrer"
            className="link-muted"
            aria-label="MIT License (opens in new tab)"
          >
            MIT License
          </a>
          .
        </p>
        <p>
          See also:{" "}
          <a
            href="https://agents.md"
            target="_blank"
            rel="noopener noreferrer"
            className="link-muted"
            aria-label="AGENTS.md website (opens in new tab)"
          >
            AGENTS.md
          </a>
        </p>
      </div>
    </footer>
  );
}
