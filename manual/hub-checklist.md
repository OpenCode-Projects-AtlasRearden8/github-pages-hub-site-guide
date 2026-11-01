# Hub checklist

Print this or paste it at the top of your ritual log. A hub that passes all of these is one you can proudly link.

## One-time setup

- [ ] One repo holds the hub; `index.html` is the only routing page.
- [ ] Three section pages exist: `/books/`, `/guides/`, `/tools/` (cards, not content).
- [ ] Every project is a card: tag + title + one-sentence blurb + one link.
- [ ] Slugs are hyphen-separated, lowercase, plural sections, no dates in slugs.
- [ ] Links are absolute from root (`/tools/prompt-vault/`).
- [ ] `style.css` loads and the site works with JavaScript off.
- [ ] Skip link jumps to `#main`; skip target exists on every page.
- [ ] Footer repeats home + sections on every page.
- [ ] `404.html` exists with three working escape links.
- [ ] Headings: one `h1` per page; section titles `h2`; card/list text readable at phone width.
- [ ] Copyright, credit, and license are set (LICENSE with `Copyright (c) 2026 Asdale Dynamics, LLC`; README credits Asdale Dynamics, LLC).

## Every build

- [ ] `python3 build.py` exits 0.
- [ ] `python3 check.py` prints `PASS`.
- [ ] Manual sweep: click every card once (at phone width).

## Every rename

- [ ] New page built *and* old slug left as a redirect stub.
- [ ] Stub uses `meta refresh` + `location.replace` + a plain readable link.
- [ ] Sprint-chain test: stub points at the final page, never at another stub.
- [ ] Rename recorded in release notes (Changed column) and manifest.

## Monthly ritual (90 minutes)

- [ ] Minutes 0–15: build + check; fix every link failure.
- [ ] Minutes 15–30: review manifest stubs; pre-wire redirect for any planned rename.
- [ ] Minutes 30–50: one piece of content polish, exactly one.
- [ ] Minutes 50–70: release notes written in three columns, dated, newest first.
- [ ] Minutes 70–80: `python3 backup.py`; verify newest backup has content; prune OK.
- [ ] Minutes 80–90: final build + check; one-line commit; ritual log updated.
- [ ] Nothing pushed half-tested: build, test, *then* commit.

## Health checks quarterly

- [ ] No page needs more than two clicks from home.
- [ ] No orphan stale stubs you should retire, and no stub pointing somewhere dead.
- [ ] No chains of redirects anywhere (A→B→C).
- [ ] No cards whose target repo/site moved without the hub noticing — check that every external target still answers.
- [ ] Backups folder still tidy (≤ a few files, named `hub-backup-*`).
