"""Lightweight HTML news / guideline sentinel scraper."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Optional, Sequence
from urllib.parse import urljoin

from .config import (
    GUIDELINE_HIT_RE,
    GUIDELINE_SOURCES,
    NEWS_SOURCES,
    NEWS_THEME_RE,
)
from .http_util import fetch_text

_THEME = re.compile(NEWS_THEME_RE, re.I)
_GUIDELINE_THEME = re.compile(GUIDELINE_HIT_RE, re.I)
_NAV_NOISE = re.compile(
    r"^(about|login|log in|register|home|contact|search|menu|cart|"
    r"jnccn|leadership|governance|foundation|membership|donate|"
    r"マイページ|日本肝臓学会とは)$",
    re.I,
)


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._in_a = False
        self._href: Optional[str] = None
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag.lower() != "a":
            return
        href = None
        for k, v in attrs:
            if k.lower() == "href":
                href = v
                break
        self._in_a = True
        self._href = href
        self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_a:
            self._text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self._in_a:
            return
        text = re.sub(r"\s+", " ", "".join(self._text_parts)).strip()
        href = (self._href or "").strip()
        if href and text:
            self.links.append((text, href))
        self._in_a = False
        self._href = None
        self._text_parts = []


def scan_source(
    source: dict[str, str],
    *,
    mailto: str,
    theme: re.Pattern[str] = _THEME,
    max_hits: int = 20,
) -> dict[str, object]:
    url = source["url"]
    out: dict[str, object] = {
        "lang": source.get("lang"),
        "name": source.get("name"),
        "url": url,
        "status": None,
        "error": None,
        "theme_hits": [],
        "link_count_scanned": 0,
    }
    try:
        html = fetch_text(url, mailto=mailto, timeout=45, retries=2)
        out["status"] = 200
    except Exception as exc:  # noqa: BLE001
        msg = str(exc)
        m = re.match(r"HTTP Error (\d+):\s*(.*)", msg)
        if m:
            out["status"] = None
            out["error"] = f"{m.group(1)}: HTTP Error {m.group(1)}: {m.group(2)}"
        else:
            out["error"] = msg[:200]
        return out

    parser = _LinkParser()
    try:
        parser.feed(html)
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"parse_error: {exc}"
        return out

    hits: list[dict[str, str]] = []
    seen: set[str] = set()
    for text, href in parser.links:
        if len(text) < 12 or _NAV_NOISE.match(text.strip()):
            continue
        if not theme.search(text) and not theme.search(href):
            continue
        abs_url = urljoin(url, href)
        key = abs_url.split("#", 1)[0]
        if key in seen:
            continue
        # Drop pure nav/footer anchors that only matched society acronyms in URL.
        if theme is _GUIDELINE_THEME and not _GUIDELINE_THEME.search(text):
            continue
        seen.add(key)
        hits.append({"text": text[:240], "href": abs_url})
        if len(hits) >= max_hits:
            break
    out["theme_hits"] = hits
    out["link_count_scanned"] = len(parser.links)
    return out


def collect_html_sentinels(
    sources: Sequence[dict[str, str]],
    *,
    mailto: str,
    theme: re.Pattern[str] = _THEME,
) -> dict[str, object]:
    scanned = [scan_source(s, mailto=mailto, theme=theme) for s in sources]
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "sources": scanned,
    }


def collect_news(*, mailto: str) -> dict[str, object]:
    return collect_html_sentinels(NEWS_SOURCES, mailto=mailto, theme=_THEME)


def collect_guidelines(*, mailto: str) -> dict[str, object]:
    return collect_html_sentinels(
        GUIDELINE_SOURCES, mailto=mailto, theme=_GUIDELINE_THEME
    )
