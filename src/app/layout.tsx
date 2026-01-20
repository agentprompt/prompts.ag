import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Agent prompt — A living reference for structured prompt formats",
  description:
    "Synthesizing evolving guidance from frontier labs so humans can write prompts with confidence.",
  openGraph: {
    title: "Agent prompt",
    description:
      "A living reference for structured prompt formats, tracking what frontier AI agents want.",
    url: "https://prompts.ag",
    siteName: "Agent prompt",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Agent prompt",
    description:
      "A living reference for structured prompt formats, tracking what frontier AI agents want.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
