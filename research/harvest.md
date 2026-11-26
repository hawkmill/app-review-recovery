# How the patterns were harvested

Public record of the compilation method, so anyone can judge — or repeat — it.

## 1. Source

Public Google Play store reviews and developer replies, fetched on **2026-11-25** through [app-pain-api](https://hawkmill.com) (`get_app_reviews`, `sort=recent` and `sort=helpful`, up to 10 pages × 50 reviews each). All data is publicly visible on the store listing linked from each pattern.

No Apple App Store reviews were used in this version. iOS harvesting is capped by Apple at roughly 50 reviews per app through this API, which is too thin to compile from. See `coverage.md`.

## 2. App selection

Reply behaviour is an **app-level** trait, not a category trait. Of 26 apps probed, 16 reply to almost no reviews at all (Amazon, Netflix, Airbnb, Venmo, Duolingo and others returned zero developer replies across 900+ reviews each), regardless of sort order.

The 10 apps kept are the ones that reply at scale:

| App | Vertical | Reviews pulled | 1-3★ with a reply |
|---|---|---|---|
| Booking.com | travel | 898 | 442 |
| Walmart | retail / e-commerce | 500 | 386 |
| Cash App | fintech | 959 | 359 |
| Discord | social | 500 | 315 |
| Revolut | fintech | 926 | 288 |
| Expedia | travel | 500 | 258 |
| TikTok | social | 500 | 253 |
| Google Maps | maps | 500 | 228 |
| Spotify | streaming | 979 | 204 |
| Canva | design | 980 | 130 |
| **Total** | | **7,242** | **2,863** |

Corpus-wide, including the non-replying apps: 15,894 reviews, 4,367 with a developer reply, 2,863 of those 1-3★.

The kept reviews are recent-biased by construction: 97% are dated 2026, with a handful back to 2018 surfaced by the `helpful` sort.

## 3. From reviews to patterns

1. **Keyword pre-bucketing** of the 2,863 replied negatives into billing / account / support / crash / feature. Buckets overlap heavily; a refund complaint usually also mentions support.
2. **Stratified reading**: a fixed-seed sample of roughly 8 review–reply pairs per app per bucket (≈340 pairs) was read in full, plus a targeted pass for (a) reviews that complain about the reply itself and (b) reviews that announce a rating change.
3. **Pattern extraction**: recurring *reply behaviours* were written up as strategy + do/dont. Each pattern was then generalised — the app, the user and the wording removed, the behaviour kept.
4. **Leak check**: `scripts/genericize.py` fails if any six-word sequence in a pattern also appears anywhere in the raw corpus (705,032 shingles checked).
5. **Reference check**: `scripts/lint_patterns.py` fails if a pattern is not cited from its category's `SKILL.md`, or a `SKILL.md` cites an id that does not exist.

What is **not** in the dataset: review ids, user names, app-specific URLs from replies (support links are described by shape, not copied), and any verbatim review or reply text. Raw harvests are kept out of the repository.

## 4. What was measured, and how reliable it is

| Claim in this repo | Basis | Confidence |
|---|---|---|
| Reply rate is app-level; 16 of 26 apps never reply | Direct count | High |
| Template share per app (68% / 42% / 1%) | Exact-duplicate count of normalised reply text | High |
| 43 reviews complain about canned/automated replies | Keyword regex; manual read of the matches | Medium (some false positives) |
| Their thumbs-up distribution matches other negatives | Median / P90 comparison | Medium |
| Upward edits rarely follow a visible reply (37 → 11) | Keyword regex on "changed my review" phrases | **Low** — see `guides/rating-recovery.md` |

Where confidence is low, the guides say so in place.

## 5. Reference documents (method only — not reproduced)

- Google Play Console Help — *View and analyze your app's ratings and reviews*: https://support.google.com/googleplay/android-developer/answer/138230
- Google Play — *Developer Policy Center* (ratings, reviews and installs): https://play.google.com/about/developer-content-policy/
- Apple — *Respond to reviews* (App Store Connect Help): https://developer.apple.com/help/app-store-connect/monitor-ratings-and-reviews/respond-to-reviews
- Apple — *App Review Guidelines*: https://developer.apple.com/app-store/review/guidelines/

Store processes and policies change; check the current version before acting on `guides/escalation-playbook.md`.

## 6. Licence and attribution

- Code (`scripts/`): MIT.
- Content (`SKILL.md`, `skills/`, `data/`, `guides/`, `research/`): CC BY 4.0 — attribution to *app-review-recovery*, compiled with [app-pain-api](https://hawkmill.com).

Reviews and developer replies are © their authors and the respective app companies. They were read as evidence and are not redistributed here. Every pattern is a paraphrase at the level of behaviour; if you believe a pattern is too close to your original text, open an issue and it will be reworded or removed.

## 7. Repeating the harvest

```bash
python3 -I scripts/harvest_via_api.py --sort recent  --out raw/harvest-recent.jsonl
python3 -I scripts/harvest_via_api.py --sort helpful --out raw/harvest-helpful.jsonl
python3 -I scripts/lint_patterns.py          # schema + references + verbatim-leak check
```

The API needs a key at `~/.app-pain/api_key` or `$APP_PAIN_API_KEY`; the keyless allowance works for a handful of calls per day. `raw/` is git-ignored. App ids are in `scripts/apps.v0.json`.
