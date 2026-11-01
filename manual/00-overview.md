# 00 · Overview: why a hub site

This is the manual for building and keeping a **personal hub site on GitHub Pages, the Asdale way**. It pairs with the small static site in this repository (`build.py` → `site/`), which is a working example of every rule the manual teaches.

The idea in one sentence: **keep one repo with a single index page whose only job is to send readers where they want to go** — books, guides, and tools — so every project you ever publish gets a door instead of a hallway maze.

## The five commitments

1. **One repo, one index.** Your hub lives in one simple repo. `index.html` routes; projects live elsewhere.
2. **Cards, not nesting.** Projects appear as cards with a title, a one-line blurb, and a link. The hub never tries to contain a project.
3. **Breadcrumbs and easy exits.** Every page knows where it sits (`Home / Tools / Prompt Vault`) and offers a way back. The 404 page is a doorway to home, books, and tools — not a dead end.
4. **Redirects when slugs change.** Rename a page and you leave a signpost at the old address. Readers with old bookmarks never hit a wall.
5. **A ninety-minute monthly ritual.** Link checks, redirect review, small polish, release notes, a tidy dated backup, ship.

## How this differs from sibling projects

| Project | What it is | What this one adds |
| --- | --- | --- |
| `github-for-everyone-handbook` | GitHub fundamentals (repos, branches, PRs) | Assumes you know those; focuses on the hub pattern and upkeep |
| `author-site-starter-template` | Starter code to clone and fill in | Teaches *why* the site is built this way, plus the maintenance ritual |

## What's in this repository

- `manual/` — the chapters, checklist, and glossary (plain Markdown, readable in the browser or a text editor).
- `build.py` — Python standard library only; generates the example site into `site/`.
- `check.py` — the test suite. It verifies the built site (links resolve, breadcrumbs exist, escapes exist, release-note columns present, redirect stubs valid, no secrets).
- `backup.py` — dated, tidy site backups with pruning.
- `site/` — generated output. Not committed; rebuildable in seconds.

## Serving the hub

The example site uses absolute paths and directory-style URLs (`/tools/prompt-vault/`), exactly what GitHub Pages serves (a `404.html` at the repo root is used automatically). To preview locally: `python3 build.py && python3 -m http.server -d site 8000`.
