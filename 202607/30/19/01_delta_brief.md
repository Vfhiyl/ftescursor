# 增量简报｜2026-07-30 UTC 19h

## 1) 增量计数

| 通道 | 本小时 | vs 18h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **119** | 119 | NEW=0 / DROPPED=0 |
| PubMed PDAT | **40** | 40 | 同窗 |
| 临床向标题子集 | **26** | 32 | 评分边界微差，非新 PMID |
| Crossref 标题过滤去重 | **126** | 132 | NEW DOI=4（无双信源必读） / DROPPED=10 |
| ClinicalTrials 相关 LastUpdate | **15**（focus 15） | 17 / 16 | DROPPED×2；无 NEW NCT |
| OpenAlex（publication_date） | **4** works / **4** preprint(7d) | 2 / 8 | works NEW DOI=2（降权）；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | 1+**4**+**2** | 0+2+2 | 谱系/类器官 SEEN；+动物/脂肪定量观察 |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。延续：TORCH III 期已入 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)），见 [`../17/`](../17/)。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. Crossref NEW（I 期，单信源）：[10.1158/1078-0432.ccr-26-1084](https://doi.org/10.1158/1078-0432.ccr-26-1084) — GPC3 TCR 融合体 CT0180 晚期 HCC Phase I（未入 EDAT；≠新标准）
2. Crossref NEW（外周）：活体肝移植挽救激素难治慢性肝 GVHD（`10.1111/petr.70415`）
3. Crossref NEW（降权）：芦荟提取物增敏顺铂 / BMP9–CKS1B 乳酸化机制预印本
4. OpenAlex NEW（降权）：VEGFA/EGF 多态与术后结局；大体积 ICC 栅格放疗技术文
5. 18h/17h 观察延续：Deep Response 终点、TORCH、M2BPGi SR/MA — 见 [`../18/`](../18/)、[`../17/`](../17/)

## 4) 已过滤噪音（例）

- ASCO Post durvalumab 关键词 → **Stage III NSCLC** 假阳性
- bioRxiv：brain-liver 葡萄糖调节（神经代谢假阳性）
- CT 行政滑出：`NCT06427941`（BGB-B2033 I 期）、`NCT07285044`（远程照护试点）— 无结果数字级更新
- Crossref DROPPED×10：上小时 MASLD/纤维化/类器官等窗滑动出窗

## 5) 相对上一小时一句话

**EDAT 119 完全相同；Crossref 出现 CT0180 I 期等单信源条目，但不构成双信源必读或指南变更。**

## 6) previous_folder

→ [`202607/30/18`](../18/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官成熟比较（降权）
3. SEEN EPMC：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线
4. SEEN EPMC：[10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 体外细胞毒
5. NEW medRxiv（降权/非 HCC 决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
