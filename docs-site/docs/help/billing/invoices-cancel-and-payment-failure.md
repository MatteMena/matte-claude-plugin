---
id: invoices-cancel-and-payment-failure
title: Invoices, cancelling and failed payments
sidebar_position: 5
---

# Invoices, cancelling and failed payments

---

## Invoices and receipts

Go to **Credits & Billing** → **Billing history**.

| Column | Shows |
|---|---|
| Date | Invoice date |
| Description | **Subscription started**, **Monthly renewal** or **Plan change** |
| Amount | Total charged |
| Status | **Paid**, **Payment due**, **Failed** or **Void** |

Actions:
- **View invoice**: open the invoice on Stripe.
- **PDF**: download it.
- **Retry payment** *(Admins)*: try an unpaid invoice again.
- **Pay on Stripe**: pay an unpaid invoice on Stripe's page.

No invoices yet? *"No invoices yet — they'll appear here after your first subscription payment."*

Each month you'll also get a *"Your plan has been renewed"* email with a link to your billing history. Top-up purchases are listed under **Transactions**.

---

## Cancel your subscription

*Owners and Admins.*

1. Go to **Credits & Billing**.
2. Click **Cancel subscription** at the top of the page.
3. Read the summary: *"You'll keep access and your remaining credits until* (end of billing period)*…"*
4. Click **Cancel subscription** to confirm, or **Keep subscription** to go back.

You can also cancel from **Manage billing** (Stripe's portal).

**What happens next:**
- You keep full access until the end of the billing period. A banner shows *"Your subscription will end on* (date)*…"*
- On that date the workspace is **paused**: every page except **Credits & Billing** is locked, and Nerve AI, workflows and the Claude/ChatGPT connector stop.
- Unused subscription credits expire. **Top-up credits are kept** for when you resubscribe.
- Your connections, workflows, advertiser groups and members are kept.

### Changed your mind?
- **Before the end date:** click **Don't cancel subscription** in the banner.
- **After it ended:** go to **Plans** and click **Subscribe** or **Resume plan**.

---

## Failed payments

If a monthly payment fails:
- Your plan status changes to **Past due**, and Stripe retries the payment automatically.
- **Nerve AI, workflows and the Claude/ChatGPT connector are paused straight away** until it's paid.
- You'll see: *"Your last payment failed. Update your billing details to keep running workflows."*
- We email you a **Payment failed** notice with an **Update Payment Method** button.

**To fix it**, either:
1. Click **Update payment method** in the banner (or **Add payment method** if no card is saved) and add a working card, **or**
2. Go to **Billing history** and click **Retry payment** or **Pay on Stripe** on the unpaid invoice.

Once paid, access returns within about a minute and your monthly credits are refreshed.

If the retry is declined again: *"Payment failed again. Please update your payment method, then try again."*

---

## When your plan is inactive

Your plan is inactive when the trial ends without a card, the subscription is canceled and has ended, a payment has failed, or no plan has been chosen.

**In the Nerve app:** every page except **Credits & Billing** is locked.

**In Claude or ChatGPT:** Nerve tools return a card instead of data:

| Card | Why | Button |
|---|---|---|
| **Plan required** | No plan chosen for this workspace | **View plans** |
| **Trial ended** | The free trial ended without a payment method | **Add payment method** |
| **Subscription canceled** | The subscription was canceled and has ended | **Resubscribe** |
| **Payment failed** | The last payment failed | **Update payment** |

Click the button, fix billing in Nerve, then go back to your chat and click **Continue after upgrading** (or just ask again). Access returns within about a minute.

Your Claude/ChatGPT connection stays in place while the plan is inactive, so you don't need to reconnect.
