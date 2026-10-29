"""One-time image prep: App Store screenshots -> WebP, app icon -> favicons.

Usage: python tools/prep_images.py <path to the murmur app repo>
Reads iphone/, ipad-13/, mac/, watch/ and store/icon-1024.png from the app repo.
"""
import sys
from pathlib import Path
from PIL import Image

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "../murmur")
OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "img"
SHOTS = OUT / "shots"
SHOTS.mkdir(parents=True, exist_ok=True)

# folder -> (output prefix, target width)
SETS = {"iphone": ("iphone", 640), "ipad-13": ("ipad", 1000), "mac": ("mac", 1600), "watch": ("watch", 416)}

for folder, (prefix, width) in SETS.items():
    for png in sorted((SRC / folder).glob("*.png")):
        im = Image.open(png).convert("RGB")
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        name = png.stem.split("-", 1)[1]  # "2-note" -> "note"
        name = name.removeprefix("ipad-").removeprefix("mac-").removeprefix("watch-")
        dest = SHOTS / f"{prefix}-{name}.webp"
        im.save(dest, "WEBP", quality=82, method=6)
        print(dest.name, im.size, dest.stat().st_size // 1024, "KB")

icon = Image.open(SRC / "store" / "icon-1024.png").convert("RGBA")
for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    icon.resize((size, size), Image.LANCZOS).save(OUT / name, optimize=True)
print("icons done")
