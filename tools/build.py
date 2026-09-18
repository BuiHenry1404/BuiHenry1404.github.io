#!/usr/bin/env python3
"""Regenerate all 10 pages.  Usage:  python3 tools/build.py

English article bodies are read back out of projects/*.html (they are the source of
truth for EN prose); Vietnamese bodies live in tools/content_vi.py.
"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import ROOT, SLUGS, build_index, build_article
from content_vi import VI

EN = {}
for slug in SLUGS:
    s = (ROOT / 'projects' / f'{slug}.html').read_text(encoding='utf-8')
    EN[slug] = dict(
        title=re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip(),
        desc=re.search(r'<meta name="description" content="(.*?)">', s, re.S).group(1).strip(),
        h1=re.search(r'<article class="wrap article">\s*<h1>(.*?)</h1>', s, re.S).group(1).strip(),
        meta=re.search(r'<div class="article__meta">(.*?)</div>', s, re.S).group(1).strip(),
        body=re.search(r'<div class="article__meta">.*?</div>\s*(.*?)\s*<a class="backlink"', s, re.S).group(1),
    )

(ROOT / 'vi' / 'projects').mkdir(parents=True, exist_ok=True)
(ROOT / 'index.html').write_text(build_index('en'), encoding='utf-8')
(ROOT / 'vi' / 'index.html').write_text(build_index('vi'), encoding='utf-8')
for slug in SLUGS:
    (ROOT / 'projects' / f'{slug}.html').write_text(build_article('en', slug, EN[slug]), encoding='utf-8')
    (ROOT / 'vi' / 'projects' / f'{slug}.html').write_text(build_article('vi', slug, VI[slug]), encoding='utf-8')
print('10 pages regenerated')
