# Story: Initialize Docs Structure

## Functional Requirements

### FR1: Create docs.json configuration

```gherkin
GIVEN the prompts.ag repository
WHEN initializing Mintlify docs structure
THEN a valid docs.json is created with site configuration
```

#### Files created/modified

1. `docs/docs.json` [new]: Mintlify site configuration with navigation, colors, contextual menu

### FR2: Create MDX file stubs

```gherkin
GIVEN docs.json defines navigation pages
WHEN initializing docs structure
THEN all referenced MDX files exist with minimal valid content
```

#### Files created/modified

1. `docs/index.mdx` [new]: Homepage stub with frontmatter
2. `docs/guidelines.mdx` [new]: Guidelines page stub
3. `docs/format.mdx` [new]: Format specification stub
4. `docs/approach.mdx` [new]: Approach page stub
5. `docs/tooling.mdx` [new]: Tooling roadmap stub
6. `docs/changelog.mdx` [new]: Changelog page stub

### FR3: Add placeholder assets

```gherkin
GIVEN Mintlify requires logo and favicon
WHEN initializing docs structure
THEN placeholder asset files are created
```

#### Files created/modified

1. `docs/logo-light.svg` [new]: Placeholder light mode logo
2. `docs/logo-dark.svg` [new]: Placeholder dark mode logo
3. `docs/favicon.png` [new]: Placeholder favicon

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component                 | Level | Justification                           |
| ------------------------- | ----- | --------------------------------------- |
| docs.json schema validity | 1     | JSON validation against Mintlify schema |
| MDX file existence        | 1     | File system checks                      |
| MDX frontmatter validity  | 1     | YAML parsing                            |

### When to Escalate

This story stays at Level 1 because:

- We're testing file creation and JSON/YAML validity
- Real Mintlify CLI verification is a Level 2 feature test

## Unit Tests (Level 1)

```typescript
// specs/.../story-21_initialize-docs/tests/initialize-docs.test.ts
import Ajv from "ajv";
import { existsSync, readFileSync } from "fs";
import { describe, expect, it } from "vitest";

describe("Story: Initialize Docs Structure", () => {
  const docsDir = "docs";

  it("GIVEN docs directory WHEN checking docs.json THEN valid JSON with required fields", () => {
    const docsJson = JSON.parse(readFileSync(`${docsDir}/docs.json`, "utf-8"));

    expect(docsJson.name).toBe("prompts.ag");
    expect(docsJson.navigation).toBeDefined();
    expect(docsJson.colors).toBeDefined();
    expect(docsJson.contextual).toBeDefined();
  });

  it("GIVEN docs.json navigation WHEN checking pages THEN all referenced MDX files exist", () => {
    const docsJson = JSON.parse(readFileSync(`${docsDir}/docs.json`, "utf-8"));
    const pages = docsJson.navigation.flatMap((group: any) => group.pages);

    for (const page of pages) {
      const filePath = `${docsDir}/${page}.mdx`;
      expect(existsSync(filePath), `Missing: ${filePath}`).toBe(true);
    }
  });

  it("GIVEN MDX files WHEN parsing frontmatter THEN valid YAML with title", () => {
    const mdxFiles = ["index", "guidelines", "format", "approach", "tooling", "changelog"];

    for (const file of mdxFiles) {
      const content = readFileSync(`${docsDir}/${file}.mdx`, "utf-8");
      expect(content).toMatch(/^---\n/); // Has frontmatter
      expect(content).toMatch(/title:/); // Has title field
    }
  });
});
```

## Architectural Requirements

### Relevant ADRs

None at this level - this is foundational setup.

## Quality Requirements

### QR1: Schema Compliance

**Requirement:** docs.json must validate against Mintlify schema
**Target:** Zero validation errors
**Validation:** JSON schema validation in unit tests

### QR2: Navigation Completeness

**Requirement:** All pages in navigation must have corresponding MDX files
**Target:** 100% coverage
**Validation:** File existence checks

## Completion Criteria

- [ ] `docs/` directory created
- [ ] `docs/docs.json` validates against Mintlify schema
- [ ] All 6 MDX stubs created with valid frontmatter
- [ ] Placeholder logo assets created
- [ ] All Level 1 tests pass

## Documentation

No user-facing documentation changes - this is infrastructure setup.
