# Solidified collectors

Hourly HCC / hepatobiliary digest collectors live under `scripts/hcc_collect/`.

Automation agents should **call these scripts** instead of rewriting scrapers each hour.

## Secrets

- **Do not commit API keys.**
- OpenAlex key stays in the Automation prompt (or env). Pass at runtime:

```bash
export OPENALEX_API_KEY='YOUR_KEY_HERE'
python -m scripts.hcc_collect \
  --trigger-utc 2026-07-31T03:00:00.000Z \
  --out 202607/31/03 \
  --mailto research@example.com
```

Or:

```bash
python -m scripts.hcc_collect \
  --trigger-utc 2026-07-31T03:00:00.000Z \
  --openalex-api-key "$OPENALEX_API_KEY"
```

## What it writes

Into `--out` (default `YYYYMM/DD/HH` from trigger):

| File | Source |
|------|--------|
| `raw_pubmed.json` | PubMed EDAT/PDAT |
| `pubmed_clinical_leaning.json` | Title/pubtype clinical filter |
| `raw_pubmed_key_abstracts.json` | EFetch abstracts for clinical PMIDs |
| `raw_crossref.json` | Crossref created-date + title filter |
| `raw_clinicaltrials.json` | CT.gov LastUpdate window |
| `raw_openalex.json` | OpenAlex `publication_date` only |
| `raw_preprints.json` | medRxiv / bioRxiv / EuropePMC PPR |
| `raw_news_sentinel.json` | HTML news sentinels |
| `raw_journals_toc.json` | Journal RSS (J Hepatol / JHEP Reports / Ann Oncol) + PubMed journal EDAT |
| `raw_regulatory.json` | openFDA labels + DailyMed RSS + FDA/NICE HTML |
| `raw_guidelines_sentinel.json` | EASL / AASLD / NCCN / JSH / CSCO / NICE hubs |
| `collect_summary.json` | Machine counts + ID sets for delta |

Markdown briefs (`01_delta_brief.md`, …), `meta.json`, and root `README.md` remain **agent-written** after comparing with the previous hour.

## OpenAlex note

Use **`from_publication_date` / `to_publication_date` only**.  
`from_created_date` / `from_updated_date` require Premium and return 429 on free tier.

## Automation agent workflow

1. `git pull origin main`
2. Export key from prompt (do not write key into any tracked file):
   `export OPENALEX_API_KEY='…'`
3. Run collector:
   `python3 -m scripts.hcc_collect --trigger-utc "$TRIGGER_UTC" --out YYYYMM/DD/HH`
4. Compare `collect_summary.json` / raw ID sets vs previous hour
5. Write only markdown + `meta.json` + root `README.md` (do **not** rewrite collectors)
6. Commit pack → `git push origin main`
