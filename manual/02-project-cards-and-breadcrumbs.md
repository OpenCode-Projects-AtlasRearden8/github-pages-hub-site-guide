# 02 · Project cards and breadcrumbs

## Project cards

A card is a self-contained link: **tag, title, blurb**.

```html
<a class="card" href="/tools/prompt-vault/">
  <span class="tag">Tool</span>
  <span class="card-title">Prompt Vault</span>
  <span class="card-blurb">Save, tag, and reuse prompts offline.</span>
</a>
```

Card rules:

- The **whole card is a link**. No "click here" text, no separate read-more link.
- The **blurb is one sentence, plain English**. "Like a friend would explain it", not feature-list prose.
- The **tag is a noun, not a emoji**: Book, Guide, Tool, Template.
- **Cards never nest content.** If a card needs four paragraphs, that content belongs on the project's own page or repo.
- Cards are **tested**: `check.py` fails the build if internal card links go nowhere.

## Breadcrumbs

Every content page carries `Home / Tools / Prompt Vault` at the top. Rules:

- The **last crumb is plain text**, not a link (you are already there).
- Every other crumb is a working link; `check.py` verifies each one.
- Depth rarely exceeds three crumbs. If you cannot decide between two crumbs paths, your information architecture is too deep — flatten a section.
- Each section page keeps one crumb: `Home / Tools`.

## Easy exits

- Header nav sits on **every full page**.
- The **skip link** (`Skip to content`, keyboard-visible on focus) goes straight to `<main>`.
- The **footer repeats** home and the main sections as plain links, so a lost reader can recover without scrolling.
- The 404 page (chapter 03) is itself an exit gallery.

The check suite asserts a breadcrumb, a home link, and a `main` landmark on every generated page — so a page that forgets its exits fails the build, not the reader.
