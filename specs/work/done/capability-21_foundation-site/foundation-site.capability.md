# Capability: Foundation Site

> **Status**: DONE — Initial site is live at prompts.ag

## Success Metric

**Quantitative Target:**

- **Baseline**: No reference site exists
- **Target**: Live, functional reference site presenting synthesized prompt format guidance
- **Measurement**: Site deployed, accessible, and presenting core content

## Testing Strategy

### Level Assignment

| Component            | Level | Justification                                                |
| -------------------- | ----- | ------------------------------------------------------------ |
| Component rendering  | 1     | Verifies individual sections render correctly                |
| Page assembly        | 2     | Verifies sections integrate into cohesive page               |
| Full site experience | 3     | Verifies complete user journey from landing to understanding |

### Escalation Rationale

- **1 → 2**: Individual components working doesn't prove they compose correctly
- **2 → 3**: Page assembly doesn't prove the content achieves user understanding

## Capability E2E Tests (Level 3)

### E2E1: User finds prompt format guidance

```typescript
describe("Capability: Foundation Site", () => {
  it("GIVEN a prompt author visits the site WHEN they scan the page THEN they understand the XML+Markdown format", async () => {
    // Given: User lands on prompts.ag
    await page.goto("https://prompts.ag");

    // When: User scrolls through content
    await expect(page.locator("text=What agents want")).toBeVisible();
    await expect(page.locator("text=Markdown in XML tags")).toBeVisible();

    // Then: User sees format specification and examples
    await expect(page.locator("text=The format")).toBeVisible();
    await expect(page.locator("pre")).toBeVisible(); // Code examples
  });
});
```

## Delivered Features

This capability delivered the following features:

### Feature: Hero Section

- Eye-catching header with main value proposition
- "What agents want" headline with supporting tagline
- Call-to-action buttons (Learn the format, View on GitHub)
- Live code example demonstrating `.ag` format
- Copy-to-clipboard functionality

### Feature: Guidelines Section ("Markdown in XML tags")

- Six synthesized guidelines from frontier lab documentation
- Source links to Anthropic, OpenAI, and Google documentation
- Accessible design with proper ARIA labels

### Feature: Format Section

- `.ag` format specification
- Format characteristics (pseudo-XML, Markdown content, no attributes, flexible whitespace)
- "Preserve, don't transform" philosophy explanation
- Code example with filename display

### Feature: Approach Section

- "Why we don't benchmark" explanation
- Methodology: follow lab recommendations, not empirical testing
- Update policy: changes when labs update guidance

### Feature: Tooling Section

- Roadmap for future developer tools
- Planned: Syntax highlighting (TextMate grammar)
- Planned: Validation (dprint plugin)
- Planned: Language server (LSP)

### Feature: Footer

- MIT License link
- Related project link (AGENTS.md)

### Feature: Design System

- Light/dark mode support (system preference)
- Responsive layout (mobile, tablet, desktop)
- Clean typography with monospace code blocks
- Tailwind CSS 4.0 styling

### Feature: SEO & Metadata

- Page title and meta description
- Open Graph tags for social sharing
- Robots meta for search indexing

## System Integration

This capability establishes the foundation that all future capabilities build upon:

- **Content structure**: Section-based layout that can expand
- **Component library**: Reusable Section, CodeExample, and icon components
- **Styling system**: CSS custom properties and Tailwind classes
- **Navigation pattern**: Anchor-based scrolling (ready for header navigation)

## Completion Criteria

- [x] All sections render correctly
- [x] Site is accessible (ARIA labels, focus states)
- [x] Site is responsive (works on mobile)
- [x] Code examples have copy functionality
- [x] Source links point to valid lab documentation
- [x] Site deployed and accessible at prompts.ag
