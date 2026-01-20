import Section from "./Section";

type ToolingItem = {
  title: string;
  description: string;
};

const toolingItems: ToolingItem[] = [
  {
    title: "Syntax highlighting",
    description: "TextMate grammar for VS Code, Sublime, and GitHub Linguist.",
  },
  {
    title: "Validation",
    description: "A dprint plugin that validates structure without reformatting content.",
  },
  {
    title: "Language server",
    description: "LSP support for autocomplete, hover info, and diagnostics.",
  },
];

export default function ToolingSection() {
  return (
    <Section id="tooling" title="Tooling">
      <p>Documentation first, tooling follows. Once the format is stable, we&apos;ll build:</p>

      <div className="space-y-4 mt-6">
        {toolingItems.map((item, index) => (
          <div key={item.title} className="flex gap-4 items-start">
            <span className="text-sm opacity-50 font-mono w-6">{index + 1}.</span>
            <div>
              <h3 className="font-semibold">{item.title}</h3>
              <p className="opacity-80">{item.description}</p>
            </div>
          </div>
        ))}
      </div>
    </Section>
  );
}
