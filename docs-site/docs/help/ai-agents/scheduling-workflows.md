---
id: scheduling-workflows
title: Schedule a workflow
sidebar_position: 4
---

# Schedule a workflow

Run a workflow automatically every day or on chosen days of the week.

---

## Set a schedule

1. Open the workflow and go to the **Schedule** tab.
2. Turn the **Status** toggle on: *"Active — schedule will run"*.
3. Choose a **Frequency**:
   - **Daily**: every day, or
   - **Weekly**: on the **Days** you tick (Su–Sa).
4. Set the **Time** (hour, minute, AM/PM) and **Timezone**.
5. Click **Save Schedule**.
6. Make sure the workflow itself is **Active** (top-bar **Activate** button). A workflow still in **Draft** won't run on schedule, and the Schedule tab warns you.

The workflow card then shows the schedule, for example *Daily · 8:00 AM · Asia/Karachi*.

---

## How scheduled runs work

- **Runs start at the top of the hour.** Nerve checks schedules once an hour, shortly after :00, and runs workflows due that hour in your chosen timezone. The minutes you set are ignored: 8:00 and 8:45 both run shortly after 8:00.
- **A workflow runs at most once every 23 hours**, even if the schedule would allow more.
- Scheduled runs appear in **Run History** with the trigger **Scheduled**.
- Scheduled runs use credits just like manual runs, and need an active plan with enough credits.

---

## Pause a schedule

Turn the **Status** toggle off (*"Inactive — schedule paused"*) and click **Save Schedule**, or click **Deactivate** on the workflow.

---

## Common questions

**Can I run a workflow hourly or monthly?**
Not at the moment. Only **Daily** and **Weekly** are available.

**My workflow didn't run at the scheduled time.**
Check that:
- the **Status** toggle is on and the workflow is **Active** (not Draft),
- the workflow didn't already run in the previous 23 hours,
- your plan is active and you have credits,
- all source platforms are still connected.
