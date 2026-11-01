#!/usr/bin/env python3
import datetime
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "site"

NAV = [
    ("Home", "/"),
    ("Books", "/books/"),
    ("Guides", "/guides/"),
    ("Tools", "/tools/"),
    ("Release notes", "/release-notes/"),
]

REDIRECTS = {
    "/tools/prompt-saver/": "/tools/prompt-vault/",
}

PAGES = {}


def page(path, title, crumb, content, description=""):
    PAGES[path] = {
        "path": path,
        "title": title,
        "crumb": crumb,
        "content": content,
        "description": description,
    }
    return path


def card(href, title, blurb, tag):
    return (
        '<a class="card" href="%s"><span class="tag">%s</span>'
        '<span class="card-title">%s</span>'
        '<span class="card-blurb">%s</span></a>'
        % (href, html.escape(tag), html.escape(title), html.escape(blurb))
    )


def columns(items):
    heads = ["Added", "Changed", "Fixed"]
    out = ['<div class="columns">']
    for head, group in zip(heads, items):
        rows = "".join("<li>%s</li>" % html.escape(r) for r in group)
        out.append(
            '<section class="column"><h3>%s</h3><ul>%s</ul></section>'
            % (head, rows)
        )
    out.append("</div>")
    return "".join(out)


LAYOUT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Dylan Asdale</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header>
  <a class="skip" href="#main">Skip to content</a>
  <nav aria-label="Main">
    <a class="brand" href="/">dylan&amp;sdale</a>
    {nav}
  </nav>
</header>
{crumb}
<main id="main">
{content}
</main>
<footer>
  <p><a href="/">Home</a> · <a href="/books/">Books</a> · <a href="/guides/">Guides</a> · <a href="/tools/">Tools</a> · <a href="/release-notes/">Release notes</a></p>
  <p>Built the Asdale way: one repo, one index, easy exits. Maintained by Asdale Dynamics, LLC.</p>
</footer>
</body>
</html>
"""


def render(page):
    nav = "".join(
        '<a href="%s"%s>%s</a>'
        % (
            href,
            ' aria-current="page"' if page["path"] == href else "",
            label,
        )
        for label, href in NAV
    )
    crumb = '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % "".join(
        '<a href="%s">%s</a> /' % (href, label)
        if href
        else "<span>%s</span>" % label
        for _, (href, label) in enumerate(page["crumb"])
    )
    return LAYOUT.format(
        title=html.escape(page["title"]),
        description=html.escape(
            page["description"]
            or "Plain-English AI books, guides, and tools."
        ),
        nav=nav,
        crumb=crumb,
        content=page["content"],
    )


def write(path, text):
    target = OUT / path.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def build():
    preview = [
        "Simple, beginner-proof pages with one job each",
        "Project cards that link out instead of nesting content here",
        "Escape hatches everywhere: a reader can always get home",
    ]
    PAGES.clear()
    page(
        "/",
        "Home",
        [(None, "Home")],
        '<section class="hero"><h1>AI, explained like a friend would.</h1>'
        '<p class="lede">Welcome to my hub. One page, three doors: pick what '
        'you came for and go straight to it.</p></section>'
        '<section class="grid">'
        + card("/books/", "Books", "The Massive AI Manual and future titles.", "Books")
        + card("/guides/", "Guides", "Step-by-step manuals for GitHub Pages, local AI, and more.", "Guides")
        + card("/tools/", "Tools", "Small utilities for prompts, chess, and FFXIV.", "Tools")
        + "</section>"
        + '<section><h2>What this hub promises</h2><ul>%s</ul></section>'
        % "".join(
            "<li>%s</li>" % html.escape(item) for item in preview
        )
        + '<section><h2>New here?</h2><p>Start with <a href="/books/">the book</a>, then check <a href="/release-notes/">release notes</a> for what just changed.</p></section>',
        description="One page routing readers to books, guides, and tools.",
    )
    page(
        "/books/",
        "Books",
        [("/", "Home"), (None, "Books")],
        '<h1>Books</h1><p>Long-form manuals, written like a friend explaining things over coffee.</p>'
        '<section class="grid">'
        + card(
            "https://dylanasdale.github.io/books/massive-ai-manual/",
            "The Massive AI Manual",
            "A plain-English guide to using AI without feeling talked down to.",
            "Book",
        )
        + "</section>",
    )
    page(
        "/guides/",
        "Guides",
        [("/", "Home"), (None, "Guides")],
        '<h1>Guides</h1><p>Project cards link to each guide; full walks live in their own repos.</p>'
        '<section class="grid">'
        + card(
            "https://github.com/dylanasdale/github-pages-hub-site-guide",
            "Build a GitHub Pages hub site",
            "The manual behind the very site you are reading.",
            "Guide",
        )
        + card(
            "https://github.com/dylanasdale/github-for-everyone-handbook",
            "GitHub for everyone",
            "Fundamentals before the hub work starts.",
            "Guide",
        )
        + card(
            "https://github.com/dylanasdale/author-site-starter-template",
            "Author site starter",
            "Starter code when you are ready to publish.",
            "Guide",
        )
        + "</section>",
    )
    page(
        "/tools/",
        "Tools",
        [("/", "Home"), (None, "Tools")],
        '<h1>Tools</h1><p>Small, local-first utilities. No clouds, no accounts, no data leaving your machine.</p>'
        '<section class="grid">'
        + card("/tools/prompt-vault/", "Prompt Vault", "Save, tag, and reuse prompts offline.", "Tool")
        + card("/tools/chess-drill/", "Chess Drill", "Spaced-repetition puzzles from your own losses.", "Tool")
        + card("/tools/ffxiv-gather/", "FFXIV Gather Log", "Track gathering routes and timers.", "Tool")
        + "</section>",
    )
    page(
        "/tools/prompt-vault/",
        "Prompt Vault",
        [("/", "Home"), ("/tools/", "Tools"), (None, "Prompt Vault")],
        '<h1>Prompt Vault</h1><p>A tiny offline prompt library. Tags, search, export — all in one folder you own.</p>'
        '<p><a href="/tools/">← Back to tools</a></p>',
    )
    page(
        "/tools/chess-drill/",
        "Chess Drill",
        [("/", "Home"), ("/tools/", "Tools"), (None, "Chess Drill")],
        '<h1>Chess Drill</h1><p>Turn games you lost into spaced-repetition puzzles. Your mistakes, your curriculum.</p>'
        '<p><a href="/tools/">← Back to tools</a></p>',
    )
    page(
        "/tools/ffxiv-gather/",
        "FFXIV Gather Log",
        [("/", "Home"), ("/tools/", "Tools"), (None, "FFXIV Gather Log")],
        '<h1>FFXIV Gather Log</h1><p>Track gathering routes and timers across Eorzea. For the unending journey.</p>'
        '<p><a href="/tools/">← Back to tools</a></p>',
    )
    page(
        "/release-notes/",
        "Release notes",
        [("/", "Home"), (None, "Release notes")],
        '<h1>Release notes</h1><p>Every release gets three columns: what was added, what changed, what was fixed.</p>'
        '<section><h2>2026-11-01 · Site refresh</h2>'
        + columns(
            [
                ["Prompt Vault tool page", "Release-note columns on this page"],
                ["Renamed /tools/prompt-saver/ to /tools/prompt-vault/ with a redirect", "Better homepage hero copy"],
                ["Link checker now catches escaped quotes", "Footer credits Asdale Dynamics, LLC"],
            ]
        )
        + "</section>"
        '<section><h2>2026-10-01 · Launch</h2>'
        + columns(
            [
                ["Hub index with three sections", "—"], ["Nav simplified to five links", "—"], ["404 page with escape links", "—"],
            ]
        )
        + "</section>",
    )
    page(
        "/maintenance/",
        "Maintenance ritual",
        [("/", "Home"), (None, "Maintenance")],
        '<h1>The ninety-minute monthly ritual</h1>'
        '<ol>'
        '<li><strong>Minutes 0–15 · Clean room.</strong> Run the link checker and read every failure. Fix broken links first.</li>'
        '<li><strong>Minutes 15–30 · Redirects.</strong> Sketch any renaming you want this month. Add redirect pages before you move anything.</li>'
        '<li><strong>Minutes 30–50 · Content.</strong> Update a card blurb, add one guide link, polish one sentence. Small and steady.</li>'
        '<li><strong>Minutes 50–70 · Release notes.</strong> Write the three columns for this release. If it is not in the notes, it did not happen.</li>'
        '<li><strong>Minutes 70–80 · Backup.</strong> Make a dated backup and prune backups older than 90 days.</li>'
        '<li><strong>Minutes 80–90 · Ship.</strong> Build, test, commit. Enjoy a clean hub for another month.</li>'
        '</ol>'
        '<p><a href="/">← Home</a></p>',
    )
    for old, new in REDIRECTS.items():
        write(
            old + "index.html",
            REDIRECT_TEMPLATE.format(
                here="https://example.com" + old,
                dest=new,
                title=old.strip("/").split("/")[-1].replace("-", " ").title(),
            ),
        )
        PAGES.pop(old, None)
    for entry in PAGES.values():
        write(entry["path"].rstrip("/") + "/index.html", render(entry))
    (OUT / "404.html").write_text(_not_found(), encoding="utf-8")
    write("/style.css", STYLESHEET)
    manifest = {
        "generated": datetime.date.today().isoformat(),
        "pages": sorted(PAGES),
        "redirects": REDIRECTS,
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print("Built %d pages, %d redirect(s), 404 page, stylesheet, manifest."
          % (len(PAGES), len(REDIRECTS)))
    return 0


REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} has moved</title>
<meta http-equiv="refresh" content="0; url={dest}">
<link rel="canonical" href="{here}">
<script>location.replace("{dest}");</script>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<main class="moved">
<h1>This page moved</h1>
<p>{title} now lives at <a href="{dest}">{dest}</a>.</p>
<p><a href="/">← Home</a></p>
</main>
</body>
</html>
"""


def _not_found():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Not found · Dylan Asdale</title>
<meta name="description" content="Nothing here, but three doors below.">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header><nav aria-label="Main"><a class="brand" href="/">dylan&amp;sdale</a></nav></header>
<main class="lost" id="main">
<h1>Nothing at this address</h1>
<p class="lede">No shame in a wrong turn. Pick a door:</p>
<section class="grid">
<a class="card" href="/"><span class="tag">Home</span><span class="card-title">Go home</span><span class="card-blurb">Start over at the hub.</span></a>
<a class="card" href="/books/"><span class="tag">Books</span><span class="card-title">Read the book</span><span class="card-blurb">The Massive AI Manual.</span></a>
<a class="card" href="/tools/"><span class="tag">Tools</span><span class="card-title">Use a tool</span><span class="card-blurb">Small, local-first utilities.</span></a>
</section>
</main>
<footer><p>Everything above also works in the footer: <a href="/">Home</a> · <a href="/books/">Books</a> · <a href="/tools/">Tools</a>.</p></footer>
</body>
</html>
"""


STYLESHEET = """:root {
  --ink: #1d2430;
  --paper: #fdfbf7;
  --accent: #1d6b5a;
  --soft: #e7f0ec;
  --muted: #5a6675;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.6;
}
header nav { display: flex; gap: 1.25rem; align-items: center; flex-wrap: wrap; }
header { background: var(--soft); border-bottom: 2px solid var(--accent); padding: .75rem 1.25rem; }
.brand { font-weight: bold; text-decoration: none; color: var(--accent); }
nav a { color: var(--ink); text-decoration: none; }
nav a:hover, main a { color: var(--accent); }
.skip { position: absolute; left: -9999px; }
.skip:focus { left: 1rem; top: 1rem; background: var(--paper); padding: .5rem; }
.crumbs { padding: .5rem 1.25rem; font-size: .9rem; color: var(--muted); }
.crumbs a { color: var(--accent); }
main { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; }
.hero h1 { font-size: 2.2rem; margin-bottom: .25rem; }
.lede { color: var(--muted); font-size: 1.1rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.card { display: flex; flex-direction: column; gap: .35rem; padding: 1rem; border: 2px solid var(--accent); border-radius: .6rem; background: #fff; text-decoration: none; color: var(--ink); }
.card:hover { background: var(--soft); }
.tag { font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; color: var(--accent); }
.card-title { font-weight: bold; font-size: 1.15rem; }
.card-blurb { color: var(--muted); font-size: .95rem; }
.columns { display: grid; grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr)); gap: 1rem; }
.column { border: 1px solid var(--muted); border-radius: .5rem; padding: 1rem; background: #fff; }
.column h3 { margin-top: 0; color: var(--accent); }
footer { background: var(--soft); border-top: 2px solid var(--accent); padding: 1rem 1.25rem; text-align: center; color: var(--muted); }
footer a { color: var(--accent); }
.moved, .lost { text-align: center; padding-top: 3rem; }
"""


if __name__ == "__main__":
    sys.exit(build())
