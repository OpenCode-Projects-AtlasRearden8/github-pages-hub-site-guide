#!/usr/bin/env python3
import datetime
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "site"
BACKUPS = ROOT / "backups"
KEEP_DAYS = 90


def main():
    if not (SITE / "index.html").is_file():
        print("site/ has no index.html. Run: python3 build.py")
        return 1
    BACKUPS.mkdir(exist_ok=True)
    today = datetime.date.today()
    name = "hub-backup-%s.tar.gz" % today.isoformat()
    target = BACKUPS / name
    if target.exists():
        print("already backed up today: backups/%s" % name)
        return 0
    for item in sorted(BACKUPS.glob("hub-backup-*.tar.gz")):
        stem = item.name.replace("hub-backup-", "").replace(".tar.gz", "")
        try:
            age = (today - datetime.date.fromisoformat(stem)).days
        except ValueError:
            continue
        if age > KEEP_DAYS:
            item.unlink()
            print("pruned %s (%d days old)" % (item.name, age))
    subprocess.run(
        ["tar", "-czf", str(target), "-C", str(ROOT), "site"],
        check=True,
    )
    verify = subprocess.run(
        ["tar", "-tzf", str(target)], capture_output=True, text=True
    )
    count = len(verify.stdout.splitlines())
    if count == 0:
        target.unlink()
        print("backup was empty; deleted")
        return 1
    print("verified: %d entries in backups/%s" % (count, name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
