# Story: Convert All Content

## Functional Requirements

### FR1: Convert Hero to index.mdx

```gherkin
GIVEN Hero.tsx contains the homepage content
WHEN converting to Mintlify MDX
THEN index.mdx contains equivalent content with proper MDX formatting
```

#### Files created/modified

1. `docs/index.mdx` [modify]: Full homepage content from Hero.tsx

### FR2: Convert WhatAgentsWantSection to guidelines.mdx

```gherkin
GIVEN WhatAgentsWantSection.tsx contains 6 guidelines with source links
WHEN converting to Mintlify MDX
THEN guidelines.mdx uses CardGroup for sources and preserves all guideline text
```

#### Files created/modified

1. `docs/guidelines.mdx` [modify]: Guidelines with `<CardGroup>` for source links

### FR3: Convert FormatSection to format.mdx

```gherkin
GIVEN FormatSection.tsx contains .ag format specification with code examples
WHEN converting to Mintlify MDX
THEN format.mdx has code blocks with syntax highlighting and titles
```

#### Files created/modified

1. `docs/format.mdx` [modify]: Format spec with titled code blocks

### FR4: Convert ApproachSection to approach.mdx

```gherkin
GIVEN ApproachSection.tsx explains why no benchmarks
WHEN converting to Mintlify MDX
THEN approach.mdx contains equivalent prose content
```

#### Files created/modified

1. `docs/approach.mdx` [modify]: Approach explanation

### FR5: Convert ToolingSection to tooling.mdx

```gherkin
GIVEN ToolingSection.tsx contains a roadmap with steps
WHEN converting to Mintlify MDX
THEN tooling.mdx uses Steps component for the roadmap
```

#### Files created/modified

1. `docs/tooling.mdx` [modify]: Roadmap with `<Steps>` component

### FR6: Create changelog.mdx

```gherkin
GIVEN the site is being migrated to Mintlify
WHEN creating initial changelog
THEN changelog.mdx has first entry documenting the migration
```

#### Files created/modified

1. `docs/changelog.mdx` [modify]: Initial changelog entry

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component              | Level | Justification                 |
| ---------------------- | ----- | ----------------------------- |
| Content text preserved | 1     | String comparison TSX → MDX   |
| Links preserved        | 1     | URL extraction and comparison |
| Code blocks preserved  | 1     | Code content extraction       |
| MDX syntax valid       | 1     | MDX parser validation         |

### When to Escalate

This story stays at Level 1 because:

- We're testing content preservation (text matching)
- Visual rendering verification is a Level 2 feature test

## Unit Tests (Level 1)

````typescript
// specs/.../story-21_convert-content/tests/convert-content.test.ts
import { readFileSync } from "fs";
import { describe, expect, it } from "vitest";

describe("Story: Convert All Content", () => {
  const docsDir = "docs";
  const srcDir = "src/components";

  describe("index.mdx (from Hero.tsx)", () => {
    it("GIVEN Hero.tsx headline WHEN checking index.mdx THEN headline text preserved", () => {
      const mdx = readFileSync(`${docsDir}/index.mdx`, "utf-8");
      expect(mdx).toContain("What agents want");
    });
  });

  describe("guidelines.mdx (from WhatAgentsWantSection.tsx)", () => {
    it("GIVEN guidelines section WHEN checking MDX THEN all 6 guidelines present", () => {
      const mdx = readFileSync(`${docsDir}/guidelines.mdx`, "utf-8");

      // Key guideline phrases
      expect(mdx).toContain("Markdown in XML tags");
      expect(mdx).toContain("descriptive tag names");
    });

    it("GIVEN source links WHEN checking MDX THEN CardGroup contains all sources", () => {
      const mdx = readFileSync(`${docsDir}/guidelines.mdx`, "utf-8");

      expect(mdx).toContain("CardGroup");
      expect(mdx).toContain("Anthropic");
      expect(mdx).toContain("OpenAI");
      expect(mdx).toContain("Google");
    });
  });

  describe("format.mdx (from FormatSection.tsx)", () => {
    it("GIVEN format section WHEN checking MDX THEN code examples preserved", () => {
      const mdx = readFileSync(`${docsDir}/format.mdx`, "utf-8");

      expect(mdx).toContain("```");
      expect(mdx).toContain("<context>");
    });
  });

  describe("tooling.mdx (from ToolingSection.tsx)", () => {
    it("GIVEN tooling roadmap WHEN checking MDX THEN Steps component used", () => {
      const mdx = readFileSync(`${docsDir}/tooling.mdx`, "utf-8");

      expect(mdx).toContain("<Steps>");
      expect(mdx).toContain("Syntax highlighting");
    });
  });

  describe("changelog.mdx", () => {
    it("GIVEN new changelog WHEN checking MDX THEN has initial migration entry", () => {
      const mdx = readFileSync(`${docsDir}/changelog.mdx`, "utf-8");

      expect(mdx).toContain("Mintlify");
    });
  });
});
````

## Architectural Requirements

### Relevant ADRs

None at this level.

## Quality Requirements

### QR1: Content Preservation

**Requirement:** All text content from TSX must appear in MDX
**Target:** 100% content preservation
**Validation:** String matching in unit tests

### QR2: Link Preservation

**Requirement:** All URLs from TSX must appear in MDX
**Target:** 100% link preservation
**Validation:** URL extraction and comparison

### QR3: MDX Syntax

**Requirement:** All MDX files must be parseable
**Target:** Zero parse errors
**Validation:** MDX parser in tests (optional)

## Completion Criteria

- [ ] index.mdx has full Hero content
- [ ] guidelines.mdx has all 6 guidelines with CardGroup sources
- [ ] format.mdx has code examples with syntax highlighting
- [ ] approach.mdx has full explanation
- [ ] tooling.mdx has Steps component roadmap
- [ ] changelog.mdx has initial entry
- [ ] All Level 1 tests pass

## Documentation

No separate documentation - the MDX files ARE the documentation.
