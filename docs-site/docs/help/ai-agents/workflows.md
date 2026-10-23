---
id: workflows
title: Create a workflow
sidebar_position: 2
---

# Create a workflow

A **workflow** is a saved, multi-step AI task, such as "Every Monday, pull last week's Meta and Google Ads performance, flag campaigns over target CPA, and email me a report." You can run it on demand or [schedule it](scheduling-workflows.md).

Go to **AI Agents** → **Workflows** in the sidebar.

---

## The Workflows page

- **My Workflows**: workflows in this workspace. Each card shows its schedule (for example *Daily · 8:00 AM · Asia/Karachi*) and a **Running · Step X/Y** badge while it runs.
- **Templates**: ready-made workflows you can copy. See [Workflow templates](workflow-templates.md).
- **All Categories**: filter by **Optimization**, **Reporting**, **Pacing**, **Creative**, **Targeting**, **CRM Sync** or **Analysis**.

Each card's menu has **Open** and **Delete**.

---

## Create a workflow

1. Click **New workflow**.
2. On **Create Workflow**, fill in:
   1. **Workflow name**: for example "Weekly cross-platform report".
   2. **Category**: Optimization, Reporting, Pacing, Creative, Targeting, CRM Sync or Analysis.
   3. **Define instructions**: describe in plain English what the workflow should do, which metrics matter and what output you want.
   4. **Connected sources**: the platforms and ad accounts it should use (choose the login, then the ad account).
      **Connected destinations**: where results go. For example, **Email report** sends a summary email to the addresses you enter. Recipients don't need a Nerve account.
3. Click **Create workflow**.

Nerve AI turns your instructions into a list of **steps** and opens the builder.

:::tip Writing good instructions
Be specific: date ranges ("last 7 days vs previous 7 days"), thresholds ("CPA above $40"), and the output you want ("a table of campaigns plus 3 recommendations"). Say whether the AI may make changes or should only recommend them.
:::

---

## The workflow builder

The builder has three tabs: **Builder**, **Runs** and **Schedule**.

### Builder tab
- **Connected Sources / Connected Destinations** (left): change the accounts or outputs. After changing sources you'll see *"Sources changed — regenerate to apply."* Click **Regenerate Steps** to update the steps.
- **Steps**: each step is an instruction to the AI agent. You can:
  - edit a step's text ("Describe what the AI agent should do in this step...")
  - **Add Step**
  - **Move up** / **Move down**
  - **Delete step**
- **Generate Steps / Regenerate Steps** rebuilds all steps from your instructions and sources.

### Top bar
| Button | What it does |
|---|---|
| **Save** | Saves your changes |
| **v1, v2…** (version) | Opens **Version History**; click **Restore** to go back to an earlier version |
| **Activate / Deactivate** | Turns the workflow on or off. A workflow must be **Active** for its schedule to run |
| **Publish Template** | Shares the workflow as a template (see [Workflow templates](workflow-templates.md)) |
| **Delete** | Deletes the workflow |
| **Run** / **Run Again** / **Stop** | Runs the workflow now, or stops a running one (see [Run workflows](running-workflows.md)) |

If you click **Run** with unsaved changes, Nerve asks to save first.

---

## Missing connections

If a source platform isn't connected, the builder shows *"⚠ Missing platform connections — this workflow cannot run until the following are resolved"*, and **Run** is disabled (*"Connect required platforms before running this workflow."*).

Connect the platform under **Get started** → **Connect accounts**, then come back and reselect the account in **Connected Sources**.

---

## Who can create workflows

**Members, Admins and Owners** can create, edit, run and delete workflows. **Viewers** can open workflows and see their runs.

---

## Next steps
- [Run workflows and view results](running-workflows.md)
- [Schedule a workflow](scheduling-workflows.md)
