"""CLI entry for solidified HCC collectors."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .collect import (
    find_previous_folder,
    folder_from_trigger,
    parse_trigger_utc,
    resolve_openalex_key,
    run_collect,
)
from .config import DEFAULT_MAILTO


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m scripts.hcc_collect",
        description=(
            "Collect PubMed / Crossref / ClinicalTrials / OpenAlex / preprints / news / "
            "media-watch raw JSON for one HCC hourly pack. API keys are NEVER read from "
            "the repo; pass --openalex-api-key or set OPENALEX_API_KEY."
        ),
    )
    p.add_argument(
        "--trigger-utc",
        required=True,
        help="Automation trigger instant, e.g. 2026-07-31T02:02:58.179Z",
    )
    p.add_argument(
        "--out",
        default=None,
        help="Output folder (default: YYYYMM/DD/HH from --trigger-utc)",
    )
    p.add_argument(
        "--repo-root",
        default=".",
        help="Repository root used to resolve relative --out / previous folder",
    )
    p.add_argument(
        "--window-hours",
        type=int,
        default=24,
        help="Lookback window ending at trigger (default: 24)",
    )
    p.add_argument(
        "--previous-dir",
        default=None,
        help="Previous pack folder for preprint continuity (default: auto-detect)",
    )
    p.add_argument(
        "--mailto",
        default=DEFAULT_MAILTO,
        help="Contact email for polite API User-Agent / Crossref mailto",
    )
    p.add_argument(
        "--openalex-api-key",
        default=None,
        help="OpenAlex API key (preferred: env OPENALEX_API_KEY). Do not commit keys.",
    )
    p.add_argument(
        "--skip-news",
        action="store_true",
        help="Skip HTML news sentinel scrape",
    )
    p.add_argument(
        "--skip-journals",
        action="store_true",
        help="Skip journal RSS / PubMed journal TOC collectors",
    )
    p.add_argument(
        "--skip-regulatory",
        action="store_true",
        help="Skip FDA/DailyMed/NICE regulatory collectors",
    )
    p.add_argument(
        "--skip-guidelines",
        action="store_true",
        help="Skip EASL/AASLD/NCCN/JSH/CSCO guideline HTML sentinels",
    )
    p.add_argument(
        "--skip-hta",
        action="store_true",
        help="Skip NICE HTA product lists + EMA CHMP highlights sentinels",
    )
    p.add_argument(
        "--skip-ctis",
        action="store_true",
        help="Skip EU CTIS public search collector",
    )
    p.add_argument(
        "--skip-media",
        action="store_true",
        help="Skip media/trade-press attention sentinel (Google News + CancerNetwork + ESMO)",
    )
    p.add_argument(
        "--abstract-limit",
        type=int,
        default=40,
        help="Max PubMed abstracts to efetch for clinical-leaning PMIDs",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    trigger = parse_trigger_utc(args.trigger_utc)
    repo_root = Path(args.repo_root).resolve()
    folder = args.out or folder_from_trigger(trigger)
    out_dir = Path(folder)
    if not out_dir.is_absolute():
        out_dir = repo_root / out_dir

    previous: Path | None = None
    if args.previous_dir:
        previous = Path(args.previous_dir)
        if not previous.is_absolute():
            previous = repo_root / previous
    else:
        rel = find_previous_folder(repo_root, folder.replace("\\", "/"))
        if rel:
            previous = repo_root / rel

    api_key = resolve_openalex_key(args.openalex_api_key)

    print(
        json.dumps(
            {
                "event": "hcc_collect_start",
                "out": str(out_dir),
                "trigger_utc": args.trigger_utc,
                "previous": str(previous) if previous else None,
                "openalex_api_key_present": bool(api_key),
            },
            ensure_ascii=False,
        ),
        flush=True,
    )

    summary = run_collect(
        out_dir=out_dir,
        trigger_utc=trigger,
        window_hours=args.window_hours,
        mailto=args.mailto,
        openalex_api_key=api_key,
        previous_dir=previous,
        skip_news=args.skip_news,
        skip_journals=args.skip_journals,
        skip_regulatory=args.skip_regulatory,
        skip_guidelines=args.skip_guidelines,
        skip_hta=args.skip_hta,
        skip_ctis=args.skip_ctis,
        skip_media=args.skip_media,
        abstract_limit=args.abstract_limit,
    )
    print(json.dumps({"event": "hcc_collect_done", **summary}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
