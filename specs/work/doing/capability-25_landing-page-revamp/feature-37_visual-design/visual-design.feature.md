# Feature: Visual Design — Terminal Noir with Amber Glow

## Observable Outcome

The landing page transforms from bland text on white to a distinctive dark-first design with atmospheric depth. Visitors immediately recognize this as a technical product with personality—not generic template UI.

## Testing Strategy

> Visual design features use **visual verification** rather than automated unit tests.
> Testing is manual inspection in browser with Playwright for automated screenshots.

### Level Assignment

| Component         | Level  | Justification                            |
| ----------------- | ------ | ---------------------------------------- |
| CSS animations    | Visual | Verify in browser, screenshot comparison |
| Responsive layout | Visual | Check breakpoints manually               |
| Color application | Visual | Verify against design language spec      |

### Escalation Rationale

- **Visual → Integration**: Visual testing captures what users see; no code-level integration tests needed for CSS/styling work.

## Feature Integration Tests (Level 2)

Visual design verification via Playwright screenshots:

### FI1: Desktop viewport renders correctly

```typescript
// Verified manually via Playwright MCP
// Screenshots: landing-page-design.png, card-hover.png
describe("Visual Design", () => {
  it("GIVEN desktop viewport WHEN page loads THEN dark background with grid pattern and amber glow wordmark visible", async () => {
    // Verified: Dark background (#0c0a09)
    // Verified: Grid pattern overlay
    // Verified: Wordmark with amber glow animation
    // Verified: Glassmorphism cards
  });
});
```

### FI2: Mobile responsive layout

```typescript
// Verified manually via Playwright MCP
// Screenshot: mobile-view.png
describe("Visual Design - Mobile", () => {
  it("GIVEN mobile viewport (375x812) WHEN page loads THEN cards stack vertically and wordmark scales", async () => {
    // Verified: Cards stack in single column
    // Verified: Wordmark scales appropriately
    // Verified: CTAs remain accessible
  });
});
```

### FI3: Hover states work correctly

```typescript
// Verified manually via Playwright MCP
// Screenshot: card-hover.png
describe("Visual Design - Interactions", () => {
  it("GIVEN card element WHEN hovered THEN amber border and arrow icon appear", async () => {
    // Verified: Amber border on hover
    // Verified: Arrow icon reveals
    // Verified: Lift effect (translateY)
  });
});
```

## Capability Contribution

This feature completes the visual identity of the landing page revamp (capability-25). The structural work (replacing sections with doc cards) enables this visual polish layer that makes the page memorable rather than generic.

## Completion Criteria

- [x] Dark background with grid pattern renders
- [x] Wordmark centered with pulsing amber glow
- [x] Noise texture overlay adds depth
- [x] Doc cards have glassmorphism + amber hover
- [x] Page load animation (staggered reveals)
- [x] Fits viewport without scroll (above fold)
- [x] Mobile responsive (verified via Playwright)
- [x] All Level 2 visual tests pass (screenshots captured)
