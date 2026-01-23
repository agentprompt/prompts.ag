# Feature: Documentation Repository Setup

## Observable Outcome

A `docs/` directory exists with valid Mintlify configuration (`docs.json`) and MDX file stubs, ready for content conversion.

## Testing Strategy

> Features require **Level 1 + Level 2** to prove the feature works with real tools.

### Level Assignment

| Component         | Level | Justification                           |
| ----------------- | ----- | --------------------------------------- |
| docs.json schema  | 1     | JSON validation against Mintlify schema |
| MDX file presence | 1     | File existence check                    |
| `mint dev` serves | 2     | Needs real Mintlify CLI to verify       |

### Escalation Rationale

- **1 → 2**: Valid JSON and file structure doesn't prove Mintlify accepts the configuration

## Feature Integration Tests (Level 2)

### FI1: Mintlify CLI accepts configuration

```bash
# tests/integration/docs-structure.integration.test.sh
cd docs/ && mint dev --port 3333 &
sleep 5
curl -s http://localhost:3333 | grep -q "prompts.ag"
kill %1
```

### FI2: All navigation pages resolve

```bash
# Verify all pages in navigation are accessible
for page in index guidelines format approach tooling changelog; do
  curl -sf http://localhost:3333/$page || exit 1
done
```

## Capability Contribution

This feature creates the foundation for content conversion. It must complete before any TSX→MDX conversion begins because:

- docs.json defines site structure and navigation
- MDX stubs establish file naming conventions
- Local development environment enables iterative testing

## Completion Criteria

- [ ] `docs/` directory created
- [ ] `docs.json` validates against Mintlify schema
- [ ] All MDX stubs created (index, guidelines, format, approach, tooling, changelog)
- [ ] `mint dev` serves site without errors
- [ ] Navigation renders correctly
