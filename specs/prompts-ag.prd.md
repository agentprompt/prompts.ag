# PRD: Agent Prompt — The Living Reference for Structured Prompts

> **Purpose**: Defines the product vision for prompts.ag, the authoritative reference for structured prompt formats that synthesizes guidance from frontier AI labs.

## Product Vision

### User Problem

**Who** are we building for?

Developers, prompt engineers, and AI practitioners who write prompts for frontier AI models (Claude, GPT, Gemini) and want to follow best practices but face conflicting, evolving, and scattered guidance.

**What** problem do they face?

```
As a prompt author, I am frustrated by uncertainty about prompt structure
because Anthropic, OpenAI, and Google each publish different guidance that evolves over time,
which prevents me from writing prompts with confidence.
```

### Current Customer Pain

- **Symptom**: Authors guess at format conventions, copy patterns from outdated blog posts, or spend hours researching each lab's latest recommendations
- **Root Cause**: No single source synthesizes and maintains current guidance from all frontier labs. Each lab's documentation lives in different places, uses different terminology, and updates independently
- **Customer Impact**: Wasted time researching, inconsistent prompt quality, anxiety about whether prompts follow best practices
- **Business Impact**: The entire AI ecosystem suffers from fragmented knowledge; prompt engineering remains more art than craft

### Customer Solution

```
Implement a living reference website that enables prompt authors to learn current best practices
through synthesized, lab-sourced guidance, resulting in confident, well-structured prompts.
```

### Customer Journey Context

- **Before**: Authors search multiple documentation sites, cross-reference blog posts, ask in forums, and still feel uncertain about whether their prompt structure is optimal
- **During**: Authors discover prompts.ag, scan the synthesized guidelines, see concrete examples, and understand where labs agree vs. differ
- **After**: Authors write prompts confidently using the `.ag` format, return to check for updates when labs release new guidance, and share the reference with colleagues

### User Assumptions

| Assumption Category  | Specific Assumption                           | Impact on Product Design                                 |
| -------------------- | --------------------------------------------- | -------------------------------------------------------- |
| Technical Capability | Users understand XML-like syntax and Markdown | Can present format without extensive tutorials           |
| User Context         | Users work with multiple AI providers         | Must synthesize across labs, not just one                |
| User Goals           | Users want confidence, not perfection         | Focus on "what labs recommend" over "optimal benchmarks" |

## Expected Outcome

### Measurable Outcome

```
Prompt authors will adopt prompts.ag as their go-to reference for structured prompt formats,
leading to recognition as the authoritative source for prompt structure guidance,
proven by organic traffic growth, return visits, and community citations.
```

### Evidence of Success

| Metric                | Current | Target                                         | Improvement                           |
| --------------------- | ------- | ---------------------------------------------- | ------------------------------------- |
| Authority Recognition | None    | Referenced in AI tooling docs and tutorials    | Recognized as the standard reference  |
| Return Visitors       | 0%      | Meaningful return rate                         | Users come back when guidance updates |
| Community Citations   | None    | Cited in prompt engineering discussions        | Organic recommendations               |
| Content Currency      | N/A     | Updated within 2 weeks of lab guidance changes | Maintains "living document" promise   |

## Scope Definition

### What's Included

- Synthesized guidelines from Anthropic, OpenAI, and Google documentation
- The `.ag` format specification (pseudo-XML + Markdown)
- Concrete code examples demonstrating the format
- Clear explanation of project methodology (why we don't benchmark)
- Links to authoritative source documentation from each lab
- Tooling roadmap (syntax highlighting, validation, LSP)

### What's Explicitly Excluded

| Excluded Capability             | Rationale                                              |
| ------------------------------- | ------------------------------------------------------ |
| Prompt templates/library        | Different product; we document format, not content     |
| Benchmarking/performance claims | Conflicts with "enduring guidance" philosophy          |
| User accounts/personalization   | Adds complexity without clear value for reference site |
| Comment system/forums           | Community should happen on GitHub, not fragmented      |

### Scope Boundaries Rationale

This product is a **reference**, not a tool or community platform. We document what agents want so authors can write with confidence. Anything that doesn't serve that reference function is out of scope. Tools come after documentation is solid.

## Product Approach

### Interaction Model

- **Interface Type**: Static website with anchor-based navigation
- **Invocation Pattern**: Direct URL access, search engine discovery, peer referrals
- **User Mental Model**: "Like MDN Web Docs but for AI prompt structure"

### User Experience Principles

1. **Scannable**: Users should find relevant guidance within 30 seconds
2. **Authoritative**: Every claim links to lab source documentation
3. **Current**: Content reflects latest lab guidance, with visible update dates
4. **Neutral**: Present lab recommendations without editorializing

### High-Level Technical Approach

**Content Model:**

- Single-page scrollable design with anchor sections
- Lab-sourced guidelines with direct citation links
- Code examples with copy-to-clipboard functionality

**Key Capabilities:**

- Present synthesized guidelines across Anthropic, OpenAI, Google
- Show format specification with concrete examples
- Explain methodology (why guidance-based, not benchmark-based)
- Link to tooling roadmap

**Technology:**

- Next.js static site for fast loading and SEO
- Tailwind CSS for clean, minimal design
- GitHub-based updates for transparency

### Product-Specific Constraints

| Constraint                | Impact on Product                            | Impact on Testing            |
| ------------------------- | -------------------------------------------- | ---------------------------- |
| Must cite sources         | Every guideline needs lab documentation link | Verify all links are valid   |
| Labs update independently | Content may become stale                     | Monitor lab docs for changes |

## Success Criteria

### User Outcomes

| Outcome                     | Success Indicator                                        |
| --------------------------- | -------------------------------------------------------- |
| Users find guidance quickly | Time-to-answer under 60 seconds for common questions     |
| Users trust the content     | Users cite prompts.ag when sharing prompt advice         |
| Users return for updates    | Meaningful return visitor rate when labs update guidance |

### Quality Attributes

| Attribute       | Target                                | Measurement Approach                    |
| --------------- | ------------------------------------- | --------------------------------------- |
| **Accuracy**    | 100% alignment with lab documentation | Manual verification against source docs |
| **Currency**    | Updated within 2 weeks of lab changes | Track lab doc update dates              |
| **Clarity**     | No ambiguous guidance                 | User feedback, GitHub issues            |
| **Performance** | Sub-2s page load                      | Lighthouse metrics                      |

### Definition of "Done"

1. Site presents synthesized guidance from all three frontier labs
2. Every guideline links to authoritative source documentation
3. Format specification is clear with concrete examples
4. Methodology section explains guidance-based approach
5. Site loads fast and works well on mobile
6. Content can be updated easily when labs change guidance

## Open Decisions

### Questions Requiring User Input

None identified — product vision is clear.

### Decisions Triggering ADRs

| Decision Topic     | Key Question                                | Options to Evaluate                       |
| ------------------ | ------------------------------------------- | ----------------------------------------- |
| Update monitoring  | How to track when labs update docs?         | Manual checks / RSS / Automated scraping  |
| Content versioning | How to handle breaking changes in guidance? | Changelog / Version archive / Just update |

### Product Trade-offs

| Trade-off         | Option A            | Option B                    | Impact                           |
| ----------------- | ------------------- | --------------------------- | -------------------------------- |
| Depth vs. Breadth | Deep per-lab pages  | Synthesized overview        | A = comprehensive, B = scannable |
| Tools vs. Docs    | Build tooling early | Document first, tools later | A = useful, B = focused          |

## Dependencies

### Technical Dependencies

| Dependency        | Version/Constraint | Purpose               | Availability       |
| ----------------- | ------------------ | --------------------- | ------------------ |
| Next.js           | >=15.0             | Static site framework | Available          |
| Lab documentation | Current            | Source material       | Published publicly |

### Performance Requirements

| Requirement Area | Target                                          | Measurement Approach         |
| ---------------- | ----------------------------------------------- | ---------------------------- |
| Page Load        | Sub-2s on 3G                                    | Lighthouse performance score |
| SEO              | Indexed for "prompt engineering format" queries | Search console monitoring    |

## Pre-Mortem Analysis

### Assumption: Labs will continue publishing prompt guidance

- **Likelihood**: Low risk — all three labs actively maintain prompt engineering docs
- **Impact**: High — without source material, product has no value
- **Mitigation**: Archive current guidance; diversify to include community-validated patterns if labs stop publishing

### Assumption: Users will trust a third-party synthesis over going to source

- **Likelihood**: Medium — depends on perceived authority and accuracy
- **Impact**: High — if users don't trust us, they won't return
- **Mitigation**: Always link to sources; be transparent about methodology; encourage verification

### Assumption: The XML+Markdown format will remain the preferred structure

- **Likelihood**: Medium — format has been stable but could shift with new model architectures
- **Impact**: Medium — would require significant content updates
- **Mitigation**: Monitor lab guidance closely; be prepared to document format evolution

### Assumption: Single-page design scales to comprehensive content

- **Likelihood**: Medium — works now but may become unwieldy with deep per-lab content
- **Impact**: Low — can add pages later without breaking existing links
- **Mitigation**: Design navigation to support future multi-page expansion
