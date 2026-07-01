---
id: google-ads
title: Google Ads
sidebar_position: 3
---

# Google Ads

Connect Claude to your Google Ads account (including MCC / manager accounts) to manage campaigns, ad groups, keywords, bidding strategies, budgets, and Performance Max asset groups.

## Connecting Google Ads

1. Go to [nerve.mattemena.com](https://nerve.mattemena.com) → **Connected Sources**
2. Click **Connect Google Ads**
3. Authorise access to your Google account
4. Select the customer accounts you want Claude to access

## MCC (Manager) Accounts

If you manage multiple accounts under an MCC, Claude can operate on any sub-account. Tools that accept a `loginCustomerId` parameter can be used to target specific child accounts within your MCC.

## What you can do

### Accounts & Insights
- List customers and MCC child accounts
- Get account summaries and performance
- Hourly performance breakdowns
- Conversions by action

### Campaigns
- List, create, update, and remove campaigns
- Supports Standard, Shopping, Display, Video, and Performance Max campaign types

### Ad Groups & Ads
- List, create, update, and remove ad groups
- Create Responsive Search Ads, Responsive Display Ads, and Video Ads
- Update ad status (enabled / paused / removed)

### Performance Max (PMax)
- Create PMax asset groups
- Get PMax asset group insights

### Keywords
- List keywords and negative keywords
- Create keywords and negative keyword lists
- Remove keywords
- Generate keyword ideas
- Get historical keyword metrics

### Bidding & Budgets
- List and create bidding strategies
- Update bidding strategies
- List, create, and update budgets

### Audiences
- List user lists (remarketing audiences)
- Create customer match audiences

### Change History
- Get account change history

## Example prompts

```
"Show me my top 10 keywords by conversion value this month"
"Create a new Search campaign called 'Summer Sale 2026' with a $200/day budget"
"What's my PMax asset group performance?"
"Generate keyword ideas for 'running shoes' in Australia"
"Pause all campaigns with a CPA over $100"
```

## Note on cost values

Google Ads returns cost values in **micros** (millionths of a currency unit). MatteMena automatically divides these by 1,000,000 before returning them to Claude, so all cost figures you see are in your account currency.

## Tool reference

See the [Google Ads tools reference →](/docs/tools/google-ads) for the full list of available tools.
