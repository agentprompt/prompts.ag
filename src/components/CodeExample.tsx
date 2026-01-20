type CodeExampleProps = {
  code: string;
  filename?: string;
};

export default function CodeExample({ code, filename }: CodeExampleProps) {
  return (
    <div className="rounded-lg border border-current/20 overflow-hidden">
      {filename && (
        <div className="px-4 py-2 border-b border-current/20 text-sm opacity-70 font-mono">
          {filename}
        </div>
      )}
      <pre className="p-4 overflow-x-auto text-sm leading-relaxed">
        <code>{code}</code>
      </pre>
    </div>
  );
}
