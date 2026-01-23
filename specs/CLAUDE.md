# specs/ Directory Guide

## Critical Commands

```bash
# See full hierarchy with status
spx spec status

# Find next work item (respects BSP ordering)
spx spec next

# Session management
spx session list          # See available handoffs
spx session pickup [id]   # Claim a session
```

**Use these commands. Do NOT manually navigate or calculate BSP ordering.**

---

## Before Implementing ANY Work Item

**⛔ BLOCKING: Invoke `/understanding-specs <path>` BEFORE writing code.**

```text
User: "Implement story-21_add-raw-method"
→ Run: spx spec next                    # Get the path
→ Invoke: /understanding-specs <path>   # Load context hierarchy (pass the path!)
→ THEN proceed with implementation
```

Example:

```bash
/understanding-specs specs/work/doing/capability-21_core-hdl-framework/feature-21_signal-types/story-21_add-raw-method
```

**Why mandatory**: Loads PRD/TRD → ADRs → work item context. Without it, you'll miss requirements and violate ADRs.

---

## When Creating Specs (PRDs, TRDs, ADRs)

**⛔ BLOCKING: Invoke `/managing-specs` BEFORE creating spec documents.**

Templates live in the skill directory, NOT in this project. Do NOT search for templates - invoke the skill.

---

## Status Rules

Status is determined by the `tests/` directory at each level:

| Directory State                    | Status      |
| ---------------------------------- | ----------- |
| Missing or empty `tests/`          | OPEN        |
| Has `*.test.*` files, no `DONE.md` | IN_PROGRESS |
| Has `DONE.md`                      | DONE        |

**HIERARCHY trumps NUMBER:** There can be multiple stories with the same number in different features and capabilities.
**BSP Ordering:** Lower number = must complete FIRST. Work on item N only after ALL items < N are DONE.

---

## TDD Workflow: Progress → Graduation

Tests exist in ONE location only. Never duplicate.

```
specs/.../story-XX/tests/    ← Progress tests (write here)
        ↓
    /reviewing-python        ← Skill `reviewing-[language]`  graduates tests — never graduate tests manually
        ↓
tests/unit/                  ← Regression tests (MUST always pass)
```

**NEVER write tests directly in `tests/`** - this breaks CI until implementation is complete.

---

## Quick Reference

| Task                         | Command/Skill                 |
| ---------------------------- | ----------------------------- |
| What's the project status?   | `spx spec status`             |
| What should I work on next?  | `spx spec next`               |
| Load context for work item   | `/understanding-specs <path>` |
| Create PRD/TRD/ADR           | `/managing-specs`             |
| Find BSP number for new item | `/managing-specs`             |
| List available sessions      | `spx session list`            |
| Claim a handoff              | `spx session pickup`          |

---

## Session Management

Sessions are stored in `.spx/sessions/`:

```
.spx/sessions/
├── todo/     # Available for pickup
└── doing/    # Currently claimed
```

Use `/handoff` to create, `/pickup` to claim.
