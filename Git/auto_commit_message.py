#!/usr/bin/env python3
"""
auto_commit_message.py

Generate a suggested commit message from the staged git diff using heuristics
inspired by GitHub's auto-generated messages. Produces a short human-friendly
subject and a body that lists changed files and example snippets.

Usage:
  python auto_commit_message.py           # prints suggestion to stdout
  python auto_commit_message.py --write <path-to-commit-msg-file>

The script is conservative and meant as a helper — always review before
committing.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


def run_git(args: List[str], cwd: str | None = None) -> str:
    try:
        out = subprocess.check_output(["git"] + args, cwd=cwd, stderr=subprocess.DEVNULL)
        return out.decode("utf-8", errors="replace")
    except subprocess.CalledProcessError:
        return ""


def get_repo_root() -> str:
    root = run_git(["rev-parse", "--show-toplevel"]).strip()
    return root or os.getcwd()


def get_staged_files(repo_root: str) -> List[str]:
    out = run_git(["diff", "--staged", "--name-only"], cwd=repo_root)
    files = [line.strip() for line in out.splitlines() if line.strip()]
    return files


def get_staged_diff_for_file(repo_root: str, filename: str) -> str:
    out = run_git(["diff", "--staged", "--unified=0", "--", filename], cwd=repo_root)
    return out


def analyze_diffs(repo_root: str, files: List[str]) -> Tuple[Dict[str, Tuple[int, int]], Dict[str, List[str]]]:
    counts: Dict[str, Tuple[int, int]] = {}
    samples: Dict[str, List[str]] = defaultdict(list)
    for f in files:
        diff = get_staged_diff_for_file(repo_root, f)
        added = 0
        removed = 0
        for line in diff.splitlines():
            if line.startswith('+++') or line.startswith('---') or line.startswith('diff '):
                continue
            if line.startswith('+'):
                # skip the git metadata additions
                added += 1
                if len(samples[f]) < 3:
                    samples[f].append(line)
            elif line.startswith('-'):
                removed += 1
                if len(samples[f]) < 3:
                    samples[f].append(line)
        counts[f] = (added, removed)
    return counts, samples


def extract_keywords_from_diff(diff_text: str) -> List[str]:
    keywords: List[str] = []
    for line in diff_text.splitlines():
        if not line:
            continue
        sign = line[0]
        if sign not in ('+', '-'):
            continue
        content = line[1:].strip()
        # capture Python function or class names
        m = re.search(r"def\s+([a-zA-Z0-9_]+)", content)
        if m:
            keywords.append(m.group(1))
            continue
        m = re.search(r"class\s+([A-Z][a-zA-Z0-9_]*)", content)
        if m:
            keywords.append(m.group(1))
            continue
        # TODO/FIXME/bug hints
        if re.search(r"\b(todo|fixme|fix|bug)\b", content, re.IGNORECASE):
            keywords.append('fix')
            continue
        # short action tokens
        for token in ('add', 'remove', 'update', 'refactor', 'rename', 'change', 'improve', 'fix'):
            if re.search(rf"\b{token}\b", content, re.IGNORECASE):
                keywords.append(token)
                break
    return keywords


def pick_type_and_scope(files: List[str], counts: Dict[str, Tuple[int, int]]) -> Tuple[str, str]:
    exts = set(os.path.splitext(f)[1].lower() for f in files)
    lower_files = [f.lower() for f in files]

    # If only docs changed
    if all(ext in {'.md', '.rst', '.txt'} or 'readme' in f for ext, f in zip(exts, lower_files)):
        return 'docs', ''

    if any('test' in f or f.startswith('tests/') or '/tests/' in f for f in lower_files):
        return 'test', ''

    if any(f.endswith('.py') for f in files):
        # simple heuristics: if we added more than removed and added significant lines -> feat
        total_added = sum(a for a, _ in counts.values())
        total_removed = sum(r for _, r in counts.values())
        if total_added - total_removed > 10:
            return 'feat', ''
        if total_removed - total_added > 10:
            return 'refactor', ''

    # Fallback: choose based on added/removed balance
    total_added = sum(a for a, _ in counts.values())
    total_removed = sum(r for _, r in counts.values())
    if total_added > total_removed:
        return 'feat', ''
    if total_removed > total_added:
        return 'refactor', ''
    return 'chore', ''


def summarize_subject(msg_type: str, scope: str, files: List[str], counts: Dict[str, Tuple[int, int]]) -> str:
    total_added = sum(a for a, _ in counts.values())
    total_removed = sum(r for _, r in counts.values())

    # Pick a primary file (largest net change)
    def net_change(f):
        a, r = counts.get(f, (0, 0))
        return abs(a - r) or (a + r)

    primary = sorted(files, key=lambda f: (-net_change(f), f))[0]
    base = os.path.splitext(os.path.basename(primary))[0]
    scope_part = f"({base})" if base and len(files) > 1 else ''

    # Decide on a verb for a more natural subject
    verb = 'Update'
    if msg_type == 'feat':
        verb = 'Add' if total_added >= total_removed else 'Implement'
    elif msg_type in ('fix', 'test'):
        verb = 'Fix'
    elif msg_type == 'refactor':
        verb = 'Refactor'
    elif msg_type == 'docs':
        verb = 'Update'

    subject = f"{verb} {base} {scope_part}".strip()
    if not subject:
        subject = f"{msg_type}: change {len(files)} files (+{total_added}/-{total_removed})"
    if len(subject) > 72:
        subject = subject[:69] + '...'
    return subject


def build_body(files: List[str], counts: Dict[str, Tuple[int, int]], samples: Dict[str, List[str]]) -> str:
    lines: List[str] = []
    lines.append('Files changed:')
    for f in files:
        a, r = counts.get(f, (0, 0))
        lines.append(f" - {f}: +{a}/-{r}")
        for s in samples.get(f, []):
            # show a trimmed version of the sample lines
            snippet = s
            if len(snippet) > 200:
                snippet = snippet[:197] + '...'
            lines.append(f"    {snippet}")
    lines.append('')
    # Suggestion section: keywords and review note
    lines.append('Suggestion:')
    all_keywords: List[str] = []
    for f in files:
        diff = get_staged_diff_for_file(get_repo_root(), f)
        all_keywords.extend(extract_keywords_from_diff(diff))

    if all_keywords:
        freq: Dict[str, int] = defaultdict(int)
        for k in all_keywords:
            freq[k] += 1
        common = sorted(freq.items(), key=lambda kv: -kv[1])[:6]
        lines.append(' - Keywords: ' + ', '.join(k for k, _ in common))

    lines.append(' - Review and edit the subject/body before committing.')
    return '\n'.join(lines)


def generate_message(repo_root: str) -> str:
    files = get_staged_files(repo_root)
    if not files:
        return ""  # caller should handle

    counts, samples = analyze_diffs(repo_root, files)
    msg_type, scope = pick_type_and_scope(files, counts)
    subject = summarize_subject(msg_type, scope, files, counts)
    body = build_body(files, counts, samples)
    return subject + "\n\n" + body


def write_to_file(path: str, text: str) -> None:
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='auto_commit_message')
    parser.add_argument('--write', '-w', help='Write the suggestion into the given commit-msg file')
    args = parser.parse_args(argv)

    repo_root = get_repo_root()
    msg = generate_message(repo_root)
    if not msg:
        print('No staged changes found. Stage files first.', file=sys.stderr)
        return 2

    if args.write:
        # If the commit file already contains content (e.g. user provided a message), do not overwrite
        try:
            with open(args.write, 'r', encoding='utf-8') as fh:
                existing = fh.read().strip()
        except FileNotFoundError:
            existing = ''

        if existing:
            # do not overwrite an existing message (safe behaviour)
            return 0

        write_to_file(args.write, msg)
        return 0
    else:
        print(msg)
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
