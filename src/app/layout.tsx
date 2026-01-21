import type { Metadata } from "next";
import "./globals.css";

const description = "A living reference for structured prompt formats, tracking what frontier AI agents want.";

export const metadata: Metadata = {
  metadataBase: new URL("https://prompts.ag"),
  title: "Agent prompt — A living reference for structured prompt formats",
  description,
  keywords: [
    "agent prompts",
    "AI prompts",
    "XML tags",
    "prompt engineering",
    "Claude",
    "GPT",
    "Gemini",
  ],
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    title: "Agent prompt",
    description,
    url: "https://prompts.ag",
    siteName: "Agent prompt",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Agent prompt",
    description,
  },
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
