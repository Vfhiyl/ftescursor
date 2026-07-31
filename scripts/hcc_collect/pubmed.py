"""PubMed EDAT / PDAT collectors via NCBI E-utilities."""

from __future__ import annotations

import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Optional
from xml.etree.ElementTree import Element

from .config import PUBMED_TERM
from .http_util import fetch_json, fetch_text, url_with_query

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def _ymd_slash(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y/%m/%d")


def _esearch(term: str, *, mailto: str, retmax: int = 200) -> dict[str, object]:
    url = url_with_query(
        f"{EUTILS}/esearch.fcgi",
        {
            "db": "pubmed",
            "term": term,
            "retmax": retmax,
            "retmode": "json",
            "email": mailto,
            "tool": "hcc_digest",
        },
    )
    data = fetch_json(url, mailto=mailto)
    if not isinstance(data, dict):
        raise TypeError("esearch returned non-object JSON")
    return data


def _esummary(ids: list[str], *, mailto: str) -> dict[str, object]:
    out: dict[str, object] = {}
    for i in range(0, len(ids), 100):
        batch = ids[i : i + 100]
        url = url_with_query(
            f"{EUTILS}/esummary.fcgi",
            {
                "db": "pubmed",
                "id": ",".join(batch),
                "retmode": "json",
                "email": mailto,
                "tool": "hcc_digest",
            },
        )
        data = fetch_json(url, mailto=mailto)
        if not isinstance(data, dict):
            raise TypeError("esummary returned non-object JSON")
        result = data.get("result")
        if isinstance(result, dict):
            out.update(result)
        time.sleep(0.35)
    return out


def _article_id_doi(article_ids: object) -> Optional[str]:
    if not isinstance(article_ids, list):
        return None
    for item in article_ids:
        if isinstance(item, dict) and item.get("idtype") == "doi":
            return str(item.get("value") or "")
    return None


def _lite_from_summary(pmid: str, summary: object) -> dict[str, object]:
    if not isinstance(summary, dict):
        return {"pmid": pmid, "title": "", "source": "", "pubdate": "", "doi": None, "pubtype": []}
    authors = summary.get("authors") or []
    author_names: list[str] = []
    if isinstance(authors, list):
        for a in authors[:8]:
            if isinstance(a, dict) and a.get("name"):
                author_names.append(str(a["name"]))
    pubtypes = summary.get("pubtype") or []
    if not isinstance(pubtypes, list):
        pubtypes = []
    return {
        "pmid": pmid,
        "title": str(summary.get("title") or ""),
        "source": str(summary.get("source") or ""),
        "pubdate": str(summary.get("pubdate") or ""),
        "epubdate": str(summary.get("epubdate") or ""),
        "authors": author_names,
        "doi": _article_id_doi(summary.get("articleids")),
        "pubtype": [str(p) for p in pubtypes],
    }


def fetch_abstracts(pmids: list[str], *, mailto: str, limit: int = 40) -> list[dict[str, str]]:
    ids = pmids[:limit]
    if not ids:
        return []
    url = url_with_query(
        f"{EUTILS}/efetch.fcgi",
        {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "xml",
            "email": mailto,
            "tool": "hcc_digest",
        },
    )
    xml_text = fetch_text(url, mailto=mailto, timeout=90)
    root = ET.fromstring(xml_text)
    out: list[dict[str, str]] = []
    for article in root.findall(".//PubmedArticle"):
        medline = article.find("MedlineCitation")
        if medline is None:
            continue
        pmid_el = medline.find("PMID")
        pmid = pmid_el.text if pmid_el is not None else ""
        title_el = article.find(".//ArticleTitle")
        title = "".join(title_el.itertext()).strip() if title_el is not None else ""
        abs_parts: list[str] = []
        for abs_el in article.findall(".//Abstract/AbstractText"):
            label = abs_el.attrib.get("Label")
            text = "".join(abs_el.itertext()).strip()
            if label:
                abs_parts.append(f"{label}: {text}")
            elif text:
                abs_parts.append(text)
        out.append({"pmid": pmid or "", "title": title, "abstract": " ".join(abs_parts)})
    return out


def collect_pubmed(
    window_start: datetime,
    window_end: datetime,
    *,
    mailto: str,
    term: str = PUBMED_TERM,
) -> dict[str, object]:
    d0 = _ymd_slash(window_start)
    d1 = _ymd_slash(window_end)
    q_edat = f"({term}) AND (\"{d0}\"[EDAT] : \"{d1}\"[EDAT])"
    q_pdat = f"({term}) AND (\"{d0}\"[PDAT] : \"{d1}\"[PDAT])"

    edat_raw = _esearch(q_edat, mailto=mailto)
    time.sleep(0.35)
    pdat_raw = _esearch(q_pdat, mailto=mailto)

    def ids_of(payload: dict[str, object]) -> list[str]:
        esearchresult = payload.get("esearchresult")
        if not isinstance(esearchresult, dict):
            return []
        idlist = esearchresult.get("idlist")
        if not isinstance(idlist, list):
            return []
        return [str(x) for x in idlist]

    edat_ids = ids_of(edat_raw)
    pdat_ids = ids_of(pdat_raw)
    summaries = _esummary(edat_ids, mailto=mailto) if edat_ids else {}

    lite: list[dict[str, object]] = []
    for pmid in edat_ids:
        lite.append(_lite_from_summary(pmid, summaries.get(pmid)))

    return {
        "query": term,
        "window_start_utc": window_start.astimezone(timezone.utc).isoformat(),
        "window_end_utc": window_end.astimezone(timezone.utc).isoformat(),
        "edat": {"count": len(edat_ids), "ids": edat_ids},
        "pdat": {"count": len(pdat_ids), "ids": pdat_ids},
        "edat_ids": edat_ids,
        "pdat_ids": pdat_ids,
        "edat_summaries_lite": lite,
        "window": {"edat_from": d0, "edat_to": d1},
    }


def text_of_element(el: Element | None) -> str:
    if el is None:
        return ""
    return "".join(el.itertext()).strip()
