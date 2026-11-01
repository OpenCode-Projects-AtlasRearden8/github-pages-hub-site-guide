# 05 · The ninety-minute monthly maintenance ritual

Once a month, ninety minutes, timer on. No ritual, no hub — a ritual kept is what separates a living hub from a brochure with a broken link.

## Minutes 0–15 · Clean room: link checks

```bash
python3 build.py && python3 check.py
```

Every `internal link … goes nowhere` failure is a promise you broke to a reader. Fix links first, before anything creative. Then do one manual sweep: click through the hub like a visitor (phone-sized window, too).

## Minutes 15–30 · Redirects

- Review the redirects manifest (`site/manifest.json`): are stubs still needed, still pointing at the *final* destination?
- Planning any rename this month? **Build the stub before you move the page.**
- Old stub whose traffic has long drained away? Retire it and note the retirement in the release notes.

## Minutes 30–50 · Content polish (small and steady)

Pick exactly one:

- Refresh one card blurb.
- Add one new project card (with section card, checked links).
- Improve one breadcrumb ambiguity.
- Fix one sentence that sounds like a manual, not a friend.

Small monthly deposits compound; do not try for a redesign on ritual day.

## Minutes 50–70 · Release notes

Write this month's entry in three columns — **Added / Changed / Fixed** — on `/release-notes/`. Dated. Most-recent first. If it happened and is not in the notes, it did not happen.

```markdown
## 2026-12-01 · Month name
**Added** · **Changed** · **Fixed**
- new tool page   - renamed X→Y (+ redirect)   - fixed dead link in /guides/
```

## Minutes 70–80 · Backup

```bash
python3 backup.py
```

- Produces `backups/hub-backup-YYYY-MM-DD.tar.gz` from the built site — tidy, dated, no editor droppings.
- Prunes backups older than 90 days automatically.
- Sanity check: `tar -tzf <newest backup> | head` — confirm it has content before you trust it.

## Minutes 80–90 · Ship and log

1. `python3 build.py && python3 check.py` one last time.
2. Commit: one line at most. `site: November ritual — link sweep, release notes, backup`.

Keep a one-line ritual log (in the release-notes page or a `ritual-log.md`): date, minutes spent, one thing fixed. Rhythm is the feature.

## If you miss a month

Skip a month, the ritual survives; skip three, treat the next one as a 3-hour deep-clean (backup *first*, then everything above).
