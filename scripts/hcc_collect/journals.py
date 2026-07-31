"""Journal TOC collectors: ScienceDirect RSS + PubMed journal EDAT proxy."""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Optional
from xml.etree.ElementTree import Element

from .config import JOURNAL_PUBMED_NAMES, JOURNAL_RSS_FEEDS, JOURNAL_THEME_RE
from .http_util import fetch_json, fetch_text, url_with_query

_THEME = re.compile(JOURNAL_THEME_RE, re.I)
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def _local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _child_text(node: Element, names: set[str]) -> str:
    for child in list(node):
        if _local(child.tag) in names:
            return "".join(child.itertext()).strip()
    return ""


def _parse_rss_items(xml_text: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_text)
    items: list[dict[str, str]] = []
    for node in root.iter():
        if _local(node.tag) != "item":
            continue
        title = _child_text(node, {"title"})
        link = _child_text(node, {"link"})
        pub = _child_text(node, {"pubDate", "date"})
        desc = _child_text(node, {"description", "summary"})
        # dc:identifier / guid often holds DOI
        doi = ""
        for child in list(node):
            loc = _local(child.tag).lower()
            text = "".join(child.itertext()).strip()
            if loc in {"identifier", "guid"} and "10." in text:
                m = re.search(r"(10\.\d{4,9}/[^\s<>\"]+)", text, re.I)
                if m:
                    doi = m.group(1).rstrip(".).,;")
                    break
        if not doi:
            m = re.search(r"(10\.\d{4,9}/[^\s<>\"]+)", f"{link} {desc}", re.I)
            if m:
                doi = m.group(1).rstrip(".).,;")
        items.append(
            {
                "title": title,
                "link": link,
                "published": pub,
                "doi": doi.lower() if doi else "",
                "summary_snip": re.sub(r"<[^>]+>", "", desc)[:280],
            }
        )
    return items


def collect_journal_rss(*, mailto: str) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for feed in JOURNAL_RSS_FEEDS:
        entry: dict[str, object] = {
            "name": feed["name"],
            "issn": feed.get("issn"),
            "rss": feed["rss"],
            "status": None,
            "error": None,
            "item_count": 0,
            "theme_items": [],
        }
        try:
            xml_text = fetch_text(feed["rss"], mailto=mailto, timeout=45, retries=2)
            entry["status"] = 200
            items = _parse_rss_items(xml_text)
            entry["item_count"] = len(items)
            theme = []
            for item in items:
                blob = f"{item.get('title','')} {item.get('summary_snip','')}"
                if _THEME.search(blob):
                    theme.append(item)
            entry["theme_items"] = theme[:30]
        except Exception as exc:  # noqa: BLE001
            entry["error"] = str(exc)[:240]
        out.append(entry)
        time.sleep(0.4)
    return out


def _ymd_slash(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y/%m/%d")


def collect_journal_pubmed(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
) -> dict[str, object]:
    d0 = _ymd_slash(window_start)
    d1 = _ymd_slash(window_end)
    journal_or = " OR ".join(f'"{name}"[Journal]' for name in JOURNAL_PUBMED_NAMES)
    term = f"({journal_or}) AND (\"{d0}\"[EDAT] : \"{d1}\"[EDAT])"
    url = url_with_query(
        f"{EUTILS}/esearch.fcgi",
        {
            "db": "pubmed",
            "term": term,
            "retmax": 100,
            "retmode": "json",
            "email": mailto,
            "tool": "hcc_digest",
        },
    )
    raw = fetch_json(url, mailto=mailto)
    ids: list[str] = []
    if isinstance(raw, dict):
        es = raw.get("esearchresult")
        if isinstance(es, dict) and isinstance(es.get("idlist"), list):
            ids = [str(x) for x in es["idlist"]]

    records: list[dict[str, object]] = []
    theme_records: list[dict[str, object]] = []
    if ids:
        time.sleep(0.35)
        sum_url = url_with_query(
            f"{EUTILS}/esummary.fcgi",
            {
                "db": "pubmed",
                "id": ",".join(ids[:100]),
                "retmode": "json",
                "email": mailto,
                "tool": "hcc_digest",
            },
        )
        summary = fetch_json(sum_url, mailto=mailto)
        result = {}
        if isinstance(summary, dict) and isinstance(summary.get("result"), dict):
            result = summary["result"]
        for pmid in ids:
            s = result.get(pmid)
            if not isinstance(s, dict):
                continue
            title = str(s.get("title") or "")
            source = str(s.get("source") or "")
            doi = None
            aids = s.get("articleids") or []
            if isinstance(aids, list):
                for a in aids:
                    if isinstance(a, dict) and a.get("idtype") == "doi":
                        doi = str(a.get("value") or "").lower()
                        break
            rec = {
                "pmid": pmid,
                "title": title,
                "source": source,
                "pubdate": s.get("pubdate"),
                "doi": doi,
            }
            records.append(rec)
            if _THEME.search(title) or _THEME.search(source):
                theme_records.append(rec)

    return {
        "query": term,
        "window": [d0, d1],
        "count": len(ids),
        "ids": ids,
        "records": records,
        "theme_records": theme_records,
        "theme_count": len(theme_records),
    }


def collect_journals(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
) -> dict[str, object]:
    rss = collect_journal_rss(mailto=mailto)
    pubmed = collect_journal_pubmed(window_start, window_end, mailto=mailto)

    # DOI union for summary / delta
    dois: list[str] = []
    seen: set[str] = set()
    for feed in rss:
        for item in feed.get("theme_items") or []:
            if not isinstance(item, dict):
                continue
            doi = str(item.get("doi") or "").lower()
            if doi and doi not in seen:
                seen.add(doi)
                dois.append(doi)
    for rec in pubmed.get("theme_records") or []:
        if not isinstance(rec, dict):
            continue
        doi = str(rec.get("doi") or "").lower()
        if doi and doi not in seen:
            seen.add(doi)
            dois.append(doi)

    return {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "rss_feeds": rss,
        "pubmed_journal_window": pubmed,
        "theme_doi_count": len(dois),
        "theme_dois": dois,
        "rss_theme_item_count": sum(
            len(f.get("theme_items") or []) for f in rss if isinstance(f, dict)
        ),
        "pubmed_theme_count": pubmed.get("theme_count"),
    }
