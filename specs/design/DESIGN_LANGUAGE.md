---
priority: high
tags: [design-system, branding, prompts.ag, landing-page]
---

# prompts.ag Design Language Handoff

<metadata>
  timestamp: 2025-01-25T19:30:00Z
  project: prompts.ag
  assets_location: /mnt/user-data/outputs/
  generator_script: generate_logos.py
</metadata>

<original_task>
Design a logo and brand identity for prompts.ag (agentprompt), a file format and specification for AI agent prompts. The brand needed to convey technical precision while remaining approachable.
</original_task>

## Brand Identity

### Core Concept

The logo uses **code brackets `[ ]`** framing the letters **"ag"** (from "agentprompt") — representing structured containment of AI instructions. The brackets evoke configuration files, JSON, and technical documentation while the enclosed text humanizes the brand.

### Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| **Amber** | `#f59e0b` | Primary brand color. Brackets, "agent" text |
| **Cream** | `#fef3c7` | Icon "ag" text on dark backgrounds |
| **Dark** | `#0c0a09` | Primary background (stone-950) |
| **Off-white** | `#fafafa` | "prompt" text, light backgrounds |
| **White** | `#ffffff` | Maximum contrast variant |
| **Dark text** | `#0c0a09` | Text on light backgrounds |

**Color logic:**
- Amber brackets are always amber (brand anchor)
- "agent" is always amber (connects to icon brackets)
- "prompt" adapts to background (light text on dark, dark text on light)
- Icon "ag" adapts to background (cream on dark, dark on light)

### Typography

| Element | Font | Weight | Notes |
|---------|------|--------|-------|
| Logo text | Fira Code | Medium (500) | Monospace, technical feel |
| Body text | System/Inter | Regular | For landing page content |
| Code snippets | Fira Code | Regular | Consistency with brand |

**Font source:** Google Fonts or self-hosted
```html
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

### Spacing & Proportions

**Icon (100×100 viewBox):**
- Regular padding: 5 units (content spans 5–95)
- Tight padding: 3 units (content spans 3–97)
- Corner radius: 12 (regular), 8 (tight)

**Wordmark (203×64 viewBox regular):**
- Horizontal padding: 8 (regular), 14 (tight)
- Vertical padding: 14 (regular), 9 (tight)
- Corner radius: 8 (regular), 6 (tight)
- Icon-to-text gap: 12 units
- Icon height: 48 units within wordmark

### Adaptive Behavior

The logo responds to system color scheme:
- **Light mode (default):** Dark background, light text
- **Dark mode:** Light/off-white background, dark text

This is inverted from typical patterns because the dark background is the "hero" presentation.

## Design Tokens (CSS Custom Properties)

```css
:root {
  /* Brand colors */
  --color-amber: #f59e0b;
  --color-cream: #fef3c7;
  --color-dark: #0c0a09;
  --color-off-white: #fafafa;
  
  /* Semantic colors */
  --color-brand-primary: var(--color-amber);
  --color-bg-primary: var(--color-dark);
  --color-bg-secondary: var(--color-off-white);
  --color-text-on-dark: var(--color-off-white);
  --color-text-on-light: var(--color-dark);
  
  /* Spacing scale (based on 4px grid) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  
  /* Border radii */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  
  /* Typography */
  --font-mono: 'Fira Code', ui-monospace, monospace;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

## Visual Language Guidelines

### Do's
- Use amber as the primary accent color sparingly
- Maintain high contrast ratios (dark bg + light text or vice versa)
- Use monospace for anything code-related
- Keep UI minimal and technical-feeling
- Use generous whitespace
- Round corners consistently (prefer 8px or 12px)

### Don'ts
- Don't use gradients on the logo
- Don't place logo on busy backgrounds without sufficient padding
- Don't use amber for large background areas (it's an accent)
- Don't mix rounded and sharp corners inconsistently
- Don't add drop shadows to the logo itself

### Component Patterns

**Cards/Panels:**
```css
.card {
  background: var(--color-bg-primary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  padding: var(--space-6);
}
```

**Buttons (primary):**
```css
.btn-primary {
  background: var(--color-amber);
  color: var(--color-dark);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-4);
  font-family: var(--font-mono);
  font-weight: 500;
}
```

**Code blocks:**
```css
.code-block {
  background: var(--color-dark);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  font-family: var(--font-mono);
  color: var(--color-off-white);
}

.code-block .keyword { color: var(--color-amber); }
.code-block .string { color: var(--color-cream); }
```

## Available Assets

### Logo Files (in outputs/)

| File | Description | Use case |
|------|-------------|----------|
| `icon-rounded.svg` | Dark bg, rounded corners | App icons, favicons |
| `icon-square.svg` | Dark bg, square corners | Social media, strict grids |
| `icon-transparent.svg` | No background | Overlays, custom backgrounds |
| `icon-adaptive.svg` | Responds to color scheme | Universal usage |
| `icon-white-bg.svg` | Light background | Dark mode contexts |
| `wordmark-dark.svg` | Full logo, dark bg | Primary usage |
| `wordmark-light.svg` | Full logo, light bg | Dark mode, inverted contexts |
| `wordmark-adaptive.svg` | Responds to color scheme | Universal usage |
| `favicon-adaptive.svg` | 32×32 adaptive | Browser favicon |

All files have `-tight` variants with reduced padding.

### Generator Script

`generate_logos.py` — Regenerates all assets with configurable padding. Edit `CONFIG` at top of file to adjust spacing, colors, or corner radii.

## Landing Page Recommendations

### Hero Section
- Dark background (`#0c0a09`)
- Centered wordmark at comfortable size (max-width ~400px)
- Tagline in off-white, monospace
- Primary CTA in amber

### Content Sections
- Alternate dark/light sections sparingly
- Use amber for highlights, links, and emphasis
- Code examples prominently featured
- Generous vertical spacing (64px+ between sections)

### Footer
- Dark background matching hero
- Subtle border-top for separation
- Links in off-white, hover in amber

## Example: Minimal Landing Page Structure

```html
<body class="bg-dark text-off-white">
  <header class="py-6">
    <img src="wordmark-dark.svg" alt="agentprompt" class="h-12">
  </header>
  
  <main>
    <section class="hero py-24 text-center">
      <h1 class="font-mono text-4xl">
        <span class="text-amber">agent</span>prompt
      </h1>
      <p class="text-cream mt-4">A file format for AI agent prompts</p>
      <button class="bg-amber text-dark mt-8 px-6 py-3 rounded-md font-mono">
        Get Started
      </button>
    </section>
    
    <section class="features py-16">
      <!-- Feature cards with subtle borders -->
    </section>
  </main>
  
  <footer class="border-t border-white/10 py-8">
    <!-- Footer content -->
  </footer>
</body>
```

## Critical Notes

1. **All SVG files use paths, not text** — No font dependencies; renders identically everywhere
2. **Adaptive SVGs use CSS `@media (prefers-color-scheme)`** — Test in both modes
3. **Amber is the brand anchor** — Should appear in every major view
4. **Dark mode inverts the background, not the brand** — Amber stays amber
5. **Fira Code Medium is essential** — Other monospace fonts will look noticeably different

---

*Generated from logo development session. See `generate_logos.py` for programmatic asset generation.*
