# Story: Terminal Noir Implementation

## Functional Requirements

### FR1: Dark-first CSS palette with amber glow variables

```gherkin
GIVEN the landing page CSS
WHEN dark-first palette is applied
THEN background is #0c0a09, foreground is #fafafa, and amber glow variables exist
```

#### Files created/modified

1. `src/app/globals.css` [modify]: Add dark-first palette, glow CSS variables, grid/noise patterns

### FR2: Wordmark component with animated glow

```gherkin
GIVEN the wordmark SVG asset
WHEN rendered on the page
THEN it displays centered with a pulsing amber glow animation (4s ease-in-out infinite)
```

#### Files created/modified

1. `src/components/Wordmark.tsx` [new]: SVG wrapper with glow animation class
2. `public/wordmark-dark.svg` [new]: Copy from assets for Next.js serving

### FR3: Glassmorphism card styling

```gherkin
GIVEN the DocCard component
WHEN rendered and hovered
THEN it has backdrop-blur, transparent background, and amber border on hover
```

#### Files created/modified

1. `src/components/DocCard.tsx` [modify]: Apply card-glass class
2. `src/app/globals.css` [modify]: Add .card-glass styles

### FR4: Page layout with background overlays

```gherkin
GIVEN the home page
WHEN rendered
THEN grid-background and noise-overlay divs are present with proper z-index
```

#### Files created/modified

1. `src/app/page.tsx` [modify]: Add background overlays, wordmark-centered layout

### FR5: Fira Code font integration

```gherkin
GIVEN the layout component
WHEN page renders
THEN Fira Code font is loaded and applied via --font-mono variable
```

#### Files created/modified

1. `src/app/layout.tsx` [modify]: Import Fira Code from next/font/google

## Testing Strategy

> Stories require **Level 1** to prove core logic works.
> Visual design stories use visual verification as Level 1 equivalent.

### Level Assignment

| Component          | Level  | Justification                   |
| ------------------ | ------ | ------------------------------- |
| CSS variables      | Visual | Verified by rendered appearance |
| Component creation | Visual | Verified by component rendering |
| Animation          | Visual | Verified by observing animation |

### When to Escalate

This story stays at visual verification because:

- CSS styling has no testable logic—output is visual
- Component structure is verified by successful render
- Animation timing is verified by observation

## Unit Tests (Level 1)

Visual verification via Playwright (equivalent to unit tests for visual work):

```typescript
// Verified via Playwright MCP browser_take_screenshot
// Files: landing-page-design.png, card-hover.png, mobile-view.png

// CSS Variables Verified:
// --accent-glow: rgba(245, 158, 11, 0.5)
// --accent-glow-soft: rgba(245, 158, 11, 0.15)
// --border-accent: rgba(245, 158, 11, 0.4)
// --grid-color: rgba(255, 255, 255, 0.03)

// Components Verified:
// - Wordmark.tsx renders with wordmark-glow class
// - DocCard.tsx renders with card-glass class
// - page.tsx has grid-background and noise-overlay divs
```

## Architectural Requirements

### Relevant ADRs

1. [DESIGN_LANGUAGE.md](../../../../design/DESIGN_LANGUAGE.md) - Brand colors, typography, wordmark usage

## Quality Requirements

### QR1: Brand Alignment

**Requirement:** All colors must match DESIGN_LANGUAGE.md
**Target:** Amber #f59e0b used for accents, dark #0c0a09 for background
**Validation:** Visual inspection against spec

### QR2: Accessibility

**Requirement:** Focus states must be visible
**Target:** 2px solid accent outline on focus-visible
**Validation:** Tab through interactive elements

### QR3: Performance

**Requirement:** Animations must not cause jank
**Target:** CSS-only animations (no JS)
**Validation:** Smooth animation on page load

## Completion Criteria

- [x] globals.css has dark-first palette with glow variables
- [x] Wordmark.tsx created with glow animation
- [x] DocCard.tsx uses card-glass class
- [x] page.tsx has grid/noise background overlays
- [x] layout.tsx loads Fira Code font
- [x] All visual verification screenshots captured
- [x] PR #6 merged to main

## Documentation

1. `specs/design/DESIGN_LANGUAGE.md` - Brand design language (updated)
2. `specs/design/guidance.md` - Design guidance notes (created)
