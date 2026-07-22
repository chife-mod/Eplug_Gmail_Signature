#!/usr/bin/env python3
"""
Pixel-diff a rendered signature against its Figma reference.

Reports overall agreement plus a per-band breakdown, so a regression points at
the row it came from instead of just moving a single global number. Text
anti-aliasing between Chrome and Figma is never bit-identical, so the useful
signal is "which bands drifted", not "is the diff zero".

Usage: qa-diff.py <render.png> <reference.png> <diff-out.png>
"""
import sys
import numpy as np
from PIL import Image

TOL = 24        # per-channel delta below which a pixel counts as matching
BANDS = [       # (@1x y0, y1, label)
    (0, 24, "top padding"),
    (24, 96, "name / title / brand"),
    (96, 108, "gap"),
    (108, 262, "contact rows"),
    (24, 120, "logo band (right)"),
    (160, 190, "Recognition & Awards rule"),
    (190, 270, "award badges"),
    (286, 464, "VUE promo card"),
    (464, 488, "bottom padding"),
]


def main(render_path, ref_path, out_path):
    a = Image.open(render_path).convert("RGB")
    b = Image.open(ref_path).convert("RGB")
    if a.size != b.size:
        print(f"  size mismatch: render {a.size} vs reference {b.size}")
        w, h = min(a.width, b.width), min(a.height, b.height)
        a, b = a.crop((0, 0, w, h)), b.crop((0, 0, w, h))

    A = np.asarray(a).astype(np.int16)
    B = np.asarray(b).astype(np.int16)
    delta = np.abs(A - B).max(axis=2)
    match = delta <= TOL

    print(f"  overall match : {100 * match.mean():6.2f}%   "
          f"(mean |delta| {delta.mean():5.2f}, worst {delta.max()})")
    print("  per band:")
    for y0, y1, label in BANDS:
        band = match[y0 * 2:y1 * 2]
        if band.size:
            print(f"    {label:28s} {100 * band.mean():6.2f}%")

    # heat map: red where it differs, faded original elsewhere
    heat = (A * 0.25 + 190).astype(np.uint8)
    heat[~match] = [255, 0, 0]
    Image.fromarray(heat).save(out_path)
    print(f"  diff map      : {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
