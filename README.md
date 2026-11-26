# app-review-recovery

34 patterns for replying to 1-3 star app reviews, taken from 2,863 public developer replies on 10 apps that actually answer their reviews.

It's a skill pack for anyone who has to write store replies: developers, support leads, or an AI agent that can read a `SKILL.md`.

```
34 patterns · 3 categories · 10 apps · Google Play · updated 2026-11-25
```

## Why this exists

Most advice on replying to bad reviews says the same thing: be empathetic, be fast, don't argue. Fine as far as it goes. It doesn't tell you what to write when someone says a charge they never made, or that your chatbot sent them in circles for an hour.

So I went to the source. I pulled the reviews of 26 large apps, kept the ones where the developer had replied, and read what the high-reply apps write, and what users posted afterwards.

Three things stood out.

Replying is an app trait, not a category trait. 16 of the 26 apps never reply at all. Of the 10 that do, two paste the same paragraph under nearly every review, and users have begun posting reviews about the template.

A reply can't settle a charge or restore an account. It can say who owns the problem and open one route to someone who can act. The replies that hold up do that and then stop.

Replies rarely change a rating. Of the "updated my review" edits I could check, most mention an app update. Two credit support getting in touch. Judge a reply by whether it opened a case, not by stars.

## What's inside

```
SKILL.md                         Router: classify the review, pick a sub-skill, follow the four-sentence shape
skills/
  billing-refund/SKILL.md        11 patterns: unrecognized charges, denied refunds, trials, fees, stuck transfers
  account-suspension/SKILL.md    12 patterns: closures, bans, verification loops, lockouts, recovery
  support-unreachable/SKILL.md   11 patterns: canned-reply backlash, chatbot loops, bugs, accessibility
data/reply-patterns.json         Machine-readable: signals, strategy, do/don't, rewritten example, source listing
guides/
  anti-patterns.md               14 things not to write, and what users did in response
  escalation-playbook.md         Triage by severity, what a reply may commit to, when to stop replying
  rating-recovery.md             How to track rating changes, and why the numbers are weaker than you'd hope
research/
  harvest.md                     Method, corpus table, confidence per claim, official references
  coverage.md                    What's missing: iOS, crash/bug, feature requests, small-developer replies
scripts/
  harvest_via_api.py             Re-run the harvest
  genericize.py                  Fails on any 6-word overlap with the source corpus
  lint_patterns.py               Schema, cross-reference and leak check (runs in CI)
```

## Quick start

```bash
git clone https://github.com/hawkmill/app-review-recovery.git
```

Then, in any agent that reads markdown:

- Claude Code or Claude: open the repo and say "Read `SKILL.md`, then draft a reply to this review: …"
- Cursor or another editor agent: point it at `skills/<category>/SKILL.md` for the category you need.
- By hand: start with the table at the end of `guides/anti-patterns.md`.

`data/reply-patterns.json` is the single source of truth. The `SKILL.md` files are prose around it, and CI checks that the two agree.

### Example

Review: "Free trial was a scam, they charged my card the yearly fee and nobody will refund it."

> Your subscription is billed by Google Play, so the refund has to come from them. Request it from the order in Play's purchase history. We've put the steps in `<article on store subscriptions>`. If Play declines and you think that's wrong, tell us and we'll see what we can do on our side.

Pattern: `BILLING-STORE-MANAGED-SUBSCRIPTION-REDIRECT`. It says who owns the money, gives one route, and promises nothing.

## Anti-patterns at a glance

| Don't write | Because | Instead |
|---|---|---|
| The same paragraph under every review | Two apps did. Users noticed and said so. | Name the situation in the first sentence |
| "We're always here to help" under a review saying support failed | It's the line users quote back as the problem | `SUP-REPLY-COMPLAINT-ACKNOWLEDGE-PRIOR-FAILURE` |
| "Contact support" under a chatbot complaint | That sends them back to the bot | `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN` |
| The cancellation policy as the answer | It starts an argument you can't win in public | `BILLING-REFUND-DENIED-NO-PUBLIC-VERDICT` |
| Why the account was closed | It confirms an accusation in public | `ACCT-CLOSURE-REGULATORY-BOUNDARY` |
| "Will be refunded within…" | A promise the person replying can't keep | A verb that commits to looking |
| A feedback board for an outage | A broken product is not a suggestion | `SUP-REPRO-DETAILS-REQUEST` |

The full list, with evidence for each, is in `guides/anti-patterns.md`.

## How it was built

I pulled 15,894 public Google Play reviews through [app-pain-api](https://hawkmill.com) on 2026-11-25. 2,863 of them are 1-3 stars with a developer reply, spread across 10 apps in fintech, travel, retail, social, streaming, design and maps. I bucketed them by complaint type, read a sample of about 340 review-reply pairs in full, and wrote down the reply behaviours that kept coming up.

Nothing is quoted. Every pattern is a description of what the reply did. A check in CI fails if six consecutive words from the source corpus turn up in the patterns.

The per-claim confidence, the corpus table and the official references are in `research/harvest.md`. Raw data isn't redistributed.

### What it doesn't cover

- iOS. There are no App Store patterns yet. See `research/coverage.md`.
- Small apps. Every app in the corpus has a support desk and a help centre. The patterns assume you do too. A solo-developer version doesn't exist.
- Outcomes. `outcome_signal` is `null` on every pattern. Public data can't show that a reply caused a rating change.
- Other languages and storefronts. The sample is English, US.

## Getting your own data

The corpus came out of [app-pain-api](https://hawkmill.com/?src=app-review-recovery#get-key), which mines app-store reviews into clustered pain points for both stores. If you want the complaint mix for your own category or app, there's a free key at [hawkmill.com](https://hawkmill.com/?src=app-review-recovery#get-key).

## License

Code in `scripts/` is MIT. Everything else (`SKILL.md`, `skills/`, `data/`, `guides/`, `research/`) is CC BY 4.0: share and adapt it, with attribution to app-review-recovery. Reviews and replies remain the property of their authors and aren't included.

## Contributing

Found a pattern that doesn't fit your app, a reply type that's missing, or a claim that's overstated? Open an issue and name the pattern id. New patterns need a source listing and have to pass `scripts/lint_patterns.py`.

## A star

If this kept you from pasting the same paragraph under a hundred reviews, a star helps. It's how I'll tell whether the next batch (iOS, crash and bug reports, feature requests) is worth writing.
