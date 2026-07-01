---
id: installation
title: Installation
sidebar_position: 2
---

# Installation

MatteMena is available as both a **Claude Code plugin** and a **Claude.ai connector**. Install the one that matches your Claude client.

---

## Prerequisites

Before installing, sign up and connect at least one ad platform:

1. Go to [nerve.mattemena.com](https://nerve.mattemena.com)
2. Create a free account
3. Under **Connected Sources**, connect Meta, TikTok, Google Ads, or any other platform

---

## Option 1: Claude Code Plugin

The Claude Code plugin is available in the plugin marketplace.

### Install from marketplace

1. Open **Claude Code**
2. Click **Add marketplace** → **Browse plugins**
3. Search for `MatteMena` or `mattemena-nerve`
4. Click **Install**

### Install from repository

1. Open **Claude Code**
2. Click **Add marketplace** → **Add from a repository**
3. Enter: `https://github.com/MatteMena/matte-claude-plugin`
4. Click **Install**

### Authenticate

After install, Claude Code will prompt you to authenticate the `mattemena-remote` connector:

1. Click **Connect** or **Login** when prompted
2. You will be redirected to `nerve.mattemena.com`
3. Sign in with your MatteMena account
4. Approve access — you'll be redirected back to Claude Code
5. Done! MatteMena tools are now available

---

## Option 2: Claude.ai Connector

The remote connector works on Claude.ai web, desktop, and mobile.

### Add as a custom connector

1. Go to [claude.ai](https://claude.ai) and open **Settings**
2. Navigate to **Connectors** → **Add custom connector**
3. Enter the server URL: `https://mcp.nerve.mattemena.com/mcp`
4. Click **Connect**
5. Complete the OAuth flow when prompted

### From the Connectors Directory

If MatteMena is listed in the [Connectors Directory](https://claude.ai/admin-settings/directory):

1. Go to **Settings** → **Connectors** → **Browse directory**
2. Search for `MatteMena`
3. Click **Add** → authenticate

---

## Option 3: Claude Desktop

1. Open Claude Desktop → **Settings** → **Extensions**
2. Add a new MCP server with:
   - **URL:** `https://mcp.nerve.mattemena.com/mcp`
   - **Type:** HTTP (Streamable)
3. Authenticate when prompted

---

## Verifying the connection

After setup, ask Claude:

> "What advertising platforms do I have connected?"

Claude will use the `check-connections` tool to list your connected accounts.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "No tools available" | Re-authenticate — your session may have expired |
| "Connection refused" | Verify the MCP URL is `https://mcp.nerve.mattemena.com/mcp` |
| "No accounts found" | Connect at least one platform at [nerve.mattemena.com](https://nerve.mattemena.com) |
| Auth loop | Clear cookies and try again; ensure `nerve.mattemena.com` is reachable |

For further help: [hello@mattemena.com](mailto:hello@mattemena.com)
