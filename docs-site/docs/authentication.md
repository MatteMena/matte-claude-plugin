---
id: authentication
title: Authentication
sidebar_position: 3
---

# Authentication

MatteMena uses **OAuth 2.0 with PKCE (S256)** — the same standard used by "Login with Google" and "Login with GitHub". No API keys, no copy-pasting credentials.

---

## How the OAuth flow works

```
1. Claude requests access → MatteMena redirects to nerve.mattemena.com login
2. You sign in → MatteMena issues an authorization code
3. Claude exchanges the code for an access token (with PKCE verification)
4. Claude uses the token for all subsequent tool calls
5. Token refreshes automatically in the background
```

### Dynamic Client Registration (DCR)

MatteMena supports **RFC 7591 Dynamic Client Registration**. Claude (or any MCP-compatible client) can register itself automatically without manual credential setup. This is why the install process is just a single OAuth click.

---

## OAuth Endpoints

| Endpoint | URL |
|----------|-----|
| MCP server | `https://mcp.nerve.mattemena.com/mcp` |
| Registration | `https://mcp.nerve.mattemena.com/register` |
| Authorization | `https://mcp.nerve.mattemena.com/authorize` |
| Token | `https://mcp.nerve.mattemena.com/token` |
| OAuth submit | `https://mcp.nerve.mattemena.com/oauth/submit` |
| Protected resource metadata | `https://mcp.nerve.mattemena.com/.well-known/oauth-protected-resource` |
| Authorization server metadata | `https://mcp.nerve.mattemena.com/.well-known/oauth-authorization-server` |

---

## Token lifetime

| Token | Lifetime |
|-------|---------|
| Access token | Short-lived (minutes to hours) |
| Refresh token | Long-lived (days) |
| Session | Refreshed automatically |

You should never need to re-authenticate unless you explicitly revoke access or the refresh token expires.

---

## Revoking access

To disconnect MatteMena from Claude:

1. Go to [nerve.mattemena.com](https://nerve.mattemena.com)
2. Navigate to **Settings** → **Connected Clients**
3. Click **Revoke** next to the Claude session

Alternatively, remove the connector in Claude's settings.

---

## Security

- All tokens are transmitted over **TLS 1.2+**
- Tokens are **never placed in URL query strings** (always in headers)
- PKCE (S256) prevents authorization code interception attacks
- Tokens are held **in memory only** — never written to disk by the MCP server
- All API calls are auth-guarded with the `x-api-key` header internally

---

## Allowed Redirect URIs

The following redirect URIs are registered for the OAuth flow:

```
https://claude.ai/api/mcp/auth_callback
http://localhost/callback
http://127.0.0.1/callback
```

Claude Code uses loopback URIs (RFC 8252) — the port is ephemeral and any port is accepted.
