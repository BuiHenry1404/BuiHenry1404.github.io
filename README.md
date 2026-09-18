# buihenry1404.github.io

Personal portfolio — **Bùi Henry, AI Engineer**. Bilingual (English / Tiếng Việt).

Live at <https://buihenry1404.github.io> · Tiếng Việt at <https://buihenry1404.github.io/vi/>

## Stack

Plain static HTML and CSS. Nothing to install, nothing to compile before deploying —
GitHub Pages serves the files as they are. The only script on a page is ~30 lines for
scroll reveal and the hero terminal animation; both fall back cleanly when JavaScript is
off or `prefers-reduced-motion` is set.

```
index.html                       landing page (EN)
projects/
  mainframe-agent.html           grounding an LLM agent in COBOL
  sdlc-platform.html             multi-agent SDLC platform
  code-retrieval.html            retrieval benchmark for coding agents
  salona.html                    booking agent with an architectural guardrail
vi/                              the same five pages in Vietnamese
assets/
  style.css                      design tokens + all styling
  henry.jpg / .webp              portrait
tools/                           page generator (see below)
```

## Design

- Dark only. Background `#0B1120`, accent `#22C55E`. Every text pair clears WCAG AA
  (lowest measured 6.56:1).
- JetBrains Mono for headings, metadata and figures; IBM Plex Sans for prose.
- Prose capped at 68 characters per line, body 17px / line-height 1.65.
- Dot grid and scanline overlays are decorative and kept faint so body copy stays crisp.
- Responsive from 375px up, no horizontal scroll at any width.
- Accent colour is one CSS variable (`--accent` in `assets/style.css`).

## Editing

Both languages share one layout, so pages are generated rather than hand-edited — that
keeps the nav, footer, language switcher and `hreflang` tags identical across all ten
files.

```bash
python3 tools/build.py     # rewrites all 10 pages
```

- **English article prose** lives in `projects/*.html` and is read back out by the
  generator, so editing those files directly is fine.
- **Vietnamese article prose** lives in `tools/content_vi.py`.
- **Landing page copy, nav labels and the hero terminal lines** for both languages live in
  `tools/build_site.py`.

Run the generator after any of those changes and commit the result. The committed HTML is
what GitHub Pages serves; the generator is a convenience, not a deploy-time build step.

## Local preview

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Deploy

Pushing to `main` publishes via GitHub Pages. `.nojekyll` keeps Jekyll from touching the
files.
