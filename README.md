# Murmur website

Marketing site for [Murmur](https://murmur.netofficials.com), the private on-device speech-to-text app for iPhone, iPad, Mac and Apple Watch. Static HTML served by GitHub Pages from `docs/`.

## Layout

- `tools/content.py`: all copy (features, platforms, use cases, guides, FAQ, prices). Edit this first.
- `tools/build.py`: generates every page in `docs/`, plus `sitemap.xml`, `robots.txt`, `llms.txt`, `pricing.md`, `CNAME`.
- `tools/og.py`: draws the 1200×630 social images in `docs/assets/og/`.
- `tools/prep_images.py`: one-time conversion of the app's App Store screenshots to WebP.
- `tools/legal/`: Privacy Policy and Terms bodies (kept in step with the app repo's `docs/privacy` and `docs/terms`).
- `docs/assets/css/site.css`, `docs/assets/js/site.js`: styles and motion. Hand-written, not generated.

## Build

```bash
python tools/build.py --og
```

Needs Python 3.12+ and Pillow (only for `--og` and `prep_images.py`). Preview with `python -m http.server -d docs 8000`.

## When the app goes live

Set `app_store_url` in `tools/content.py` to the App Store link and rebuild. Every download button and the `SoftwareApplication` schema switch over.

## Design rules

Same as the app: solid and flat, dark only, no gradients, glows, blur or glass. Colours mirror `MurmurTheme`. All motion stops under Reduce Motion.

## Domain

`docs/CNAME` is `murmur.netofficials.com`. DNS needs a `CNAME` record for `murmur` pointing at `killoldesai.github.io`.
