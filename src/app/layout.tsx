import type { Metadata, Viewport } from "next";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "What agents want — Structured prompt formats for AI",
  description:
    "A living reference for structured prompt formats. Learn how Anthropic, OpenAI, and Google recommend structuring prompts with XML-like tags and Markdown content.",
  keywords: ["agent prompts", "AI prompts", "prompt engineering"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" dir="ltr">
      <body className="antialiased">{children}</body>
    </html>
  );
}
