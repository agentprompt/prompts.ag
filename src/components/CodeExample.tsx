"use client";

import { useState } from "react";
import CopyIcon from "./icons/CopyIcon";

export type CodeExampleProps = {
  code: string;
  filename?: string;
  language?: string;
};

export default function CodeExample({ code, filename, language = "ag" }: CodeExampleProps) {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error("Failed to copy to clipboard:", err);
    }
  };

  return (
    <div className="rounded-lg border border-[var(--border)] bg-[var(--surface)] overflow-hidden">
      <div className="flex items-center justify-between px-4 py-2 border-b border-[var(--border)]">
        <span className="text-sm text-[var(--text-muted)] font-mono">{filename || "\u00A0"}</span>
        <button
          onClick={copyToClipboard}
          className="p-1.5 rounded-md bg-transparent hover:bg-current/10 transition-colors cursor-pointer"
          aria-label="Copy to clipboard"
        >
          {copied
            ? (
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            )
            : <CopyIcon className="w-4 h-4" />}
        </button>
      </div>
      <pre className="p-4 overflow-x-auto text-sm leading-relaxed" tabIndex={0}>
        <code className={`language-${language}`}>{code}</code>
      </pre>
    </div>
  );
}
