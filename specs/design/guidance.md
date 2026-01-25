## How to keep design in check

You’re fighting two failure modes that cause expensive rework:
 1. Style drift: each change is “locally reasonable” but globally inconsistent (spacing, typography, radii, colors, component variants, layout patterns).
 2. Code drift: the agent “learns” from whatever code happens to exist (including earlier agent slop) instead of from your intended design system and shadcn primitives.

The fix is to give the agent a single authoritative source of truth for UI decisions, plus hard guardrails that make shortcuts fail fast.

Make “design truth” explicit and local in the repo

Create a small, unambiguous contract the agent must follow:

1) One UI entry point: shadcn primitives + your wrappers
 • Treat components/ui/*(shadcn) as the only primitive UI layer.
 • Everything app-specific goes into components/app/* built only from components/ui/*.
 • Ban “random Tailwind soup” in app/** and “bespoke” one-off buttons/inputs/cards.

Practical rule:
 • No <button className="..."> in app code. Use <Button /> (or a tiny wrapper).
 • No ad-hoc form fields. Use Form, Input, Select, Textarea, etc. (and your wrappers if needed).
 • Layout is allowed to use Tailwind freely, but typography, color, and interactive elements must come from the system.

1) Tokens first, classes second

Put all visual identity into tokens:
 • app/globals.css: CSS variables for color, radius, etc. (shadcn already does this well)
 • tailwind.config.ts: extends with semantic tokens only (e.g., bg-background, text-foreground)
 • Define a spacing + typography scale you actually use (and document it).

Then give the agent a “don’t invent tokens” rule:
 • Only use predefined color utilities (bg-background, text-foreground, bg-muted, border-border, etc.)
 • Only use a small allowed set of spacing increments (e.g., 2/3/4/6/8/12/16) unless there’s a documented exception.

1) A short “UI spec” the agent must obey

Add docs/ui-spec.md (1–2 pages max) with:
 • Layout patterns (page shell, header, section spacing, max widths)
 • Typography rules (which classes for H1/H2/body/muted)
 • Component usage rules (never raw button/input; use shadcn)
 • Examples of “good” and “bad” patterns (literally snippets)

This is the file you keep pointing the agent to, repeatedly.

Make copying “existing slop” less likely than using the system

1) Create a component catalog the agent can’t ignore

Add app/(dev)/ui (or Storybook) that showcases:
 • Buttons (all variants/sizes)
 • Form patterns (validated forms)
 • Cards, tables, dialogs, toasts
 • Page layout templates

Agents imitate what’s easiest to inspect. Give them a clean “exhibit hall.”

1) Prefer wrappers for “the big 5” to prevent micro-divergence

Even with shadcn, drift happens when people use variants inconsistently. Add thin wrappers in components/app/ for:
 • AppButton (or just enforce Button)
 • AppCard (standard padding, header layout)
 • AppSection (standard section spacing, titles)
 • AppPage (max width, page padding, breadcrumb slot)
 • AppFormField (label/help/error layout)

Wrappers reduce “creative freedom” in exactly the places that cause drift.

Force fast failure with tooling

1) Lint rules that block the usual shortcuts

Use ESLint (plus a couple targeted rules) to ban primitives in app code:
 • Disallow raw <button>, <input>, <select>, <textarea> outside components/ui (and maybe components/app wrappers).
 • Disallow importing from components/ui directly from deep leaf pages if you want wrappers to be mandatory.
 • Disallow className on Button except through cn() and only for layout tweaks (optional but effective).

Even a simple lint rule catches 80% of drift.

1) CI gates that punish “looks fine to the agent”

Add:
 • pnpm lint
 • pnpm typecheck
 • pnpm test
 • pnpm test:e2e (Playwright on key flows)
 • Visual regression (Chromatic/Storybook or Percy/Playwright screenshots)

Agents are very willing to “ship” without checking UI consistency. Visual diffs are the cheapest antidote.

Drive the agent with a workflow that prevents “improv UI”

1) Require an explicit plan + inventory step before edits

Before any code change, the agent must:
 1. List relevant existing components/patterns it will reuse (file paths).
 2. State which tokens/variants it will use (e.g., Button variant="secondary", Card, Dialog).
 3. Describe any new component it wants to add and why it can’t reuse an existing one.

This single step prevents “grep-and-mimic” because you force it to justify reuse from the right place.

1) Forbid copying markup/classes from app pages

Make this an explicit instruction:
 • “Do not replicate Tailwind class strings from existing pages. Only replicate patterns from the UI catalog or shadcn primitives.”

Agents will still read existing code, but this makes it normatively wrong to treat it as a style guide.

1) Make it cheap to do the right thing

Give the agent ready-made templates:
 • components/app/page-shell.tsx
 • components/app/section.tsx
 • components/app/empty-state.tsx
 • components/app/data-table.tsx

If the “good” path is one import away, agents stop improvising.

A concrete “agent contract” prompt you can reuse

Use something like this as the top-of-task instruction (Codex / Claude Code), and keep it stable:

UI Consistency Contract (must follow)
- The only UI primitives are shadcn components in components/ui/**.
- App UI must be composed from components/ui/**and components/app/** only.
- Do not create raw <button>, <input>, <select>, <textarea> in app/**or components/app/**.
- Do not copy Tailwind class strings from existing app pages; they may contain legacy inconsistencies.
- Use only semantic tokens (bg-background, text-foreground, border-border, etc.) and documented spacing/typography rules in docs/ui-spec.md.
- Before coding: list the existing components/patterns you will reuse (with file paths). If adding a component, explain why reuse is insufficient.
- After coding: run lint, typecheck, and relevant tests; fix issues. No “seems fine”.

The highest-leverage guardrail: one canonical page template

If you do only one thing: create a single page layout template (shell + section + typography rules) and require all new pages to use it. Most “inconsistent design” is actually inconsistent layout scaffolding, not button styling.
