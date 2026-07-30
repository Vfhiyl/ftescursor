# 增量简报｜2026-07-30 UTC 08h

## 1) 增量计数

| 通道 | 本小时 | vs 07h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **93** | 93 | **ID 集相同**（NEW=0 / DROPPED=0） |
| PubMed PDAT | **26** | 26 | 同 |
| 临床向标题子集 | **22** | 24 | 分类波动；无新 PMID |
| Crossref 标题过滤去重 | **89** | 84 | **+5 NEW DOI**（非材料）；DROPPED 0 |
| ClinicalTrials 相关 LastUpdate | **14**（focus 14） | 15 / 14 | DROPPED 1 黑色素瘤肝转移 NCT；NEW=0 |
| OpenAlex（publication_date） | **2** works / **4** preprint(7d) | —（首启对照） | works NEW DOI=0（与 PM/CR 重合）；preprint NEW=4（降权） |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **2**（EPMC） | 2 | NEW = 0；2 条 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

**无新增必读。**

请继续看最近实质包：
- [`../../29/18/01_delta_brief.md`](../../29/18/01_delta_brief.md) — JLCA 转化定义；BTC CGD→手术；NI±仑伐（PFS≠OS）
- 成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **NEW Crossref** DOI [10.21037/tcr-2026-1-0342](https://doi.org/10.21037/tcr-2026-1-0342) — 不可切除 HCC：ICI+靶向 vs TKI 单药肝毒性；单刊、无双信源，安全信号观察，不升必读。
2. **NEW Crossref** DOI [10.1080/14728222.2026.2708824](https://doi.org/10.1080/14728222.2026.2708824) — 慢性肝病/HCC T 细胞功能障碍空间免疫框架；机制向。
3. **NEW Crossref** DOI [10.21037/tcr-2026-0745](https://doi.org/10.21037/tcr-2026-0745) / [10.21037/tcr-2026-0825](https://doi.org/10.21037/tcr-2026-0825) — 棕榈酰化基因签名 / HOXD9 预后分层；生物信息学降权。
4. **CT DROPPED** [NCT07281924](https://clinicaltrials.gov/study/NCT07281924) — 黑色素瘤肝转移（07h 重入后再次滚出）；**非 HCC**，窗缘闪烁。
5. 延续观察（UNCHANGED PMID）：[42527085](https://pubmed.ncbi.nlm.nih.gov/42527085/) LEN after DT（DCR/ORR≠OS）；[42527069](https://pubmed.ncbi.nlm.nih.gov/42527069/) MILR PSM；[42527617](https://pubmed.ncbi.nlm.nih.gov/42527617/) Y-90 RS。

## 4) 已过滤噪音（例）

- Crossref NEW erratum：TCR 文献计量勘误 `10.21037/tcr-20262-7`（不写结论）
- OpenAlex 2 works 均已与 PubMed/Crossref 去重，不重复升权
- OpenAlex 7d preprint：lncRNA 免疫监测、纳米递送、筛查卫生经济学、RMTI 分级层 — 默认降权

## 5) 相对上一小时一句话

**PubMed EDAT ID 集与 07h 完全相同；Crossref +5 非材料 DOI（机制/生物信息/单刊肝毒性/勘误）；CT 滚出黑色素瘤肝转移 NCT；OpenAlex 无独有新 DOI——无实质增量。**

## 6) previous_folder

→ [`202607/30/07`](../07/)

## 7) 预印本观察（未同行评议）

1. SEEN：DOI [10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 单中心机器人辅助肝切除学习曲线（见 03h）。
2. SEEN：DOI [10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 植物成分体外细胞毒（见 02h）。
3. OpenAlex preprint（7d，未进必读）：[10.21203/rs.3.rs-10483008/v1](https://doi.org/10.21203/rs.3.rs-10483008/v1) lncRNA 免疫监测；[10.21203/rs.3.rs-10334645/v1](https://doi.org/10.21203/rs.3.rs-10334645/v1) 纳米 EGFR；[10.21203/rs.3.rs-9874676/v1](https://doi.org/10.21203/rs.3.rs-9874676/v1) C-GALAD 筛查经济学；[10.21203/rs.3.rs-10501583/v1](https://doi.org/10.21203/rs.3.rs-10501583/v1) RMTI 分诊层。
4. medRxiv / bioRxiv details API 近窗主题命中：**0**（见 `raw_preprints.json`）。
