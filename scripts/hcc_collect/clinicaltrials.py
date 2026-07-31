"""ClinicalTrials.gov v2 LastUpdate window collector."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Optional

from .config import CT_FORCE_INCLUDE_NCTS, CT_QUERY_COND
from .http_util import fetch_json, url_with_query

CT_BASE = "https://clinicaltrials.gov/api/v2/studies"

_FOCUS_RE = re.compile(
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|"
    r"\bTACE\b|\bHAIC\b|hepatic artery|intrahepatic|"
    r"biliary tract|bile duct|\bBTC\b|"
    r"(?<![A-Za-z])liver cancer(?![A-Za-z])|(?<![A-Za-z])cancer of the liver(?![A-Za-z])",
    re.I,
)
_FALSE_RE = re.compile(
    r"\b(colorectal|CRLM|breast cancer|lung cancer|prostate cancer|NSCLC|"
    r"mental health|PCOS|cervix|amyloidosis)\b",
    re.I,
)
_BASKET_HINT = re.compile(
    r"beyond walls|basket|solid neoplasm|multiple myeloma|amyloidosis",
    re.I,
)


def _ymd(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")


def _dig(d: object, *path: str) -> object:
    cur: object = d
    for key in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(key)
    return cur


def _parse_study(study: dict[str, object]) -> dict[str, object]:
    nct = str(_dig(study, "protocolSection", "identificationModule", "nctId") or "")
    title = str(
        _dig(study, "protocolSection", "identificationModule", "briefTitle") or ""
    )
    conditions_raw = _dig(study, "protocolSection", "conditionsModule", "conditions")
    conditions: list[str] = []
    if isinstance(conditions_raw, list):
        conditions = [str(c) for c in conditions_raw]
    status = str(
        _dig(study, "protocolSection", "statusModule", "overallStatus") or ""
    )
    last_update = str(
        _dig(study, "protocolSection", "statusModule", "lastUpdatePostDateStruct", "date")
        or _dig(study, "protocolSection", "statusModule", "lastUpdatePostDate")
        or ""
    )
    phases_raw = _dig(study, "protocolSection", "designModule", "phases")
    phases: list[str] = []
    if isinstance(phases_raw, list):
        phases = [str(p) for p in phases_raw]
    summary = str(
        _dig(study, "protocolSection", "descriptionModule", "briefSummary") or ""
    )
    return {
        "nct": nct,
        "nctId": nct,
        "title": title,
        "conditions": conditions,
        "lastUpdatePostDate": last_update,
        "overallStatus": status,
        "phases": phases,
        "briefSummary": summary[:500],
        "force_include": False,
    }


def _is_focus(rec: dict[str, object]) -> bool:
    if rec.get("force_include"):
        return True
    title = str(rec.get("title") or "")
    conditions = [str(c) for c in (rec.get("conditions") or [])]
    cond_blob = " | ".join(conditions)
    # Prefer title signal; avoid "Cancer Liver" + "Cancer of Cervix" → "Liver Cancer" FP.
    if _FOCUS_RE.search(title):
        return True
    if _BASKET_HINT.search(title) or len(conditions) >= 12:
        return False
    if _FALSE_RE.search(title) and not _FOCUS_RE.search(cond_blob):
        return False
    # Condition-level match only when the study is narrowly themed.
    if len(conditions) <= 6 and _FOCUS_RE.search(cond_blob):
        if _FALSE_RE.search(cond_blob) and not _FOCUS_RE.search(title):
            # e.g. Hep B + cervix + "Cancer Liver" wording — require title theme.
            return False
        return True
    return False


def collect_clinicaltrials(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    force_include: tuple[str, ...] | list[str] | None = None,
    page_size: int = 100,
) -> dict[str, object]:
    d0 = _ymd(window_start)
    d1 = _ymd(window_end)
    force = {x.upper() for x in (force_include or CT_FORCE_INCLUDE_NCTS)}

    url = url_with_query(
        CT_BASE,
        {
            "query.cond": CT_QUERY_COND,
            "filter.advanced": f"AREA[LastUpdatePostDate]RANGE[{d0},{d1}]",
            "pageSize": page_size,
            "format": "json",
        },
    )
    payload = fetch_json(url, mailto=mailto, timeout=90)
    studies_raw = []
    if isinstance(payload, dict):
        studies_raw = payload.get("studies") or []
        if not isinstance(studies_raw, list):
            studies_raw = []

    related: list[dict[str, object]] = []
    seen: set[str] = set()
    for study in studies_raw:
        if not isinstance(study, dict):
            continue
        rec = _parse_study(study)
        nct = str(rec.get("nct") or "").upper()
        if not nct or nct in seen:
            continue
        if nct in force:
            rec["force_include"] = True
        seen.add(nct)
        related.append(rec)

    # Ensure force-includes appear even if API window missed them (best-effort fetch).
    for nct in sorted(force):
        if nct in seen:
            continue
        try:
            one = fetch_json(
                f"https://clinicaltrials.gov/api/v2/studies/{nct}",
                mailto=mailto,
                timeout=60,
            )
            if isinstance(one, dict):
                # v2 single study may wrap under 'protocolSection' directly
                if "protocolSection" in one:
                    rec = _parse_study(one)
                elif isinstance(one.get("studies"), list) and one["studies"]:
                    first = one["studies"][0]
                    rec = _parse_study(first if isinstance(first, dict) else {})
                else:
                    continue
                rec["force_include"] = True
                related.append(rec)
                seen.add(nct)
        except Exception:  # noqa: BLE001
            related.append(
                {
                    "nct": nct,
                    "nctId": nct,
                    "title": "",
                    "conditions": [],
                    "lastUpdatePostDate": "",
                    "overallStatus": "",
                    "phases": [],
                    "briefSummary": "",
                    "force_include": True,
                    "fetch_error": "force_include_missed_window",
                }
            )

    # Drop solid-tumor / PCOS / generic basket noise from "related".
    related_kept = [r for r in related if _is_focus(r)]
    focus = list(related_kept)
    return {
        "window": [d0, d1],
        "total_fetched": len(studies_raw),
        "related": related_kept,
        "related_ncts": [str(r.get("nct")) for r in related_kept],
        "focus": focus,
        "focus_ncts": [str(r.get("nct")) for r in focus],
        "related_count": len(related_kept),
        "focus_count": len(focus),
        "query_cond": CT_QUERY_COND,
    }
