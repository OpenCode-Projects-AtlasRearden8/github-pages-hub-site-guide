# Glossary

Plain English, like everything else here. Each entry says what it is in one breath, then why you care.

- **404 page** · The page GitHub Pages shows when an address does not exist. Yours is a doorway with three escape links, not a dead end.
- **Backup** · A dated archive of your built site, made with `backup.py`, pruned after 90 days. Tidy means named by date and small, not fat.
- **Breadcrumb** · The little trail at the top of a page (`Home / Tools / Prompt Vault`). It tells readers where they are, and every crumb but the last is a working link.
- **Card** · A linked tile with a tag, a title, and a one-sentence blurb. The only way the hub mentions a project.
- **Chain (redirect)** · A stub pointing to another stub. Always redirect to the final page; chains are how reader trust leaks.
- **Escape hatch** · Any plain link that lets a reader start over: nav, breadcrumbs, footer links, the 404's doors. Every page needs at least one.
- **GitHub Pages** · Free web hosting for static files straight from a repository. Where the hub lives.
- **Hub index** · Your one `index.html` whose only job is routing readers to books, guides, and tools. One repo, one index.
- **Build (the site)** · Running `build.py`, which generates every HTML page into `site/`. The build is boring on purpose; boring is reliable.
- **Check (the site)** · Running `check.py`, the test suite. Verifies links resolve, breadcrumbs exist, escapes exist, redirect stubs point somewhere real, and no secrets slipped into the HTML.
- **Link check** · The monthly sweep that hunts dead links. Fifteen minutes now beats an angry reader later.
- **Maintenance ritual** · The ninety minutes you give the hub each month: link checks, redirect review, one polish, release notes, backup, ship. Skipping it for a month is fine; skipping it forever is how sites die.
- **Manifest (`manifest.json`)** · The machine-readable record of built pages and live redirects, regenerated on each build. Redirect audits read it; you read the release notes.
- **Redirect stub** · A tiny page left at an old slug so old links still work: `meta refresh` for crawlers, `location.replace` for browsers, a plain HTML link for everyone else.
- **Release notes** · The dated log of what you added, changed, and fixed — written in three columns. If it is not in the notes, it did not happen.
- **Section page** · `/books/`, `/guides/`, or `/tools/`. A listing of cards, never a destination. Depth stays at two clicks.
- **Slug** · The human part of a URL (`/tools/prompt-vault/`). Paragraph-length, lowercase, hyphen-separated, forever.
- **Stub** · Short for redirect stub.
- **Static site** · A website made of plain files, no server code. Fully visible if JavaScript breaks, loads fast, and can be backed up as a folder.
