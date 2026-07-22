#!/usr/bin/env python3
"""
Build the production @2x email assets for signature-2-v4.

Everything is sliced out of ONE full-frame @4x export of the Figma node
(`_src/frame-1-2282@4x.png`) rather than exported node by node.

That matters: exporting node 1:2332 on its own came back with the plain source
bitmap, while on the canvas that badge carries a colour treatment (mean red 63
in context vs 104 standalone) — the per-node export silently dropped it and the
pixel-diff lit up. Slicing the composed frame bakes in every blend, overlay and
clip exactly as the design renders, so an asset can never disagree with the
design it was cut from.

Crop rectangles are @1x frame coordinates, measured off the reference render by
template-matching (see qa/) — not guessed from layer metadata.

Encoder per asset, because a signature is fetched on every open and the whole
set should stay well under ~100 KB:
  * PNG  for icons, logo and the VUE lockup — hard edges, flat colour.
  * JPEG for the award photos and the card background — continuous tone, where
         PNG costs ~12x the bytes for no visible gain.

Run: python3 scripts/build-assets.py
"""
import pathlib
from PIL import Image

D = pathlib.Path("public/assets/images/sig-ep")
MASTER = D / "_src" / "frame-1-2282@4x.png"
SRC_SCALE = 4    # master export scale
OUT_SCALE = 2    # production scale

# name -> (x, y, w, h) in @1x frame coordinates, and encoder
SLICES = [
    ("chip-mail",     (24,    108, 18,  18),  "png"),
    ("chip-phone",    (24,    134, 18,  18),  "png"),
    ("chip-pin",      (24,    176, 18,  18),  "png"),
    ("chip-globe",    (24,    218, 18,  18),  "png"),
    ("chip-linkedin", (24,    244, 18,  18),  "png"),
    ("ep-logo",       (347.5,  73, 130, 47),  "png"),
    # rule / "Recognition & Awards" / rule as one slice: the table build-out of
    # two nested 3-row rule tables cost ~1.3K chars against Gmail's 10K cap
    ("ra-header",     (249,   169, 327, 14),  "png"),
    ("award-1",       (249,   197, 67,  67),  "jpg"),
    ("award-2",       (322.5, 197, 67,  67),  "jpg"),
    ("award-3",       (395.5, 197, 87,  67),  "jpg"),
    ("award-4",       (489,   197, 87,  67),  "jpg"),
    # The whole VUE promo card, text and CTA included, shipped as ONE linked
    # image. Three audit findings converge on this: (a) Gmail's signature editor
    # caps signatures at 10,000 chars and the table-built card alone was ~9K of
    # markup; (b) Gmail web deletes any style attribute containing
    # background-image:url(), taking border-radius with it; (c) drawing live
    # HTML text over a background that already contains the same text produces
    # ghosting at any rendering difference. A flat <img> sidesteps all three.
    # Cut with the frame's white page behind it, so the rounded corners arrive
    # pre-composited and survive clients that drop border-radius.
    ("vue-card",      (24,    286, 552, 178), "jpg"),
]

QUALITY = {"vue-card": 92}


def slice_asset(master, box, out_w, out_h):
    x, y, w, h = box
    crop = master.crop((round(x * SRC_SCALE), round(y * SRC_SCALE),
                        round((x + w) * SRC_SCALE), round((y + h) * SRC_SCALE)))
    return crop.resize((out_w, out_h), Image.LANCZOS)


if __name__ == "__main__":
    master = Image.open(MASTER).convert("RGB")
    expected = (600 * SRC_SCALE, 488 * SRC_SCALE)
    assert master.size == expected, f"master is {master.size}, expected {expected}"

    total = 0
    for name, box, fmt in SLICES:
        w, h = box[2] * OUT_SCALE, box[3] * OUT_SCALE
        img = slice_asset(master, box, w, h)
        if fmt == "png":
            path = D / f"{name}.png"
            img.save(path, optimize=True)
        else:
            path = D / f"{name}.jpg"
            img.save(path, quality=QUALITY.get(name, 88), optimize=True)
        kb = path.stat().st_size / 1024
        total += kb
        print(f"  {path.name:20s} {w:4d}x{h:<4d} {kb:7.1f} KB")
    print(f"  {'':20s} {'':9s} {'-' * 10}")
    print(f"  {'TOTAL':20s} {'':9s} {total:7.1f} KB")
