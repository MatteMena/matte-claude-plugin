---
id: running-workflows
title: Run workflows and view results
sidebar_position: 3
---

# Run workflows and view results

---

## Run a workflow

1. Open the workflow from **AI Agents** → **Workflows**.
2. Click **Run** in the top bar.
3. The steps run in order. You can watch each step's progress live on the **Runs** tab.

You can keep editing the workflow while it runs; your edits apply to the next run.

:::info You can close your browser
Workflows run on Nerve's servers. Closing the tab or browser **doesn't stop the run**. When you reopen the workflow, it reconnects and shows the latest progress.
:::

### Stop a run
Click **Stop**. Steps that hadn't started are marked **Skipped**. You're notified by email when a run is stopped.

### Run it again
After a run finishes, click **Run Again**.

---

## The Runs tab

### Current Run
Each step has a card showing its status: **Running…**, **Completed**, **Failed**, **Skipped** or **Pending**.

- **View output** / **Hide output**: see what the AI produced in that step.
- **▶ Run**: run just that one step.
- **↻ Retry**: rerun a failed step.

When you run a single step, the AI still has the results of the earlier steps in that run.

### Run History
A table of past runs, filterable by **All**, **Completed**, **Failed**, **Cancelled** or **Running** (use **Prev** / **Next** to page).

| Column | Meaning |
|---|---|
| Start date / Complete date | When the run started and finished |
| Status | Completed, Failed, Cancelled or Running |
| Trigger | **Manual** (you clicked Run) or **Scheduled** |
| Version | Which workflow version ran |
| Duration | How long it took |
| **Credits** | Credits charged for the run |
| Output files | Files the run created |

Click **View run details** to open the **Run Detail** page.

---

## Run Detail page

Shows the **Run Progress** of every step, the data the AI requested and received, and **Files generated** (preview or download).

### Retry a failed run
Click **Retry Run**. Nerve picks up where the run failed and doesn't redo the steps that already completed.

---

## Email reports

If the workflow has an **Email report** destination, each successful run sends an email titled **"*(workflow name)* — report ready"**. It contains an AI summary and a **View full report** or **Open in Matte** button. Recipients don't need a Nerve account.

---

## Credits for workflow runs

- A run is charged **once, when it completes**. The amount appears in the **Credits** column and under **Credits & Billing** → **Transactions** as **Workflow run**.
- **Failed runs are never charged.** The run shows *"N credits waived — not charged"*. Retrying doesn't charge twice.
- If your workspace runs out of credits during a run, it stops with **"Stopped — out of credits"**. Steps that had completed are still charged. Everyone in the workspace gets a *"Workflow stopped — insufficient credits"* email.

See [Credits and top-ups](../billing/credits-and-top-ups.md).

---

## Troubleshooting

| Problem | What to do |
|---|---|
| **Run** is disabled | A source platform isn't connected; see *Missing connections* in [Create a workflow](workflows.md#missing-connections). Viewers can't run workflows. |
| **Run failed** | Open **View run details** to see which step failed and why, then **Retry Run**. Expired connections are a common cause; check **Connect accounts**. |
| **Stopped — out of credits** | [Buy a top-up or upgrade](../billing/credits-and-top-ups.md), then **Retry Run**. |
| No report email arrived | Check the **Email report** destination addresses and spam. Emails are only sent for successful runs. |
