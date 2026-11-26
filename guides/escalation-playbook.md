# Escalation playbook: what to settle before you reply

The patterns tell you how to phrase a reply. This guide is about the decisions that come first: which reviews need a human in the loop, what the public reply is allowed to commit to, and when to stop replying.

The channel descriptions are generic — substitute your own support URL, registered-email address, in-app report path and feedback board. The patterns name the *shape* of the route, not the destination.

---

## 1. Triage by severity before drafting

Severity is on every pattern. It decides who writes the reply and how fast.

| Severity | Examples | Who replies | Timing target |
|---|---|---|---|
| **high** | unrecognized charge, account closed, money stuck with a real-world consequence, reply complaint, chatbot loop | A person, with the account/order visible if possible | Same day |
| **medium** | store-billed subscription, verification loop, common crash, accessibility | A person or an agent draft reviewed by a person | Within 2-3 days |
| **low** | paywall objection, feature request, data-quality report | Agent draft, spot-checked | Within a week |

An agent may draft any of these. A person should approve every **high** before it posts — these are the replies that get screenshotted.

---

## 2. What the public reply is allowed to commit to

**Allowed**

- That the case will be *looked at* by someone who can see the account.
- The channel and the information to bring.
- A factual explanation of why a check or policy exists.
- The settings path that fixes something today.

**Not allowed**

- A refund, a credit, or a compensation amount.
- A timeline for a refund, transfer, review, or fix.
- That an account will be restored or a restriction lifted.
- That a feature will ship.
- Who was right.

If the user asks for one of these in the review, the reply acknowledges the request and routes it. The answer is given privately by someone with the authority to give it.

---

## 3. Compensation: where the lines are

Compensation decisions are not made in store replies. Decide them in your support process; the reply only opens the door.

- **Refunds for store-billed purchases** belong to the app store. Say so. Do not route the user to your own support as if you could refund it — that produces a loop where each side says the other owns it.
- **Goodwill credits for service failures** (travel, delivery) are a support decision. The reply routes to a channel where an agent can see the order. Never name an amount publicly.
- **Account-held funds** after a closure: the reply routes to a review channel. It never says when or whether funds will be released.

---

## 4. The one-channel rule

Pick the channel by what the case needs, and give exactly one.

| The case needs… | Route shape | Pattern |
|---|---|---|
| The agent to see a specific order or transaction | Path from the order record to its support chat | `BILLING-ORDER-LEVEL-CHARGE-DEEP-LINK-PATH` |
| Account verification before anything can be discussed | Registered-email address | `BILLING-OPAQUE-FEES-ASK-FOR-DETAILS-PRIVATELY`, `ACCT-CLOSURE-REGULATORY-BOUNDARY` |
| A person, bypassing a bot | The click on the support page that opens a human | `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN` |
| Structured bug details | In-app report | `SUP-COMMUNITY-FORUM-WITH-IN-APP-REPORT` |
| A fresh attempt after support failed | A different link from the one that failed | `SUP-SECOND-ATTEMPT-DEDICATED-LINK` |
| A formal appeal | The review request inside the violation notice | `ACCT-RESTRICTED-BY-ASSOCIATION-REVIEW-REQUEST` |

Giving two or more channels in one reply lowers the chance the user picks the right one.

---

## 5. When to take it offline entirely

Some cases should never get a public reply with content:

- **Legal threats.** ("I'm issuing proceedings.") Acknowledge once, route to your legal or escalations contact, stop.
- **Data-breach or privacy allegations.** Do not confirm, deny or discuss in the thread. Route to the privacy contact. Coordinate the wording with whoever owns that incident.
- **Security researchers or fraud reports with exploit detail.** Reply with a security contact only. Do not engage with the detail.
- **Abusive or harassing reviews.** Report through the store's mechanism. A public reply to abuse is a public argument.
- **Suspected coordinated or fake reviews.** Report to the store. Do not reply.

For all of these, the reply — if any — is one or two sentences: acknowledgement plus a single channel.

---

## 6. Store escalation channels

Both stores have official processes for reviews that violate their rules. Use them instead of replying.

- **Google Play** — report a review from Play Console ("Reply to reviews" → report). Google's policy page on Google Play reviews and the Play Console Help article on replying to reviews describe what counts as a policy violation.
- **Apple App Store** — report a review via App Store Connect ("Ratings & Reviews" → report a concern). Apple's "Report a concern" guidance describes the criteria.

Check the current documentation before relying on either; the processes and criteria change. See `research/harvest.md` §4 for the reference list.

---

## 7. When to stop replying

- **The user has edited the review twice to say it is not fixed.** A third public reply adds nothing. Route once more privately if a channel exists; otherwise leave it.
- **The reply thread has become an argument.** Do not post a rebuttal. onlookers read the last message as the developer's position.
- **The review is about a decision that is final** (a closure after appeal, a refund correctly denied under the terms). Say the outcome is final and where to read the policy, once. Do not re-explain.
- **You have nothing new to give.** If the reply would be the same as your last one, do not post it.

A review with a calm, correct, final reply ages better than one with five replies defending the developer.

---

## 8. Internal handoff: what to log with the reply

For any **high** severity reply, record alongside it:

1. The pattern id used.
2. The channel given.
3. Whether the case was opened internally (ticket id).
4. Whether the user edited the review afterwards, and in which direction.

This is what turns a reply library into a recovery tracker — see `guides/rating-recovery.md`.
