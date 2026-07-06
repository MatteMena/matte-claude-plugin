---
name: matte-campaign-optimizer
description: Optimize live campaigns across Meta, TikTok, Google Ads, and Snapchat via the Matte connector — pacing checks, pausing underperformers, scaling winners, budget reallocation, bid/CPA adjustments. Use this whenever someone asks to optimize a campaign, reallocate budget, pause what's not working, scale a winner, or check pacing. This skill checks for an existing Nerve Workflow Builder automation before doing the work manually — if the account already has a saved workflow that covers the request, use that instead of reimplementing the logic in chat.
---

# Campaign Optimizer

Handles the ongoing tuning that keeps a live account healthy. Read `matte-connector-core` first for the read/write rules — every action here writes to a live spending account.

## Step 1 — Check for an existing Nerve workflow first

Before doing anything manually, check whether a Workflow Builder automation already covers this request (Budget Reallocation, Campaign Monitor, Creative Optimizer, etc). If one exists and is Active:
- Point to it and offer to trigger/check its Runs log instead of rebuilding the logic here
- Don't duplicate a workflow's reallocation math in chat — that's how the same rule ends up maintained in two places and drifts out of sync

Only do the optimization directly in this skill when:
- No workflow covers the specific request, or
- The person explicitly wants a one-off, ad hoc action ("just pause this ad set right now") rather than a recurring automation

## Step 2 — Pull current state

Via `check-connections` then `multi-execute`, pull recent performance (last 7-14 days for tactical decisions, 30 for budget reallocation) plus current structure: campaign/ad set status, budgets, bid settings.

## Step 3 — Common optimization actions

**Pacing**: compare spend-to-date vs. days elapsed in the flight. Flag anything more than ~20% off pace in either direction before touching budgets.

**Pause underperformers**: define "underperforming" against the plan's actual KPI target, not a generic rule — e.g. CPO above target CAC for 7+ days with enough volume to be statistically meaningful, not a single bad day.

**Scale winners**: when scaling budget up, keep it incremental — a common rule of thumb is no more than ~20% budget increase per adjustment for platforms with learning phases (Meta, TikTok), since a bigger jump can reset delivery. State this to the person before applying it, since account-specific limits may differ.

**Budget reallocation**: shift spend from underperforming to overperforming campaigns while keeping total budget constant, mirroring the same 5-step logic as the Nerve Budget Reallocation workflow (fetch → analyze → rank → plan → apply) — but again, check Step 1 first, since this is exactly the kind of thing that workflow likely already automates.

**Bid/CPA adjustments**: only adjust if there's enough conversion volume for the change to be meaningful — flag when there isn't rather than adjusting on thin data.

## Step 4 — Confirm before writing

For every action: state the current value, the proposed new value, and which campaigns/ad sets are affected. Wait for a yes. This applies even to pausing — a paused campaign stops spending immediately, so confirm rather than assuming urgency means skip-the-check.

## Step 5 — Report back

After changes: what was changed, what it was before, and what to watch for over the next few days (e.g. "give the learning phase 3-4 days to stabilize before judging this"). If a change didn't apply cleanly (platform rejected it, hit a minimum budget floor), say so.
