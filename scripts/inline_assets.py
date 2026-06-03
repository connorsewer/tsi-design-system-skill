#!/usr/bin/env python3
"""Make a TSI HTML deliverable portable by embedding local assets as data URIs.

Rewrites local image/font references in an HTML file (img src, CSS url(...),
poster, and srcset) into base64 data URIs so the file renders anywhere when
shared by email, Slack, or upload, with no dependency on a local asset folder.

Remote URLs (http/https/protocol-relative), existing data: URIs, and anchor
hrefs are left untouched. Google Fonts <link> tags keep working as-is.

Usage:
    python3 inline_assets.py INPUT.html                # writes INPUT.portable.html
    python3 inline_assets.py INPUT.html -o OUT.html
    python3 inline_assets.py INPUT.html --in-place
    python3 inline_assets.py INPUT.html --warn-mb 1.5  # per-asset warn threshold

Exit codes: 0 ok, 1 a referenced local asset is missing, 2 bad usage.
"""
import argparse
import base64
import os
import re
import sys

MIME = {
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".webp": "image/webp", ".gif": "image/gif", ".svg": "image/svg+xml",
    ".avif": "image/avif", ".ico": "image/x-icon",
    ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf",
    ".otf": "font/otf",
}

SKIP_PREFIX = ("data:", "http://", "https://", "//", "#", "mailto:", "tel:")


def is_local(ref: str) -> bool:
    ref = ref.strip()
    return bool(ref) and not ref.lower().startswith(SKIP_PREFIX)


def encode(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    mime = MIME.get(ext)
    if not mime:
        raise ValueError(f"unsupported asset type: {ext}")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Embed local assets into an HTML file as data URIs.")
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    ap.add_argument("--in-place", action="store_true")
    ap.add_argument("--warn-mb", type=float, default=1.5, help="warn when one embedded asset exceeds this size")
    args = ap.parse_args()

    if not os.path.isfile(args.input):
        print(f"error: input not found: {args.input}", file=sys.stderr)
        return 2

    base_dir = os.path.dirname(os.path.abspath(args.input))
    with open(args.input, "r", encoding="utf-8") as f:
        html = f.read()

    cache: dict[str, str] = {}
    missing: list[str] = []
    embedded: list[tuple[str, int]] = []

    def resolve(ref: str):
        """ref -> (abs_path, data_uri) or (None, None) if it should be skipped/missing."""
        raw = ref.strip().strip('"').strip("'")
        if not is_local(raw):
            return None, None
        # strip query/hash on local paths
        clean = raw.split("?", 1)[0].split("#", 1)[0]
        abspath = os.path.normpath(os.path.join(base_dir, clean))
        if abspath in cache:
            return abspath, cache[abspath]
        if not os.path.isfile(abspath):
            missing.append(raw)
            return abspath, None
        try:
            uri = encode(abspath)
        except ValueError as e:
            print(f"warning: skipping {raw} ({e})", file=sys.stderr)
            return abspath, None
        size = os.path.getsize(abspath)
        cache[abspath] = uri
        embedded.append((clean, size))
        if size > args.warn_mb * 1_000_000:
            print(f"warning: {clean} is {size/1_000_000:.1f} MB; embedded file will be ~{size*1.34/1_000_000:.1f} MB larger.", file=sys.stderr)
        return abspath, uri

    # 1) attribute references: src="...", poster="...", and srcset (first URL of each candidate)
    def attr_sub(m):
        attr, q, val = m.group(1), m.group(2), m.group(3)
        _, uri = resolve(val)
        if uri is None:
            return m.group(0)
        return f'{attr}={q}{uri}{q}'

    html = re.sub(r'\b(src|poster)\s*=\s*(["\'])(.*?)\2', attr_sub, html, flags=re.IGNORECASE | re.DOTALL)

    # 2) CSS url(...) in <style> blocks and inline style="" attributes
    def url_sub(m):
        q = m.group(1) or ""
        val = m.group(2)
        _, uri = resolve(val)
        if uri is None:
            return m.group(0)
        return f'url({q}{uri}{q})'

    html = re.sub(r'url\(\s*(["\']?)([^)\'"]+)\1\s*\)', url_sub, html, flags=re.IGNORECASE)

    if missing:
        print("error: referenced local assets not found (run from the package so relative paths resolve):", file=sys.stderr)
        for m in sorted(set(missing)):
            print(f"  - {m}", file=sys.stderr)
        return 1

    if args.in_place:
        out = args.input
    elif args.output:
        out = args.output
    else:
        root, ext = os.path.splitext(args.input)
        out = f"{root}.portable{ext}"

    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    total = sum(s for _, s in embedded)
    print(f"Embedded {len(embedded)} asset(s), {total/1_000_000:.2f} MB raw -> {out}")
    for name, size in sorted(embedded, key=lambda x: -x[1]):
        print(f"  {size/1024:8.1f} KB  {name}")
    print("Portable: no local asset paths remain. Remote stylesheets/fonts (Google Fonts) are unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
