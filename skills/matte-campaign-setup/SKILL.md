---
name: matte-campaign-setup
description: Build and launch campaigns, ad sets/ad groups, and ads on Meta, TikTok, Google Ads, or Snapchat via the Matte connector, starting from an approved media plan or a verbal brief. Use this whenever someone asks to "set up this campaign," "launch this," "build the ad sets," or hands over a media plan (including one built by matte-media-planner) and wants it turned into a live account. This skill only creates things through explicit, staged confirmation — it never fires create calls straight off a plan without the person signing off on structure, budgets, and targeting first.
---

# Campaign Setup

Turns an approved plan into a live campaign. Read `matte-connector-core` first, especially the read/write confirmation rules — this skill is almost entirely write calls, so that section matters more here than anywhere else.

## Step 1 — Get the plan

Either:
- A media plan already built (from `matte-media-planner`, or a client doc) — read the Detail Media Plan tab for structure and budgets, Control Settings for the split logic
- Or a verbal brief given directly in chat

If the brief is vague on anything structural (objective, budget, targeting, flight dates), ask before building anything. Don't infer campaign structure from a half-finished plan.

## Step 2 — Lay out the build plan and confirm

Before calling any `create-*` tool, write out exactly what's about to be built:

- Campaign name, objective, budget (daily or lifetime), flight dates
- Ad set / ad group structure — one per targeting segment or funnel stage, named clearly
- Targeting per ad set — audience, placements, geo
- Ads per ad set — creative assets, copy, format
- Platform-specific settings that matter (bid strategy, delivery type, conversion event)

Show this as a plan and get an explicit yes. This is the single most important step — once campaigns are live and spending, undoing a mistake costs real money, not just a rebuild.

## Step 3 — Build in the right order

Always top-down: campaign → ad set/ad group → ad. Don't create ads before the ad set they belong to exists.

1. `create-*-campaign` — get the campaign ID back before proceeding
2. `create-*-adset` / `create-*-adgroup` — one call per ad set, using the campaign ID
3. `create-*-ad` — one call per ad, using the ad set ID

Use `get-tool-schemas` on each create tool before calling it if you haven't used it recently in this conversation — platform-specific required fields (e.g. Meta's `optimization_goal`, Google's `bidding_strategy_type`) are easy to get wrong from memory.

**Launch state**: build everything paused by default unless the person explicitly says to launch live immediately. Confirm before flipping anything to active — a paused review window catches mistakes before they spend budget.

## Step 4 — Verify after building

After the full structure is created, pull it back (`get-campaigns`, `get-adsets`, `get-ads`) and confirm against the plan from Step 2: right budgets, right targeting, right names, right count of ad sets/ads. Catch a mismatch here, not after it's spent money.

## Step 5 — Report back

Summarize what was built: campaign/ad set/ad names, IDs, budgets, current status (paused/active), and a direct link to the account if the platform supports deep links. If anything in the plan couldn't be built as specified (e.g. an audience too small, a budget below platform minimum), say so clearly rather than silently adjusting it.

## Guardrails

- Never launch live without explicit confirmation
- Never guess a missing required field — ask or check `get-tool-schemas`
- If a create call fails partway through a multi-step build (e.g. ad set created, ad creation fails), stop and tell the person exactly what exists so far rather than retrying blindly or leaving it half-built without saying so
