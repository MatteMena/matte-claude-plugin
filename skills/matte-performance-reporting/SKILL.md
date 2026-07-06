---
name: matte-performance-reporting
description: Build HTML performance reports with real visuals (charts, funnels, scroll-based storytelling) for paid media campaigns across Meta, TikTok, Google Ads, Snapchat, and GA4, pulled live via the Matte connector and styled in the Platformance brand system. Use this whenever someone asks to "build a report," "create a performance report," wants a dashboard, a storybook/storytelling report, or an exec summary of campaign performance. Two output modes: a compact single-page exec dashboard, or a multi-page animated storybook report — ask which if it's not obvious from the request. Always pull live account data first, never fabricate numbers.
---

# Performance Reporting

Builds HTML performance reports styled in the Platformance brand system, using real data pulled live through the Matte connector. Read `matte-connector-core` first for the MCP workflow, and `references/platformance-brand.md` for the full visual spec before writing any HTML.

## Step 1 — Scope the report

Confirm:
- **Account(s) / platform(s)** — single platform or cross-platform comparison
- **Date range** — default last 30 days
- **Mode**:
  - **Exec dashboard** — single page, compact, scannable, CEO-ready. Default when someone just says "build a report."
  - **Storybook** — multi-page, scroll-animated, fixed dot nav, one narrative arc per section. Use when someone explicitly asks for a "storytelling," "story format," or "presentation-style" report, or when the audience is external/client-facing.

## Step 2 — Pull the data

Via `check-connections` then `multi-execute`, pull for the account(s) and date range:
- Meta: `get-insights` (with breakdowns for age/gender if doing demographics), `get-campaigns`
- Google Ads: `get-google-ads-insights`, `get-google-ads-campaigns`
- TikTok: `get-tiktok-insights`, `get-tiktok-campaigns`
- Snapchat: `get-snapchat-stats`, `get-snapchat-campaigns`
- GA4 (if tying to on-site outcomes): `get-ga4-ecommerce-report`, `get-ga4-channel-grouping`, `get-ga4-conversions`

Pull the previous equivalent period too (e.g. prior 30 days) so the report can show period-over-period change, not just absolute numbers.

## Step 3 — Metrics & funnel per platform

Don't force every platform into the same funnel — use what's actually native to each:

- **Meta/TikTok/Snapchat (social, ecommerce-style funnel)**: Spend, Impressions, Reach, Frequency, Clicks, CTR, CPC, CPM, LPV, Add to Cart, Checkout Initiated, Purchases, Cost/Purchase, Cost/ATC, Cost/Checkout, Video Views. Funnel: Impressions → LPV → ATC → Checkout → Purchase.
- **Google Ads (search/PMax funnel)**: Spend, Impressions, Clicks, CTR, CPC, Conversions, Cost/Conversion, Conversion Rate, Search Impression Share where available.
- **GA4 (site-side)**: Sessions, Users, Conversion Rate, Revenue, Transactions — used to validate platform-reported conversions, not replace them.

Campaign-level table should always include: Spend, primary volume metric (Impressions/Clicks), CTR, Conversions, Cost/Conversion, and a spend-share visual.

## Step 4 — Build the HTML

Read `references/platformance-brand.md` first — it has the full color palette, typography, spacing, and chart color mapping. Non-negotiables:
- Light theme only, never dark
- Title is generic ("Meta Ads Performance Report" / "Paid Media Performance Report" for cross-platform) — never put the raw account name in the title
- Real Chart.js charts for anything trend-based, not static images
- Funnel and demographic breakdowns get their own visual, not just a table

For the storybook mode specifically: one page/section per narrative beat (e.g. overview → channel performance → funnel → creative/demographic insights → recommendations), scroll-triggered animations between sections, fixed dot navigation on the side, single self-contained HTML export.

## Step 5 — Deliver

Save as an HTML file and present it — don't paste raw HTML into the chat. If the report is going to a client, mention it's ready to export/share as-is.
