#!/usr/bin/env python3
"""Verbatim-leak check: no pattern text may share a word shingle with the raw review corpus.

Usage:
  genericize.py [data/reply-patterns.json] [raw/]

Exit 1 when a shingle matches. Raw corpus is optional: without it only the pattern file is
loaded and the check is skipped (reported as such). Shingle length is 6 words, case-folded,
punctuation-stripped — long enough that a match means copied text, not a common phrase.

Importable: `longest_overlap(text, corpus_shingles)` for use from lint_patterns.py.
"""
import glob
import json
import os
import re
import sys

SHINGLE = 6
TEXT_FIELDS = ("situation", "reply_strategy", "example_case")
WORDS = re.compile(r"[a-z0-9']+")


def shingles(text, n=SHINGLE):
    ws = WORDS.findall(text.lower())
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def load_corpus(raw_dir):
    """Every review body and developer reply in the raw corpus, as one set of shingles."""
    out = set()
    for path in glob.glob(os.path.join(raw_dir, "**", "*.json*"), recursive=True):
        with open(path) as f:
            records = (json.loads(l) for l in f) if path.endswith(".jsonl") else json.load(f)
            for r in records:
                for k in ("body", "devReply"):
                    if r.get(k):
                        out |= shingles(r[k])
    return out


def longest_overlap(text, corpus):
    """(length in words, matched text) of the first corpus shingle found in `text`, else (0, "")."""
    ws = WORDS.findall(text.lower())
    for i in range(len(ws) - SHINGLE + 1):
        s = " ".join(ws[i:i + SHINGLE])
        if s in corpus:
            return SHINGLE, s
    return 0, ""


def check(data, raw_dir):
    """Return (leak_count, message). Message states when the check was skipped."""
    if not os.path.isdir(raw_dir):
        return 0, f"genericize: raw corpus not found at {raw_dir!r} - verbatim check SKIPPED"
    corpus = load_corpus(raw_dir)
    bad = 0
    for p in data["patterns"]:
        for field in TEXT_FIELDS:
            n, hit = longest_overlap(p[field], corpus)
            if n:
                bad += 1
                print(f"LEAK {p['id']}.{field}: {n}-word overlap: {hit!r}")
    return bad, f"genericize: {len(corpus)} corpus shingles, {bad} verbatim leaks"


def main():
    patterns_path = sys.argv[1] if len(sys.argv) > 1 else "data/reply-patterns.json"
    raw_dir = sys.argv[2] if len(sys.argv) > 2 else "raw"
    with open(patterns_path) as f:
        data = json.load(f)
    bad, msg = check(data, raw_dir)
    print(msg)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
