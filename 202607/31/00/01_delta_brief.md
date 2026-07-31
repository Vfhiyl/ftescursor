# 增量简报｜2026-07-31 UTC 00h

## 1) 增量计数

| 通道 | 本小时 | vs 23h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **48** | 124 | **NEW=0** / DROPPED=76（日历窗滚出） |
| PubMed PDAT | **16** | 43 | 同窗下移 |
| 临床向标题子集 | **13** | 27 | 含 TORCH / CT0180 SEEN |
| Crossref 标题过滤去重 | **66** | 139 | NEW DOI=8 / DROPPED≈81（窗滚为主） |
| ClinicalTrials 相关 LastUpdate | **4**（focus 4） | 15 / 15 | NEW=1（BTC III 期行政更新）/ DROPPED=12（窗滚） |
| OpenAlex（publication_date） | **3** works / **6** preprint(7d) | 29 / 6 | OpenAlex-only NEW=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **1**+**3**+**0** | 1+4+1 | 实质 SEEN；EPMC 机器人肝切除出窗 |
| EDAT ID 集与上一小时相同？ | **否** | — | **实质增量：Crossref NEW CMH SR/MA** |

## 2) 本小时必读（≤5）

1. **NEW（Crossref；SR/MA，待 PubMed 对账）**：[doi:10.3350/cmh.2026.0535](https://doi.org/10.3350/cmh.2026.0535) — *Clin Mol Hepatol*：**外照射放疗 vs 局部消融治疗 HCC** 的系统综述与 Meta 分析（created `2026-07-30T23:17Z`，恰在上小时采集之后）。单通道索引 → **不抽取效应量/不改标准**；升权因证据类型为 SR/MA。

无新增双信源 III 期结果。延续：TORCH III 期仍在 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)）。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. SEEN EDAT：CT0180 GPC3-TCR I 期 [PMID 42531433](https://pubmed.ncbi.nlm.nih.gov/42531433/)（不升标准）
2. SEEN Crossref：CCA 全球指南比较 [10.5582/bst.2026.01104](https://doi.org/10.5582/bst.2026.01104)（≠ 面板改版）
3. SEEN Crossref：肝切除后心血管 PAF [10.5582/bst.2026.01126](https://doi.org/10.5582/bst.2026.01126)
4. Crossref 回流观察：肝切除前 PNI [10.3329/jssmc.v17i1.92339](https://doi.org/10.3329/jssmc.v17i1.92339)（21h 已见）
5. CT NEW（行政）：[NCT06622057](https://clinicaltrials.gov/study/NCT06622057) — D07001+卡培他滨，晚期 **BTC** III 期招募中（LastUpdate 2026-07-30）
6. CT SEEN：[NCT07738055](https://clinicaltrials.gov/study/NCT07738055) envafolimab+suvemcitug+HAIC 转化；[NCT04194775](https://clinicaltrials.gov/study/NCT04194775) nofazinlimab
7. SEEN 临床向：ICI 后仑伐替尼 [PMID 42527085](https://pubmed.ncbi.nlm.nih.gov/42527085/)；后上段微创 vs 开放 PSM [PMID 42527069](https://pubmed.ncbi.nlm.nih.gov/42527069/)
8. OpenAlex SEEN works：早期 HCC 病毒感染患病率（IJGII）；余为机制/纳米递送

## 4) 已过滤噪音（例）

- Crossref NEW：肝局限 mCRC 生物制剂转换结局；乳腺癌化疗肝损 nomogram；肝硬化膳食宏量营养素队列；泛癌肝转移前生态位单细胞；MASLD 妇女结直肠癌风险评论；肝硬化腹水脐疝个案
- PubMed EDAT DROPPED×76：主要为 7/29 索引条目滚出 24h 窗，**非撤稿**
- CT DROPPED×12：LastUpdate 滚出窗，focus 试验多半仍在进行
- OncLive 403 / NHC 412 / Minzdrav 不可达；HAS 首页无主题命中

## 5) 相对上一小时一句话

**日历窗使 EDAT/CT 表面收缩且无新 PMID；Crossref 在 23:17Z 新现 CMH「EBRT vs 局部消融」HCC SR/MA，为本小时主增量。**

## 6) previous_folder

→ [`202607/30/23`](../../30/23/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官（降权）
3. SEEN medRxiv（非决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
4. bioRxiv 母鸡肝 atlas（兽医/生理向）— 降权不进必读
5. OpenAlex preprint SEEN×6（Research Square 等）— 默认不进必读
