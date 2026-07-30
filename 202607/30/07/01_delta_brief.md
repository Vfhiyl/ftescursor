# 增量简报｜2026-07-30 UTC 07h

## 1) 增量计数

| 通道 | 本小时 | vs 06h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **93** | 93 | **ID 集相同**（NEW=0 / DROPPED=0） |
| PubMed PDAT | **26** | 26 | 同 |
| 临床向标题子集 | **24** | 24 | 同；无新 PMID |
| Crossref 标题过滤去重 | **84** | 83 | **+2 NEW DOI**（非材料）；DROPPED 1 |
| ClinicalTrials 相关 LastUpdate | **15**（focus 14） | 14 / 14 | **+1 NEW NCT**（黑色素瘤肝转移 FP 重入） |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **2**（EPMC） | 2 | NEW = 0；2 条 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

**无新增必读。**

请继续看最近实质包：
- [`../../29/18/01_delta_brief.md`](../../29/18/01_delta_brief.md) — JLCA 转化定义；BTC CGD→手术；NI±仑伐（PFS≠OS）
- 成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **NEW Crossref** DOI [10.36283/ziun-pjmd/013](https://doi.org/10.36283/ziun-pjmd/013) — 初诊即晚期 HCC 临床特征/病因描述性单刊；无终点、无双信源，降权。
2. **NEW Crossref** DOI [10.1016/j.bbrc.2026.154370](https://doi.org/10.1016/j.bbrc.2026.154370) — SERBP1 启动子 SNP rs3762314 易感/表型；遗传生物标志，降权。
3. **NEW CT** [NCT07281924](https://clinicaltrials.gov/study/NCT07281924) — 黑色素瘤肝转移 Hepzato+Opdualag（01h 曾 DROPPED）；窗缘重入，**非 HCC**，无 results 模块。
4. 延续观察（UNCHANGED PMID）：[42527085](https://pubmed.ncbi.nlm.nih.gov/42527085/) LEN after DT（DCR/ORR≠OS）；[42527069](https://pubmed.ncbi.nlm.nih.gov/42527069/) MILR PSM；[42527617](https://pubmed.ncbi.nlm.nih.gov/42527617/) Y-90 RS。

## 4) 已过滤噪音（例）

- Crossref DROPPED：DCTPP1 liver-cancer target 综述（`10.3390/cimb48080770`）滚出过滤集
- SNP / 描述性流行病学仅登记，不写疗效结论
- CT 黑色素瘤肝转移重入不计入 focus 实质更新

## 5) 相对上一小时一句话

**PubMed EDAT ID 集与 06h 完全相同；Crossref +2 非材料 DOI（描述性晚期 HCC / SERBP1 SNP）；CT +1 黑色素瘤肝转移 NCT 重入；预印本/指南/新闻无实质变化——无实质增量。**

## 6) previous_folder

→ [`202607/30/06`](../06/)

## 7) 预印本观察（未同行评议）

1. SEEN：DOI [10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 单中心机器人辅助肝切除学习曲线（见 03h）。
2. SEEN：DOI [10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 植物成分体外细胞毒（见 02h）。
3. medRxiv / bioRxiv details API 近窗主题命中：**0**（见 `raw_preprints.json`）。
