# Story: Verify Local Development

## Functional Requirements

### FR1: Install Mintlify CLI

```gherkin
GIVEN a developer machine with Node.js
WHEN setting up local development
THEN Mintlify CLI is installed and available
```

#### Files created/modified

1. `package.json` [modify]: Add `mint` to devDependencies (optional)

### FR2: Run mint dev successfully

```gherkin
GIVEN docs/ directory with valid configuration
WHEN running mint dev
THEN local server starts without errors on port 3333
```

#### Files created/modified

None - verification only

### FR3: Verify all pages accessible

```gherkin
GIVEN mint dev is running
WHEN accessing each page defined in navigation
THEN all pages return 200 status and render content
```

#### Files created/modified

None - verification only

## Testing Strategy

> Stories require **Level 1** to prove core logic works.
> However, this story is primarily **Level 2** verification.

### Level Assignment

| Component              | Level | Justification              |
| ---------------------- | ----- | -------------------------- |
| CLI installation check | 1     | Command existence check    |
| Server startup         | 2     | Requires real Mintlify CLI |
| Page accessibility     | 2     | Requires running server    |

### When to Escalate

This story requires Level 2 because:

- The primary purpose is verifying Mintlify CLI works
- Cannot be tested without the real binary
- This is integration testing by definition

## Unit Tests (Level 1)

```typescript
// specs/.../story-21_verify-local/tests/verify-local.test.ts
import { execSync } from "child_process";
import { describe, expect, it } from "vitest";

describe("Story: Verify Local Development", () => {
  it("GIVEN developer environment WHEN checking mint CLI THEN command exists", () => {
    // This test verifies mint is installed
    // Skip if not installed (CI may not have it)
    try {
      const result = execSync("which mint || command -v mint", {
        encoding: "utf-8",
      });
      expect(result.trim()).toBeTruthy();
    } catch {
      // CLI not installed - skip test
      console.log("Mintlify CLI not installed - skipping");
    }
  });
});
```

## Integration Tests (Level 2)

These tests run at the **feature level** (`feature-71_deployment/tests/`):

```bash
# feature-71_deployment/tests/deployment.integration.test.sh

#!/bin/bash
set -e

# Start mint dev in background
cd docs
mint dev --port 3333 &
MINT_PID=$!

# Wait for server to start
sleep 10

# Test all pages
for page in "" "guidelines" "format" "approach" "tooling" "changelog"; do
  echo "Testing /$page..."
  curl -sf "http://localhost:3333/$page" > /dev/null || {
    echo "FAIL: /$page not accessible"
    kill $MINT_PID 2>/dev/null
    exit 1
  }
done

echo "All pages accessible"
kill $MINT_PID 2>/dev/null
exit 0
```

## Architectural Requirements

### Relevant ADRs

None at this level.

## Quality Requirements

### QR1: Server Stability

**Requirement:** mint dev must start without errors
**Target:** Clean startup, no warnings
**Validation:** Process exit code and stdout

### QR2: Page Accessibility

**Requirement:** All navigation pages must be accessible
**Target:** 100% of pages return 200
**Validation:** HTTP status checks

## Completion Criteria

- [ ] Mintlify CLI installed (globally or via npx)
- [ ] `mint dev` starts successfully in docs/ directory
- [ ] All 6 pages accessible via localhost
- [ ] Navigation works between pages
- [ ] No console errors during page loads

## Documentation

Add to README.md:

````markdown
## Local Development

```bash
# Install Mintlify CLI
npm i -g mint

# Start local server
cd docs && mint dev

# View at http://localhost:3333
```
````

```
```
