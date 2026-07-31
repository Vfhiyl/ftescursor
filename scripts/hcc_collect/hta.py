"""HTA / reimbursement sentinels: NICE product lists + EMA CHMP highlights."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Optional
from urllib.parse import urljoin

from .config import (
    EMA_CHMP_HIGHLIGHTS_RE,
    EMA_NEWS_URL,
    HTA_NICE_LISTS,
    JOURNAL_THEME_RE,
    REGULATORY_DRUG_TERMS,
)
from .http_util import fetch_text

_GUIDANCE_HREF = re.compile(
    r"/guidance/(ta|htg|ng|ipg|mtg|dg|indevelopment/gid-|prioritisation/gid-)",
    re.I,
)
_THEME = re.compile(JOURNAL_THEME_RE, re.I)
_DRUG = re.compile("|".join(re.escape(x) for x in REGULATORY_DRUG_TERMS), re.I)
_CHMP_TITLE = re.compile(EMA_CHMP_HIGHLIGHTS_RE, re.I)


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.title = ""
        self._in_a = False
        self._href: Optional[str] = None
        self._parts: list[str] = []
        self._in_title = False
        self._title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if tag == "title":
            self._in_title = True
            self._title_parts = []
        if tag != "a":
            return
        href = None
        for k, v in attrs:
            if k.lower() == "href":
                href = v
                break
        self._in_a = True
        self._href = href
        self._parts = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)
        if self._in_a:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self.title = re.sub(r"\s+", " ", "".join(self._title_parts)).strip()
            self._in_title = False
        if tag != "a" or not self._in_a:
            return
        text = re.sub(r"\s+", " ", "".join(self._parts)).strip()
        href = (self._href or "").strip()
        if href and text:
            self.links.append((text, href))
        self._in_a = False
        self._href = None
        self._parts = []


def _parse_html(html: str) -> _LinkParser:
    parser = _LinkParser()
    parser.feed(html)
    return parser


def _guidance_id(url: str) -> str:
    m = re.search(
        r"/guidance/(ta\d+|htg\d+|ng\d+|ipg\d+|mtg\d+|dg\d+|indevelopment/[^?#]+|prioritisation/[^?#]+)",
        url,
        re.I,
    )
    return m.group(1).lower() if m else url


def collect_nice_lists(*, mailto: str) -> dict[str, object]:
    lists_out: list[dict[str, object]] = []
    all_ids: list[str] = []
    seen_ids: set[str] = set()

    for src in HTA_NICE_LISTS:
        entry: dict[str, object] = {
            "name": src["name"],
            "status": src["status"],
            "url": src["url"],
            "page_status": None,
            "error": None,
            "items": [],
        }
        try:
            html = fetch_text(src["url"], mailto=mailto, timeout=45, retries=2)
            entry["page_status"] = 200
            parsed = _parse_html(html)
            items: list[dict[str, str]] = []
            seen_href: set[str] = set()
            for text, href in parsed.links:
                abs_url = urljoin(src["url"], href).split("#", 1)[0]
                if not _GUIDANCE_HREF.search(abs_url):
                    continue
                if abs_url in seen_href:
                    continue
                # Skip chapter anchors / recommendation fragments.
                if "/chapter/" in abs_url.lower():
                    continue
                if len(text) < 12:
                    continue
                seen_href.add(abs_url)
                gid = _guidance_id(abs_url)
                item = {
                    "id": gid,
                    "title": text[:300],
                    "url": abs_url,
                }
                items.append(item)
                if gid not in seen_ids:
                    seen_ids.add(gid)
                    all_ids.append(gid)
            entry["items"] = items
            entry["item_count"] = len(items)
        except Exception as exc:  # noqa: BLE001
            entry["error"] = str(exc)[:240]
            entry["item_count"] = 0
        lists_out.append(entry)

    return {
        "lists": lists_out,
        "unique_guidance_ids": all_ids,
        "unique_guidance_count": len(all_ids),
    }


def _find_latest_chmp_highlights(news_html: str, base: str) -> Optional[dict[str, str]]:
    parsed = _parse_html(news_html)
    candidates: list[tuple[str, str]] = []
    for text, href in parsed.links:
        if not _CHMP_TITLE.search(text):
            continue
        abs_url = urljoin(base, href).split("#", 1)[0]
        candidates.append((text[:300], abs_url))
    if not candidates:
        return None
    # News page lists newest first; take first CHMP highlights link.
    title, url = candidates[0]
    return {"title": title, "url": url}


def collect_ema_chmp(*, mailto: str) -> dict[str, object]:
    out: dict[str, object] = {
        "news_url": EMA_NEWS_URL,
        "news_status": None,
        "error": None,
        "latest_highlights": None,
        "items": [],
        "hcc_related_items": [],
    }
    try:
        news_html = fetch_text(EMA_NEWS_URL, mailto=mailto, timeout=45, retries=2)
        out["news_status"] = 200
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"news_fetch: {exc}"[:240]
        return out

    latest = _find_latest_chmp_highlights(news_html, EMA_NEWS_URL)
    if not latest:
        out["error"] = "no_chmp_highlights_link_on_news"
        return out
    out["latest_highlights"] = latest

    try:
        page_html = fetch_text(latest["url"], mailto=mailto, timeout=60, retries=2)
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"highlights_fetch: {exc}"[:240]
        return out

    parsed = _parse_html(page_html)
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for text, href in parsed.links:
        abs_url = urljoin(latest["url"], href).split("#", 1)[0]
        if "/medicines/human/" not in abs_url:
            continue
        if abs_url in seen:
            continue
        if len(text) < 3:
            continue
        seen.add(abs_url)
        items.append({"title": text[:240], "url": abs_url})

    # Also keep plain-text HCC mentions from the article body (not only links).
    body = re.sub(r"<script[\s\S]*?</script>", " ", page_html, flags=re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"\s+", " ", body)
    mentions: list[str] = []
    for m in re.finditer(
        r".{0,60}(hepatocellular|\bHCC\b|cholangiocarcin|liver cancer|"
        r"biliary tract cancer|bile duct cancer).{0,80}",
        body,
        re.I,
    ):
        snip = m.group(0).strip()
        if snip and snip not in mentions:
            mentions.append(snip[:220])
        if len(mentions) >= 10:
            break

    hcc_items = [
        it
        for it in items
        if _THEME.search(it["title"])
        or _THEME.search(it["url"])
        or _DRUG.search(it["title"])
    ]
    # Drug-name alone on CHMP page is noisy (Imfinzi bladder etc.); keep drug hits
    # only when title/url also has oncology liver context OR appears in HCC mentions.
    mention_blob = " ".join(mentions).lower()
    refined: list[dict[str, str]] = []
    for it in hcc_items:
        title_u = f"{it['title']} {it['url']}"
        if re.search(
            r"hepatocellular|cholangiocarcin|liver cancer|\bHCC\b|biliary tract|bile duct",
            title_u,
            re.I,
        ):
            refined.append(it)
            continue
        # Keep named product if body mentions HCC near that brand (weak signal).
        brand = it["title"].split(":")[0].strip()
        if brand and brand.lower() in mention_blob and re.search(
            r"hepatocellular|cholangiocarcin|liver cancer|\bHCC\b",
            mention_blob,
            re.I,
        ):
            refined.append(it)

    out["items"] = items
    out["item_count"] = len(items)
    out["hcc_related_items"] = refined
    out["hcc_related_count"] = len(refined)
    out["body_hcc_mentions"] = mentions
    return out


def collect_hta(*, mailto: str) -> dict[str, object]:
    nice = collect_nice_lists(mailto=mailto)
    ema = collect_ema_chmp(mailto=mailto)
    return {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "nice": nice,
        "ema_chmp": ema,
        "counts": {
            "nice_unique_guidance": nice.get("unique_guidance_count"),
            "nice_published_ta": next(
                (
                    len(x.get("items") or [])
                    for x in (nice.get("lists") or [])
                    if isinstance(x, dict) and x.get("status") == "published_ta"
                ),
                0,
            ),
            "nice_in_development": next(
                (
                    len(x.get("items") or [])
                    for x in (nice.get("lists") or [])
                    if isinstance(x, dict) and x.get("status") == "in_development"
                ),
                0,
            ),
            "ema_chmp_items": ema.get("item_count"),
            "ema_chmp_hcc_related": ema.get("hcc_related_count"),
            "ema_body_hcc_mentions": len(ema.get("body_hcc_mentions") or []),
        },
        "notes": [
            "HAS Transparency avis lists are JS-heavy / often 403; deferred.",
            "NICE product lists are the primary structured HTA sentinel for HCC.",
            "EMA CHMP highlights are meeting-level title sentinels, not a full HTA DB.",
        ],
    }
