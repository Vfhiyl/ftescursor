"""OpenAlex works collector (publication_date only; free tier)."""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Optional
from urllib.parse import quote

from .config import HCC_ANCHOR_RE, OPENALEX_FULLTEXT_OR
from .http_util import fetch_json

OPENALEX_BASE = "https://api.openalex.org/works"
_THEME = re.compile(HCC_ANCHOR_RE, re.I)


def _ymd(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")


def _normalize_doi(doi: object) -> Optional[str]:
    if not doi:
        return None
    s = str(doi).strip()
    s = s.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return s.lower() or None


def _lite_work(w: dict[str, object]) -> dict[str, object]:
    return {
        "id": w.get("id"),
        "doi": _normalize_doi(w.get("doi")),
        "title": w.get("title") or w.get("display_name"),
        "publication_date": w.get("publication_date"),
        "type": w.get("type"),
        "cited_by_count": w.get("cited_by_count"),
    }


def _call_works(
    *,
    filt: str,
    mailto: str,
    api_key: Optional[str],
    per_page: int = 50,
) -> tuple[list[dict[str, object]], dict[str, object], str]:
    # Encode spaces; keep commas/pipes/colons as OpenAlex filter syntax.
    filt_q = quote(filt, safe=":,|")
    q = f"filter={filt_q}&per_page={per_page}&mailto={quote(mailto)}"
    if api_key:
        q += f"&api_key={quote(api_key)}"
    url = f"{OPENALEX_BASE}?{q}"
    payload = fetch_json(url, mailto=mailto, timeout=90)
    results: list[dict[str, object]] = []
    meta: dict[str, object] = {}
    if isinstance(payload, dict):
        raw_results = payload.get("results") or []
        if isinstance(raw_results, list):
            for item in raw_results:
                if isinstance(item, dict):
                    results.append(item)
        m = payload.get("meta")
        if isinstance(m, dict):
            meta = dict(m)
            meta.setdefault("x_query", {"url": f"/works?filter={filt}&per_page={per_page}"})
    return results, meta, url


def collect_openalex(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    api_key: Optional[str] = None,
    preprint_days: int = 7,
    fulltext_or: str = OPENALEX_FULLTEXT_OR,
) -> dict[str, object]:
    d0 = _ymd(window_start)
    d1 = _ymd(window_end)
    pre_start = _ymd(window_end - timedelta(days=preprint_days))

    # Free tier: publication_date only. Do NOT use from_created_date / from_updated_date.
    works_filter = (
        f"from_publication_date:{d0},to_publication_date:{d1},"
        f"fulltext.search:{fulltext_or}"
    )
    preprint_filter = (
        f"from_publication_date:{pre_start},to_publication_date:{d1},"
        f"type:preprint,fulltext.search:{fulltext_or}"
    )
    optional_filter = (
        f"from_publication_date:{d0},to_publication_date:{d1},"
        f"fulltext.search:TACE immunotherapy|EMERALD hepatocellular"
    )

    works_raw, meta_works, _ = _call_works(
        filt=works_filter, mailto=mailto, api_key=api_key
    )
    pre_raw, meta_pre, _ = _call_works(
        filt=preprint_filter, mailto=mailto, api_key=api_key
    )
    opt_raw, _, _ = _call_works(
        filt=optional_filter, mailto=mailto, api_key=api_key
    )

    works = [_lite_work(w) for w in works_raw]
    # fulltext.search is broad; keep title-theme preprints for the digest.
    preprints = []
    for w in pre_raw:
        lite = _lite_work(w)
        title = str(lite.get("title") or "")
        if _THEME.search(title):
            preprints.append(lite)
    optional = [_lite_work(w) for w in opt_raw]

    return {
        "filter_mode": "publication_date_only",
        "window": [d0, d1],
        "preprint_window": [pre_start, d1],
        "works_count": len(works),
        "works": works,
        "preprints_theme": preprints,
        "preprint_count": len(preprints),
        "optional_tace_immuno": optional,
        "meta_works": meta_works,
        "meta_preprints": meta_pre,
        "calls_used": 3,
        "api_key_present": bool(api_key),
    }
