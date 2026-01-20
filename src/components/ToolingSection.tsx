import Section from "./Section";

export default function ToolingSection() {
  return (
    <Section id="tooling" title="Tooling">
      <p>
        Documentation first, tooling follows. Once the format is stable,
        we&apos;ll build:
      </p>

      <div className="space-y-4 mt-6">
        <div className="flex gap-4 items-start">
          <span className="text-sm opacity-50 font-mono w-6">1.</span>
          <div>
            <h3 className="font-semibold">Syntax highlighting</h3>
            <p className="opacity-80">
              TextMate grammar for VS Code, Sublime, and GitHub Linguist.
            </p>
          </div>
        </div>

        <div className="flex gap-4 items-start">
          <span className="text-sm opacity-50 font-mono w-6">2.</span>
          <div>
            <h3 className="font-semibold">Validation</h3>
            <p className="opacity-80">
              A dprint plugin that validates structure without reformatting
              content.
            </p>
          </div>
        </div>

        <div className="flex gap-4 items-start">
          <span className="text-sm opacity-50 font-mono w-6">3.</span>
          <div>
            <h3 className="font-semibold">Language server</h3>
            <p className="opacity-80">
              LSP support for autocomplete, hover info, and diagnostics.
            </p>
          </div>
        </div>
      </div>
    </Section>
  );
}
