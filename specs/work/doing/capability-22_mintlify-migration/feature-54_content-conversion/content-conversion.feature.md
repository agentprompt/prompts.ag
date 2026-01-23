# Feature: Content Conversion (TSX → MDX)

## Observable Outcome

All existing prompts.ag content is converted from React TSX components to Mintlify MDX files, preserving all text, code examples, and links.

## Testing Strategy

> Features require **Level 1 + Level 2** to prove the feature works with real tools.

### Level Assignment

| Component            | Level | Justification                            |
| -------------------- | ----- | ---------------------------------------- |
| Content preservation | 1     | Text comparison between TSX and MDX      |
| MDX syntax validity  | 1     | MDX parser validation                    |
| Rendered output      | 2     | Needs `mint dev` to verify visual output |

### Escalation Rationale

- **1 → 2**: Valid MDX syntax doesn't prove content renders correctly in Mintlify

## Feature Integration Tests (Level 2)

### FI1: All content sections visible

```typescript
describe("Feature: Content Conversion", () => {
  it("GIVEN MDX files are converted WHEN viewing each page THEN all content is visible", async () => {
    // Given: mint dev is running
    await page.goto("http://localhost:3333/guidelines");

    // Then: Key content from WhatAgentsWantSection.tsx is visible
    await expect(page.locator("text=Markdown in XML tags")).toBeVisible();
    await expect(page.locator("text=Use descriptive tag names")).toBeVisible();
  });
});
```

### FI2: Code blocks render with syntax highlighting

```typescript
describe("Feature: Content Conversion", () => {
  it("GIVEN format.mdx has code blocks WHEN viewing the page THEN syntax highlighting is applied", async () => {
    await page.goto("http://localhost:3333/format");

    // Then: Code blocks have highlighting classes
    const codeBlock = page.locator("pre code");
    await expect(codeBlock).toHaveAttribute("class", /language-/);
  });
});
```

## Content Mapping

| Source TSX Component        | Target MDX File  | Key Content                    |
| --------------------------- | ---------------- | ------------------------------ |
| `Hero.tsx`                  | `index.mdx`      | Hero headline, value prop      |
| `WhatAgentsWantSection.tsx` | `guidelines.mdx` | 6 guidelines, source links     |
| `FormatSection.tsx`         | `format.mdx`     | .ag format spec, code examples |
| `ApproachSection.tsx`       | `approach.mdx`   | Why no benchmarks              |
| `ToolingSection.tsx`        | `tooling.mdx`    | Roadmap with steps             |
| (new)                       | `changelog.mdx`  | Initial entry for migration    |

## MDX Components to Use

- `<Card>` and `<CardGroup>` for source links (Anthropic, OpenAI, Google)
- `<Steps>` for tooling roadmap
- `<Tip>`, `<Note>` for callouts
- Code blocks with `title` attribute for filenames

## Capability Contribution

This is the core value of the migration - converting content while gaining Mintlify's features. Each story converts one TSX file, enabling incremental progress and testing.

## Completion Criteria

- [ ] All 5 TSX components converted to MDX
- [ ] changelog.mdx created with initial entry
- [ ] All content text preserved (no missing paragraphs)
- [ ] All code examples preserved
- [ ] All links preserved and functional
- [ ] Visual output matches original site intent
