---
id: advertiser-groups
title: Advertiser groups
sidebar_position: 1
---

# Advertiser groups

An **advertiser group** bundles the Meta, TikTok and Google Ads accounts that belong to one advertiser (a brand or client). It also sets that advertiser's objective and **KPI targets**.

Advertiser groups power:
- the [Analytics dashboard](analytics-dashboard.md), which always shows one group at a time,
- **Performance Alerts**, which compare actual results with your targets,
- choosing accounts in [Nerve AI chat](../ai-agents/nerve-ai-chat.md#choose-accounts).

Go to **Settings** → **Advertiser groups**.

---

## Create an advertiser group

1. Click **New advertiser group**.
2. **Advertiser details**
   - **Advertiser name** (required), for example "Acme Beauty"
   - **Website URL** (optional)
   - **Industry**: Beauty & personal care, Food & beverage, Retail & ecommerce, Real estate, Finance, Travel & hospitality, Healthcare, Automotive, Education or Other
   - **Target currency**: currently USD
3. **Connected ad accounts** (required): tick the **Meta**, **TikTok** and **Google Ads** accounts that belong to this advertiser. You can only pick accounts you've already [connected](../accounts/connect-accounts.md).
4. **KPIs to track**: choose an objective:
   **Sales / ecommerce**, **Lead generation**, **Conversions**, **App installs**, **Traffic** or **Awareness**.
   Nerve pre-fills sensible **Media KPIs** and **Business KPIs** (a primary and a secondary for each). Adjust them and enter a **Target** for each, for example *Primary media KPI: CTR 2.5%*.
5. Click **Save advertiser group**.

---

## Edit or delete a group

On the group's card, click **Edit group** (or **⋮** → **Edit**), make your changes and click **Save changes**.

To delete, click **⋮** → **Delete** and confirm. The group's accounts become ungrouped; the accounts themselves stay connected.

---

## Rules and limits

- **Up to 3 advertiser groups per workspace.** At the limit, **New advertiser group** is disabled. Delete a group to create another.
- **An ad account can be in only one group at a time.**
- Only **Meta**, **TikTok** and **Google Ads** accounts can be added to groups.

---

## Troubleshooting

| Message | What to do |
|---|---|
| "Advertiser name is required" | Enter a name. |
| "Select at least one ad account (Meta, TikTok or Google Ads)" | Tick at least one account. If none are listed, [connect a platform](../accounts/connect-accounts.md) first. |
| An account I want isn't listed | It may already be in another group (remove it there first), or it's not a Meta, TikTok or Google Ads account. |
| "You've reached the limit of 3 advertiser groups" | Delete a group you no longer need. |
