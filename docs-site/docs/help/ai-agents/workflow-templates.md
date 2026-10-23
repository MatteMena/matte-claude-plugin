---
id: workflow-templates
title: Workflow templates
sidebar_position: 5
---

# Workflow templates

Templates let you reuse a workflow with different ad accounts, for example the same weekly report for every client.

---

## Use a template

1. Go to **AI Agents** → **Workflows** → **Templates** tab.
2. On a template card, click **Activate workflow**.
3. In the **Activate "*(template name)*"** window, choose **your own account** for each source the template needs.
   - If you haven't connected a platform, its row shows **Connect →**. If you're at your plan limit, it shows **Plan limit reached**.
4. **Activate** becomes clickable once every source has an account. Click it.

A new workflow using your accounts appears under **My Workflows**. You can then edit it, run it or [schedule it](scheduling-workflows.md).

---

## Publish your own template

1. Open a workflow you've built and tested.
2. Click **Publish Template** in the top bar.
3. Enter a **Template Name** and an optional **Description**.
4. Publish.

When you publish, Nerve AI swaps your specific account names for placeholders (such as `{{meta_ads_account}}`) and removes your account connections. Whoever uses the template chooses their own accounts.

---

## Common questions

**Does publishing a template share my data?**
No. Only the instructions and steps are shared, and your account names and connections are removed.

**Who can use templates?**
Members, Admins and Owners.
