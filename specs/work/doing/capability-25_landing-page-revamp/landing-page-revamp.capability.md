# Capability: Landing Page Revamp

## Context

Two properties now exist:

- **prompts.ag**: Landing page (Next.js)
- **docs.prompts.ag**: Reference documentation (Mintlify)

The current landing page duplicates content that now lives in docs. It has full guidelines, format spec, approach essay, and tooling roadmap sections. This was appropriate before docs existed—now it's redundant and confusing.

**Problem**: Visitors don't immediately understand what prompts.ag is or why they should care.

**Solution**: Strip the landing page to its essential job—answer "what is this?" and point to docs.

## Success Metric

**Quantitative Target:**

- **Baseline**: 5+ scrollable sections, duplicated content, unclear purpose
- **Target**: Single-screen landing page with clear value proposition and 3-4 doc links
- **Measurement**: Page can be understood without scrolling; all content sections link to docs

## Design System Foundation

Before revamping components, establish a lightweight design system:

### Tokens (CSS Variables)

```css
:root {
  --background: ...;
  --foreground: ...;
  --muted: ...;
  --muted-foreground: ...;
  --primary: ...;
  --primary-foreground: ...;
  --border: ...;
  --radius: ...;
}
```

### Spacing Scale (6 values only)

```
4 (1rem), 6 (1.5rem), 8 (2rem), 12 (3rem), 16 (4rem), 24 (6rem)
```

### Typography Scale

```
text-sm, text-base, text-lg, text-xl, text-2xl, text-4xl
```

### Reusable Wrappers

- `<Section>` - consistent vertical rhythm, max-width, padding
- `<Card>` - optional, for linking to docs sections

## Landing Page Structure

### Hero (Keep, Refine)

- **Headline**: "What agents want" (keep—it's distinctive)
- **Subheadline**: One sentence explaining what prompts.ag is
- **Code example**: Keep—shows rather than tells
- **CTA**: "Read the docs →" linking to docs.prompts.ag

### Content Cards (Replace Sections)

Replace WhatAgentsWantSection, FormatSection, ApproachSection, ToolingSection with a simple card grid:

| Card       | Links To                   | Description              |
| ---------- | -------------------------- | ------------------------ |
| Guidelines | docs.prompts.ag/guidelines | "Markdown in XML tags"   |
| Format     | docs.prompts.ag/format     | ".ag specification"      |
| Approach   | docs.prompts.ag/approach   | "Why we don't benchmark" |
| Tooling    | docs.prompts.ag/tooling    | "Editor support"         |

### Footer (Keep)

- MIT license
- AGENTS.md link
- GitHub link

## Verification

Open the page. Look at it. Click the links.

- Does it look right?
- Do the links work?
- Does dark mode work?

That's it.

## Files to Modify

### Remove (content now in docs)

- `src/components/WhatAgentsWantSection.tsx` → delete or gut
- `src/components/FormatSection.tsx` → delete or gut
- `src/components/ApproachSection.tsx` → delete or gut
- `src/components/ToolingSection.tsx` → delete or gut
- `src/components/ProblemSection.tsx` → delete (never activated)

### Modify

- `src/components/Hero.tsx` → refine copy, update CTA to docs
- `src/app/page.tsx` → replace sections with card grid
- `src/app/globals.css` → add/verify design tokens

### Create

- `src/components/Section.tsx` → if not reusable enough, refine
- `src/components/DocCard.tsx` → card linking to docs section
- `specs/ui-spec.md` → lightweight design system reference

## Completion Criteria

- [ ] Design tokens defined in globals.css
- [ ] ui-spec.md documents tokens, spacing, typography
- [ ] Hero updated with refined copy and docs CTA
- [ ] Content sections replaced with card grid
- [ ] All cards link to correct docs.prompts.ag pages
- [ ] Page fits in viewport without scroll (above fold)
- [ ] Dark mode works via CSS variables
