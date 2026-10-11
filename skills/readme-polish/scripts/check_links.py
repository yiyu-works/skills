#!/usr/bin/env python3
"""Check local inline Markdown links. Does not fetch URLs or check anchors."""
import argparse, json, re, sys
from pathlib import Path
from urllib.parse import urlsplit, unquote

def check(markdown, root):
    markdown, root = Path(markdown).resolve(), Path(root).resolve()
    markdown.relative_to(root)
    text = markdown.read_text(encoding='utf-8')
    text = re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)
    problems = []
    for match in re.finditer(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)', text):
        target = match.group(1).strip('<>')
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else (markdown.parent / unquote(url.path))
        path = path.resolve()
        try:
            path.relative_to(root)
        except ValueError:
            problems.append({'target': target, 'reason': 'outside repository'})
            continue
        if not path.exists():
            problems.append({'target': target, 'reason': 'missing local path'})
    return problems

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('markdown',type=Path);p.add_argument('--root',type=Path,required=True)
    a=p.parse_args()
    try:
        problems=check(a.markdown,a.root)
    except (OSError,ValueError) as e:
        p.error(str(e))
    print(json.dumps({'file':str(a.markdown),'problems':problems,'scope':'inline Markdown local file links only'},ensure_ascii=False,indent=2))
    return bool(problems)
if __name__=='__main__':sys.exit(main())
