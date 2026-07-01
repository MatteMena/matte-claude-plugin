---
id: google-ads
title: Google Ads Tools
sidebar_position: 4
---

# Google Ads Tools

All tools for managing Google Ads accounts, campaigns, ad groups, ads, keywords, bidding strategies, budgets, and Performance Max.

## Account Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `list-google-ads-connections` | Read | List all Google Ads connections |
| `list-google-ads-customers` | Read | List all accessible customer accounts |
| `list-google-ads-customer-clients` | Read | List child accounts under an MCC |
| `get-google-ads-customer` | Read | Get details for a specific customer |
| `get-google-ads-account-summary` | Read | Get performance summary for a customer |

## Campaign Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-campaigns` | Read | List campaigns |
| `create-google-ads-campaign` | Write | Create a new campaign |
| `update-google-ads-campaign` | Write | Update campaign settings |
| `remove-google-ads-campaign` | Delete | Remove a campaign |

## Ad Group Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-ad-groups` | Read | List ad groups |
| `create-google-ads-ad-group` | Write | Create a new ad group |
| `update-google-ads-ad-group` | Write | Update ad group settings |
| `remove-google-ads-ad-group` | Delete | Remove an ad group |

## Ad Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads` | Read | List ads |
| `create-google-ads-responsive-search-ad` | Write | Create a Responsive Search Ad |
| `create-google-ads-responsive-display-ad` | Write | Create a Responsive Display Ad |
| `create-google-ads-video-ad` | Write | Create a Video Ad |
| `create-google-ads-pmax-asset-group` | Write | Create a Performance Max asset group |
| `update-google-ads-ad-status` | Write | Enable, pause, or remove an ad |
| `remove-google-ads-ad` | Delete | Remove an ad |

## Performance Max Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-pmax-asset-group-insights` | Read | Get Performance Max asset group performance |

## Insights Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-insights` | Read | Get performance metrics with date ranges and breakdowns |
| `get-google-ads-search-terms` | Read | Get search term performance |
| `get-google-ads-hourly-insights` | Read | Get hourly performance breakdown |
| `get-google-ads-conversions-by-action` | Read | Get conversions by conversion action |
| `get-google-ads-change-history` | Read | Get account change history |

## Keyword Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `list-google-ads-keywords` | Read | List keywords for an ad group |
| `get-google-ads-negative-keyword-lists` | Read | List negative keyword lists |
| `get-google-ads-negative-keywords` | Read | List negative keywords |
| `generate-google-keyword-ideas` | Read | Generate keyword ideas from seed keywords or URLs |
| `get-google-keyword-historical-metrics` | Read | Get historical search volume and competition data |
| `create-google-ads-keywords` | Write | Add keywords to an ad group |
| `remove-google-ads-keyword` | Delete | Remove a keyword |
| `create-google-ads-negative-keyword-list` | Write | Create a shared negative keyword list |

## Budget Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-budgets` | Read | List campaign budgets |
| `create-google-ads-budget` | Write | Create a new campaign budget |
| `update-google-ads-budget` | Write | Update a campaign budget |

## Bidding Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-bidding-strategies` | Read | List bidding strategies |
| `create-google-ads-bidding-strategy` | Write | Create a portfolio bidding strategy |
| `update-google-ads-bidding-strategy` | Write | Update a bidding strategy |

## Asset Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `list-google-ads-assets` | Read | List account-level assets |

## Audience Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-ads-user-lists` | Read | List remarketing user lists |
| `create-google-ads-customer-match` | Write | Create a Customer Match audience |

:::tip MCC accounts
For MCC (manager) accounts, pass `loginCustomerId` to target a specific child account. Omitting it defaults to the top-level MCC account.
:::
