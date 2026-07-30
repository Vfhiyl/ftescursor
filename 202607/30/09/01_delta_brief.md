# 增量简报｜2026-07-30 UTC 09h

## 1) 增量计数

| 通道 | 本小时 | vs 08h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **93** | 93 | **ID 集相同**（NEW=0 / DROPPED=0） |
| PubMed PDAT | **26** | 26 | 同 |
| 临床向标题子集 | **25** | 22 | 分类波动；无新 PMID |
| Crossref 标题过滤去重 | **91** | 89 | **+5 NEW DOI**（全假阳性/非材料）；DROPPED 3 |
| ClinicalTrials 相关 LastUpdate | **15**（focus 14） | 14 / 14 | NEW 1 黑色素瘤肝转移 NCT（窗缘闪烁）；focus 同 |
| OpenAlex（publication_date） | **2** works / **4** preprint(7d) | 2 / 4 | works NEW DOI=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **2**（EPMC） | 2 | NEW = 0；2 条 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

**无新增必读。**

请继续看最近实质包：
- [`../../29/18/01_delta_brief.md`](../../29/18/01_delta_brief.md) — JLCA 转化定义；BTC CGD→手术；NI±仑伐（PFS≠OS）
- 成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **CT NEW（非材料）** [NCT07281924](https://clinicaltrials.gov/study/NCT07281924) — 黑色素瘤肝转移 Hepzato+Opdualag；08h 滚出后再次重入；**非 HCC**。
2. **NEW Crossref FP** DOI [10.21873/anticanres.18305](https://doi.org/10.21873/anticanres.18305) — RCC pembro+lenvatinib（lenvatinib 查询假阳性；此前多次进出）。
3. **NEW Crossref** DOI [10.1007/s00464-026-13089-6](https://doi.org/10.1007/s00464-026-13089-6) — 良性肝病微创 vs 开腹切除 textbook outcome；非 HCC 终点。
4. 延续观察（UNCHANGED PMID）：[42527085](https://pubmed.ncbi.nlm.nih.gov/42527085/) LEN after DT（DCR/ORR≠OS）；[42527069](https://pubmed.ncbi.nlm.nih.gov/42527069/) MILR PSM；[42527617](https://pubmed.ncbi.nlm.nih.gov/42527617/) Y-90 RS。

## 4) 已过滤噪音（例）

- Crossref EMERALD 查询假阳性：Emerald-spotted Wood-Dove / Swallow-tailed Hummingbird / Emerald Connections Weatherization
- Crossref DROPPED：儿科肝移植家庭心理、肝移植 MDR 感染、SSRN LT 优先排序 DL（窗缘滚出）
- OpenAlex 2 works / 4 preprint 与 08h 相同，无独有新 DOI

## 5) 相对上一小时一句话

**PubMed EDAT ID 集与 08h 完全相同；Crossref +5 全为鸟类/节能/RCC/良性肝病假阳性；CT 黑色素瘤肝转移 NCT 再次闪烁重入；OpenAlex 无新增——无实质增量。**

## 6) previous_folder

→ [`202607/30/08`](../08/)

## 7) 预印本观察（未同行评议）

1. SEEN：DOI [10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 单中心机器人辅助肝切除学习曲线（见 03h）。
2. SEEN：DOI [10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 植物成分体外细胞毒（见 02h）。
3. OpenAlex preprint（7d，UNCHANGED）：lncRNA / 纳米 EGFR / C-GALAD 筛查经济学 / RMTI — 默认降权。
4. medRxiv / bioRxiv details API 近窗主题命中：**0**（见 `raw_preprints.json`）。
