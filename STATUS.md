# STATUS — github-pages-hub-site-guide

 Reviewed against the original goal on 2026-11-01. The folder started empty; the entire project was built from scratch to match the goal, then built and tested until everything passed.

## What was built

A tested guide + working example site for the *Asdale-way* GitHub Pages hub:

- **`manual/`** — seven plain-Markdown docs:
  - `00-overview.md` — why a hub site, the five commitments, how it differs from `github-for-everyone-handbook` (fundamentals) and `author-site-starter-template` (starter code)
  - `01-one-repo-one-index.md` — repo shape, the one routing page, slug rules
  - `02-project-cards-and-breadcrumbs.md` — card pattern, breadcrumbs, easy exits
  - `03-error-pages-and-redirects.md` — friendly escapable 404; redirect stubs for slug changes
  - `04-release-notes.md` — the three columns (Added / Changed / Fixed)
  - `05-maintenance-ritual.md` — the ninety-minute monthly ritual: link checks → redirects → one polish → release notes → tidy backup → ship
  - `hub-checklist.md` and `glossary.md`
- **`build.py`** — dependency-free Python build generating `site/`: one routing index with project cards, sections with cards, per-project landing pages, breadcrumbs + skip links on every page, an escapable `404.html`, a working redirect stub (`/tools/prompt-saver/` → `/tools/prompt-vault/`) plus a `manifest.json`, release-notes page with three columns, and a maintenance-ritual page.
- **`check.py`** — the test suite (see Verification).
- **`backup.py`** — dated tidy backups to `backups/hub-backup-YYYY-MM-DD.tar.gz`, pruned after 90 days, verified non-empty.
- **`README.md`** — run instructions, contents table, tests description, credit to Asdale Dynamics, LLC.
- **`LICENSE`** — MIT, `Copyright (c) 2026 Asdale Dynamics, LLC`.

## How to run

```bash
python3 build.py && python3 check.py     # build then test
python3 -m http.server -d site 8000      # optional preview
python3 backup.py                        # optional tidy backup
```

Python 3.10+ only; no third-party dependencies.

## Verification results (2026-11-01)

- `python3 build.py` → `Built 9 pages, 1 redirect(s), 404 page, stylesheet, manifest.` (exit 0)
- `python3 check.py` → `PASS: 11 html files validated` (exit 0). Suite covers: every internal link resolves; every full page has breadcrumb, escape hatch to home, `main` landmark, footer credit, lang/charset; 404 has all three escape links; hub index routes to all three sections with cards; release-notes page has all three column headings; redirect stub has meta refresh and points only at an existing final destination; secret-scan over HTML passes.
- Grid/mutation test: deliberately deleted `site/tools/prompt-vault/` and `site/release-notes/index.html`; the suite failed with the exact reasons, then passed once restored.
- `python3 backup.py` → verified 23-entry archive; second run correctly reports "already backed up today".
- Live preview smoke test: `/`, `/tools/`, `/tools/prompt-saver/` return 200; the stub serves the redirect to `/tools/prompt-vault/`; unknown paths return 404.
- Secret scan over the whole repo: no hits. No remote push, nothing published, git identity only (no co-author trailers).

## Known gaps / honest notes

- The check suite validates *structure and internal links*; external card URLs (GitHub, book pages) are pointed at real projects but not fetched/crawled during the ritual — the manual tells you to click them manually.
- The example site is illustrative, not the real dylanasdale.github.io; copying it live means replacing placeholder copy and external links with real ones.
- Python's built-in preview server shows its generic 404, not `site/404.html` (GitHub Pages does use it) — noted in the README.
- `manual/04-release-notes.md` is prose-first; the example site keeps its real columns in `build.py` + `site/release-notes/`.
- Cross-references between sibling repos (handbook, starter template) are by name only.
