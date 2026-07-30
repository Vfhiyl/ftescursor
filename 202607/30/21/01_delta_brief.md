# 增量简报｜2026-07-30 UTC 21h

## 1) 增量计数

| 通道 | 本小时 | vs 20h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **119** | 119 | NEW=0 / DROPPED=0 |
| PubMed PDAT | **40** | 40 | 同窗 |
| 临床向标题子集 | **27** | 30 | 评分边界微差，非新 PMID |
| Crossref 标题过滤去重 | **142** | 125 | NEW DOI=17（无双信源必读） / DROPPED=0 |
| ClinicalTrials 相关 LastUpdate | **15**（focus 15） | 15 / 15 | NEW=0 / DROPPED=0（Phase1 行政闪回已 soft-exclude） |
| OpenAlex（publication_date） | **2** works / **4** preprint(7d) | 2 / 4 | works NEW=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **1**+**4**+**2** | 1+4+2 | 全 SEEN |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。延续：TORCH III 期已入 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)），见 [`../17/`](../17/)。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. Crossref NEW（术式/单信源）：[10.1097/sla.0000000000007166](https://doi.org/10.1097/sla.0000000000007166) — 恶性肝肿瘤右/左六段切除术式（≠疗效终点）
2. Crossref NEW（单中心观察）：[10.3329/jssmc.v17i1.92339](https://doi.org/10.3329/jssmc.v17i1.92339) — 肝切除术前预后营养指数与结局
3. 20h 观察延续：利比亚 HCC 肝肾生物标志物 `10.65405/rg255s55` — 见 [`../20/`](../20/)
4. 19h 观察延续：CT0180 GPC3-TCR I 期（`10.1158/1078-0432.ccr-26-1084`）— 见 [`../19/`](../19/)
5. 18h/17h 观察延续：Deep Response 终点、TORCH、M2BPGi SR/MA — 见 [`../18/`](../18/)、[`../17/`](../17/)

## 4) 已过滤噪音（例）

- Crossref NEW 簇：MASLD 自噬/表观遗传、肝硬化再入院、体外肝支持、PBC 肾受累、RA 肝纤维化、猪模型 histotripsy、ViT-UNet 影像分割、纪念性移植学讣文等 — 均非 HCC 决策级
- Crossref NEW 个案：SBRT 后十二指肠晚反应高压氧（胆管细胞癌背景）— 降权
- CT 原始 API 再现 `NCT06427941`（BGB-B2033 I 期）— 行政闪回，已 soft-exclude；非结果级
- bioRxiv：uveal melanoma / BAP1 + doxycycline 假阳性已剔除

## 5) 相对上一小时一句话

**EDAT 119 完全相同；Crossref 分页补全后多出术式/营养指数等单信源观察项，但试验/预印本/指南/新闻均无实质新增。**

## 6) previous_folder

→ [`202607/30/20`](../20/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官成熟比较（降权）
3. SEEN EPMC：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线
4. SEEN EPMC：[10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 体外细胞毒
5. SEEN medRxiv（降权/非 HCC 决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
