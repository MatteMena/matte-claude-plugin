"""
Platformance Media Plan builder — 5-tab template (Summary, Detail Plan, Control
Settings, Spec Sheet, Rationale). Adapt CONFIG per engagement and run.

Fill in CONFIG below with the confirmed brief, then:
    python build_media_plan.py output.xlsx
Then recalc with the xlsx skill's scripts/recalc.py before delivering.
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ---------------------------------------------------------------------------
# CONFIG — fill this in per engagement before running
# ---------------------------------------------------------------------------
CONFIG = {
    "client": "CLIENT NAME",
    "project": "Project description",
    "campaign": "Campaign description",
    "budget": 300000,
    "currency": "SAR",
    "market": "KSA",
    "date": "Jul 2026",
    "months": ["Jul-26", "Aug-26", "Sep-26", "Oct-26", "Nov-26", "Dec-26"],
    "phase_split": {"Awareness": 0.40, "Conversion": 0.60},
    "reach_factor": 0.45,
    # channel -> split % within its phase
    "awareness_channels": {"Meta": 0.40, "TikTok": 0.30, "Snapchat": 0.30},
    "conversion_channels": {"Meta": 0.35, "Google Search": 0.30, "Google PMax": 0.20, "TikTok": 0.15},
    # channel -> rate assumptions. model: CPM | CPC | CPI
    "rates": {
        "Meta":           {"model": "CPM", "rate": 35, "ctr": 0.012, "conv_rate": 0.02},
        "TikTok":         {"model": "CPM", "rate": 25, "ctr": 0.010, "conv_rate": 0.015},
        "Snapchat":       {"model": "CPM", "rate": 20, "ctr": 0.008, "conv_rate": 0.0},
        "Google Search":  {"model": "CPC", "rate": 3.5, "ctr": 0.0, "conv_rate": 0.05},
        "Google PMax":    {"model": "CPC", "rate": 2.0, "ctr": 0.0, "conv_rate": 0.03},
    },
    # channel -> {phase, objective, why, primary_kpi} — the brief-specific reasoning
    "rationale": {
        "Meta":          {"phase": "Both", "objective": "Reach + Retargeting", "why": "Fill in market-specific reasoning.", "primary_kpi": "CPO"},
        "TikTok":        {"phase": "Both", "objective": "Reach + Engagement", "why": "Fill in market-specific reasoning.", "primary_kpi": "CTR"},
        "Snapchat":      {"phase": "Awareness", "objective": "Incremental Reach", "why": "Fill in market-specific reasoning.", "primary_kpi": "Reach"},
        "Google Search":  {"phase": "Conversion", "objective": "Purchase Intent", "why": "Fill in market-specific reasoning.", "primary_kpi": "CPO"},
        "Google PMax":    {"phase": "Conversion", "objective": "Cross-network Conversion", "why": "Fill in market-specific reasoning.", "primary_kpi": "ROAS"},
    },
    "client_facing": True,
}

SPEC_LIBRARY = {
    "Meta":            {"format": "Feed / Stories / Reels", "dims": "1:1, 4:5, 9:16", "duration": "\u226460s (Reels/Stories)", "copy": "Primary text \u2264125 chars", "file": "JPG/PNG/MP4"},
    "TikTok":          {"format": "In-feed", "dims": "9:16", "duration": "9\u201315s ideal", "copy": "Native/UGC style outperforms polished", "file": "MP4"},
    "Snapchat":        {"format": "Snap Ad / Story Ad", "dims": "9:16", "duration": "\u22643s hook", "copy": "\u2014", "file": "MP4"},
    "Google Search":   {"format": "Responsive Search Ad", "dims": "\u2014", "duration": "\u2014", "copy": "15 headlines \u226430 chars, 4 descriptions \u226490 chars", "file": "\u2014"},
    "Google PMax":     {"format": "Responsive assets", "dims": "Multiple ratios", "duration": "\u2014", "copy": "Multiple headline/description variants", "file": "JPG/PNG/MP4"},
    "Google UAC":      {"format": "App promo", "dims": "Multiple ratios", "duration": "\u2014", "copy": "Short headline set", "file": "Per store specs"},
    "Apple Search Ads": {"format": "Text/keyword", "dims": "\u2014", "duration": "\u2014", "copy": "Standard App Store metadata", "file": "\u2014"},
    "Programmatic DSP": {"format": "Display/Video", "dims": "Standard IAB sizes", "duration": "Varies", "copy": "\u2014", "file": "JPG/PNG/MP4"},
    "X":               {"format": "Feed", "dims": "1:1, 16:9", "duration": "\u22642:20 video", "copy": "\u2264280 chars", "file": "JPG/PNG/MP4"},
}

# ---------------------------------------------------------------------------
# Style helpers
# ---------------------------------------------------------------------------
NAVY, DARKBLUE, SLATE, ACCENT = "0D2137", "1A1A2E", "1A3A5C", "1B6CA8"
GREEN, ORANGE = "1E7145", "C55A11"
LIGHTBLUE, LIGHTGREEN, LIGHTORANGE, GREY, CHECKGREY = "D6E4F0", "E2EFDA", "FCE4D6", "F2F2F2", "D9D9D9"
INPUT_BLUE, RED, WARM_ORANGE, BODY = "0000FF", "C00000", "E26B0A", "4A4A4A"

thin = Side(style="thin", color="000000")
medium = Side(style="medium", color="000000")
THIN_BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)


def font(size=8, bold=False, color="4A4A4A"):
    return Font(name="Arial", size=size, bold=bold, color=color)


def style_cell(cell, value=None, fill_color=None, font_size=8, bold=False,
               font_color=BODY, border=THIN_BORDER, wrap=False, align="left"):
    if value is not None:
        cell.value = value
    if fill_color:
        cell.fill = fill(fill_color)
    cell.font = font(font_size, bold, font_color)
    if border:
        cell.border = border
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    return cell


def set_widths(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


# ---------------------------------------------------------------------------
# Control Settings tab
# ---------------------------------------------------------------------------
def build_control_settings(wb, cfg):
    ws = wb.create_sheet("Control Settings")
    ws.sheet_properties.tabColor = "4A4A4A"
    ws.merge_cells("A1:C1")
    style_cell(ws["A1"], f"{cfg['client'].upper()} \u2014 MEDIA PLAN ASSUMPTIONS", NAVY, 12, True, "FFFFFF", None)
    ws.merge_cells("A2:C2")
    style_cell(ws["A2"], "All blue cells are inputs. All other cells reference these.", SLATE, 8, False, LIGHTBLUE, None)

    row = 4
    ws.merge_cells(f"A{row}:B{row}")
    style_cell(ws[f"A{row}"], "MONTHLY PAID BUDGETS", ACCENT, 9, True, "FFFFFF", None)
    row += 1
    for i, h in enumerate(["Month", "Paid Budget", "% of Total"]):
        style_cell(ws.cell(row=row, column=1 + i), h, NAVY, 8, True, "FFFFFF")
    month_rows = {}
    for i, m in enumerate(cfg["months"]):
        row += 1
        month_rows[m] = row
        band = LIGHTBLUE if i % 2 == 0 else None
        style_cell(ws.cell(row=row, column=1), m, band, 8, True, BODY)
        c = style_cell(ws.cell(row=row, column=2), round(cfg["budget"] / len(cfg["months"]), 2), band, 8, False, INPUT_BLUE)
        style_cell(ws.cell(row=row, column=3), f"=B{row}/{cfg['budget']}", band, 8, False, BODY)
        ws.cell(row=row, column=3).number_format = "0.0%"
    total_row = row + 1
    style_cell(ws.cell(row=total_row, column=1), "TOTAL", NAVY, 8, True, "FFFFFF")
    style_cell(ws.cell(row=total_row, column=2), f"=SUM(B{row - len(cfg['months']) + 1}:B{row})", NAVY, 8, True, "FFFFFF")
    budget_total_ref = f"'Control Settings'!$B${total_row}"

    row = total_row + 2
    ws.merge_cells(f"A{row}:B{row}")
    style_cell(ws[f"A{row}"], "PHASE BUDGET SPLIT", ACCENT, 9, True, "FFFFFF", None)
    phase_rows = {}
    for phase, pct in cfg["phase_split"].items():
        row += 1
        phase_rows[phase] = row
        band = LIGHTGREEN if phase == "Awareness" else LIGHTORANGE
        pcolor = GREEN if phase == "Awareness" else ORANGE
        style_cell(ws.cell(row=row, column=1), f"{phase} %", band, 8, True, pcolor)
        style_cell(ws.cell(row=row, column=2), pct, band, 8, False, INPUT_BLUE)
        ws.cell(row=row, column=2).number_format = "0%"
    check_row = row + 1
    style_cell(ws.cell(row=check_row, column=1), "CHECK (must = 100%)", CHECKGREY, 8, True, BODY)
    style_cell(ws.cell(row=check_row, column=2), f"=SUM(B{row-1}:B{row})", CHECKGREY, 8, True, BODY)
    ws.cell(row=check_row, column=2).number_format = "0%"

    def channel_split_block(title, channels, band, header_color, start_row):
        r = start_row
        ws.merge_cells(f"A{r}:B{r}")
        style_cell(ws[f"A{r}"], title, header_color, 9, True, "FFFFFF", None)
        rows = {}
        for ch, pct in channels.items():
            r += 1
            rows[ch] = r
            style_cell(ws.cell(row=r, column=1), ch, band, 8, True, BODY)
            style_cell(ws.cell(row=r, column=2), pct, band, 8, False, INPUT_BLUE)
            ws.cell(row=r, column=2).number_format = "0%"
        r += 1
        style_cell(ws.cell(row=r, column=1), "CHECK (must = 100%)", CHECKGREY, 8, True, BODY)
        first = r - len(channels)
        style_cell(ws.cell(row=r, column=2), f"=SUM(B{first}:B{r-1})", CHECKGREY, 8, True, BODY)
        ws.cell(row=r, column=2).number_format = "0%"
        return rows, r

    row = check_row + 2
    aware_rows, row = channel_split_block("AWARENESS CHANNEL SPLITS", cfg["awareness_channels"], LIGHTGREEN, GREEN, row)
    row += 2
    conv_rows, row = channel_split_block("CONVERSION CHANNEL SPLITS", cfg["conversion_channels"], LIGHTORANGE, ORANGE, row)

    row += 2
    ws.merge_cells(f"A{row}:C{row}")
    style_cell(ws[f"A{row}"], "CHANNEL RATES & BENCHMARKS", ACCENT, 9, True, "FFFFFF", None)
    row += 1
    for i, h in enumerate(["Channel", "Rate", "CTR", "Conv. Rate"]):
        style_cell(ws.cell(row=row, column=1 + i), h, NAVY, 8, True, "FFFFFF")
    rate_rows = {}
    for i, (ch, r) in enumerate(cfg["rates"].items()):
        row += 1
        rate_rows[ch] = row
        band = LIGHTBLUE if i % 2 == 0 else None
        style_cell(ws.cell(row=row, column=1), f"{ch} ({r['model']})", band, 8, True, BODY)
        style_cell(ws.cell(row=row, column=2), r["rate"], band, 8, False, INPUT_BLUE)
        style_cell(ws.cell(row=row, column=3), r["ctr"], band, 8, False, INPUT_BLUE)
        ws.cell(row=row, column=3).number_format = "0.0%"
        style_cell(ws.cell(row=row, column=4), r["conv_rate"], band, 8, False, INPUT_BLUE)
        ws.cell(row=row, column=4).number_format = "0.0%"

    row += 2
    ws.merge_cells(f"A{row}:B{row}")
    style_cell(ws[f"A{row}"], "REACH FACTOR", ACCENT, 9, True, "FFFFFF", None)
    row += 1
    style_cell(ws.cell(row=row, column=1), "Reach as % of Impressions", LIGHTBLUE, 8, True, BODY)
    style_cell(ws.cell(row=row, column=2), cfg["reach_factor"], LIGHTBLUE, 8, False, INPUT_BLUE)
    ws.cell(row=row, column=2).number_format = "0%"

    set_widths(ws, {"A": 26, "B": 16, "C": 14, "D": 14})
    return {
        "budget_total_ref": budget_total_ref,
        "phase_rows": phase_rows,
        "aware_rows": aware_rows,
        "conv_rows": conv_rows,
        "rate_rows": rate_rows,
        "reach_factor_row": row,
        "month_rows": month_rows,
    }


# ---------------------------------------------------------------------------
# Detail Media Plan tab
# ---------------------------------------------------------------------------
def build_detail_plan(wb, cfg, cs_refs):
    ws = wb.create_sheet("Detail Media Plan")
    ws.sheet_properties.tabColor = ACCENT

    header_fields = [("CLIENT", cfg["client"]), ("PROJECT", cfg["project"]), ("CAMPAIGN", cfg["campaign"]),
                      ("BUDGET", f"{cfg['budget']:,} {cfg['currency']}"), ("MARKET", cfg["market"]),
                      ("PLATFORMS", ", ".join(list(cfg["awareness_channels"]) + list(cfg["conversion_channels"]))),
                      ("DATE", cfg["date"])]
    for i, (label, value) in enumerate(header_fields, start=1):
        style_cell(ws.cell(row=i, column=1), label, DARKBLUE, 10, True, "FFFFFF", None)
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=3)
        style_cell(ws.cell(row=i, column=2), value, None, 10, False, DARKBLUE, None)
    # medium outer box
    ws["A1"].border = Border(top=medium, left=medium)
    for r in range(2, 7):
        ws.cell(row=r, column=1).border = Border(left=medium)
    ws["A7"].border = Border(bottom=medium, left=medium)

    columns = ["Phase", "Platform", "Placement / Targeting", "Ad Format", "Duration", "Buying\nModel", "Unit",
               "Rate\n(SAR)", "Est.\nImpressions", "Est.\nReach", "Est.\nCTR", "Est.\nClicks", "Conv.\nRate",
               "Est.\nOrders", "CPO\n(SAR)", "Total Budget\n(SAR)"] + cfg["months"]
    header_row = 9
    for i, h in enumerate(columns, start=1):
        c = style_cell(ws.cell(row=header_row, column=i), h, NAVY, 8, True, "FFFFFF", wrap=True, align="center")
    ws.row_dimensions[header_row].height = 41

    def phase_block(phase, channels, phase_color, phase_fill, start_row, budget_pct_ref):
        banner_row = start_row
        last_col = get_column_letter(len(columns))
        ws.merge_cells(start_row=banner_row, start_column=1, end_row=banner_row, end_column=len(columns))
        obj = "Reach, Brand Recall, Video Views" if phase == "Awareness" else "Purchases, Leads, ROAS"
        style_cell(ws.cell(row=banner_row, column=1),
                   f"\u25b6  PHASE {'1' if phase == 'Awareness' else '2'} \u2014 {phase.upper()}  |  "
                   f"{budget_pct_ref}% of Monthly Budget  |  Objective: {obj}",
                   phase_fill, 9, True, "FFFFFF", border=Border(left=thin, right=thin))
        r = banner_row
        first_data_row = r + 1
        for ch in channels:
            r += 1
            style_cell(ws.cell(row=r, column=2), ch, None, 8, True, BODY)
            for col in range(3, len(columns) + 1):
                style_cell(ws.cell(row=r, column=col), None, None, 8, False, BODY)
            rate_row = cs_refs["rate_rows"].get(ch)
            rate_ref = f"'Control Settings'!$B${rate_row}" if rate_row else 0
            model = cfg["rates"].get(ch, {}).get("model", "CPM")
            style_cell(ws.cell(row=r, column=8), f"={rate_ref}" if rate_row else "n/a", None, 8, False, INPUT_BLUE)
        if channels:
            ws.merge_cells(start_row=first_data_row, start_column=1, end_row=r, end_column=1)
            style_cell(ws.cell(row=first_data_row, column=1), phase, None, 8, False, phase_color)
        subtotal_row = r + 1
        ws.merge_cells(start_row=subtotal_row, start_column=1, end_row=subtotal_row, end_column=7)
        style_cell(ws.cell(row=subtotal_row, column=1), f"{phase.upper()} PHASE \u2014 SUBTOTAL", NAVY, 8, True, "FFFFFF")
        if channels:
            style_cell(ws.cell(row=subtotal_row, column=16), f"=SUM(P{first_data_row}:P{r})", NAVY, 8, True, "FFFFFF")
        return subtotal_row + 2  # leaves one blank spacer row

    row = header_row + 1
    row = phase_block("Awareness", list(cfg["awareness_channels"]), GREEN, GREEN,
                       row, round(cfg["phase_split"]["Awareness"] * 100))
    row = phase_block("Conversion", list(cfg["conversion_channels"]), ORANGE, ORANGE,
                       row, round(cfg["phase_split"]["Conversion"] * 100))

    grand_total_row = row
    ws.merge_cells(start_row=grand_total_row, start_column=1, end_row=grand_total_row, end_column=7)
    style_cell(ws.cell(row=grand_total_row, column=1), "GRAND TOTAL \u2014 ALL PHASES", NAVY, 10, True, "FFFFFF")

    set_widths(ws, {"A": 21.7, "B": 18, "C": 33.2, "D": 25.9, "E": 15.5, "F": 17.9, "G": 7,
                     "H": 8, "I": 14, "J": 12, "K": 7, "L": 11, "M": 9, "N": 10, "O": 10, "P": 14.7})
    return {"grand_total_row": grand_total_row}


# ---------------------------------------------------------------------------
# Media Plan Summary tab
# ---------------------------------------------------------------------------
def build_summary(wb, cfg):
    ws = wb.create_sheet("Media Plan Summary")
    ws.sheet_properties.tabColor = GREEN
    ws.merge_cells("A2:H2")
    style_cell(ws["A2"], "CAMPAIGN OVERVIEW", NAVY, 10, True, "FFFFFF", border=Border(top=medium, left=medium, right=medium))

    fields = [("Client", cfg["client"], "Market", cfg["market"]),
              ("Product", cfg["project"], "Campaign Period", cfg["date"]),
              ("Strategy", "Full-funnel Awareness + Conversion", "Total Net Budget", f"{cfg['budget']:,} {cfg['currency']}"),
              ("Awareness Channels", ", ".join(cfg["awareness_channels"]), "Conv Channels", ", ".join(cfg["conversion_channels"])),
              ("Primary KPI", "CPO", "Secondary KPI", "CTR")]
    for i, (l1, v1, l2, v2) in enumerate(fields):
        r = 3 + i
        band = LIGHTBLUE if i % 2 == 0 else None
        style_cell(ws.cell(row=r, column=1), l1, SLATE, 8, True, "FFFFFF")
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        style_cell(ws.cell(row=r, column=2), v1, band, 8, False, BODY)
        style_cell(ws.cell(row=r, column=5), l2, SLATE, 8, True, "FFFFFF")
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=8)
        style_cell(ws.cell(row=r, column=6), v2, band, 8, False, BODY)
    ws.cell(row=7, column=1).border = Border(bottom=medium, left=medium)

    row = 9
    ws.merge_cells(f"A{row}:H{row}")
    style_cell(ws[f"A{row}"], "BUDGET SUMMARY BY PHASE", ACCENT, 10, True, "FFFFFF", None)
    row += 1
    for i, h in enumerate(["Phase", "Channels", "Media Budget (SAR)", "Budget %", "Est. Impressions", "Est. Clicks", "Est. Orders", "Avg. CPO (SAR)"]):
        style_cell(ws.cell(row=row, column=1 + i), h, NAVY, 8, True, "FFFFFF")
    for phase, channels in [("Awareness", cfg["awareness_channels"]), ("Conversion", cfg["conversion_channels"])]:
        row += 1
        pcolor = GREEN if phase == "Awareness" else ORANGE
        style_cell(ws.cell(row=row, column=1), phase, None, 8, False, pcolor)
        style_cell(ws.cell(row=row, column=2), ", ".join(channels), None, 8, False, BODY)
        pct = cfg["phase_split"][phase]
        style_cell(ws.cell(row=row, column=3), round(cfg["budget"] * pct, 2), None, 8, False, BODY)
        style_cell(ws.cell(row=row, column=4), pct, None, 8, False, BODY)
        ws.cell(row=row, column=4).number_format = "0%"
    row += 1
    style_cell(ws.cell(row=row, column=1), "GRAND TOTAL", NAVY, 8, True, "FFFFFF")
    style_cell(ws.cell(row=row, column=3), cfg["budget"], NAVY, 8, True, "FFFFFF")

    row += 2
    ws.merge_cells(f"A{row}:H{row}")
    style_cell(ws[f"A{row}"], "KPI FRAMEWORK", ACCENT, 10, True, "FFFFFF", None)
    row += 1
    for i, h in enumerate(["KPI", "Definition", "Measurement Tool", "Priority"]):
        style_cell(ws.cell(row=row, column=1 + i), h, NAVY, 8, True, "FFFFFF")
    for i, (kpi, definition, priority) in enumerate([
        ("CPO", "Cost per Order/Purchase", "Primary"),
        ("CTR", "Click-through Rate", "Secondary"),
        ("Reach", "Unique users reached", "Secondary"),
    ]):
        row += 1
        band = LIGHTBLUE if i % 2 == 0 else None
        style_cell(ws.cell(row=row, column=1), kpi, band, 8, False, BODY)
        style_cell(ws.cell(row=row, column=2), definition, band, 8, False, BODY)
        style_cell(ws.cell(row=row, column=3), "Matte connector / platform insights", band, 8, False, ACCENT)
        pcolor, pfill = ("FFFFFF", GREEN) if priority == "Primary" else (BODY, GREY)
        style_cell(ws.cell(row=row, column=4), priority, pfill, 7, priority == "Primary", pcolor)

    if not cfg["client_facing"]:
        row += 2
        style_cell(ws.cell(row=row, column=1), "Prepared by Platformance", None, 7, False, BODY)

    set_widths(ws, {"A": 18, "B": 22, "C": 16, "D": 12, "E": 15, "F": 12, "G": 12, "H": 14})


# ---------------------------------------------------------------------------
# Spec Sheet tab — filtered to selected channels only
# ---------------------------------------------------------------------------
def build_spec_sheet(wb, cfg):
    ws = wb.create_sheet("Spec Sheet")
    ws.sheet_properties.tabColor = ACCENT
    selected = list(dict.fromkeys(list(cfg["awareness_channels"]) + list(cfg["conversion_channels"])))

    headers = ["Channel", "Ad Format", "Dimensions / Ratio", "Duration / Length", "Copy Limits", "File Requirements"]
    for i, h in enumerate(headers, start=1):
        style_cell(ws.cell(row=1, column=i), h, NAVY, 8, True, "FFFFFF")
    row = 1
    for i, ch in enumerate(selected):
        spec = SPEC_LIBRARY.get(ch)
        if not spec:
            continue
        row += 1
        band = LIGHTBLUE if i % 2 == 0 else None
        vals = [ch, spec["format"], spec["dims"], spec["duration"], spec["copy"], spec["file"]]
        for c, v in enumerate(vals, start=1):
            style_cell(ws.cell(row=row, column=c), v, band, 8, False, BODY, wrap=True)

    set_widths(ws, {"A": 16, "B": 22, "C": 20, "D": 18, "E": 34, "F": 18})


# ---------------------------------------------------------------------------
# Rationale tab
# ---------------------------------------------------------------------------
def build_rationale(wb, cfg):
    ws = wb.create_sheet("Rationale")
    ws.sheet_properties.tabColor = GREEN
    ws.merge_cells("A1:E1")
    style_cell(ws["A1"], "CHANNEL STRATEGY RATIONALE", ACCENT, 10, True, "FFFFFF", None)

    headers = ["Channel", "Phase", "Objective", f"Why Selected \u2014 {cfg['market']} Context", "Primary KPI"]
    for i, h in enumerate(headers, start=1):
        style_cell(ws.cell(row=2, column=i), h, NAVY, 8, True, "FFFFFF")

    row = 2
    selected = list(dict.fromkeys(list(cfg["awareness_channels"]) + list(cfg["conversion_channels"])))
    for i, ch in enumerate(selected):
        r = cfg["rationale"].get(ch)
        if not r:
            continue
        row += 1
        band = LIGHTBLUE if i % 2 == 0 else None
        phase_fill = {"Awareness": LIGHTGREEN, "Conversion": LIGHTORANGE}.get(r["phase"], LIGHTBLUE)
        style_cell(ws.cell(row=row, column=1), ch, band, 8, True, BODY)
        style_cell(ws.cell(row=row, column=2), r["phase"], phase_fill, 8, False, BODY)
        style_cell(ws.cell(row=row, column=3), r["objective"], band, 8, False, BODY)
        style_cell(ws.cell(row=row, column=4), r["why"], band, 7, False, BODY, wrap=True)
        style_cell(ws.cell(row=row, column=5), r["primary_kpi"], GREY, 8, False, ACCENT)

    set_widths(ws, {"A": 16, "B": 12, "C": 20, "D": 50, "E": 14})


# ---------------------------------------------------------------------------
def main(out_path):
    wb = Workbook()
    wb.remove(wb.active)
    cs_refs = build_control_settings(wb, CONFIG)
    build_detail_plan(wb, CONFIG, cs_refs)
    build_summary(wb, CONFIG)
    build_spec_sheet(wb, CONFIG)
    build_rationale(wb, CONFIG)
    wb._sheets.sort(key=lambda s: ["Media Plan Summary", "Detail Media Plan", "Control Settings",
                                    "Spec Sheet", "Rationale"].index(s.title))
    wb.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "media_plan.xlsx")
