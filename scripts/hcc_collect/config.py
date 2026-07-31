"""Static collector configuration. No API secrets here."""

from __future__ import annotations

DEFAULT_MAILTO = "research@example.com"
USER_AGENT_TEMPLATE = "HCC-Digest/1.0 (mailto:{mailto}; +https://github.com/Vfhiyl/ftescursor)"

# PubMed Title/Abstract OR-term (aligned to hourly packs on main).
PUBMED_TERM = (
    '("hepatocellular carcinoma"[Title/Abstract] OR "liver cancer"[Title/Abstract] OR '
    "HCC[Title/Abstract] OR cholangiocarcinoma[Title/Abstract] OR "
    'hepatectomy[Title/Abstract] OR "hepatobiliary"[Title/Abstract] OR '
    'TACE[Title/Abstract] OR "hepatic resection"[Title/Abstract] OR '
    "HAIC[Title/Abstract] OR SBRT[Title/Abstract] OR radioembolization[Title/Abstract] OR "
    '"Y-90"[Title/Abstract] OR yttrium-90[Title/Abstract] OR '
    "atezolizumab[Title/Abstract] OR durvalumab[Title/Abstract] OR "
    "lenvatinib[Title/Abstract])"
)

CROSSREF_QUERIES = [
    "hepatocellular carcinoma",
    "hepatectomy HCC",
    "TACE immunotherapy",
    "cholangiocarcinoma",
    "liver transplantation HCC",
    "EMERALD hepatocellular",
    "HAIC hepatocellular",
    "SBRT hepatocellular",
]

CROSSREF_TITLE_RE = (
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|\bTACE\b|"
    r"liver cancer|hepatic resection|bile duct|biliary tract|yttrium|radioembol|"
    r"\bHAIC\b|\bSBRT\b|lenvatinib|atezolizumab|durvalumab|hepatoma|"
    r"locoregional|liver transplantation"
)

CT_QUERY_COND = "hepatocellular carcinoma OR liver cancer OR cholangiocarcinoma"

# Keep even when conditions look CRC / solid-tumor metastatic.
CT_FORCE_INCLUDE_NCTS = (
    "NCT07715903",
)

# EU CTIS public search (undocumented JSON API behind euclinicaltrials.eu).
CTIS_SEARCH_URL = "https://euclinicaltrials.eu/ctis-public-api/search"
CTIS_RETRIEVE_URL = "https://euclinicaltrials.eu/ctis-public-api/retrieve"
CTIS_MEDICAL_CONDITIONS = (
    "hepatocellular carcinoma",
    "cholangiocarcinoma",
)

OPENALEX_FULLTEXT_OR = "TACE|cholangiocarcinoma|hepatectomy|hepatocellular carcinoma"

NEWS_SOURCES = [
    {"lang": "en", "name": "ESMO Daily Reporter", "url": "https://dailyreporter.esmo.org/"},
    {"lang": "en", "name": "ASCO Post", "url": "https://ascopost.com/"},
    {"lang": "en", "name": "OncLive", "url": "https://www.onclive.com/"},
    {"lang": "ja", "name": "日経がんナビ", "url": "https://oncolo.jp/"},
    {"lang": "zh", "name": "国家卫健委", "url": "https://www.nhc.gov.cn/"},
    {"lang": "fr", "name": "HAS", "url": "https://www.has-sante.fr/"},
    {"lang": "de", "name": "AWMF", "url": "https://www.awmf.org/"},
    {"lang": "ru", "name": "Minzdrav", "url": "https://minzdrav.gov.ru/"},
    {"lang": "ko", "name": "KLCA", "url": "https://www.livercancer.or.kr/"},
]

# Hepatobiliary-focused guideline / practice-update landing pages (HTML sentinel).
GUIDELINE_SOURCES = [
    {
        "lang": "en",
        "name": "EASL Clinical Practice Guidelines",
        "url": "https://easl.eu/publication-category/clinical-practice-guidelines/",
    },
    {
        "lang": "en",
        "name": "AASLD Practice Guidelines",
        "url": "https://www.aasld.org/practice-guidelines",
    },
    {
        "lang": "en",
        "name": "NCCN Recently Published Guidelines",
        "url": "https://www.nccn.org/guidelines/recently-published-guidelines",
    },
    {
        "lang": "en",
        "name": "NCCN Hepatocellular Carcinoma (public detail)",
        "url": "https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1438",
    },
    {
        "lang": "ja",
        "name": "JSH",
        "url": "https://www.jsh.or.jp/",
    },
    {
        "lang": "zh",
        "name": "CSCO",
        "url": "https://www.csco.org.cn/",
    },
    {
        "lang": "en",
        "name": "NICE liver cancers guidance",
        "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer/liver-cancers",
    },
]

# Journal TOC: Elsevier ScienceDirect RSS (stable) + PubMed journal EDAT fallback.
JOURNAL_RSS_FEEDS = [
    {
        "name": "Journal of Hepatology",
        "issn": "0168-8278",
        "rss": "https://rss.sciencedirect.com/publication/science/01688278",
    },
    {
        "name": "JHEP Reports",
        "issn": "2589-5559",
        "rss": "https://rss.sciencedirect.com/publication/science/25895559",
    },
    {
        "name": "Annals of Oncology",
        "issn": "0923-7534",
        "rss": "https://rss.sciencedirect.com/publication/science/09237534",
    },
]

# LWW/Karger often 403 RSS; use PubMed [Journal] EDAT window as TOC proxy.
JOURNAL_PUBMED_NAMES = [
    "J Hepatol",
    "JHEP Reports",
    "Hepatology",
    "Liver Cancer",
    "Ann Oncol",
]

# Regulatory / label watchlist (generic + common brands).
REGULATORY_DRUG_TERMS = [
    "atezolizumab",
    "tecentriq",
    "durvalumab",
    "imfinzi",
    "tremelimumab",
    "imjudo",
    "lenvatinib",
    "lenvima",
    "sorafenib",
    "nexavar",
    "regorafenib",
    "stivarga",
    "cabozantinib",
    "cabometyx",
    "bevacizumab",
    "avastin",
    "nivolumab",
    "opdivo",
    "pembrolizumab",
    "keytruda",
    "camrelizumab",
    "sintilimab",
    "donafenib",
    "tiragolumab",
]

REGULATORY_HTML_SOURCES = [
    {
        "name": "FDA Oncology approval notifications",
        "url": (
            "https://www.fda.gov/drugs/resources-information-approved-drugs/"
            "oncology-cancerhematologic-malignancies-approval-notifications"
        ),
    },
]

# NICE HTA product lists (static HTML titles; best HTA sentinel for HCC).
HTA_NICE_LISTS = [
    {
        "name": "NICE liver cancers — published TA",
        "status": "published_ta",
        "url": (
            "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer/"
            "liver-cancers/products?GuidanceProgramme=TA&Status=Published"
        ),
    },
    {
        "name": "NICE liver cancers — in development",
        "status": "in_development",
        "url": (
            "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer/"
            "liver-cancers/products?Status=InDevelopment"
        ),
    },
    {
        "name": "NICE liver cancers — updated in last 6 months",
        "status": "updated_6m",
        "url": (
            "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer/"
            "liver-cancers/products?ProductType=Guidance&Recent=UpdatedInLast6Months"
            "&Status=Published"
        ),
    },
]

EMA_NEWS_URL = "https://www.ema.europa.eu/en/news"
EMA_CHMP_HIGHLIGHTS_RE = (
    r"Meeting highlights from the Committee for Medicinal Products for Human Use \(CHMP\)"
)

NEWS_THEME_RE = (
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatectomy|\bTACE\b|\bHAIC\b|"
    r"\bSBRT\b|EMERALD|lenvatinib|atezolizumab|durvalumab|liver cancer|"
    r"肝细胞癌|肝癌|胆管癌|肝切除|肝がん|肝細胞癌"
)

CLINICAL_KEYS_RE = (
    r"trial|phase\s*[I1-3IVX]+|randomi|meta-analy|systematic review|cohort|"
    r"prospective|retrospective|survival|overall survival|progression|resect|"
    r"transplant|TACE|TARE|SBRT|neoadjuvant|adjuvant|guideline|consensus|outcome|"
    r"prognos|recurrence|immunotherap|atezolizumab|durvalumab|pembrolizumab|"
    r"camrelizumab|lenvatinib|sorafenib|bevacizumab|HAIC|radioembol|ablation|"
    r"microwave|\bRFA\b|BCLC|Child-Pugh|\bMELD\b|emboliz|conversion|"
    r"perioperative|locoregional|Y-90|yttrium|finotonlimab|sintilimab|"
    r"TORCH|EMERALD|GPC3|TCR"
)

FALSE_FRIENDS_RE = (
    r"\b(colorectal|CRLM|ADHD|pediatric cholecystectomy|appendec|"
    r"breast cancer|lung cancer|prostate cancer|NSCLC|veterinary)\b"
)

HCC_ANCHOR_RE = (
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|"
    r"\bTACE\b|liver cancer|hepatic|bile duct|biliary|hepatoma|\bHAIC\b|\bSBRT\b"
)

# Stricter theme for journal TOC / guideline hubs (avoid bare hepatic/biliary noise).
JOURNAL_THEME_RE = (
    r"hepatocellular|\bHCC\b|cholangiocarcin|hepatobiliary|hepatectomy|"
    r"\bTACE\b|\bHAIC\b|\bSBRT\b|liver cancer|hepatoma|"
    r"liver transplantation|locoregional|radioembol|yttrium|"
    r"lenvatinib|atezolizumab|durvalumab|BCLC"
)

GUIDELINE_HIT_RE = (
    JOURNAL_THEME_RE
    + r"|liver cancer|hepatocellular|cholangiocarcin|"
    r"CSCO.*肝|肝癌诊疗|肝細胞癌|肝がん"
)

PREPRINT_THEME_RE = HCC_ANCHOR_RE

# medRxiv / bioRxiv false-friend title patterns (imaging fat fraction, non-HCC liver biology, etc.)
PREPRINT_FP_RE = (
    r"fat fraction|hepatic glucose|microrobot|cerebellar|photoreceptor|"
    r"sea turtle|stereotaxis|microbiota transitions|nicotinam|"
    r"brain-liver|dopamine reward"
)
