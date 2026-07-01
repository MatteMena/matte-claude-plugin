---
id: meta
title: Meta Tools
sidebar_position: 2
---

# Meta Tools

All tools for managing Meta (Facebook/Instagram) ad accounts, campaigns, creatives, audiences, and pixels.

## Account Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `list-meta-connections` | Read | List all Meta ad account connections in your workspace |
| `get-user-ad-accounts` | Read | Get all ad accounts accessible to your Meta user |
| `get-ad-account` | Read | Get details for a specific ad account |
| `get-account-summary` | Read | Get a performance summary for an ad account |

## Campaign Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-campaigns` | Read | List campaigns for an ad account |
| `create-meta-campaign` | Write | Create a new campaign |
| `update-meta-campaign` | Write | Update campaign name, status, budget, or objective |
| `delete-meta-campaign` | Delete | Delete a campaign |

## Ad Set Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-ad-sets` | Read | List ad sets for a campaign or account |
| `create-meta-ad-set` | Write | Create a new ad set with targeting and schedule |
| `update-meta-ad-set` | Write | Update ad set settings |
| `delete-meta-ad-set` | Delete | Delete an ad set |

## Ad Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-ads` | Read | List ads for an ad set or account |
| `get-graph-ad-previews` | Read | Get ad preview URLs |
| `create-meta-ad` | Write | Create a new ad |
| `update-meta-ad` | Write | Update ad status or creative |
| `delete-meta-ad` | Delete | Delete an ad |

## Creative Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-meta-ad-creatives` | Read | List all ad creatives in an account |
| `get-meta-ad-creative` | Read | Get a specific ad creative |
| `create-meta-ad-creative` | Write | Create a new ad creative |
| `delete-meta-ad-creative` | Delete | Delete an ad creative |

## Asset Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-ad-images` | Read | List ad images in an account |
| `get-ad-videos` | Read | List ad videos in an account |

## Insights Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-insights` | Read | Get performance metrics with date ranges and breakdowns |
| `get-report-keys` | Read | List available saved reports |
| `get-report-content` | Read | Get content of a specific saved report |

## Pixel Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-meta-pixels` | Read | List Meta pixels for an account |
| `get-meta-pixel-stats` | Read | Get event statistics for a pixel |

## Audience Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-meta-custom-audiences` | Read | List custom audiences |
| `create-meta-custom-audience` | Write | Create a custom audience from a customer list |
| `create-meta-lookalike-audience` | Write | Create a lookalike audience based on a source audience |

## Other Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-meta-pages` | Read | List Facebook Pages connected to your account |
