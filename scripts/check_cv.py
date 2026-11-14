#!/usr/bin/env python3
"""Fail if a PDF carries a phone number, a full date, or a tel: link.

Looks at the visible text (pdftotext) AND every stream, decompressed, so
link annotations and metadata hidden in compressed object streams are seen.
Prints only what kind of thing matched, never the value.

Usage: python3 scripts/check_cv.py cv.pdf   (exit 0 = clean)
"""
import re
import subprocess
import sys
import zlib

MONTHS = rb"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
PATTERNS = {
    "tel: link": re.compile(rb"tel:"),
    "phone number": re.compile(rb"\+\d{2}[\s\d]{8,}"),
    "full date": re.compile(rb"\b\d{1,2}(?:st|nd|rd|th)?\s+" + MONTHS + rb"\s+\d{4}|\b\d{1,2}[/.]\d{1,2}[/.]\d{4}\b"),
    "birth/born": re.compile(rb"(?i)\b(?:birth|born)\b"),
}


def layers(path):
    raw = open(path, "rb").read()
    yield raw
    for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", raw, re.S):
        try:
            yield zlib.decompress(m.group(1))
        except zlib.error:
            pass  # not Flate-compressed (or binary font data): raw bytes already scanned
    text = subprocess.run(["pdftotext", path, "-"], capture_output=True)
    yield None if text.returncode else text.stdout


def main(path):
    found = set()
    for data in layers(path):
        if data is None:
            found.add("unreadable text (pdftotext failed)")
        else:
            found |= {name for name, rx in PATTERNS.items() if rx.search(data)}
    found = sorted(found)
    if found:
        print(f"{path}: FOUND {', '.join(found)} - do not commit")
        return 1
    print(f"{path}: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
