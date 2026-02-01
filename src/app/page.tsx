import DocCard from "@/components/DocCard";
import Footer from "@/components/Footer";
import Wordmark from "@/components/Wordmark";

const docLinks = [
  {
    title: "Guidelines",
    description: "Core principles for structuring prompts. Markdown content, XML tags, clear hierarchy.",
    href: "https://docs.prompts.ag/guidelines",
  },
  {
    title: "Format",
    description: "The .ag file specification. How to write prompts that models parse reliably.",
    href: "https://docs.prompts.ag/format",
  },
  {
    title: "Approach",
    description: "Why we synthesize lab guidance instead of benchmarking. The philosophy behind prompts.ag.",
    href: "https://docs.prompts.ag/approach",
  },
  {
    title: "Tooling",
    description: "Editor support, syntax highlighting, and integrations for working with .ag files.",
    href: "https://docs.prompts.ag/tooling",
  },
];

export default function Home() {
  return (
    <>
      {/* Background layers */}
      <div className="grid-background" aria-hidden="true" />
      <div className="noise-overlay" aria-hidden="true" />

      <main className="min-h-screen flex flex-col">
        {/* Hero Section */}
        <header className="flex-1 flex flex-col items-center justify-center px-6 py-16 md:py-24">
          <div className="text-center max-w-2xl mx-auto">
            {/* Wordmark with glow */}
            <div className="animate-in opacity-0 mb-8">
              <Wordmark className="mx-auto" />
            </div>

            {/* Tagline */}
            <p className="animate-in opacity-0 animation-delay-100 text-lg md:text-xl text-[var(--text-secondary)] mb-10 leading-relaxed font-display">
              Structured prompts that models prefer.
              <br />
              <span className="text-[var(--text-muted)]">
                Markdown content in XML tags—the format frontier labs recommend.
              </span>
            </p>

            {/* CTAs */}
            <div className="animate-in opacity-0 animation-delay-200 flex flex-wrap justify-center gap-4">
              <a href="https://docs.prompts.ag" className="btn-primary">
                Read the docs
                <svg
                  className="w-4 h-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M17 8l4 4m0 0l-4 4m4-4H3"
                  />
                </svg>
              </a>
              <a
                href="https://github.com/agentprompt/prompts.ag"
                target="_blank"
                rel="noopener noreferrer"
                className="btn-secondary"
                aria-label="View on GitHub (opens in new tab)"
              >
                GitHub
              </a>
            </div>
          </div>
        </header>

        {/* Doc Cards Section */}
        <section className="px-6 pb-16">
          <div className="max-w-5xl mx-auto">
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {docLinks.map((doc, index) => (
                <DocCard
                  key={doc.title}
                  title={doc.title}
                  description={doc.description}
                  href={doc.href}
                  className={`animate-in opacity-0 animation-delay-${(index + 3) * 100}`}
                />
              ))}
            </div>
          </div>
        </section>

        <Footer />
      </main>
    </>
  );
}
