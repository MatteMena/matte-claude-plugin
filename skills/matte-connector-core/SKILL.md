---
name: matte-connector-core
description: How to use the MatteMena/Nerve MCP connector (mattemena-remote) to read or write Meta, TikTok, Google Ads, GA4, Snapchat, Google Sheets, or HubSpot data. Use this whenever a task touches connected ad accounts or marketing data through Matte — pulling campaigns, insights, or account structure, checking which accounts are connected, or creating/updating/pausing/deleting anything in a live ad account. This is the base workflow every other Matte skill (media-planner, account-audit, performance-reporting) builds on — consult it first whenever those skills call MCP tools, and consult it directly for one-off requests like "show me my Meta campaigns" or "pause that ad set" that don't need a full audit or report.
---

# Matte Connector Core

The MatteMena MCP server (`mattemena-remote`) exposes 185+ tools across Meta, TikTok, Google Ads, GA4, Snapchat, Google Sheets, and HubSpot. It runs in **Tool Discovery Mode** by default, so only 4 meta-tools are visible at any time — everything else is found through them.

## The 4 discovery tools

| Tool | Use it to |
|---|---|
| `check-connections` | See which platforms/accounts are actually connected. Call this first in any new session before assuming an account exists. |
| `search-tools` | Find the right tool(s) by natural-language query, e.g. `"meta campaign insights"` or `"pause google ads ad group"`. |
| `get-tool-schemas` | Get the exact parameters a tool needs before calling it (do this before any write/create/delete call so you don't guess params). |
| `multi-execute` | Run several tool calls in one round trip. Use this instead of calling tools one at a time whenever you need data from more than one platform, or several endpoints on the same platform (e.g. campaigns + insights + ad sets together). |

**Standard pattern for any task:**
1. `check-connections` — confirm the platform/account you need is actually connected. If not, tell the person and point them to nerve.mattemena.com to connect it — don't fabricate account data.
2. `search-tools` with a plain-language description of what you need.
3. `get-tool-schemas` for any write/create/update/delete tool before calling it.
4. `multi-execute` to batch the actual calls, especially across platforms.

## Read vs write — always confirm before writing

Tool name prefixes tell you the operation:

| Prefix | Operation |
|---|---|
| `get-*`, `list-*`, `search-*`, `find-*` | Read — safe, no confirmation needed |
| `create-*`, `add-*` | Creates a new resource — confirm scope/budget with the person first |
| `update-*` | Modifies something live — state exactly what's changing before calling |
| `delete-*`, `remove-*`, `clear-*` | Destructive — always confirm explicitly, this can't be undone |

Never chain a write call straight off a read without restating what you're about to change and getting a yes. For budget or status changes specifically: state the current value, the new value, and wait for confirmation before calling the tool.

## Platform-specific things to get right

**Google Ads**
- Costs come back in **micros** (millionths of the account currency) — Matte converts these automatically, but if a number looks 1,000,000x too big, that's the giveaway.
- MCC (manager) accounts need `loginCustomerId` to target a specific child account. Omit it and you're querying the top-level MCC, not the child account the person actually means.
- Use `list-google-ads-customer-clients` to enumerate child accounts under an MCC before asking which one they mean.

**Meta**
- Ad account IDs are `act_XXXXXXXXXX` — always confirm you've got the right one if the person manages more than one (check `list-meta-connections` or `get-user-ad-accounts`).

**TikTok**
- Spark Ads need a connected TikTok identity (`get-tiktok-identities`) — if Spark Ad data is missing, that's usually why.

**GA4**
- All GA4 tools are read-only. There's no write path here.

**Snapchat**
- Snapchat tool coverage is thinner than the others (~12 tools vs 30-40+ elsewhere) — if something doesn't exist, say so rather than approximating with a Meta/Google equivalent.

## When account data isn't there

If `check-connections` comes back empty for a platform, or a tool call fails with an auth error: don't guess or use stale numbers from earlier in the conversation. Tell the person the account isn't connected (or the session expired) and point them to nerve.mattemena.com → Connected Sources to fix it. Re-authentication is done by removing and re-adding the connector in Claude's settings.

## If they manage multiple accounts

Ask which account if it's ambiguous — don't default to "the first one that comes back." A quick disambiguating question ("Meta account 'ABC Corp' or 'XYZ Retail'?") is cheaper than pulling and presenting the wrong account's numbers.
