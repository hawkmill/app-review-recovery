---
name: billing-refund
description: Reply patterns for app-store reviews about money — unrecognized charges, denied refunds, trial-to-paid conversions, hidden fees, stuck transfers, price display mismatches, order-level disputes and automatic deductions. 11 patterns with signals, do/dont and rewritten examples. Use when a 1-3 star review is about being charged, not refunded, or misled on price.
---

# Billing and refund replies

The rule for this category: **the public reply never settles the charge.** It gets the user to the place where the charge can be seen by someone (or something) that can act on it, and it never predicts the outcome.

## Pick the pattern

| If the review says… | Pattern | Severity |
|---|---|---|
| "charge I never made" / "unknown merchant" | `BILLING-UNRECOGNIZED-CHARGE-INAPP-DISPUTE` | high |
| "free trial" / "charged after trial" / "cancel my subscription" | `BILLING-STORE-MANAGED-SUBSCRIPTION-REDIRECT` | medium |
| "everything costs money now" / "paywalled" | `BILLING-FREE-VS-PAID-BOUNDARY-CLARIFY` | low |
| "hidden fees" / "fees went up" / "rip off" with no specifics | `BILLING-OPAQUE-FEES-ASK-FOR-DETAILS-PRIVATELY` | high |
| money hasn't arrived and it mattered (bill, emergency) | `BILLING-DELAYED-TRANSFER-URGENCY-PLUS-CAUSE` | high |
| "instant" option did not arrive instantly | `BILLING-STUCK-INSTANT-PAYMENT-SECOND-CHANCE` | high |
| "they wouldn't refund me" / cancellation policy dispute | `BILLING-REFUND-DENIED-NO-PUBLIC-VERDICT` | high |
| price shown ≠ price charged | `BILLING-PRICE-DISPLAY-MISMATCH-SPLIT-ROUTING` | high |
| charge belongs to one order (double charge, delivery fee) | `BILLING-ORDER-LEVEL-CHARGE-DEEP-LINK-PATH` | medium |
| a feature took money automatically and it cost them something real | `BILLING-AUTOMATIC-DEDUCTION-NAME-THE-STAKES` | high |
| credit or voucher will not apply at checkout | `BILLING-UNUSED-CREDIT-ESCALATE-WITH-REFERENCE` | medium |

## Three moves that separate good from bad replies here

**1. Say who owns the money problem.** If the app store billed it, the developer cannot refund it. Where this boundary was blurred, users came back saying both the developer and the store had refused and they were stuck in the middle. Say in sentence one that the store manages the subscription, then give the store's refund flow.

**2. Move specifics off the thread.** "Tell me which fees, from your registered email" does three things: it gets the right account, it stops a public argument, and it signals a human will look. Never ask for amounts, card details or dates in the reply itself.

**3. Match the stakes.** A stuck transfer covering a hospital bill and a $3 delivery fee are not the same reply. The high-severity patterns all open by naming the concrete consequence ("stranded at a gas station", "cost you money for food") before anything about process. Generic empathy lines on high-stakes complaints read as dismissal.

## When the review is really two reviews

Price complaints often contain a product bug and a charge dispute at once (price display hid the total; booking got charged anyway). Answer both in separate sentences: feedback routed to the product team, the specific charge routed to support. Reply only to one and the user edits the review to say you ignored the other.

## Never

- Give an ETA on a refund or transfer.
- Say the charge was valid or the refund was correctly denied.
- Restate the cancellation policy as the whole reply.
- Send the same paragraph to every refund review (the most common failure in the corpus — see `guides/anti-patterns.md` §2).

## Examples

All rewritten; no original text. Sources are the store listings on each pattern.

**Unrecognized charge** → "If you see a payment you don't recognize, you can report it from the transaction screen in the app. If anything about that review is unclear afterwards, write to us at `<support address>` and we'll take another look."

**Trial converted, store-billed** → "Your subscription is billed by Google Play, so the refund has to come from them — you can request it from the order in Play's purchase history. We've put the steps in `<article on store subscriptions>`. If Play declines and you think that's wrong, tell us and we'll see what we can do on our side."

**Stuck transfer with consequences** → "Getting money there for a bill and having it sit pending is the last thing you need. Timing on that route depends on the intermediary bank and we can't speed it from here, but we can look at this specific transfer — send your registered email to `<address>` and a specialist will check it today."

**Price mismatch** → "Showing one price and charging another isn't acceptable, and we've passed your screenshot detail to the team that owns checkout. For the charge itself, open `<support URL>` with booking `<reference>` and an agent will review it."
