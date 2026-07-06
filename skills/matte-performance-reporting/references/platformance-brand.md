# Platformance Brand System

Use this for every HTML report the `performance-reporting` skill produces.

## Theme
- Light theme only, never dark
- Background: `#F5F6FA`
- Canvas/card background: `#FFFFFF`

## Typography
- Primary font: **Gilroy** (fallback: `-apple-system`)
- Numbers/metrics: **DM Mono**
- Never use Inter or Roboto

## Colors
- Primary: `#1D2968`
- Accent: `#4B5BD6`
- Borders: `#E5E7EB`

### Chart color mapping
| Metric | Color |
|---|---|
| Spend | `#3B5BDB` |
| Revenue | `#2DD4BF` |
| Conversions | `#38BDF8` |
| AOV | `#A855F7` |

## Shape & spacing
- Buttons: pill-shaped
- Cards: 12px radius
- Modals: 16px radius
- CTA fill: 135deg gradient, `#1D2968` → `#4B5BD6`

## Tables
- Headers: 11px, weight 600, UPPERCASE only

## Layout rules
- Title is always generic — e.g. "Meta Ads Performance Report" or "Paid Media Performance Report" for cross-platform. Never show the raw ad account name at the top.
- White cards on `#F5F6FA` background, subtle shadows
- Any nav/header accent uses the brand sidebar gradient (`#1D2968` → `#4B5BD6`)

## Standard sections for any report
1. Header/title (generic, per above)
2. KPI summary cards (Spend, primary conversion metric, Cost/Conversion, ROAS if ecommerce)
3. Trend chart(s) — Chart.js, using the color mapping above
4. Funnel visual (platform-appropriate — see SKILL.md Step 3)
5. Campaign breakdown table — Spend, Impressions, CTR, Conversions, Cost/Conversion, spend-share bar
6. Demographic breakdown (age + gender pie charts) — Meta only, via `get-insights` with `breakdowns:["age"]` and `breakdowns:["gender"]`
7. Insights / recommendations — plain-language takeaways, not just repeated numbers
