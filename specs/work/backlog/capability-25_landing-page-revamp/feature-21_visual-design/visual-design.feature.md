# Feature: Visual Design — Terminal Noir with Amber Glow

## Observable Outcome

The landing page transforms from bland text on white to a distinctive dark-first design with atmospheric depth. Visitors immediately recognize this as a technical product with personality—not generic template UI.

## Design Direction

**Aesthetic**: Terminal Noir with Amber Glow

A dark, atmospheric landing page that leans into the code/terminal aesthetic. The amber accent becomes a luminous glow against deep darkness—like syntax highlighting in a dimly lit room.

### Key Visual Elements

| Element        | Treatment                                                   |
| -------------- | ----------------------------------------------------------- |
| **Background** | Dark (#0c0a09) with subtle grid pattern evoking code editor |
| **Wordmark**   | Centered hero with animated ambient amber glow              |
| **Cards**      | Glassmorphism with amber accent borders on hover            |
| **Typography** | Fira Code throughout, dramatic scale contrast               |
| **Texture**    | Subtle noise overlay for depth                              |
| **Animation**  | Pulsing glow on wordmark, staggered card reveals            |

### Color Application

From [DESIGN_LANGUAGE.md](../../../design/DESIGN_LANGUAGE.md):

- **Amber (#f59e0b)**: Glow effects, accent borders, CTAs, hover states
- **Dark (#0c0a09)**: Primary background (stone-950)
- **Off-white (#fafafa)**: Body text, secondary elements
- **Cream (#fef3c7)**: Subtle highlights, code strings

### Visual Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│                    [subtle grid bg]                      │
│                                                          │
│              ╔═══════════════════════╗                   │
│              ║   [ag] agentprompt    ║  ← wordmark       │
│              ╚═══════════════════════╝    with glow      │
│                    ~~~~~~~~~~~~~~~                       │
│                     amber glow                           │
│                                                          │
│           "Structured prompts that models prefer"        │
│                                                          │
│              ┌──────────┐  ┌──────────┐                  │
│              │ Read docs│  │  GitHub  │                  │
│              └──────────┘  └──────────┘                  │
│                                                          │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│   │Guidelines│  │ Format  │  │Approach │  │ Tooling │    │
│   │         │  │         │  │         │  │         │    │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│        ↑ glassmorphism cards with amber hover            │
│                                                          │
│   ─────────────────────────────────────────────────────  │
│                      footer                              │
└─────────────────────────────────────────────────────────┘
```

## Testing Strategy

> Visual design features use **visual verification** rather than unit tests.
> Testing is manual inspection in browser with Playwright for automated screenshots.

### Level Assignment

| Component         | Level  | Justification                            |
| ----------------- | ------ | ---------------------------------------- |
| CSS animations    | Visual | Verify in browser, screenshot comparison |
| Responsive layout | Visual | Check breakpoints manually               |
| Dark mode         | Visual | Toggle system preference, verify         |

### Verification Checklist

- [ ] Wordmark displays centered with amber glow animation
- [ ] Grid pattern visible but subtle on background
- [ ] Cards have glassmorphism effect (backdrop-blur)
- [ ] Hover states show amber accent borders
- [ ] Staggered animation on page load
- [ ] Mobile responsive (cards stack, wordmark scales)
- [ ] No light mode (dark-first, forced dark)

## Implementation Files

### Modify

| File                         | Changes                                                          |
| ---------------------------- | ---------------------------------------------------------------- |
| `src/app/globals.css`        | Dark-first palette, glow animations, grid pattern, noise texture |
| `src/app/page.tsx`           | Replace Hero with wordmark-centered layout                       |
| `src/components/Hero.tsx`    | Remove, merge into page or new component                         |
| `src/components/DocCard.tsx` | Add glassmorphism, amber hover border                            |

### Create

| File                                | Purpose                                  |
| ----------------------------------- | ---------------------------------------- |
| `src/components/Wordmark.tsx`       | SVG wordmark with glow animation wrapper |
| `src/components/GridBackground.tsx` | CSS grid pattern background              |

### Assets

| File                                | Usage                          |
| ----------------------------------- | ------------------------------ |
| `assets/wordmark/wordmark-dark.svg` | Hero wordmark (already exists) |

## Capability Contribution

This feature completes the visual identity of the landing page revamp (capability-25). The structural work is done—content sections replaced with doc cards. This feature adds the visual polish that makes the page memorable rather than generic.

## Completion Criteria

- [ ] Dark background with grid pattern renders
- [ ] Wordmark centered with pulsing amber glow
- [ ] Noise texture overlay adds depth
- [ ] Doc cards have glassmorphism + amber hover
- [ ] Page load animation (staggered reveals)
- [ ] Fits viewport without scroll (above fold)
- [ ] Screenshots captured for visual regression
