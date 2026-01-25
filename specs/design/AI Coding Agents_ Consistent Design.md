# **Governing the Machine: Architecting Deterministic AI Workflows for Next.js and ShadCN UI**

## **1\. The Epistemological Crisis of AI-Generated Interfaces**

The integration of Large Language Models (LLMs) into the software development lifecycle has precipitated a fundamental shift in the economics of code production. Tools such as Claude Code, GitHub Copilot, and Cursor have reduced the marginal cost of syntax generation to near zero. However, in the specific domain of component-based front-end architectures—exemplified by the Next.js, TailwindCSS, and ShadCN UI stack—this velocity often comes at the expense of architectural integrity.1 The central challenge facing modern engineering teams is no longer how to generate code, but how to prevent "AI drift," a phenomenon where the stochastic nature of generative models leads to a gradual accumulation of technical debt, visual inconsistencies, and "slop"—code that is syntactically valid but architecturally incoherent.1

### **1.1 The Mechanics of "Slop" and the Mimicry Paradox**

To understand how to drive a state-of-the-art agent effectively, one must first dissect the pathology of its failure modes. When an agent is tasked with "modifying a Next.js site using ShadCN UI," it does not inherently understand the design philosophy of the project. Instead, it operates as a probabilistic engine seeking the most likely completion based on the context provided.

The most pernicious source of degradation arises from the "Grep Trap".3 Standard agentic workflows often rely on naive retrieval mechanisms—searching the codebase for similar files to use as templates. While intended to promote consistency, this mechanism often creates a feedback loop of degradation known as the "Mimicry Paradox." If the existing codebase contains even a single instance of an anti-pattern—such as hardcoding a hex color value (\#0f172a) instead of using a Tailwind semantic variable (bg-slate-900), or manually implementing a button instead of importing the ShadCN primitive—the agent is statistically likely to latch onto this deviation as the "local convention".1

This mimicry is reinforced by the agent's tendency to prioritize local context (the files immediately surrounding the task) over global architectural rules. The agent "greps" through the directory, identifies a component that looks similar to the requested feature, and clones its structure—warts and all. In doing so, it bypasses the carefully constructed utility layers of ShadCN and Tailwind, treating the project not as a coherent system of tokens and primitives, but as a collection of loose text files to be emulated.1

### **1.2 Hallucination in the Absence of Live Context**

A secondary, yet equally critical, failure mode is the hallucination of component APIs. ShadCN UI is built on a "headless" philosophy, utilizing Radix UI primitives that are styled via Tailwind and copied directly into the project's components/ui directory. Unlike traditional npm libraries (e.g., Material UI), where the source code is hidden in node\_modules, ShadCN components are mutable files within the codebase.

AI models, trained on vast datasets with knowledge cutoffs, often possess outdated or conflated internal representations of these libraries.2 An agent might confidently generate a \<Button loading={true} /\> component, assuming the existence of a loading prop common in other design systems. If the local ShadCN implementation does not support this prop, the generated code will fail at runtime or require manual wrapping. The agent "guesses" because it lacks a live connection to the *actual* TypeScript interfaces defining the components in the current project environment.2 It fills the gap in its retrieval-augmented generation (RAG) context with probabilistic tokens, stitching together a solution that mimics the *appearance* of correctness while violating the *strictness* of the type system.

### **1.3 The Visual Consistency Gap**

Finally, text-based coding agents suffer from a sensory deficit: they cannot "see" the output they generate. When an agent predicts a sequence of Tailwind classes, it is manipulating semantic abstractions of visual properties (p-4, flex, items-center). It cannot verify alignment, contrast ratios, or responsive behavior across viewports.

This leads to "style drift," where margins, paddings, and font sizes deviate incrementally from the design tokens.4 An agent might interpret "add some space" as mt-4 in one instance and my-6 in another, leading to a jagged, unprofessional rhythm in the user interface. Without a feedback loop that incorporates visual verification, the agent continues to hallucinate layout adjustments, compounding the drift until the application requires a costly "visual refactor".6

## ---

**2\. Infrastructure as Context: The Context Engineering Paradigm**

The solution to these pathologies lies in shifting the developer's role from "writer of code" to "architect of context." We must engineer the environment in which the agent operates, replacing probabilistic guessing with deterministic retrieval. This is achieved through the deployment of Model Context Protocol (MCP) servers and the rigorous definition of "Constitutional" context files.

### **2.1 The Model Context Protocol (MCP) Revolution**

The Model Context Protocol (MCP) represents a paradigm shift in how AI agents interact with development environments. Rather than relying solely on pre-trained knowledge or text-based search, MCP allows an agent to establish a live, structured connection to the runtime environment and file system.2

#### **2.1.1 The ShadCN MCP Server: Grounding the Agent in Truth**

The ShadCN MCP server acts as the authoritative source of truth for component definitions. By integrating this server, we enable the agent to query the component registry directly, bypassing the need to "guess" imports or props.2

**Mechanism of Action:**

When an agent is tasked with "implementing a card with a form," the enabled MCP workflow fundamentally alters the execution path:

1. **Tool Call vs. Hallucination:** Instead of generating the import statement immediately, the agent executes a tool call: get\_component\_schema('card').  
2. **Retrieval:** The MCP server accesses the local components.json configuration and the components/ui directory, returning the *exact* TypeScript interface and file path of the Card component as it exists in the project.7  
3. **Deterministic Generation:** The agent utilizes this schema to generate code that strictly adheres to the component's API. It knows, for instance, that CardContent must be a child of Card, and that className overrides should be merged using the cn() utility, because the schema dictates it.8

**Configuration Strategy:**

For environments like Cursor or Claude Code, the setup requires explicit configuration in the project's MCP settings file.

**Table 1: Comparative Configuration for MCP Integration**

| Environment | Configuration File | Command / Argument | Operational Impact |
| :---- | :---- | :---- | :---- |
| **Cursor** | .cursor/mcp.json | npx shadcn@latest mcp | Enables the Cursor agent to execute npx commands to query the registry dynamically. 2 |
| **Claude Code** | \~/.claude/config.json | claude mcp add shadcn | Registers the server globally, allowing it to persist across sessions and projects. 7 |
| **Project Scope** | components.json | registries object | Defines private or custom registries (e.g., internal company UI kits) for the agent to access. 2 |

This infrastructure eliminates the "outdated patterns" problem. Even if the AI's training data suggests a pattern from 2023, the MCP server provides the live 2024/2025 definition, forcing the model to align with the current reality.2

#### **2.1.2 Playwright MCP: The Visual Feedback Loop**

To address the visual consistency gap, the infrastructure must be augmented with the Playwright MCP server. This tool gives the agent "hands" to manipulate a browser and "eyes" to inspect the result.9

**Integration Workflow:**

* **Verification Prompt:** "Verify the mobile responsiveness of the newly created navbar. Ensure the hamburger menu is actionable."  
* **Agent Execution:** The agent utilizes the Playwright MCP to launch a headless browser, resize the viewport to 375px, and inspect the accessibility tree.  
* **Self-Correction:** If the agent detects that the menu button is obscured by another element (via bounding box analysis), it can self-correct the z-index in the Tailwind classes before presenting the solution to the user.11

This closes the loop between code generation and visual rendering, transforming the agent from a blind architect into a sighted builder.

### **2.2 Constitutional AI: The Role of Context Files**

While MCP servers provide dynamic access to tools, "Constitutional" context files—specifically .cursorrules and CLAUDE.md—provide the static laws that govern the agent's behavior. These files are not merely suggestions; they are the rigid constraints that prevent "slop."

#### **2.2.1 The .cursorrules Specification**

For users of the Cursor IDE, the .cursorrules file located at the project root is the primary mechanism for behavioral control.12 To prevent ShadCN/Next.js specific anti-patterns, this file must be exhaustive.

**Critical Rule Definitions:**

* **Tech Stack Enclosure:** Explicitly define the boundaries of the stack to prevent the agent from importing extraneous libraries.  
  * *Rule:* "You are an expert in Next.js 15 (App Router), React 19, TailwindCSS, and ShadCN UI. Do not suggest solutions using Pages Router, Bootstrap, or Material UI.".13  
* **Styling Orthodoxy:** Enforce the "Utility-First" philosophy to prevent the proliferation of CSS modules or arbitrary styles.  
  * *Rule:* "Always use Tailwind utility classes. Do not create .css or .module.css files unless explicitly requested. Use the cn() utility from @/lib/utils for class merging. Do not use the @apply directive.".14  
* **Component Architecture:** Dictate the structure of the React components to ensure maintainability.  
  * *Rule:* "Prefer React Server Components (RSC) by default. Only use 'use client' at the leaf nodes of the render tree where interactivity is strictly required. Use named exports for all components.".15  
* **The "Anti-Slop" Clause:** Explicitly prohibit the "Grep Trap."  
  * *Rule:* "Before creating a new UI component, ALWAYS check the components/ui directory to see if a ShadCN primitive exists. Do not reinvent the wheel. Do not assume props exist; verify them via MCP or by reading the component file.".13

**Table 2: The .cursorrules Governance Matrix**

| Category | Rule / Constraint | Rationale for Consistency |
| :---- | :---- | :---- |
| **Architecture** | "Use Server Actions for mutations." | Prevents API route proliferation and enforces Next.js 15 best practices. 16 |
| **Styling** | "Use CSS variables for colors (e.g., bg-primary)." | Prevents hardcoded hex values and ensures dark mode compatibility. 14 |
| **Imports** | "Group imports: React \-\> Next \-\> Libs \-\> Local." | Maintains readability and prevents circular dependency confusion. 17 |
| **Logic** | "Use Zod for all form validation." | Enforces type safety and ShadCN form compatibility. 14 |

#### **2.2.2 The CLAUDE.md Protocol**

For developers interacting with Claude Code via the CLI, the CLAUDE.md file serves a parallel purpose, focusing on operational commands and high-level architectural maps.18

**Key Architectural Inclusions:**

* **Project Geography:** A concise ASCII tree of the app directory helps the agent navigate without performing excessive ls commands, reducing token usage and confusion.20  
* **Design Token Reference:** A condensed listing of the primary design tokens (colors, spacing, typography) acts as a "cheat sheet," allowing the agent to select the correct Tailwind classes without needing to parse the entire globals.css file.21  
* **Command Dictionary:** Explicit instructions on how to run tests (pnpm test), lint code (pnpm lint), and start the server. This prevents the agent from attempting to use npm or yarn in a pnpm monorepo, which can cause lockfile drift.17

## ---

**3\. Operational Protocols: The Agentic Workflow Loop**

Establishing the correct infrastructure is only half the battle. The second half is defining the *interaction model*. Treating an AI agent as a chatbot—a conversational partner—is a fundamental error in engineering contexts. To drive a state-of-the-art agent, one must enforce a strict "Agent Workflow Protocol" that mirrors the discipline of a senior engineer.3

### **3.1 The R-C-P-R-B Protocol (Research-Clarify-Plan-Review-Build)**

To prevent the agent from taking shortcuts, every significant task must be forced through a structured sequence known as the R-C-P-R-B protocol.3

#### **Phase 1: Research (The Targeted Grep)**

Instead of allowing the agent to "grep" blindly, the user must direct the research phase. The goal is to identify *specific* relevant files and establish the "ground truth" before any code is conceived.

* **The Problem:** A prompt like "Update the header" leads to the agent scanning the entire codebase and potentially modifying the wrong file.  
* **The Protocol Prompt:** "Research the current header implementation. Identify the file defining the layout shell (layout.tsx) and any existing navigation components. List the file paths you intend to analyze.".3  
* **Insight:** This forces the agent to explicitize its search space. If it lists old-header.tsx (a deprecated component), the user can correct it immediately, preventing work on dead code.

#### **Phase 2: Clarify (The Assumption Check)**

The agent must be configured (via .cursorrules or prompt) to ask clarifying questions before proceeding to the planning phase.

* **Agent Interaction:** "I found Header.tsx. It currently uses a static position. Do you want the sticky behavior to persist on mobile viewports, or only on desktop? Should the background be translucent?".3  
* **Strategic Value:** This step forces the agent to expose its internal assumptions. It allows the human architect to inject design constraints (e.g., "Mobile header must be static to avoid iOS Safari layout shifts") that the agent could not have inferred from the code alone.

#### **Phase 3: Plan (The "Plan Mode" Enforcement)**

Most advanced tools, including Cursor and Claude Code, support a "Plan Mode" or allow a prompt to request a detailed implementation plan. This is the most critical gate in the workflow.22

* **Requirement:** The plan must be granular. It should list the specific Tailwind classes to be added, the ShadCN components to be imported, and the logic changes required.  
* **Validation:** The human reviews the plan, not the code. Reviewing natural language is cognitively cheaper and faster than reviewing diffs.  
* **Correction Example:** "You proposed using bg-white for the sticky header. Our design system requires bg-background/95 backdrop-blur-sm for dark mode support. Update the plan.".3

#### **Phase 4: Review and Build**

Only after the plan is explicitly approved does the agent generate code. The human then reviews the diffs, watching specifically for "slop" markers like hardcoded values or unused imports. Because the plan was vetted, the code review focuses on implementation details (syntax, performance) rather than architectural intent.3

### **3.2 The "Zoom-In" Methodology: Managing Context Windows**

For complex UI tasks, such as "Building a SaaS Dashboard," attempting to generate the entire page in a single turn results in hallucinated components and poor layout consistency. The context window becomes saturated, and the agent begins to prioritize completion over precision.6

**The "Zoom-In" Strategy:**

1. **Macro Pass (The Skeleton):** "Generate the high-level layout grid for the dashboard using standard div elements and Tailwind width/height classes. Do not add content or components yet."  
   * *Result:* A clean wireframe that establishes the spatial relationships.  
2. **Meso Pass (The Component Injection):** "Replace the top-left quadrant div with the Card component from ShadCN. Include a CardHeader and CardContent."  
   * *Result:* The correct structural components are placed within the validated layout.  
3. **Micro Pass (The Polish):** "Apply the muted-foreground color token to the subtitle text. Ensure the button uses the outline variant and includes the ArrowRight icon from Lucide.".6

This iterative approach keeps the agent's attention focused on a manageable scope ("Micro-Context"), allowing for rigorous verification of ShadCN adherence at each layer of abstraction.

## ---

**4\. The Generative UI Pipeline: v0.dev Integration**

For the initial creation of complex UI sections, pure coding agents often struggle with aesthetic nuance. They can write correct code, but they lack the "design eye" to combine Tailwind classes into a visually pleasing result. **v0.dev** (by Vercel) serves as a specialized generative UI tool that understands ShadCN and Tailwind natively, bridging the gap between design and code.23

### **4.1 The Hybrid Workflow: From Generative to Deterministic**

The optimal workflow combines the aesthetic capability of v0 with the architectural rigor of Cursor/Claude.

#### **Phase 1: Generative Ideation (v0)**

Use v0 to iterate on the *visual* design. The prompt here focuses on "vibe" and structure rather than code specifics.

* **Prompt:** "Create a pricing table with three tiers. The middle tier should be highlighted as 'Most Popular'. Use ShadCN cards, badges, and check icons. The aesthetic should be clean and professional."  
* **Advantage:** v0 renders the UI instantly, allowing for rapid visual feedback that a text-based coding agent cannot provide.23

#### **Phase 2: The Export Protocol**

Once the design is finalized in v0, the code must be transported into the local development environment. Blind copy-pasting is a source of errors, as it may miss dependencies or configuration nuances.

* **The npx Bridge:** Utilize the npx v0 add \<component-id\> command in the local terminal.25  
* **Automatic Reconciliation:** The npx command detects the local project configuration (e.g., CSS variables vs. utility classes, TypeScript strictness). It transforms the v0 code to match the project's standards automatically, installing any missing Radix primitives (e.g., Accordion, Dialog) that the new component relies on.27

#### **Phase 3: Architectural Integration (Cursor)**

Open the newly added file in Cursor. The agent's role now shifts from "creator" to "integrator."

* **The Integration Prompt:** "I have added pricing-section.tsx via v0. Refactor it to use our project's existing SectionWrapper component for margins. Ensure the typography matches our h2 and p variants defined in typography.tsx. Wire the 'Subscribe' buttons to the handleSubscription server action.".28

This workflow leverages the strengths of each tool: v0 for visual creativity and boilerplate generation, and Cursor/Claude for rigorous architectural integration and business logic implementation.30

## ---

**5\. Automated Governance and Quality Assurance**

Even with strict protocols and optimized infrastructure, entropy (drift) is inevitable over the lifecycle of a software project. To maintain a "State-of-the-Art" codebase, we must implement automated governance systems that police the agent's output.

### **5.1 Visual Regression Testing: The Hard Gate**

To catch "visual slop"—such as a button misaligned by 2 pixels due to an agent arbitrarily changing a class—visual regression testing is essential. This turns UI consistency from a subjective human opinion into a binary test result.

**The Playwright MCP Implementation:**

1. **Prompting the Test:** "Create a visual regression test for the landing page using Playwright. Take a snapshot of the Hero section and compare it to the baseline hero-snapshot.png.".31  
2. **Execution via Agent:** The Playwright MCP runs this test. If the agent's recent change caused a layout shift, the test fails.  
3. **The Feedback Loop:** The agent is fed the failure report. "The test failed with a 5% pixel difference. Analyze the layout shift."  
4. **Self-Healing:** The "Healer" agent (a concept within the Playwright ecosystem) can attempt to adjust the CSS to resolve the regression, checking its work against the snapshot until the test passes.32

**Table 3: Playwright MCP Actions for Visual QA**

| Action | Description | Usage in Agent Workflow |
| :---- | :---- | :---- |
| page.screenshot() | Captures pixel state of a component. | Used to establish baselines for new UI features. 35 |
| expect(page).toHaveScreenshot() | Asserts visual fidelity. | The primary gate for detecting "style drift." 36 |
| page.accessibility.snapshot() | Captures the A11y tree. | Ensures AI changes don't break screen readers. 37 |

### **5.2 Architectural Decision Records (ADRs) as "Long-Term Memory"**

AI agents lack historical context on *why* a decision was made. Why did we choose nuqs for URL state management instead of standard useSearchParams? Without this context, an agent might suggest refactoring the code back to the standard pattern, reintroducing the problems we solved.

**The Automated ADR Workflow:**

1. **Trigger:** When a significant architectural change is requested (e.g., "Switch form validation to Zod").  
2. **Agent Task:** "Generate an ADR for this change. Document the context, the decision, the consequences, and the alternatives considered.".38  
3. **Storage:** Save this record as docs/adr/001-zod-validation.md.39  
4. **Context Injection:** Update the .cursorrules or CLAUDE.md to reference the docs/adr directory. "Refer to the active ADRs in docs/adr before proposing architectural changes."  
5. **Result:** The agent "reads" the ADRs as part of its research phase. It learns: "I cannot use Yup for validation; this project mandates Zod per ADR-001." This creates a persistent institutional memory that guides the AI.40

## ---

**6\. Future Outlook: The Evolution of "Vibe Coding"**

The methodologies described in this report represent the transition from "Vibe Coding"—the loose, prompt-driven generation of software—to "Systems Engineering with AI." As agents become more capable, the role of the developer will continue to abstract upwards. We are moving toward a future where the codebase itself is a dynamic entity, continuously gardened by agents operating under strict constitutional constraints.

The "State-of-the-Art" in 2026 is not defined by the raw intelligence of the model, but by the sophistication of the harness that surrounds it. By implementing **MCP servers** to ground the agent in reality, enforcing **strict protocols** (R-C-P-R-B) to discipline its execution, and utilizing **governance tools** (ADRs, Visual Testing) to police its output, we transform these stochastic models into deterministic engines of production. The result is a Next.js application that leverages the exponential speed of AI without sacrificing the architectural integrity, design consistency, and maintainability that define professional software engineering.

## ---

**7\. Appendices: Technical Configurations**

### **Appendix A: Optimized .cursorrules Template for Next.js/ShadCN**

# **Project Behavior Rules**

## **Stack Definitions**

* **Framework**: Next.js 15 (App Router)  
* **Language**: TypeScript (Strict Mode)  
* **Styling**: TailwindCSS v4 (Utility-first)  
* **UI Library**: ShadCN UI (Radix Primitives)  
* **Icons**: Lucide React

## **UI & Styling Guidelines**

* **Component Sourcing**:  
  * BEFORE creating a new UI element, ALWAYS check components/ui via MCP or file search.  
  * If a primitive exists, use it. Do not reimplement functionality.  
* **Tailwind Usage**:  
  * Use cn() for class merging.  
  * Adhere to mobile-first design (e.g., flex-col md:flex-row).  
  * Use semantic colors (bg-muted) over hex codes (\#f3f4f6).  
* **Anti-Patterns**:  
  * NO @apply in CSS files.  
  * NO default export for components; use named exports.  
  * NO "magic numbers" for spacing; use Tailwind spacing scale.

## **Architecture Constraints**

* **Server Components**:  
  * Default to Server Components (RSC).  
  * Use 'use client' ONLY for interactive leaves (forms, buttons with hooks).  
* **Data Fetching**:  
  * Use Server Actions for mutations.  
  * Use Suspense boundaries for async data loading.

## **Workflow Protocol**

1. **Research**: Identify relevant files and existing components.  
2. **Clarify**: Ask questions if requirements are ambiguous.  
3. **Plan**: Outline the implementation steps before writing code.  
4. **Build**: Generate code matching the plan.  
   13

### **Appendix B: Playwright Visual Regression Test Prompt**

"Create a Playwright test file tests/visual/landing-page.spec.ts.

The test should:

1. Navigate to the / route.  
2. Wait for the Hero component to be visible.  
3. Take a screenshot of the entire page: await expect(page).toHaveScreenshot('landing-page.png', { fullPage: true });.  
4. Ensure the viewport is set to 1280x720.  
   Run this test and report any visual regressions."  
   31

#### **Works cited**

1. AI Slop Code: AI is hiding incompetence that used to be obvious : r/cscareerquestions, accessed January 25, 2026, [https://www.reddit.com/r/cscareerquestions/comments/1oa5nx7/ai\_slop\_code\_ai\_is\_hiding\_incompetence\_that\_used/](https://www.reddit.com/r/cscareerquestions/comments/1oa5nx7/ai_slop_code_ai_is_hiding_incompetence_that_used/)  
2. How to use AI to build accurate ShadCN components \- LogRocket ..., accessed January 25, 2026, [https://blog.logrocket.com/ai-shadcn-components/](https://blog.logrocket.com/ai-shadcn-components/)  
3. How can we configure the cursor AI code agent using the best ..., accessed January 25, 2026, [https://medium.com/@vaibhavhpatil/how-to-effectively-we-can-configure-cursor-ai-code-agent-using-agent-best-practices-b9fd2e6b0ed8](https://medium.com/@vaibhavhpatil/how-to-effectively-we-can-configure-cursor-ai-code-agent-using-agent-best-practices-b9fd2e6b0ed8)  
4. How I Built an App with Cursor AI Agent for the First Time (the Good, the Bad, and the Drama) \- DEV Community, accessed January 25, 2026, [https://dev.to/katya\_pavlopoulos/how-i-built-an-app-with-cursor-ai-agent-for-the-first-time-the-good-the-bad-and-the-drama-168o](https://dev.to/katya_pavlopoulos/how-i-built-an-app-with-cursor-ai-agent-for-the-first-time-the-good-the-bad-and-the-drama-168o)  
5. How To Vibe Code Beautiful Front Ends: No More AI Slop \- YouTube, accessed January 25, 2026, [https://www.youtube.com/watch?v=XI8JtpWza74](https://www.youtube.com/watch?v=XI8JtpWza74)  
6. After building 10+ projects with AI, here's how to actually design great looking UIs fast : r/cursor \- Reddit, accessed January 25, 2026, [https://www.reddit.com/r/cursor/comments/1mf7o47/after\_building\_10\_projects\_with\_ai\_heres\_how\_to/](https://www.reddit.com/r/cursor/comments/1mf7o47/after_building_10_projects_with_ai_heres_how_to/)  
7. MCP Server \- Shadcn UI, accessed January 25, 2026, [https://ui.shadcn.com/docs/registry/mcp](https://ui.shadcn.com/docs/registry/mcp)  
8. Tailwind (shadcn/ui Integration) | Cursor Rules Guide | cursorrules, accessed January 25, 2026, [https://cursorrules.org/article/tailwind-shadcn-ui-integration-cursorrules-prompt-](https://cursorrules.org/article/tailwind-shadcn-ui-integration-cursorrules-prompt-)  
9. Testing with Playwright and Claude Code \- nikiforovall.blog, accessed January 25, 2026, [https://nikiforovall.blog/ai/2025/09/06/playwright-claude-code-testing.html](https://nikiforovall.blog/ai/2025/09/06/playwright-claude-code-testing.html)  
10. Using Playwright MCP with Claude Code \- Simon Willison: TIL, accessed January 25, 2026, [https://til.simonwillison.net/claude-code/playwright-mcp-claude-code](https://til.simonwillison.net/claude-code/playwright-mcp-claude-code)  
11. AI Visual Debugging: Fix Sites with Playwright MCP \- YouTube, accessed January 25, 2026, [https://www.youtube.com/watch?v=SW\_Z9gOvMNQ](https://www.youtube.com/watch?v=SW_Z9gOvMNQ)  
12. Cursor AI: 5 Advanced Features You're Not Using \- Builder.io, accessed January 25, 2026, [https://www.builder.io/blog/cursor-advanced-features](https://www.builder.io/blog/cursor-advanced-features)  
13. The ultimate .cursorrules for TypeScript, React 19, Next.js 15, Vercel AI SDK, Shadcn UI, Radix UI, and Tailwind CSS : r/cursor \- Reddit, accessed January 25, 2026, [https://www.reddit.com/r/cursor/comments/1gjd96h/the\_ultimate\_cursorrules\_for\_typescript\_react\_19/](https://www.reddit.com/r/cursor/comments/1gjd96h/the_ultimate_cursorrules_for_typescript_react_19/)  
14. awesome-cursorrules/rules/typescript-shadcn-ui-nextjs-cursorrules-prompt-fil/.cursorrules at main · PatrickJS/awesome-cursorrules \- GitHub, accessed January 25, 2026, [https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-shadcn-ui-nextjs-cursorrules-prompt-fil/.cursorrules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/typescript-shadcn-ui-nextjs-cursorrules-prompt-fil/.cursorrules)  
15. Next.js React Standard.js Cursor Rules rule by ... \- Cursor Directory, accessed January 25, 2026, [https://cursor.directory/nextjs-react-vite-javascript-cursor-rules](https://cursor.directory/nextjs-react-vite-javascript-cursor-rules)  
16. awesome-cursorrules/rules/nextjs-react-typescript-cursorrules-prompt-file/.cursorrules at main · PatrickJS/awesome-cursorrules \- GitHub, accessed January 25, 2026, [https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-react-typescript-cursorrules-prompt-file/.cursorrules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs-react-typescript-cursorrules-prompt-file/.cursorrules)  
17. CLAUDE.md – Next.js \+ TypeScript \+ Tailwind \+ shadcn \+ React ..., accessed January 25, 2026, [https://gist.github.com/gregsantos/2fc7d7551631b809efa18a0bc4debd2a](https://gist.github.com/gregsantos/2fc7d7551631b809efa18a0bc4debd2a)  
18. AI Coding Prompts \- shadcn.io, accessed January 25, 2026, [https://www.shadcn.io/prompts](https://www.shadcn.io/prompts)  
19. Docs \- shadcn/studio MCP Server, accessed January 25, 2026, [https://shadcnstudio.com/docs/getting-started/shadcn-studio-mcp-server](https://shadcnstudio.com/docs/getting-started/shadcn-studio-mcp-server)  
20. Creating the Perfect CLAUDE.md for Claude Code \- Dometrain, accessed January 25, 2026, [https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/](https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/)  
21. claude-visual-style-guide/CLAUDE.md at main \- GitHub, accessed January 25, 2026, [https://github.com/jcmrs/claude-visual-style-guide/blob/main/CLAUDE.md](https://github.com/jcmrs/claude-visual-style-guide/blob/main/CLAUDE.md)  
22. Best practices for coding with agents · Cursor, accessed January 25, 2026, [https://cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices)  
23. Building Faster with V0 and Claude Code: Lessons Learned from Vibe Coding \- Strapi, accessed January 25, 2026, [https://strapi.io/blog/building-faster-with-v0-and-claude-code-lessons-learned-from-vibe-coding](https://strapi.io/blog/building-faster-with-v0-and-claude-code-lessons-learned-from-vibe-coding)  
24. How to Export v0 Projects to Cursor Like a PRO\! \- YouTube, accessed January 25, 2026, [https://www.youtube.com/watch?v=SwEWAGMU0\_0](https://www.youtube.com/watch?v=SwEWAGMU0_0)  
25. Become a v0 expert \- Vercel Community, accessed January 25, 2026, [https://community.vercel.com/t/become-a-v0-expert/5981](https://community.vercel.com/t/become-a-v0-expert/5981)  
26. Why is running v0.dev projects locally so hard? : r/nextjs \- Reddit, accessed January 25, 2026, [https://www.reddit.com/r/nextjs/comments/1izsaie/why\_is\_running\_v0dev\_projects\_locally\_so\_hard/](https://www.reddit.com/r/nextjs/comments/1izsaie/why_is_running_v0dev_projects_locally_so_hard/)  
27. v0 by Vercel: A Guide With Demo Project \- DataCamp, accessed January 25, 2026, [https://www.datacamp.com/tutorial/vercel-v0](https://www.datacamp.com/tutorial/vercel-v0)  
28. How to Integrate V0.dev with Cursor: A Complete Guide \- Bitcot, accessed January 25, 2026, [https://www.bitcot.com/how-to-integrate-v0-dev-with-cursor-a-complete-guide/](https://www.bitcot.com/how-to-integrate-v0-dev-with-cursor-a-complete-guide/)  
29. v0 to Cursor? : r/vercel \- Reddit, accessed January 25, 2026, [https://www.reddit.com/r/vercel/comments/1i4g3vb/v0\_to\_cursor/](https://www.reddit.com/r/vercel/comments/1i4g3vb/v0_to_cursor/)  
30. Build a Production Ready Trip Planner in 6 hours: Rapid App Development with Claude, ClaudeCode, and V0.dev | by Chanchai Lee \- Medium, accessed January 25, 2026, [https://medium.com/@leechanchai/build-a-trip-planner-in-a-weekend-rapid-app-development-with-claude-claudecode-and-v0-dev-aa5080570c5d](https://medium.com/@leechanchai/build-a-trip-planner-in-a-weekend-rapid-app-development-with-claude-claudecode-and-v0-dev-aa5080570c5d)  
31. Automating Visual Regression Checks with Playwright MCP \- TestDino, accessed January 25, 2026, [https://testdino.com/blog/playwright-mcp-visual-regression/](https://testdino.com/blog/playwright-mcp-visual-regression/)  
32. Playwright Test Agents, accessed January 25, 2026, [https://playwright.dev/docs/test-agents](https://playwright.dev/docs/test-agents)  
33. Playwright MCP \+ Claude: The Future of AI Visual Testing \- YouTube, accessed January 25, 2026, [https://www.youtube.com/watch?v=ey\_z3iPIjnc](https://www.youtube.com/watch?v=ey_z3iPIjnc)  
34. Visual Regression Testing with Playwright \- DEV Community, accessed January 25, 2026, [https://dev.to/nishikr/visual-regression-testing-with-playwright-42ff](https://dev.to/nishikr/visual-regression-testing-with-playwright-42ff)  
35. How to Perform Visual Regression Testing Using Playwright \- BrowserStack, accessed January 25, 2026, [https://www.browserstack.com/guide/visual-regression-testing-using-playwright](https://www.browserstack.com/guide/visual-regression-testing-using-playwright)  
36. Visual Regression Testing with Playwright: Catch UI Bugs Before Release \- YouTube, accessed January 25, 2026, [https://www.youtube.com/watch?v=n\_SCVtvAf8M](https://www.youtube.com/watch?v=n_SCVtvAf8M)  
37. microsoft/playwright-mcp: Playwright MCP server \- GitHub, accessed January 25, 2026, [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)  
38. AI generated Architecture Decision Records (ADR) \- Dennis Adolfi, accessed January 25, 2026, [https://adolfi.dev/blog/ai-generated-adr/](https://adolfi.dev/blog/ai-generated-adr/)  
39. About MADR \- Architectural Decision Records, accessed January 25, 2026, [https://adr.github.io/madr/](https://adr.github.io/madr/)  
40. Using AI Agents to Enforce Architectural Standards | by Dave Patten | Medium, accessed January 25, 2026, [https://medium.com/@dave-patten/using-ai-agents-to-enforce-architectural-standards-41d58af235a0](https://medium.com/@dave-patten/using-ai-agents-to-enforce-architectural-standards-41d58af235a0)  
41. ADR process \- AWS Prescriptive Guidance, accessed January 25, 2026, [https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)  
42. awesome-cursorrules/rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file/.cursorrules at main · PatrickJS/awesome-cursorrules \- GitHub, accessed January 25, 2026, [https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file/.cursorrules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file/.cursorrules)