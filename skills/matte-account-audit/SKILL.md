---
name: matte-account-audit
description: Run a deep, severity-scored audit of connected Meta, Google Ads, TikTok, Snapchat, or GA4 accounts — pulls live account structure and performance via the Matte connector and checks it against a full benchmark checklist covering budget/pacing, bidding, targeting, creative fatigue, tracking, audience overlap, and wasted spend. Use this whenever someone asks for an account audit, health check, campaign review, wants to know why performance dropped, or asks "what's wrong with my account." Always pulls real live data first — never audits from memory or assumptions.
---

# Account Audit

Pulls live structure and performance for a connected account and scores every issue found by severity. Read `matte-connector-core` first for the MCP workflow.

## Step 1 — Scope the audit

Confirm before pulling data:
- Which account(s) and platform(s) — if the person says "audit my account" and multiple are connected, ask which
- Date range — default to last 30 days, but pull 90 days too if you need to judge trend, not just a snapshot
- Whether they want everything or a specific angle (e.g. "just look at wasted spend")

## Step 2 — Pull the data

Via `check-connections` then `multi-execute`, pull in parallel:
- Account structure: campaigns, ad sets/ad groups, ads/creatives
- Performance: insights for the date range, broken down by campaign at minimum
- Platform-specific extras where relevant: Google search terms (`get-google-ads-search-terms`), Meta pixel stats, TikTok pixel events, Google Ads change history, Google Ads negative keyword lists

Don't skip the structure pull and go straight to insights — issues like naming chaos, duplicate campaigns, or missing UTM structure only show up in the structure data.

## Step 3 — Run the checklist

Full checklist by category is in `references/audit-checklist.md` — read it before scoring findings. It covers: account structure & naming, budget & pacing, bidding & targeting, creative & fatigue, tracking & conversions, audience overlap & sizing, ad approval/policy, and wasted spend. Go through every category — this is a deep audit, not a spot check.

## Step 4 — Score severity

For every issue found, assign:

| Severity | Meaning |
|---|---|
| **Critical** | Actively burning budget with no return, or tracking is broken (conversions not firing) |
| **High** | Meaningfully hurting performance — e.g. stuck in learning phase for weeks, audience overlap cannibalizing spend |
| **Medium** | Suboptimal but not urgent — e.g. ad fatigue creeping up, slightly loose match types |
| **Low** | Hygiene/best-practice — e.g. inconsistent naming convention |

Where you can, attach a rough $ or % impact estimate (e.g. "search terms audit found 12% of spend going to irrelevant queries over 30 days"). Don't fabricate precision you don't have — say "estimated" when it is.

## Step 5 — Output

Structure the findings as:

1. **Executive summary** — account health in 2-3 sentences, count of issues by severity
2. **Findings table** — issue, severity, affected campaign(s), estimated impact, fix
3. **Quick wins** — things fixable in under 15 minutes with clear upside (pause X, fix negative keyword, raise budget on Y)
4. **Strategic fixes** — bigger changes needing more thought (restructure account, rebuild audiences, fix tracking setup)

Lead with the highest-severity items. Don't bury a critical tracking issue under ten low-severity naming nitpicks.
