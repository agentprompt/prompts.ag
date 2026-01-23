# Feature: OSS Program Application

## Observable Outcome

Mintlify OSS program approval received, enabling free Pro tier access ($300/month value) for prompts.ag documentation hosting.

## Testing Strategy

> This feature has no automated tests - it's a human action with external dependency.

### Level Assignment

| Component              | Level | Justification                 |
| ---------------------- | ----- | ----------------------------- |
| Application submission | N/A   | Human action, external system |
| Approval verification  | N/A   | Email/dashboard confirmation  |

### Escalation Rationale

- **No escalation**: This is a blocking external dependency, not code

## Prerequisites

- [ ] Verify prompts.ag repo is public
- [ ] Verify MIT license is present
- [ ] Prepare project description for application

## Application Steps

1. Go to https://mintlify.typeform.com/oss-program
2. Fill in project details:
   - **Project name**: prompts.ag
   - **Repository**: https://github.com/agentprompt/prompts.ag
   - **License**: MIT
   - **Description**: Living reference for structured prompt formats, tracking what frontier AI agents want
3. Submit application
4. Wait for approval email

## Eligibility Criteria (prompts.ag qualifies)

- Open source with recognized license (MIT ✓)
- Not venture-backed or revenue-funded ✓
- Not owned by a for-profit company ✓

## Capability Contribution

This feature is a **blocking dependency** for all other features. Without OSS program approval:

- No Mintlify dashboard access
- No deployment capability
- No custom domain configuration

## Completion Criteria

- [ ] Application submitted
- [ ] Approval received (email or dashboard access)
- [ ] Pro tier features confirmed available
