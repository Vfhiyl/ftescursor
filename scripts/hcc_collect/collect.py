"""Orchestrate all collectors and write raw pack files."""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from .clinical_leaning import filter_clinical
from .clinicaltrials import collect_clinicaltrials
from .crossref import collect_crossref
from .news import collect_news
from .openalex import collect_openalex
from .preprints import collect_preprints
from .pubmed import collect_pubmed, fetch_abstracts


def parse_trigger_utc(value: str) -> datetime:
    s = value.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def folder_from_trigger(trigger: datetime) -> str:
    return trigger.strftime("%Y%m/%d/%H")


def find_previous_folder(repo_root: Path, current_folder: str) -> Optional[str]:
    """Find the chronologically previous YYYYMM/DD/HH directory under repo_root."""
    cur = repo_root / current_folder
    candidates: list[str] = []
    for meta in repo_root.glob("*/[0-9][0-9]/[0-9][0-9]/meta.json"):
        folder = str(meta.parent.relative_to(repo_root)).replace("\\", "/")
        if folder < current_folder:
            candidates.append(folder)
    if not candidates:
        # also allow deeper glob already used; try listing year roots
        for meta in repo_root.glob("*/*/*/meta.json"):
            folder = str(meta.parent.relative_to(repo_root)).replace("\\", "/")
            if folder < current_folder and folder != current_folder:
                candidates.append(folder)
    if not candidates:
        return None
    return sorted(set(candidates))[-1]


def _load_json(path: Path) -> object | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _continuity_from_previous(prev_dir: Path) -> list[dict[str, object]]:
    raw = _load_json(prev_dir / "raw_preprints.json")
    if not isinstance(raw, dict):
        return []
    out: list[dict[str, object]] = []
    for key in ("medrxiv", "biorxiv"):
        items = raw.get(key) or []
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict) and item.get("doi"):
                out.append(item)
    cont = raw.get("continuity") or []
    if isinstance(cont, list):
        for item in cont:
            if isinstance(item, dict) and item.get("doi"):
                out.append(item)
    return out


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run_collect(
    *,
    out_dir: Path,
    trigger_utc: datetime,
    window_hours: int = 24,
    mailto: str,
    openalex_api_key: Optional[str] = None,
    previous_dir: Optional[Path] = None,
    skip_news: bool = False,
    abstract_limit: int = 40,
) -> dict[str, object]:
    window_end = trigger_utc
    window_start = trigger_utc - timedelta(hours=window_hours)
    collected_at = datetime.now(timezone.utc)

    pubmed = collect_pubmed(window_start, window_end, mailto=mailto)
    write_json(out_dir / "raw_pubmed.json", pubmed)

    lite = pubmed.get("edat_summaries_lite") or []
    if not isinstance(lite, list):
        lite = []
    clinical = filter_clinical(
        [x for x in lite if isinstance(x, dict)]
    )
    write_json(out_dir / "pubmed_clinical_leaning.json", clinical)

    clinical_pmids = [str(x.get("pmid")) for x in clinical if x.get("pmid")]
    abstracts = fetch_abstracts(clinical_pmids, mailto=mailto, limit=abstract_limit)
    write_json(out_dir / "raw_pubmed_key_abstracts.json", abstracts)

    crossref = collect_crossref(window_start, window_end, mailto=mailto)
    write_json(out_dir / "raw_crossref.json", crossref)

    trials = collect_clinicaltrials(window_start, window_end, mailto=mailto)
    write_json(out_dir / "raw_clinicaltrials.json", trials)

    openalex = collect_openalex(
        window_start,
        window_end,
        mailto=mailto,
        api_key=openalex_api_key,
    )
    write_json(out_dir / "raw_openalex.json", openalex)

    continuity: list[dict[str, object]] = []
    if previous_dir is not None:
        continuity = _continuity_from_previous(previous_dir)
    preprints = collect_preprints(
        window_start, window_end, mailto=mailto, continuity=continuity
    )
    write_json(out_dir / "raw_preprints.json", preprints)

    news: dict[str, object] | None = None
    if not skip_news:
        news = collect_news(mailto=mailto)
        write_json(out_dir / "raw_news_sentinel.json", news)

    summary = {
        "folder": str(out_dir).replace("\\", "/"),
        "trigger_utc": trigger_utc.isoformat().replace("+00:00", "Z"),
        "collected_at_utc": collected_at.isoformat(),
        "window_start_utc": window_start.isoformat(),
        "window_end_utc": window_end.isoformat(),
        "window_hours": window_hours,
        "mailto": mailto,
        "openalex_api_key_present": bool(openalex_api_key),
        "counts": {
            "pubmed_edat": pubmed.get("edat", {}).get("count")
            if isinstance(pubmed.get("edat"), dict)
            else len(pubmed.get("edat_ids") or []),
            "pubmed_pdat": pubmed.get("pdat", {}).get("count")
            if isinstance(pubmed.get("pdat"), dict)
            else len(pubmed.get("pdat_ids") or []),
            "pubmed_clinical_leaning": len(clinical),
            "crossref_title_filtered": crossref.get("unique_title_filtered_count"),
            "clinicaltrials_related": trials.get("related_count"),
            "clinicaltrials_focus": trials.get("focus_count"),
            "openalex_works": openalex.get("works_count"),
            "openalex_preprints": openalex.get("preprint_count"),
            "preprints_medrxiv": preprints.get("counts", {}).get("medrxiv")
            if isinstance(preprints.get("counts"), dict)
            else None,
            "preprints_biorxiv": preprints.get("counts", {}).get("biorxiv")
            if isinstance(preprints.get("counts"), dict)
            else None,
            "preprints_europepmc_ppr": preprints.get("counts", {}).get("europepmc_ppr")
            if isinstance(preprints.get("counts"), dict)
            else None,
            "news_sources_ok": sum(
                1
                for s in (news or {}).get("sources", [])
                if isinstance(s, dict) and s.get("status") == 200
            )
            if news
            else None,
        },
        "id_sets": {
            "pubmed_edat_ids": pubmed.get("edat_ids") or [],
            "crossref_dois": [
                str(x.get("DOI"))
                for x in (crossref.get("unique_title_filtered") or [])
                if isinstance(x, dict)
            ],
            "clinicaltrials_focus_ncts": trials.get("focus_ncts") or [],
            "openalex_dois": [
                str(x.get("doi"))
                for x in (openalex.get("works") or [])
                if isinstance(x, dict) and x.get("doi")
            ],
        },
        "files_written": [
            "raw_pubmed.json",
            "pubmed_clinical_leaning.json",
            "raw_pubmed_key_abstracts.json",
            "raw_crossref.json",
            "raw_clinicaltrials.json",
            "raw_openalex.json",
            "raw_preprints.json",
        ]
        + (["raw_news_sentinel.json"] if news is not None else []),
    }
    write_json(out_dir / "collect_summary.json", summary)
    return summary


def resolve_openalex_key(cli_value: Optional[str]) -> Optional[str]:
    if cli_value:
        return cli_value.strip() or None
    for env_name in ("OPENALEX_API_KEY", "OPENALEX_KEY"):
        val = os.environ.get(env_name)
        if val and val.strip():
            return val.strip()
    return None
