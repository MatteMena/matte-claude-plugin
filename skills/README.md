# Matte Connector — Skills

Four skills for the `matte-claude-plugin` repo. Drop this whole `skills/` folder
into the repo root (same level as `dist/` and `.claude-plugin/`) — Claude Code
auto-discovers any `skills/*/SKILL.md`, no changes needed to `plugin.json`.
Run `claude plugin validate .` after adding to confirm.

## Structure

```
skills/
├── matte-connector-core/          how to use the MatteMena MCP (discovery mode,
│   └── SKILL.md                   read/write rules, per-platform gotchas —
│                                   the other three skills build on this)
│
├── matte-media-planner/           agency-grade media plans, delivered as a
│   ├── SKILL.md                   branded 5-tab Excel file (not a chat reply)
│   ├── references/
│   │   └── media-plan-brand-spec.md   exact Platformance colors/fonts/borders/formulas
│   └── scripts/
│       └── build_media_plan.py        openpyxl generator, edit CONFIG per brief and run
│
├── matte-account-audit/           deep, severity-scored audits of live accounts
│   ├── SKILL.md
│   └── references/
│       └── audit-checklist.md         the 8-category checklist (structure, pacing,
│                                       tracking, overlap, wasted spend, etc.)
│
├── matte-performance-reporting/   HTML storytelling / exec-dashboard reports
│   ├── SKILL.md
│   └── references/
│       └── platformance-brand.md      brand spec for the HTML reports
│
├── matte-campaign-setup/          turns an approved plan into a live campaign
│   └── SKILL.md                       (staged confirmation, paused by default)
│
└── matte-campaign-optimizer/      pacing, pausing, scaling, reallocation
    └── SKILL.md                       checks for an existing Nerve workflow first
```

## Which skill does what

- **matte-connector-core** — not usually invoked directly by a person; it's the
  shared MCP playbook (check-connections → search-tools → multi-execute,
  read/write confirmation rules, Google Ads micros, MCC `loginCustomerId`, etc).
  Read this whenever any of the other three skills touch live account data.
- **matte-media-planner** — "build me a media plan." Takes a full brief,
  summarizes it back for confirmation, then builds the 5-tab Excel deliverable.
- **matte-account-audit** — "audit my account" / "why is performance down."
  Pulls live structure + performance, runs the full checklist, severity-scores
  every finding.
- **matte-performance-reporting** — "build a report" / "show me a dashboard."
  Exec-dashboard or scroll-animated storybook HTML, Platformance-branded.
- **matte-campaign-setup** — "launch this" / "build the ad sets." Takes an
  approved plan (or a verbal brief), lays out exactly what's about to be
  built, confirms, then creates it top-down (campaign → ad set → ad),
  paused by default.
- **matte-campaign-optimizer** — "optimize this account" / "pause what's not
  working" / "reallocate budget." Checks for a matching Nerve Workflow
  Builder automation first so the same logic doesn't get maintained in two
  places; falls back to manual pacing/pause/scale/reallocation only when
  nothing already covers the request.

## Known follow-up

`build_media_plan.py` covers the core structure and formula logic faithfully
but isn't pixel-identical to the original template on every border rule.
Worth generating one real sample plan and checking it against a live brief
before it's in regular rotation.
