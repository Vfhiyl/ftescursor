# 增量简报｜2026-07-31 UTC 01h

## 1) 增量计数

| 通道 | 本小时 | vs 00h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **48** | 48 | **NEW=0** / DROPPED=0（ID 集相同） |
| PubMed PDAT | **16** | 16 | 同 |
| 临床向标题子集 | **16** | 13 | 阈值波动；TORCH / CT0180 SEEN |
| Crossref 标题过滤去重 | **59** | 66 | NEW DOI=1（观察级）/ DROPPED≈8（集合抖动） |
| ClinicalTrials 相关 LastUpdate | **4**（focus 4） | 4 / 4 | NEW=0 |
| OpenAlex（publication_date） | **3** works / **6** preprint(7d) | 3 / 6 | OpenAlex-only NEW=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **1**+**3**+**0** | 1+3+0 | 实质 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。上一小时 Crossref NEW 的 CMH「EBRT vs 局部消融」SR/MA（[doi:10.3350/cmh.2026.0535](https://doi.org/10.3350/cmh.2026.0535)）仍 **未见 PubMed PMID**，不重复升权。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **NEW（Crossref；单源评论，不升必读）**：[doi:10.1016/j.dld.2026.07.001](https://doi.org/10.1016/j.dld.2026.07.001) — *Dig Liver Dis*：晚期 HCC 免疫治疗试验的 **survival fragility** 需结合临床语境解读（created `2026-07-30T23:58:57Z`）
2. SEEN Crossref：CMH SR/MA EBRT vs 局部消融 [10.3350/cmh.2026.0535](https://doi.org/10.3350/cmh.2026.0535)（待 PubMed）
3. SEEN EDAT：TORCH III 期 [PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / 社论 [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)
4. SEEN EDAT：CT0180 GPC3-TCR I 期 [PMID 42531433](https://pubmed.ncbi.nlm.nih.gov/42531433/)（不升标准）
5. SEEN Crossref：CCA 全球指南比较 [10.5582/bst.2026.01104](https://doi.org/10.5582/bst.2026.01104)（≠ 面板改版）
6. CT SEEN：[NCT06622057](https://clinicaltrials.gov/study/NCT06622057) BTC III 期；[NCT07738055](https://clinicaltrials.gov/study/NCT07738055) HAIC 转化；[NCT04194775](https://clinicaltrials.gov/study/NCT04194775) nofazinlimab；[NCT07715903](https://clinicaltrials.gov/study/NCT07715903) carfilzomib HAI

## 4) 已过滤噪音（例）

- Crossref DROPPED×8：多为相对上小时集合抖动（CRC 肝局限、乳腺癌 CILI、脐疝腹水等噪音出窗），非撤稿
- 预印本 hen-liver atlas：兽医/生理向 — 降权
- OncLive 403 / NHC 412 / がんナビ 500 / Minzdrav 不可达

## 5) 相对上一小时一句话

**EDAT 48 条 ID 集完全相同；仅 Crossref 新现 1 篇 DLD「survival fragility」评论（观察级），无实质临床增量。**

## 6) previous_folder

→ [`202607/31/00`](../00/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官（降权）
3. SEEN medRxiv（非决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
4. bioRxiv 母鸡肝 atlas — 降权不进必读
5. OpenAlex preprint SEEN×6 — 默认不进必读
