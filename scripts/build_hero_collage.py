"""Rebuild assets/images/hero_collage.jpg, the homepage hero background.

Usage (from the repo root):
    pip install pillow
    python scripts/build_hero_collage.py

To update the collage with different/new photos: edit the PHOTOS list below
(paths are relative to the repo root, source images live in
assets/images/socials/), then re-run the script and commit the new
assets/images/hero_collage.jpg.

Each entry is a path, or a (path, vertical_centering) tuple if the default
crop doesn't frame the photo well. vertical_centering ranges 0-1: lower
values keep more of the top of the source image, higher values keep more of
the bottom (PIL's ImageOps.fit `centering` argument, y-axis only — see
https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit).
Default is 0.4 (leans slightly toward the top, since most group photos have
more headroom than legroom above the crop).
"""

from PIL import Image, ImageOps

PHOTOS = [
    "assets/images/socials/Beach_2024_1.jpeg",
    "assets/images/socials/CNY_2024_1.jpeg",
    "assets/images/socials/CNY_2024_3.jpeg",
    "assets/images/socials/Cricket.png",
    "assets/images/socials/LaserTag_1.png",
    "assets/images/socials/Mar_24_darts.jpg",
    ("assets/images/socials/TreeTop.jpeg", 0.58),  # crop leans down so people aren't dwarfed by the treehouse above them
    "assets/images/socials/CNY_2026.jpeg",
]

OUTPUT = "assets/images/hero_collage.jpg"
COLS, ROWS = 4, 2
TILE_W, TILE_H = 600, 400
GAP = 6
GAP_COLOR = (58, 26, 16)  # matches .hero background #3a1a10 in assets/css/main.css
DEFAULT_CENTERING_Y = 0.4


def build():
    canvas_w = COLS * TILE_W + (COLS - 1) * GAP
    canvas_h = ROWS * TILE_H + (ROWS - 1) * GAP
    canvas = Image.new("RGB", (canvas_w, canvas_h), GAP_COLOR)

    for i, entry in enumerate(PHOTOS):
        path, centering_y = entry if isinstance(entry, tuple) else (entry, DEFAULT_CENTERING_Y)

        img = Image.open(path)
        img = ImageOps.exif_transpose(img)  # respect phone photo rotation metadata
        img = img.convert("RGB")
        fitted = ImageOps.fit(img, (TILE_W, TILE_H), method=Image.LANCZOS, centering=(0.5, centering_y))

        col, row = i % COLS, i // COLS
        x, y = col * (TILE_W + GAP), row * (TILE_H + GAP)
        canvas.paste(fitted, (x, y))

    canvas.save(OUTPUT, quality=85, optimize=True)
    print(f"Saved {OUTPUT} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    build()
