---
id: analytics-dashboard
title: Analytics dashboard
sidebar_position: 2
---

# Analytics dashboard

**Analytics** shows cross-platform ad performance for one [advertiser group](advertiser-groups.md) at a time: spend, revenue, ROAS, KPIs against your targets, and every campaign in one place.

Go to **Monitor** → **Analytics** in the sidebar.

:::note Before you start
Analytics needs at least one advertiser group. If you don't have one, you'll see *"Set up an advertiser group to see analytics"*. Click **Create advertiser group**.
:::

Analytics currently covers **Meta**, **Google Ads** and **TikTok**.

---

## Choose what you're looking at

At the top of the page:

1. **Advertiser group**: pick the group to view.
2. **Date range**: pick a preset (**Today**, **Yesterday**, **Last 7 days**, **Last 14 days**, **Last 30 days**, **Last 90 days**, **This month**, **Last month**, **This quarter**) or choose dates on the calendar, then click **Apply**.

A banner confirms which group's accounts the dashboard is filtered to, with a link to edit the group.

---

## Summary cards

| Card | Shows |
|---|---|
| **Total Spend** | Spend across all accounts in the group |
| **Total Revenue** | Revenue reported by the platforms |
| **Blended ROAS** | Total revenue ÷ total spend |
| **Purchases** | Total purchases, with **Cost per purchase** |
| **Top Platform** | The platform with the best results for the range |

Each card shows the change compared with the previous period of the same length. A **—** means a platform didn't report that metric.

---

## Charts

- **Platforms** toggles hide or show a platform's line on the charts (the totals don't change).
- **Daily Spend / Impressions by Platform**: day-by-day trend for each platform.
- **KPI** chart, with two tabs:
  - **Media KPI**: CTR, CPC, CPM, Clicks
  - **Business KPI**: Leads, Cost per Lead, ROAS, Revenue, Purchases, CPP, CPA
- Click **Show table** to see a chart's numbers, or **Show chart** to switch back.

---

## Platform Breakdown

One card per platform with **Total Spend**, **Revenue**, **ROAS**, **Purchases**, **CTR** and **Impressions**.

---

## Performance Alerts

Compares actual results against the KPI targets in your advertiser group. Each alert shows the **Actual**, **Target** and the **Δ vs target**, with a status:

| Status | Meaning |
|---|---|
| **ON TRACK** | Meeting or beating the target |
| **AT RISK** | Close to missing the target |
| **OFF TRACK** | Missing the target |
| **NOT TRACKED** | The platforms don't report this KPI |
| **NO DATA** | No data for this date range |

Click **Diagnose with AI** on an alert to open a [Nerve AI chat](../ai-agents/nerve-ai-chat.md) that investigates the cause.

No alerts? Add KPI targets to the group: *"No KPI targets set for this advertiser group yet."*

---

## Campaigns table

Every campaign in the group, with **Campaign**, **Platform**, **Status**, **Spend**, **Impressions**, **Clicks**, **CTR**, **CPC**, **Purchases** and **ROAS**. Use **Search campaigns…** to find one. On mobile, use the filter to narrow by platform and status (Active / Paused).

---

## Troubleshooting

| Message | What to do |
|---|---|
| "No supported ad accounts linked" | The group has no Meta, Google Ads or TikTok accounts. [Edit the group](advertiser-groups.md#edit-or-delete-a-group). |
| "N accounts failed to load — totals below are incomplete" | Click **Reconnect** if a connection expired, or refresh to retry if it timed out. |
| "No data could be loaded" | Check your connections under **Connect accounts**, then refresh. |
| "No campaigns ran in this date range." | Pick a wider date range. |
| Numbers differ slightly from the platform's own dashboard | Platforms update and re-attribute data for several days. Use the same date range and timezone when comparing. |
