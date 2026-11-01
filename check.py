#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "site"

failures = []


def fail(msg):
    failures.append(msg)


def check(cond, msg):
    if not cond:
        fail(msg)


def read(rel):
    return (OUT / rel).read_text(encoding="utf-8")


def internal_hrefs(text):
    hrefs = []
    for match in re.finditer(r'(?:href|src)="([^"]+)"', text):
        href = match.group(1)
        if href.startswith(("/#", "#", "http", "mailto:", "//")):
            continue
        hrefs.append(href)
    return hrefs


def target_exists(href):
    if href.startswith("/"):
        rel = href.lstrip("/")
    else:
        rel = ""
    if href.endswith("/"):
        return (OUT / rel.rstrip("/")).is_dir()
    return (OUT / rel).is_file()


if not OUT.is_dir():
    fail("site/ has not been built. Run: python3 build.py")
else:
    html_files = sorted(OUT.rglob("*.html"))
    check(bool(html_files), "no HTML files built")
    manifest = None
    redirect_paths = set()
    redirects = OUT / "manifest.json"
    check(redirects.is_file(), "missing manifest.json")
    if redirects.is_file():
        manifest = json.loads(redirects.read_text(encoding="utf-8"))
        redirect_paths = set(manifest["redirects"])
    for built in html_files:
        rel = "/" + str(built.relative_to(OUT)).replace("\\", "/")
        page_url = rel.replace("index.html", "")
        if page_url in redirect_paths or rel.endswith("404.html"):
            continue
        text = built.read_text(encoding="utf-8")
        check('lang="en"' in text, f"{rel}: missing lang attribute")
        check("charset" in text, f"{rel}: missing charset")
        check(
            'aria-label="Breadcrumb"' in text,
            f"{rel}: missing breadcrumb nav",
        )
        check(
            'href="/"' in text and "Skip to content" in text,
            f"{rel}: missing escape hatch to home",
        )
        check('id="main"' in text, f"{rel}: missing main landmark")
        check(
            "Asdale Dynamics, LLC" in text,
            f"{rel}: missing footer credit",
        )
        for href in internal_hrefs(text):
            check(
                target_exists(href),
                f"{rel}: internal link {href} goes nowhere",
            )

    index_path = OUT / "index.html"
    if not index_path.is_file():
        fail("missing /index.html (the one page that routes everything)")
    else:
        hub = index_path.read_text(encoding="utf-8")
        for section in ('href="/books/"', 'href="/guides/"', 'href="/tools/"'):
            check(section in hub, f"/index.html missing routing link {section}")
        check('class="card"' in hub, "/index.html has no project cards")

    not_found_path = OUT / "404.html"
    if not not_found_path.is_file():
        fail("missing /404.html")
    else:
        nf = not_found_path.read_text(encoding="utf-8")
        for escape in ('href="/"', 'href="/books/"', 'href="/tools/"'):
            check(escape in nf, f"/404.html missing escape link {escape}")

    redirects = OUT / "manifest.json"
    check(redirects.is_file(), "missing manifest.json")
    if redirects.is_file() and manifest:
        for old in manifest["redirects"]:
            old_file = OUT / old.lstrip("/") / "index.html"
            check(
                old_file.is_file(),
                f"redirect stub missing for {old}",
            )
            if old_file.is_file():
                stub = old_file.read_text(encoding="utf-8")
                check(
                    'http-equiv="refresh"' in stub,
                    f"{old} redirect stub missing meta refresh",
                )
                check(
                    manifest["redirects"][old] in stub
                    and "location.replace" in stub,
                    f"{old} redirect stub does not point at its destination",
                )
                dest = manifest["redirects"][old]
                check(
                    target_exists(dest),
                    f"{old} redirect stub points at missing destination {dest}",
                )
        notes = OUT / "release-notes" / "index.html"
        check(notes.is_file(), "missing /release-notes/")
        if notes.is_file():
            rn = notes.read_text(encoding="utf-8")
            for head in ("Added", "Changed", "Fixed"):
                check(f"<h3>{head}</h3>" in rn, f"release notes missing {head} column")
            check('class="columns"' in rn, "release notes not laid out in columns")

    secrets = re.compile(
        r"sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,}|api[_-]?key\s*=\s*['\"][^'\"]{8,}",
        re.IGNORECASE,
    )
    for built in html_files:
        text = built.read_text(encoding="utf-8")
        check(not secrets.search(text), f"{built.name}: possible secret embedded")

    style = OUT / "style.css"
    check(style.is_file(), "missing style.css")

if failures:
    print("FAIL (%d)" % len(failures))
    for item in failures:
        print("  -", item)
    sys.exit(1)
print("PASS: %d html files validated" % len(sorted(OUT.rglob("*.html"))))
sys.exit(0)
