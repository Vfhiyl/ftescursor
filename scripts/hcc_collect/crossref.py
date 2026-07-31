"""Crossref works collector with cursor pagination + title filter."""

from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from typing import Optional

from .config import CROSSREF_QUERIES, CROSSREF_TITLE_RE
from .http_util import fetch_json, url_with_query

_TITLE_RE = re.compile(CROSSREF_TITLE_RE, re.I)
CROSSREF_BASE = "https://api.crossref.org/works"


def _ymd(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")


def _title_of(item: dict[str, object]) -> str:
    titles = item.get("title")
    if isinstance(titles, list) and titles:
        return str(titles[0])
    return ""


def _container_of(item: dict[str, object]) -> str:
    titles = item.get("container-title")
    if isinstance(titles, list) and titles:
        return str(titles[0])
    return ""


def _created_of(item: dict[str, object]) -> Optional[str]:
    created = item.get("created")
    if isinstance(created, dict):
        date_time = created.get("date-time")
        if date_time:
            return str(date_time)
    return None


def collect_crossref(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    queries: list[str] | None = None,
    rows: int = 100,
    max_pages_per_query: int = 8,
) -> dict[str, object]:
    d0 = _ymd(window_start)
    d1 = _ymd(window_end)
    qlist = queries or list(CROSSREF_QUERIES)
    all_by_doi: dict[str, dict[str, object]] = {}
    page_log: list[dict[str, object]] = []

    for query in qlist:
        cursor = "*"
        for page in range(max_pages_per_query):
            url = url_with_query(
                CROSSREF_BASE,
                {
                    "query": query,
                    "filter": f"from-created-date:{d0},until-created-date:{d1}",
                    "rows": rows,
                    "cursor": cursor,
                    "mailto": mailto,
                },
            )
            try:
                payload = fetch_json(url, mailto=mailto, timeout=90, retries=4)
            except Exception as exc:  # noqa: BLE001
                page_log.append(
                    {
                        "q": query,
                        "page": page,
                        "error": str(exc),
                    }
                )
                break
            if not isinstance(payload, dict):
                break
            message = payload.get("message")
            if not isinstance(message, dict):
                break
            items = message.get("items") or []
            if not isinstance(items, list):
                items = []
            new = 0
            for item in items:
                if not isinstance(item, dict):
                    continue
                doi = str(item.get("DOI") or "").lower()
                if not doi or doi in all_by_doi:
                    continue
                all_by_doi[doi] = item
                new += 1
            page_log.append(
                {
                    "q": query,
                    "page": page,
                    "batch": len(items),
                    "new": new,
                    "total_unique": len(all_by_doi),
                }
            )
            next_cursor = message.get("next-cursor")
            if not items or not next_cursor or new == 0:
                break
            cursor = str(next_cursor)
            time.sleep(1.1)

    filtered: list[dict[str, object]] = []
    for doi, item in all_by_doi.items():
        title = _title_of(item)
        if not _TITLE_RE.search(title):
            continue
        filtered.append(
            {
                "DOI": doi,
                "title": title,
                "created": _created_of(item),
                "type": item.get("type"),
                "container": _container_of(item),
                "publisher": item.get("publisher"),
                "URL": item.get("URL") or f"https://doi.org/{doi}",
            }
        )
    filtered.sort(key=lambda r: str(r.get("created") or ""), reverse=True)

    return {
        "window_created_date": [d0, d1],
        "queries": qlist,
        "all_dois_count": len(all_by_doi),
        "title_filtered_count": len(filtered),
        "unique_title_filtered": filtered,
        "unique_title_filtered_count": len(filtered),
        "page_log": page_log,
        "items_lite": filtered,
    }
