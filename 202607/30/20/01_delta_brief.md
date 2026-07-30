# 增量简报｜2026-07-30 UTC 20h

## 1) 增量计数

| 通道 | 本小时 | vs 19h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **119** | 119 | NEW=0 / DROPPED=0 |
| PubMed PDAT | **40** | 40 | 同窗 |
| 临床向标题子集 | **30** | 26 | 评分边界微差，非新 PMID |
| Crossref 标题过滤去重 | **125** | 126 | NEW DOI=1（噪音/观察） / DROPPED=2 |
| ClinicalTrials 相关 LastUpdate | **15**（focus 15） | 15 / 15 | NEW=0 / DROPPED=0 |
| OpenAlex（publication_date） | **2** works / **4** preprint(7d) | 4 / 4 | works NEW=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | 1+**4**+**2** | 1+4+2 | 全 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。延续：TORCH III 期已入 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)），见 [`../17/`](../17/)。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. Crossref NEW（降权）：[10.65405/rg255s55](https://doi.org/10.65405/rg255s55) — 利比亚西北部 HCC 肝肾生物标志物单中心评估（≠疗效/指南信号）
2. 19h 观察延续：CT0180 GPC3-TCR I 期（`10.1158/1078-0432.ccr-26-1084`）— 见 [`../19/`](../19/)
3. 18h/17h 观察延续：Deep Response 终点、TORCH、M2BPGi SR/MA — 见 [`../18/`](../18/)、[`../17/`](../17/)

## 4) 已过滤噪音（例）

- Crossref DROPPED：`10.21873/anticanres.18305`（RCC pembro+LEN 假阳性簇再滑出）
- CT 原始 API 再次出现 `NCT07285044`（远程 CARE 试点）— 行政滑入，已 soft-exclude；非结果级
- OpenAlex works 窗内仅机制/专家会背景条目（相对 19h 无 NEW DOI）

## 5) 相对上一小时一句话

**EDAT 119 完全相同；Crossref 仅多 1 条单中心生物标志物噪音 DOI，试验/预印本/指南均无实质新增。**

## 6) previous_folder

→ [`202607/30/19`](../19/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官成熟比较（降权）
3. SEEN EPMC：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线
4. SEEN EPMC：[10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 体外细胞毒
5. SEEN medRxiv（降权/非 HCC 决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
