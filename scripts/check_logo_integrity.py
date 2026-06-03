#!/usr/bin/env python3
"""Audit an HTML file for TSI logo aspect-ratio integrity.

ABSOLUTE RULE: official logos and brand marks are never stretched, squashed,
or otherwise distorted. Their aspect ratio is locked, always.

The safe pattern is to constrain ONE dimension and let the other compute:
    .logo { height: 32px; width: auto; }        /* or width set, height auto */
If both dimensions must be bounded, use object-fit: contain (never cover/fill).

This script scans <img> tags that reference brand marks (logo / symbol /
sub-brand lockup / sub-brand icon) and flags anything that can distort them.

Usage:
    python3 check_logo_integrity.py FILE.html [FILE2.html ...]

Exit codes: 0 clean, 1 violations found, 2 bad usage.
"""
import re
import sys

# src tokens that indicate an official brand mark (not a photo / people illustration)
MARK_TOKENS = ("logo", "symbol", "sub-arm", "sub-loanservicing", "sub-cxbpo",
               "sub-healthcare", "lockup", "/icon-", "icon-arm", "icon-loanservicing",
               "icon-cxbpo", "icon-healthcare", "icon.svg")

IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE | re.DOTALL)
ATTR_RE = lambda name: re.compile(rf'\b{name}\s*=\s*(["\'])(.*?)\1', re.IGNORECASE | re.DOTALL)
STYLE_RE = ATTR_RE("style")
SRC_RE = ATTR_RE("src")
WIDTH_ATTR_RE = ATTR_RE("width")
HEIGHT_ATTR_RE = ATTR_RE("height")


def is_mark(src: str) -> bool:
    s = src.lower()
    return any(tok in s for tok in MARK_TOKENS)


def css_val(style: str, prop: str):
    m = re.search(rf'(?:^|;)\s*{prop}\s*:\s*([^;]+)', style, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def fixed(v):
    """A length that pins a dimension (not auto / unset / 100% only-one-side)."""
    if not v:
        return False
    v = v.strip().lower()
    return v not in ("auto", "", "100%", "fit-content", "max-content", "min-content", "unset", "inherit", "initial")


def audit_img(tag: str):
    """Return list of (severity, message) for one <img> tag, or []."""
    src_m = SRC_RE.search(tag)
    src = src_m.group(2) if src_m else ""
    if not is_mark(src):
        return []
    issues = []
    label = src.split("/")[-1][:48] or "(logo)"
    style = (STYLE_RE.search(tag).group(2) if STYLE_RE.search(tag) else "")

    of = css_val(style, "object-fit")
    if of in ("cover", "fill", "scale-down"):
        issues.append(("FAIL", f"{label}: object-fit:{of} distorts/crops the mark. Use 'contain' or remove it."))

    # transform scale with two unequal factors
    tr = css_val(style, "transform") or ""
    for m in re.finditer(r'scale\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\)', tr):
        if m.group(1) != m.group(2):
            issues.append(("FAIL", f"{label}: non-uniform transform scale({m.group(1)},{m.group(2)}) stretches the mark."))
    if re.search(r'scalex\(', tr) and not re.search(r'scaley\(', tr) or (re.search(r'scaley\(', tr) and not re.search(r'scalex\(', tr)):
        issues.append(("FAIL", f"{label}: single-axis scaleX/scaleY stretches the mark."))

    # dimensions from inline style and attributes
    w = css_val(style, "width")
    h = css_val(style, "height")
    wa = WIDTH_ATTR_RE.search(tag)
    ha = HEIGHT_ATTR_RE.search(tag)
    w = w if w is not None else (wa.group(2) if wa else None)
    h = h if h is not None else (ha.group(2) if ha else None)

    if w == "100%" and h == "100%":
        issues.append(("FAIL", f"{label}: width:100% + height:100% forces the mark to fill and distort. Set one dimension, other auto."))
    elif fixed(w) and fixed(h) and of != "contain":
        issues.append(("WARN", f"{label}: both width ({w}) and height ({h}) pinned. Set only one (other 'auto'), or add object-fit:contain, to guarantee ratio."))

    return issues


def audit_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return None
    fails, warns, checked = [], [], 0
    for tag in IMG_RE.findall(html):
        src_m = SRC_RE.search(tag)
        if src_m and is_mark(src_m.group(2)):
            checked += 1
        for sev, msg in audit_img(tag):
            (fails if sev == "FAIL" else warns).append(msg)
    # global red flag: object-fit:fill / cover declared on a .logo-ish selector in a <style> block
    for m in re.finditer(r'\.[a-z0-9_-]*(logo|symbol|mark|lockup)[a-z0-9_-]*\s*\{[^}]*object-fit\s*:\s*(cover|fill)', html, re.IGNORECASE):
        fails.append(f"CSS rule sets object-fit:{m.group(2)} on a logo selector; that distorts the mark.")
    return checked, fails, warns


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_logo_integrity.py FILE.html [...]", file=sys.stderr)
        return 2
    any_fail = False
    for path in sys.argv[1:]:
        res = audit_file(path)
        if res is None:
            any_fail = True
            continue
        checked, fails, warns = res
        print(f"\n{path}  ({checked} brand mark(s) checked)")
        for msg in fails:
            print(f"  FAIL  {msg}")
        for msg in warns:
            print(f"  warn  {msg}")
        if not fails and not warns:
            print("  ok  all marks preserve aspect ratio")
        if fails:
            any_fail = True
    print()
    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
