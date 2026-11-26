# Coverage: what this library does and does not cover

Honest gap list, so no one applies a pattern outside where it was observed.

## What v0 covers

| Dimension | Coverage | Note |
|---|---|---|
| Store | **Google Play only** | No iOS patterns yet |
| Categories | 3 of 5 planned | billing/refund, account closure/lockout, support-unreachable |
| Reply-rich apps | 10 | Heavily fintech, travel, social; one retailer |
| Languages | English-language reviews (`country=us`) | Other locales not sampled |
| Review sentiment | 1-3★ with a developer reply | Positive reviews with replies were not compiled |
| Time window | 97% dated 2026; oldest 2018 (a handful via `helpful` sort) | Recent-biased by construction |

## Gaps, ranked by cost

### 1. Apple App Store — none

Every pattern is tagged `store: google`. The reply mechanics are similar enough that most strategies transfer (the store cannot DM reviewers on either platform), but Apple-specific things are missing:

- The "Report a concern" flow for reviews that violate Apple's terms.
- Store-managed subscription refunds via Apple's **Report a Problem** — the iOS analogue of `BILLING-STORE-MANAGED-SUBSCRIPTION-REDIRECT`.
- Apple's editorial rules on what a developer may say in a reply.

Why: app-pain-api returns roughly 50 iOS reviews per app at most (Apple's anti-scraping), which is not enough to compile from. Options for v1: harvest iOS over many more apps, or hand-collect from App Store Connect for an app you own.

### 2. Pure crash and bug reports — no dedicated skill

The corpus has plenty of crash complaints (≈930 replied negatives mention a technical fault), but they were folded into `support-unreachable` as two patterns (`SUP-REPRO-DETAILS-REQUEST`, `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE`). A dedicated `crash-bug` skill would want:

- Update-regression complaints ("broke after the update") — very common, and the corpus shows they often get the most likes.
- Device-specific failures (one phone model, one OS version).
- "Known issue, fix shipping in version X" replies — **none observed in this corpus**; would need a different source.

### 3. Feature requests — one pattern

`SUP-FEATURE-PARKING-DEDICATED-BOARD` is the only pattern. Removed-feature backlash ("bring back X"), which drew some of the highest-liked reviews in the corpus (thousands of thumbs-up), deserves its own pattern and probably its own skill.

### 4. Verticals with no reply-rich app found

- **E-commerce beyond Walmart**: Temu replied to 25 of 500; eBay, AliExpress, Amazon effectively zero. Marketplace-specific patterns (seller disputes, item-not-as-described) are missing.
- **Food delivery, ride-hailing**: DoorDash, Uber, Uber Eats returned no or unusable data.
- **Games**: not probed at all.
- **Health, finance outside payments, education, B2B/SaaS**: not probed.

### 5. Small-developer replies — none by construction

The 10 apps are all large consumer products with support organisations. Their replies assume a support desk, a help centre and a feedback board. A solo developer replying to 5 reviews a week needs shorter patterns without a routing step. That version does not exist yet and probably should.

### 6. Outcomes — almost nothing

`outcome_signal` is `null` on all 34 patterns. See `guides/rating-recovery.md` for why and what would change it.

## Bucket sizes in the corpus (keyword, overlapping)

| Bucket | Replied 1-3★ reviews matching | Compiled into |
|---|---|---|
| billing | 936 | 11 patterns |
| crash | 929 | 2 patterns (in support-unreachable) |
| support | 867 | 11 patterns |
| account | 679 | 12 patterns |
| feature | 427 | 1 pattern |
| none of the above | 571 | — |

The 571 uncategorised replies were not read systematically. They are the first place to look for v1 patterns.

## Suggested v1 order

1. Apple App Store (store tag + refund flow + report-a-concern) — biggest gap for anyone shipping on both stores.
2. `feature-request` skill incl. removed-feature backlash — cheap, material is in the corpus.
3. `crash-bug` skill — material is in the corpus; needs the "known issue" reply from elsewhere.
4. Read the 571 uncategorised replies.
5. Non-US locales, starting with a non-English market, to test whether strategies transfer.
