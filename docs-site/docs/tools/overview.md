---
id: overview
title: Tool Reference Overview
sidebar_position: 1
---

# Tool Reference

MatteMena exposes **185+ tools** across 7 advertising and marketing platforms.

In **Tool Discovery Mode** (default), Claude automatically finds and calls the right tools via 4 discovery meta-tools — you never need to select tools manually. See [Discovery Tools →](/docs/tools/discovery).

## Tools by Platform

| Platform | Read Tools | Write Tools | Delete Tools | Total |
|----------|-----------|-------------|--------------|-------|
| [Meta](/docs/tools/meta) | 17 | 10 | 6 | 33 |
| [TikTok](/docs/tools/tiktok) | 15 | 10 | 3 | 28 |
| [Google Ads](/docs/tools/google-ads) | 22 | 16 | 4 | 42 |
| [GA4](/docs/tools/ga4) | 17 | 0 | 0 | 17 |
| [Snapchat](/docs/tools/snapchat) | 5+ | 3+ | 1+ | ~12 |
| [Google Sheets](/docs/tools/google-sheets) | 10 | 6 | 1 | 17 |
| [HubSpot](/docs/tools/hubspot) | 12 | 9 | 6 | 27 |

## Tool naming convention

Tools follow a consistent naming pattern:

| Prefix | Operation |
|--------|-----------|
| `get-*`, `list-*` | Read data (non-destructive) |
| `create-*`, `add-*` | Create a new resource |
| `update-*` | Modify an existing resource |
| `delete-*`, `remove-*`, `clear-*` | Remove a resource |
| `search-*`, `find-*` | Search / filter |
| `generate-*` | Generate suggestions (e.g. keyword ideas) |

## Discovery Tools

When `TOOL_DISCOVERY_MODE=true`, only these 4 tools are exposed:

| Tool | Purpose |
|------|---------|
| `search-tools` | Find relevant tools by natural language query |
| `multi-execute` | Execute multiple tools in parallel |
| `get-tool-schemas` | Get JSON Schema for specific tools |
| `check-connections` | Check which platforms are connected |

[Discovery Tools reference →](/docs/tools/discovery)
