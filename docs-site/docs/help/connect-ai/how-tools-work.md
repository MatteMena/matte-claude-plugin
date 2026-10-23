---
id: how-tools-work
title: How Nerve tools work in Claude and ChatGPT
sidebar_position: 3
---

# How Nerve tools work in Claude and ChatGPT

Nerve gives your AI assistant access to hundreds of actions across your ad platforms. Rather than loading them all at once, it gives the AI a few **discovery tools** that find and run the right actions for each request. You don't need to name tools yourself; just ask in plain English.

---

## The tools you'll see

When Claude or ChatGPT works with Nerve, you may see these tool names in the chat:

| Tool | What it does |
|---|---|
| **search tools** | Finds the right actions for your request, for example "Meta campaign insights". |
| **get tool schemas** | Looks up exactly what information an action needs. |
| **multi execute** | Runs one or more actions at once, such as pulling Meta, Google and TikTok data in parallel. |
| **check connections** | Lists which platforms your workspace has connected. |
| **show plan status** | Shows your Nerve plan and trial status, with a link to billing. Always available, even when your plan is inactive. |

More detail: [Tool Discovery Mode](../../tools/discovery.md).

---

## Platforms available

Meta (Facebook / Instagram), Google Ads, TikTok Ads, Snapchat Ads, LinkedIn Ads, X Ads, Amazon Ads (Sponsored Products), Display & Video 360, Google Analytics 4, Google Tag Manager, Google Sheets, HubSpot and Radius Analytics.

The AI can only use platforms you've [connected in Nerve](../accounts/connect-accounts.md).

---

## Does using Nerve in Claude or ChatGPT use credits?

**No.** Tool calls from Claude or ChatGPT don't use Nerve credits. Credits are only used by [Nerve AI chat](../ai-agents/nerve-ai-chat.md) and [workflow runs](../ai-agents/running-workflows.md) inside the Nerve app.

You do need an **active Nerve plan or trial**. If it's inactive, tools return a plan card instead of data. See [When your plan is inactive](../billing/invoices-cancel-and-payment-failure.md#when-your-plan-is-inactive).

Your Claude or ChatGPT subscription's own usage limits still apply.

---

## Safety

- Ask for **reads** freely: reports, insights, audits.
- For **changes** (pausing, budgets, new campaigns), the AI should describe what it will do and ask you to confirm. ChatGPT always asks before write actions; in Claude, you can set the connector's tool permissions to **ask before running**.
- New campaigns are best created **paused** so you can review them on the platform before they spend.

---

## Tips for better results

- Name the account if you have several: *"For Meta account 'ABC Corp'…"*
- Give a date range: *"last 7 days vs the previous 7"*
- Ask for a format: *"as a table"*, *"top 5 by ROAS"*
