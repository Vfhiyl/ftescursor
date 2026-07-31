"""Media / trade-press attention sentinels (agenda signals, not clinical evidence)."""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html import unescape
from xml.etree.ElementTree import Element

from .config import (
    MEDIA_GOOGLE_NEWS_FEEDS,
    MEDIA_HTML_SOURCES,
    MEDIA_NOISE_RE,
    MEDIA_THEME_RE,
)
from .http_util import fetch_text
from .news import scan_source

_THEME = re.compile(MEDIA_THEME_RE, re.I)
_NOISE = re.compile(MEDIA_NOISE_RE, re.I)
_TAG = re.compile(r"<[^>]+>")


def _local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _child_text(node: Element, names: set[str]) -> str:
    for child in list(node):
        if _local(child.tag) in names:
            return "".join(child.itertext()).strip()
    return ""


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", unescape(_TAG.sub(" ", text or ""))).strip()


def _split_gnews_title(title: str) -> tuple[str, str]:
    """Google News titles often end with ' - SourceName'."""
    t = title.strip()
    if " - " in t:
        body, source = t.rsplit(" - ", 1)
        if 1 < len(source) < 80:
            return body.strip(), source.strip()
    if " |" in t:
        body, source = t.rsplit(" |", 1)
        if 1 < len(source.strip()) < 80:
            return body.strip(), source.strip()
    return t, ""


def _parse_rss_items(xml_text: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_text)
    items: list[dict[str, str]] = []
    for node in root.iter():
        if _local(node.tag) != "item":
            continue
        raw_title = _child_text(node, {"title"})
        link = _child_text(node, {"link"})
        pub = _child_text(node, {"pubDate", "date"})
        desc = _clean_text(_child_text(node, {"description", "summary"}))[:280]
        title, source = _split_gnews_title(raw_title)
        if not title:
            continue
        items.append(
            {
                "title": title[:240],
                "source": source[:80],
                "link": link,
                "published": pub,
                "summary_snip": desc,
            }
        )
    return items


def _is_theme(blob: str) -> bool:
    return bool(_THEME.search(blob))


def _is_noise(blob: str) -> bool:
    return bool(_NOISE.search(blob))


def collect_google_news(*, mailto: str, max_items: int = 20) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for feed in MEDIA_GOOGLE_NEWS_FEEDS:
        entry: dict[str, object] = {
            "lang": feed.get("lang"),
            "name": feed.get("name"),
            "url": feed["url"],
            "status": None,
            "error": None,
            "item_count": 0,
            "theme_items": [],
            "dropped_noise": 0,
        }
        try:
            xml_text = fetch_text(
                feed["url"],
                mailto=mailto,
                headers={"Accept": "application/rss+xml, application/xml, text/xml, */*"},
                timeout=45,
                retries=2,
            )
            entry["status"] = 200
            items = _parse_rss_items(xml_text)
            entry["item_count"] = len(items)
            kept: list[dict[str, str]] = []
            dropped = 0
            for item in items:
                blob = f"{item.get('title', '')} {item.get('summary_snip', '')}"
                if not _is_theme(blob):
                    continue
                if _is_noise(blob):
                    dropped += 1
                    continue
                kept.append(item)
                if len(kept) >= max_items:
                    break
            entry["theme_items"] = kept
            entry["dropped_noise"] = dropped
        except Exception as exc:  # noqa: BLE001
            entry["error"] = str(exc)[:240]
        out.append(entry)
        time.sleep(0.35)
    return out


def collect_media_html(*, mailto: str, max_hits: int = 25) -> list[dict[str, object]]:
    scanned: list[dict[str, object]] = []
    for source in MEDIA_HTML_SOURCES:
        row = scan_source(source, mailto=mailto, theme=_THEME, max_hits=max_hits)
        # Drop noise titles from HTML hits too.
        hits = row.get("theme_hits") or []
        if isinstance(hits, list):
            cleaned: list[dict[str, str]] = []
            dropped = 0
            for hit in hits:
                if not isinstance(hit, dict):
                    continue
                text = str(hit.get("text") or "")
                if _is_noise(text):
                    dropped += 1
                    continue
                # Prefer article-like URLs over bare section labels.
                href = str(hit.get("href") or "")
                if text.lower() in {"liver cancer", "hepatocellular carcinoma"} and "/view/" not in href:
                    continue
                cleaned.append({"text": text[:240], "href": href})
            row["theme_hits"] = cleaned
            row["dropped_noise"] = dropped
        scanned.append(row)
        time.sleep(0.35)
    return scanned


def collect_media(*, mailto: str) -> dict[str, object]:
    google = collect_google_news(mailto=mailto)
    html_sources = collect_media_html(mailto=mailto)

    g_count = sum(
        len(s.get("theme_items") or [])
        for s in google
        if isinstance(s, dict)
    )
    h_count = sum(
        len(s.get("theme_hits") or [])
        for s in html_sources
        if isinstance(s, dict)
    )
    noise = sum(int(s.get("dropped_noise") or 0) for s in google if isinstance(s, dict))
    noise += sum(int(s.get("dropped_noise") or 0) for s in html_sources if isinstance(s, dict))

    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "role": "attention_signal",
        "note": (
            "Trade / news agenda signals only — not clinical evidence. "
            "Prefer PubMed / trials / guidelines / HTA for practice-changing claims."
        ),
        "google_news": google,
        "html_sources": html_sources,
        "counts": {
            "google_news_theme_items": g_count,
            "html_theme_hits": h_count,
            "total_theme_items": g_count + h_count,
            "dropped_noise": noise,
            "google_feeds_ok": sum(
                1 for s in google if isinstance(s, dict) and s.get("status") == 200
            ),
            "html_sources_ok": sum(
                1 for s in html_sources if isinstance(s, dict) and s.get("status") == 200
            ),
        },
    }
