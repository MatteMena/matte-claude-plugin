---
id: subscribe-and-payment-methods
title: Subscribe and manage payment methods
sidebar_position: 3
---

# Subscribe and manage payment methods

All billing is on the **Credits & Billing** page. To open it, either:
- click the **credits widget** at the bottom of the sidebar, or
- go to **Settings** → **Billing**.

The page has four tabs: **Plans**, **Credits**, **Transactions** and **Billing history**. Payments are processed securely by **Stripe**; Nerve never sees your full card number.

*Only Owners and Admins can make billing changes.*

---

## Subscribe to a paid plan

Use this if your free trial has already been used, or to start paying straight away.

1. Go to **Credits & Billing** → **Plans**.
2. Click **Subscribe** (or **Resume plan**) on Pro or Agency.
3. In the confirmation window:
   - Optional: click **Have a coupon code?** and enter it.
   - Note: *"This starts a paid subscription. No new free trial."*
4. Click **Continue to Stripe**.
5. Enter your card details on Stripe's secure checkout page and confirm.
6. You're returned to Nerve with *"Subscription activated — your credits are ready…"*

If you leave the Stripe page without paying, you'll see *"Checkout canceled — you have not been charged."*

---

## Add a payment card

You need a saved card to continue after a [free trial](free-trial.md), or to fix a [failed payment](invoices-cancel-and-payment-failure.md#failed-payments).

### From the app
1. Open **Add payment method** from any of these:
   - the trial card on the **Plans** tab,
   - a payment banner at the top of the page,
   - **Billing history** tab → **Payment method** → **+ Add payment method**.
2. Enter your card details. Name, email and phone are optional.
3. Click **Save card**.

### From the Stripe billing portal
Click **Manage billing** at the top of the page. Stripe's portal opens, where you can add or update cards and see invoices.

---

## Manage saved cards

On the **Billing history** tab, under **Payment method**, each card shows as *Visa •••• 4242 · Expires MM/YY*.

- **Make default**: use this card for future charges.
- **X**: remove the card.
  You can't remove your **default** card. Set another card as default first, or manage it in the billing portal.

:::info Cards are shared by billing email
Cards are saved against the billing email. If you own several workspaces with the same email, they share the same saved cards.
:::

---

## Promo and coupon codes

- **During a trial:** enter it in the **Promo code** field on the trial card.
- **When subscribing:** click **Have a coupon code?** in the confirmation window.

---

## Troubleshooting

| Problem | What to do |
|---|---|
| My card was declined | Check the details and that your bank allows online/international payments, or try another card. |
| "Set another card as default before removing this one…" | Click **Make default** on another card first, then remove the old one. |
| I can't see billing buttons | Only Owners and Admins can manage billing. Ask a workspace admin. |
| "Checkout canceled — you have not been charged." | You left the Stripe page. Click **Subscribe** again when you're ready. |
| Paid but the workspace is still locked | Wait about a minute and refresh. If it's still locked, email [hello@mattemena.com](mailto:hello@mattemena.com). |
