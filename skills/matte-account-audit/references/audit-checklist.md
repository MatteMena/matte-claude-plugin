# Audit Checklist Reference

Go through every category below for the connected platform(s) in scope. Not every item applies to every platform — skip what doesn't apply rather than forcing a finding.

## 1. Account structure & naming
- Duplicate or overlapping campaigns targeting the same audience/objective
- Inconsistent or missing naming convention (can't tell objective/market/date from the name)
- Campaigns left active with $0 recent spend (should be paused or archived)
- Ad sets/ad groups with only one ad (no creative testing happening)

## 2. Budget & pacing
- Campaigns underspending significantly vs. daily budget (targeting too narrow, bid too low, or budget cap misconfigured)
- Campaigns overspending/pacing too fast relative to flight length
- Lifetime budget campaigns close to running out with no plan
- Shared budgets starving high performers to feed low performers

## 3. Bidding & targeting
- Bid strategy mismatched to objective (e.g. lowest-cost bidding on a campaign that needs cost caps)
- Audience too narrow (under ~50k for prospecting on Meta/TikTok, thin keyword volume on Google)
- Broad match keywords with no negative keyword list (Google) — check `get-google-ads-negative-keyword-lists`
- Manual bids that haven't been touched in 30+ days while performance has drifted

## 4. Creative & fatigue
- High frequency (Meta/TikTok) — above ~4-5 in a 7-day window on a prospecting campaign is a fatigue flag
- Same creative running unchanged for 60+ days with declining CTR
- No video in a video-native placement (Reels/TikTok feed)
- Ad copy/creative not localized for the market (e.g. English-only creative running in KSA)

## 5. Tracking & conversions
- Pixel/conversion action not firing (check `get-meta-pixel-stats`, `get-tiktok-pixel-events`, or GA4 events for zero/near-zero recent activity)
- Conversion value not passing through (purchases logging but revenue showing $0)
- GA4 and platform-reported conversions wildly mismatched (check attribution windows before flagging as broken)
- Missing UTM parameters — can't tie platform spend to GA4 sessions/conversions

## 6. Audience overlap & sizing
- Multiple active audiences targeting the same core segment, competing in the same auction
- Lookalike/custom audiences not refreshed in 90+ days
- Retargeting audience windows too long (e.g. 180-day cart abandoners diluting relevance) or too short (missing valid re-engagement)

## 7. Ad approval / policy
- Disapproved or limited-delivery ads still counted as "active" in the account
- Ads stuck in review for an unusually long time
- Policy violations that will recur if the same creative pattern is reused

## 8. Wasted spend
- Search terms report (Google) showing spend on clearly irrelevant queries — check `get-google-ads-search-terms`
- Placements with spend but no conversions over the full lookback window (Meta/TikTok placement breakdowns)
- Geo-targeting spend leaking outside the intended market
- Device breakdown showing one device driving cost with no conversions (may warrant a bid adjustment, not necessarily an exclusion)

## Platform notes
- **Meta / TikTok**: check learning phase status — campaigns stuck in "learning limited" for 2+ weeks aren't optimizing and are a High severity flag.
- **Google Ads**: check `get-google-ads-change-history` for recent changes that correlate with a performance drop before attributing it to something else.
- **GA4**: read-only, so findings here feed into the tracking/attribution section rather than being independently fixable through Matte.
- **Snapchat**: tool coverage is thinner — expect fewer granular findings here than Meta/Google/TikTok.
