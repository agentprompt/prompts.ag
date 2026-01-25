type DocCardProps = {
  title: string;
  description: string;
  href: string;
  className?: string;
};

export default function DocCard({ title, description, href, className = "" }: DocCardProps) {
  return (
    <a
      href={href}
      className={`group block p-6 card-glass ${className}`}
    >
      <h3 className="font-display text-lg font-semibold mb-2 flex items-center gap-2">
        {title}
        <svg
          className="w-4 h-4 opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200"
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
      </h3>
      <p className="text-[var(--text-muted)] text-sm leading-relaxed">{description}</p>
    </a>
  );
}
