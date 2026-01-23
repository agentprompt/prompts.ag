# prompts.ag Migration to Mintlify

> Migration guide for moving prompts.ag from Next.js with hardcoded TSX content to Mintlify documentation platform.

## Objective

Adopt Mintlify's "Copy page as markdown" / "View page as markdown" pattern, which serves MDX content that renders as rich HTML while offering the same source as downloadable markdown for LLM consumption.

---

## Why Mintlify

### The Pattern We're Adopting

Anthropic's Claude Code docs (https://code.claude.com/docs/en/best-practices) demonstrate the pattern:

- **HTML page**: `https://code.claude.com/docs/en/best-practices`
- **Markdown**: `https://code.claude.com/docs/en/best-practices.md`

The markdown version contains MDX with custom components like `<Tip>`, `<Steps>`, `<Step>`, `<Callout>` — what they call "Markdown for LLMs" is actually MDX that both renders beautifully and serves as clean context for AI tools.

### Features We Get

| Feature | Description |
|---------|-------------|
| `.md` endpoint | Every page available at `{url}.md` |
| Copy page button | Contextual menu copies MDX to clipboard |
| `/llms.txt` | Auto-generated index of all pages with descriptions |
| `/llms-full.txt` | All content combined in one file |
| Open in Claude | One-click to start Claude conversation with page context |
| AI Assistant | Built-in chat that answers questions from docs |

---

## OSS Program

### Eligibility (prompts.ag qualifies if open-source)

- Open source with recognized license (MIT, Apache 2.0, GPL, etc.)
- **Not** venture-backed or revenue-funded
- **Not** owned or primarily maintained by a for-profit company

### What's Included (Free, normally $300/month)

- Custom domain support
- AI Assistant chat
- API playground
- Advanced analytics
- Version control integration
- All Pro features

### Application

**Apply here**: https://mintlify.typeform.com/oss-program

---

## Migration Steps

### Step 1: Apply to OSS Program

Do this first. Approval is typically quick for legitimate open-source projects.

### Step 2: Create Documentation Repository

Create a new Git repository for docs content:

```
prompts-ag-docs/
├── docs.json           # Site configuration (required)
├── index.mdx           # Homepage
├── favicon.png
├── logo-light.svg
├── logo-dark.svg
├── images/
│   └── ...
└── [content-pages].mdx
```

### Step 3: Configure `docs.json`

This is the main configuration file:

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
      "url": "https://github.com/your-org/prompts-ag"
    }
  ],
  "topbarCtaButton": {
    "name": "Get Started",
    "url": "/quickstart"
  },
  "navigation": [
    {
      "group": "Getting Started",
      "pages": ["index", "quickstart"]
    },
    {
      "group": "Guides",
      "pages": ["prompt-engineering", "best-practices"]
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

### Step 4: Convert TSX Content to MDX

#### MDX File Structure

Each page is an `.mdx` file with frontmatter:

```mdx
---
title: "Page Title"
description: "Brief description for SEO and llms.txt"
icon: "rocket"
---

# Page Title

Your content here...
```

#### Available Components

Mintlify provides these built-in components (no imports needed):

##### Tip / Note / Warning

```mdx
<Tip>
  Helpful suggestion or best practice.
</Tip>

<Note>
  Important information the reader should know.
</Note>

<Warning>
  Critical warning about potential issues.
</Warning>

<Info>
  General informational callout.
</Info>
```

##### Steps

```mdx
<Steps>
  <Step title="First Step">
    Description of what to do first.
    
    ```bash
    npm install something
    ```
  </Step>
  <Step title="Second Step">
    Description of the next action.
  </Step>
  <Step title="Third Step">
    Final step description.
  </Step>
</Steps>
```

##### Cards

```mdx
<CardGroup cols={2}>
  <Card title="Quick Start" icon="rocket" href="/quickstart">
    Get up and running in 5 minutes
  </Card>
  <Card title="API Reference" icon="code" href="/api">
    Complete API documentation
  </Card>
</CardGroup>
```

##### Accordion

```mdx
<AccordionGroup>
  <Accordion title="How do I get started?">
    Follow our quickstart guide to begin.
  </Accordion>
  <Accordion title="What are the prerequisites?">
    You'll need Node.js 18+ installed.
  </Accordion>
</AccordionGroup>
```

##### Tabs

```mdx
<Tabs>
  <Tab title="npm">
    ```bash
    npm install package-name
    ```
  </Tab>
  <Tab title="yarn">
    ```bash
    yarn add package-name
    ```
  </Tab>
  <Tab title="pnpm">
    ```bash
    pnpm add package-name
    ```
  </Tab>
</Tabs>
```

##### Code Blocks

````mdx
```javascript title="example.js"
const greeting = "Hello, world!";
console.log(greeting);
```

```bash
# With line highlighting
npm install package  # This line is highlighted
```
````

##### Tables (Standard Markdown)

```mdx
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

### Step 5: Set Up Local Development

Install the Mintlify CLI:

```bash
npm i -g mint
```

Clone your docs repo and run:

```bash
cd prompts-ag-docs
mint dev
```

Preview at `http://localhost:3000`

### Step 6: Connect Repository to Mintlify

1. Go to https://dashboard.mintlify.com
2. Connect your GitHub account
3. Select your docs repository
4. Install the GitHub App for automatic deployments

### Step 7: Configure Custom Domain

1. In Mintlify dashboard, go to Settings → Custom Domain
2. Add `prompts.ag` (or subdomain like `docs.prompts.ag`)
3. Configure DNS:
   - **CNAME**: Point to your Mintlify subdomain
   - Or use their DNS instructions for apex domains

### Step 8: Enable Contextual Menu

In `docs.json`, ensure contextual options are configured:

```json
{
  "contextual": {
    "options": [
      "copy",      // Copy page as Markdown
      "view",      // View as Markdown (.md URL)
      "claude"     // Open in Claude
    ]
  }
}
```

You can also add custom options:

```json
{
  "contextual": {
    "options": [
      "copy",
      "view",
      {
        "title": "Open in ChatGPT",
        "description": "Ask ChatGPT about this page",
        "icon": "message",
        "href": {
          "base": "https://chat.openai.com",
          "query": [
            {
              "key": "q",
              "value": "Help me understand: $page"
            }
          ]
        }
      }
    ]
  }
}
```

---

## Content Conversion Checklist

When converting existing TSX pages to MDX:

- [ ] Extract text content from JSX
- [ ] Convert custom React components to Mintlify equivalents
- [ ] Add frontmatter (title, description) to each page
- [ ] Update internal links to use relative paths without extensions
- [ ] Move images to `/images/` directory
- [ ] Update image references to absolute paths (`/images/example.png`)
- [ ] Test code blocks render correctly with syntax highlighting
- [ ] Verify navigation structure in `docs.json`

---

## File Naming Conventions

- Use kebab-case: `prompt-engineering.mdx` not `promptEngineering.mdx`
- Reference in navigation without extension: `"prompt-engineering"` not `"prompt-engineering.mdx"`
- Links within content: `[link text](/page-name)` not `[link text](/page-name.mdx)`

---

## Auto-Generated Files

Once deployed, Mintlify automatically generates:

| File | URL | Purpose |
|------|-----|---------|
| llms.txt | `prompts.ag/llms.txt` | Index of all pages with descriptions |
| llms-full.txt | `prompts.ag/llms-full.txt` | All content in one file |
| {page}.md | `prompts.ag/{page}.md` | Individual page as markdown |

These require no configuration — they're generated from your MDX content automatically.

---

## Resources

- **Mintlify Docs**: https://mintlify.com/docs
- **Components Reference**: https://mintlify.com/docs/components
- **OSS Program Application**: https://mintlify.typeform.com/oss-program
- **GitHub**: https://github.com/mintlify
- **Example**: Claude Code Docs at https://code.claude.com/docs

---

## Notes from Investigation

### How the "Copy page as markdown" Works

1. Content is authored as MDX files with custom components
2. Mintlify renders MDX → HTML for the web view
3. Adding `.md` to any URL serves the raw MDX source
4. The "Copy page" button fetches the `.md` version and copies to clipboard
5. Custom components like `<Tip>` remain in the markdown — LLMs handle them well

### Why MDX Over Pure Markdown

- Richer formatting without losing markdown simplicity
- Components are semantic (LLMs understand `<Warning>` intent)
- Single source of truth for both human-readable docs and LLM context
- No build step needed to generate separate markdown versions
