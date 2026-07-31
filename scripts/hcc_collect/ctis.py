"""EU CTIS public search collector (undocumented JSON API)."""

from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from typing import Optional

from .config import CTIS_MEDICAL_CONDITIONS, CTIS_RETRIEVE_URL, CTIS_SEARCH_URL
from .http_util import fetch_json, post_json

_FOCUS_RE = re.compile(
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|"
    r"biliary tract|\bBTC\b|bile duct cancer|intrahepatic|"
    r"(?<![A-Za-z])liver cancer(?![A-Za-z])",
    re.I,
)
# "excluding cholangiocarcinoma" / solid-tumor basket noise.
_EXCLUDE_RE = re.compile(
    r"excluding cholangiocarcin|solid tumors?\s*\(excluding|"
    r"chronic pancreatitis|primary biliary cholangitis|\bPBC\b",
    re.I,
)
_BASKET_RE = re.compile(
    r"selected advanced or metastatic solid tumors|"
    r"advanced or metastatic solid tumors|"
    r"locally advanced or metastatic solid tumors",
    re.I,
)


def _parse_eu_date(value: object) -> Optional[str]:
    """Normalize CTIS dates to YYYY-MM-DD when possible."""
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    # 09/07/2026 or 2026-07-09T...
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})$", s)
    if m:
        d, mo, y = m.group(1), m.group(2), m.group(3)
        return f"{y}-{mo}-{d}"
    if "T" in s:
        return s.split("T", 1)[0]
    if re.match(r"\d{4}-\d{2}-\d{2}", s):
        return s[:10]
    return s


def _is_focus(title: str, conditions: str) -> bool:
    blob = f"{title} {conditions}"
    if _EXCLUDE_RE.search(blob):
        return False
    if not _FOCUS_RE.search(blob):
        return False
    # Basket trials that only mention HCC among many tumors: keep but mark later.
    return True


def _is_basket(title: str, conditions: str) -> bool:
    blob = f"{title} {conditions}"
    # Multi-cohort solid-tumor studies (KEYNOTE-158 style) → observe only.
    if len(re.findall(r"\([A-Z]\)\s", conditions)) >= 4:
        return True
    if re.search(r"advanced solid tumors|predictive biomarkers", title, re.I):
        return True
    if _BASKET_RE.search(blob) and not re.search(
        r"hepatocellular carcinoma|\bHCC\b|cholangiocarcin",
        title,
        re.I,
    ):
        parts = re.split(r"[,;]", conditions)
        hcc_parts = [p for p in parts if _FOCUS_RE.search(p)]
        return len(parts) >= 3 and len(hcc_parts) <= 2
    return False


def _search_condition(
    condition: str,
    *,
    mailto: str,
    page_size: int = 50,
    max_pages: int = 3,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows: list[dict[str, object]] = []
    meta: dict[str, object] = {"condition": condition, "pages": [], "error": None}
    for page in range(1, max_pages + 1):
        payload = {
            "pagination": {"page": page, "size": page_size},
            "searchCriteria": {"medicalCondition": condition},
            "sort": {"property": "lastUpdated", "direction": "DESC"},
        }
        try:
            data = post_json(CTIS_SEARCH_URL, payload, mailto=mailto, timeout=60)
        except Exception as exc:  # noqa: BLE001
            meta["error"] = str(exc)[:240]
            break
        if not isinstance(data, dict):
            meta["error"] = "non_object_response"
            break
        pagination = data.get("pagination") if isinstance(data.get("pagination"), dict) else {}
        batch = data.get("data") if isinstance(data.get("data"), list) else []
        meta["pages"].append(
            {
                "page": page,
                "batch": len(batch),
                "totalRecords": pagination.get("totalRecords"),
                "totalPages": pagination.get("totalPages"),
            }
        )
        if page == 1:
            meta["totalRecords"] = pagination.get("totalRecords")
        for item in batch:
            if isinstance(item, dict):
                rows.append(item)
        total_pages = int(pagination.get("totalPages") or 1)
        if page >= total_pages or not batch:
            break
        time.sleep(0.45)
    return rows, meta


def _lite_row(item: dict[str, object]) -> dict[str, object]:
    title = str(item.get("ctTitle") or item.get("shortTitle") or "")
    conditions = str(item.get("conditions") or "")
    ct = str(item.get("ctNumber") or "")
    return {
        "ctNumber": ct,
        "title": title,
        "shortTitle": item.get("shortTitle"),
        "conditions": conditions,
        "ctStatus": item.get("ctStatus"),
        "trialPhase": item.get("trialPhase"),
        "sponsor": item.get("sponsor"),
        "sponsorType": item.get("sponsorType"),
        "decisionDateOverall": item.get("decisionDateOverall"),
        "decisionDateOverall_ymd": _parse_eu_date(item.get("decisionDateOverall")),
        "lastUpdated_ymd": _parse_eu_date(
            item.get("lastUpdated") or item.get("decisionDateOverall")
        ),
        "trialCountries": item.get("trialCountries"),
        "therapeuticAreas": item.get("therapeuticAreas"),
        "url": (
            f"https://euclinicaltrials.eu/search-for-clinical-trials/?lang=en&query={ct}"
            if ct
            else "https://euclinicaltrials.eu/ctis-public/search"
        ),
        "is_basket": _is_basket(title, conditions),
        "focus": _is_focus(title, conditions),
    }


def collect_ctis(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    conditions: tuple[str, ...] | list[str] | None = None,
    page_size: int = 50,
    max_pages_per_condition: int = 2,
) -> dict[str, object]:
    """Collect CTIS trials for HCC/CCA conditions; flag recent window updates."""
    conds = list(conditions or CTIS_MEDICAL_CONDITIONS)
    w0 = window_start.astimezone(timezone.utc).date().isoformat()
    w1 = window_end.astimezone(timezone.utc).date().isoformat()

    by_id: dict[str, dict[str, object]] = {}
    call_log: list[dict[str, object]] = []
    for cond in conds:
        rows, meta = _search_condition(
            cond,
            mailto=mailto,
            page_size=page_size,
            max_pages=max_pages_per_condition,
        )
        call_log.append(meta)
        for item in rows:
            lite = _lite_row(item)
            ct = str(lite.get("ctNumber") or "")
            if not ct:
                continue
            prev = by_id.get(ct)
            if prev is None:
                lite["matched_conditions"] = [cond]
                by_id[ct] = lite
            else:
                matched = prev.get("matched_conditions")
                if isinstance(matched, list) and cond not in matched:
                    matched.append(cond)
                if lite.get("focus"):
                    prev["focus"] = True
                # Prefer richer title/conditions; recompute basket on update.
                if len(str(lite.get("title") or "")) > len(str(prev.get("title") or "")):
                    prev["title"] = lite.get("title")
                if len(str(lite.get("conditions") or "")) > len(
                    str(prev.get("conditions") or "")
                ):
                    prev["conditions"] = lite.get("conditions")
                prev["is_basket"] = _is_basket(
                    str(prev.get("title") or ""),
                    str(prev.get("conditions") or ""),
                )
                if lite.get("is_basket"):
                    prev["is_basket"] = True

    related = [r for r in by_id.values() if r.get("focus")]
    related.sort(
        key=lambda r: str(r.get("lastUpdated_ymd") or r.get("decisionDateOverall_ymd") or ""),
        reverse=True,
    )

    recent = []
    for r in related:
        day = str(r.get("lastUpdated_ymd") or r.get("decisionDateOverall_ymd") or "")
        if day and w0 <= day <= w1:
            recent.append(r)

    focus = [r for r in related if not r.get("is_basket")]
    basket = [r for r in related if r.get("is_basket")]

    return {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "api": {
            "search": CTIS_SEARCH_URL,
            "retrieve": CTIS_RETRIEVE_URL,
            "note": "Undocumented public JSON API behind euclinicaltrials.eu; no SLA.",
        },
        "window": [w0, w1],
        "conditions_queried": conds,
        "call_log": call_log,
        "related": related,
        "related_count": len(related),
        "focus": focus,
        "focus_count": len(focus),
        "basket_observe": basket,
        "basket_count": len(basket),
        "recent_in_window": recent,
        "recent_count": len(recent),
        "recent_ct_numbers": [str(r.get("ctNumber")) for r in recent],
        "focus_ct_numbers": [str(r.get("ctNumber")) for r in focus],
    }
