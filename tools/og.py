"""Draws 1200x630 social preview images in the flat Murmur style."""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BG, SURFACE, ACCENT, RECORD, TEXT, TEXT3 = "#111116", "#1C1C23", "#5EE0C6", "#FF5A6E", "#F4F3F8", "#8F8D9C"
FONTS = Path("C:/Windows/Fonts")


def font(bold, size):
    for name in (["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]):
        try:
            return ImageFont.truetype(str(FONTS / name), size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def wrap(draw, text, fnt, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        test = (line + " " + w).strip()
        if draw.textlength(test, font=fnt) <= width:
            line = test
        else:
            lines.append(line)
            line = w
    lines.append(line)
    return lines


def draw_logo(d, x, y, s):
    d.rounded_rectangle([x, y, x + s, y + s], radius=s * 0.22, fill="#17161B", outline="#2A2A33", width=2)
    k = s / 1024
    for cx, top, bot in [(266, 276, 748), (389, 358, 635), (512, 460, 563), (635, 358, 635), (758, 276, 748)]:
        d.line([x + cx * k, y + top * k, x + cx * k, y + bot * k], fill=ACCENT, width=max(2, round(76 * k)))
        r = 38 * k
        for yy in (top, bot):
            d.ellipse([x + cx * k - r, y + yy * k - r, x + cx * k + r, y + yy * k + r], fill=ACCENT)


def draw_one(title, kicker, dest):
    im = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(im)
    draw_logo(d, 72, 64, 72)
    d.text((164, 78), "Murmur", font=font(True, 40), fill=TEXT)
    d.text((72, 186), kicker.upper(), font=font(True, 24), fill=ACCENT)
    size = 76
    while True:
        f = font(True, size)
        lines = wrap(d, title, f, 1050)
        if len(lines) <= 3 or size <= 48:
            break
        size -= 6
    y = 228
    for ln in lines[:3]:
        d.text((72, y), ln, font=f, fill=TEXT)
        y += int(size * 1.15)
    n, x0, gap = 110, 0, 1200 / 110
    for i in range(n):
        env = math.sin(math.pi * i / (n - 1)) ** 1.4
        h = 6 + env * 70 * (0.45 + 0.55 * abs(math.sin(i * 1.7) * math.cos(i * 0.37)))
        cx = x0 + i * gap + gap / 2
        d.rounded_rectangle([cx - 2.5, 572 - h / 2, cx + 2.5, 572 + h / 2], radius=2, fill=RECORD)
    d.text((1128, 186), "On-device · Private · Offline", font=font(False, 22), fill=TEXT3, anchor="ra")
    im.save(dest, "PNG", optimize=True)


def draw_all(items, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    seen = set()
    for name, title, kicker in items:
        if name in seen:
            continue
        seen.add(name)
        draw_one(title, kicker, out_dir / f"{name}.png")
    print(f"drew {len(seen)} social images")
