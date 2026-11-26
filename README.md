# app-review-recovery

**34 reply patterns for 1-3★ app reviews, compiled from 2,863 public developer replies across 10 apps that actually reply.**

An open skill pack for drafting store replies to negative app reviews — for developers, support leads, and AI agents (Claude Code, Cursor, or any assistant that can read a `SKILL.md`).

```
34 patterns   ·   3 categories   ·   10 apps   ·   4 verticals   ·   Google Play   ·   updated 2026-11-25
```

---

## Why

Most "how to reply to bad reviews" advice is generic: be empathetic, be fast, don't argue. This pack is built from what high-reply apps **actually publish**, and from what users posted **afterwards** — including the replies that made things worse.

Three things in the corpus that generic advice misses:

1. **Reply rate is an app trait, not a category trait.** 16 of 26 apps probed never reply at all. Of the 10 that do, two run almost entirely on templates — and users post reviews complaining about it.
2. **The reply never settles a charge or restores an account.** Its whole job is to say who owns the problem and open exactly one route to someone who can act.
3. **Public replies rarely flip a rating.** Most visible "changed my review" edits credit an app update or an offline fix. Measure replies on cases opened, not stars.

## What's inside

```
SKILL.md                         Router: classify the review → sub-skill → four-sentence shape → red lines
skills/
  billing-refund/SKILL.md        11 patterns: unrecognized charges, denied refunds, trials, fees, stuck transfers
  account-suspension/SKILL.md    12 patterns: closures, bans, verification loops, lockouts, recovery
  support-unreachable/SKILL.md   11 patterns: canned-reply backlash, chatbot loops, bugs, accessibility
data/reply-patterns.json         Machine-readable: signals, strategy, do/don't, rewritten example, source listing
guides/
  anti-patterns.md               14 things not to write, and what users did in response
  escalation-playbook.md         Triage by severity, what a reply may commit to, when to stop replying
  rating-recovery.md             How to track rating changes — and why the numbers are weaker than you'd hope
research/
  harvest.md                     Method, corpus table, confidence per claim, official references
  coverage.md                    What's missing: iOS, crash/bug, feature requests, small-developer replies
scripts/
  harvest_via_api.py             Re-run the harvest
  genericize.py                  Fails on any 6-word overlap with the source corpus
  lint_patterns.py               Schema + cross-reference + leak check (run in CI)
```

## Quick start

```bash
git clone https://github.com/hawkmill/app-review-recovery.git
```

Then, in any agent that reads markdown:

- **Claude Code / Claude** — open the repo and say: *"Read `SKILL.md`, then draft a reply to this review: …"*
- **Cursor / any editor agent** — point it at `skills/<category>/SKILL.md` for the category you need.
- **By hand** — start with the anti-pattern table at the end of `guides/anti-patterns.md`.

For programmatic use, `data/reply-patterns.json` is the single source of truth; the `SKILL.md` files are prose around it and are cross-checked against it in CI.

### Example

Review: *"Free trial was a scam, they charged my card the yearly fee and nobody will refund it."*

> Your subscription is billed by Google Play, so the refund has to come from them — request it from the order in Play's purchase history. We've put the steps in `<article on store subscriptions>`. If Play declines and you think that's wrong, tell us and we'll see what we can do on our side.

Pattern: `BILLING-STORE-MANAGED-SUBSCRIPTION-REDIRECT`. It says who owns the money, gives one route, promises nothing.

## Anti-patterns at a glance

| Don't write… | Because | Instead |
|---|---|---|
| The same paragraph under every review | Two apps did; users posted reviews about the template | Name the situation in sentence one |
| "We're always here to help" under a review saying support failed | It is the line users quote back as the problem | `SUP-REPLY-COMPLAINT-ACKNOWLEDGE-PRIOR-FAILURE` |
| "Contact support" under a chatbot complaint | Sends them back to the bot | `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN` |
| The cancellation policy as the answer | Starts an argument you can't win in public | `BILLING-REFUND-DENIED-NO-PUBLIC-VERDICT` |
| Why the account was closed | Confirms an accusation in public | `ACCT-CLOSURE-REGULATORY-BOUNDARY` |
| "Will be refunded within…" | A promise the replier can't keep | A verb that commits to looking |
| A feedback board for an outage | A broken product is not a suggestion | `SUP-REPRO-DETAILS-REQUEST` |

Full list with evidence: `guides/anti-patterns.md`.

## Method, in one paragraph

15,894 public Google Play reviews were pulled through [app-pain-api](https://hawkmill.com) on 2026-11-25; 2,863 are 1-3★ with a developer reply, from 10 apps (fintech, travel, retail, social, streaming, design, maps). Reviews were bucketed by complaint type, a stratified sample of ~340 review–reply pairs was read in full, and recurring reply *behaviours* were written up as patterns. No review or reply is reproduced: a CI check fails if any six-word sequence in the patterns also appears in the corpus. Details, per-claim confidence and the official references are in `research/harvest.md`. Raw data is not redistributed.

### Limitations

- **Google Play only.** No iOS patterns yet — see `research/coverage.md`.
- **Large consumer apps only.** Patterns assume a support desk and a help centre. A solo-developer edition does not exist yet.
- **No outcome data.** `outcome_signal` is `null` on every pattern; public data cannot show that a reply caused a rating change.
- **English, US storefront.**

## Data

The review corpus behind this pack was compiled with **[app-pain-api](https://hawkmill.com)** — app-store review mining with LLM-clustered pain points, share percentages and severity, for both stores. If you want the complaint-type distribution for **your own** category or app, grab a free key at [hawkmill.com](https://hawkmill.com/?src=app-review-recovery#get-key).

## License

Code (`scripts/`) is **MIT**. Content (`SKILL.md`, `skills/`, `data/`, `guides/`, `research/`) is **CC BY 4.0** — share and adapt with attribution to *app-review-recovery*. Reviews and replies remain © their authors and are not included.

## Contributing

Found a pattern that doesn't fit your app, a reply type that's missing, or a claim that's overstated? Open an issue with the pattern id. New patterns need a source listing and must pass `scripts/lint_patterns.py`.

## Star

If this saved you from sending the same paragraph under a hundred reviews, a star is the whole ask. It's what makes the next category (iOS, crash/bug, feature requests) worth compiling.
