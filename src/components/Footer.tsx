export default function Footer() {
  return (
    <footer className="px-6 py-12 border-t border-current/10">
      <div className="max-w-4xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4 text-sm opacity-70">
        <p>
          Agent prompt is open source under the{" "}
          <a
            href="https://github.com/agentprompt/prompts.ag/blob/main/LICENSE"
            target="_blank"
            rel="noopener noreferrer"
            className="underline"
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
            className="underline"
          >
            AGENTS.md
          </a>
        </p>
      </div>
    </footer>
  );
}
