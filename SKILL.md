---
name: app-review-recovery
description: Draft store replies to 1-3 star app reviews using 34 reply patterns compiled from public developer replies across 10 high-reply Google Play apps. Covers billing/refund disputes, account closure and lockout, and "support is unreachable" complaints. Use when replying to app store reviews, writing developer responses to negative reviews, or reviewing a draft reply before posting.
license: MIT (code) + CC BY 4.0 (content)
---

# App Review Recovery

Reply to negative app-store reviews with patterns taken from what high-reply apps actually publish.

## What this is

- `data/reply-patterns.json` — 34 patterns. Each has the complaint signals that trigger it, the reply strategy, `do` / `dont` lists, one rewritten example, and the store listing it was observed under.
- Three sub-skills with the decision logic: `skills/billing-refund`, `skills/account-suspension`, `skills/support-unreachable`.
- `guides/anti-patterns.md` — what not to write, with the user backlash each one produces.

Patterns are **descriptions of reply behaviour**, not copied text. No review or reply is reproduced verbatim. See `research/harvest.md`.

## Route the review first

Classify by what the user is asking for, not by their tone.

| The review mainly says… | Go to | Frequency in corpus |
|---|---|---|
| I was charged / not refunded / the price was wrong / money is stuck | `skills/billing-refund/SKILL.md` | 11 patterns |
| My account was closed / locked / restricted / I can't get in | `skills/account-suspension/SKILL.md` | 12 patterns |
| Support never answered / it's a bot / don't reply with the same line / a bug I can't get fixed | `skills/support-unreachable/SKILL.md` | 11 patterns |

One review often carries two (a refund dispute **and** "your bot is useless"). Handle the money or account issue first; the support complaint is usually a symptom of it.

Not covered yet: pure crash/bug reports with no support complaint, and feature requests. Route those with `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE` and `SUP-FEATURE-PARKING-DEDICATED-BOARD` and note the gap — see `research/coverage.md`.

## The four-sentence shape

Nearly every effective reply in the corpus fits this order. Drop a sentence when it does not apply; do not add a fifth.

1. **Name their situation.** One clause, in their terms. "Your transfer for a hospital bill is still pending" beats "We're sorry your experience was not satisfactory."
2. **Give the thing only you can give.** The in-app path, the settings screen, the reason a check exists, the store that owns the refund.
3. **One route to a human.** Exactly one. Say what to bring (order number, device model, itinerary).
4. **Stop.** No closing formula. "We're always here to help" under a review that says support never helped is the line users in the corpus most clearly quote back as the problem.

## Red lines (all categories)

- Never promise a refund, a timeline, or that an account will be restored.
- Never state or hint at why an account was closed in public.
- Never ask for card numbers, passwords, IDs or full email addresses in the reply. Ask for the *registered* email so they write in.
- Never reuse one paragraph across unrelated reviews. Two apps in the corpus posted one template under most of their replies; users noticed and said so in later reviews.
- Never rule on who was right about a charge or a policy.

## Before you post

Run `guides/anti-patterns.md` §1 against the draft. If the reply could be pasted under a different app's review without editing, it is a template and needs the situation named.

## What a reply can and cannot do

Public replies rarely flip a rating on their own. In this corpus, most visible "changed my review" edits credited an app update or an offline resolution, not the reply. Treat the reply as the thing that gets the user into a channel where the problem can actually be fixed. `guides/rating-recovery.md` has the method and the limits.

## Data

Compiled from 15,894 public Google Play reviews (4,367 with a developer reply; 2,863 negative ones with a reply) across 10 apps that reply at scale, harvested 2026-11-25 through [app-pain-api](https://hawkmill.com/?src=app-review-recovery#get-key). Source listings are on every pattern.
