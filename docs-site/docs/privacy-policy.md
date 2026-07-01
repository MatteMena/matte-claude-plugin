---
id: privacy-policy
title: Privacy Policy
sidebar_position: 11
---

# Privacy Policy — MatteMena Connector

*Last updated: 2026-06-30*

This page covers the privacy policy for the **MatteMena Connector** — the MCP server / Claude plugin that connects Claude to your advertising accounts on Meta, TikTok, Google Ads, Google Analytics (GA4), Snapchat Ads, Google Sheets, and HubSpot.

For the full MatteMena Nerve website privacy policy, see [nerve.mattemena.com/privacy-policy](https://nerve.mattemena.com/privacy-policy).

---

## Data Collected by the Connector

| Category | Examples | Purpose |
|----------|---------|---------|
| **Authentication credentials** | OAuth access tokens, refresh tokens | Authenticate requests to advertising platforms on your behalf |
| **Account identifiers** | Ad account IDs, workspace IDs, customer IDs | Route API calls to the correct account |
| **Ad platform data** | Campaign names, metrics, creatives, audience data | Returned to Claude in response to your queries — not stored |
| **Tool call logs** | Tool name, timestamp, error messages | Debugging, reliability monitoring, abuse prevention |

We do **not** collect:

- Claude conversation content or chat history
- Payment card numbers (billing is handled by Stripe)
- Sensitive personal data (health, biometric, financial account numbers)

---

## How Connector Data Is Used

We use the data above to:

- **Execute tool calls** — pass your credentials to the relevant platform APIs and return results to Claude
- **Maintain session state** — hold OAuth tokens in memory for the duration of a connection session
- **Monitor service health** — detect errors and latency via logs and error monitoring
- **Provide support** — diagnose issues when you contact us

We do **not**:

- Use your advertising data to train AI or machine-learning models
- Build profiles for advertising purposes
- Share your ad platform data with third parties for their own marketing

---

## Sub-Processors

| Sub-Processor | Role | Data Shared |
|---------------|------|-------------|
| Meta (Facebook/Instagram) | Ad platform API | Credentials, account IDs, query parameters |
| TikTok for Business | Ad platform API | Credentials, account IDs, query parameters |
| Google (Ads & Analytics) | Ad platform API | Credentials, customer IDs, query parameters |
| Snapchat Ads | Ad platform API | Credentials, org/account IDs, query parameters |
| Google Sheets | Sheets API | Credentials, spreadsheet IDs, query parameters |
| HubSpot | CRM API | Credentials, object IDs, query parameters |
| Amazon Web Services (AWS) | Hosting (ap-southeast-1) | Request logs, error logs |
| Sentry | Error monitoring | Anonymised error traces — no personal data |
| Stripe | Billing | Payment and subscription data |
| Clerk | User authentication | Email address, session tokens |

---

## Data Retention

| Data Type | Where Stored | Retention |
|-----------|-------------|-----------|
| OAuth access tokens | In-memory only | Cleared when session ends — never written to disk |
| API keys | Encrypted in PostgreSQL (AWS ap-southeast-1) | Until you revoke or delete your account |
| Tool call / error logs | AWS CloudWatch | 30 days, then auto-deleted |
| Account and workspace data | PostgreSQL (AWS ap-southeast-1) | Until you delete your account; removed within 30 days |

Ad platform data (campaigns, insights, etc.) is fetched on demand and returned directly to Claude. **It is not stored in our systems.**

---

## Security

- **OAuth 2.0 + PKCE** (RFC 6749 + RFC 7636) — no credentials in URL query strings
- **Dynamic Client Registration** (RFC 7591) — each Claude session gets a short-lived client credential
- **TLS 1.2+** on all connections
- **Auth-guarded endpoints** — every API call requires a valid credential in the request header
- **Least-privilege scoping** — keys are scoped to workspace permissions only

---

## Your Rights

You may:

- **Access** — request a copy of your personal data
- **Delete** — delete your account from the dashboard; all associated data is removed within 30 days
- **Revoke** — revoke any connected platform's OAuth token from your account settings

Contact: [hello@mattemena.com](mailto:hello@mattemena.com)
