"""Score PubMed records for clinical relevance."""

from __future__ import annotations

import re
from typing import Iterable, Mapping, Sequence

from .config import CLINICAL_KEYS_RE, FALSE_FRIENDS_RE, HCC_ANCHOR_RE

_KEYS = re.compile(CLINICAL_KEYS_RE, re.I)
_FALSE = re.compile(FALSE_FRIENDS_RE, re.I)
_ANCHOR = re.compile(HCC_ANCHOR_RE, re.I)

_CLINICAL_PUBTYPES = {
    "clinical trial",
    "randomized controlled trial",
    "meta-analysis",
    "systematic review",
    "practice guideline",
    "guideline",
    "observational study",
    "multicenter study",
}


def score_title(title: str, pubtypes: Sequence[str] | None = None) -> int:
    title = title or ""
    pts = [p.lower() for p in (pubtypes or [])]
    score = 0
    if _KEYS.search(title):
        score += 1
    if any(p in _CLINICAL_PUBTYPES or "clinical trial" in p for p in pts):
        score += 1
    if _FALSE.search(title) and not _ANCHOR.search(title):
        return 0
    if not _ANCHOR.search(title) and score == 0:
        return 0
    return score


def filter_clinical(
    records: Iterable[Mapping[str, object]],
) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for rec in records:
        title = str(rec.get("title") or "")
        pubtypes = rec.get("pubtype") or rec.get("pubtypes") or []
        if not isinstance(pubtypes, (list, tuple)):
            pubtypes = []
        sc = score_title(title, [str(p) for p in pubtypes])
        if sc <= 0:
            continue
        out.append(
            {
                "pmid": rec.get("pmid"),
                "title": title,
                "pubdate": rec.get("pubdate"),
                "source": rec.get("source"),
                "doi": rec.get("doi"),
                "score": sc,
            }
        )
    out.sort(key=lambda r: (-int(r["score"]), str(r.get("pmid") or "")))
    return out
