---
id: faq
title: FAQ & Troubleshooting
sidebar_position: 10
---

# FAQ & Troubleshooting

## General

### What is MatteMena?

MatteMena connects Claude to your advertising platforms (Meta, TikTok, Google Ads, GA4, Snapchat, Google Sheets, HubSpot) so you can manage campaigns, pull reports, and analyse performance using natural language.

### Is this an official Anthropic product?

No. MatteMena is an independent product available at [nerve.mattemena.com](https://nerve.mattemena.com). It is available as a third-party plugin/connector in Claude's marketplace.

### Which Claude plans support this?

- **Claude.ai** (Pro, Team, Enterprise) — via the Connectors feature
- **Claude Code** — via the plugin marketplace
- **Claude Desktop** — via MCP server configuration

---

## Installation

### The plugin won't install / validate

Run `claude plugin validate ./matte-claude-plugin` and check for errors. Common causes:
- The GitHub repo must be **public**
- `plugin.json` must have `name`, `version`, `mcpServers`, and `privacy_policies` fields

### I don't see the MatteMena connector in the directory

The listing may still be pending review. In the meantime, add it as a custom connector:
- URL: `https://mcp.nerve.mattemena.com/mcp`

---

## Authentication

### The OAuth flow isn't completing

1. Make sure `nerve.mattemena.com` is reachable from your browser
2. Check that your browser isn't blocking the redirect
3. Try in a private/incognito window
4. Clear cookies for `nerve.mattemena.com` and retry

### My session keeps expiring

This usually means the refresh token has expired. Re-authenticate by removing and re-adding the connector in Claude's settings.

---

## Tools & Data

### Claude says "no platforms connected"

Claude uses `check-connections` to see your accounts. If it returns nothing:
1. Go to [nerve.mattemena.com](https://nerve.mattemena.com)
2. Ensure at least one platform is connected under **Connected Sources**
3. Re-authenticate MatteMena in Claude

### I'm getting wrong account data

Verify your connected accounts at nerve.mattemena.com. If you manage multiple ad accounts, you may need to specify which account you want:
> "Show me campaigns for my Meta account 'ABC Corp' (act_12345)"

### Google Ads cost values look too large

MatteMena automatically converts Google Ads micros (millionths of currency) to your account currency. If values still look wrong, check whether your account currency matches what you're expecting.

### I can't see TikTok Spark Ads

Spark Ads require a connected TikTok identity. Check that your TikTok identity is set up under your advertiser account.

---

## Support

For any issue not covered here, contact [hello@mattemena.com](mailto:hello@mattemena.com) with:
- Your MatteMena workspace email
- The platform you're trying to use
- The exact error message from Claude
