# Platformance Media Plan — Excel Brand Spec

Adapted from the verified Platformance production template. This version splits into **five tabs** instead of the earlier four: Rationale is pulled out of the Summary tab into its own, and a Spec Sheet tab is added. Follow this exactly — it's not a style suggestion, it's the deliverable standard.

## 1. Colors

| Hex | ARGB | Usage |
|---|---|---|
| `#0D2137` | `FF0D2137` | Column header rows, Grand Total rows, Subtotal rows, Financial Summary header, section title bars — the primary dark anchor |
| `#1A1A2E` | `FF1A1A2E` | Detail Media Plan header block labels (CLIENT, PROJECT, CAMPAIGN, BUDGET, MARKET, PLATFORMS, DATE) |
| `#1A3A5C` | `FF1A3A5C` | Summary campaign info label cells |
| `#1B6CA8` | `FF1B6CA8` | Section banners (BUDGET SUMMARY, KPI FRAMEWORK, etc.), Control Settings sub-headers |
| `#1E7145` | `FF1E7145` | Phase 1 Awareness banner fill; Awareness label font; Awareness section headers |
| `#C55A11` | `FFC55A11` | Phase 2 Conversion banner fill; Conversion label font; Conversion section headers |
| `#D6E4F0` | `FFD6E4F0` | Alternating even-row fill; input cells (with blue font); highlighted summary values |
| `#E2EFDA` | `FFE2EFDA` | Awareness-phase inputs in Control Settings |
| `#FCE4D6` | `FFFCE4D6` | Conversion-phase inputs in Control Settings |
| `#F2F2F2` | `FFF2F2F2` | Financial Summary data rows, secondary badges |
| `#D9D9D9` | `FFD9D9D9` | CHECK validation rows |

Font colors: white `#FFFFFF` on dark fills, body text `#4A4A4A`, blue `#0000FF` for hardcoded inputs (Control Settings + Rate column), red `#C00000` for Target CAC/CPO output cells, orange `#E26B0A` for monthly CAC targets.

## 2. Typography

Arial everywhere, no exceptions.

| Element | Size | Bold |
|---|---|---|
| Tab main title | 12pt | Yes |
| Header block labels | 10pt | Yes |
| Section banners | 10pt | Yes |
| Phase banner rows | 9pt | Yes |
| Column headers | 8pt | Yes |
| Body data rows | 8pt | Varies |
| Small/rationale text | 7pt | No |

Column headers use `\n` line breaks for two-line labels with wrap text enabled, e.g. `"Rate\n(SAR)"`, `"Est.\nImpressions"`, `"CPO\n(SAR)"`.

## 3. Sheet architecture — five tabs

| Tab | Tab color | Purpose |
|---|---|---|
| **Media Plan Summary** | `#1E7145` | Campaign overview, budget summary by phase, monthly forecast, KPI framework |
| **Detail Media Plan** | `#1B6CA8` | Full line-item plan with monthly budget columns and phase banners |
| **Control Settings** | `#4A4A4A` | All assumption inputs — every other tab references this |
| **Spec Sheet** | `#1B6CA8` | Ad specs per channel, filtered to only channels actually selected |
| **Rationale** | `#1E7145` | Why each selected channel made the plan — one row per channel |

## 4. Border system

| Style | Where |
|---|---|
| Medium | Outer edges of the header block, outer edges of the Summary campaign info grid |
| Thin | All data table cells — column headers, data rows, subtotals, grand totals, financial summary |
| None | Phase banner rows (left/right thin only, no top/bottom); blank spacer rows |

Phase banner rows visually "float" between the column header row and first data row — no top or bottom border, just left/right thin.

## 5. Detail Media Plan tab — structure

**Header block (rows 1–7):** CLIENT, PROJECT, CAMPAIGN, BUDGET, MARKET, PLATFORMS, DATE. Labels `#1A1A2E` fill, white bold 10pt. Values merged, transparent fill, `#1A1A2E` 10pt text. Medium border box around the outer edge only, open interior.

**Row 8:** blank spacer, dash placeholder, ~15pt height, no fill/border.

**Row 9:** column header row, `#0D2137` fill, white bold 8pt, thin border, wrap text, ~41pt height for two-line wrapping.

**Column sequence:** Phase | Platform | Placement/Targeting | Ad Format | Duration | Buying Model | Unit | Rate (SAR) | Est. Impressions | Est. Reach | Est. CTR | Est. Clicks | Conv. Rate | Est. Installs | Est. Orders | CPO (SAR) | Total Budget (SAR) | [monthly columns] | *(2-char spacer col, no fill)* | Month | Paid Budget (SAR) | Forecast Orders | Target CAC (SAR)

**Phase banners:** merged full-width row, `#1E7145` (Awareness) or `#C55A11` (Conversion) fill, white bold 9pt, content like `▶ PHASE 1 — AWARENESS | Brand Launch & Reach | 40% of Monthly Budget | Objective: Reach, Brand Recall`. Left/right thin border only.

**Line items:** one row per channel/placement. Phase label merged vertically down column A in the phase's font color, no fill. Rate column (`#0000FF` blue) references Control Settings. All other metric columns are formulas, never hardcoded.

**Subtotals/Grand Total:** `#0D2137` fill, white bold, thin border all sides, blank spacer row before and after.

**Financial Summary block:** Media Spend (net) → Agency Fee (6%) → VAT (15% on fee) → Grand Total. `#0D2137` header/footer, `#F2F2F2` data rows.

**Notes block:** 6 numbered notes, 7pt, left/right thin border, bottom border closes it. Cover: rate source/market, phase split %, channel split location, forecast source, fee structure, CPI channel logic.

## 6. Media Plan Summary tab — structure

**Campaign info grid (rows 2–7):** `#0D2137` "CAMPAIGN OVERVIEW" title bar, then label/value pairs two per row (Client/Market, Product/Campaign Period, Strategy/Total Net Budget, Awareness Channels/Conv Channels, Primary KPI/Secondary KPI). Labels `#1A3A5C` fill white bold, values alternating `#D6E4F0`/white. Medium border on outer edge, thin internal dividers.

**Budget Summary by Phase:** `#1B6CA8` section banner, `#0D2137` column headers, phase rows in phase font color, `#0D2137` grand total. Columns: Phase | Channels | Media Budget (SAR) | Budget % | Est. Impressions | Est. Clicks | Est. Orders | Avg. CPO (SAR). All formula-linked to Detail Media Plan.

**Monthly Forecast:** same banner treatment, alternating row fills, key cells colored (Total Budget red `#C00000`, Awareness Budget green, Conversion Budget orange, Target CAC warm orange).

**KPI Framework:** `#1B6CA8` banner, `#0D2137` headers, Priority column badges (Primary = `#1E7145` fill white, Secondary = `#F2F2F2`).

No rationale text on this tab — see the Rationale tab.

## 7. Control Settings tab — structure

Renamed from "Control Panel" but same function: every input the workbook depends on lives here, in blue font, nowhere else.

- **Section A — Monthly Paid Budgets:** month | budget | % of total, alternating fill
- **Section B — Phase Budget Split:** Awareness % (`#E2EFDA`/green font) and Conversion % (`#FCE4D6`/orange font) — must sum to 100%, add a CHECK row
- **Section C — Awareness Channel Splits:** per-channel %, `#E2EFDA` fill, CHECK row sums to 100%
- **Section D — Conversion Channel Splits:** per-channel %, `#FCE4D6` fill, CHECK row sums to 100%
- **Section E — Awareness Channel Rates:** CPM rate + CTR per channel
- **Section F — Conversion Channel Rates:** CPM/CPC/CPI rate + conversion rate + CTR per channel (CPI channels: conv rate = 1, CTR = 0)
- **Section G — Forecast KPIs:** monthly CAC/CPO targets, total order targets
- **Section H — Reach Factor:** single input, default 0.45

Instruction row at top: "All blue cells are inputs. All other cells reference these."

## 8. Spec Sheet tab — structure (new)

Not present in the earlier template — built fresh each time, **filtered to only the channels selected** in Control Settings (zero-split channels are omitted entirely, not shown grayed out).

Columns: Channel | Ad Format | Dimensions / Aspect Ratio | Duration / Length | Copy Limits | File Requirements | Notes

Standard specs by channel (use what applies to the formats actually in the plan):

| Channel | Format | Dimensions | Duration | Copy | File |
|---|---|---|---|---|---|
| Meta | Feed | 1:1 or 4:5 | — | Primary text ≤125 chars | JPG/PNG/MP4 |
| Meta | Stories/Reels | 9:16 | ≤60s | — | MP4 |
| TikTok | In-feed | 9:16 | 9–15s ideal | Native/UGC style outperforms polished | MP4 |
| Snapchat | Snap Ad / Story Ad | 9:16 | ≤3s hook | — | MP4 |
| Google Search (RSA) | Text | — | — | 15 headlines ≤30 chars, 4 descriptions ≤90 chars | — |
| Google Display/PMax | Responsive | Multiple ratios | — | Multiple headline/description variants | JPG/PNG/MP4 |
| Google UAC | App promo | Multiple ratios | — | Short headline set | Per Play/App Store specs |
| Apple Search Ads | Text/keyword | — | — | Standard App Store metadata | — |
| Programmatic DSP | Display/Video | Standard IAB sizes | Varies | — | JPG/PNG/MP4 per placement |
| X (Twitter) | Feed | 1:1 or 16:9 | ≤2:20 video | ≤280 chars | JPG/PNG/MP4 |

Header row `#0D2137` fill white bold, thin borders, alternating row fill `#D6E4F0`/white like other data tables.

## 9. Rationale tab — structure (new, split out of Summary)

One row per selected channel, written as a planner's justification, not a restatement of specs.

Columns: Channel | Phase | Objective | Why Selected — [Market] Context | Primary KPI

- Section banner `#1B6CA8`, column headers `#0D2137` white bold
- Phase column colored per phase (green/orange/blue for "Both")
- "Why Selected" column wider, 7pt, plain-language reasoning tied to the actual brief (market behavior, funnel stage, audience fit) — not generic platform marketing copy
- Primary KPI column `#F2F2F2` fill, `#1B6CA8` font

## 10. Formula logic

```
Monthly Channel Budget = Total_Monthly_Budget × Phase_Split% × Channel_Split%
Impressions (CPM)      = (Monthly_Budget / CPM_Rate) × 1000
Reach                  = Est_Impressions × Reach_Factor   (default 0.45)
Clicks (CPM)           = Est_Impressions × CTR
Clicks (CPC)           = Monthly_Budget / CPC_Rate
Orders                 = Est_Clicks × Conv_Rate
Installs (CPI)         = Monthly_Budget / CPI_Rate        (Conv Rate = 1 for these)
CPO                    = IFERROR(Total_Budget / Est_Orders, "—")
Agency Fee             = Media_Spend × 0.06
VAT                    = Agency_Fee × 0.15
Grand Total            = Media_Spend + Agency_Fee + VAT
Phase Split Check      = Awareness% + Conversion%          (must = 1)
Channel Split Check    = SUM(channel %) per phase           (must = 1)
```

Every calculated cell is a formula referencing Control Settings — never a Python-calculated hardcoded number.

## 11. File naming & client-facing rules

```
[CLIENT_ABBR]_[PRODUCT_SHORT]_MediaPlan_Platformance_[DD_MM_YYYY]_[Version].xlsx
```

For client-facing delivery: remove "Prepared by Platformance" and any agency branding, keep the rate disclaimer ("All rates are [market] market benchmarks. Actual CPCs/CPMs subject to auction dynamics."), keep the Control Settings instruction note.

## 12. Delivery checklist

- [ ] Five tabs in order: Media Plan Summary, Detail Media Plan, Control Settings, Spec Sheet, Rationale
- [ ] Arial throughout, no exceptions
- [ ] Every calculated cell is a formula, zero hardcoded results
- [ ] Blue font on every Control Settings input
- [ ] Phase split check = 100%, channel split checks = 100% for each phase
- [ ] Spec Sheet contains only channels with nonzero budget split
- [ ] Rationale has one row per channel actually in the plan, reasoning tied to the real brief
- [ ] Zero formula errors after recalculation (`scripts/recalc.py`)
- [ ] No agency attribution if client-facing
