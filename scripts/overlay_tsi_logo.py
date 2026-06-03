#!/usr/bin/env python3
"""Composite an official transparent TSI logo onto a generated raster image."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw


POSITIONS = {"top-left", "top-right", "bottom-left", "bottom-right", "center"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Overlay an official transparent TSI logo PNG onto an image.")
    parser.add_argument("--input", required=True, help="Input image path.")
    parser.add_argument("--logo", required=True, help="Transparent official logo PNG path.")
    parser.add_argument("--output", required=True, help="Output image path. Source is never overwritten.")
    parser.add_argument("--position", default="top-left", choices=sorted(POSITIONS))
    parser.add_argument("--logo-width-percent", type=float, default=16.0, help="Logo width as percent of image width.")
    parser.add_argument("--logo-width-px", type=int, default=None, help="Optional fixed logo width in pixels.")
    parser.add_argument("--margin-percent", type=float, default=4.0, help="Margin as percent of shorter image side.")
    parser.add_argument("--opacity", type=float, default=1.0, help="Logo opacity from 0.1 to 1.0.")
    parser.add_argument("--plaque", choices=["none", "white", "dark"], default="none", help="Optional contrast plaque behind logo.")
    parser.add_argument("--plaque-opacity", type=float, default=0.82)
    parser.add_argument("--plaque-padding-percent", type=float, default=1.4)
    parser.add_argument("--metadata", action="store_true", help="Write output JSON sidecar metadata.")
    return parser.parse_args()


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def load_rgba(path: Path) -> Image.Image:
    if not path.is_file():
        raise FileNotFoundError(path)
    return Image.open(path).convert("RGBA")


def scale_logo(logo: Image.Image, base_width: int, width_percent: float, width_px: int | None) -> Image.Image:
    target_width = width_px if width_px else int(base_width * (width_percent / 100.0))
    target_width = max(24, target_width)
    ratio = target_width / logo.width
    target_height = max(1, int(logo.height * ratio))
    return logo.resize((target_width, target_height), Image.Resampling.LANCZOS)


def apply_opacity(logo: Image.Image, opacity: float) -> Image.Image:
    opacity = clamp(opacity, 0.1, 1.0)
    if opacity == 1.0:
        return logo
    logo = logo.copy()
    alpha = logo.getchannel("A")
    alpha = alpha.point(lambda value: int(value * opacity))
    logo.putalpha(alpha)
    return logo


def compute_position(base: Image.Image, logo: Image.Image, position: str, margin: int) -> Tuple[int, int]:
    if position == "top-left":
        return margin, margin
    if position == "top-right":
        return base.width - logo.width - margin, margin
    if position == "bottom-left":
        return margin, base.height - logo.height - margin
    if position == "bottom-right":
        return base.width - logo.width - margin, base.height - logo.height - margin
    return (base.width - logo.width) // 2, (base.height - logo.height) // 2


def draw_plaque(base: Image.Image, xy: Tuple[int, int], logo: Image.Image, kind: str, opacity: float, padding: int) -> None:
    if kind == "none":
        return
    x, y = xy
    alpha = int(255 * clamp(opacity, 0.1, 1.0))
    color = (255, 255, 255, alpha) if kind == "white" else (0, 30, 65, alpha)
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    rect = [x - padding, y - padding, x + logo.width + padding, y + logo.height + padding]
    radius = max(4, min(16, padding))
    draw.rounded_rectangle(rect, radius=radius, fill=color)
    base.alpha_composite(overlay)


def write_metadata(args: argparse.Namespace, output: Path, logo_size: Tuple[int, int], xy: Tuple[int, int]) -> None:
    data = {
        "file": output.name,
        "source_image": str(Path(args.input).resolve()),
        "logo": str(Path(args.logo).resolve()),
        "position": args.position,
        "logo_size": {"width": logo_size[0], "height": logo_size[1]},
        "placement_xy": {"x": xy[0], "y": xy[1]},
        "opacity": args.opacity,
        "plaque": args.plaque,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "method": "deterministic transparent PNG compositing; no logo generation",
    }
    output.with_suffix(output.suffix + ".json").write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    source = Path(args.input)
    logo_path = Path(args.logo)
    output = Path(args.output)

    if output.resolve() == source.resolve():
        print("Refusing to overwrite the source image.", file=sys.stderr)
        return 2

    base = load_rgba(source)
    logo = load_rgba(logo_path)
    logo = scale_logo(logo, base.width, args.logo_width_percent, args.logo_width_px)
    logo = apply_opacity(logo, args.opacity)

    margin = int(min(base.width, base.height) * (args.margin_percent / 100.0))
    padding = int(min(base.width, base.height) * (args.plaque_padding_percent / 100.0))
    xy = compute_position(base, logo, args.position, margin)

    output.parent.mkdir(parents=True, exist_ok=True)
    composed = base.copy()
    draw_plaque(composed, xy, logo, args.plaque, args.plaque_opacity, padding)
    composed.alpha_composite(logo, xy)

    if output.suffix.lower() in {".jpg", ".jpeg"}:
        composed.convert("RGB").save(output, quality=95)
    else:
        composed.save(output)

    if args.metadata:
        write_metadata(args, output, logo.size, xy)

    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
