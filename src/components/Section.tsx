import React from "react";

export type SectionProps = React.PropsWithChildren<{
  id?: string;
  className?: string;
  title: string;
  center?: boolean;
  maxWidthClass?: string;
}>;

export default function Section({
  className = "",
  id,
  title,
  children,
  center = false,
  maxWidthClass = "max-w-4xl",
}: SectionProps) {
  const headingId = id ? `${id}-heading` : undefined;

  return (
    <section
      id={id}
      className={`${className} px-6 py-10`}
      aria-labelledby={headingId}
    >
      <div className={`${maxWidthClass} mx-auto flex flex-col gap-4`}>
        <h2
          id={headingId}
          className={`text-2xl font-semibold tracking-tight ${center ? "mx-auto text-center" : ""}`}
        >
          {title}
        </h2>
        <div className="space-y-4 leading-relaxed">{children}</div>
      </div>
    </section>
  );
}
