# Rating recovery: what a public reply can and cannot do

How to track whether replies are associated with changed ratings, and an honest account of what the corpus shows.

---

## 1. The finding first

**In this corpus, public replies were rarely associated with a visible rating increase.**

A keyword screen of 15,894 reviews found:

| Edited-review type | Found | Had a developer reply visible |
|---|---|---|
| Edited **up** to 4-5★ | 37 | 11 |
| Edited, **still** 1-2★ | 89 | 29 |

Read the numbers carefully before citing them:

- The screen is a regular expression over phrases like "changed my review" / "editing my review". It misses edits that don't use those words and catches some false positives. Treat the counts as orders of magnitude.
- Most upward edits that were readable credited an **app update** ("the update fixed it", "you can do that now") or an **offline resolution** ("they sorted it over the phone"), not the public reply.
- Of the 11 upward edits with a visible reply, 2 credited support getting in touch and resolving things offline. The rest mostly mention app updates — and several of those are complaints *about* the update, so the regex over-counts upward edits.

**What this means.** The reply's job is to be the start of a path that ends in a resolved case. It is not persuasion. A reply written to "win" a star is a reply written for the wrong audience.

---

## 2. Why correlation is all you get

There is no control group. You cannot see what the same user would have done without a reply. Three confounders dominate:

1. **Selection.** Apps reply more to reviews they think they can resolve.
2. **Edits lag.** The reply may be months before the edit; an update in between is often the cause.
3. **Visibility.** The store shows only the current text and rating; the original rating is only known if the user mentions it.

So `outcome_signal` on each pattern is `null` unless a public, observable edit exists. Even then it records an *association*. The pattern library never claims causation, and neither should you in public.

---

## 3. What is observable, and how to observe it

Re-harvest the same app on a schedule and diff review ids.

| Signal | How to detect | Strength |
|---|---|---|
| Review edited to a higher rating | Rating increased for the same review id | Strong association |
| Review edited to a lower rating | Rating decreased for the same review id | Strong association — treat as a reply failure signal |
| User's edited text mentions support contacting them | Keyword on the edited body | Medium; the offline path worked |
| User's edited text mentions an update | Keyword on the edited body | Weak; not reply-attributable |
| Review deleted | Id disappears from the store | Ambiguous |

`scripts/harvest_via_api.py` keeps review ids in the raw output so the diff is possible. Raw ids never leave your machine — the published patterns carry only the store listing.

---

## 4. A tracking loop

1. **Snapshot** the app's reviews (both `recent` and `helpful` sorts).
2. **Reply**, and log the pattern id next to the review id.
3. **Re-snapshot** at 7 and 30 days.
4. **Diff**: rating direction, edit text keywords.
5. **Attribute** conservatively: count only upward edits with no mention of an update as "possibly reply-associated".
6. **Feed back**: patterns whose replies are followed by downward edits go to the top of the anti-pattern list.

Report the result as: "Of N replied reviews, X were later edited upward and Y downward. Z of the upward edits mentioned an update." Do not report a "recovery rate".

---

## 5. What plausibly does help

These are hypotheses consistent with the corpus, not proven:

- **Speed.** 5 of the 29 downward edits with a reply say the problem is still not fixed. A same-day reply that opens a case shortens the window in which that happens.
- **A human at the end.** Both upward edits that credited support describe a person who could act getting in touch.
- **Closing the loop.** Where support resolved a case offline, the edited review said so. Ask support to invite the user to update their review *after* resolution — never as a condition of help.
- **No template.** We did not find an upward edit that credited a public reply's wording. Replies were credited, where at all, as the route to a person.

---

## 6. What to tell stakeholders

- A reply programme is a **support routing** investment with a **public-signal** side effect: prospective users see a developer that responds.
- Expect rating change to come from fixes, not replies. Measure the replies on **cases opened** and **downward edits avoided**, not stars.
- Any tool or agency that promises "we will raise your rating by replying" is selling something the public data does not support.

---

## 7. Red lines

- Never condition support on a rating change.
- Never offer anything in exchange for changing a review. Both stores prohibit it.
- Never ask a user to remove a review. Ask, after resolving, whether they would like to update it.
- Never post a user's support correspondence to prove a point.
