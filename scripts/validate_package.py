#!/usr/bin/env python3
"""Validate the TSI Design System 2.0 package structure."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "DESIGN.md",
    "AGENTS.md",
    "CLAUDE.md",
    "agents/openai.yaml",
    "uploads/TSI_BrandIdentityGuide_FINAL_022123.pdf",
    "uploads/TSI_PPT_Widescreen_Poppins.pptx",
    "uploads/brand_guide_text.txt",
    "evals/evals.json",
    "assets/reference/adventurous-visual-system-contact-sheet.png",
    "scripts/overlay_tsi_logo.py",
]

REQUIRED_REFERENCES = [
    "brand-foundations.md",
    "logo-and-assets.md",
    "visual-modes.md",
    "generated-imagery.md",
    "adventurous-backgrounds-and-accents.md",
    "components-and-patterns.md",
    "motion.md",
    "surface-contracts.md",
    "qa-rubric.md",
    "external-standards.md",
]

REQUIRED_EXAMPLES = [
    "landing-page.html",
    "mini-deck.html",
    "product-visual.html",
    "prompt-book.html",
]

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_files(failures: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"Missing required file: {rel}", failures)
    for name in REQUIRED_REFERENCES:
        if not (ROOT / "references" / name).is_file():
            fail(f"Missing reference file: references/{name}", failures)


def validate_assets(failures: list[str]) -> None:
    official = ROOT / "assets" / "official"
    generated = ROOT / "assets" / "generated-v2"
    previews = generated / "previews"

    if len(list(official.glob("*"))) < 40:
        fail("Expected at least 40 official assets in assets/official", failures)

    required_official = [
        "logo-primary-on-white.png",
        "logo-primary-white.png",
        "symbol-rgb.png",
        "icon-arm.png",
        "people-01.png",
        "portrait-1.png",
    ]
    for name in required_official:
        if not (official / name).is_file():
            fail(f"Missing official asset: assets/official/{name}", failures)

    preview_images = sorted(previews.glob("*.webp")) if previews.exists() else []
    if len(preview_images) != 10:
        fail(f"Expected exactly 10 generated-v2 WebP previews; found {len(preview_images)}", failures)

    for image in preview_images:
        sidecar = generated / (image.name.replace("-preview.webp", ".png.json"))
        if not sidecar.is_file():
            fail(f"Missing metadata sidecar for {image.name}", failures)
            continue
        try:
            data = json.loads(sidecar.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid JSON sidecar for {image.name}: {exc}", failures)
            continue
        for key in ["id", "title", "prompt", "generation_mode", "source_path", "review_status"]:
            if key not in data:
                fail(f"Sidecar {sidecar.name} missing key: {key}", failures)
        if data.get("preview_path") != f"previews/{image.name}":
            fail(f"Sidecar {sidecar.name} preview_path does not match {image.name}", failures)

    manifest = generated / "manifest.json"
    if not manifest.is_file():
        fail("Missing assets/generated-v2/manifest.json", failures)
    if not (generated / "generated-v2-preview-contact-sheet.webp").is_file():
        fail("Missing assets/generated-v2/generated-v2-preview-contact-sheet.webp", failures)


def validate_examples(failures: list[str]) -> None:
    examples = ROOT / "examples"
    for name in REQUIRED_EXAMPLES:
        path = examples / name
        if not path.is_file():
            fail(f"Missing example: examples/{name}", failures)
            continue

        html = read_text(path)
        if "<style" not in html:
            fail(f"{name} must include inline CSS in a <style> tag", failures)
        if "prefers-reduced-motion" not in html:
            fail(f"{name} must include reduced-motion handling", failures)
        if re.search(r'<link[^>]+rel=["\']stylesheet["\']', html, re.I):
            if "fonts.googleapis.com" not in html:
                fail(f"{name} must not use external stylesheets except Google Fonts", failures)
        if re.search(r'src=["\']https?://', html, re.I):
            fail(f"{name} must use relative package asset paths for images/scripts", failures)
        if "assets/official/" not in html and name != "prompt-book.html":
            fail(f"{name} should place at least one official asset", failures)


def validate_evals(failures: list[str]) -> None:
    path = ROOT / "evals" / "evals.json"
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid evals JSON: {exc}", failures)
        return
    if data.get("skill_name") != "tsi-design-system":
        fail("evals/evals.json skill_name must be tsi-design-system", failures)
    evals = data.get("evals", [])
    if len(evals) < 4:
        fail("Expected at least 4 eval prompts", failures)
    for item in evals:
        if not item.get("prompt") or not item.get("expected_output"):
            fail(f"Eval {item.get('id', '<unknown>')} missing prompt or expected_output", failures)
        if len(item.get("expectations", [])) < 4:
            fail(f"Eval {item.get('id', '<unknown>')} should have at least 4 expectations", failures)


def main() -> int:
    failures: list[str] = []
    validate_required_files(failures)
    validate_assets(failures)
    validate_examples(failures)
    validate_evals(failures)

    if failures:
        print("Package validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Package validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
