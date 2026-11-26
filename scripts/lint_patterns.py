#!/usr/bin/env python3
"""CI guard for data/reply-patterns.json: schema completeness plus the verbatim-leak check.

Usage:
  lint_patterns.py [data/reply-patterns.json] [raw/]

Exit 1 on any failure. See genericize.py for the leak check (skipped when raw/ is absent).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # python -I omits the script dir
import genericize  # noqa: E402

CATEGORIES = {"billing_refund", "account_suspension", "support_unreachable", "crash_bug", "feature_request"}
SEVERITIES = {"high", "medium", "low"}
OUTCOMES = {"null", "review_edited_higher", "user_replied_positive"}
STORES = {"google", "apple"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9]+(-[A-Z0-9]+)+$")
SOURCE_RE = re.compile(r"^https://(play\.google\.com/store/apps/details\?id=[\w.]+|apps\.apple\.com/.+)$")
LISTS = ("complaint_signals", "do", "dont")
TEXTS = ("situation", "reply_strategy", "example_case")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def lint(data):
    errs = []
    ids = set()
    for p in data["patterns"]:
        pid = p.get("id", "<missing id>")
        for k in ("id", "store", "category", "severity", "source", "outcome_signal", "captured_at", *LISTS, *TEXTS):
            if k not in p:
                errs.append(f"{pid}: missing field {k!r}")
        if not ID_RE.match(p.get("id", "")):
            errs.append(f"{pid}: id must be UPPER-KEBAB-CASE")
        if p["id"] in ids:
            errs.append(f"{pid}: duplicate id")
        ids.add(p["id"])
        if "category" in p and p["category"] not in CATEGORIES:
            errs.append(f"{pid}: unknown category {p.get('category')!r}")
        if "severity" in p and p["severity"] not in SEVERITIES:
            errs.append(f"{pid}: unknown severity {p.get('severity')!r}")
        if "store" in p and p["store"] not in STORES:
            errs.append(f"{pid}: unknown store {p.get('store')!r}")
        if "outcome_signal" in p and p["outcome_signal"] not in OUTCOMES:
            errs.append(f"{pid}: outcome_signal must be one of {sorted(OUTCOMES)}")
        if "source" in p and not SOURCE_RE.match(p["source"]):
            errs.append(f"{pid}: source must be a store listing URL")
        if "captured_at" in p and not DATE_RE.match(p["captured_at"]):
            errs.append(f"{pid}: captured_at must be YYYY-MM-DD")
        for k in LISTS:
            if not p.get(k):
                errs.append(f"{pid}: {k} must be a non-empty list")
        for k in TEXTS:
            if not (p.get(k) or "").strip():
                errs.append(f"{pid}: {k} must be non-empty text")
    return errs


DOC_FOR = {
    "billing_refund": "skills/billing-refund/SKILL.md",
    "account_suspension": "skills/account-suspension/SKILL.md",
    "support_unreachable": "skills/support-unreachable/SKILL.md",
}
REF_RE = re.compile(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`")


def lint_refs(data, root):
    """Every pattern is referenced from its category's SKILL.md; no doc cites an unknown id."""
    errs = []
    ids = {p["id"] for p in data["patterns"]}
    docs = {}
    for path in set(DOC_FOR.values()) | {"SKILL.md"}:
        full = os.path.join(root, path)
        docs[path] = set(REF_RE.findall(open(full).read())) if os.path.isfile(full) else None
    for p in data["patterns"]:
        doc = DOC_FOR.get(p["category"])
        refs = docs.get(doc) if doc else None
        if refs is None:
            if doc:
                errs.append(f"{doc}: missing")
        elif p["id"] not in refs:
            errs.append(f"{p['id']}: not referenced in {doc}")
    for path, refs in docs.items():
        if refs:
            for unknown in sorted(refs - ids):
                errs.append(f"{path}: references unknown pattern {unknown}")
    return errs


def main():
    patterns_path = sys.argv[1] if len(sys.argv) > 1 else "data/reply-patterns.json"
    raw_dir = sys.argv[2] if len(sys.argv) > 2 else "raw"
    with open(patterns_path) as f:
        data = json.load(f)

    errs = lint(data)
    for e in errs:
        print("LINT", e)
    print(f"lint: {len(data['patterns'])} patterns, {len(errs)} schema errors")

    root = os.path.dirname(os.path.dirname(os.path.abspath(patterns_path)))
    ref_errs = lint_refs(data, root)
    for e in ref_errs:
        print("LINT", e)
    print(f"lint: {len(ref_errs)} reference errors")

    leaks, msg = genericize.check(data, raw_dir)
    print(msg)
    return 1 if (errs or ref_errs or leaks) else 0


if __name__ == "__main__":
    sys.exit(main())
