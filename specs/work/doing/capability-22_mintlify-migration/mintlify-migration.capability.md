# Capability: Mintlify Migration

> **Status**: BACKLOG — Migrate prompts.ag from Next.js to Mintlify documentation platform

## Success Metric

**Quantitative Target:**

- **Baseline**: Custom Next.js site with hardcoded TSX content
- **Target**: Mintlify-hosted site with MDX content, `.md` endpoints, and LLM-friendly features
- **Measurement**: Site live on prompts.ag with all existing content plus Mintlify's built-in features working

## Why Mintlify

### The Pattern We're Adopting

Anthropic's Claude Code docs demonstrate the ideal pattern for a site about AI prompt formats:

- **HTML page**: `https://code.claude.com/docs/en/best-practices`
- **Markdown**: `https://code.claude.com/docs/en/best-practices.md`

Every page serves both as rich HTML for humans and clean markdown for LLMs. This is exactly what prompts.ag should embody — eating our own dog food.

### Features We Get for Free

| Feature             | Description                                 | Replaces from capability-24 |
| ------------------- | ------------------------------------------- | --------------------------- |
| `.md` endpoint      | Every page available at `{url}.md`          | — (new)                     |
| Copy page button    | Contextual menu copies MDX to clipboard     | Copy-to-clipboard           |
| `/llms.txt`         | Auto-generated index of all pages           | — (new)                     |
| `/llms-full.txt`    | All content combined in one file            | — (new)                     |
| Open in Claude      | One-click to start Claude conversation      | — (new)                     |
| AI Assistant        | Built-in chat answering questions from docs | — (new)                     |
| RSS feed            | Auto-generated for changelogs               | RSS feed                    |
| Changelog           | Built-in `Update` components with filtering | Changelog                   |
| Navigation          | Auto-generated from content structure       | Sticky header navigation    |
| Dark mode           | Built-in theme switching                    | Dark mode toggle            |
| Syntax highlighting | Built-in code block highlighting            | Syntax highlighting         |

### OSS Program

Mintlify offers free Pro tier ($300/month value) for qualifying open-source projects:

- Open source with recognized license (MIT ✓)
- Not venture-backed or revenue-funded ✓
- Not owned by a for-profit company ✓

**Apply**: https://mintlify.typeform.com/oss-program

## Testing Strategy

### Level Assignment

| Component               | Level | Justification                                   |
| ----------------------- | ----- | ----------------------------------------------- |
| Individual MDX pages    | 1     | Verifies content renders correctly              |
| Site navigation & links | 2     | Verifies pages integrate into cohesive site     |
| Complete migration      | 3     | Verifies feature parity + new capabilities work |

### Escalation Rationale

- **1 → 2**: Pages rendering individually doesn't prove navigation works
- **2 → 3**: Navigation working doesn't prove all Mintlify features (llms.txt, .md endpoints) function correctly

## Capability E2E Tests (Level 3)

### E2E1: Content accessible as markdown

```typescript
describe("Capability: Mintlify Migration", () => {
  it("GIVEN the site is migrated WHEN accessing any page with .md suffix THEN raw MDX is returned", async () => {
    // Given: Site is live on Mintlify
    const response = await fetch("https://prompts.ag/format.md");

    // Then: Response contains MDX content
    expect(response.status).toBe(200);
    const content = await response.text();
    expect(content).toContain("<"); // Has MDX tags
    expect(content).toContain("# "); // Has markdown headers
  });
});
```

### E2E2: LLM index files generated

```typescript
describe("Capability: Mintlify Migration", () => {
  it("GIVEN the site is migrated WHEN accessing llms.txt THEN index of all pages is returned", async () => {
    // Given: Site is live on Mintlify
    const response = await fetch("https://prompts.ag/llms.txt");

    // Then: Response contains page index
    expect(response.status).toBe(200);
    const content = await response.text();
    expect(content).toContain("format");
    expect(content).toContain("approach");
  });
});
```

### E2E3: All existing content preserved

```typescript
describe("Capability: Mintlify Migration", () => {
  it("GIVEN the site is migrated WHEN visiting the homepage THEN all sections are present", async () => {
    // Given: Site is live on Mintlify
    await page.goto("https://prompts.ag");

    // Then: All content sections exist
    await expect(page.locator("text=What agents want")).toBeVisible();
    await expect(page.locator("text=Markdown in XML tags")).toBeVisible();
    await expect(page.locator("text=The format")).toBeVisible();
    await expect(page.locator("text=Why we don't benchmark")).toBeVisible();
    await expect(page.locator("text=Tooling")).toBeVisible();
  });
});
```

## Planned Features

### Feature: OSS Program Application

**Prerequisites:**

- Verify prompts.ag repo is public with MIT license
- Prepare application with project description

**Application:**

- Apply at https://mintlify.typeform.com/oss-program
- Wait for approval (typically quick for legitimate projects)

---

### Feature: Documentation Repository Setup

**Create new repository structure:**

```
prompts-ag-docs/
├── docs.json           # Site configuration
├── index.mdx           # Homepage (hero + overview)
├── format.mdx          # The .ag format specification
├── guidelines.mdx      # Markdown in XML tags
├── approach.mdx        # Why we don't benchmark
├── tooling.mdx         # Tooling roadmap
├── changelog.mdx       # Product updates
├── favicon.png
├── logo-light.svg
├── logo-dark.svg
└── images/
```

**Configure docs.json:**

```json
{
  "$schema": "https://mintlify.com/schema.json",
  "name": "prompts.ag",
  "logo": {
    "light": "/logo-light.svg",
    "dark": "/logo-dark.svg"
  },
  "favicon": "/favicon.png",
  "colors": {
    "primary": "#0D9373",
    "light": "#07C983",
    "dark": "#0D9373"
  },
  "topbarLinks": [
    {
      "name": "GitHub",
      "url": "https://github.com/agentprompt/prompts.ag"
    }
  ],
  "navigation": [
    {
      "group": "Reference",
      "pages": ["index", "guidelines", "format", "approach"]
    },
    {
      "group": "Resources",
      "pages": ["tooling", "changelog"]
    }
  ],
  "contextual": {
    "options": ["copy", "view", "claude"]
  },
  "feedback": {
    "thumbsRating": true
  }
}
```

---

### Feature: Content Conversion (TSX → MDX)

Convert each section from React TSX to Mintlify MDX:

| Current TSX Component     | Target MDX File | Notes                         |
| ------------------------- | --------------- | ----------------------------- |
| Hero.tsx                  | index.mdx       | Combine with overview content |
| WhatAgentsWantSection.tsx | guidelines.mdx  | Use `<Card>` for source links |
| FormatSection.tsx         | format.mdx      | Use code blocks with titles   |
| ApproachSection.tsx       | approach.mdx    | Standard markdown             |
| ToolingSection.tsx        | tooling.mdx     | Use `<Steps>` for roadmap     |
| Footer.tsx                | (built-in)      | Configure in docs.json        |

**MDX Features to Use:**

- `<Tip>`, `<Note>`, `<Warning>` for callouts
- `<Card>` and `<CardGroup>` for source links
- `<Steps>` for the tooling roadmap
- `<Tabs>` for multi-lab examples (future)
- Code blocks with `title` for filenames

---

### Feature: Deployment & Custom Domain

**Connect to Mintlify:**

1. Go to https://dashboard.mintlify.com
2. Connect GitHub account
3. Select docs repository
4. Install GitHub App for automatic deployments

**Configure custom domain:**

1. In Mintlify dashboard → Settings → Custom Domain
2. Add `prompts.ag`
3. Configure DNS (CNAME or A record per Mintlify instructions)
4. Wait for SSL provisioning

---

### Feature: Contextual Menu Configuration

Enable the "Markdown for LLMs" features:

```json
{
  "contextual": {
    "options": [
      "copy", // Copy page as Markdown
      "view", // View as Markdown (.md URL)
      "claude", // Open in Claude
      {
        "title": "Open in ChatGPT",
        "description": "Ask ChatGPT about this page",
        "icon": "message",
        "href": {
          "base": "https://chat.openai.com",
          "query": [{ "key": "q", "value": "Help me understand: $page" }]
        }
      }
    ]
  }
}
```

---

### Feature: Verify Auto-Generated Files

After deployment, verify these endpoints work:

| File          | URL                        | Purpose                              |
| ------------- | -------------------------- | ------------------------------------ |
| llms.txt      | `prompts.ag/llms.txt`      | Index of all pages with descriptions |
| llms-full.txt | `prompts.ag/llms-full.txt` | All content in one file              |
| {page}.md     | `prompts.ag/{page}.md`     | Individual page as markdown          |
| RSS           | `prompts.ag/rss.xml`       | Changelog feed                       |

---

## Migration Checklist

- [ ] Apply to Mintlify OSS program
- [ ] Receive approval
- [ ] Create docs repository with structure
- [ ] Configure docs.json
- [ ] Convert Hero.tsx → index.mdx
- [ ] Convert WhatAgentsWantSection.tsx → guidelines.mdx
- [ ] Convert FormatSection.tsx → format.mdx
- [ ] Convert ApproachSection.tsx → approach.mdx
- [ ] Convert ToolingSection.tsx → tooling.mdx
- [ ] Create changelog.mdx
- [ ] Add logo assets (light/dark)
- [ ] Test locally with `mint dev`
- [ ] Connect repository to Mintlify dashboard
- [ ] Configure custom domain
- [ ] Verify DNS propagation
- [ ] Verify all .md endpoints work
- [ ] Verify llms.txt and llms-full.txt generated
- [ ] Verify contextual menu (copy, view, claude)
- [ ] Archive or redirect old Next.js site

## System Integration

This capability is a **platform migration** that:

- **Replaces** the Next.js foundation from capability-21
- **Enables** many features planned in capability-24 via Mintlify built-ins
- **Preserves** all existing content (converted to MDX)
- **Adds** LLM-friendly features that align perfectly with prompts.ag's mission

## Completion Criteria

- [ ] Site live at prompts.ag on Mintlify
- [ ] All existing content accessible
- [ ] `.md` endpoints work for all pages
- [ ] `llms.txt` and `llms-full.txt` generated
- [ ] Contextual menu shows copy/view/claude options
- [ ] Dark/light mode works
- [ ] Navigation functions correctly
- [ ] RSS feed available for changelog

## Reference

See [prompts-ag-mintlify-migration-guide.md](../../../prompts-ag-mintlify-migration-guide.md) for detailed technical guidance.
