# Capability: Enhanced Reference

> **Status**: BACKLOG — Content expansion to establish prompts.ag as the authoritative reference
>
> **Prerequisite**: capability-22 (Mintlify Migration) must be complete

## Success Metric

**Quantitative Target:**

- **Baseline**: Mintlify site with migrated foundation content
- **Target**: Comprehensive reference with rich examples, lab comparisons, and community trust signals
- **Measurement**: Increased engagement (time on site, return visits), community citations, and organic search traffic

## Context: What Mintlify Already Provides

After capability-22 completes, these features are built-in and **not included** in this capability:

| Feature             | Mintlify Built-in                      |
| ------------------- | -------------------------------------- |
| Navigation          | Auto-generated from content structure  |
| Dark mode           | Built-in theme switching               |
| Syntax highlighting | Built-in code blocks                   |
| Changelog           | `Update` components with tag filtering |
| RSS feed            | Auto-generated for changelogs          |
| Copy-to-clipboard   | Contextual "Copy page" menu            |
| Analytics           | Included in Pro tier (OSS program)     |

This capability focuses on **content expansion** that Mintlify doesn't provide out of the box.

## Testing Strategy

### Level Assignment

| Component              | Level | Justification                                   |
| ---------------------- | ----- | ----------------------------------------------- |
| Individual MDX pages   | 1     | Verifies new content renders correctly          |
| Cross-page navigation  | 2     | Verifies content integrates into site structure |
| Complete user journeys | 3     | Verifies users achieve their goals efficiently  |

### Escalation Rationale

- **1 → 2**: Pages rendering doesn't prove they're discoverable
- **2 → 3**: Discoverable content doesn't prove users find value faster

## Capability E2E Tests (Level 3)

### E2E1: User finds lab-specific guidance

```typescript
describe("Capability: Enhanced Reference", () => {
  it("GIVEN a Claude user WHEN they visit /anthropic THEN they see Anthropic-specific guidance", async () => {
    // Given: User wants Anthropic-specific info
    await page.goto("https://prompts.ag/anthropic");

    // Then: Page has Anthropic-specific content
    await expect(page.locator("text=Claude")).toBeVisible();
    await expect(page.locator("text=Anthropic")).toBeVisible();
    // And links to official docs
    await expect(page.locator("a[href*='docs.anthropic.com']")).toBeVisible();
  });
});
```

### E2E2: User copies example prompt pattern

```typescript
describe("Capability: Enhanced Reference", () => {
  it("GIVEN a user wants a prompt template WHEN they visit /examples THEN they can copy working patterns", async () => {
    // Given: User navigates to examples
    await page.goto("https://prompts.ag/examples");

    // Then: Multiple example categories exist
    await expect(page.locator("text=Code Review")).toBeVisible();
    await expect(page.locator("text=Writing")).toBeVisible();

    // And: Code blocks are copyable (Mintlify built-in)
    await expect(page.locator("pre code")).toBeVisible();
  });
});
```

### E2E3: User understands lab differences

```typescript
describe("Capability: Enhanced Reference", () => {
  it("GIVEN a user working with multiple labs WHEN they visit /comparison THEN they see where labs agree and differ", async () => {
    // Given: User navigates to comparison
    await page.goto("https://prompts.ag/comparison");

    // Then: Comparison table exists
    await expect(page.locator("table")).toBeVisible();
    await expect(page.locator("text=Anthropic")).toBeVisible();
    await expect(page.locator("text=OpenAI")).toBeVisible();
    await expect(page.locator("text=Google")).toBeVisible();
  });
});
```

## Planned Features

This capability expands content to make prompts.ag the comprehensive reference for prompt structure.

---

### Feature: Lab-Specific Pages

**Dedicated pages for each frontier lab:**

- `/anthropic` — Claude-specific guidance
- `/openai` — GPT-specific guidance
- `/google` — Gemini-specific guidance

**Each page includes:**

- Lab's official recommendations with source citations
- Lab-specific examples and patterns
- Known quirks or unique behaviors
- Links to official documentation
- Cross-references to comparison page where labs differ

**MDX structure:**

```
labs/
├── anthropic.mdx
├── openai.mdx
└── google.mdx
```

---

### Feature: Examples Gallery

**Real-world prompt patterns organized by use case:**

| Category          | Examples                                             |
| ----------------- | ---------------------------------------------------- |
| Code Review       | PR review, code explanation, refactoring suggestions |
| Writing           | Blog posts, documentation, technical writing         |
| Analysis          | Data analysis, research synthesis, summarization     |
| Structured Output | JSON generation, form filling, extraction            |

**Each example includes:**

- The complete `.ag` prompt pattern
- Explanation of why the structure works
- Variations for different labs (if applicable)
- "Copy as markdown" via Mintlify's built-in menu

**MDX structure:**

```
examples/
├── index.mdx          # Gallery overview with CardGroup
├── code-review.mdx
├── writing.mdx
├── analysis.mdx
└── structured-output.mdx
```

---

### Feature: Lab Comparison Table

**Side-by-side comparison showing where labs agree vs. differ:**

| Topic                 | Anthropic                       | OpenAI    | Google    |
| --------------------- | ------------------------------- | --------- | --------- |
| Tag naming            | Descriptive, no canonical names | Similar   | Similar   |
| Attributes on tags    | Discouraged                     | Allowed   | Allowed   |
| Nesting depth         | Encouraged for hierarchy        | Supported | Supported |
| Long context handling | Repeat instructions             | Similar   | Similar   |

**Implementation:**

- Single `/comparison` page with comprehensive table
- Use Mintlify's table styling
- Link each cell to source documentation
- Add `<Tip>` callouts for key differences

---

### Feature: Source Quotations

**Direct quotes from lab documentation:**

- Adds credibility by showing exact lab language
- Uses Mintlify's `<Note>` or custom callout styling
- Each quote links to source URL
- Collapsible/expandable for space efficiency using `<Accordion>`

**Example:**

```mdx
<Accordion title="What Anthropic says">
> "There are no canonical 'best' tag names... The key is to be consistent."
> — [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/...)
</Accordion>
```

---

### Feature: "Last Updated" Indicators

**Show content currency:**

- Add `lastUpdated` to page frontmatter
- Display "Last verified: {date}" on each page
- Link to changelog for recent updates
- Consider automated checking against lab doc URLs

**Frontmatter example:**

```yaml
---
title: "Anthropic / Claude"
description: "Prompt structure guidance for Claude"
lastUpdated: "2025-01-15"
---
```

---

### Feature: Contributing Guide

**Clear path for community input:**

- `/contributing` page explaining how to suggest improvements
- Link to GitHub issues for feedback
- Guidelines for what contributions are welcome
- Process for verifying against lab documentation

---

### Feature: Social Proof (When Applicable)

**Build trust through visible adoption:**

- GitHub stars badge in header (via docs.json topbar)
- "Used by" or "Cited in" section on homepage
- Community testimonials (curated, only when genuine)

**Note:** Only add when there's genuine traction to display.

---

## Content Checklist

- [ ] Create `/anthropic` page with Claude-specific guidance
- [ ] Create `/openai` page with GPT-specific guidance
- [ ] Create `/google` page with Gemini-specific guidance
- [ ] Create `/examples` index with CardGroup navigation
- [ ] Create `/examples/code-review` with patterns
- [ ] Create `/examples/writing` with patterns
- [ ] Create `/examples/analysis` with patterns
- [ ] Create `/examples/structured-output` with patterns
- [ ] Create `/comparison` with lab comparison table
- [ ] Add source quotations to guideline pages
- [ ] Add `lastUpdated` frontmatter to all pages
- [ ] Create `/contributing` guide
- [ ] Update navigation in docs.json

## Feature Prioritization

| Priority | Feature                   | Effort | Impact |
| -------- | ------------------------- | ------ | ------ |
| P0       | Examples gallery          | Medium | High   |
| P0       | Lab comparison table      | Medium | High   |
| P1       | Lab-specific pages        | High   | High   |
| P1       | Source quotations         | Low    | Medium |
| P2       | "Last updated" indicators | Low    | Medium |
| P2       | Contributing guide        | Low    | Low    |
| P3       | Social proof              | Low    | Low    |

## System Integration

This capability builds on the Mintlify platform established in capability-22:

- **Extends navigation**: New pages auto-populate in Mintlify's nav
- **Uses built-in components**: `<Card>`, `<Accordion>`, `<Tabs>` for rich content
- **Leverages Mintlify features**: Copy-to-clipboard, syntax highlighting, dark mode
- **Adds content value**: Examples, comparisons, and lab-specific depth

## Completion Criteria

- [ ] Lab-specific pages exist for Anthropic, OpenAI, Google
- [ ] Examples gallery has at least 4 categories with real patterns
- [ ] Comparison table shows where labs agree and differ
- [ ] All pages have `lastUpdated` frontmatter
- [ ] Source quotations appear on guideline pages
- [ ] Contributing guide explains how to suggest improvements
- [ ] Users can find lab-specific guidance in under 30 seconds
