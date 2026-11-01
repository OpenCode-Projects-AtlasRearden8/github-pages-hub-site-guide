# 01 · One repo, one index

## The shape of the thing

```
hub-repo/
├── index.html            ← the one routing page
├── 404.html              ← the escape hatch
├── books/index.html      ← section listing (cards)
├── guides/index.html     ← section listing (cards)
├── tools/index.html      ← section listing (cards)
├── tools/prompt-vault/index.html   ← one landing page per project
├── tools/prompt-saver/index.html   ← old slug left as a redirect stub
├── style.css
└── release-notes/index.html
```

Rules:

- **`index.html` routes.** Three cards, three doors: Books, Guides, Tools. Nothing else competes for attention. A reader should find their path in one glance and one click.
- **Sections are listings, not destinations.** A section page is a grid of cards pointing *out* — to GitHub repos, to published pages, to your book's sales page. The hub stays small forever.
- **One landing page per project.** For projects that deserve their own hub page, give them a slug (`/tools/prompt-vault/`) and a breadcrumb. That page is also cards-and-links; it still doesn't contain the project.
- **Absolute paths from root.** Links look like `/tools/prompt-vault/`, not `../../tools/`. GitHub Pages serves from a stable root (for personal sites, the domain root), so absolute paths are safe and readable.

## URL slugs

- Hyphen-separated, lowercase, plural sections: `/books/`, `/guides/`, `/tools/`.
- Project slug = short, human, memorable: `prompt-vault`, not `pv-beta-2`.
- Slugs are *forever*. If a slug must change, that is a redirect (chapter 03), not a forklift.

## The 30-second test

Open your hub. Ask a friend: "Find the chess tool." If they can't click two links or fewer, the index is doing too much. Move detail out, cards in.
