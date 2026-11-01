# 03 · Error pages and redirects

## The 404 is a doorway, not a dead end

GitHub Pages serves your repo-root `404.html` for any unknown URL. Build it in the shape of the hub itself — three doors:

- **Home** — start over at the index.
- **Books** — the thing most first-time visitors came for.
- **Tools** — the thing regulars came for.

Copy matters. "Nothing at this address. No shame in a wrong turn. Pick a door:" is friendlier than "Error 404 — resource not found." The kind voice is a feature, not decoration; use it here too.

Rule: **every 404 has at least three escape links, and they all work.** `check.py` enforces this.

## Redirects when slugs change

When a slug changes — `prompt-saver` → `prompt-vault` — you do three things:

1. **Build the new page** at the new slug.
2. **Leave a redirect stub** at the old slug:

```html
<meta http-equiv="refresh" content="0; url=/tools/prompt-vault/">
<link rel="canonical" href="https://example.com/tools/prompt-saver/">
<script>location.replace("/tools/prompt-vault/");</script>
```

The meta refresh carries crawlers; the `location.replace` carries humans *without* polluting back-button history; and the plain HTML link below ("Prompt Saver now lives at …") carries everyone else, including text-only browsers.

3. **Record it in the redirects manifest** so the ritual can audit it (chapter 05).

## Never do this

- **Never delete a slug and leave nothing behind.** External links (chat messages, Reddit, emails) break silently. A missing redirect is an invisible debt.
- **Never chain redirects** (A→B→C). Redirect straight to the final slug. `check.py` verifies each stub points directly at a real page rather than another stub (currently enforced by requiring the destination and refresh; keep chains out by convention).
- **Never redirect to the homepage.** Send readers to the page they meant to reach, or its section. Homepage-redirects teach people that your links lie.

## When a *project* moves off the hub

If a tool graduates to its own repo and site, replace its hub landing page with one redirect stub pointing there. You keep the URL you advertised; the project keeps its independence.
