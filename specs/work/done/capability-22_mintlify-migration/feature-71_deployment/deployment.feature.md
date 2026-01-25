# Feature: Deployment & Custom Domain

## Observable Outcome

prompts.ag is live on Mintlify with custom domain, serving all content with `.md` endpoints, `llms.txt`, and contextual menu features.

## Testing Strategy

> Features require **Level 1 + Level 2** to prove the feature works with real tools.

### Level Assignment

| Component              | Level | Justification                       |
| ---------------------- | ----- | ----------------------------------- |
| Local `mint dev` works | 2     | Needs real Mintlify CLI             |
| Dashboard connection   | N/A   | Human action via Mintlify dashboard |
| Custom domain config   | N/A   | Human action via DNS and dashboard  |
| Live site verification | 3     | E2E test against production         |

### Escalation Rationale

- **2 → 3**: Local development working doesn't prove production deployment works

## Feature Integration Tests (Level 2)

### FI1: Local development serves all pages

```bash
# Start local server
cd docs/ && mint dev --port 3333 &
sleep 5

# Verify all pages serve
for page in "" guidelines format approach tooling changelog; do
  curl -sf "http://localhost:3333/$page" > /dev/null || exit 1
done

kill %1
```

## Deployment Steps

### Story 1: Local Testing

- Run `mint dev` locally
- Verify all pages render
- Verify navigation works
- Verify code blocks have syntax highlighting

### Story 2: Connect Mintlify (Human Action)

1. Go to https://dashboard.mintlify.com
2. Connect GitHub account
3. Select prompts.ag repository (or docs subdirectory)
4. Install GitHub App for automatic deployments
5. Verify preview deployment works

### Story 3: Configure Custom Domain (Human Action)

1. In Mintlify dashboard → Settings → Custom Domain
2. Add `prompts.ag`
3. Get DNS configuration (CNAME or A record)
4. Update DNS records at domain registrar
5. Wait for SSL provisioning
6. Verify site accessible at https://prompts.ag

## Capability Contribution

This feature is the final step - making the migrated site live. It depends on:

- feature-21 (OSS approval) for dashboard access
- feature-37 (docs structure) for deployable content
- feature-54 (content conversion) for complete content

## Completion Criteria

- [ ] `mint dev` serves site locally without errors
- [ ] Repository connected to Mintlify dashboard
- [ ] Preview deployment successful
- [ ] Custom domain configured
- [ ] DNS propagated
- [ ] SSL certificate active
- [ ] Site live at https://prompts.ag
