---
id: nerve-ai-chat
title: Chat with Nerve AI
sidebar_position: 1
---

# Chat with Nerve AI

**Nerve AI** is the AI assistant built into the app. It can analyse performance, check pacing and suggest or make changes across your connected ad accounts. You don't need Claude or ChatGPT to use it.

Go to **AI Agents** → **Agents** in the sidebar.

---

## Start a chat

1. Open **Agents**. A new chat shows four starter cards:
   - **Campaign health check**
   - **Check budget pacing**
   - **Top performers today**
   - **Where should I move budget?**
2. [Choose your accounts](#choose-accounts) (required).
3. Click a starter card or type in **Ask anything...**
   - **Enter** sends; **Shift + Enter** adds a new line.
4. While it works you'll see *"Nerve AI is pulling your data…"* and each data request as it happens. The written answer appears once it's complete.

To start over, click **New chat** at the top, or **+** in the **Chats** list.

---

## Choose accounts

Nerve AI only works with the accounts you choose. Until you choose at least one, you'll see **Select ad accounts to start**.

In the message box:

- **Account picker** (shows **All accounts** until you choose): search with **Search all accounts…**, tick accounts, or use **Select all N** / **Clear** for a platform.
- **Select advertiser group**: chooses every account in one of your [advertiser groups](../analytics/advertiser-groups.md). Click **Clear group scope** to undo.

Platforms you can choose in chat: **Meta**, **Google Ads**, **TikTok**, **Snapchat**, **Display & Video 360** and **GA4**.

- Your last choice is remembered for new chats in this workspace.
- Each chat remembers its own accounts when you reopen it.
- If you change accounts during a chat, the change applies from your next message.

---

## While Nerve AI is answering

- **Stop**: interrupts the current answer.
- **Copy**: copies a message.
- If you close the tab mid-answer, the answer keeps going; reopen the chat and it reconnects.

---

## Files Nerve AI creates

When Nerve AI creates a report, spreadsheet or chart, it appears under **Files generated** in the chat.

- Click the eye icon to preview. HTML reports open in a viewer with **Open in new tab** and **Fullscreen**.
- Click **Download** to save the file.

:::note
You can't upload your own files to Nerve AI chat. To work with your own files (for example a brief or creative), use Claude or ChatGPT with the [Nerve connector](../connect-ai/claude.md).
:::

---

## Chat history

- Your past chats are listed under **Chats**, with dates. On mobile, open the **Chat history** icon.
- Click **Archive** to remove a chat from the list. Files from archived chats are removed too, so download anything you need first.
- Chats created by [workflow runs](running-workflows.md) are not shown here.

---

## How much does a chat cost?

Every Nerve AI reply uses [credits](../billing/credits-and-top-ups.md). The cost depends on how much work the reply needed: longer answers and more data pulled cost more. The credits widget in the sidebar updates after each reply, and each charge appears as **AI agent chat** under **Credits & Billing** → **Transactions**.

**Failed replies are never charged.** They show as **Credits waived (not charged)**.

If you run out of credits, you'll see *"Insufficient credits. Please top up or upgrade your plan."* See [Credits and top-ups](../billing/credits-and-top-ups.md).

---

## Who can chat

**Members, Admins and Owners** can chat. **Viewers** can read existing chats but can't send messages.

---

## Troubleshooting

| Message | What to do |
|---|---|
| **No ad accounts connected** | Click **Connect accounts** and [connect a platform](../accounts/connect-accounts.md). |
| **Account Not Set Up**: "Please connect at least one platform account before starting a chat." | Connect at least one platform first. |
| **Select ad accounts to start** | Choose accounts with the account picker or an advertiser group. |
| **Couldn't save account scope** | Your account choice applies to this message only. Try again; if it persists, refresh the page. |
| **Failed to start chat** | Refresh and try again. Check your plan is active and you have credits. |
| "Insufficient credits…" | [Buy a top-up or upgrade](../billing/credits-and-top-ups.md). |
| Amazon Ads accounts don't appear in the picker | Amazon Ads isn't available in Nerve AI chat yet. Use Claude or ChatGPT with the Nerve connector. |
