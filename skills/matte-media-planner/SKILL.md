---
name: matte-media-planner
description: Build agency-grade paid media plans across Meta, TikTok, Google Ads, Snapchat, X, and Programmatic DSP, delivered as a branded Platformance Excel file — not a chat summary. Use this whenever someone asks for a media plan, budget allocation, channel plan, flight plan, or "how should I split my budget across platforms." Always takes a full brief first and summarizes it back for confirmation before building anything. The output is a 5-tab .xlsx: Media Plan Summary, Detail Media Plan, Control Settings, Spec Sheet, and Rationale — built with openpyxl following the exact Platformance formatting spec, never a plain unstyled spreadsheet.
---

# Media Planner

Builds a full paid media plan as a branded Excel deliverable, the way an agency planner would hand it to a client. Read `matte-connector-core` first if any part of the brief needs live account data.

This is a two-part job: **take the brief properly, then build.** Don't skip straight to the spreadsheet off a half-formed request.

## Step 1 — Take the brief

Before building anything, gather (ask only for what's genuinely missing — don't re-ask what's already been said):

- **Client / project / campaign name**
- **Objective**: awareness, traffic, leads, ecommerce sales, app installs, retargeting
- **Total budget**, currency, and **flight period** (start/end or duration)
- **Market(s)** — matters a lot in the Gulf; UAE, KSA, and the wider region price and behave differently
- **Phase strategy** — full-funnel (Awareness + Conversion split) or single-phase. Default assumption if unstated: 40% Awareness / 60% Conversion, but say so explicitly rather than silently assuming it.
- **Channel preference or constraints** — any platform the client wants included, excluded, or already knows they're committed to
- **KPI targets** — target CAC/CPO, ROAS, or volume targets if the client has them (from an RFP, brief doc, or stated goal)
- **Live account context** — if an account is already connected via Matte, pull recent actuals (`check-connections` → insights) to ground the rate assumptions instead of using pure benchmarks

If any account is connected, pull real CPM/CPC/CPA data before defaulting to benchmark rates — see `matte-connector-core` for the pull pattern.

## Step 2 — Summarize the brief back

Before building the file, restate the brief in plain language and confirm it: objective, budget, flight, market, phase split, channel shortlist, and KPI targets. This is the checkpoint — get a yes before spending the build effort. Treat this like an account planner reading the brief back to a client on a call, not a form confirmation.

## Step 3 — Select channels and set assumptions

Pick channels based on objective and market fit, not an even spread:
- Search intent, high purchase intent → Google Search, PMax
- Visual/social discovery, retargeting, broad reach → Meta
- Younger audience, video-first, UGC-style → TikTok
- Incremental low-cost reach in Gulf markets → Snapchat
- App install objective → Google UAC, Apple Search Ads
- Reach/frequency at scale, programmatic efficiency → Programmatic DSP
- Real-time conversation, news-adjacent → X

Set rate assumptions (CPM/CPC/CPI, CTR, conversion rate) per channel — from live account data if connected, otherwise market benchmark ranges, clearly labeled as such. These live in the **Control Settings** tab as blue input cells; nothing else in the workbook should be a hardcoded number where a formula referencing Control Settings will do.

## Step 4 — Build the workbook

Read `references/media-plan-brand-spec.md` in full before writing any code — it has the exact colors, fonts, borders, merged-cell layout, and formula logic. Then use `scripts/build_media_plan.py` as the starting template: it already implements the tab structure and brand system, parameterized by client/budget/channels/rates. Adapt it to the specific brief rather than rewriting from scratch each time.

**Five tabs, in this order:**

1. **Media Plan Summary** — campaign overview grid, budget summary by phase, monthly forecast, KPI framework. No rationale text here — that's its own tab now.
2. **Detail Media Plan** — full line-item plan: phase banners, one row per channel/placement, monthly budget columns, formulas throughout (impressions, clicks, conversions, CPO all calculated, never hardcoded).
3. **Control Settings** — every input: monthly budgets, phase split %, channel split % per phase, rate/CTR/conversion benchmarks, reach factor. Blue font on every input cell. This is what the other tabs reference.
4. **Spec Sheet** — ad specs (format, dimensions/ratio, duration, copy limits, file requirements) for **only the channels actually selected** in Control Settings — don't list specs for channels not in the plan.
5. **Rationale** — one row per selected channel: phase, objective, why it was selected for this market/brief, primary KPI. This is the "why," written like a planner justifying the plan to a client, not a restatement of the spec sheet.

After building: run `scripts/recalc.py <file>.xlsx` (from the `xlsx` skill) to force formula recalculation, and confirm zero formula errors before delivering. Check the phase-split and channel-split validation checks in Control Settings both resolve to 100%.

## Step 5 — Deliver

Save to the output directory, present the file, and don't paste the workbook contents into chat. Use the file naming convention: `[CLIENT_ABBR]_[PRODUCT_SHORT]_MediaPlan_Platformance_[DD_MM_YYYY]_[Version].xlsx`.

Client-facing rule: no "Prepared by Platformance" or agency branding in the delivered file unless this is explicitly for internal use — ask if it's unclear which.
