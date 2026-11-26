#!/usr/bin/env python3
"""Pull store reviews (with developer replies) from app-pain-api into raw/harvest.jsonl.

Usage:
  harvest_via_api.py [--apps apps.json] [--pages 10] [--out raw/harvest.jsonl] [--sleep 0.5]

apps.json: [{"store": "android", "appId": "com.squareup.cash", "vertical": "fintech"}, ...]
Key resolution mirrors app-pain-skill/scripts/mcp_call.sh: $APP_PAIN_API_KEY, else ~/.app-pain/api_key.
Raw output is research material only — never published (see research/harvest.md).
"""
import argparse
import json
import os
import sys
import time
import urllib.request

MCP_URL = os.environ.get("APP_PAIN_MCP_URL", "https://hawkmill.com/mcp")


def api_key():
    key = os.environ.get("APP_PAIN_API_KEY", "")
    if not key:
        path = os.path.expanduser("~/.app-pain/api_key")
        if os.path.isfile(path):
            with open(path) as f:
                key = f.read().strip()
    return key


def call_tool(tool, arguments, key, timeout=170):
    payload = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": tool, "arguments": arguments},
    }).encode()
    headers = {"Content-Type": "application/json",
               "Accept": "application/json, text/event-stream",
               # The edge in front of hawkmill.com returns 403 to urllib's default UA.
               "User-Agent": "curl/8.7.1"}
    if key:
        headers["x-api-key"] = key
    req = urllib.request.Request(MCP_URL, data=payload, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", "replace")
    # Strip SSE framing; keep only data: lines.
    datas = [line[len("data: "):] for line in body.splitlines() if line.startswith("data: ")]
    for raw in datas:
        msg = json.loads(raw)
        if "error" in msg:
            raise RuntimeError(msg["error"])
        result = msg.get("result", {})
        if result.get("isError"):
            raise RuntimeError(result)
        for c in result.get("content", []):
            try:
                return json.loads(c["text"])
            except (KeyError, json.JSONDecodeError):
                continue
    raise RuntimeError("no data payload in response: %r" % body[:200])


def call_reviews(store, app_id, page, sort, key, retries):
    last = None
    for attempt in range(retries + 1):
        try:
            return call_tool("get_app_reviews",
                             {"store": store, "appId": app_id, "page": page, "sort": sort}, key)
        except Exception as e:  # noqa: BLE001 - transient network errors are common here
            last = e
            time.sleep(2 * (attempt + 1))
    raise last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apps", default="apps.v0.json")
    ap.add_argument("--pages", type=int, default=10)
    ap.add_argument("--out", default="raw/harvest.jsonl")
    ap.add_argument("--sleep", type=float, default=0.5)
    ap.add_argument("--sort", choices=["recent", "helpful"], default="recent",
                    help="helpful surfaces far more 1-2 star reviews; use it for reply harvesting")
    ap.add_argument("--retries", type=int, default=3,
                    help="retries per page for transient SSL EOF / resets")
    a = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    apps = json.load(open(os.path.join(here, a.apps)))
    key = api_key()
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)

    # Dedupe is per sort order: the same review id can legitimately appear in both runs.
    seen, written, with_reply = set(), 0, 0
    if os.path.isfile(a.out):
        with open(a.out) as prev:
            for line in prev:
                seen.add(json.loads(line)["rid"])
    with open(a.out, "a") as out:
        for app in apps:
            store, app_id = app["store"], app["appId"]
            got = 0
            limit = app.get("pages", a.pages)
            for page in range(1, limit + 1):
                try:
                    d = call_reviews(store, app_id, page, a.sort, key, a.retries)
                except Exception as e:  # noqa: BLE001 - log and keep going
                    print(f"[warn] {store}/{app_id} p{page}: {e}", file=sys.stderr)
                    break
                reviews = d.get("reviews") or []
                if not reviews:
                    break
                # Pages seen on a previous run are skipped record-by-record; the walk only
                # ends on an empty / short page, so resumed runs still reach the deeper pages.
                fresh = [r for r in reviews if r.get("id") not in seen]
                for r in fresh:
                    rid = r.get("id")
                    if rid in seen:
                        continue
                    seen.add(rid)
                    rec = {
                        "rid": rid, "sort": a.sort,
                        "store": store, "appId": app_id, "vertical": app.get("vertical"),
                        "rating": r.get("rating"), "date": r.get("date"),
                        "version": r.get("version"), "country": r.get("country"),
                        "thumbsUp": r.get("thumbsUp"),
                        "body": r.get("body"), "devReply": r.get("devReply"),
                    }
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    written += 1
                    got += 1
                    if r.get("devReply"):
                        with_reply += 1
                if len(reviews) < 50:
                    break  # last page
                time.sleep(a.sleep)
            print(f"{app.get('vertical','?'):10s} {store}/{app_id:40s} pulled {got}")
    print(f"\ntotal reviews written: {written}  with devReply: {with_reply} "
          f"({with_reply / written:.0%})" if written else "nothing written")


if __name__ == "__main__":
    main()
