---
name: account-suspension
description: Reply patterns for app-store reviews about account closure, bans, restrictions, repeated verification, age and device checks, sign-in code failures and lost access to an old account. 12 patterns with signals, do/dont and rewritten examples. Use when a 1-3 star review says "closed", "locked", "suspended", "banned", "can't log in" or "can't recover".
---

# Account closure and lockout replies

This is the most emotional category in the corpus: the user has lost access to something of theirs (money, contacts, a following, a history). The public reply cannot restore access. It can do exactly three things: explain *why* a check exists, show *where* to go next, and avoid making the user feel accused.

## Pick the pattern

| If the review says… | Pattern | Severity |
|---|---|---|
| "closed for violating policy, nobody told me what" | `ACCT-CLOSURE-POLICY-LINK-PLUS-APPEAL` | high |
| regulated account closed, "no explanation" | `ACCT-CLOSURE-REGULATORY-BOUNDARY` | high |
| "frozen again", same documents requested repeatedly | `ACCT-REPEATED-VERIFICATION-EXPLAIN-WHY` | medium |
| "says my device is rooted / is an emulator" | `ACCT-DEVICE-INTEGRITY-BLOCK-EXPLAIN-AND-FIX` | medium |
| age verification failed for an adult | `ACCT-AGE-VERIFICATION-CORRECT-IN-APP` | medium |
| restricted because of a group/server they were in | `ACCT-RESTRICTED-BY-ASSOCIATION-REVIEW-REQUEST` | high |
| "suspended out of nowhere" (reason is visible in settings) | `ACCT-SUSPENSION-SHOW-WHERE-THE-REASON-IS` | medium |
| sign-in code never arrived | `ACCT-SIGNIN-CODE-NOT-ARRIVING-FALLBACK` | medium |
| can't sign in, probably wrong method | `ACCT-SIGNIN-METHOD-MISMATCH` | low |
| verification link loops | `ACCT-VERIFICATION-LINK-TECHNICAL-CATCH` | medium |
| wants an old account back, lost the email/phone | `ACCT-LOCKED-OUT-OF-OLD-ACCOUNT-IN-APP-REPORT` | high |
| "shadowbanned", no engagement | `ACCT-REACH-DROPPED-VISIBILITY-COMPLAINT` | medium |

## The three-part shape for closures

Replies that stayed calm under abuse all did the same three things, in order:

1. **Neutral frame, one sentence.** Closures follow a review and, for regulated products, legal requirements. No adjectives about the user.
2. **The public/private line.** "We can't discuss the specifics of an account on a public platform." This is the sentence that makes it legitimate to not answer the question they asked.
3. **A channel that can actually see the account.** A registered-email address, an appeal link, the review request inside the violation notice. Not a general help page.

Leaving out (2) makes the reply look evasive. Leaving out (3) makes it final, and the user edits the review to say so.

## What never goes in the reply

- The reason for the closure, even softened ("activity that may resemble…").
- Any confirmation that the user *is* or *is not* "shadowbanned".
- Credentials, old emails, phone numbers. For lost-account recovery, the only correct move is a numbered in-app report path.

## Technical lockouts: name the catch

For verification loops and device blocks, the best replies named the *specific* non-obvious condition — the link only opens on the same phone and profile as the app; only the newest link is valid; the app requires official manufacturer software. Users who received "try again later" came back with edited reviews saying it still failed. If you know the catch, say it; if you don't, ask for a screen recording rather than a description.

## Example

Rewritten; no original text.

**Closure, regulated product** → "Account closures are decided after a review and in line with requirements we have to meet as a regulated company. We can't go into the details of your account on a public page. If you'd like clarification, email `<address>` from the address registered to the account and the team will respond there."

**Age check** → "You can correct your age group in the app: Settings → Account → Confirm Age. Pick card, selfie or ID — if one method fails, tap Retry and choose another. `<help link>` if none of them work."

**Lost old account** → "Recovering an old account has to be done inside the app — we can't do it from a review. Open Profile → Menu → Report a Problem and the team will look at it. We know the wait is frustrating."
