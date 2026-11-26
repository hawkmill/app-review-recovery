# Anti-patterns: what not to write, and what users do in response

Every item below was observed in the public developer replies of apps that reply at scale, and — where noted — in what users posted afterwards. Reviewer text is paraphrased, never quoted.

---

## 1. The check to run on every draft

> Could this reply be pasted under a different app's review without editing?

If yes, it is a template. Name the situation in the first sentence before posting anything.

---

## 2. One paragraph under every review

**What it looks like.** The same 30-word apology-plus-"contact support" under hundreds of unrelated 1-star reviews.

**How common.** Two apps in the corpus ran on templates:

| App | Replied 1-3★ reviews | Distinct replies | Share of the single most-used reply |
|---|---|---|---|
| Short-video app | 253 | 5 | 68% |
| Travel booking app | 442 | 41 | 42% |
| Reference: design tool | 130 | 130 | 1% |

**What users do.** They post reviews *about the reply*: that support "keeps auto-replying", that the response is a template, asking the developer not to bother with the standard line. 43 reviews in the corpus complain about canned or automated replies explicitly.

**What it does not do.** Those complaint reviews do not get exceptional likes — their thumbs-up distribution matches other negative reviews (median 3 vs 2). The cost is not virality; it is that every templated reply burns the one chance to route that user to a human.

**Fix.** One sentence that could only have been written for this review. The situation-naming sentence in the four-sentence shape.

---

## 3. "We're always here to help" under a review saying support never helped

**What it looks like.** A stock empathy line and a support URL, posted under a review whose entire content is that support failed.

**What users do.** Edit the review: *"I contacted them many times. Still not resolved."* Some pre-empt it: *"don't respond with 'we are here to help'."*

**Fix.** `SUP-REPLY-COMPLAINT-ACKNOWLEDGE-PRIOR-FAILURE`. Concede the earlier failure by name, offer a *different* entry point, stop.

---

## 4. Sending a bot-loop complainant back to the bot

**What it looks like.** User says the virtual agent repeats wrong answers. Reply: "contact our support team".

**What users do.** Return to the same loop. The edited review says the refund was confirmed by email and never arrived.

**Fix.** `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN`. Name the automation, describe the click that reaches a person.

---

## 5. Ruling on the case in public

**What it looks like.** Restating the cancellation policy, or explaining that the charge was correct, as the reply to a refund dispute.

**Why it backfires.** The store thread becomes an argument you cannot win: the user's account data cannot be shown, so every reply looks like stonewalling, and onlookers see a developer telling a customer they are wrong.

**Fix.** `BILLING-REFUND-DENIED-NO-PUBLIC-VERDICT`. "We'd like to look into this" + one channel + the reference number to bring. No verdict.

---

## 6. Hinting at why an account was closed

**What it looks like.** "Accounts are closed when activity resembles …" followed by the policy category.

**Why it backfires.** It confirms an accusation in public, invites a debate about the policy, and can disclose information about the account.

**Fix.** `ACCT-CLOSURE-REGULATORY-BOUNDARY`. Neutral frame → public/private line → registered-email channel.

---

## 7. Promise-shaped words

**Banned in replies, all categories:** "will be refunded", "within 24 hours", "we'll restore your account", "rest assured".

Use verbs that commit to *looking*: review, look into, check, investigate.

---

## 8. Asking for details in the reply

Card numbers, amounts, dates, passwords, ID documents, full email addresses. Ask for the *registered* email so the user writes in; the details go there.

---

## 9. A survey link for a specific, high-stakes complaint

**What it looks like.** A long review about a failed order or a medical payment. Reply: "we value your thoughts, please complete this survey."

**When a survey is fine.** "The app could be easier to use." When it is not: anything with money, access or safety at stake.

---

## 10. A feedback board for an outage

**What it looks like.** App will not load. Reply: "please post or upvote suggestions on our feedback site."

**Why it backfires.** A broken product is not a suggestion. Users read it as the developer not understanding the review.

**Fix.** `SUP-REPRO-DETAILS-REQUEST` or `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE`. The board is for `SUP-FEATURE-PARKING-DEDICATED-BOARD` only.

---

## 11. A forum as the only destination

**What it looks like.** Every detailed complaint gets the same "please create a post in our community forum".

**What users do.** Some report going there and finding existing threads on their topic locked. One edited their review to say so.

**Fix.** `SUP-COMMUNITY-FORUM-WITH-IN-APP-REPORT`. Prefer the in-app report that routes structured details to the team; offer the forum second.

---

## 12. A social DM as the only channel

"DM us on Instagram" as the sole route excludes anyone not on that network. One user replied in the review that they do not use it. Offer it as an extra, never as the only path.

---

## 13. "Try again later" for a verification loop

Generic retry advice for a specific technical catch (link only opens on the same device, only the newest link is valid). Users came back with edited reviews saying it still failed.

**Fix.** `ACCT-VERIFICATION-LINK-TECHNICAL-CATCH`. Name the catch. If you don't know it, ask for a screen recording.

---

## 14. More than four troubleshooting steps

A wall of update / restart / clear cache / reinstall / check permissions / check connection / reset network. It reads as "we don't know which one it is".

**Fix.** `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE`. Three or four, ordered least to most disruptive, then one escalation.

---

## Quick table

| Draft contains… | Replace with pattern |
|---|---|
| Same paragraph as yesterday's reply | Name the situation (§1, §2) |
| "We're always here to help" under a support complaint | `SUP-REPLY-COMPLAINT-ACKNOWLEDGE-PRIOR-FAILURE` |
| "Contact support" under a bot complaint | `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN` |
| Policy restated as the answer | `BILLING-REFUND-DENIED-NO-PUBLIC-VERDICT` |
| Reason for closure | `ACCT-CLOSURE-REGULATORY-BOUNDARY` |
| "Will be refunded" | A verb that commits to looking (§7) |
| Card number / password / ID request | Registered-email request (§8) |
| Survey link on a money complaint | Order- or case-specific route (§9) |
| Feedback board on an outage | `SUP-REPRO-DETAILS-REQUEST` |
| Forum as the only route | `SUP-COMMUNITY-FORUM-WITH-IN-APP-REPORT` |
| "Try again later" on a loop | `ACCT-VERIFICATION-LINK-TECHNICAL-CATCH` |
| Five or more troubleshooting steps | `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE` |
