---
name: support-unreachable
description: Reply patterns for reviews where the complaint is about support itself — canned replies, AI chat loops, "nobody got back to me", "don't respond with the same line" — plus technical bugs that need details and accessibility complaints. 11 patterns with signals, do/dont and rewritten examples. Use when a 1-3 star review is about the developer's reply or support, not the product.
---

# "Support is unreachable" replies

This category has a trap: the complaint is about the *previous reply*. Sending the standard reply again is the thing being complained about. 43 reviews in the corpus complain about canned or automated replies by name — several quote the boilerplate back.

## Pick the pattern

| If the review says… | Pattern | Severity |
|---|---|---|
| "don't respond with 'we're here to help'", "you closed the chat" | `SUP-REPLY-COMPLAINT-ACKNOWLEDGE-PRIOR-FAILURE` | high |
| "the chatbot just repeats itself", "I need a human" | `SUP-AI-CHAT-LOOP-ROUTE-TO-HUMAN` | high |
| "nobody contacted me", "how do I even reach you" | `SUP-NO-DM-ON-STORE-STATE-AND-COMPENSATE` | medium |
| blocking bug with no detail | `SUP-REPRO-DETAILS-REQUEST` | medium |
| common crash/lag symptom | `SUP-TROUBLESHOOT-LADDER-THEN-ESCALATE` | medium |
| known symptom with a dedicated article | `SUP-SYMPTOM-NAMED-HELP-ARTICLE` | medium |
| paying subscriber with a problem | `SUP-SUBSCRIPTION-HOLDER-EXPLICIT-INVESTIGATION` | medium |
| "I've contacted you many times" | `SUP-SECOND-ATTEMPT-DEDICATED-LINK` | medium |
| data-quality complaint (wrong route, wrong place) | `SUP-COMMUNITY-FORUM-WITH-IN-APP-REPORT` | low |
| feature request / removed feature | `SUP-FEATURE-PARKING-DEDICATED-BOARD` | low |
| dyslexia, eye strain, screen reader | `SUP-ACCESSIBILITY-WORKAROUND-PLUS-BOARD` | medium |

## Say the limit out loud

Stores do not let developers message reviewers. The replies that worked said so directly: "we can't message you here". That one sentence converts "they're ignoring me" into "here is the one place that works". Always pair it with exactly one channel and a list of what to bring.

## Acknowledge before you route

For reply complaints, the opening must concede that the earlier attempt did not help — in plain words, by name if the store shows a name. The structure is *concede → fresh link → stop*. No "however", no defence of the support team, no restating the hours the team is available.

## For bots: give the click

When the complaint is an automated agent, "contact support" sends them back into the same loop. Describe the specific click that reaches a person (the option on the support page that opens a live agent). If there is no such click, that is a product problem the reply cannot fix; escalate internally and keep the reply short.

## Technical: ask or ladder, not both

Two patterns, pick one:
- **Not reproducible from the review** → ask for device model, app/OS version and what happens on screen. Do not ladle troubleshooting on someone who has not told you what broke.
- **Common symptom** → three or four ordered steps (update → restart → clear cache → reinstall), then one escalation. More than four steps reads as "we don't know".

Name help articles by symptom, not internal title, so they survive a broken link.

## Routing sinks and when they backfire

- **Feedback board** is right for feature requests and wrong for outages — replying to a bug with "post your suggestion" was one of the recurring complaints in the corpus.
- **Survey link** for a long, specific service-failure complaint reads as dismissal. Use it for "the app could be easier" complaints only.
- **Community forum** is acceptable as a second option, never the only one: at least one user in the corpus reported following the forum link and finding every thread on their topic locked.
- **Social DM** as the only channel excludes people who do not use that network.

## Example

Rewritten; no original text.

**Reply complaint** → "Chad — it sounds like our last conversation didn't get this fixed, and that's on us. We'd like to look again with a fresh pair of eyes: `<dedicated link>`. If it's the same answer again, say so there and it gets escalated."

**Chatbot loop** → "Sorry the virtual agent kept giving you the same wrong answer. To reach a person, open `<support URL>`, choose Chat, then pick 'agent' — it skips the bot. Have your booking reference ready and they can see the refund you were promised."

**Blocking bug** → "Sorry you're stuck at sign-in. Could you email `<address>` with your phone model, the app version (Settings → About) and what you see when it freezes? That's what we need to reproduce it."
