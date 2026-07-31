"""FDA / DailyMed / NICE-style regulatory sentinels."""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Optional
from urllib.parse import urlencode
from xml.etree.ElementTree import Element

from .config import (
    JOURNAL_THEME_RE,
    REGULATORY_DRUG_TERMS,
    REGULATORY_HTML_SOURCES,
)
from .http_util import fetch_json, fetch_text
from .news import scan_source

_THEME = re.compile(JOURNAL_THEME_RE, re.I)
_DRUG_RE = re.compile(
    "|".join(re.escape(x) for x in REGULATORY_DRUG_TERMS),
    re.I,
)
DAILYMED_RSS = "https://dailymed.nlm.nih.gov/dailymed/rss.cfm"
OPENFDA_LABEL = "https://api.fda.gov/drug/label.json"


def _ymd_compact(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y%m%d")


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def _child_text(node: Element, names: set[str]) -> str:
    for child in list(node):
        if _local(child.tag) in names:
            return "".join(child.itertext()).strip()
    return ""


def collect_dailymed_rss(*, mailto: str, max_hits: int = 40) -> dict[str, object]:
    out: dict[str, object] = {
        "rss": DAILYMED_RSS,
        "status": None,
        "error": None,
        "item_count": 0,
        "hits": [],
    }
    try:
        xml_text = fetch_text(DAILYMED_RSS, mailto=mailto, timeout=60, retries=2)
        out["status"] = 200
    except Exception as exc:  # noqa: BLE001
        out["error"] = str(exc)[:240]
        return out

    root = ET.fromstring(xml_text)
    hits: list[dict[str, str]] = []
    total = 0
    for node in root.iter():
        if _local(node.tag) != "item":
            continue
        total += 1
        title = _child_text(node, {"title"})
        link = _child_text(node, {"link"})
        desc = _child_text(node, {"description"})
        pub = _child_text(node, {"pubDate"})
        blob = f"{title} {desc}"
        if not (_DRUG_RE.search(blob) or _THEME.search(blob)):
            continue
        hits.append(
            {
                "title": title[:300],
                "link": link,
                "published": pub,
                "matched": "drug_or_hcc",
            }
        )
        if len(hits) >= max_hits:
            break
    out["item_count"] = total
    out["hits"] = hits
    out["hit_count"] = len(hits)
    return out


def _openfda_query(
    search: str,
    *,
    mailto: str,
    limit: int = 25,
) -> dict[str, object]:
    url = OPENFDA_LABEL + "?" + urlencode(
        {
            "search": search,
            "limit": str(limit),
            "sort": "effective_time:desc",
        }
    )
    try:
        payload = fetch_json(url, mailto=mailto, timeout=60, retries=2)
    except Exception as exc:  # noqa: BLE001
        return {"search": search, "error": str(exc)[:240], "results": [], "total": 0}

    results_out: list[dict[str, object]] = []
    total = 0
    if isinstance(payload, dict):
        meta = payload.get("meta")
        if isinstance(meta, dict) and isinstance(meta.get("results"), dict):
            total = int(meta["results"].get("total") or 0)
        for row in payload.get("results") or []:
            if not isinstance(row, dict):
                continue
            openfda = row.get("openfda") if isinstance(row.get("openfda"), dict) else {}
            brand = openfda.get("brand_name") or []
            generic = openfda.get("generic_name") or []
            indications = row.get("indications_and_usage") or []
            ind_text = " ".join(str(x) for x in indications) if isinstance(indications, list) else str(indications)
            results_out.append(
                {
                    "effective_time": row.get("effective_time"),
                    "brand_name": brand[:3] if isinstance(brand, list) else brand,
                    "generic_name": generic[:3] if isinstance(generic, list) else generic,
                    "set_id": (openfda.get("spl_set_id") or [None])[0]
                    if isinstance(openfda.get("spl_set_id"), list)
                    else openfda.get("spl_set_id"),
                    "indications_snip": ind_text[:400],
                    "hcc_mention": bool(_THEME.search(ind_text)),
                }
            )
    return {
        "search": search,
        "error": None,
        "total": total,
        "results": results_out,
        "url": url,
    }


def collect_openfda(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
) -> dict[str, object]:
    # Label churn is sparse vs papers: look back at least 30 days for effective_time.
    from datetime import timedelta

    lookback_start = min(window_start, window_end - timedelta(days=30))
    d0 = _ymd_compact(lookback_start)
    d1 = _ymd_compact(window_end)
    # Primary: indications mention HCC in recent effective_time window.
    q_hcc = (
        'indications_and_usage:("hepatocellular carcinoma" OR "liver cancer") '
        f"AND effective_time:[{d0} TO {d1}]"
    )
    hcc = _openfda_query(q_hcc, mailto=mailto, limit=25)
    time.sleep(0.5)

    # Secondary: watchlist drugs with any recent label effective_time (may be non-HCC).
    # Keep only rows that mention HCC in indications.
    drug_or = " OR ".join(f'"{d}"' for d in REGULATORY_DRUG_TERMS[:12])
    q_drugs = (
        f"openfda.generic_name:({drug_or}) OR openfda.brand_name:({drug_or}) "
        f"AND effective_time:[{d0} TO {d1}]"
    )
    drugs = _openfda_query(q_drugs, mailto=mailto, limit=25)
    drug_hcc = [
        r
        for r in (drugs.get("results") or [])
        if isinstance(r, dict) and r.get("hcc_mention")
    ]

    return {
        "window_effective_time": [d0, d1],
        "indications_hcc": hcc,
        "watchlist_recent": {
            "search": drugs.get("search"),
            "error": drugs.get("error"),
            "total": drugs.get("total"),
            "hcc_related_results": drug_hcc,
            "hcc_related_count": len(drug_hcc),
        },
    }


def collect_regulatory_html(*, mailto: str) -> list[dict[str, object]]:
    # Cast a wide net on the page, then keep HCC/liver-anchored rows only.
    wide = re.compile(
        JOURNAL_THEME_RE
        + r"|"
        + "|".join(re.escape(x) for x in REGULATORY_DRUG_TERMS)
        + r"|hepatocellular|liver cancer|hepatic",
        re.I,
    )
    # FDA oncology page lists many IO approvals; keep only liver/biliary disease rows.
    keep = re.compile(
        r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|"
        r"liver cancer|liver transplant|bile duct|biliary tract|\bBTC\b|"
        r"肝細胞|肝癌|胆管",
        re.I,
    )
    out: list[dict[str, object]] = []
    for source in REGULATORY_HTML_SOURCES:
        scanned = scan_source(source, mailto=mailto, theme=wide, max_hits=40)
        raw_hits = scanned.get("theme_hits") or []
        if not isinstance(raw_hits, list):
            raw_hits = []
        hits = [
            h
            for h in raw_hits
            if isinstance(h, dict)
            and keep.search(str(h.get("text") or "") + " " + str(h.get("href") or ""))
        ]
        scanned["theme_hits_prefilter_count"] = len(raw_hits)
        scanned["theme_hits"] = hits[:25]
        out.append(scanned)
    return out


def collect_regulatory(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
) -> dict[str, object]:
    dailymed = collect_dailymed_rss(mailto=mailto)
    openfda = collect_openfda(window_start, window_end, mailto=mailto)
    html_sources = collect_regulatory_html(mailto=mailto)

    openfda_n = 0
    ind = openfda.get("indications_hcc")
    if isinstance(ind, dict):
        openfda_n += len(ind.get("results") or [])
    wl = openfda.get("watchlist_recent")
    if isinstance(wl, dict):
        openfda_n += int(wl.get("hcc_related_count") or 0)

    return {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "dailymed": dailymed,
        "openfda": openfda,
        "html_sources": html_sources,
        "counts": {
            "dailymed_hits": dailymed.get("hit_count") or len(dailymed.get("hits") or []),
            "openfda_hcc_rows": openfda_n,
            "html_sources_ok": sum(
                1 for s in html_sources if isinstance(s, dict) and s.get("status") == 200
            ),
            "html_theme_hits": sum(
                len(s.get("theme_hits") or [])
                for s in html_sources
                if isinstance(s, dict)
            ),
        },
    }
