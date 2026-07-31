"""medRxiv / bioRxiv / EuropePMC preprint collectors."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Optional
from urllib.parse import quote

from .config import PREPRINT_FP_RE, PREPRINT_THEME_RE
from .http_util import fetch_json

_THEME = re.compile(PREPRINT_THEME_RE, re.I)
_FP = re.compile(PREPRINT_FP_RE, re.I)

BIORXIV_DETAILS = "https://api.biorxiv.org/details"


def _ymd(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")


def _in_window(date_s: str, d0: str, d1: str) -> bool:
    if not date_s:
        return False
    day = date_s[:10]
    return d0 <= day <= d1


def _server_details(
    server: str,
    d0: str,
    d1: str,
    *,
    mailto: str,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Return (kept, fp_trimmed)."""
    url = f"{BIORXIV_DETAILS}/{server}/{d0}/{d1}"
    try:
        payload = fetch_json(url, mailto=mailto, timeout=90)
    except Exception as exc:  # noqa: BLE001
        return [], [{"server": server, "error": str(exc)}]

    collection = []
    if isinstance(payload, dict):
        collection = payload.get("collection") or []
        if not isinstance(collection, list):
            collection = []

    kept: list[dict[str, object]] = []
    trimmed: list[dict[str, object]] = []
    seen: set[str] = set()
    for item in collection:
        if not isinstance(item, dict):
            continue
        doi = str(item.get("doi") or "").lower()
        title = str(item.get("title") or "")
        date = str(item.get("date") or "")
        if not doi or doi in seen:
            continue
        seen.add(doi)
        if not _in_window(date, d0, d1) and date:
            # API already scoped; keep anyway if present.
            pass
        blob = f"{title} {item.get('category') or ''}"
        if _FP.search(title) and not _THEME.search(blob):
            trimmed.append({"doi": doi, "title": title, "reason": f"{server}_fp"})
            continue
        if not _THEME.search(blob):
            trimmed.append({"doi": doi, "title": title, "reason": f"{server}_offtheme"})
            continue
        kept.append(
            {
                "doi": doi,
                "title": title,
                "date": date,
                "server": server,
                "version": str(item.get("version") or ""),
                "abstract_snip": str(item.get("abstract") or "")[:280],
            }
        )
    return kept, trimmed


def _europepmc(d0: str, d1: str, *, mailto: str) -> list[dict[str, object]]:
    query = (
        "SRC:PPR AND "
        "(hepatocellular OR HCC OR cholangiocarcinoma OR hepatectomy OR TACE OR "
        '"liver cancer" OR hepatobiliary) AND '
        f"FIRST_PDATE:[{d0} TO {d1}]"
    )
    url = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        f"?query={quote(query)}&format=json&pageSize=100&resultType=lite"
    )
    try:
        payload = fetch_json(url, mailto=mailto, timeout=90)
    except Exception:  # noqa: BLE001
        return []
    results = []
    if isinstance(payload, dict):
        result_list = payload.get("resultList")
        if isinstance(result_list, dict):
            results = result_list.get("result") or []
            if not isinstance(results, list):
                results = []
    out: list[dict[str, object]] = []
    for item in results:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "")
        if _FP.search(title) and not _THEME.search(title):
            continue
        out.append(
            {
                "id": item.get("id"),
                "doi": str(item.get("doi") or "").lower() or None,
                "title": title,
                "firstPublicationDate": item.get("firstPublicationDate"),
                "source": item.get("source") or "PPR",
            }
        )
    return out


def collect_preprints(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    continuity: Optional[list[dict[str, object]]] = None,
) -> dict[str, object]:
    d0 = _ymd(window_start)
    d1 = _ymd(window_end)

    med, med_fp = _server_details("medrxiv", d0, d1, mailto=mailto)
    bio, bio_fp = _server_details("biorxiv", d0, d1, mailto=mailto)
    epmc = _europepmc(d0, d1, mailto=mailto)

    # Continuity: retain prior-hour theme preprints still useful for SEEN tracking.
    cont_out: list[dict[str, object]] = []
    have = {str(x.get("doi") or "").lower() for x in med + bio}
    for item in continuity or []:
        doi = str(item.get("doi") or "").lower()
        if not doi or doi in have:
            continue
        server = str(item.get("server") or "")
        title = str(item.get("title") or "")
        rec = {
            "doi": doi,
            "title": title,
            "date": item.get("date"),
            "server": server,
            "version": item.get("version"),
            "via": "continuity",
        }
        if server == "medrxiv":
            med.append(rec)
        elif server == "biorxiv":
            bio.append(rec)
        cont_out.append(
            {
                "doi": doi,
                "server": server,
                "title": title,
                "date": item.get("date"),
                "version": item.get("version"),
            }
        )
        have.add(doi)

    fp_trimmed = [x for x in (med_fp + bio_fp) if "error" not in x]
    return {
        "window": [d0, d1],
        "medrxiv": med,
        "biorxiv": bio,
        "europepmc_ppr": epmc,
        "counts": {
            "medrxiv": len(med),
            "biorxiv": len(bio),
            "europepmc_ppr": len(epmc),
        },
        "fp_trimmed": fp_trimmed,
        "continuity": cont_out,
    }
