---
id: chatgpt
title: Connect Nerve to ChatGPT
sidebar_position: 2
---

# Connect Nerve to ChatGPT

Connect Nerve to ChatGPT so it can read and manage your connected ad accounts.

In the app, the same steps are under **Get started** → **Connect to AI** → **ChatGPT**.

:::caution Paid ChatGPT plan required
Custom connectors need ChatGPT **Plus**, **Pro**, **Business**, **Enterprise** or **Edu**. On Business, Enterprise and Edu, a workspace admin may need to allow custom MCP servers first.
:::

:::note Before you start
- [Connect at least one ad platform](../accounts/connect-accounts.md) in Nerve.
- Sign in to [nerve.mattemena.com](https://nerve.mattemena.com) in the same browser you use for ChatGPT.
:::

---

## Steps

1. In ChatGPT, open **Settings** → **Plugins** (under Integrations).
2. Click **Add** → **Custom / MCP server**.
3. Fill in:
   - **Name:** `Nerve`
   - **Connection:** **Server URL**
   - **URL:** `https://mcp.nerve.mattemena.com/mcp`
   - **Authentication:** **OAuth**
4. Tick **I understand and want to continue**, then click **Create**.
5. You're sent to Nerve's approval screen, **"ChatGPT is Requesting Access"**. Check the workspace and click **Connect**.
6. When you see **"Successfully Connected!"**, you're returned to ChatGPT.
7. Start a new chat, click **+** and enable **Nerve**.

### Try it
> "What advertising platforms do I have connected?"

---

## Good to know

- **Reading data** (reports, insights, account lists) runs without asking.
- **Changes** (pausing campaigns, editing budgets, creating ads) ask you to confirm in ChatGPT before they run.
- You may have seen older guides mention a **Developer mode** toggle. ChatGPT no longer needs it.

---

## Troubleshooting

| Problem | What to do |
|---|---|
| I can't find **Plugins** / **Add custom** | Check you're on a paid plan. On Business/Enterprise/Edu, ask your ChatGPT admin to allow custom MCP servers. |
| Nerve isn't used in my chat | Click **+** in the chat and enable **Nerve**, or start a new chat. |
| Authorization keeps looping | Sign in to [nerve.mattemena.com](https://nerve.mattemena.com) in the same browser first, then try again. |
| "Invalid Request" | The approval link expired (after 5 minutes) or was incomplete. Start again from ChatGPT. |
| ChatGPT shows a plan or payment error | Your workspace plan is inactive. See [When your plan is inactive](../billing/invoices-cancel-and-payment-failure.md#when-your-plan-is-inactive). |

---

## Disconnect ChatGPT

Remove the **Nerve** connector in ChatGPT under **Settings** → **Plugins**.
