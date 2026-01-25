import type { Metadata, Viewport } from "next";
import { Fira_Code } from "next/font/google";
import "./globals.css";

const firaCode = Fira_Code({
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  variable: "--font-mono",
  display: "swap",
});

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export function generateMetadata(): Metadata {
  const siteUrl = "https://prompts.ag";

  return {
    metadataBase: new URL(siteUrl),
    title: "What agents want — Structured prompt formats for AI",
    description:
      "A living reference for structured prompt formats. Learn how Anthropic, OpenAI, and Google recommend structuring prompts with XML-like tags and Markdown content.",
    keywords: ["agent prompts", "AI prompts", "prompt engineering"],
    openGraph: {
      title: "What agents want — Structured prompt formats for AI",
      description:
        "A living reference for structured prompt formats. Learn how Anthropic, OpenAI, and Google recommend structuring prompts with XML-like tags and Markdown content.",
      url: "./",
      siteName: "prompts.ag",
      locale: "en_US",
      type: "website",
    },
    twitter: {
      title: "What agents want — Structured prompt formats for AI",
      card: "summary_large_image",
    },
    robots: {
      index: true,
      follow: true,
    },
  };
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" dir="ltr" className={firaCode.variable}>
      <body className="antialiased">{children}</body>
    </html>
  );
}
