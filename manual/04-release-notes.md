# 04 · Release notes

The hub keeps a single release-notes page: `/release-notes/`. Every meaningful change to the hub earns an entry, and entries use **three columns** — a consistent form makes the upkeep trivial.

## The columns

| Column | What belongs |
| --- | --- |
| **Added** | New cards, new pages, new redirects, new tools/guides published elsewhere |
| **Changed** | Renames (with the redirect noted), rewritten blurbs, section reorganization, copy improvements |
| **Fixed** | Dead links, wrong breadcrumbs, 404 dead ends you created and eliminated |

## Format

One dated section per release, newest first, three columns inside:

```html
<section>
  <h2>2026-11-01 · Site refresh</h2>
  <div class="columns">
    <section class="column"><h3>Added</h3><ul><li>Prompt Vault tool page</li></ul></section>
    <section class="column"><h3>Changed</h3><ul><li>Renamed /tools/prompt-saver/ → /tools/prompt-vault/ (redirect live)</li></ul></section>
    <section class="column"><h3>Fixed</h3><ul><li>Dead link in /guides/</li></ul></section>
  </div>
</section>
```

Column deskside rules:

- **Bullet fragments or full sentences — pick one tone** per entry and keep it for the whole page. Keep dashes/hyphen consistent.
- **One line per bullet.** If it needs two, it is two bullets.
- **Renames always mention the old slug and the redirect.** This is your redirect audit trail: when chapter 05 says "review the redirects manifest", the notes tell you when each stub was created and why.
- **"—" is a legal bullet.** A release that only *fixed* things may show `Added —`. Never invent filler.

## Why bother

Release notes are three things at once:

1. **Reader service** — regulars can see the hub is alive and what moved.
2. **Your memory** — three months from now, the columns answer "did I already fix that?".
3. **The ritual's agenda** — half of maintenance minutes 50–70 is just writing down what minutes 0–50 discovered.

The check suite asserts the notes page exists and carries the three column headings; an entry with no columns fails the build.
