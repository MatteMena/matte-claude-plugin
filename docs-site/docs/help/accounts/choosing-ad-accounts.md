---
id: choosing-ad-accounts
title: Choose which ad accounts to use
sidebar_position: 2
---

# Choose which ad accounts to use

When you [connect a platform](connect-accounts.md), Nerve imports every ad account that login can access. You then choose which of them to use in each place:

| Where | How you choose | Why it matters |
|---|---|---|
| **Nerve AI chat** | The account picker in the message box | Limits the AI to the accounts you're asking about |
| **Workflows** | **Connected Sources** in the workflow builder | Sets which accounts a workflow reads and changes |
| **Advertiser groups** | **Connected ad accounts** in the group form | Groups one advertiser's accounts for Analytics and KPI alerts |
| **Claude / ChatGPT** | Name the account in your prompt | The AI can see every connected account; say which one you mean |

---

## In Nerve AI chat

1. Open **AI Agents** → **Agents**.
2. In the message box, click the **account picker**. It shows **All accounts** until you choose.
3. Search with **Search all accounts…**, tick accounts, or use **Select all N** / **Clear** for a platform.
4. Or click **Select advertiser group** to choose every account in an [advertiser group](../analytics/advertiser-groups.md). **Clear group scope** removes it.

Your choice is remembered for new chats in this workspace. More in [Chat with Nerve AI](../ai-agents/nerve-ai-chat.md).

---

## In workflows

In the workflow builder, under **Connected Sources**, choose a **user account** (the login), then the **ad account** under it. Click **Refresh** if a newly connected account isn't listed yet. Platforms you haven't connected show as **Not connected**.

More in [Create a workflow](../ai-agents/workflows.md).

---

## In Claude or ChatGPT

Your connector can see every account connected in the workspace. If you manage several, name the one you mean:

> "Show me campaigns for my Meta account 'ABC Corp' (act_12345)"

To check what's connected, ask:

> "What advertising platforms do I have connected?"
