"""Builds the static site into docs/ from tools/content.py.

Usage: python tools/build.py          (pages, sitemap, robots, llms.txt)
       python tools/build.py --og     (also redraws the social preview images)
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

from content import SITE, PRICES, LANGUAGES, FEATURES, PLATFORMS, USE_CASES, GUIDES, FAQ

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
TOOLS = Path(__file__).resolve().parent
D = SITE["domain"]
FEAT = {f["slug"]: f for f in FEATURES}
esc = html.escape


def plain(s):
    return re.sub(r"<[^>]+>", "", s)


# ------------------------------------------------------------------ icons
ICONS = {
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4M8 22h8"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "cloud": '<path d="M17.5 19H7a5 5 0 1 1 1.1-9.9A6 6 0 0 1 19.6 11 4 4 0 0 1 17.5 19z"/>',
    "upload": '<path d="M12 15V3M7 8l5-5 5 5"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>',
    "sparkles": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0"/><path d="M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/>',
    "edit": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
    "share": '<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M16 6l-4-4-4 4M12 2v13"/>',
    "sync": '<path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 12a9 9 0 0 1 15.5-6.2L21 8"/><path d="M21 3v5h-5M3 21v-5h5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    "wave": '<path d="M4 10v4M8 6v12M12 9v6M16 5v14M20 10v4"/>',
    "watch": '<rect x="6" y="6" width="12" height="12" rx="3"/><path d="M9 6l1-4h4l1 4M9 18l1 4h4l1-4"/>',
    "phone": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
    "tablet": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M11 18h2"/>',
    "laptop": '<rect x="4" y="4" width="16" height="11" rx="2"/><path d="M2 19h20"/>',
    "plane": '<path d="M2 16l20-6-20-6 4 6z"/><path d="M6 10h8"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "captions": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M7 15h4M15 15h2M7 11h2M13 11h4"/>',
    "graduation": '<path d="M22 10L12 5 2 10l10 5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "bookmark": '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "nocloud": '<path d="M2 2l20 20"/><path d="M5.8 8.1A6 6 0 0 0 7 20h10m3.3-1.6A4.5 4.5 0 0 0 17.5 11h-.7A6 6 0 0 0 9.5 6.4"/>',
}


def icon(name, cls=""):
    return (f'<span class="icon {cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></span>')


def svg(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# ------------------------------------------------------------------ pieces
def store_button(cls="btn"):
    if SITE["app_store_url"]:
        return f'<a class="{cls}" href="{SITE["app_store_url"]}">{svg("phone")}Download on the App Store</a>'
    return f'<a class="{cls}" href="/pricing/">{svg("phone")}Coming soon to the App Store</a>'


def wave(bars=72, cls=""):
    return f'<div class="wave {cls}" data-bars="{bars}" aria-hidden="true"></div>'


def section_head(eyebrow, h2, lead="", center=True, rec=False):
    c = " center" if center else ""
    e = ' rec' if rec else ''
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="head{c}" data-reveal><span class="eyebrow{e}">{eyebrow}</span><h2>{h2}</h2>{lead_html}</div>'


def answer_box(q, a):
    return f'<div class="answer-box" data-reveal><strong>{esc(q)}</strong><p>{esc(a)}</p></div>'


def faq_block(faqs, title="Frequently asked questions", eyebrow="FAQ"):
    items = "".join(
        f'<details data-reveal style="--i:{i % 4}"><summary>{esc(q)}</summary><div class="answer"><p>{esc(a)}</p></div></details>'
        for i, (q, a) in enumerate(faqs))
    return f'<section class="section tight" aria-labelledby="faq-h"><div class="wrap">' \
           f'<div class="head center" data-reveal><span class="eyebrow">{eyebrow}</span><h2 id="faq-h">{title}</h2></div>' \
           f'<div class="faq">{items}</div></div></section>'


def feature_card(f, i=0):
    return (f'<a class="card" href="/features/{f["slug"]}/" data-reveal style="--i:{i % 4}">{icon(f["icon"], f["color"])}'
            f'<h3>{esc(f["name"])}</h3><p>{esc(f["card"])}</p><span class="more">Learn more</span></a>')


def related(slugs, title="Related features"):
    cards = "".join(feature_card(FEAT[s], i) for i, s in enumerate(slugs))
    return f'<section class="section tight"><div class="wrap">{section_head("Keep exploring", title)}<div class="grid g3">{cards}</div></div></section>'


def cta_band(h2="Your words stay yours.", lead="Record, transcribe and summarize on your own device. No account, no uploads, works offline."):
    return (f'<section class="section tight"><div class="wrap"><div class="cta-band" data-reveal>'
            f'<span class="eyebrow">Murmur for iPhone, iPad, Mac and Apple Watch</span><h2>{h2}</h2><p class="lead">{lead}</p>'
            f'<div class="btn-row" style="justify-content:center">{store_button()}<a class="btn ghost" href="/features/">See all features</a></div>'
            f'<p class="store-note">Free to download. Pro from {PRICES["monthly"]} a month, {PRICES["yearly"]} a year with a {PRICES["trial_days"]}-day free trial, or {PRICES["lifetime"]} once.</p>'
            f'{wave(90, "small")}</div></div></section>')


def crumbs_html(crumbs):
    items = ['<li><a href="/">Home</a></li>']
    for i, (name, path) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li><span aria-current="page">{esc(name)}</span></li>')
        else:
            items.append(f'<li><a href="{path}">{esc(name)}</a></li>')
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def shot_img(name, alt, kind="phone", eager=False):
    sizes = {"phone": (640, 1391), "tablet": (1000, 1333), "wide": (1600, 1000), "watch": (416, 496)}
    w, h = sizes[kind]
    cls = {"phone": "shot phone-shot", "tablet": "shot", "wide": "shot", "watch": "shot watch-shot"}[kind]
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="{cls}" style="margin:0"><img src="/assets/img/shots/{name}.webp" width="{w}" height="{h}" '
            f'alt="{esc(alt)}" {loading} decoding="async"></figure>')


# ------------------------------------------------------------------ motion graphics
def viz(kind):
    if kind == "transcribe":
        return ('<div class="viz viz-transcribe" aria-hidden="true"><span class="viz-label">Transcribing on this device</span>'
                f'{wave(48, "small accent")}<div class="words">Okay, let\'s start with the Q4 roadmap. The big question is Watch first or sync first.</div>'
                '<div class="meter"><span>Whisper Large v3 Turbo</span><span class="bar"><i></i></span><span class="pct">0%</span></div></div>')
    if kind == "offline":
        return ('<div class="viz viz-offline" aria-hidden="true"><span class="plane">Airplane mode <span class="tog"></span></span>'
                f'<div class="row"><div class="node"><div>{svg("phone")}Your device</div></div>'
                '<div class="path"><i></i><i></i><i></i><span class="wall"></span></div>'
                f'<div class="node cloud"><div>{svg("cloud")}Servers</div></div></div>'
                '<p class="caption">Audio never leaves your device. There is no server to send it to.</p></div>')
    if kind == "record":
        flags = "".join(f'<span class="flag" style="left:{x}%;animation-delay:{d}s"></span>' for x, d in [(22, 0), (51, 1.2), (78, 2.4)])
        return ('<div class="viz viz-record" aria-hidden="true"><span class="viz-label">Recording</span>'
                '<div class="rec-btn"><span></span></div><div class="timer" data-timer>00:00</div>'
                f'<div class="timeline">{flags}{wave(64, "small")}</div></div>')
    if kind == "summary":
        todos = "".join(f'<div class="todo" style="--d:{d}s"><span class="box"></span>{t}</div>'
                        for t, d in [("Priya shares the updated timeline by Friday", 0), ("Jordan starts the migration spike", .3), ("Alex books the design review", .6)])
        return ('<div class="viz viz-summary" aria-hidden="true"><span class="viz-label">Meeting summary</span>'
                '<div class="lines" style="margin-top:16px"><i></i><i></i><i></i><i></i></div>'
                f'<div class="sum-card"><h5>Action items</h5>{todos}</div></div>')
    if kind == "search":
        return ('<div class="viz viz-search" aria-hidden="true"><span class="viz-label">Search all notes</span>'
                f'<div class="field" style="margin-top:14px">{svg("search")}<span class="typed">roadmap</span></div>'
                '<div class="doc"><p><small class="count">Product sync · 00:04</small><br>Okay, let\'s start with the Q4 <mark>roadmap</mark>.</p>'
                '<p><small class="count">Planning call · 12:41</small><br>Put the <mark>roadmap</mark> in the shared folder.</p>'
                '<p><small class="count">Team offsite · 03:15</small><br>The <mark>roadmap</mark> for next year starts with Mac.</p></div></div>')
    if kind == "export":
        files = "".join(f'<div class="file {c}"><i></i><i></i><b>{t}</b></div>' for c, t in [("f1", "TXT"), ("f2", "MD"), ("f3", "SRT"), ("f4", "M4A")])
        return f'<div class="viz viz-export" aria-hidden="true"><span class="viz-label">Export</span><div class="files">{files}</div></div>'
    if kind == "dictionary":
        return ('<div class="viz viz-dict" aria-hidden="true"><span class="viz-label">Custom dictionary</span>'
                '<div class="sentence">We moved the cluster to <span class="swap"><span class="bad">cube or nettys</span><span class="good">Kubernetes</span></span> '
                'after <span class="swap"><span class="bad">Shiv on</span><span class="good">Siobhan</span></span> signed off.</div>'
                '<div class="dict-words"><span class="chip">Kubernetes</span><span class="chip">Siobhan</span><span class="chip">CloudKit</span><span class="chip plain">+ Add word</span></div></div>')
    if kind == "sync":
        return ('<div class="viz viz-sync" aria-hidden="true"><div class="sync-wrap">'
                '<svg class="lines" viewBox="0 0 420 260" preserveAspectRatio="none"><path d="M210 76 L48 184"/><path d="M210 76 L210 184"/><path d="M210 76 L372 184"/>'
                '<path class="flow" d="M210 76 L48 184"/><path class="flow" d="M210 76 L210 184"/><path class="flow" d="M210 76 L372 184"/></svg>'
                f'<div class="sync-node top"><div>{svg("cloud")}Your iCloud</div></div>'
                f'<div class="sync-node l"><div>{svg("phone")}iPhone</div></div><div class="sync-node m"><div>{svg("tablet")}iPad</div></div>'
                f'<div class="sync-node r"><div>{svg("laptop")}Mac</div></div></div></div>')
    if kind == "import":
        items = "".join(f'<div class="queue-item" style="--d:{d}s"><span class="ft">{t}</span><span class="nm">{n}<small>{s}</small><span class="pg"><i style="--d:{d}s"></i></span></span></div>'
                        for t, n, s, d in [("MP4", "Team offsite.mp4", "Video · 48 min", 0), ("M4A", "Interview with Dana.m4a", "Audio · 32 min", .5), ("WAV", "Lecture 8.wav", "Audio · 1 h 12 min", 1)])
        return f'<div class="viz viz-import" aria-hidden="true"><span class="viz-label" style="margin-bottom:14px">Import queue</span>{items}</div>'
    if kind == "speakers":
        rows = "".join(f'<div class="spk"><div class="top"><span style="color:{c}">{n}</span><span class="small">{w}%</span></div><div class="tbar"><i style="--w:{w}%;background:{c}"></i></div></div>'
                       for n, w, c in [("Alex", 35, "var(--accent)"), ("Jordan", 35, "var(--lilac)"), ("Priya", 30, "var(--amber)")])
        return f'<div class="viz" aria-hidden="true"><span class="viz-label" style="margin-bottom:18px">Talk time</span><div class="spk-group">{rows}</div></div>'
    if kind == "watch":
        return ('<div class="viz viz-watch" aria-hidden="true"><div class="wp"><div class="watch"><div class="rec-btn"><span></span></div></div>'
                '<div class="path"><i></i></div><div class="mini-phone"><i></i><i style="width:70%"></i><i class="new"></i><i style="width:80%"></i></div></div>'
                '<p class="caption small" style="margin-top:20px">Recorded on the watch, transcribed on the iPhone.</p></div>')
    raise ValueError(kind)


# ------------------------------------------------------------------ schema
def org():
    return {"@type": "Organization", "@id": f"{D}/#org", "name": "Murmur", "url": f"{D}/",
            "logo": {"@type": "ImageObject", "url": f"{D}/assets/img/icon-512.png", "width": 512, "height": 512}}


def website():
    return {"@type": "WebSite", "@id": f"{D}/#website", "name": "Murmur", "url": f"{D}/",
            "description": SITE["tagline"], "publisher": {"@id": f"{D}/#org"}, "inLanguage": "en-US"}


def software_app():
    offers = [
        {"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD", "description": "First 2 minutes of every note"},
        {"@type": "Offer", "name": "Murmur Pro Yearly", "price": PRICES["yearly"].strip("$"), "priceCurrency": "USD",
         "description": f"Billed yearly, {PRICES['trial_days']}-day free trial"},
        {"@type": "Offer", "name": "Murmur Pro Monthly", "price": PRICES["monthly"].strip("$"), "priceCurrency": "USD", "description": "Billed monthly"},
        {"@type": "Offer", "name": "Murmur Pro Lifetime", "price": PRICES["lifetime"].strip("$"), "priceCurrency": "USD", "description": "One-time purchase"},
    ]
    app = {"@type": "SoftwareApplication", "@id": f"{D}/#app", "name": "Murmur: Private Transcription",
           "alternateName": "Murmur", "applicationCategory": "BusinessApplication", "applicationSubCategory": "Transcription",
           "operatingSystem": "iOS, iPadOS, macOS 15 or later, watchOS 11 or later",
           "description": "On-device speech-to-text with Whisper for iPhone, iPad, Mac and Apple Watch. No account, no uploads, works offline.",
           "url": f"{D}/", "image": f"{D}/assets/img/icon-512.png", "publisher": {"@id": f"{D}/#org"},
           "offers": offers, "inLanguage": "en", "featureList": [f["name"] for f in FEATURES]}
    if SITE["app_store_url"]:
        app["downloadUrl"] = SITE["app_store_url"]
    return app


def schema_graph(page):
    url = D + "/" + page["path"]
    graph = [org(), website()]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{D}/"}]
    for i, (name, path) in enumerate(page.get("crumbs", [])):
        crumbs.append({"@type": "ListItem", "position": i + 2, "name": name, "item": D + path})
    webpage = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": page["title"], "description": page["desc"],
               "isPartOf": {"@id": f"{D}/#website"}, "inLanguage": "en-US", "dateModified": SITE["updated"],
               "primaryImageOfPage": {"@type": "ImageObject", "url": f"{D}/assets/og/{page['og']}.png"}}
    if page.get("crumbs"):
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": crumbs})
        webpage["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if page.get("app"):
        graph.append(software_app())
        webpage["about"] = {"@id": f"{D}/#app"}
    if page.get("article"):
        graph.append({"@type": "Article", "@id": url + "#article", "headline": page["title"], "description": page["desc"],
                      "image": f"{D}/assets/og/{page['og']}.png", "datePublished": SITE["updated"], "dateModified": SITE["updated"],
                      "author": {"@id": f"{D}/#org"}, "publisher": {"@id": f"{D}/#org"}, "mainEntityOfPage": {"@id": url + "#webpage"}})
    if page.get("faqs"):
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faqs"]]})
    graph.append(webpage)
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


# ------------------------------------------------------------------ layout
NAV = [("Features", "/features/"), ("Platforms", "/platforms/"), ("Use cases", "/use-cases/"),
       ("Guides", "/guides/"), ("Pricing", "/pricing/"), ("FAQ", "/faq/")]


def header(active):
    links = "".join(f'<a href="{href}"{" aria-current=\"page\"" if active == href else ""}>{name}</a>' for name, href in NAV)
    get = SITE["app_store_url"] or "/pricing/"
    return (f'<header class="site-head"><div class="wrap"><a class="brand" href="/" aria-label="Murmur home">'
            f'<img src="/assets/img/favicon.svg" width="32" height="32" alt="">Murmur</a>'
            f'<button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>'
            f'<nav class="nav" id="nav" aria-label="Main">{links}<a class="btn sm" href="{get}">Get Murmur</a></nav></div></header>')


def footer():
    def col(title, items):
        lis = "".join(f'<li><a href="{h}">{esc(n)}</a></li>' for n, h in items)
        return f'<div><h2>{title}</h2><ul>{lis}</ul></div>'
    return ('<footer class="site-foot"><div class="wrap"><div class="foot-grid">'
            '<div><a class="brand" href="/"><img src="/assets/img/favicon.svg" width="32" height="32" alt="">Murmur</a>'
            '<p class="small" style="margin-top:14px;max-width:300px">Private speech to text with Whisper on your own iPhone, iPad, Mac and Apple Watch. No account, no uploads.</p></div>'
            + col("Product", [("All features", "/features/"), ("Pricing", "/pricing/"), ("FAQ", "/faq/"), ("Support", "/support/")])
            + col("Features", [(f["name"], f"/features/{f['slug']}/") for f in FEATURES[:7]])
            + col("Platforms", [(p["name"], f"/{p['slug']}/") for p in PLATFORMS])
            + col("Use cases", [(u["name"], f"/use-cases/{u['slug']}/") for u in USE_CASES])
            + col("Guides", [(g["nav"], f"/guides/{g['slug']}/") for g in GUIDES])
            + '</div><div class="foot-bottom"><span>© <span data-year>2026</span> Murmur. Made for Apple devices. Apple, iPhone, iPad, Mac and Apple Watch are trademarks of Apple Inc.</span>'
            '<span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/support/">Support</a></span></div></div></footer>')


def layout(page, body):
    url = D + "/" + page["path"]
    og = f"{D}/assets/og/{page['og']}.png"
    title = page["title"] if page["path"] == "" else f'{page["title"]} | Murmur'
    if len(title) > 62:
        title = page["title"]
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(page['desc'])}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#111116">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="{'article' if page.get('article') else 'website'}">
<meta property="og:site_name" content="Murmur">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(page['title'])}">
<meta name="twitter:description" content="{esc(page['desc'])}">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="text/plain" href="/llms.txt" title="LLM summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={SITE['updated']}">
<script type="application/ld+json">{schema_graph(page)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(page.get('nav', ''))}
<main id="main">
{crumbs_html(page['crumbs']) if page.get('crumbs') else ''}
{body}
</main>
{footer()}
<script src="/assets/js/site.js?v={SITE['updated']}" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ page bodies
def hero_sub(eyebrow, h1, lead, q=None, a=None, buttons=True, chips=None):
    b = f'<div class="btn-row" style="justify-content:center">{store_button()}<a class="btn ghost" href="/pricing/">See pricing</a></div>' if buttons else ""
    c = ""
    if chips:
        c = '<div class="chips" style="margin-top:24px">' + "".join(f'<span class="chip"><span class="dot"></span>{x}</span>' for x in chips) + "</div>"
    ans = f'<div style="margin-top:44px">{answer_box(q, a)}</div>' if q else ""
    return (f'<section class="hero hero-sub"><div class="wrap center hero-copy"><span class="eyebrow">{eyebrow}</span>'
            f'<h1>{h1}</h1><p class="lead">{lead}</p>{b}{c}</div><div class="wrap">{ans}</div></section>')


def home_body():
    t_lines = [
        ("Alex", "var(--accent)", "00:04", "Okay, let's start with the Q4 roadmap. The big question is Watch first or sync first."),
        ("Priya", "var(--amber)", "00:15", "Watch is smaller, and it's the most requested feature in support emails."),
        ("Jordan", "var(--lilac)", "00:24", "Sync needs CloudKit migration work. That's at least three weeks on its own."),
        ("Alex", "var(--accent)", "00:33", "Then Watch first, and we move sync to December."),
    ]
    lines = "".join(f'<div class="tline"><b style="color:{c}">● {n}</b><small>{t}</small><p>{esc(x)}</p></div>' for n, c, t, x in t_lines)
    phone = (f'<div class="device-stage"><div class="phone" data-live-transcript aria-hidden="true"><div class="phone-top"><span>9:41</span><span>●●●</span></div>'
             f'<h4>Product sync</h4><p class="meta">Oct 28 · 42:10 · 3 speakers</p><div class="seg"><span class="on">Transcript</span><span>Summary</span></div>'
             f'{lines}<div class="phone-bar"><span class="play"></span><span class="track"><i></i></span><span class="small">1×</span></div></div>'
             f'<div class="float-card f1" aria-hidden="true"><span class="ic">{svg("plane")}</span>Works in airplane mode</div>'
             f'<div class="float-card f2" aria-hidden="true"><span class="ic">{svg("lock")}</span>0 bytes uploaded</div>'
             f'<div class="float-card f3" aria-hidden="true"><span class="ic">{svg("sparkles")}</span>Summary ready</div></div>')
    hero = (f'<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">'
            f'<span class="eyebrow rec">On-device Whisper transcription</span>'
            f'<h1>Speech to text that <span class="hl">never leaves</span> your device.</h1>'
            f'<p class="lead">Murmur records and transcribes meetings, lectures, interviews and voice notes with Whisper running on your iPhone, iPad, Mac or Apple Watch. No account. No uploads. Works offline.</p>'
            f'<div class="btn-row">{store_button()}<a class="btn ghost" href="#how">See how it works</a></div>'
            f'<div class="chips"><span class="chip"><span class="dot"></span>Private · Offline</span><span class="chip"><span class="dot"></span>No account</span><span class="chip plain">iPhone · iPad · Mac · Watch</span></div>'
            f'</div>{phone}</div><div class="hero-wave">{wave(140)}</div></section>')

    words = ["Meetings", "Lectures", "Interviews", "Voice notes", "Podcasts", "Subtitles", "Research", "Journaling", "Sermons", "Field notes"]
    marquee = '<div class="marquee" aria-hidden="true"><div class="marquee-track">' + "".join(f"<span>{w}</span>" for w in words * 2) + "</div></div>"

    stats = ('<section class="section tight"><div class="wrap"><div class="stats">'
             '<div class="stat" data-reveal><strong data-count="0">0</strong><span>servers that see your audio</span></div>'
             '<div class="stat" data-reveal style="--i:1"><strong data-count="0">0</strong><span>accounts to create</span></div>'
             f'<div class="stat" data-reveal style="--i:2"><strong data-count="{len(LANGUAGES)}">{len(LANGUAGES)}</strong><span>languages, plus auto-detect</span></div>'
             '<div class="stat" data-reveal style="--i:3"><strong data-count="4">4</strong><span>Apple devices, one purchase</span></div>'
             '</div></div></section>')

    how = (f'<section class="section" id="how"><div class="wrap">{section_head("How it works", "From voice to searchable text <span class=\"hl\">in three steps</span>", "Murmur downloads its Whisper model once. After that every step happens on your device.")}'
           '<div class="reveal-group"><div class="progress-line"><i></i></div><div class="steps">'
           '<div class="step" data-reveal><h3>Record or import</h3><p>Tap the record button, drop bookmarks as you go, or bring in audio and video from Files, Photos and other apps.</p></div>'
           '<div class="step" data-reveal style="--i:1"><h3>Whisper transcribes on device</h3><p>Whisper Large v3 Turbo turns speech into timestamped lines on your Neural Engine. Nothing is uploaded.</p></div>'
           '<div class="step" data-reveal style="--i:2"><h3>Read, search, summarize, share</h3><p>Tap a line to replay it, search every note, get an on-device summary and export to text, Markdown or SRT.</p></div>'
           '</div></div></div></section>')

    privacy = (f'<section class="section alt"><div class="wrap split"><div data-reveal>'
               f'<span class="eyebrow">Private by design</span><h2>Your recordings <span class="hl">stay with you</span></h2>'
               f'<p class="lead">Most transcription apps upload your audio to their servers. Murmur runs the speech model on your device instead, so there is nothing to upload and nobody to trust.</p>'
               f'<ul class="checks"><li><span><strong>No account, no analytics, no ads.</strong> The App Store privacy label is Data Not Collected.</span></li>'
               f'<li><span><strong>Works in airplane mode</strong> after a one-time model download.</span></li>'
               f'<li><span><strong>Optional iCloud sync</strong> uses your own private iCloud, never a server of ours.</span></li></ul>'
               f'<div class="btn-row" style="margin-top:28px"><a class="btn ghost" href="/features/private-by-design/">How Murmur protects your privacy</a></div>'
               f'</div><div data-reveal style="--i:1">{viz("offline")}</div></div></section>')

    feats = "".join(feature_card(f, i) for i, f in enumerate(FEATURES[2:11]))
    features = (f'<section class="section"><div class="wrap">{section_head("Features", "Everything you need <span class=\"hl\">after you hit record</span>", "Murmur is a complete transcription workspace: capture, transcript, summary, search and export.")}'
                f'<div class="grid g3">{feats}</div><div class="center" style="margin-top:36px"><a class="btn ghost" href="/features/">Explore all features</a></div></div></section>')

    showcase = (f'<section class="section tight"><div class="wrap"><div class="split"><div data-reveal>{viz("summary")}</div><div data-reveal style="--i:1">'
                f'<span class="eyebrow">Private AI summaries</span><h2>Action items, <span class="hl">without the cloud</span></h2>'
                f'<p class="lead">On devices with Apple Intelligence, Murmur turns a transcript into a Meeting, Lecture or Bullet point summary with a checklist of action items, made on the device.</p>'
                f'<a class="btn ghost" href="/features/ai-summaries/">About summaries</a></div></div>'
                f'<div class="split rev" style="margin-top:clamp(64px,9vw,120px)"><div data-reveal>{viz("search")}</div><div data-reveal style="--i:1">'
                f'<span class="eyebrow">Search</span><h2>Find the moment <span class="hl">someone said it</span></h2>'
                f'<p class="lead">Search every transcript and summary at once. Each hit shows its timestamp, and one tap plays it.</p>'
                f'<a class="btn ghost" href="/features/search/">About search</a></div></div></div></section>')

    tabs, panels = [], []
    for i, p in enumerate(PLATFORMS):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button role="tab" id="tab-{p["slug"]}" aria-controls="panel-{p["slug"]}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{p["name"]}</button>')
        main_shot = shot_img(p["shots"][0][0], f'Murmur on {p["name"]}: {p["shots"][0][1]}', p["kind"])
        pts = "".join(f'<li><span><strong>{esc(t)}.</strong> {esc(d)}</span></li>' for t, d in p["points"][:4])
        panels.append(f'<div class="tab-panel split{" on" if i == 0 else ""}" role="tabpanel" id="panel-{p["slug"]}" aria-labelledby="tab-{p["slug"]}"{"" if i == 0 else " hidden"}>'
                      f'<div>{main_shot}</div><div><h3 style="font-size:32px">{p["h1"]}</h3><p class="lead">{esc(p["lead"])}</p><ul class="checks">{pts}</ul>'
                      f'<div class="btn-row" style="margin-top:28px"><a class="btn ghost" href="/{p["slug"]}/">Murmur for {p["name"]}</a></div></div></div>')
    platforms = (f'<section class="section alt"><div class="wrap">{section_head("Every Apple device", "One app. <span class=\"hl\">Four devices.</span>", "Buy Pro once and it works on your iPhone, iPad and Mac. Apple Watch records and sends to your iPhone.")}'
                 f'<div class="center" data-tabs><div class="tabs" role="tablist" aria-label="Platforms">{"".join(tabs)}</div></div>'
                 f'<div style="text-align:left">{"".join(panels)}</div></div></section>')

    ucs = "".join(f'<a class="card" href="/use-cases/{u["slug"]}/" data-reveal style="--i:{i}">{icon(u["icon"], ["", "c1", "c2", "c3", "c4"][i % 5])}<h3>{u["name"]}</h3><p>{esc(u["desc"])}</p><span class="more">Learn more</span></a>'
                  for i, u in enumerate(USE_CASES))
    use_cases = f'<section class="section"><div class="wrap">{section_head("Use cases", "Made for the moments <span class=\"hl\">you cannot repeat</span>")}<div class="grid g3">{ucs}' \
                f'<a class="card" href="/guides/" data-reveal style="--i:5">{icon("file", "c5")}<h3>Guides</h3><p>Step-by-step how-tos for Voice Memos, Mac, subtitles and more.</p><span class="more">Read the guides</span></a></div></div></section>'

    compare = (f'<section class="section tight"><div class="wrap">{section_head("On-device vs cloud", "Why on-device <span class=\"hl\">matters</span>")}'
               '<div class="table-wrap" data-reveal><table><thead><tr><th></th><th class="us">Murmur (on device)</th><th>Typical cloud transcription</th></tr></thead><tbody>'
               '<tr><td>Where your audio goes</td><td class="us yes">Stays on your device</td><td>Uploaded to a server</td></tr>'
               '<tr><td>Works offline</td><td class="us yes">Yes</td><td>No</td></tr>'
               '<tr><td>Account required</td><td class="us yes">No</td><td>Usually</td></tr>'
               '<tr><td>Summaries</td><td class="us yes">On device, with Apple Intelligence</td><td>Server-side AI</td></tr>'
               '<tr><td>Pricing</td><td class="us">Free to try, Pro from $3.99/month or $39.99 once</td><td>Often per minute or per seat</td></tr>'
               '</tbody></table></div><p class="center small" style="margin-top:16px"><a href="/guides/on-device-vs-cloud-transcription/">Read the full comparison</a></p></div></section>')

    return hero + marquee + stats + how + privacy + features + showcase + platforms + use_cases + compare + pricing_cards(compact=True) + faq_block(FAQ[:8]) + cta_band()


def pricing_cards(compact=False):
    perks = ["Full transcripts of every note", "Edit, find and replace", "Export TXT, Markdown, SRT, audio", "On-device summaries", "iPhone, iPad and Mac"]
    lis = "".join(f"<li>{p}</li>" for p in perks)
    get = SITE["app_store_url"] or "/pricing/"
    btn = "Start free trial" if SITE["app_store_url"] else "Coming soon"
    plans = (f'<div class="plan" data-reveal><h3>Monthly</h3><div class="price">{PRICES["monthly"]}<small>/month</small></div><p class="note">Flexible. Cancel any time.</p><ul>{lis}</ul><a class="btn ghost" href="{get}">{"Choose monthly" if SITE["app_store_url"] else btn}</a></div>'
             f'<div class="plan best" data-reveal style="--i:1"><span class="badge">Best value</span><h3>Yearly</h3><div class="price">{PRICES["yearly"]}<small>/year</small></div><p class="note">{PRICES["trial_days"]}-day free trial. Less than $1.70 a month.</p><ul>{lis}</ul><a class="btn" href="{get}">{btn}</a></div>'
             f'<div class="plan" data-reveal style="--i:2"><h3>Lifetime</h3><div class="price">{PRICES["lifetime"]}<small> once</small></div><p class="note">Pay once, keep Pro on all your devices.</p><ul>{lis}</ul><a class="btn ghost" href="{get}">{"Buy lifetime" if SITE["app_store_url"] else btn}</a></div>')
    more = '<p class="center small" style="margin-top:24px">Prices in USD. Local prices are shown in the App Store. <a href="/pricing/">Compare Free and Pro</a></p>' if compact else ""
    return (f'<section class="section tight" id="pricing"><div class="wrap">{section_head("Pricing", "Free to start. <span class=\"hl\">Pro when you need it.</span>", "Every note shows its first 2 minutes free. Pro unlocks everything, including notes you recorded before upgrading.")}'
            f'<div class="plans">{plans}</div>{more}</div></section>')


def feature_body(f):
    blocks = "".join(f'<div class="card" data-reveal style="--i:{i % 3}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(f["blocks"]))
    steps = "".join(f'<div class="step" data-reveal style="--i:{i}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(f["steps"]))
    img, alt, kind = f["shot"]
    top = (f'<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><span class="eyebrow">{esc(f["name"])}</span>'
           f'<h1 style="font-size:clamp(38px,5.2vw,64px)">{f["h1"]}</h1><p class="lead">{esc(f["lead"])}</p>'
           f'<div class="btn-row">{store_button()}<a class="btn ghost" href="/features/">All features</a></div></div>'
           f'<div class="hero-viz" style="animation:rise .9s var(--ease) .2s both">{viz(f["viz"])}</div></div></section>'
           f'<section class="section tight"><div class="wrap">{answer_box(f["q"], f["a"])}</div></section>')
    shot = (f'<section class="section tight"><div class="wrap split"><div data-reveal>{shot_img(img, alt, kind)}</div><div data-reveal style="--i:1">'
            f'<span class="eyebrow">In the app</span><h2>How it works</h2>'
            f'<div class="steps" style="grid-template-columns:1fr;margin-top:24px">{steps}</div></div></div></section>')
    details = f'<section class="section alt"><div class="wrap">{section_head("Details", "What you get")}<div class="grid g3">{blocks}</div></div></section>'
    return top + shot + details + faq_block(f["faqs"]) + related(f["related"]) + cta_band()


def features_hub_body():
    cards = "".join(feature_card(f, i) for i, f in enumerate(FEATURES))
    return (hero_sub("Features", "Everything Murmur does, <span class=\"hl\">on your device</span>",
                     "Recording, Whisper transcription, summaries, search, editing, export and sync. Pick a feature to see how it works.",
                     "What can Murmur do?",
                     "Murmur records and imports audio, transcribes it with Whisper on your device, labels speakers, summarizes with Apple Intelligence, searches every note, fixes words with a custom dictionary and find and replace, exports text, Markdown, SRT and audio, and syncs through your private iCloud if you want it.")
            + f'<section class="section tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>'
            + f'<section class="section alt"><div class="wrap split"><div data-reveal>{viz("transcribe")}</div><div data-reveal style="--i:1">'
              f'<span class="eyebrow">The engine</span><h2>Whisper Large v3 Turbo, <span class="hl">on the Neural Engine</span></h2>'
              f'<p class="lead">Murmur runs OpenAI\'s open-source Whisper through WhisperKit, which converts it for Apple\'s Neural Engine and GPU. That is how a large, accurate model fits on a phone.</p>'
              f'<a class="btn ghost" href="/guides/what-is-whisper/">What is Whisper?</a></div></div></section>'
            + cta_band())


def platform_body(p):
    figs = "".join(f'<figure class="{ {"phone": "", "tablet": "", "wide": "wide", "watch": "watch"}[p["kind"]] }">{shot_img(n, f"Murmur on {p["name"]}: {c}", p["kind"])}<figcaption>{esc(c)}</figcaption></figure>'
                   for n, c in p["shots"])
    pts = "".join(f'<div class="card" data-reveal style="--i:{i % 3}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(p["points"]))
    others = "".join(f'<a class="card" href="/{o["slug"]}/" data-reveal style="--i:{i}">{icon(o["icon"])}<h3>Murmur for {o["name"]}</h3><p>{esc(o["lead"])}</p><span class="more">Learn more</span></a>'
                     for i, o in enumerate(x for x in PLATFORMS if x is not p))
    extra = f'<section class="section tight"><div class="wrap split"><div data-reveal>{viz("watch")}</div><div data-reveal style="--i:1"><span class="eyebrow">Watch to iPhone</span><h2>Record on your wrist, <span class="hl">read on your phone</span></h2><p class="lead">The watch records in a compact format and sends the file to your iPhone with its own ID, so a retry never makes a duplicate note.</p></div></div></section>' if p["slug"] == "apple-watch" else ""
    return (hero_sub(f"Murmur for {p['name']}", p["h1"], p["lead"], p["q"], p["a"])
            + f'<section class="section tight"><div class="wrap"><div class="shots-row" tabindex="0" aria-label="{p["name"]} screenshots">{figs}</div></div></section>'
            + extra
            + f'<section class="section alt"><div class="wrap">{section_head("On " + p["name"], "Built for " + p["name"])}<div class="grid g3">{pts}</div></div></section>'
            + faq_block(p["faqs"])
            + f'<section class="section tight"><div class="wrap">{section_head("Also on", "Murmur on your other devices")}<div class="grid g3">{others}</div></div></section>'
            + cta_band())


def platforms_hub_body():
    cards = "".join(f'<a class="card big" href="/{p["slug"]}/" data-reveal style="--i:{i}">{icon(p["icon"], ["", "c2", "c4", "c1"][i])}<h3>Murmur for {p["name"]}</h3><p>{esc(p["lead"])}</p><span class="more">Learn more</span></a>'
                    for i, p in enumerate(PLATFORMS))
    return (hero_sub("Platforms", "iPhone, iPad, Mac <span class=\"hl\">and Apple Watch</span>",
                     "One universal app. Buy Pro once with your Apple ID and use it on every device.",
                     "Which devices does Murmur work on?",
                     "Murmur works on iPhone, iPad, Macs with Apple silicon running macOS 15 or later, and Apple Watch. iPhone, iPad and Mac transcribe on the device; Apple Watch records and sends audio to your iPhone. Optional iCloud sync keeps transcripts in step across devices.")
            + f'<section class="section tight"><div class="wrap"><div class="grid g2">{cards}</div></div></section>'
            + f'<section class="section alt"><div class="wrap split"><div data-reveal>{viz("sync")}</div><div data-reveal style="--i:1"><span class="eyebrow">iCloud sync</span><h2>Start on one device, <span class="hl">finish on another</span></h2><p class="lead">Turn on iCloud sync and your notes, transcripts, folders and dictionary follow you between iPhone, iPad and Mac through your own private iCloud.</p><a class="btn ghost" href="/features/icloud-sync/">About iCloud sync</a></div></div></section>'
            + cta_band())


def use_case_body(u):
    pains = "".join(f"<li><span>{esc(x)}</span></li>" for x in u["pains"])
    steps = "".join(f'<div class="step" data-reveal style="--i:{i}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(u["steps"]))
    four = " four" if len(u["steps"]) == 4 else ""
    vmap = {"meeting-transcription": "summary", "lecture-transcription": "search", "interview-transcription": "offline", "voice-memo-transcription": "record", "video-subtitles": "export"}
    return (hero_sub(f"For {u['name'].lower()}", u["h1"], u["lead"], u["q"], u["a"])
            + f'<section class="section tight"><div class="wrap split"><div data-reveal><span class="eyebrow rec">The problem</span><h2>What gets in the way</h2><ul class="checks">{pains}</ul></div><div data-reveal style="--i:1">{viz(vmap[u["slug"]])}</div></div></section>'
            + f'<section class="section alt"><div class="wrap">{section_head("Workflow", "How to do it with Murmur")}<div class="reveal-group"><div class="progress-line"><i></i></div><div class="steps{four}">{steps}</div></div></div></section>'
            + faq_block(u["faqs"])
            + related(u["features"][:3], "Features that help")
            + cta_band())


def use_cases_hub_body():
    cards = "".join(f'<a class="card" href="/use-cases/{u["slug"]}/" data-reveal style="--i:{i % 3}">{icon(u["icon"], ["", "c1", "c2", "c3", "c4"][i])}<h3>{u["name"]}</h3><p>{esc(u["desc"])}</p><span class="more">Learn more</span></a>'
                    for i, u in enumerate(USE_CASES))
    return (hero_sub("Use cases", "Private transcription <span class=\"hl\">for real work</span>",
                     "How people use Murmur for meetings, lectures, interviews, voice notes and subtitles.", buttons=False)
            + f'<section class="section tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>' + cta_band())


def guide_body(g):
    heads = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"])
    toc = '<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads) + '<li><a href="#faq-h">FAQ</a></li></ol></nav>'
    rel = "".join(f'<li><a href="/features/{s}/">{FEAT[s]["name"]}</a></li>' for s in g["related"])
    return (hero_sub("Guide", g["h1"], g["lead"], g["q"], g["a"], buttons=False)
            + f'<section class="section tight"><div class="wrap"><article class="prose">'
              f'<p class="meta">Last updated {SITE["updated_human"]} · By the Murmur team</p>{toc}{g["body"]}'
              f'<h2>Related</h2><ul>{rel}</ul></article></div></section>'
            + faq_block(g["faqs"]) + cta_band())


def guides_hub_body():
    cards = "".join(f'<a class="card" href="/guides/{g["slug"]}/" data-reveal style="--i:{i % 3}">{icon("file", ["", "c1", "c2", "c3", "c4"][i])}<h3>{esc(g["nav"])}</h3><p>{esc(g["desc"])}</p><span class="more">Read guide</span></a>'
                    for i, g in enumerate(GUIDES))
    return (hero_sub("Guides", "Transcription guides <span class=\"hl\">and explainers</span>",
                     "Practical how-tos for transcribing on iPhone and Mac, plus plain-English explainers on Whisper and on-device speech recognition.", buttons=False)
            + f'<section class="section tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>' + cta_band())


PRICING_FAQ = [
    ("What is free in Murmur?", "Everything works on the free version, and every note shows its first 2 minutes. Recording and transcription are not capped; the full transcript is saved, so upgrading later unlocks your older notes."),
    ("How does the free trial work?", f"The yearly plan starts with a {PRICES['trial_days']}-day free trial. You are not charged if you cancel at least 24 hours before the trial ends."),
    ("Does one purchase work on iPhone, iPad and Mac?", "Yes. Murmur is a universal purchase tied to your Apple ID."),
    ("How do I restore my purchase on a new device?", "Open Settings in Murmur and tap Restore purchases. Murmur also checks your purchases when it starts."),
    ("Can I get a refund?", "Purchases are handled by Apple. Request a refund at reportaproblem.apple.com."),
    ("Is Family Sharing supported?", "Subscriptions and the lifetime plan follow Apple's Family Sharing settings for each product, as configured on the App Store."),
]


def pricing_body():
    rows = [("Record and import", "yes", "yes"), ("On-device Whisper transcription", "yes", "yes"), ("Read transcripts", "First 2 minutes of each note", "Full transcript"),
            ("Search all notes", "yes", "yes"), ("Edit transcript and speakers", "Notes up to 2 minutes", "All notes"), ("Find and replace", "Notes up to 2 minutes", "All notes"),
            ("Export TXT, Markdown, SRT, audio", "Notes up to 2 minutes", "All notes"), ("On-device summaries", "Notes up to 2 minutes", "All notes"),
            ("iCloud sync", "yes", "yes"), ("Apple Watch app", "yes", "yes")]
    cell = lambda v, us=False: f'<td class="{"us " if us else ""}{"yes" if v == "yes" else ""}">{"Included" if v == "yes" else v}</td>'
    table = "".join(f"<tr><td>{n}</td>{cell(a)}{cell(b, True)}</tr>" for n, a, b in rows)
    return (hero_sub("Pricing", "Simple pricing. <span class=\"hl\">No account.</span>",
                     "Download Murmur free and try it on your own recordings. Upgrade to Pro for full transcripts and every tool.",
                     "How much does Murmur cost?",
                     f"Murmur is free to download and shows the first 2 minutes of every note. Murmur Pro costs {PRICES['monthly']} a month, {PRICES['yearly']} a year with a {PRICES['trial_days']}-day free trial, or {PRICES['lifetime']} once for lifetime access. Prices are in US dollars; the App Store shows your local price.",
                     buttons=False)
            + pricing_cards()
            + f'<section class="section tight"><div class="wrap">{section_head("Compare", "Free vs Pro")}<div class="table-wrap" data-reveal><table><thead><tr><th>Feature</th><th>Free</th><th class="us">Pro</th></tr></thead><tbody>{table}</tbody></table></div>'
              '<p class="small center" style="margin-top:20px;max-width:760px;margin-left:auto;margin-right:auto">Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period. Manage or cancel them in your Apple ID settings under Subscriptions. '
              'See our <a href="/terms/">Terms of Use</a> and <a href="/privacy/">Privacy Policy</a>. Machine-readable pricing: <a href="/pricing.md">pricing.md</a>.</p></div></section>'
            + faq_block(PRICING_FAQ, "Pricing questions") + cta_band())


def faq_body():
    return (hero_sub("FAQ", "Questions, <span class=\"hl\">answered</span>",
                     "Everything people ask about Murmur: privacy, offline use, accuracy, devices and pricing.", buttons=False)
            + faq_block(FAQ, "Murmur FAQ", "All questions")
            + '<section class="section tight"><div class="wrap center"><p class="lead">Still stuck? <a href="/support/">Visit support</a>.</p></div></section>'
            + cta_band())


def support_body():
    cards = (f'<a class="card" href="{SITE["support_url"]}" rel="noopener" data-reveal>{icon("message")}<h3>Report a problem or idea</h3><p>Open an issue on GitHub. Please do not include private recordings or transcripts.</p><span class="more">Open GitHub issues</span></a>'
             f'<a class="card" href="/faq/" data-reveal style="--i:1">{icon("book", "c2")}<h3>Read the FAQ</h3><p>Answers about privacy, offline use, devices and pricing.</p><span class="more">Go to FAQ</span></a>'
             f'<a class="card" href="/pricing/" data-reveal style="--i:2">{icon("sync", "c4")}<h3>Purchases</h3><p>Restore purchases from Settings in Murmur. Refunds go through Apple at reportaproblem.apple.com.</p><span class="more">See pricing</span></a>')
    tips = [("The transcript is empty or stuck", "Check that the speech model finished downloading in Settings. Transcription runs one note at a time; queued notes wait their turn."),
            ("Names are misspelled", "Add them to the custom dictionary, then fix existing notes with Find and replace."),
            ("The Summary tab is missing", "Summaries need a device with Apple Intelligence turned on. Murmur hides the tab on other devices."),
            ("Notes do not appear on my other devices", "iCloud sync is off by default. Turn it on in Settings on each device, make sure each is signed in to the same Apple ID, and reopen Murmur."),
            ("Apple Watch recordings are not arriving", "Open Murmur on your iPhone and keep the watch near it. Recordings wait on the watch and send when the two are connected.")]
    tip_html = "".join(f'<div class="card" data-reveal style="--i:{i % 3}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(tips))
    return (hero_sub("Support", "How can we <span class=\"hl\">help?</span>", "Murmur has no account and no server, so we cannot see your notes. Here is how to fix common issues and reach us.", buttons=False)
            + f'<section class="section tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>'
            + f'<section class="section alt"><div class="wrap">{section_head("Troubleshooting", "Common fixes")}<div class="grid g3">{tip_html}</div></div></section>')


def legal_body(name):
    body = (TOOLS / "legal" / f"{name}.html").read_text(encoding="utf-8")
    body = body.replace('<div class="card">', '<div class="card answer-box" style="margin:24px 0">')
    return f'<section class="section tight"><div class="wrap"><article class="prose">{body}</article></div></section>'


def not_found_body():
    return (hero_sub("404", "This page <span class=\"hl\">went quiet</span>", "We could not find that page. Try one of these instead.", buttons=False)
            + f'<section class="section tight"><div class="wrap center"><div class="btn-row" style="justify-content:center"><a class="btn" href="/">Home</a><a class="btn ghost" href="/features/">Features</a><a class="btn ghost" href="/faq/">FAQ</a></div>{wave(80)}</div></section>')


# ------------------------------------------------------------------ page list
def pages():
    P = []
    P.append(dict(path="", og="home", title="Murmur: Private Speech to Text, Fully Offline",
                  desc="Transcribe meetings, lectures and voice notes on iPhone, iPad, Mac and Apple Watch with Whisper on your device. No account, no uploads, works offline.",
                  body=home_body(), faqs=FAQ[:8], app=True, og_title="Speech to text that never leaves your device"))
    P.append(dict(path="features/", og="features", title="Features: on-device transcription, summaries, search and export",
                  desc="Everything Murmur does: on-device Whisper transcription, recording with bookmarks, summaries, speaker labels, search, dictionary, export and iCloud sync.",
                  body=features_hub_body(), crumbs=[("Features", "/features/")], nav="/features/", og_title="Everything Murmur does, on your device"))
    for f in FEATURES:
        P.append(dict(path=f"features/{f['slug']}/", og=f"feature-{f['slug']}", title=f["title"], desc=f["desc"], body=feature_body(f),
                      crumbs=[("Features", "/features/"), (f["name"], f"/features/{f['slug']}/")], faqs=f["faqs"], nav="/features/", og_title=plain(f["h1"])))
    P.append(dict(path="platforms/", og="platforms", title="Murmur for iPhone, iPad, Mac and Apple Watch",
                  desc="Murmur is one universal app for iPhone, iPad, Mac and Apple Watch with on-device Whisper transcription and optional iCloud sync.",
                  body=platforms_hub_body(), crumbs=[("Platforms", "/platforms/")], nav="/platforms/", app=True, og_title="iPhone, iPad, Mac and Apple Watch"))
    for p in PLATFORMS:
        P.append(dict(path=f"{p['slug']}/", og=f"platform-{p['slug']}", title=p["title"], desc=p["desc"], body=platform_body(p),
                      crumbs=[("Platforms", "/platforms/"), (p["name"], f"/{p['slug']}/")], faqs=p["faqs"], nav="/platforms/", app=True, og_title=plain(p["h1"])))
    P.append(dict(path="use-cases/", og="use-cases", title="Use cases: meetings, lectures, interviews, voice notes, subtitles",
                  desc="How people use Murmur's private, on-device transcription for meetings, lectures, interviews, voice memos and video subtitles.",
                  body=use_cases_hub_body(), crumbs=[("Use cases", "/use-cases/")], nav="/use-cases/", og_title="Private transcription for real work"))
    for u in USE_CASES:
        P.append(dict(path=f"use-cases/{u['slug']}/", og=f"use-{u['slug']}", title=u["title"], desc=u["desc"], body=use_case_body(u),
                      crumbs=[("Use cases", "/use-cases/"), (u["name"], f"/use-cases/{u['slug']}/")], faqs=u["faqs"], nav="/use-cases/", og_title=plain(u["h1"])))
    P.append(dict(path="guides/", og="guides", title="Transcription guides for iPhone and Mac",
                  desc="Step-by-step guides to transcribing Voice Memos, audio on Mac and video subtitles, plus explainers on Whisper and on-device speech recognition.",
                  body=guides_hub_body(), crumbs=[("Guides", "/guides/")], nav="/guides/", og_title="Transcription guides and explainers"))
    for g in GUIDES:
        P.append(dict(path=f"guides/{g['slug']}/", og=f"guide-{g['slug']}", title=g["title"], desc=g["desc"], body=guide_body(g),
                      crumbs=[("Guides", "/guides/"), (g["nav"], f"/guides/{g['slug']}/")], faqs=g["faqs"], nav="/guides/", article=True, og_title=g["h1"]))
    P.append(dict(path="pricing/", og="pricing", title="Pricing: free to try, Pro from $3.99 a month",
                  desc=f"Murmur is free to download. Pro is {PRICES['monthly']}/month, {PRICES['yearly']}/year with a {PRICES['trial_days']}-day free trial, or {PRICES['lifetime']} lifetime. One purchase for iPhone, iPad and Mac.",
                  body=pricing_body(), crumbs=[("Pricing", "/pricing/")], faqs=PRICING_FAQ, nav="/pricing/", app=True, og_title="Free to start. Pro when you need it."))
    P.append(dict(path="faq/", og="faq", title="Murmur FAQ: privacy, offline use, accuracy and pricing",
                  desc="Answers about Murmur: does it upload audio, does it work offline, which languages and devices it supports, accuracy, speaker labels and pricing.",
                  body=faq_body(), crumbs=[("FAQ", "/faq/")], faqs=FAQ, nav="/faq/", og_title="Questions, answered"))
    P.append(dict(path="support/", og="support", title="Support and troubleshooting",
                  desc="Get help with Murmur: fix common transcription, sync and Apple Watch issues, restore purchases, and report a problem.",
                  body=support_body(), crumbs=[("Support", "/support/")], og_title="How can we help?"))
    P.append(dict(path="privacy/", og="privacy", title="Privacy Policy",
                  desc="Murmur's privacy policy: no data collected, recordings and transcripts stay on your device, optional iCloud sync to your private iCloud.",
                  body=legal_body("privacy"), crumbs=[("Privacy Policy", "/privacy/")], og_title="Privacy Policy"))
    P.append(dict(path="terms/", og="terms", title="Terms of Use",
                  desc="Terms of Use for the Murmur app, including Murmur Pro subscriptions and the lifetime purchase.",
                  body=legal_body("terms"), crumbs=[("Terms of Use", "/terms/")], og_title="Terms of Use"))
    P.append(dict(path="404.html", og="home", title="Page not found", desc="This page could not be found.", body=not_found_body(), noindex=True, og_title="Page not found"))
    return P


# ------------------------------------------------------------------ machine-readable files
def llms_txt(P):
    lines = ["# Murmur", "",
             "> Murmur is a speech-to-text app for iPhone, iPad, Mac and Apple Watch that transcribes audio with OpenAI's Whisper model running on the user's own device. No account, no uploads, no analytics; works offline after a one-time model download.",
             "",
             "Key facts:",
             "- Engine: Whisper Large v3 Turbo (compressed, about 632 MB, recommended) or Small (about 500 MB), run on device through WhisperKit.",
             f"- Languages: {', '.join(LANGUAGES)}, plus auto-detect. App interface in English.",
             "- Devices: iPhone, iPad, Mac with Apple silicon (macOS 15+), Apple Watch (records and sends audio to iPhone).",
             "- Summaries: Meeting, Lecture and Bullet point templates with action items, made on device with Apple Intelligence on supported devices.",
             "- Export: plain text (speakers, timestamps, summary), Markdown, SRT subtitles, M4A audio.",
             "- Privacy: App Store privacy label 'Data Not Collected'. Optional iCloud sync uses the user's private CloudKit database; audio is not synced.",
             f"- Pricing (USD): free download showing the first 2 minutes of each note; Pro {PRICES['monthly']}/month, {PRICES['yearly']}/year with {PRICES['trial_days']}-day free trial, {PRICES['lifetime']} lifetime. Universal purchase.",
             "- Speaker labels are added manually; Murmur does not detect speakers automatically. Murmur does not join online calls and does not translate.",
             ""]
    groups = [("Main pages", lambda p: p["path"] in ("", "pricing/", "faq/", "features/", "platforms/", "support/")),
              ("Features", lambda p: p["path"].startswith("features/") and p["path"] != "features/"),
              ("Platforms", lambda p: p.get("nav") == "/platforms/" and p["path"] != "platforms/"),
              ("Use cases", lambda p: p["path"].startswith("use-cases/") and p["path"] != "use-cases/"),
              ("Guides", lambda p: p["path"].startswith("guides/") and p["path"] != "guides/"),
              ("Legal", lambda p: p["path"] in ("privacy/", "terms/"))]
    for title, pred in groups:
        lines.append(f"## {title}")
        lines.append("")
        for p in P:
            if pred(p):
                lines.append(f"- [{p['title']}]({D}/{p['path']}): {p['desc']}")
        lines.append("")
    lines += ["## Optional", "", f"- [Pricing (Markdown)]({D}/pricing.md): Plans, prices and limits in plain text.", ""]
    return "\n".join(lines)


def pricing_md():
    return f"""# Murmur pricing

Last updated: {SITE['updated']}. Prices in US dollars; the App Store shows local prices, which vary by country.
One purchase covers iPhone, iPad and Mac with the same Apple ID (universal purchase). No account is needed.

## Free — $0
- Record, import and transcribe on device with no cap on number or length of notes.
- Each note shows the first 2 minutes of its transcript. The full transcript is saved and unlocks if you upgrade.
- Search reads the full text of every note.
- Edit, find and replace, export and summaries for notes up to 2 minutes long.
- iCloud sync and the Apple Watch app included.

## Murmur Pro Monthly — {PRICES['monthly']} per month
- Full transcripts for every note, including older notes.
- Edit, find and replace, export (TXT, Markdown, SRT, M4A) and on-device summaries for all notes.
- Auto-renews monthly.

## Murmur Pro Yearly — {PRICES['yearly']} per year
- Everything in Pro.
- {PRICES['trial_days']}-day free trial.
- Auto-renews yearly.

## Murmur Pro Lifetime — {PRICES['lifetime']} one time
- Everything in Pro, paid once.

Subscriptions renew automatically unless cancelled at least 24 hours before the end of the period. Manage them in Apple ID settings under Subscriptions.
More: {D}/pricing/
"""


def write(path, text):
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8", newline="\n")


def main():
    P = pages()
    for p in P:
        target = p["path"] + ("index.html" if p["path"].endswith("/") or p["path"] == "" else "")
        write(target, layout(p, p["body"]))
    urls = [p for p in P if not p.get("noindex")]

    def prio(p):
        return "1.0" if p["path"] == "" else "0.9" if p["path"] in ("features/", "pricing/") else "0.5" if p["path"] in ("privacy/", "terms/") else "0.8"
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append(f"<url><loc>{D}/{p['path']}</loc><lastmod>{SITE['updated']}</lastmod><priority>{prio(p)}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"# Search engines and AI assistants are welcome.\nUser-agent: *\nAllow: /\n\nSitemap: {D}/sitemap.xml\n")
    write("llms.txt", llms_txt(P))
    write("pricing.md", pricing_md())
    write("CNAME", D.split("//")[1] + "\n")
    write(".nojekyll", "")
    write("site.webmanifest", json.dumps({"name": "Murmur", "short_name": "Murmur", "start_url": "/", "display": "standalone",
                                          "background_color": "#111116", "theme_color": "#111116",
                                          "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                    {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    if "--og" in sys.argv:
        from og import draw_all
        draw_all([(p["og"], p.get("og_title", p["title"]), p["crumbs"][0][0] if p.get("crumbs") else "Private transcription") for p in P], OUT / "assets" / "og")
    print(f"built {len(P)} pages, {len(urls)} in sitemap")


if __name__ == "__main__":
    main()
