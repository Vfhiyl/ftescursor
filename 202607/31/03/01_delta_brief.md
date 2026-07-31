# 增量简报｜2026-07-31 UTC 03h

## 1) 增量计数

| 通道 | 本小时 | vs 02h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **48** | 48 | **NEW=0** / DROPPED=0（ID 集相同） |
| PubMed PDAT | **16** | 16 | 同 |
| 临床向标题子集 | **22** | 14 | 阈值波动；TORCH / CT0180 SEEN |
| Crossref 标题过滤去重 | **57** | 56 | NEW DOI=1（TP53 综述，不升权） |
| ClinicalTrials 相关 LastUpdate | **4**（focus 4） | 4 / 4 | NEW=0 |
| OpenAlex（publication_date） | **4** works / **8** preprint(7d) | 3 / 6 | OpenAlex-only NEW=0；preprint NEW=3（解剖/学习曲线） |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **1**+**3**+**5** | 1+2+2 | NEW=4（多为假阳性/非 HCC 决策） |
| 专业新闻 NEW URL | **0** | 1（ESMO SEEN） | 首页命中延续，无新 URL |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。CMH「EBRT vs 局部消融」SR/MA（[doi:10.3350/cmh.2026.0535](https://doi.org/10.3350/cmh.2026.0535)）仍 **未见 PubMed PMID**，不重复升权。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **NEW（Crossref；单源综述）**：[10.1186/s12935-026-04408-x](https://doi.org/10.1186/s12935-026-04408-x) — TP53 mutation in HCC（Cancer Cell International；机制/叙事综述，不进必读）
2. SEEN Crossref：CMH SR/MA [10.3350/cmh.2026.0535](https://doi.org/10.3350/cmh.2026.0535)（待 PubMed）
3. SEEN Crossref：DLD survival fragility [10.1016/j.dld.2026.07.001](https://doi.org/10.1016/j.dld.2026.07.001)
4. SEEN 新闻：ESMO [TACE combinations still uncertain](https://dailyreporter.esmo.org/esmo-gastrointestinal-cancers-congress-2026/news/the-place-for-tace-combinations-in-hepatocellular-carcinoma-is-still-uncertain)
5. SEEN EDAT：TORCH III 期 [PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / 社论 [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)
6. SEEN EDAT：CT0180 GPC3-TCR I 期 [PMID 42531433](https://pubmed.ncbi.nlm.nih.gov/42531433/)
7. CT SEEN：[NCT06622057](https://clinicaltrials.gov/study/NCT06622057)；[NCT07738055](https://clinicaltrials.gov/study/NCT07738055)；[NCT04194775](https://clinicaltrials.gov/study/NCT04194775)；[NCT07715903](https://clinicaltrials.gov/study/NCT07715903)

## 4) 已过滤噪音（例）

- bioRxiv NEW `10.1101/2025.10.27.684732`：脑–肝葡萄糖环路（小鼠；假阳性）
- EPMC：神经母细胞瘤肝 FNH-like、替戈拉生 HTA、乙肝/丙肝性功能障碍 — 非 HCC 疗效信号
- OpenAlex works NEW 与 PubMed 重叠：脊柱胆管癌转移 SRS（非原发 HCC 决策）
- ASCO Post 超时 / OncLive 403 / NHC 412 / Minzdrav 不可达

## 5) 相对上一小时一句话

**EDAT 48 条 ID 集完全相同；仅 Crossref 新增 1 篇 TP53 综述与若干预印本/解剖观察，无实质临床增量。**

## 6) previous_folder

→ [`202607/31/02`](../02/)

## 7) 预印本观察（未同行评议）

1. **NEW** OpenAlex/RS：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线（单中心）
2. **NEW** OpenAlex/RS：[10.21203/rs.3.rs-10347193/v1](https://doi.org/10.21203/rs.3.rs-10347193/v1) — P6a–RHV 三维解剖/ML（术式观察）
3. **NEW** OpenAlex/RS：[10.21203/rs.3.rs-10169506/v1](https://doi.org/10.21203/rs.3.rs-10169506/v1) — Glissonean 蒂解剖（Laennec）
4. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系
5. SEEN medRxiv（非决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
