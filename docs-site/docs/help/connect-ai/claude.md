---
id: claude
title: Connect Nerve to Claude
sidebar_position: 1
---

# Connect Nerve to Claude

Connect Nerve to Claude so Claude can read and manage your connected ad accounts in any chat.

In the app, the same steps are under **Get started** → **Connect to AI** → **Claude**.

:::note Before you start
- [Connect at least one ad platform](../accounts/connect-accounts.md) in Nerve.
- Sign in to [nerve.mattemena.com](https://nerve.mattemena.com) in the **same browser** you use for Claude. This avoids sign-in loops.
:::

---

## Option 1: Remote connector (recommended)

Works in **Claude.ai** (web, desktop and mobile apps) and **Claude Desktop**.

1. **Copy the MCP URL:**
   ```
   https://mcp.nerve.mattemena.com/mcp
   ```
2. **Add the connector in Claude:**
   1. In Claude, open **Settings** → **Connectors**.
   2. Click **Add custom connector**.
   3. Name it **Nerve** and paste the URL.
   4. Save. (The **Open Claude** button in Nerve's **Connect to AI** page opens this screen for you.)
3. **Connect and authorize:**
   1. Click **Connect** on the new connector.
   2. You're sent to Nerve's approval screen: **"Claude is Requesting Access"**. It shows your workspace, your connected platforms and what Claude will be able to do:
      - View your ad accounts and campaigns
      - Read advertising insights and analytics
      - Access performance summaries
   3. Check the workspace name is right (use the workspace switcher to change it), then click **Connect**.
   4. You'll see **"Successfully Connected!"**, and you're returned to Claude.
4. **Allow the tools:** in the connector's settings in Claude, enable its tool permissions.

### Try it
Start a new chat and ask:

> "What advertising platforms do I have connected?"

---

## Option 2: Claude.ai plugin

1. In Claude.ai, open **Settings** → **Plugins** → **Add** → **From GitHub**.
2. Paste `https://github.com/MatteMena/matte-claude-plugin`.
3. Install **Mattemena Nerve**, then authorize as in step 3 above.

---

## Option 3: Claude Code

1. In Claude Code, choose **Add marketplace** → **Add from a repository**.
2. Enter `https://github.com/MatteMena/matte-claude-plugin`.
3. Install `mattemena-nerve` and sign in when asked.

The plugin also adds ready-made skills: account audits, campaign optimisation, campaign setup, media planning and performance reports. See [Installation](../../installation.md) for details.

---

## Which workspace does Claude use?

The one you picked on the approval screen. To switch Claude to a different workspace, remove the connector in Claude, add it again, and choose the other workspace when you approve.

---

## Troubleshooting

| Problem | What to do |
|---|---|
| The connector doesn't show up in my chat | In the chat, open the tools/connectors menu and make sure **Nerve** is turned on. |
| Authorization keeps looping | Sign in at [nerve.mattemena.com](https://nerve.mattemena.com) in the same browser first, then click **Connect** again. Private/incognito windows can also help. |
| "Invalid Request" on the approval screen | The link was incomplete or too old. Approval links expire after 5 minutes. Start the connection again from Claude. |
| **Connect an Advertising Account** on the approval screen | Your workspace has no connected platforms. Connect one using the buttons shown, then click **Connect**. |
| Claude says it can't access my accounts | Ask "What platforms do I have connected?" If none, check **Connect accounts** in Nerve. If a connection shows **Expired**, click **Reconnect**. |
| Claude shows **Plan required**, **Trial ended**, **Subscription canceled** or **Payment failed** | Your workspace's plan is inactive. Click the card's button, fix billing, then **Continue after upgrading**. See [When your plan is inactive](../billing/invoices-cancel-and-payment-failure.md#when-your-plan-is-inactive). |
| Claude isn't using Nerve | Mention it in your prompt: "Using Nerve, show me…" |

---

## Disconnect Claude

Remove the **Nerve** connector in Claude under **Settings** → **Connectors**.
