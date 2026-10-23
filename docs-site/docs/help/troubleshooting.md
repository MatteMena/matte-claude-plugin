---
id: troubleshooting
title: Troubleshooting
sidebar_position: 99
---

# Troubleshooting

Common messages in Nerve, and how to fix them. Can't find yours? Email [hello@mattemena.com](mailto:hello@mattemena.com) with your workspace name, what you were doing, and the exact message.

---

## Sign-in and workspaces

| Message | Fix | Guide |
|---|---|---|
| "Couldn't find your account…" | Sign up instead, or check the email for typos | [Sign up](getting-started/sign-up.md) |
| "An account with this email already exists…" | Use **Sign in** / **Forgot password?** | [Sign up](getting-started/sign-up.md) |
| "That code has expired…" | Click **Resend code** | [Sign up](getting-started/sign-up.md) |
| "Failed to create workspace" | Try again; contact support if it persists | [Create a workspace](getting-started/create-workspace.md) |
| Every page sends me to Credits & Billing | Your plan is inactive | [Plan inactive](billing/invoices-cancel-and-payment-failure.md#when-your-plan-is-inactive) |
| "Member limit reached…" | Remove a member, cancel a pending invite, or upgrade | [Members and roles](workspace/members-and-roles.md) |

## Connecting accounts

| Message | Fix | Guide |
|---|---|---|
| "Failed to open popup. Please allow popups for this site." | Allow popups for nerve.mattemena.com | [Connect accounts](accounts/connect-accounts.md) |
| "Connection cancelled" | The popup was closed; click **Connect →** again | [Connect accounts](accounts/connect-accounts.md) |
| "Authorization failed" | Retry and approve all permissions | [Connect accounts](accounts/connect-accounts.md) |
| **Expired** / **Revoked** / **Needs reconnect** | Click **Reconnect** | [Connect accounts](accounts/connect-accounts.md#connection-statuses) |
| "Platform limit reached…" / **Limit reached** | Disconnect a platform or upgrade | [Plans and pricing](billing/plans-and-pricing.md) |
| Connected, but no ad accounts appear | The login has no access to them; fix access on the platform, then **Reconnect** | [Connect accounts](accounts/connect-accounts.md) |

## Nerve AI and workflows

| Message | Fix | Guide |
|---|---|---|
| **Select ad accounts to start** | Pick accounts or an advertiser group | [Nerve AI chat](ai-agents/nerve-ai-chat.md#choose-accounts) |
| **No ad accounts connected** | Connect a platform | [Connect accounts](accounts/connect-accounts.md) |
| "Insufficient credits. Please top up or upgrade your plan." | Buy a top-up or upgrade | [Credits](billing/credits-and-top-ups.md) |
| **Stopped — out of credits** | Top up, then **Retry Run** | [Running workflows](ai-agents/running-workflows.md) |
| "Missing platform connections…" | Connect the platform, then reselect it in **Connected Sources** | [Create a workflow](ai-agents/workflows.md#missing-connections) |
| **Run failed** | Open **View run details**, fix the cause, then **Retry Run** (failed runs aren't charged) | [Running workflows](ai-agents/running-workflows.md) |
| Scheduled workflow didn't run | Check it's **Active** and the schedule is on; runs happen on the hour | [Scheduling](ai-agents/scheduling-workflows.md) |

## Analytics

| Message | Fix | Guide |
|---|---|---|
| "Set up an advertiser group to see analytics" | Create an advertiser group | [Advertiser groups](analytics/advertiser-groups.md) |
| "N accounts failed to load…" | Reconnect expired accounts, or refresh | [Analytics](analytics/analytics-dashboard.md) |
| "You've reached the limit of 3 advertiser groups" | Delete a group you no longer need | [Advertiser groups](analytics/advertiser-groups.md) |

## Claude and ChatGPT

| Message | Fix | Guide |
|---|---|---|
| Authorization keeps looping | Sign in to nerve.mattemena.com in the same browser first | [Claude](connect-ai/claude.md#troubleshooting) |
| "Invalid Request" | The approval link expired (5 minutes); start again from Claude/ChatGPT | [Claude](connect-ai/claude.md#troubleshooting) |
| **Connect an Advertising Account** | Connect a platform on that screen, then **Connect** | [Claude](connect-ai/claude.md) |
| **Plan required** / **Trial ended** / **Subscription canceled** / **Payment failed** | Fix billing, then **Continue after upgrading** | [Plan inactive](billing/invoices-cancel-and-payment-failure.md#when-your-plan-is-inactive) |
| Nerve isn't used in my chat | Enable the Nerve connector in that chat | [ChatGPT](connect-ai/chatgpt.md) |

## Billing

| Message | Fix | Guide |
|---|---|---|
| "Your free trial has ended. Add a payment method…" | Add a card; the pending invoice is paid automatically | [Free trial](billing/free-trial.md) |
| "Your last payment failed…" | Update your card or **Retry payment** | [Failed payments](billing/invoices-cancel-and-payment-failure.md#failed-payments) |
| "Free trial already used on this account." | Choose a paid plan with **Subscribe** | [Plans and pricing](billing/plans-and-pricing.md) |
| "Subscribe to a plan to purchase top-up credits." | Choose a plan first | [Credits](billing/credits-and-top-ups.md) |
| "Ask a workspace admin to add a payment method…" | Only Owners/Admins can manage billing | [Members and roles](workspace/members-and-roles.md) |
