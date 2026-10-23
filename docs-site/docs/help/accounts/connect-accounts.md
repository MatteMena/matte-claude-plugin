---
id: connect-accounts
title: Connect your ad accounts
sidebar_position: 1
---

# Connect your ad accounts

Connect your advertising and analytics platforms so Nerve AI, workflows, Analytics and your Claude/ChatGPT connector can work with your data.

Connections belong to the **workspace**: once one person connects an account, everyone in the workspace can use it, according to their [role](../workspace/members-and-roles.md).

---

## Supported platforms

| Platform | How you connect |
|---|---|
| **Meta Ads** (Facebook / Instagram) | Sign in to Facebook in a popup |
| **TikTok Ads** | Sign in to TikTok for Business in a popup |
| **Google Ads** | Sign in with Google in a popup |
| **Google Analytics 4** | Sign in with Google in a popup |
| **Display & Video 360** | Sign in with Google in a popup |
| **Tag Manager** | Sign in with Google in a popup |
| **Amazon Ads** | Sign in to Amazon in a popup |
| **X Ads** | Sign in to X in a popup |
| **Snapchat Ads** | Connect through the in-app connection window |
| **LinkedIn Ads** | Connect through the in-app connection window |
| **Google Sheets** | Connect through the in-app connection window |
| **HubSpot** | Connect through the in-app connection window |
| **Radius Analytics** | Uses your Nerve login; your organisation needs Radius access |

---

## Connect a platform

1. In the sidebar, go to **Get started** → **Connect accounts** (*Step 1 of 3, Connect your ad accounts*).
2. In the **Platforms** grid, click **Connect →** on the platform you want.
3. A popup opens. Sign in to the platform and approve access.
   - Use a login with access to the ad accounts you want. For Meta, that usually means a Business Manager admin; for Google Ads, a manager (MCC) or account user.
4. When the popup says **"Authorization successful! You can close this window."**, it closes automatically.
5. The card now shows **✓ N Connected**, and the account appears under **Your connections**.

Every ad account the login can access is imported automatically; there's no separate "pick accounts" step. You choose which accounts to use later, in chat, workflows and advertiser groups. See [Choose which ad accounts to use](choosing-ad-accounts.md).

:::tip Allow popups
If you see *"Failed to open popup. Please allow popups for this site."*, allow popups for `nerve.mattemena.com` in your browser and click **Connect →** again.
:::

### Add a second login for the same platform
Click **+ Add another** on the platform card. This is useful when your ad accounts are split across two Facebook or Google logins.

---

## Platform card states

| Card shows | Meaning |
|---|---|
| **Connect →** | Not connected yet |
| **Connecting...** | The sign-in popup is open |
| **✓ N Connected** + **+ Add another** | Connected; you can add another login |
| **N active • N need attention** + **Review accounts →** | Some connections need reconnecting |
| **Limit reached** | Your plan's platform or account limit has been reached (see below) |
| **Contact admin** | Your role can't add connections; ask an Admin or Owner |

Cards that need attention are listed first, then connected platforms, then the rest.

---

## Your connections

Below the grid, **Your connections** lists every connected account, with a summary such as *(3 active • 1 need attention)*.

- Search with **Search accounts...**
- Filter by **All**, **Active** or **Needs attention**
- Columns: **Platform**, **Account**, **Status**, **Details**, **Actions**

### Connection statuses

| Status | What it means | What to do |
|---|---|---|
| **Active** | Syncing normally. | Nothing |
| **Expiring soon** | The access token expires in under 7 days. | Click **Reconnect** to avoid interruption |
| **Expired** | Access expired; data is not syncing. | Click **Reconnect** |
| **Revoked** | Access was removed on the platform's side. | Click **Reconnect** |
| **Pending** | Setup wasn't finished. | Click **Reconnect** to complete it |
| **Needs reconnect** | The platform reports a problem with the connection. | Click **Reconnect** |
| **Disconnected** | The account was disconnected. | Connect it again if needed |

When any account needs attention, a banner appears at the top: *"N account(s) need reconnection"*, with a **Reconnect *(platform)*** or **Review accounts** button.

### Actions

- **Reconnect**: runs the platform sign-in again and refreshes the same connection. Your workflows and settings keep working.
- **Verify** (in the actions menu): runs a live check that the connection still works. Not available for Google Sheets, HubSpot or Radius.
- **Disconnect**: asks you to confirm (*"Are you sure you want to disconnect this account? This action cannot be undone."*). Workflows and chats that use the account stop being able to read it.

---

## Plan limits

| | Pro | Agency | Enterprise |
|---|---|---|---|
| Different platforms you can connect | 3 | 10 | Unlimited |
| Logins per platform | 2 | 2 | 2 |

If you reach a limit, the card shows **Limit reached** or you'll see *"Platform limit reached. Upgrade your plan to connect more."* Disconnect an unused platform, or [upgrade your plan](../billing/plans-and-pricing.md).

---

## Who can connect accounts

| Role | Can do |
|---|---|
| **Viewer** | See connections only |
| **Member**, **Admin**, **Owner** | Connect, reconnect and disconnect |

---

## Troubleshooting

| Problem | What to do |
|---|---|
| "Connection cancelled" | The popup was closed before you finished. Click **Connect →** again. |
| "Authorization failed" / "No authorization code received" | Try again in the same browser, and make sure you approved all requested permissions. |
| "Authorization was declined" (X Ads) | Click **Connect →** again and choose **Authorize**. |
| Connected but no ad accounts appear | The login you used has no access to those ad accounts. Check its access in Business Manager, Google Ads or TikTok, then click **Reconnect**. |
| "You don't have access to Radius. Please contact your administrator." | Your organisation hasn't been given Radius access. Contact support. |
| An account keeps expiring | Some platforms expire access periodically; reconnect when you see **Expiring soon**. If you changed your platform password, reconnect straight away. |
